### **Section 3.3 – Managing networking resources**

#### **Adding a subnet to an existing VPC**

![Image](https://d33wubrfki0l68.cloudfront.net/57750035ef2c7221ce9bdece3154ff503d5fdc9c/a0271/gcpimages/02-architecture/00-public-private-subnet.png)

![Image](https://miro.medium.com/1%2A6HWT7WGREFABwDf8poEqCQ.jpeg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/VPC_network_subset.max-1700x1700.png)

This bullet tests whether you understand **how VPCs and subnets actually work in Google Cloud** and whether you can **extend a network safely without breaking existing workloads**. On the ACE exam, this often appears in **growth or multi-region expansion scenarios**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Add a **new subnet** to an **existing VPC**
* Understand **global VPC vs regional subnets**
* Choose **CIDR ranges correctly**
* Avoid conflicts and downtime

> **Exam mindset:**
> *“The VPC already exists—how do I extend it to a new region or workload?”*

---

## 2️⃣ Core networking facts (MUST KNOW)

### VPC vs Subnet

* **VPC network**: **Global**
* **Subnet**: **Regional**

This means:

* One VPC can have **multiple subnets**
* Each subnet lives in **exactly one region**
* Subnets **do not overlap**

> **ACE rule:**
> You **do not create a new VPC** just to add a subnet.

---

## 3️⃣ When you add a subnet (EXAM SCENARIOS)

Add a subnet when:

* Expanding to a **new region**
* Separating workloads (prod / dev)
* Needing a **new IP range**
* Supporting new services (GKE, Cloud Run connectors, etc.)

**Exam signals**

* “Expand to europe-west1”
* “New workload needs IPs”
* “Avoid changing existing subnets”

---

## 4️⃣ CIDR planning (VERY IMPORTANT)

### Rules you must follow

* CIDR ranges **must not overlap**
* Choose size based on:

  * VM count
  * GKE Pods (if applicable)
* Subnet CIDR:

  * Can be **expanded later**
  * Cannot be shrunk

> **ACE trap:**
> Overlapping CIDRs = subnet creation fails.

---

## 5️⃣ Adding a subnet (CLI – exam-relevant)

### Create a new subnet in an existing VPC

```bash
gcloud compute networks subnets create app-subnet-eu \
  --network=my-vpc \
  --region=europe-west1 \
  --range=10.20.0.0/24
```

What this does:

* Keeps the **same VPC**
* Adds a **new regional subnet**
* Does **not impact existing subnets**

---

## 6️⃣ What does NOT change when adding a subnet

Adding a subnet:

* ❌ Does NOT cause downtime
* ❌ Does NOT affect existing VMs
* ❌ Does NOT change firewall rules automatically

Firewall rules:

* Apply at the **VPC level**
* May need updates to allow traffic to/from the new subnet

> **Exam signal:**
> “VMs in new subnet can’t communicate” → firewall rules

---

## 7️⃣ Adding subnet vs expanding subnet (EXAM TRAP)

| Action                 | Use when                   |
| ---------------------- | -------------------------- |
| **Add new subnet**     | New region or isolation    |
| **Expand subnet CIDR** | Same region, need more IPs |

> **ACE rule:**
> You **cannot** shrink a subnet, only expand it.

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Deploy workloads in a new region using the same network”

✅ **Add a new subnet to the existing VPC**

---

### Scenario 2

> “Existing subnet ran out of IPs in us-central1”

❌ Add new subnet (wrong)
✅ **Expand the existing subnet CIDR**

---

### Scenario 3

> “New subnet added but traffic is blocked”

✅ Likely cause:

* Firewall rules not updated

---

## 9️⃣ Common ACE exam traps

❌ Creating a new VPC instead of a subnet
❌ Overlapping CIDR ranges
❌ Forgetting subnets are regional
❌ Expecting firewall rules to auto-adjust
❌ Shrinking subnet CIDRs (not allowed)

---

## 🔑 One-line ACE memory hooks

* **VPC = global**
* **Subnet = regional**
* **No overlap**
* **Adding subnet = no downtime**
* **Firewall rules may need updates**

---
 
