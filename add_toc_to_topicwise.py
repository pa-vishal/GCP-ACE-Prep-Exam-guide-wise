#!/usr/bin/env python3
"""
Add StackEdit-style TOC to Topic-wise HTML pages that have StackEdit layout
but are missing the left TOC column (stackedit__left).
"""
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TOPIC_WISE = ROOT / "Topic-wise"


def slugify(text: str) -> str:
    t = text.strip().lower()
    t = re.sub(r"\s+", "-", t)
    t = re.sub(r"[^\w\-.]", "", t)
    return t or "section"


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).strip()


def extract_headings(html_content: str) -> list[tuple[int, str, str]]:
    """Return list of (level, id, label) for h1-h6 that have id or we can add one."""
    headings = []
    # Match <hN ... id="..." ...>content</hN> or <hN>content</hN>
    pattern = re.compile(
        r'<h([1-6])([^>]*)>(.*?)</h\1>',
        re.DOTALL | re.IGNORECASE
    )
    for m in pattern.finditer(html_content):
        level = int(m.group(1))
        attrs = m.group(2)
        inner = m.group(3)
        id_match = re.search(r'\bid=["\']([^"\']+)["\']', attrs)
        id_val = id_match.group(1) if id_match else slugify(strip_html(inner))
        label = strip_html(inner) or id_val
        label = html.unescape(label)
        headings.append((level, id_val, label))
    return headings


def build_toc_html(headings: list[tuple[int, str, str]]) -> str:
    """StackEdit-style TOC: ul > li > ul > li (empty) + li > a for each."""
    if not headings:
        return '\n<ul>\n<li></li>\n</ul>\n'
    items = []
    for _lev, id_, label in headings:
        label_esc = html.escape(label)
        items.append(f'<li><a href="#{id_}">{label_esc}</a></li>')
    inner = "\n".join(items)
    return f"\n<ul>\n<li>\n<ul>\n<li></li>\n{inner}\n</ul>\n</li>\n</ul>\n"


def add_ids_to_headings(html_content: str) -> str:
    """Ensure every h1-h6 has an id attribute."""
    def repl(m):
        full = m.group(0)
        if re.search(r'\bid=', m.group(2)):
            return full
        level = m.group(1)
        attrs = m.group(2)
        inner = m.group(3)
        id_val = slugify(strip_html(inner))
        return f'<h{level}{attrs} id="{id_val}">{inner}</h{level}>'
    return re.sub(
        r'<h([1-6])([^>]*)>(.*?)</h\1>',
        repl,
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )


def process_file(path: Path) -> bool:
    """Add TOC to file if it has StackEdit but no stackedit__left. Return True if modified."""
    content = path.read_text(encoding="utf-8", errors="replace")
    if "stackedit__left" in content or "stackedit__toc" in content:
        return False  # already has TOC
    if 'class="stackedit"' not in content and "stackedit.io/style.css" not in content:
        return False  # not StackEdit style
    if 'stackedit__html' not in content:
        return False

    body_match = re.search(r'<body[^>]*>(.*)</body>', content, re.DOTALL | re.IGNORECASE)
    if not body_match:
        return False
    body_inner = body_match.group(1).strip()

    toc_div_match = re.search(
        r'<div\s+class="stackedit__html"[^>]*>(.*)',
        body_inner,
        re.DOTALL
    )
    if not toc_div_match:
        return False
    main_content = toc_div_match.group(1)
    # Find closing </div> for the first stackedit__html
    depth = 1
    i = 0
    while i < len(main_content):
        if main_content[i:i+4] == "<div":
            depth += 1
            j = main_content.find(">", i)
            i = (j + 1) if j != -1 else (i + 1)
        elif main_content[i:i+6] == "</div>":
            depth -= 1
            if depth == 0:
                main_content = main_content[:i]
                break
            i += 6
        else:
            i += 1

    main_content = add_ids_to_headings(main_content)
    headings = extract_headings(main_content)

    if not headings:
        main_content = '<div id="content">' + main_content + '</div>'
        title = path.stem.replace("-", " ").replace("_", " ")
        toc_html = build_toc_html([(1, "content", title)])
    else:
        toc_html = build_toc_html(headings)

    new_body_inner = f'''  <div class="stackedit__left">
    <div class="stackedit__toc">
      {toc_html}
    </div>
  </div>
  <div class="stackedit__right">
    <div class="stackedit__html">
{main_content}
    </div>
  </div>'''

    old_body = re.search(r'<body[^>]*>.*</body>', content, re.DOTALL | re.IGNORECASE)
    if not old_body:
        return False
    new_body = '<body class="stackedit">\n' + new_body_inner + '\n</body>'
    new_content = content.replace(old_body.group(0), new_body)
    if new_content == content:
        return False
    path.write_text(new_content, encoding="utf-8")
    return True


def main():
    modified = []
    for path in sorted(TOPIC_WISE.rglob("*.html")):
        if path.name.lower() == "index.html" and path.parent == TOPIC_WISE:
            continue
        try:
            if process_file(path):
                modified.append(path.relative_to(ROOT))
        except Exception as e:
            print(f"Error {path}: {e}")
    for p in modified:
        print("Added TOC:", p)
    print("Done." if modified else "No files needed TOC.")


if __name__ == "__main__":
    main()
