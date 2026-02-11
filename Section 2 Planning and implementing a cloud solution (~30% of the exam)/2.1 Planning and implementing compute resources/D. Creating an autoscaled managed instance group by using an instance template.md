 ### **Section 2.1 – Creating an autoscaled managed instance group (MIG) using an instance template**

![Image](https://docs.cloud.google.com/static/compute/docs/tutorials/images/globally-autoscaling-compute-engine-architecture.png)

![Image](https://docs.cloud.google.com/build/images/devops.png)

![Image](https://cloud.google.com/compute/images/mig-overview.svg)

This bullet tests whether you understand **how Compute Engine achieves scale and high availability**. The ACE exam is not asking you to design complex autoscaling policies—it’s checking that you know **the required building blocks and when to use them**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Recognize that **autoscaling requires a Managed Instance Group**
* Know that **instance templates are mandatory**
* Choose **zonal vs regional MIGs** correctly
* Understand **what autoscaling reacts to** (CPU, load)

> **Exam mindset:**
> *“If traffic increases or a VM fails, what automatically replaces or scales it?”*

---

## 2️⃣ Core concepts (must be automatic)

### 🧱 Instance Template

* A **blueprint** for VMs
* Defines:

  * Machine type
  * Boot disk
  * Image
  * Startup script
  * Network settings
* **Immutable** (you create a new version to change it)

> **Hard rule:**
> You **cannot** create a MIG without an instance template.

---

### 👥 Managed Instance Group (MIG)

* A group of **identical VMs**
* Managed by Google
* Supports:

  * Autohealing
  * Autoscaling
  * Rolling updates

Two types:

* **Zonal MIG**
* **Regional MIG**

---

## 3️⃣ Zonal vs Regional MIG (EXAM FAVORITE)

| Type         | Behavior                | Use when                  |
| ------------ | ----------------------- | ------------------------- |
| Zonal MIG    | VMs in one zone         | Cost-sensitive, simple HA |
| Regional MIG | VMs spread across zones | Survive zone failure      |

**Exam signals**

* “High availability” → **Regional MIG**
* “Single zone is acceptable” → **Zonal MIG**

---

## 4️⃣ Autoscaling basics (ACE level)

Autoscaling can be based on:

* **CPU utilization** (most common)
* Load balancer metrics
* Custom metrics (not deeply tested)

**Key idea**

* Autoscaler **adds/removes VMs**
* You define:

  * Minimum instances
  * Maximum instances
  * Target utilization

---

## 5️⃣ Creating an instance template (CLI)

```bash
gcloud compute instance-templates create web-template \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --tags=http-server
```

---

## 6️⃣ Creating a Managed Instance Group

### Zonal MIG

```bash
gcloud compute instance-groups managed create web-mig \
  --base-instance-name=web \
  --template=web-template \
  --size=2 \
  --zone=us-central1-a
```

---

### Regional MIG

```bash
gcloud compute instance-groups managed create web-mig \
  --base-instance-name=web \
  --template=web-template \
  --size=2 \
  --region=us-central1
```

---

## 7️⃣ Enabling autoscaling

```bash
gcloud compute instance-groups managed set-autoscaling web-mig \
  --max-num-replicas=10 \
  --min-num-replicas=2 \
  --target-cpu-utilization=0.6 \
  --region=us-central1
```

---

## 8️⃣ Health checks & autohealing (exam awareness)

* MIGs use **health checks**
* Unhealthy VMs are:

  * Automatically recreated
* Commonly paired with:

  * Load balancers

> **Exam signal:**
> “Replace failed VM automatically” → **MIG + health check**

---

## 9️⃣ Real ACE-style scenarios

### Scenario 1

> “Application must scale automatically based on traffic”

✅ **Managed Instance Group with autoscaling**

---

### Scenario 2

> “VMs must be identical and auto-recreated if they fail”

✅ **MIG + instance template**

---

### Scenario 3

> “Workload must survive a zone failure”

✅ **Regional MIG**

---

## 10️⃣ Common ACE exam traps

❌ Trying to autoscale individual VMs
❌ Forgetting instance templates
❌ Using zonal MIG when zone failure must be tolerated
❌ Thinking MIGs replace backups

---

## 🔑 One-line ACE memory hooks

* **Template = blueprint**
* **MIG = scale + heal**
* **Regional MIG = zone-level HA**

--- 
