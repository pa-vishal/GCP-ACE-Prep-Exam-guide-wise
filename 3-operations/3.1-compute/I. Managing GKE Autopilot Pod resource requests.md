### **Section 3.1 – Managing compute resources**

#### **Managing GKE Autopilot Pod resource requests**

![Image](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-architecture.svg)

![Image](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c48368669fc5b3f179eb_Kubernetes-Limits-and-Request-04-1-1170x585.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A2000/0%2ApOYdvtoh6ZHe7lG3)

This bullet is **Autopilot-specific and frequently tested**. The ACE exam checks whether you understand that **in Autopilot, Pod resource requests are mandatory and drive scheduling, scaling, and cost**—you don’t manage nodes at all.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **why Pod resource requests are required in Autopilot**
* Set **CPU/memory requests correctly**
* Predict **cost and scheduling behavior**
* Diagnose **Pending Pods** in Autopilot

> **Exam mindset:**
> *“In Autopilot, Pods define capacity—nodes follow.”*

---

## 2️⃣ How GKE Autopilot works (mental model)

```
Pod spec (requests) → Autopilot provisions capacity → Pod runs
```

Key implications:

* You **do not** size nodes
* You **do not** manage node pools
* **Requests = scheduling + billing unit**

> **ACE rule:**
> In Autopilot, **requests are not optional**.

---

## 3️⃣ Requests vs limits in Autopilot (MUST KNOW)

### Resource **requests**

* **Required**
* Used for:

  * Scheduling
  * Capacity provisioning
  * Billing

### Resource **limits**

* Optional
* Cap maximum usage

> **Exam trap:**
> Setting only limits (no requests) → **Pod rejected**

---

## 4️⃣ Required fields (exam-relevant)

For every container in Autopilot, you must specify:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "1Gi"
```

Optional:

```yaml
limits:
  cpu: "1"
  memory: "2Gi"
```

> **ACE signal:**
> “Pod won’t schedule in Autopilot” → missing/invalid requests

---

## 5️⃣ Billing behavior (VERY IMPORTANT)

* Autopilot **bills based on requests**, not actual usage
* Over-requesting = higher cost
* Under-requesting = throttling or OOM kills

> **Exam rule:**
> Right-size requests to control cost.

---

## 6️⃣ Common scheduling failures & causes

| Symptom                  | Likely cause           |
| ------------------------ | ---------------------- |
| Pod rejected at creation | Missing requests       |
| Pod Pending              | Requests too large     |
| High cost                | Requests oversized     |
| OOMKilled                | Memory request too low |

---

## 7️⃣ Autopilot vs Standard GKE (EXAM COMPARISON)

| Feature           | Autopilot | Standard  |
| ----------------- | --------- | --------- |
| Node management   | ❌         | ✅         |
| Requests required | ✅         | ❌         |
| Billing based on  | Requests  | Node size |
| Node pools        | ❌         | ✅         |

> **ACE rule:**
> If the question mentions **Autopilot**, think **Pod specs**, not nodes.

---

## 8️⃣ Interaction with autoscaling (exam awareness)

* **HPA** still works:

  * Scales **number of Pods**
* Autopilot:

  * Automatically provisions capacity behind the scenes

```
HPA scales Pods
↓
Autopilot adds capacity
```

> **Exam trap:**
> You never configure node autoscaling in Autopilot.

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Pod creation fails in Autopilot”

✅ Check:

* CPU & memory requests present

---

### Scenario 2

> “Autopilot cluster costs are unexpectedly high”

✅ Likely cause:

* Over-provisioned requests

---

### Scenario 3

> “Pods are throttled or OOMKilled”

✅ Likely cause:

* Requests too low (limits too tight)

---

## 🔑 One-line ACE memory hooks

* **Autopilot = Pods define capacity**
* **Requests are mandatory**
* **Billing = requests**
* **No nodes to manage**

--- 
