### **Section 1.2 – Linking projects to a billing account**

![Image](https://docs.cloud.google.com/static/billing/docs/images/access-control-org.png)

![Image](https://docs.cloud.google.com/static/billing/docs/images/subaccounts.png)

This bullet is **one of the highest-yield ACE topics**. Many scenario questions quietly depend on whether you recognize that **projects must be explicitly linked to a billing account** before most resources can run.

---

## 1️⃣ What “linking a project to a billing account” means

Linking means:

* Assigning **one billing account** to **one project**
* Allowing that project to **incur charges**
* Enabling creation of **billable resources**

> **Hard rule (memorize)**
> A project with **no billing account = mostly unusable**

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you can:

### ✅ Identify when a project is **not billed**

### ✅ Know that **billing is per project**, not per org/folder

### ✅ Understand **who is allowed** to link projects

### ✅ Choose linking vs creating a new billing account

### ❌ What it does NOT test

* Invoices
* Taxes
* Credits handling
* Cost optimization (later bullets)

---

## 3️⃣ Billing account ↔ project relationship (EXAM CORE)

| Rule                                         | True / False |
| -------------------------------------------- | ------------ |
| A project can have multiple billing accounts | ❌ False      |
| A billing account can have many projects     | ✅ True       |
| Billing auto-links on project creation       | ❌ False      |
| Billing can be changed later                 | ✅ True       |

---

## 4️⃣ Who can link a project to a billing account

To link a project, you need:

* **Billing Account User** (or Admin) on the billing account
* **Project Owner** (or equivalent) on the project

> **Exam trap**
> Project Owner alone is **not sufficient** without billing permission.

---

## 5️⃣ Linking a project via CLI (VERY exam-relevant)

### 🔹 Link a project to a billing account

```bash
gcloud billing projects link my-project \
  --billing-account=000000-AAAAAA-BBBBBB
```

---

### 🔹 Verify billing linkage

```bash
gcloud billing projects describe my-project
```

Look for:

```text
billingEnabled: true
billingAccountName: billingAccounts/000000-AAAAAA-BBBBBB
```

---

### 🔹 Unlink a project (exam awareness)

```bash
gcloud billing projects unlink my-project
```

> ⚠️ Unlinking **stops billable resources** from working

---

## 6️⃣ Linking via Console (conceptual)

Exam-level understanding:

1. Go to **Billing**
2. Select billing account
3. Link project

You won’t be tested on UI steps — only **outcomes**.

---

## 7️⃣ What happens if a project is NOT linked (exam favorites)

### 🚫 You cannot:

* Create VMs
* Deploy GKE clusters
* Use Cloud Run
* Create load balancers
* Use Cloud SQL

### ✅ You *can*:

* View project
* Enable APIs
* Assign IAM roles
* Create some free-tier resources (limited)

> **Exam phrase**
> “Resources fail immediately after project creation” → **Billing**

---

## 8️⃣ Moving projects between billing accounts (exam logic)

You can:

* Unlink from Billing A
* Link to Billing B

Use cases:

* Separate dev/prod costs
* Change ownership
* Migrate between teams

> **Important**
> Resources remain, but **new usage bills to the new account**

---

## 9️⃣ Real exam-style scenarios

### Scenario 1

> “A project exists, APIs enabled, IAM correct, but deployments fail”

✅ Root cause:

* Project not linked to billing account

---

### Scenario 2

> “Finance wants prod charges on a different invoice”

✅ Action:

* Link prod project to a different billing account

---

### Scenario 3

> “CI/CD pipeline fails on first run”

✅ Root cause:

* Missing billing linkage

---

## 10️⃣ Common exam traps

❌ Assume billing auto-links
❌ Confuse billing IAM with project IAM
❌ Think budgets enforce limits
❌ Assume billing account = organization

---

## 🔑 One-line exam memory hook

> **No billing link → no real resources**

---
 
