### **Section 3.4 – Monitoring and logging**

#### **Exporting logs to external systems (e.g., on-premises, BigQuery)**

This is a **high-value operational topic**. The ACE exam tests whether you understand:

* Logs are stored in **Cloud Logging**
* Exporting logs requires a **log sink**
* Different destinations serve different purposes
* IAM and routing matter

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain what a **log sink** is
* Export logs to:

  * BigQuery
  * Cloud Storage
  * Pub/Sub (for on-prem or external systems)
* Choose the right destination
* Avoid confusing logs with metrics

> **Exam mindset:**
> *“Logs need to go somewhere else — how do I route them?”*

---

## 2️⃣ Cloud Logging basics (foundation)

Logs are automatically collected from:

* Compute Engine
* GKE
* Cloud Run
* Load balancers
* Many managed services

Logs are stored in:

* **Log buckets** (by default)

To export logs, you create:

> **Log Sink**

---

## 3️⃣ What is a Log Sink? (MUST KNOW)

A **log sink**:

* Routes logs from Logging to a destination
* Uses:

  * A filter
  * A destination
* Requires IAM permissions

Flow:

```
Cloud Logging
   ↓ (log sink)
Destination (BigQuery / GCS / PubSub)
```

> **ACE rule:**
> Exporting logs = create a **log sink**

---

## 4️⃣ Common export destinations (VERY IMPORTANT)

### 1️⃣ BigQuery (EXAM FAVORITE)

Use when:

* You need analytics on logs
* Long-term retention
* Complex SQL queries

Example scenario:

> “Analyze error trends over 12 months”

✅ Export logs to **BigQuery**

---

### 2️⃣ Cloud Storage

Use when:

* Archival storage
* Compliance
* Cheap long-term retention

Example:

> “Retain logs for 7 years”

✅ Export to **Cloud Storage**

---

### 3️⃣ Pub/Sub (for external/on-prem systems)

Use when:

* Streaming logs to SIEM
* Sending logs to on-prem systems
* Real-time external processing

Flow:

```
Logging → Sink → Pub/Sub → External consumer
```

> **ACE rule:**
> On-prem integration → **Pub/Sub**

---

## 5️⃣ Creating a log sink (CLI example)

```bash
gcloud logging sinks create my-bq-sink \
  bigquery.googleapis.com/projects/my-project/datasets/logs_dataset \
  --log-filter="severity>=ERROR"
```

This:

* Exports only ERROR logs
* Routes them to BigQuery

> **Exam note:**
> You’re tested on the concept, not full CLI syntax.

---

## 6️⃣ IAM considerations (VERY IMPORTANT)

When creating a sink:

* Logging creates a **service account**
* That service account needs:

  * BigQuery Data Editor (for BigQuery)
  * Storage Object Creator (for GCS)
  * Pub/Sub Publisher (for Pub/Sub)

> **ACE trap:**
> Sink created but no logs exported → missing IAM on destination.

---

## 7️⃣ Filtering logs before export (EXAM SIGNAL)

Log sinks support filters like:

* `severity>=ERROR`
* `resource.type="gce_instance"`
* Specific log names

> **ACE rule:**
> Filter early to reduce cost.

---

## 8️⃣ Logs vs metrics (COMMON EXAM TRAP)

| Need                  | Tool              |
| --------------------- | ----------------- |
| Alert on CPU          | Monitoring metric |
| Export log entries    | Log sink          |
| Count log errors      | Log-based metric  |
| Analyze logs with SQL | BigQuery          |

> **ACE trap:**
> Don’t export logs just to create alerts — use log-based metrics instead.

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Security team wants logs in SIEM”

✅ Create log sink → Pub/Sub

---

### Scenario 2

> “Run analytics on audit logs”

✅ Export to BigQuery

---

### Scenario 3

> “Store logs cheaply for compliance”

✅ Export to Cloud Storage

---

### Scenario 4

> “Sink created but no data appears”

✅ Check:

* Filter logic
* Destination IAM permissions

---

## 🔟 Common ACE exam traps

❌ Forgetting IAM on destination
❌ Exporting all logs unnecessarily
❌ Confusing metrics with logs
❌ Using BigQuery when streaming is required
❌ Expecting automatic cross-project export

---

## 🔑 One-line ACE memory hooks

* **Export = log sink**
* **Analytics = BigQuery**
* **Archive = GCS**
* **On-prem = Pub/Sub**
* **IAM required for sink to write**

---
 
