### **Section 3.1 – Managing compute resources**

#### **Working with GKE node pools**

*(add, edit, remove a node pool; autoscaling node pool)*

![Image](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-architecture.svg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/5.max-2000x2000.png)

![Image](https://cdn.prod.website-files.com/68ad5281556da93bd7179b0e/68b79f42d778386c448da0d7_685d2e66568c4363263db929_465385bc-b1de-4671-ac9e-00c26e784994.png)

This bullet is about **how GKE capacity is managed**. The ACE exam tests whether you understand **why node pools exist**, **when to add or change them**, and **how autoscaling works at the node layer** (distinct from Pod autoscaling).

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **what a node pool is**
* Add/remove node pools to meet **workload needs**
* Enable **node pool autoscaling**
* Avoid mixing incompatible workloads in one pool

> **Exam mindset:**
> *“If Pods can’t schedule or costs are too high, what do I change at the node layer?”*

---

## 2️⃣ What a node pool is (mental model)

A **node pool** is:

* A group of **identical worker nodes**
* With the same:

  * Machine type
  * Disk type/size
  * Labels/taints
  * Autoscaling settings

```
GKE Cluster
 ├── Node Pool A (general)
 ├── Node Pool B (GPU)
 └── Node Pool C (spot/preemptible)
```

> **Key rule:**
> **Node pools let you mix node types in one cluster.**

---

## 3️⃣ Why node pools matter (EXAM FAVORITE)

Use **multiple node pools** to:

* Separate workloads (prod vs batch)
* Add **GPUs** without affecting others
* Use **Spot nodes** for cost savings
* Apply different autoscaling policies

**Exam signals**

* “Different machine types”
* “GPU workloads”
* “Cost optimization”
* “Workloads have different requirements”

---

## 4️⃣ Adding a node pool (CLI – exam-relevant)

```bash
gcloud container node-pools create high-mem-pool \
  --cluster=my-cluster \
  --region=us-central1 \
  --machine-type=e2-highmem-4 \
  --num-nodes=2
```

Use when:

* Existing pool doesn’t meet workload needs
* Pods are pending due to resource constraints

---

## 5️⃣ Editing a node pool (conceptual)

You can update:

* Autoscaling settings
* Node count
* Labels and taints
* Upgrade settings

> **Exam awareness:**
> You generally **cannot change machine type** of an existing pool — you create a new one instead.

---

## 6️⃣ Removing a node pool (CLI – exam-relevant)

```bash
gcloud container node-pools delete high-mem-pool \
  --cluster=my-cluster \
  --region=us-central1
```

Use when:

* Pool is unused
* Migrating workloads to a new pool
* Cost optimization

> **Exam trap:**
> Deleting a node pool **removes all Pods running on it**

---

## 7️⃣ Node pool autoscaling (VERY IMPORTANT)

### What it does

* Automatically adjusts **number of nodes**
* Based on **Pod scheduling demand**

> This is **NOT** the same as HPA (Pod autoscaling).

---

### Enable autoscaling on a node pool

```bash
gcloud container node-pools update default-pool \
  --cluster=my-cluster \
  --region=us-central1 \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=5
```

**Exam signals**

* “Pods pending due to insufficient CPU”
* “Cluster should scale automatically”

---

## 8️⃣ Node autoscaling vs Pod autoscaling (EXAM TRAP)

| Feature                             | Scales |
| ----------------------------------- | ------ |
| **Node pool autoscaling**           | Nodes  |
| **Horizontal Pod Autoscaler (HPA)** | Pods   |

> **Exam rule:**
> If Pods can’t schedule → **node pool autoscaling**

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Add GPU capacity without affecting existing workloads”

✅ **Create a new GPU node pool**

---

### Scenario 2

> “Reduce costs for batch workloads”

✅ **Spot node pool + autoscaling**

---

### Scenario 3

> “Pods stuck in Pending (Insufficient CPU)”

✅ **Enable or increase node pool autoscaling**

---

## 10️⃣ Common ACE exam traps

❌ Trying to change machine type of an existing pool
❌ Mixing critical and batch workloads in one pool
❌ Confusing node autoscaling with HPA
❌ Deleting a pool before draining workloads

---

## 🔑 One-line ACE memory hooks

* **Node pool = node type**
* **Multiple pools = flexibility**
* **Pending Pods = scale nodes**
* **Autoscaling nodes ≠ autoscaling Pods**

---
 
