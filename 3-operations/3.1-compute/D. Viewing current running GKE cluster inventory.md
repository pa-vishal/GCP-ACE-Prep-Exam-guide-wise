
### **Section 3.1 – Managing compute resources**

#### **Viewing current running GKE cluster inventory**

*(nodes, Pods, Services)*

![Image](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-architecture.svg)

![Image](https://leading-bell-3e1c02e64d.media.strapiapp.com/Wa3_f4_9988b95743.png)

![Image](https://21854652.fs1.hubspotusercontent-na1.net/hubfs/21854652/Imported_Blog_Media/gke-workload-identity.png)

This bullet tests whether you can **quickly inspect what’s running inside a GKE cluster** and **separate infrastructure problems from application problems**. On the ACE exam, this is classic **triage**: before fixing anything, **see the inventory**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* View **nodes**, **Pods**, and **Services**
* Understand **scope** (cluster-wide vs namespace)
* Use **kubectl** correctly after authentication
* Interpret basic status fields

> **Exam mindset:**
> *“Is the problem the cluster, the nodes, or the workload?”*

---

## 2️⃣ Prerequisite (often implied on the exam)

Before you can view inventory:

* You must have **kubectl installed**
* You must have fetched **cluster credentials**

```bash
gcloud container clusters get-credentials my-cluster \
  --region=us-central1
```

> **Exam trap:**
> kubectl installed but not configured → inventory commands fail

---

## 3️⃣ Viewing nodes (INFRASTRUCTURE LAYER)

### What nodes represent

* Worker machines running Pods
* Backed by Compute Engine VMs (Standard)
* Fully managed by Google (Autopilot)

### List nodes

```bash
kubectl get nodes
```

**Key fields to recognize**

* `STATUS` → Ready / NotReady
* `ROLES`
* `VERSION`

> **Exam signal:**
> Pods failing across many services → check **nodes first**

---

## 4️⃣ Viewing Pods (WORKLOAD LAYER)

### What Pods represent

* Smallest deployable unit
* One or more containers

### List Pods (current namespace)

```bash
kubectl get pods
```

### List Pods across all namespaces

```bash
kubectl get pods --all-namespaces
```

**Key status values**

* `Running`
* `Pending`
* `CrashLoopBackOff`
* `ImagePullBackOff`

> **Exam signal:**
> “App not responding” → check **Pod status**

---

## 5️⃣ Viewing Services (NETWORKING LAYER)

### What Services represent

* Stable networking endpoints for Pods
* Abstract Pod IP churn

### List Services

```bash
kubectl get services
```

**Key types**

* `ClusterIP` – internal only
* `LoadBalancer` – external access
* `NodePort` – exposed via node IPs

> **Exam signal:**
> “Pods running but app unreachable” → check **Service**

---

## 6️⃣ Namespace awareness (VERY important)

By default:

* kubectl shows resources in the **current namespace**

### Check current namespace

```bash
kubectl config view --minify | grep namespace
```

### List resources in a specific namespace

```bash
kubectl get pods -n my-namespace
```

> **Exam trap:**
> “No Pods found” → wrong namespace

---

## 7️⃣ Inventory layers (MENTAL MODEL – MEMORIZE)

```
Cluster
 ├── Nodes (compute)
 ├── Pods (workloads)
 └── Services (networking)
```

Troubleshooting order:

1. Nodes
2. Pods
3. Services

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Application is down in GKE”

✅ First steps:

* `kubectl get nodes`
* `kubectl get pods`
* `kubectl get services`

---

### Scenario 2

> “Cluster exists but no workloads appear”

✅ Likely cause:

* Wrong namespace

---

### Scenario 3

> “Pods stuck in Pending”

✅ Likely causes:

* Insufficient node capacity
* Scheduling constraints

---

## 9️⃣ Common ACE exam traps

❌ Using `gcloud` instead of `kubectl` for workload inventory
❌ Forgetting namespaces
❌ Assuming Autopilot nodes are visible/manageable
❌ Debugging Services before Pods

---

## 🔑 One-line ACE memory hooks

* **Nodes = compute**
* **Pods = workloads**
* **Services = access**
* **Wrong namespace = empty results**

---
 
