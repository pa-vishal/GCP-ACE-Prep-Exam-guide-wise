### **Section 3.4 – Monitoring and logging**

#### **Deploying Google Cloud Managed Service for Prometheus**

This bullet is about **Kubernetes-native monitoring** using Prometheus, but managed by Google.
The ACE exam tests whether you understand:

* What Managed Service for Prometheus (GMP) is
* Why it exists
* Where it runs
* How it integrates with Cloud Monitoring

Not how to handcraft Helm charts.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain what Managed Service for Prometheus does
* Know that it is **for Kubernetes environments**
* Understand that it:

  * Scrapes metrics
  * Sends them to Cloud Monitoring
* Recognize when to use it instead of standalone Prometheus

> **Exam mindset:**
> *“We’re running Kubernetes and need Prometheus-style metrics — what’s the managed option?”*

---

# 2️⃣ What is Google Cloud Managed Service for Prometheus?

It is:

* A **fully managed Prometheus-compatible monitoring solution**
* Designed for:

  * GKE
  * Kubernetes workloads
* Integrated into **Cloud Monitoring**

It allows you to:

* Use Prometheus scraping
* Keep PromQL queries
* Avoid managing Prometheus infrastructure

---

# 3️⃣ Why not run your own Prometheus? (EXAM LOGIC)

Running self-managed Prometheus requires:

* Managing:

  * Storage
  * Scaling
  * Upgrades
* Handling high cardinality metrics

Managed Service:

* Removes operational overhead
* Stores metrics in Cloud Monitoring backend

> **ACE rule:**
> If question says “reduce operational overhead” → Managed Service

---

# 4️⃣ How it works (High-Level Flow)

```
Kubernetes Pods
   ↓
Prometheus scraping
   ↓
Managed collectors
   ↓
Cloud Monitoring backend
```

Key points:

* Metrics become part of Cloud Monitoring
* Can be used in:

  * Dashboards
  * Alerts
  * SLOs

---

# 5️⃣ Where it is used (VERY IMPORTANT)

Primarily used in:

* **GKE clusters**
* Kubernetes environments

Not typically used for:

* Cloud Run
* Cloud SQL
* Compute Engine standalone VMs

> **ACE trap:**
> Prometheus service is for Kubernetes workloads.

---

# 6️⃣ Prometheus vs Cloud Monitoring (DISTINCTION)

| Feature             | Prometheus | Cloud Monitoring      |
| ------------------- | ---------- | --------------------- |
| Pull-based scraping | Yes        | No (built-in metrics) |
| PromQL support      | Yes        | Limited               |
| Managed by Google   | With GMP   | Yes                   |

Managed Service bridges both worlds.

---

# 7️⃣ Typical ACE exam scenarios

### Scenario 1

> “GKE workloads expose Prometheus metrics endpoint”

✅ Use Managed Service for Prometheus.

---

### Scenario 2

> “Avoid maintaining Prometheus servers manually”

✅ Use managed service.

---

### Scenario 3

> “Create alerts based on Kubernetes custom metrics”

✅ Prometheus metrics + Cloud Monitoring alerts.

---

# 8️⃣ Integration with Alerting

Prometheus metrics ingested via GMP:

* Appear in Cloud Monitoring
* Can trigger alerting policies
* Can be visualized in dashboards

> **ACE rule:**
> Prometheus metrics become first-class Monitoring metrics.

---

# 9️⃣ Common ACE exam traps

❌ Installing standalone Prometheus when managed service exists
❌ Using it for non-Kubernetes workloads
❌ Confusing it with Ops Agent
❌ Expecting it to monitor Cloud Run

---

# 🔑 One-line ACE memory hooks

* **Kubernetes metrics → Prometheus**
* **Managed Service = no infra to manage**
* **Integrates with Monitoring**
* **Reduces operational overhead**

---
 
