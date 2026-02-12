### **Section 3.4 – Monitoring and logging**

#### **Creating Cloud Monitoring alerts based on resource metrics**

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2AgP1M5_Er9ZyLX2XX.jpg)

![Image](https://docs.cloud.google.com/static/monitoring/images/recommended-alerts.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/pub_sub.max-700x700.jpg)

This is a **core ACE topic**. The exam is not testing advanced SRE design—it’s testing whether you can **turn metrics into actionable alerts**, choose the **right signal**, and avoid noisy or useless alerts.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify **which metrics to alert on**
* Create an alert based on **resource metrics**
* Choose **thresholds and duration**
* Route alerts to **notification channels**
* Avoid confusing **monitoring vs logging**

> **Exam mindset:**
> *“When something goes wrong, how do I get notified in time?”*

---

## 2️⃣ Cloud Monitoring basics (foundation)

### What Cloud Monitoring does

* Collects **metrics** from:

  * Compute Engine
  * GKE
  * Cloud Run
  * Cloud SQL
  * Load balancers
* Evaluates metrics against **alerting policies**

> **ACE rule:**
> **Metrics trigger alerts; logs do not (directly).**

---

## 3️⃣ Resource metrics vs other signals (MUST KNOW)

### Resource metrics

* CPU utilization
* Memory utilization
* Disk usage
* Network throughput
* Instance uptime

These are the **most tested** metrics for ACE.

### Not tested deeply

* Custom metrics
* Complex SLO-based alerting

> **ACE signal:**
> “Alert when CPU is high” → **resource metric alert**

---

## 4️⃣ Alerting policy components (VERY IMPORTANT)

Every alerting policy has **four core parts**:

### 1. **Metric**

What you are measuring
Example: `compute.googleapis.com/instance/cpu/utilization`

---

### 2. **Condition**

When the alert should fire
Examples:

* CPU > 80%
* Memory > 90%
* Instance uptime < expected

---

### 3. **Duration**

How long the condition must hold
Example:

* CPU > 80% for **5 minutes**

> **ACE trap:**
> No duration = noisy alerts

---

### 4. **Notification channel**

Where the alert is sent
Examples:

* Email
* SMS
* PagerDuty
* Slack (via webhook)

---

## 5️⃣ Creating a metric-based alert (conceptual steps)

**Console flow (exam-level awareness):**

1. Cloud Monitoring → Alerting
2. Create alerting policy
3. Select **resource metric**
4. Set threshold + duration
5. Choose notification channel

> **Exam note:**
> You are tested on **what you configure**, not where you click.

---

## 6️⃣ Common resource-metric alerts (ACE FAVORITES)

### Compute Engine

* CPU utilization too high
* VM uptime unexpectedly low (crashes)

### GKE

* Node CPU usage
* Pod restarts (derived metric)

### Cloud SQL

* CPU usage
* Storage nearing limit

### Cloud Run

* Request latency
* Instance count spikes

> **ACE rule:**
> Alert on **symptoms**, not root causes.

---

## 7️⃣ Threshold selection (exam logic)

### Bad alert

* CPU > 80% for 10 seconds

### Good alert

* CPU > 80% for 5 minutes

> **ACE signal:**
> “Reduce alert noise” → increase **duration**, not threshold

---

## 8️⃣ Notification channels (exam awareness)

* Alerts do nothing unless someone sees them
* Channels must be:

  * Created first
  * Reused across policies

> **ACE trap:**
> Creating alerts without notification channels = useless

---

## 9️⃣ Monitoring vs logging (COMMON EXAM TRAP)

| Tool                 | Purpose                     |
| -------------------- | --------------------------- |
| **Cloud Monitoring** | Metrics, thresholds, alerts |
| **Cloud Logging**    | Logs, errors, text entries  |

> **ACE trap:**
> You **cannot** create a CPU alert from logs.

---

## 🔟 Common ACE exam scenarios

### Scenario 1

> “Notify admin if VM CPU is too high for 5 minutes”

✅ **Cloud Monitoring alert on CPU utilization**

---

### Scenario 2

> “Alert fires too often due to spikes”

✅ **Increase evaluation duration**

---

### Scenario 3

> “User wants to be emailed when Cloud SQL storage is almost full”

✅ **Metric-based alert + email notification**

---

## 11️⃣ Common ACE exam traps

❌ Using logs instead of metrics
❌ No duration set (alert storms)
❌ Alert without notification channel
❌ Alerting on non-actionable metrics
❌ Expecting Monitoring to auto-fix issues

---

## 🔑 One-line ACE memory hooks

* **Metrics → alerts**
* **Threshold + duration**
* **Logs ≠ alerts**
* **No channel = no value**
* **Alert on symptoms**

---

