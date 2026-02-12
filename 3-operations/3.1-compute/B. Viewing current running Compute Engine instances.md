### **Section 3.1 – Managing compute resources**

#### **Viewing current running Compute Engine instances**

![Image](https://docs.cloud.google.com/static/compute/images/operations_console.png)

![Image](https://i.sstatic.net/oRIFi.jpg)

![Image](https://docs.cloud.google.com/static/scheduler/docs/images/scheduling-instances-architecture-pubsub.png)

This bullet tests whether you can **quickly assess what is running, where it’s running, and in what state**. On the ACE exam, this often appears as **triage**: “What’s running right now?” before deciding what to fix.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* List **current VMs** in a project
* Identify **state** (RUNNING, TERMINATED)
* Understand **scope** (project, zone)
* Choose **CLI vs Console** appropriately

> **Exam mindset:**
> *“Before troubleshooting or changing anything—what’s actually running?”*

---

## 2️⃣ Where you can view running instances

### 🖥️ A. Cloud Console (visual, quick checks)

**What you see**

* VM name
* Status (Running / Stopped)
* Zone
* Internal / external IPs
* Machine type

**Use when**

* Quick visual inspection
* Small environments
* Verifying status before/after changes

> **Exam reality:**
> Console is acceptable—but **CLI is often implied** in ops scenarios.

---

### ⌨️ B. gcloud CLI (MOST TESTED)

#### List all instances in the current project

```bash
gcloud compute instances list
```

**Output includes**

* NAME
* ZONE
* MACHINE_TYPE
* INTERNAL_IP
* EXTERNAL_IP
* STATUS

---

#### Filter only running instances

```bash
gcloud compute instances list \
  --filter="status=RUNNING"
```

> **Exam signal:**
> “View currently running instances” → **filter by status**

---

#### List instances in a specific zone

```bash
gcloud compute instances list \
  --filter="zone:us-central1-a"
```

---

## 3️⃣ Understanding VM states (MUST know)

| State                      | Meaning                    |
| -------------------------- | -------------------------- |
| **RUNNING**                | VM is active and billable  |
| **TERMINATED**             | VM stopped (disk persists) |
| **PROVISIONING / STAGING** | VM starting                |
| **STOPPING**               | VM shutting down           |

> **Exam trap:**
> TERMINATED VMs **do not incur CPU charges**, but disks still cost money.

---

## 4️⃣ Scope & permissions (exam awareness)

* VM listing is:

  * **Project-scoped**
  * Requires:

    * `compute.instances.list` permission
* Project Viewer can list instances
* Billing access is **not required** just to view

> **Exam signal:**
> “User can’t see instances” → missing IAM permission

---

## 5️⃣ Common ACE exam scenarios

### Scenario 1

> “Operations team wants to see which VMs are currently running”

✅ **gcloud compute instances list --filter="status=RUNNING"**

---

### Scenario 2

> “Identify which VMs are incurring compute charges”

✅ **RUNNING instances only**

---

### Scenario 3

> “VM exists but cannot be connected to”

✅ First step:

* Confirm **status = RUNNING**

---

## 6️⃣ Common ACE exam traps

❌ Forgetting to filter by status
❌ Assuming stopped VMs are deleted
❌ Confusing project scope with organization scope
❌ Thinking billing permission is needed to view VMs

---

## 🔑 One-line ACE memory hooks

* **RUNNING = billing**
* **TERMINATED ≠ deleted**
* **List first, troubleshoot second**

---
 
