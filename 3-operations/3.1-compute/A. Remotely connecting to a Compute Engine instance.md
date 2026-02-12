### **Section 3.1 – Managing compute resources**

#### **Remotely connecting to a Compute Engine instance**

![Image](https://docs.cloud.google.com/static/compute/docs/connect/ssh-best-practices/flowchart.svg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/enabling_beyondcorp.max-1200x1200.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1358/format%3Awebp/1%2APIv8q2RIZDmBUc8MGzKEqw.png)

This bullet is **very high-yield**. The ACE exam repeatedly tests whether you can **choose the correct remote access method** based on **network exposure, security posture, and permissions**—not whether you can memorize SSH syntax.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify **all supported ways** to connect to a VM
* Choose the **most secure** method when prompted
* Diagnose **why SSH fails**
* Understand **how IAM, firewall rules, and networking interact**

> **Exam mindset:**
> *“Can the user reach the VM, and is it allowed?”*

---

## 2️⃣ Supported remote connection methods (MUST KNOW)

### 🔑 A. SSH using external IP (most basic)

**How it works**

* VM has an **external IP**
* Firewall allows **tcp:22**
* SSH key or OS Login used

**Use when**

* Simple setup
* Dev / test environments
* No strict security constraints

**Exam signals**

* “VM has external IP”
* “Quick access”
* “SSH from laptop”

---

### 🌐 B. SSH via IAP (BEST PRACTICE & EXAM FAVORITE)

**How it works**

* VM **does NOT need an external IP**
* Traffic tunnels through **Identity-Aware Proxy**
* Uses IAM permissions

**Requirements**

* IAP TCP forwarding enabled
* Firewall allows **tcp:22 from IAP IP range**
* User has:

  * `roles/iap.tunnelResourceAccessor`
  * SSH permission (OS Login or key)

**Use when**

* Production environments
* No public IPs allowed
* Secure, auditable access

**Exam signals**

* “No external IP”
* “Secure access”
* “Use IAM-based access”

> **ACE rule:**
> If security is mentioned → **IAP SSH**

---

### 🖥️ C. Browser-based SSH (Console)

**How it works**

* Uses same backend as SSH/IAP
* Launched from Cloud Console

**Use when**

* Troubleshooting
* No local SSH tools available

**Exam reality**

* Treated the same as SSH/IAP conceptually

---

### 🔐 D. OS Login (authentication method, not transport)

**What it controls**

* **WHO** can SSH (via IAM)
* Not **HOW** traffic reaches VM

**Exam signals**

* “Centralized access”
* “Remove user access instantly”
* “Audit SSH access”

> OS Login is often paired with **external IP SSH** or **IAP SSH**

---

## 3️⃣ Required components checklist (EXAM GOLD)

For SSH to work, **ALL must be true**:

| Component                   | Required |
| --------------------------- | -------- |
| VM is running               | ✅        |
| Network path exists         | ✅        |
| Firewall allows tcp:22      | ✅        |
| User has SSH permission     | ✅        |
| Authentication method valid | ✅        |

> **Exam trap:**
> One missing item = connection fails

---

## 4️⃣ CLI connection examples (ACE-level)

### SSH using gcloud (auto-handles keys)

```bash
gcloud compute ssh my-vm \
  --zone=us-central1-a
```

---

### SSH via IAP

```bash
gcloud compute ssh my-vm \
  --zone=us-central1-a \
  --tunnel-through-iap
```

---

## 5️⃣ Firewall rules for SSH (VERY common failure)

### Allow SSH (external IP)

```bash
gcloud compute firewall-rules create allow-ssh \
  --network=my-vpc \
  --direction=INGRESS \
  --rules=tcp:22 \
  --source-ranges=0.0.0.0/0
```

### Allow SSH from IAP

* Source range: `35.235.240.0/20`
* Port: `22`

> **Exam signal:**
> “IAP SSH fails” → missing firewall rule

---

## 6️⃣ Decision table (MEMORIZE)

| Scenario                          | Best method    |
| --------------------------------- | -------------- |
| VM has external IP, simple access | SSH            |
| VM has NO external IP             | IAP SSH        |
| Secure production access          | IAP + OS Login |
| Centralized access control        | OS Login       |
| Quick troubleshooting             | Browser SSH    |

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “VM has no external IP but must be accessed securely”

✅ **IAP SSH**

---

### Scenario 2

> “User removed from IAM should lose SSH immediately”

✅ **OS Login**

---

### Scenario 3

> “SSH times out despite correct credentials”

✅ Likely cause:

* Firewall missing
* Wrong source range
* VM not running

---

## 8️⃣ Common ACE exam traps

❌ Assuming SSH works without firewall rules
❌ Confusing OS Login with network connectivity
❌ Using external IP when security is required
❌ Forgetting IAP needs its own firewall rule

---

## 🔑 One-line ACE memory hooks

* **External IP = simple SSH**
* **No external IP = IAP**
* **Security = IAP + OS Login**
* **SSH fails → check firewall first**

---
 
