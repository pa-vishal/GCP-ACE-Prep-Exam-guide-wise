### **Section 2.1 – Launching a compute instance**

*(availability policy, SSH keys)*

![Image](https://docs.cloud.google.com/static/compute/images/instance-lifecycle.png)

![Image](https://media2.dev.to/dynamic/image/width%3D800%2Cheight%3D%2Cfit%3Dscale-down%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j6ppnpx0vnd4jks6wu9.png)

![Image](https://docs.cloud.google.com/static/compute/docs/connect/ssh-best-practices/flowchart.svg)

This bullet is about **creating VMs correctly the first time**. The ACE exam tests whether you understand **availability behavior**, **access methods**, and **safe defaults**—not deep OS tuning.

---

## 1️⃣ What the ACE exam is actually testing

You’re expected to know how to:

* Launch a VM with the **right availability behavior**
* Choose **how users access** the VM (SSH)
* Avoid common mistakes that break access or HA

> **Exam mindset:** “If I create a VM this way, what happens during maintenance or failure—and can I still log in?”

---

## 2️⃣ Availability policy (VERY exam-relevant)

### What it controls

* What happens to the VM during **host maintenance**
* Whether the VM is **restarted automatically** after a crash
* Whether the VM is **preemptible / Spot**

### Key settings you must recognize

#### 🔹 On host maintenance

* **Migrate (default)** → Live migration during maintenance
* **Terminate** → VM stops during maintenance

**Exam signals**

* “Zero downtime during maintenance” → **Migrate**
* “Uses GPUs / special hardware” → **Terminate** (live migration not supported)

---

#### 🔹 Automatic restart

* **On** → VM restarts after crash
* **Off** → VM stays stopped

**Exam signals**

* “Production workload” → **On**
* “Batch job” → **Off** (often paired with Spot)

---

#### 🔹 Spot (Preemptible) VMs

* Cheap
* Can stop **anytime**
* No SLA

**Exam signals**

* “Fault-tolerant”
* “Batch processing”
* “Cost-sensitive”

---

## 3️⃣ SSH access to Compute Engine (EXAM FAVORITE)

### Three common SSH methods

#### ✅ A. OS Login (BEST PRACTICE)

* Uses IAM for SSH
* Centralized access control
* No manual key management

**Exam signals**

* “Centralized access”
* “Use IAM for SSH”
* “Avoid managing keys”

```bash
gcloud compute project-info add-metadata \
  --metadata enable-oslogin=TRUE
```

---

#### B. Project-wide SSH keys

* Stored in project metadata
* Applies to all VMs

**Exam signals**

* Small teams
* Simpler setups

---

#### C. Instance-specific SSH keys

* Stored on the VM
* Least scalable

**Exam signals**

* One-off access
* Temporary VM

---

## 4️⃣ Launching a VM via CLI (ACE-level)

### Basic VM creation

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium
```

---

### VM with availability options

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --maintenance-policy=MIGRATE \
  --restart-on-failure
```

---

### Spot VM

```bash
gcloud compute instances create my-spot-vm \
  --zone=us-central1-a \
  --provisioning-model=SPOT
```

---

## 5️⃣ Networking & access basics (quick exam reminders)

* VM needs:

  * **Firewall rule** allowing SSH (tcp:22)
  * Either:

    * External IP **or**
    * IAP / bastion (advanced)

> **Exam trap:**
> VM exists but cannot SSH → usually **firewall** or **SSH key/OS Login** issue

---

## 6️⃣ Common ACE exam scenarios

### Scenario 1

> “VM must survive host maintenance without downtime”

✅ **Live migration (MIGRATE)**

---

### Scenario 2

> “Batch processing job, cost sensitive”

✅ **Spot VM** + automatic restart off

---

### Scenario 3

> “Centralized, auditable SSH access”

✅ **OS Login**

---

### Scenario 4

> “VM restarts automatically after crash”

✅ **Automatic restart enabled**

---

## 7️⃣ Common exam traps

❌ Choosing Spot for production stateful apps
❌ Forgetting GPUs disable live migration
❌ Managing SSH keys manually when OS Login is requested
❌ Ignoring firewall rules for SSH

---

## 🔑 One-line ACE memory hooks

* **Migrate = uptime**
* **Terminate = special hardware**
* **Spot = cheap & interruptible**
* **OS Login = IAM-based SSH**

---
 
