### **Section 3.4 – Monitoring and logging**

#### **Creating and ingesting Cloud Monitoring custom metrics (e.g., from applications or logs)**

This is a **deeper operational topic**. The ACE exam is not testing you on writing full metric pipelines — it’s testing whether you understand:

* When **built-in metrics are insufficient**
* How **custom metrics enter Cloud Monitoring**
* The difference between **application metrics vs log-based metrics**

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain what a **custom metric** is
* Distinguish between:

  * Application-generated metrics
  * Log-based metrics
* Understand the ingestion flow
* Use custom metrics in **alerting policies**

> **Exam mindset:**
> *“Built-in metrics don’t measure this — how do I track it?”*

---

## 2️⃣ Why custom metrics exist

Built-in metrics cover:

* CPU
* Memory
* Network
* Request count
* Latency

But they do NOT cover:

* Business KPIs (orders per minute)
* Application-level queue depth
* Feature flags
* Custom error counters

> **ACE rule:**
> If the metric is application-specific → **custom metric**

---

## 3️⃣ Two ways to create custom metrics (VERY IMPORTANT)

### 1️⃣ Application-generated custom metrics

Application sends metrics directly to Cloud Monitoring.

Flow:

```
Application → Monitoring API → Cloud Monitoring → Alerting/Dashboard
```

Used for:

* Business metrics
* Real-time counters
* App-specific signals

---

### 2️⃣ Log-based metrics (EXAM FAVORITE)

Create a metric derived from **logs**.

Flow:

```
Application logs → Cloud Logging → Log-based metric → Monitoring → Alert
```

Used for:

* Counting error messages
* Tracking specific log patterns
* Monitoring structured log fields

> **ACE rule:**
> If the data already exists in logs → use **log-based metric**

---

## 4️⃣ Log-based metrics (MUST KNOW)

You define:

* A log filter
* A metric type (counter or distribution)

Example use cases:

* Count occurrences of `"ERROR"`
* Track number of 500 HTTP responses
* Extract latency field from structured logs

> **Exam signal:**
> “Create alert when specific log appears” → **log-based metric**

---

## 5️⃣ Custom metric types (exam awareness)

| Type         | Use case                     |
| ------------ | ---------------------------- |
| Counter      | Event count                  |
| Gauge        | Current value                |
| Distribution | Latency or size measurements |

You do NOT need to memorize syntax — just concepts.

---

## 6️⃣ Ingesting application metrics (conceptual flow)

Applications:

* Use client libraries
* Send metrics via API
* Must have proper IAM permissions

Required permission:

* `monitoring.metricWriter`

> **ACE trap:**
> Missing IAM → metrics never appear

---

## 7️⃣ Using custom metrics in alerts

Once created:

* Custom metrics behave like built-in metrics
* Can be:

  * Used in alerting policies
  * Displayed in dashboards
  * Aggregated

> **ACE rule:**
> Custom metrics integrate fully with Monitoring.

---

## 8️⃣ Custom metrics vs logs (COMMON EXAM TRAP)

| If you need…       | Use              |
| ------------------ | ---------------- |
| CPU alert          | Built-in metric  |
| Count log error    | Log-based metric |
| Track business KPI | Custom metric    |
| Store log entries  | Cloud Logging    |

> **ACE trap:**
> Logs alone cannot trigger metric alerts without a log-based metric.

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Alert when application logs contain ‘PaymentFailed’”

✅ Create **log-based metric**
✅ Create alert on that metric

---

### Scenario 2

> “Track orders per minute for dashboard”

✅ Application-generated custom metric

---

### Scenario 3

> “Metric not visible in Monitoring”

✅ Check:

* IAM role (`metricWriter`)
* Correct project
* Correct metric type

---

## 🔟 Common ACE exam traps

❌ Using logs directly for alerting
❌ Forgetting to create log-based metric first
❌ Missing `monitoring.metricWriter` role
❌ Creating custom metric when built-in metric exists

---

## 🔑 One-line ACE memory hooks

* **Built-in first, custom if needed**
* **Logs → log-based metric → alert**
* **App metrics → Monitoring API**
* **IAM required for ingestion**

---
 
