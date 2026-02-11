### **Section 2.1 – Configuring VM Manager**

![Image](https://miro.medium.com/1%2A2rbe2_3EMYBiRCSqsUo0-w.png)

![Image](https://media2.dev.to/dynamic/image/width%3D800%2Cheight%3D%2Cfit%3Dscale-down%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7taov33ojel9nr5d8wz8.jpg)

This bullet tests whether you understand **how Google Cloud manages OS-level operations at scale** for Compute Engine VMs—**patching, inventory, and compliance**—without logging into each VM.

---

## 1️⃣ What VM Manager is (exam framing)

**VM Manager** is a suite of services that lets you **manage the OS state of VMs centrally**, including:

* OS **inventory** (packages, OS version)
* **Patch management** (schedule updates)
* **Compliance visibility**

> **Key idea:**
> VM Manager = *fleet-level OS management*, not application management.

---

## 2️⃣ What the ACE exam actually tests

You should be able to:

### ✅ Identify **when VM Manager is the right tool**

* Many VMs
* Need consistent OS patching
* Want visibility into installed packages

### ✅ Know the **prerequisites**

* VM Manager APIs enabled
* Ops Agent (or OS Config agent) present

### ❌ What it does NOT test

* Writing custom patch scripts
* Kernel-level tuning
* Application patching

---

## 3️⃣ Core VM Manager capabilities (must know)

### 🧾 A. OS Inventory

* Collects:

  * OS version
  * Installed packages
  * Package versions
* Used for:

  * Auditing
  * Vulnerability tracking

**Exam signals**

* “See what packages are installed”
* “Inventory of VMs”

---

### 🔄 B. Patch management

* Apply OS patches:

  * On-demand
  * On a schedule
* Supports:

  * Reboot control
  * Maintenance windows

**Exam signals**

* “Apply security patches across VMs”
* “Automate OS updates”

---

### 🛡️ C. Compliance reporting

* Shows:

  * Patch compliance status
  * Which VMs are out of date

**Exam signals**

* “Which VMs are missing patches?”

---

## 4️⃣ How VM Manager works (mental model)

```
Project
 └── VM Manager
      ├── OS Config API
      ├── Agent on VM
      └── Inventory / Patch jobs
```

* Google manages orchestration
* VMs report state via agent

---

## 5️⃣ Prerequisites (VERY exam-relevant)

### Required:

* **OS Config API** enabled
* **Ops Agent** (or OS Config agent) installed on VMs
* Supported OS (most Linux distros, Windows)

> **Exam trap:**
> VM Manager won’t work if the agent is missing.

---

## 6️⃣ Enabling required APIs (CLI)

```bash
gcloud services enable osconfig.googleapis.com \
  --project=my-project
```

(Ops Agent is often installed separately, but exam expects you to know it’s required.)

---

## 7️⃣ Patch jobs (conceptual – exam level)

You can:

* Target:

  * All VMs
  * VMs by label
  * Specific zones
* Control:

  * Reboot behavior
  * Patch window

> You are **not tested** on exact patch job syntax—only on **capability**.

---

## 8️⃣ VM Manager vs other tools (exam clarity)

| Tool       | Purpose                 |
| ---------- | ----------------------- |
| VM Manager | OS inventory & patching |
| Ops Agent  | Metrics & logs          |
| SSH        | Manual access           |
| IAM        | Permissions             |

> **VM Manager ≠ Monitoring**

---

## 9️⃣ Real ACE-style scenarios

### Scenario 1

> “Security team wants to ensure all VMs have latest OS patches”

✅ **VM Manager (Patch management)**

---

### Scenario 2

> “List installed packages across all VMs”

✅ **VM Manager (OS Inventory)**

---

### Scenario 3

> “Patch VMs without logging in individually”

✅ **VM Manager**

---

## 10️⃣ Common ACE exam traps

❌ Thinking VM Manager manages applications
❌ Forgetting agent/API prerequisites
❌ Using SSH for fleet-wide patching
❌ Confusing VM Manager with Ops Agent

---

## 🔑 One-line ACE memory hook

> **VM Manager = OS-level control at scale**

---
 
