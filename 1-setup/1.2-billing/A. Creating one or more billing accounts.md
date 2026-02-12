
### **Section 1.2 – Creating one or more billing accounts**

![Image](https://docs.cloud.google.com/static/billing/docs/images/resource-hierarchy-overview.png)

![Image](https://docs.cloud.google.com/static/billing/docs/images/access-control-org.png)

This bullet is about **financial ownership and separation**, not spending optimization yet. The ACE exam uses billing accounts to test whether you understand **who pays**, **who controls billing**, and **how projects are isolated financially**.

---

## 1️⃣ What a billing account is (exam framing)

A **billing account** is:

* A container for **payment methods**
* The **financial owner** of cloud usage
* Linked to one or more **projects**

> **Key rule**
> **Resources don’t incur cost unless their project is linked to a billing account**

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you can:

### ✅ Understand why you might need **multiple billing accounts**

### ✅ Know the **relationship between billing accounts and projects**

### ✅ Identify **who can create and manage billing accounts**

### ❌ What it does NOT test

* Tax setup
* Invoices and payments
* Detailed cost optimization (that comes later)

---

## 3️⃣ Who can create billing accounts

To create a billing account, you must:

* Be a **billing administrator** (or equivalent)
* Have a valid **payment method**
* Be associated with:

  * A Google Cloud Organization **or**
  * A standalone (no-domain) setup

> **Exam trap**
> Project Owner ≠ Billing Account Creator (not always)

---

## 4️⃣ Why create MORE than one billing account (exam-favorite)

### Common valid reasons

#### 🧱 1. Cost isolation

* Separate:

  * Dev vs Prod
  * Different departments
  * Different customers

> “Ensure prod costs are not affected by dev experiments”
> ✅ Use separate billing accounts

---

#### 🧾 2. Different payment methods

* Different credit cards
* Different legal entities

---

#### 🔐 3. Different billing admins

* Finance team controls prod billing
* Engineering controls dev billing

---

#### 📊 4. Budget & reporting boundaries

* Budgets are defined **per billing account**
* Clean financial reporting

---

## 5️⃣ Billing account ↔ project relationship (very important)

* A **project can be linked to only ONE billing account**
* A billing account can be linked to **MANY projects**
* Projects can be **moved** between billing accounts

```
Billing Account A
 ├── Project 1
 ├── Project 2

Billing Account B
 └── Project 3
```

---

## 6️⃣ Creating a billing account (conceptual steps)

The ACE exam expects **conceptual knowledge**, not UI memorization.

High-level flow:

1. Go to **Billing**
2. Create new billing account
3. Add payment method
4. Assign billing administrators

---

## 7️⃣ CLI interaction with billing accounts (exam-aware)

### 🔹 List billing accounts you have access to

```bash
gcloud billing accounts list
```

---

### 🔹 Describe a billing account

```bash
gcloud billing accounts describe BILLING_ACCOUNT_ID
```

---

### 🔹 Important limitation (exam trap)

❌ You **cannot** create billing accounts via `gcloud`

> Billing account creation is **console-driven**

---

## 8️⃣ IAM & billing accounts (high-level)

Billing accounts have their **own IAM roles**, separate from projects:

| Role                  | Purpose       |
| --------------------- | ------------- |
| Billing Account Admin | Full control  |
| Billing Account User  | Link projects |
| Billing Viewer        | View costs    |

> **Exam clue**
> If someone needs to link projects → **Billing Account User**

---

## 9️⃣ Real exam-style scenarios

### Scenario 1

> “A company wants separate invoices for prod and dev”

✅ Correct:

* Create **two billing accounts**
* Link projects accordingly

---

### Scenario 2

> “A new project is created but resources fail to start”

✅ Root cause:

* Project not linked to a billing account

---

### Scenario 3

> “Finance team must manage payments, not engineers”

✅ Correct:

* Assign billing IAM roles
* Separate billing account ownership

---

## 10️⃣ Common exam traps

❌ Assume one billing account per organization
❌ Assume projects auto-bill without linkage
❌ Confuse project IAM with billing IAM
❌ Think budgets stop spending (they don’t)

---

## 🔑 One-line exam memory hook

> **Billing account = who pays**
> **Project = what spends**

--- 
