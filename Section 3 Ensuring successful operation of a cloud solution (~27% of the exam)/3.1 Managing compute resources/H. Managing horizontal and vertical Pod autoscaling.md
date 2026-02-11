### **Section 3.1 – Managing compute resources**

#### **Managing horizontal and vertical Pod autoscaling configurations**

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2A0wJBUCAWTLAe62PHmhoLOQ.gif)

![Image](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-autoscale-1.svg)

![Image](https://developers.redhat.com/sites/default/files/vpa_diagram_0.png)

This bullet is **classic ACE exam material**. The exam is testing whether you understand **what scales Pods, what scales nodes, and when to use each autoscaling type**—not how to tune metrics deeply.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Differentiate **Horizontal Pod Autoscaling (HPA)** vs **Vertical Pod Autoscaling (VPA)**
* Know **what each one changes**
* Choose the **right autoscaler for the scenario**
* Avoid confusing Pod autoscaling with **node autoscaling**

> **Exam mindset:**
> *“Do I need more Pods, or do my Pods need more resources?”*

---

## 2️⃣ Horizontal Pod Autoscaler (HPA) – MOST TESTED

### What HPA does

* **Scales the number of Pods**
* Based on:

  * CPU utilization (most common)
  * Memory utilization
  * Custom metrics (recognition-level)

```
High load → more Pods
Low load  → fewer Pods
```

### Use when

* Stateless workloads
* Web apps
* APIs
* Traffic-based scaling

### Exam signals

* “Increase replicas automatically”
* “Handle traffic spikes”
* “Scale out”

> **ACE rule:**
> If the app can run multiple copies → **HPA**

---

### Viewing HPA

```bash
kubectl get hpa
```

---

### Conceptual HPA configuration

* Target CPU (e.g., 60%)
* Min Pods
* Max Pods

> **Exam note:**
> You’re tested on **what HPA does**, not YAML syntax.

---

## 3️⃣ Vertical Pod Autoscaler (VPA)

### What VPA does

* **Adjusts CPU/memory requests and limits**
* Scales **up/down**, not out/in
* May **restart Pods** to apply changes

```
Pod too small → increase CPU/memory
Pod oversized → reduce CPU/memory
```

### Use when

* Stateful workloads
* Apps that cannot scale horizontally
* Resource tuning over time

### Exam signals

* “Adjust CPU/memory automatically”
* “Single Pod workload”
* “Right-size resources”

> **ACE rule:**
> If replicas don’t help → **VPA**

---

## 4️⃣ HPA vs VPA (MUST MEMORIZE)

| Feature                 | HPA | VPA |
| ----------------------- | --- | --- |
| Scales Pods count       | ✅   | ❌   |
| Scales CPU/memory       | ❌   | ✅   |
| Best for stateless apps | ✅   | ❌   |
| May restart Pods        | ❌   | ✅   |
| Handles traffic spikes  | ✅   | ❌   |

---

## 5️⃣ Pod autoscaling vs Node autoscaling (EXAM TRAP)

| Autoscaler                | Scales        |
| ------------------------- | ------------- |
| **HPA**                   | Pods          |
| **VPA**                   | Pod resources |
| **Node pool autoscaling** | Nodes         |

> **ACE trap:**
> Pods pending due to lack of CPU → **node pool autoscaling**, not HPA

---

## 6️⃣ How they work together (exam awareness)

Typical production setup:

```
HPA → increases Pods
↓
Node autoscaler → adds nodes
```

> **Exam signal:**
> “Traffic increases and cluster scales automatically” → HPA + node autoscaling

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “Web app should handle traffic spikes automatically”

✅ **Horizontal Pod Autoscaler**

---

### Scenario 2

> “Application runs as a single Pod and needs more memory over time”

✅ **Vertical Pod Autoscaler**

---

### Scenario 3

> “Pods stuck in Pending (Insufficient CPU)”

✅ **Node pool autoscaling**, not HPA/VPA

---

### Scenario 4

> “Minimize restarts while scaling”

✅ **HPA**, not VPA

---

## 8️⃣ Common ACE exam traps

❌ Using VPA for traffic spikes
❌ Expecting HPA to change Pod memory
❌ Forgetting Pods need requests set for HPA
❌ Confusing Pod autoscaling with node autoscaling

---

## 🔑 One-line ACE memory hooks

* **HPA = more Pods**
* **VPA = bigger Pods**
* **Pending Pods = scale nodes**
* **Traffic spikes = HPA**

--- 
