### **Section 3.3 – Managing networking resources**

#### **Reserving static external or internal IP addresses**

![Image](https://miro.medium.com/1%2AW_pESAt3DPtGilWqPpljOg.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AsD90kDhRB6u4oIvVE0rGkw.png)

![Image](https://labresources.whizlabs.com/010c3004937dd6e39b9f2eb128b00d80/ipv4-vs-ipv6-en.webp)

This bullet tests whether you understand **IP address lifecycle and stability** in Google Cloud. The ACE exam frequently frames this as **“my IP keeps changing”** or **“I need a fixed IP for allowlists / DNS”**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Distinguish **ephemeral vs static IPs**
* Reserve **external vs internal** static IPs
* Choose **regional vs global** correctly
* Avoid unnecessary IP charges

> **Exam mindset:**
> *“Does this workload need a stable IP, and who needs to reach it?”*

---

## 2️⃣ Ephemeral vs static IPs (MUST KNOW)

### 🌊 Ephemeral IP

* Assigned automatically
* **Changes** when:

  * VM is stopped and restarted
* No cost when attached

### 📌 Static IP

* Reserved explicitly
* **Does not change**
* Can be attached/detached
* **Costs money when unused**

> **ACE rule:**
> If the IP must not change → **Static IP**

---

## 3️⃣ External vs internal static IPs

### 🌐 External static IP

**Use when**

* Internet-facing services
* DNS records
* Allowlisting from external systems

**Exam signals**

* “Public endpoint”
* “Firewall allowlist”
* “DNS A record”

---

### 🏠 Internal static IP

**Use when**

* Private services inside VPC
* Backend systems
* Fixed internal endpoints

**Exam signals**

* “Internal-only”
* “Private access”
* “No internet exposure”

---

## 4️⃣ Regional vs global IPs (VERY IMPORTANT)

### Regional IPs

* Used by:

  * Compute Engine VMs
  * Network Load Balancers
* Bound to **one region**

### Global IPs

* Used by:

  * HTTP(S) Load Balancers
* Anycast across Google’s edge

> **ACE rule:**
> Global load balancer → **Global static IP**

---

## 5️⃣ Reserving a static external IP (CLI – exam-relevant)

### Regional external IP

```bash
gcloud compute addresses create my-static-ip \
  --region=us-central1
```

### Global external IP

```bash
gcloud compute addresses create my-global-ip \
  --global
```

---

## 6️⃣ Reserving a static internal IP

```bash
gcloud compute addresses create my-internal-ip \
  --region=us-central1 \
  --subnet=my-subnet \
  --addresses=10.10.0.50
```

> **Exam trap:**
> Internal IPs must be **within the subnet CIDR**.

---

## 7️⃣ Attaching a static IP (exam awareness)

### Attach to a VM

* During VM creation, or
* Update VM network interface

> You are **not tested** on the exact attach flags—only that it’s possible.

---

## 8️⃣ Cost implications (EXAM FAVORITE)

* **Unused static IPs incur charges**
* Ephemeral IPs do not incur cost when attached

> **ACE trap:**
> “Reserve just in case” → ❌ leads to unnecessary cost

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “VM’s public IP changes after restart”

✅ **Reserve and attach a static external IP**

---

### Scenario 2

> “Create DNS record for a global web app”

✅ **Global static external IP**

---

### Scenario 3

> “Backend service needs fixed private IP”

✅ **Static internal IP**

---

### Scenario 4

> “Reduce cost when stable IP not required”

✅ **Use ephemeral IP**

---

## 🔟 Common ACE exam traps

❌ Using ephemeral IP when stability is required
❌ Reserving static IPs and forgetting to use them
❌ Using regional IP for global HTTP(S) LB
❌ Assigning internal IP outside subnet range

---

## 🔑 One-line ACE memory hooks

* **Stable = static**
* **Internet = external**
* **Private = internal**
* **Global LB = global IP**
* **Unused static IP = cost**

---
 
