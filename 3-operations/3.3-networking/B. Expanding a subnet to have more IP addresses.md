### **Section 3.3 – Managing networking resources**

#### **Expanding a subnet to have more IP addresses**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/VPC_network_subset.max-1700x1700.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/subnetwork-2.max-1200x1200.png)

![Image](https://media.licdn.com/dms/image/v2/D4D12AQGcldNje_SZWw/article-cover_image-shrink_720_1280/B4DZjNIm7uG8AI-/0/1755788246392?e=2147483647\&t=Y6Ochsjbp_G--b0jmyzPR12dvlrqSGJQxrFN5iEoXZ0\&v=beta)

This bullet is a **classic ACE exam trap**. The exam tests whether you know **the one allowed way to fix IP exhaustion in Google Cloud**—and the **one thing you cannot do**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Recognize **IP exhaustion symptoms**
* Know that subnets **can be expanded but never shrunk**
* Expand a subnet **without downtime**
* Choose subnet expansion vs adding a new subnet correctly

> **Exam mindset:**
> *“We’re out of IPs—what’s the fastest, safest fix?”*

---

## 2️⃣ Core rule (MUST MEMORIZE)

> **Google Cloud subnets can be expanded, but they can never be reduced.**

This rule appears **directly or indirectly** in multiple ACE questions.

---

## 3️⃣ When subnet expansion is the correct answer

Expand a subnet when:

* You are in the **same region**
* Existing resources depend on the subnet
* You need **more IPs quickly**
* You want **zero downtime**

**Exam signals**

* “Subnet ran out of IPs”
* “Cannot create new VM”
* “Pods failing due to IP exhaustion”
* “Do not disrupt existing workloads”

---

## 4️⃣ What subnet expansion does (and does not do)

### ✅ What it does

* Increases available IP addresses
* Keeps the **same subnet**
* Does **not restart** existing VMs
* Works immediately

### ❌ What it does NOT do

* Does not change existing IPs
* Does not shrink the subnet
* Does not affect other subnets
* Does not automatically update firewall rules

> **ACE trap:**
> Firewall rules may still block traffic if CIDR-based rules are too narrow.

---

## 5️⃣ CIDR expansion rules (VERY IMPORTANT)

You can only:

* Expand to a **larger CIDR**
* Expand **within the same address block**

Example:

* `10.10.0.0/24` → `10.10.0.0/23` ✅
* `10.10.0.0/24` → `10.10.1.0/24` ❌

> **ACE rule:**
> Expansion must be a **superset of the original range**.

---

## 6️⃣ Expanding a subnet (CLI – exam-relevant)

### Update subnet IP range

```bash
gcloud compute networks subnets expand-ip-range app-subnet \
  --region=us-central1 \
  --prefix-length=23
```

What this does:

* Expands subnet from `/24` to `/23`
* Immediately adds more usable IPs
* Does **not** interrupt traffic

---

## 7️⃣ Subnet expansion vs adding a new subnet (EXAM FAVORITE)

| Problem                      | Correct action    |
| ---------------------------- | ----------------- |
| IP exhaustion in same region | **Expand subnet** |
| Need new region              | Add new subnet    |
| Isolate workloads            | Add new subnet    |
| Existing subnet in use       | Expand subnet     |

> **ACE trap:**
> Adding a new subnet does **not** fix IP exhaustion for existing resources.

---

## 8️⃣ GKE-specific exam signal

If the question mentions:

* GKE Pods failing to schedule
* IP address exhaustion
* Alias IP ranges

✅ **Subnet expansion is usually the fix**

> You are **not expected** to redesign IP ranges on the exam—just expand.

---

## 9️⃣ Common ACE exam traps

❌ Trying to shrink a subnet
❌ Creating a new VPC
❌ Adding a new subnet instead of expanding
❌ Changing CIDR blocks incorrectly
❌ Expecting downtime during expansion

---

## 🔑 One-line ACE memory hooks

* **Subnets only grow**
* **Expand = no downtime**
* **Same region = expand**
* **Different region = new subnet**
* **CIDR must be a superset**

---
 
