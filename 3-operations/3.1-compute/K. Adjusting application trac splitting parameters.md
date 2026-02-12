### **Section 3.1 – Managing compute resources**

#### **Adjusting application traffic-splitting parameters**

*(Cloud Run, Cloud Run functions, GKE)*

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2A_RHjDg-9VHr4egOR.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A2000/1%2AWG0jvAOdkOfER60FygS6qQ.png)

![Image](https://docs.cloud.google.com/static/run/docs/images/service-health-load-balancer.svg)

This bullet tests whether you understand **how to safely route traffic between versions** across **serverless and Kubernetes platforms**. The ACE exam focuses on **which platform supports traffic splitting natively, how it’s controlled, and when to use it**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify **which services support traffic splitting**
* Adjust traffic **without redeploying** (when possible)
* Choose the **right rollout strategy** (canary / blue-green)
* Avoid downtime during updates

> **Exam mindset:**
> *“How do I shift users to a new version safely?”*

---

## 2️⃣ Platform support overview (MUST KNOW)

| Platform                | Traffic splitting support | How it’s done                   |
| ----------------------- | ------------------------- | ------------------------------- |
| **Cloud Run**           | ✅ Native                  | By **revision**                 |
| **Cloud Run functions** | ⚠️ Limited / indirect     | By **versions** (gen-dependent) |
| **GKE**                 | ❌ Not native              | Via **Service / Ingress / LB**  |

> **ACE rule:**
> **Cloud Run is the simplest and most tested for traffic splitting.**

---

## 3️⃣ Cloud Run traffic splitting (MOST TESTED)

### How it works

* Traffic is split **across revisions**
* Percentages must total **100%**
* Changes are **instant** and reversible

### Adjust traffic (no redeploy)

```bash
gcloud run services update-traffic my-service \
  --to-revisions=rev-v2=80,rev-v1=20 \
  --region=us-central1
```

### Common use cases

* Canary deployments (e.g., 5–10%)
* Gradual rollouts
* Instant rollback

> **ACE signal:**
> “Shift traffic gradually” → **Cloud Run traffic splitting**

---

## 4️⃣ Cloud Run functions traffic behavior (exam awareness)

Cloud Run functions (especially Gen 2):

* Are backed by **Cloud Run**
* Support **versioning**
* Traffic routing is **less explicit** than Cloud Run services

### Exam expectation

* Know that:

  * New deployments create **new versions**
  * Traffic typically moves to **latest**
* Deep traffic-split commands are **not tested**

> **ACE guidance:**
> If the question mentions **precise traffic percentages**, Cloud Run (service) is the answer—not Functions.

---

## 5️⃣ GKE traffic splitting (CONCEPTUAL – EXAM AWARENESS)

GKE does **not** split traffic by default at the workload level.

### How it’s achieved

* Multiple Deployments
* Single Service selecting multiple versions
* Or:

  * Ingress
  * HTTP(S) Load Balancer
  * Service Mesh (advanced; recognition only)

### Typical pattern

```
Users
 ↓
Load Balancer / Ingress
 ↓
Service
 ├── Pods v1 (90%)
 └── Pods v2 (10%)
```

> **ACE rule:**
> Traffic splitting in GKE is **infrastructure-driven**, not Pod-driven.

---

## 6️⃣ Blue/Green vs Canary (MUST RECOGNIZE)

| Strategy       | Description                 | Best used with |
| -------------- | --------------------------- | -------------- |
| **Blue/Green** | Switch 100% traffic at once | Cloud Run      |
| **Canary**     | Gradual % rollout           | Cloud Run, GKE |
| **Rolling**    | Incremental Pod replacement | GKE            |

> **Exam signal:**
> “Test with small % of users” → **Canary**

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “Route 10% of users to new version, 90% to old”

✅ **Cloud Run traffic splitting**

---

### Scenario 2

> “Instant rollback without redeploying”

✅ **Adjust traffic percentages**

---

### Scenario 3

> “Kubernetes app needs gradual rollout”

✅ **Ingress / Load Balancer–based traffic split**

---

## 8️⃣ Common ACE exam traps

❌ Expecting GKE Pods to split traffic automatically
❌ Redeploying when traffic update is sufficient
❌ Assuming Functions support full traffic controls
❌ Forgetting traffic must total 100%

---

## 🔑 One-line ACE memory hooks

* **Cloud Run = native traffic split**
* **Functions = limited**
* **GKE = LB/Ingress based**
* **Rollback = traffic shift, not redeploy**

---
 
