### **Section 1.2 – Setting up billing exports**

![Image](https://docs.cloud.google.com/static/billing/docs/images/resource-hierarchy-overview.png)

![Image](https://developer.harness.io/assets/images/gcp-smp-arch-91cc36f55eb5d2536bd96d28e076c888.png)

This bullet is about **cost visibility and analysis**, not cost control. On the ACE exam, billing exports test whether you know **where billing data goes**, **why you export it**, and **which export to choose**.

---

## 1️⃣ What billing exports are (exam framing)

**Billing exports** automatically send **detailed cost and usage data** from a **billing account** to:

* **BigQuery** (for analysis & reporting)
* **Cloud Storage** (for archival)

> **Hard rule (memorize)**
> Billing exports are **read-only data pipelines**. They **do not affect charges**.

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you can:

### ✅ Choose **BigQuery vs Cloud Storage** exports

### ✅ Know billing exports are configured at the **billing account level**

### ✅ Understand **use cases** (analysis vs archival)

### ❌ What it does NOT test

* Writing complex BigQuery SQL
* Schema memorization
* Custom ETL pipelines

---

## 3️⃣ Types of billing exports (VERY exam-relevant)

### 📊 A. BigQuery billing export (MOST tested)

Exports:

* Detailed line items
* Usage by project, service, SKU
* Labels, credits, discounts

**Use when**

* Analyzing costs
* Building dashboards
* Chargeback / showback
* Forecasting

> **Exam signal**
> “Analyze”, “report”, “break down costs” → **BigQuery export**

---

### 🗄️ B. Cloud Storage billing export

Exports:

* CSV/JSON files
* Periodic snapshots

**Use when**

* Archival
* External processing
* Compliance retention

> Less flexible than BigQuery

---

## 4️⃣ Where billing exports are configured

Billing exports are set up:

* **On the billing account**
* Not per project
* Apply to **all linked projects**

> **Exam trap**
> You cannot configure billing exports at project level.

---

## 5️⃣ Setting up a BigQuery billing export (conceptual)

Exam-level flow:

1. Go to **Billing**
2. Select **Billing account**
3. Enable **BigQuery export**
4. Choose:

   * BigQuery project
   * Dataset
5. Export starts automatically

> No resource restarts required.

---

## 6️⃣ Permissions needed (exam awareness)

To configure exports, you need:

* **Billing Account Admin** (or equivalent)
* BigQuery dataset permissions

> Project Owner alone is **not sufficient**.

---

## 7️⃣ CLI considerations (exam reality)

❌ Billing export setup is **not typically done via `gcloud`**
✅ ACE expects **conceptual understanding**, not commands

(Exports are managed via Console or Billing APIs.)

---

## 8️⃣ Real exam-style scenarios

### Scenario 1

> “Finance wants a detailed cost breakdown by project and service”

✅ Correct:

* Enable **BigQuery billing export**

---

### Scenario 2

> “Company needs long-term raw billing records for compliance”

✅ Correct:

* Export to **Cloud Storage**

---

### Scenario 3

> “Build dashboards showing daily spend trends”

✅ Correct:

* BigQuery billing export
* Use BI tools on top

---

## 9️⃣ Billing exports vs budgets vs quotas (EXAM GOLD)

| Tool           | Purpose            |
| -------------- | ------------------ |
| Billing export | Cost data analysis |
| Budget         | Alerts             |
| Quota          | Hard usage limit   |
| Org Policy     | Restriction        |

> **Billing export = visibility, not control**

---

## 10️⃣ Common exam traps

❌ Think exports reduce cost
❌ Think exports stop spending
❌ Configure at project instead of billing account
❌ Confuse exports with budgets

---

## 🔑 One-line exam memory hook

> **Exports show where money went — not how to stop it**

---

