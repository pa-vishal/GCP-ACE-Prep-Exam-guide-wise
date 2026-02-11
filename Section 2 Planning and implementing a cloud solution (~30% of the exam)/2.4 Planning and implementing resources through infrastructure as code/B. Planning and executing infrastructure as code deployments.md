### **Section 2.4 – Planning and executing infrastructure as code (IaC) deployments**

*(versioning, state management, updates)*

![Image](https://cdn.prod.website-files.com/644656ba41efb6b601e93ca6/666ca94313bc92617e6eb9fa_AD_4nXe-5_WQu-YNEB3tjjsejMPFliYTzRNjfX5D4sBknnJ9T-25KaQ1UAv3JsxDelee3icN2knxbdR7O6Upx--gqbvpij3hpWqgifxPez8_0ZtHflV45C1BsL3Wzs_tSLjn7WhK9JoiuY6EAd3gAtPfFU3-HaJ-.png)

![Image](https://f.hubspotusercontent10.net/hubfs/6897318/Blog/Infrastructure-as-code-scheme.png)

![Image](https://www.researchgate.net/publication/385642360/figure/fig3/AS%3A11431281289184829%401731051358040/GitOps-workflow-Kamath-et-al-2023-Three-Components-of-GitOps-Workflows-Infrastructure.jpg)

This bullet is about **how IaC is operated safely over time**, not how to write templates. The ACE exam checks whether you understand **why versioning and state exist, what can go wrong, and how updates are applied without breaking environments**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **why IaC must be versioned**
* Understand **what state is and why it matters**
* Recognize **safe vs unsafe update patterns**
* Avoid manual changes that cause drift

> **Exam mindset:**
> *“How do teams safely change infrastructure repeatedly?”*

---

## 2️⃣ Versioning IaC (exam framing)

### What versioning means

* Store IaC code in **version control** (Git)
* Track:

  * What changed
  * When
  * Why
* Enables:

  * Rollbacks
  * Audits
  * Collaboration

### Exam signals

* “Track changes”
* “Rollback”
* “Multiple environments”
* “Collaboration”

> **ACE rule:**
> IaC without version control defeats the purpose.

---

## 3️⃣ State management (VERY exam-relevant)

### What “state” is

* A record of:

  * Resources that exist
  * Their current configuration
* Used to:

  * Detect drift
  * Calculate updates

### Terraform example (conceptual)

* `.tfstate` file tracks real resources
* Compared against desired config

---

### Local vs remote state (exam-level)

| State type   | Use when                    |
| ------------ | --------------------------- |
| Local state  | Solo developer, experiments |
| Remote state | Teams, CI/CD                |

**Common remote backends**

* Cloud Storage
* Terraform Cloud

> **Exam trap:**
> Multiple people using local state → conflicts & corruption

---

## 4️⃣ Updates & lifecycle (EXAM FAVORITE)

### How updates work

1. Change IaC code
2. Plan (preview changes)
3. Apply changes safely

### Terraform commands (recognition-level)

```bash
terraform plan
terraform apply
```

> **Exam note:**
> You’re tested on **the concept of planning before applying**, not command syntax.

---

### Safe updates

* Incremental
* Predictable
* Reviewed via plan output

### Unsafe updates (exam traps)

❌ Manual changes in Console
❌ Editing live resources directly
❌ Ignoring plan output

---

## 5️⃣ Drift detection (important concept)

### What drift is

* Real infrastructure ≠ IaC definition

### Causes

* Manual console edits
* Emergency fixes outside IaC

### Why it’s bad

* Next apply may:

  * Undo changes
  * Destroy resources

> **Exam signal:**
> “Unexpected changes after apply” → drift

---

## 6️⃣ Rollbacks & recovery (exam awareness)

* Rollbacks are done by:

  * Reverting IaC code
  * Reapplying
* Not by editing resources manually

> **ACE principle:**
> **Infrastructure changes flow from code → cloud**, never the reverse.

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “Multiple engineers deploying infrastructure safely”

✅ **Remote state + version control**

---

### Scenario 2

> “Need to preview changes before deployment”

✅ **Plan step**

---

### Scenario 3

> “Infrastructure behaves unexpectedly after manual change”

✅ **State drift**

---

## 8️⃣ Decision table (MEMORIZE)

| Requirement        | Best Practice     |
| ------------------ | ----------------- |
| Team collaboration | Remote state      |
| Change visibility  | Version control   |
| Safe updates       | Plan before apply |
| Avoid drift        | No manual changes |

---

## 9️⃣ Common ACE exam traps

❌ Manual edits outside IaC
❌ Sharing local state files
❌ Skipping plan step
❌ Treating IaC as one-time setup

---

## 🔑 One-line ACE memory hooks

* **Code is the source of truth**
* **State tracks reality**
* **Plan before apply**
* **Manual changes cause drift**

--- 
