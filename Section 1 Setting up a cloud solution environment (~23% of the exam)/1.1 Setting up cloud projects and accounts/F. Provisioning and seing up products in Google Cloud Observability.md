
### **Section 1.1 – Provisioning and setting up products in Google Cloud Observability**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/1_Logging__Monitoring.max-1600x1600.jpg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/image3_YN7Di28.max-2000x2000.png)

This bullet is **very important for the ACE exam**, but it is **tested conceptually**, not operationally. The exam checks whether you understand **what to enable, when, and why**, not how to tune dashboards like an SRE.

---

## 1️⃣ What “Google Cloud Observability” actually means

**Google Cloud Observability** is the umbrella for services that let you:

* **See** what’s happening
* **Detect** problems
* **Troubleshoot** performance issues

It includes:

| Product          | Purpose                      |
| ---------------- | ---------------------------- |
| Cloud Monitoring | Metrics, dashboards, alerts  |
| Cloud Logging    | Logs from services & apps    |
| Cloud Trace      | Request latency tracing      |
| Cloud Profiler   | CPU / memory profiling       |
| Error Reporting  | App error aggregation        |
| Ops Agent        | Unified metrics + logs agent |

> **Exam framing**:
> Observability = **Monitoring + Logging + Diagnostics**

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you can:

### ✅ Identify which observability product to use

* Metrics → Monitoring
* Logs → Logging
* Latency → Trace
* CPU/memory hotspots → Profiler
* App crashes → Error Reporting

### ✅ Know what must be enabled vs what is automatic

* Some observability works **out of the box**
* Some requires **API enablement or agents**

### ❌ What the exam does NOT test

* Writing advanced alerting expressions
* Custom dashboards in depth
* SRE-level tuning

---

## 3️⃣ What is automatic vs what must be provisioned

### 🟢 Enabled automatically (exam-relevant)

* **Cloud Logging** (for most GCP services)
* **Basic Monitoring metrics**
* **Audit Logs** (Admin Activity)

> New project → logging & basic metrics already flow

---

### 🟡 Requires explicit setup / enablement

| Product                 | Requirement        |
| ----------------------- | ------------------ |
| Cloud Monitoring alerts | You configure them |
| Ops Agent               | Install on VM      |
| Cloud Trace             | Enable API         |
| Cloud Profiler          | Enable API + agent |
| Error Reporting         | App integration    |

---

## 4️⃣ Enabling observability APIs via CLI (gcloud)

### 🔹 Enable core observability APIs

```bash
gcloud services enable \
  monitoring.googleapis.com \
  logging.googleapis.com \
  cloudtrace.googleapis.com \
  cloudprofiler.googleapis.com \
  errorreporting.googleapis.com \
  --project=my-project
```

> **ACE exam tip**:
> If observability “doesn’t work” → first check **API enablement**

---

## 5️⃣ Ops Agent (VERY exam-relevant for VMs)

### What Ops Agent does

* Collects:

  * Metrics (CPU, memory, disk)
  * Logs (system + app)
* Replaces legacy monitoring/logging agents

---

### Installing Ops Agent on a VM

```bash
curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
sudo bash add-google-cloud-ops-agent-repo.sh --also-install
```

> **Exam pattern**:
> “VM metrics/logs not appearing” → **Install Ops Agent**

---

## 6️⃣ Observability per compute type (exam favorite)

| Compute         | Observability behavior              |
| --------------- | ----------------------------------- |
| Compute Engine  | Needs Ops Agent for full visibility |
| GKE             | Metrics/logs mostly automatic       |
| Cloud Run       | Fully managed, auto-integrated      |
| Cloud Functions | Auto-integrated                     |
| App Engine      | Auto-integrated                     |

> **Serverless = observability by default**

---

## 7️⃣ Monitoring alerts (conceptual)

You can create alerts based on:

* CPU usage
* Memory usage
* Request latency
* Error rate

**Exam-level understanding**

* Alerts = Monitoring
* Logs ≠ alerts
* Metrics drive alerts

---

## 8️⃣ Real exam-style scenarios

### Scenario 1

> “VM is running but no metrics appear in Monitoring”

✅ Correct answer:

* Install **Ops Agent**

---

### Scenario 2

> “Application latency troubleshooting is required”

✅ Correct tool:

* **Cloud Trace**

---

### Scenario 3

> “Find which function is consuming most CPU”

✅ Correct tool:

* **Cloud Profiler**

---

### Scenario 4

> “See application crashes across services”

✅ Correct tool:

* **Error Reporting**

---

## 9️⃣ Common exam traps

❌ Confuse Logging with Monitoring
❌ Assume Ops Agent is automatic
❌ Use Trace when logs are needed
❌ Think alerts come from logs directly

---

## 🔑 One-line exam memory hook

> **Metrics → Monitoring**
> **Logs → Logging**
> **Latency → Trace**
> **CPU hotspots → Profiler**

--- 
