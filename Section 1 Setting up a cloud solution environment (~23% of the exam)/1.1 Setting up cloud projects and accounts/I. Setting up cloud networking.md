
### **Section 1.1 – Setting up cloud networking**

![Image](https://d33wubrfki0l68.cloudfront.net/57750035ef2c7221ce9bdece3154ff503d5fdc9c/a0271/gcpimages/02-architecture/00-public-private-subnet.png)

![Image](https://docs.cloud.google.com/static/architecture/images/vpc-bps-native-firewall-rules.svg)

![Image](https://media2.dev.to/dynamic/image/width%3D1000%2Cheight%3D420%2Cfit%3Dcover%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzplra525nwe9j4x6az2y.png)

This bullet is **core ACE material**. Networking is not tested deeply, but you are expected to **set up the right primitives correctly** and recognize **default vs custom behavior**.

---

## 1️⃣ What “setting up cloud networking” means (exam framing)

At the ACE level, this means being able to:

* Create and configure a **VPC network**
* Design **subnets** correctly
* Understand **global vs regional** scope
* Enable basic connectivity for compute and managed services

> **Exam mindset:**
> You are wiring the foundation so workloads can communicate **securely and predictably**.

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you can:

### ✅ Choose **default VPC vs custom VPC**

### ✅ Create subnets with correct **region & IP ranges**

### ✅ Understand **global VPC / regional subnet** behavior

### ✅ Recognize when **Shared VPC** is appropriate (conceptually)

### ❌ What it does NOT test

* Advanced routing protocols
* Deep firewall optimization
* BGP tuning
* Packet-level debugging

---

## 3️⃣ Core networking components you must know

### 🌐 VPC Network

* **Global** resource
* Container for subnets, routes, firewall rules

Two types:

* **Default VPC**
* **Custom VPC**

---

### 📍 Subnets

* **Regional**
* IP ranges are **CIDR blocks**
* Can be expanded (but not shrunk)

---

### 🔥 Firewall Rules

* Apply at VPC level
* Control ingress/egress
* Required even for “internal” access

---

### 🧭 Routes

* Control traffic flow
* Automatically created for subnets
* Can be customized

---

## 4️⃣ Default VPC vs Custom VPC (EXAM FAVORITE)

| Feature          | Default VPC    | Custom VPC   |
| ---------------- | -------------- | ------------ |
| Auto-created     | ✅ Yes          | ❌ No         |
| Subnets          | One per region | User-defined |
| Firewall rules   | Open-ish       | Explicit     |
| Production-ready | ❌ No           | ✅ Yes        |

> **Exam rule**
>
> * Learning / quick start → Default VPC
> * Production / control → Custom VPC

---

## 5️⃣ Creating a custom VPC (CLI)

### 🔹 Create a VPC (custom mode)

```bash
gcloud compute networks create my-vpc \
  --subnet-mode=custom
```

---

### 🔹 Create a subnet

```bash
gcloud compute networks subnets create my-subnet \
  --network=my-vpc \
  --region=us-central1 \
  --range=10.10.0.0/24
```

---

### 🔹 List networks

```bash
gcloud compute networks list
```

---

### 🔹 List subnets

```bash
gcloud compute networks subnets list
```

---

## 6️⃣ Firewall rules (basic but exam-relevant)

### Example: allow SSH

```bash
gcloud compute firewall-rules create allow-ssh \
  --network=my-vpc \
  --allow=tcp:22 \
  --source-ranges=0.0.0.0/0
```

> **Exam warning:**
> No firewall rule = **no traffic**, even inside VPC

---

## 7️⃣ Shared VPC (conceptual only for Section 1.1)

**Shared VPC** allows:

* Central networking project (host)
* Other projects (service projects) use the same VPC

**When exam expects Shared VPC**

* Multiple teams
* Centralized network control
* Separation of duties

> You are **not expected** to configure Shared VPC deeply at this stage — only recognize **when it’s the right choice**.

---

## 8️⃣ Connectivity basics (exam awareness)

* VMs in same VPC → private IP communication works
* Different VPCs → need **VPC Peering**
* On-prem → **Cloud VPN / Interconnect** (high level)

---

## 9️⃣ Common exam scenarios

### Scenario 1

> “VMs cannot communicate internally”

✅ Root cause:

* Missing firewall rule

---

### Scenario 2

> “Production network must restrict IP ranges”

✅ Correct choice:

* Custom VPC with explicit subnets

---

### Scenario 3

> “Multiple projects need same network”

✅ Correct choice:

* Shared VPC

---

## 10️⃣ Common exam traps

❌ Assume default VPC is secure
❌ Forget subnets are regional
❌ Think firewall rules are optional
❌ Confuse VPC (global) with subnet (regional)

---

## 🔑 One-line exam memory hook

> **VPC is global, subnets are regional, firewalls control everything**

--- 
