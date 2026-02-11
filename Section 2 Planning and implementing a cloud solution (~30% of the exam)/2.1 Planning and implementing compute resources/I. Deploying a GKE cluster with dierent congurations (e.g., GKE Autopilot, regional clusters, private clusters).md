### **Section 2.1 – Deploying a GKE cluster with different configurations**

*(GKE Autopilot, regional clusters, private clusters)*

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/gke_autopilot.max-1800x1800.jpg)

![Image](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-architecture.svg)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AKrDCJ68dUfGcCTsKsk-YvQ.jpeg)

This bullet is **very high-yield**. The ACE exam is testing whether you can **pick the right GKE cluster mode and topology** based on **operations effort, availability, and security**—not whether you can tune Kubernetes internals.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Choose **Autopilot vs Standard**
* Choose **regional vs zonal**
* Know **when to use private clusters**
* Avoid overengineering

> **Exam mindset:**
> *“How much control do I need, and how much reliability/security is required?”*

---

## 2️⃣ GKE Standard vs GKE Autopilot (MOST tested choice)

### ☸️ **GKE Standard**

**What it is**

* You manage:

  * Node pools
  * Node sizes
  * Autoscaling behavior (nodes)
* Google manages the control plane

**Use when**

* You need:

  * Custom node types
  * GPUs
  * DaemonSets with special requirements
  * More control over nodes

**Exam signals**

* “Custom node pools”
* “Specific machine types”
* “More control over cluster”

---

### 🚀 **GKE Autopilot**

**What it is**

* Fully managed Kubernetes
* Google manages:

  * Nodes
  * Scaling
  * Bin packing
* You pay per Pod resources

**Use when**

* You want:

  * Minimal operations
  * Best practices enforced
  * No node management

**Exam signals**

* “Minimize operational overhead”
* “Serverless Kubernetes”
* “No node management”

> **ACE rule:**
> If no node-level customization is required → **Autopilot**

---

## 3️⃣ Zonal vs Regional clusters (AVAILABILITY TEST)

### 🧱 **Zonal cluster**

* Control plane in **one zone**
* Worker nodes in one zone

**Use when**

* Dev / test
* Cost-sensitive
* Zone failure is acceptable

**Exam signals**

* “Development environment”
* “Lower cost”

---

### 🌍 **Regional cluster**

* Control plane replicated across zones
* Worker nodes spread across zones

**Use when**

* Production workloads
* Need **zone failure tolerance**

**Exam signals**

* “High availability”
* “Production cluster”
* “Survive zone failure”

> **Exam rule:**
> Production + HA → **Regional cluster**

---

## 4️⃣ Private GKE clusters (SECURITY TEST)

### What makes a cluster “private”

* Nodes **do not have public IPs**
* Control plane has **private endpoint**
* Access via:

  * VPN
  * Bastion
  * Private networking

### Use when

* Security-sensitive workloads
* Regulatory environments
* No public node exposure allowed

**Exam signals**

* “No public IPs”
* “Private access”
* “Security requirement”

---

## 5️⃣ Decision table (MEMORIZE)

| Requirement        | Best Choice      |
| ------------------ | ---------------- |
| Minimal ops        | GKE Autopilot    |
| Node-level control | GKE Standard     |
| Production HA      | Regional cluster |
| Dev / test         | Zonal cluster    |
| No public node IPs | Private cluster  |

---

## 6️⃣ Creating clusters (CLI – exam-aware)

### GKE Autopilot (regional by default)

```bash
gcloud container clusters create-auto my-autopilot \
  --region=us-central1
```

---

### GKE Standard (zonal)

```bash
gcloud container clusters create my-cluster \
  --zone=us-central1-a
```

---

### Private cluster (conceptual CLI)

```bash
gcloud container clusters create my-private-cluster \
  --enable-private-nodes \
  --master-ipv4-cidr=172.16.0.0/28 \
  --region=us-central1
```

> **ACE note:**
> You are tested on **why**, not on memorizing flags.

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “Kubernetes with minimal operational effort”

✅ **GKE Autopilot**

---

### Scenario 2

> “Production cluster must survive zone failure”

✅ **Regional cluster**

---

### Scenario 3

> “Nodes must not have public IPs”

✅ **Private GKE cluster**

---

### Scenario 4

> “Need GPUs and custom node pools”

✅ **GKE Standard**

---

## 8️⃣ Common ACE exam traps

❌ Choosing Standard when Autopilot fits
❌ Using zonal clusters for production HA
❌ Assuming Autopilot allows node customization
❌ Forgetting private clusters affect access methods

---

## 🔑 One-line ACE memory hooks

* **Autopilot = no nodes to manage**
* **Standard = control**
* **Regional = HA**
* **Private = security**

--- 
