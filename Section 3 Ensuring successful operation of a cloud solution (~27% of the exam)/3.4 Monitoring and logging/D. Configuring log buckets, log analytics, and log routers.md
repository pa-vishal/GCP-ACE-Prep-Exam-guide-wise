### **Section 3.4 – Monitoring and logging**

#### **Configuring log buckets, log analytics, and log routers**

This bullet is about **how logs are stored, routed, retained, and analyzed inside Google Cloud**. The ACE exam checks whether you understand the **internal flow of logs**, not deep SIEM design.

---

# 1️⃣ Big Picture: How Logs Flow in GCP

```
Resources → Cloud Logging API → Log Router → Log Buckets → Analysis / Export
```

There are **three key components** here:

| Component     | Role                          |
| ------------- | ----------------------------- |
| Log Router    | Decides where logs go         |
| Log Bucket    | Stores logs                   |
| Log Analytics | Lets you query logs using SQL |

> **ACE rule:**
> Logs always pass through the **Log Router** first.

---

# 2️⃣ Log Buckets (Storage Layer)

## What is a Log Bucket?

A **log bucket**:

* Stores log entries
* Has configurable:

  * **Retention period**
  * Location (region)
  * CMEK encryption (optional)

By default:

* Logs go to the `_Default` bucket
* Audit logs may go to `_Required`

---

## Retention (VERY EXAM RELEVANT)

You can configure:

* Retention days (e.g., 30, 90, 365)
* Longer retention = higher cost

> **Exam signal:**
> “Retain logs for 2 years” → configure log bucket retention.

---

## Regional vs Global Buckets

* You can create **regional log buckets**
* Helps with:

  * Data residency requirements
  * Compliance

> **ACE trap:**
> Retention is configured at the bucket level, not per log entry.

---

# 3️⃣ Log Router (Routing Engine)

The **Log Router**:

* Automatically receives all logs
* Routes logs to:

  * Log buckets
  * Log sinks (BigQuery, GCS, Pub/Sub)

You configure routing by:

* Creating log sinks
* Defining filters

> **ACE rule:**
> Router decides **where logs go**, not how they’re stored.

---

# 4️⃣ Log Analytics (SQL on Logs)

Log Analytics allows:

* SQL-style querying of logs
* BigQuery-like experience
* No need to export logs to BigQuery

It operates directly on:

* Log buckets

> **Exam signal:**
> “Query logs using SQL without exporting” → **Log Analytics**

---

## Log Analytics vs BigQuery (IMPORTANT DISTINCTION)

| Feature             | Log Analytics      | BigQuery Export |
| ------------------- | ------------------ | --------------- |
| SQL query           | Yes                | Yes             |
| External BI tools   | Limited            | Full            |
| Cross-dataset joins | Limited            | Yes             |
| Long-term analytics | Better in BigQuery |                 |

> **ACE rule:**
> Simple SQL on logs → Log Analytics
> Complex analytics → BigQuery export

---

# 5️⃣ Creating Custom Log Buckets (Exam Awareness)

You may:

* Create bucket in specific region
* Set retention
* Attach CMEK
* Route specific logs to it

CLI example (conceptual):

```bash
gcloud logging buckets create my-secure-bucket \
  --location=us-central1 \
  --retention-days=365
```

> You’re tested on **what it accomplishes**, not syntax.

---

# 6️⃣ Common ACE Exam Scenarios

### Scenario 1

> “Logs must be retained for 7 years”

✅ Create log bucket with extended retention.

---

### Scenario 2

> “Security logs must remain in EU region”

✅ Create regional log bucket in EU.

---

### Scenario 3

> “Run SQL queries on logs without exporting to BigQuery”

✅ Enable Log Analytics.

---

### Scenario 4

> “Only ERROR logs should be exported”

✅ Configure log sink filter in router.

---

# 7️⃣ Common ACE Exam Traps

❌ Confusing log bucket with Cloud Storage
❌ Exporting logs unnecessarily
❌ Forgetting retention settings
❌ Thinking Log Analytics replaces BigQuery
❌ Ignoring IAM on log buckets

---

# 8️⃣ Monitoring vs Logging (Reminder)

| Tool          | Purpose          |
| ------------- | ---------------- |
| Monitoring    | Metrics + alerts |
| Logging       | Log entries      |
| Log Analytics | SQL on logs      |
| Log Router    | Routing engine   |

---

# 🔑 One-line ACE Memory Hooks

* **Logs → Router → Bucket**
* **Retention set on bucket**
* **SQL on logs = Log Analytics**
* **Export = Log Sink**
* **Compliance → Regional bucket**

--- 
