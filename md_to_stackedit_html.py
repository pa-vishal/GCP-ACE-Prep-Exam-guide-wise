#!/usr/bin/env python3
"""
Convert all .md files to StackEdit-themed HTML (one HTML per MD).
Uses same structure and https://stackedit.io/style.css as the reference.
"""
import re
import html
import sys
from pathlib import Path

def _long_path(p: Path) -> Path:
    """On Windows, use long path prefix to avoid MAX_PATH (260) errors."""
    p = p.resolve()
    s = str(p)
    if sys.platform == "win32" and len(s) > 200 and not s.startswith("\\\\?\\"):
        return Path("\\\\?\\" + s)
    return p

try:
    import markdown
except ImportError:
    print("Run: pip install markdown")
    raise SystemExit(1)

STACKEDIT_CSS = "https://stackedit.io/style.css"
ROOT = Path(__file__).resolve().parent


def slugify(text: str, _separator: str = "-") -> str:
    """Create URL-safe id from heading text (StackEdit-style). TocExtension passes (value, separator)."""
    t = text.strip().lower()
    t = re.sub(r"\s+", _separator, t)
    t = re.sub(r"[^\w\-.]", "", t)  # keep alphanumeric, dash, underscore, period
    return t or "section"


def build_toc_html(toc_tokens: list) -> str:
    """Build StackEdit-style TOC: ul > li > ul > li > a."""
    if not toc_tokens:
        return "\n<ul>\n<li></li>\n</ul>\n"
    items = []
    for token in toc_tokens:
        name = token.get("name", "").strip()
        name = html.unescape(name)  # avoid double-escape (e.g. &amp; -> &)
        id_ = token.get("id", slugify(name))
        name_esc = html.escape(name)
        items.append(f'<li><a href="#{id_}">{name_esc}</a></li>')
    inner = "\n".join(items)
    return f"\n<ul>\n<li>\n<ul>\n<li></li>\n{inner}\n</ul>\n</li>\n</ul>\n"


def md_to_stackedit_html(md_path: Path) -> None:
    """Convert one .md file to StackEdit-style HTML beside it."""
    content = md_path.read_text(encoding="utf-8", errors="replace")
    title = md_path.stem

    md_engine = markdown.Markdown(
        extensions=[
            "toc",
            "fenced_code",
            "tables",
            "nl2br",
            "sane_lists",
        ],
        extension_configs={
            "toc": {
                "title": "",
                "toc_depth": "2-6",
                "slugify": slugify,
                "permalink": False,
            }
        },
    )
    body_html = md_engine.convert(content)
    toc_tokens = getattr(md_engine, "toc_tokens", [])
    toc_html = build_toc_html(toc_tokens)

    title_esc = html.escape(title)
    html_content = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_esc}</title>
  <link rel="stylesheet" href="{STACKEDIT_CSS}" />
</head>

<body class="stackedit">
  <div class="stackedit__left">
    <div class="stackedit__toc">
      {toc_html}
    </div>
  </div>
  <div class="stackedit__right">
    <div class="stackedit__html">
      {body_html}
    </div>
  </div>
</body>

</html>
"""
    out_path = md_path.with_suffix(".html")
    write_path = _long_path(out_path)
    write_path.write_text(html_content, encoding="utf-8")
    try:
        print(out_path.relative_to(ROOT))
    except ValueError:
        print(out_path)


def main():
    for md_path in sorted(ROOT.rglob("*.md")):
        if md_path.name.startswith("."):
            continue
        if md_path.name.lower() == "index.md":
            continue
        md_path = _long_path(md_path)
        if not md_path.is_file():
            print(f"Skip (not found): {md_path}", flush=True)
            continue
        try:
            md_to_stackedit_html(md_path)
        except Exception as e:
            print(f"Error {md_path}: {e}", flush=True)
    print("Done.")


if __name__ == "__main__":
    main()
