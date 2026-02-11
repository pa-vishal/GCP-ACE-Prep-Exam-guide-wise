### **Section 2.3 – Creating a VPC with subnets**

*(custom mode VPC, Shared VPC)*

![Image](https://d33wubrfki0l68.cloudfront.net/57750035ef2c7221ce9bdece3154ff503d5fdc9c/a0271/gcpimages/02-architecture/00-public-private-subnet.png)

![Image](https://docs.cloud.google.com/static/architecture/images/vpc-bps-multi-nic-shared-vpc.png)

![Image](https://miro.medium.com/1%2A6HWT7WGREFABwDf8poEqCQ.jpeg)

This bullet is **core networking foundation**. The ACE exam tests whether you understand **how Google Cloud networking is structured**, **when to choose custom mode**, and **when Shared VPC is the right architectural choice**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Create a **VPC** and **subnets** correctly
* Understand **global VPC vs regional subnets**
* Choose **custom mode** over default for production
* Recognize **Shared VPC** use cases

> **Exam mindset:**
> *“Who owns the network, where do IPs live, and who is allowed to use it?”*

---

## 2️⃣ Core concepts you MUST lock in

### 🌐 VPC network

* **Global** resource
* Container for:

  * Subnets
  * Routes
  * Firewall rules
* Does **not** live in a region

### 📍 Subnets

* **Regional**
* Define IP ranges (CIDR)
* Live **inside a VPC**
* Can be expanded (not shrunk)

> **Exam trap:**
> VPC = global, subnet = regional

---

## 3️⃣ Default VPC vs Custom mode VPC (VERY exam-relevant)

### ❌ Default VPC

* Automatically created
* One subnet per region
* Broad firewall rules
* Not production-friendly

**Use when**

* Learning
* Quick tests
* Demos

---

### ✅ Custom mode VPC (EXAM DEFAULT CHOICE)

* You create subnets explicitly
* Full control over:

  * Regions
  * CIDR ranges
  * Firewall exposure

**Use when**

* Production workloads
* Security matters
* IP planning is required

> **ACE rule:**
> If the question says *production*, *secure*, or *controlled* → **Custom VPC**

---

## 4️⃣ Creating a custom VPC and subnet (CLI – exam-relevant)

### Create a custom-mode VPC

```bash
gcloud compute networks create my-vpc \
  --subnet-mode=custom
```

---

### Create a subnet

```bash
gcloud compute networks subnets create app-subnet \
  --network=my-vpc \
  --region=us-central1 \
  --range=10.10.0.0/24
```

---

### List networks and subnets

```bash
gcloud compute networks list
gcloud compute networks subnets list
```

---

## 5️⃣ Shared VPC (BIG exam concept)

### What Shared VPC is

Shared VPC lets you:

* Create a **host project** that owns the VPC
* Attach **service projects** that deploy resources
* Centralize **network control**

```
Host Project (VPC owner)
 ├── Subnets
 ├── Firewall rules
 └── Routes
        ↑
Service Projects
 └── VMs, GKE, Cloud Run (via connectors)
```

---

## 6️⃣ When the ACE exam expects Shared VPC

Use Shared VPC when:

* Multiple teams/projects
* Centralized networking team
* Separation of duties
* Strong governance

**Exam signals**

* “Central networking team”
* “Multiple projects share same network”
* “Control networking centrally”

---

## 7️⃣ What Shared VPC is NOT

❌ Not VPC Peering
❌ Not a VPN
❌ Not per-region

> **Exam trap:**
> Shared VPC = **one VPC, many projects**

---

## 8️⃣ IAM implications (exam awareness)

* Host project admins:

  * Control subnets and firewalls
* Service project admins:

  * Deploy resources **into approved subnets**

> **Exam signal:**
> “Teams deploy without controlling the network” → **Shared VPC**

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Production network with tight IP control”

✅ **Custom mode VPC**

---

### Scenario 2

> “Multiple projects must share the same network”

✅ **Shared VPC**

---

### Scenario 3

> “Engineer cannot create VM due to subnet permission”

✅ Missing:

* Shared VPC IAM role on subnet

---

## 10️⃣ Common ACE exam traps

❌ Using default VPC for production
❌ Thinking subnets are global
❌ Confusing Shared VPC with peering
❌ Forgetting to create subnets in custom VPC

---

## 🔑 One-line ACE memory hooks

* **VPC = global**
* **Subnet = regional**
* **Custom VPC = production**
* **Shared VPC = central control**

--- 
