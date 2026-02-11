### **Section 2.3 – Differentiating Network Service Tiers**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/Service-Tiers_v9-18-21_4XW7EzT.max-2000x2000.jpg)

![Image](https://gcpnuggets.com/content/images/2023/06/tiers-choosing.svg)

This bullet is **small in wording but high-yield on the ACE exam**. The exam tests whether you understand **performance vs cost tradeoffs** and **when Premium Tier is required by design**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Differentiate **Premium Tier vs Standard Tier**
* Know which services **require Premium**
* Choose the **cheapest tier that still meets requirements**

> **Exam mindset:**
> *“Does this workload need Google’s global backbone?”*

---

## 2️⃣ The two Network Service Tiers (lock this in)

### 🌍 **Premium Tier**

**What it is**

* Traffic stays on **Google’s global backbone**
* Uses Google’s edge locations
* Lowest latency, highest reliability

**Key characteristics**

* Global anycast IPs
* Best performance
* Higher cost

**Automatically used by**

* Global HTTP(S) Load Balancer
* Global external IPs
* Cloud CDN

**Exam signals**

* “Global users”
* “Low latency worldwide”
* “High availability”
* “Global load balancing”

---

### 🌐 **Standard Tier**

**What it is**

* Traffic uses **public internet**
* Enters Google network at the region
* Lower cost, higher latency

**Key characteristics**

* Regional IPs
* Cost-optimized
* Less predictable performance

**Exam signals**

* “Cost-sensitive”
* “Regional users”
* “No global latency requirement”

---

## 3️⃣ HARD exam rule (memorize)

> **If a service is global, it MUST use Premium Tier**

This is not optional.

Examples:

* Global HTTP(S) Load Balancer → **Premium only**
* Global external IP → **Premium only**

You cannot downgrade these to Standard.

---

## 4️⃣ When the ACE exam expects each tier

### Use **Premium Tier** when:

* Internet-facing global apps
* Global load balancing
* Latency-sensitive workloads
* SLA requirements

### Use **Standard Tier** when:

* Regional workloads
* Cost is more important than latency
* No global distribution required

---

## 5️⃣ Decision table (MEMORIZE)

| Requirement           | Tier     |
| --------------------- | -------- |
| Global users          | Premium  |
| HTTP(S) Load Balancer | Premium  |
| Lowest latency        | Premium  |
| Cost optimization     | Standard |
| Regional-only access  | Standard |

---

## 6️⃣ Common ACE exam scenarios

### Scenario 1

> “Serve users worldwide with minimal latency”

✅ **Premium Tier**

---

### Scenario 2

> “Internal regional service, cost-sensitive”

✅ **Standard Tier**

---

### Scenario 3

> “Global HTTP(S) Load Balancer in use”

✅ **Premium Tier (mandatory)**

---

## 7️⃣ Common ACE exam traps

❌ Thinking Standard Tier can be used with global load balancers
❌ Choosing Premium when no global requirement exists
❌ Assuming Standard Tier is insecure
❌ Forgetting that tier impacts latency, not firewalling

---

## 🔑 One-line ACE memory hooks

* **Global = Premium**
* **Regional & cheap = Standard**
* **HTTP(S) LB = Premium only**

---
 
