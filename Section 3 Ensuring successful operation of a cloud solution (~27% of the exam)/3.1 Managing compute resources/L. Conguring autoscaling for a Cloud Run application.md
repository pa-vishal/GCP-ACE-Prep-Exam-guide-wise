### **Section 3.1 – Managing compute resources**

#### **Configuring autoscaling for a Cloud Run application**

![Image](https://miro.medium.com/1%2A2gnIctgRQtHYoq6btZ7qYA.png)

![Image](https://docs.cloud.google.com/static/run/docs/images/billable-time-with-min-instances.svg)

![Image](https://docs.cloud.google.com/static/run/docs/images/cloud-run-security-arch.svg)

This bullet is **very frequently tested**. The ACE exam checks whether you understand **how Cloud Run scales**, **which knobs you can control**, and **how scaling affects cost, performance, and availability**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **how Cloud Run autoscaling works**
* Configure **min instances**, **max instances**, and **concurrency**
* Choose settings to balance **cost vs latency**
* Diagnose **cold starts** and **throttling**

> **Exam mindset:**
> *“How do I handle variable traffic without managing servers?”*

---

## 2️⃣ How Cloud Run autoscaling works (MENTAL MODEL)

```
Incoming requests
 ↓
Cloud Run creates instances
 ↓
Each instance handles N concurrent requests
 ↓
Scale out / scale in automatically
```

Key points:

* Scaling is **request-driven**
* Instances are **stateless**
* Scaling is **automatic and fast**

> **ACE rule:**
> You never scale Cloud Run by CPU or memory directly—**requests drive scaling**.

---

## 3️⃣ Core autoscaling controls (MUST KNOW)

### A. **Max instances** (VERY IMPORTANT)

* Upper limit on number of instances
* Prevents:

  * Cost explosions
  * Backend overload (DB, APIs)

```bash
gcloud run services update my-service \
  --max-instances=50 \
  --region=us-central1
```

**Exam signals**

* “Protect backend systems”
* “Limit cost”

---

### B. **Min instances** (COLD START CONTROL)

* Keeps instances **warm**
* Reduces cold-start latency
* Increases baseline cost

```bash
gcloud run services update my-service \
  --min-instances=1 \
  --region=us-central1
```

**Exam signals**

* “Low latency required”
* “Avoid cold starts”

> **ACE tradeoff:**
> Min instances = better latency, higher cost

---

### C. **Concurrency** (THROUGHPUT CONTROL)

* Number of concurrent requests per instance
* Default: **80**
* Lower concurrency:

  * More instances
  * Lower per-instance load
* Higher concurrency:

  * Fewer instances
  * More efficient CPU usage

```bash
gcloud run services update my-service \
  --concurrency=20 \
  --region=us-central1
```

**Exam signals**

* “CPU-heavy requests”
* “Long-running requests”

---

## 4️⃣ Autoscaling + pricing (EXAM FAVORITE)

Cloud Run billing is based on:

* CPU & memory **while requests are handled**
* Number of instances created
* Request duration

Key implications:

* Overly low concurrency → more instances → higher cost
* High min instances → always-on cost

> **ACE rule:**
> Right-size concurrency before raising max instances.

---

## 5️⃣ Common autoscaling scenarios (EXAM PRACTICE)

### Scenario 1

> “Traffic spikes cause database overload”

✅ Fix:

* Set **max instances**
* Optionally lower concurrency

---

### Scenario 2

> “Users complain about cold-start latency”

✅ Fix:

* Set **min instances ≥ 1**

---

### Scenario 3

> “CPU-intensive requests time out”

✅ Fix:

* Lower **concurrency**
* Possibly increase CPU allocation

---

### Scenario 4

> “Unpredictable traffic with cost sensitivity”

✅ Fix:

* Keep **min instances = 0**
* Tune **concurrency**

---

## 6️⃣ Autoscaling vs other platforms (EXAM COMPARISON)

| Platform       | Scaling unit         |
| -------------- | -------------------- |
| Cloud Run      | Requests → instances |
| GKE            | Pods & nodes         |
| Compute Engine | VMs (manual / MIG)   |

> **Exam trap:**
> Do not apply GKE autoscaling logic to Cloud Run.

---

## 7️⃣ What you do NOT control in Cloud Run (EXAM TRAP)

❌ Node size
❌ Node autoscaling
❌ OS-level tuning

> **ACE rule:**
> Cloud Run abstracts infrastructure completely.

---

## 8️⃣ Common ACE exam traps

❌ Expecting Cloud Run to scale on CPU metrics
❌ Forgetting min instances affect cost
❌ Setting max instances too high without backend capacity
❌ Treating concurrency as “threads” instead of requests

---

## 🔑 One-line ACE memory hooks

* **Cloud Run scales on requests**
* **Max instances = cost & backend protection**
* **Min instances = cold-start control**
* **Concurrency = efficiency knob**

--- 
