### **Section 3.2 – Managing storage resources**

#### **Estimating costs of data storage resources**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/figure-two-pricing-blogl1vz.max-1000x1000.PNG)

![Image](https://www.cloudkeeper.com/cms-assets/s3fs-public/2023-07/Table.jpg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/1_packaging_option.max-1400x1400.jpg)

![Image](https://cdn.prod.website-files.com/5e0096e310bfa7cae89f5e1b/643d6e190b11c45d7c9f6407_Screenshot%202023-04-17%20at%2019.34.08.png)

This bullet tests whether you can **estimate and compare storage costs at a high level** and **choose cost-effective configurations**. The ACE exam does **not** expect exact dollar math—it expects you to know **what drives cost** and **how to reduce it**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify **pricing dimensions** for each storage service
* Compare **cost drivers** across services
* Choose **cheaper alternatives** when requirements allow
* Apply **cost-control features** (lifecycle rules, partitions, tiers)

> **Exam mindset:**
> *“What will make the bill go up—and how do I control it?”*

---

## 2️⃣ Universal storage cost drivers (MEMORIZE)

Almost all GCP storage costs come from:

1. **Amount of data stored** (GB/month)
2. **Storage class or tier**
3. **Access frequency**
4. **Operations** (reads/writes)
5. **Network egress** (leaving GCP)

> **ACE trap:**
> Ingress is usually free; **egress costs money**.

---

## 3️⃣ Cloud Storage cost estimation (VERY HIGH-YIELD)

### Cost components

* **Storage cost** (per GB/month)
* **Operation cost** (GET, PUT, LIST)
* **Data retrieval cost** (Nearline/Coldline/Archive)
* **Egress cost**

### Storage class cost order (cheapest storage → most expensive access)

```
Archive → Coldline → Nearline → Standard
```

### Exam signals

* “Rarely accessed backups” → **Archive**
* “Infrequent access” → **Coldline/Nearline**
* “Frequently accessed” → **Standard**

> **ACE rule:**
> Pick the **cheapest class that still meets access needs**.

---

## 4️⃣ BigQuery cost estimation

### Two main cost areas

#### A. Storage

* Charged per GB/month
* Active vs long-term storage pricing
* Partitioned tables reduce cost

#### B. Query processing

* Charged per **data scanned**
* On-demand pricing or flat-rate

### Cost-control features (EXAM FAVORITES)

* **Partitioned tables**
* **Clustered tables**
* **Maximum bytes billed**
* **Views** (logical abstraction)

> **ACE trap:**
> Unpartitioned tables = expensive scans.

---

## 5️⃣ Cloud SQL & AlloyDB cost estimation

### Cost components

* Instance size (CPU + memory)
* Storage size (GB)
* High availability (standby replica)
* Backups and snapshots

### Exam signals

* “HA enabled” → higher cost
* “Bigger machine type” → higher cost

> **ACE rule:**
> Right-size instances; HA doubles compute cost.

---

## 6️⃣ Spanner cost estimation (recognition-level)

### Cost drivers

* Number of nodes or processing units
* Storage used
* Multi-region configuration

### Exam awareness

* Spanner is **expensive by design**
* Chosen for **scale + consistency**, not cost savings

> **ACE signal:**
> If cost sensitivity is mentioned → **Spanner is likely wrong**

---

## 7️⃣ Firestore & Bigtable cost estimation

### Firestore

* Charged by:

  * Reads
  * Writes
  * Deletes
  * Storage

**Exam signals**

* “High read/write frequency” → cost driven by ops

---

### Bigtable

* Charged by:

  * Node count
  * Storage
* Not by queries

**Exam signals**

* “Always-on nodes” → constant baseline cost

---

## 8️⃣ Cost estimation tools (exam awareness)

### Pricing Calculator

* Used to:

  * Estimate monthly cost
  * Compare options

### Budgets & alerts

* Detect overspend
* Do **not** stop usage automatically

> **ACE rule:**
> Budgets = alerting, not enforcement.

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Estimate cheapest way to store long-term backups”

✅ **Cloud Storage Archive**

---

### Scenario 2

> “Analytics costs are unexpectedly high”

✅ Likely cause:

* Large unpartitioned BigQuery queries

---

### Scenario 3

> “Relational DB cost doubled after enabling HA”

✅ Expected:

* Standby instance cost

---

### Scenario 4

> “Firestore bill spikes with traffic”

✅ Cause:

* Increased read/write operations

---

## 🔟 Common ACE exam traps

❌ Choosing Standard storage for cold data
❌ Ignoring retrieval costs in Archive/Coldline
❌ Forgetting egress charges
❌ Using Spanner for cost-sensitive apps
❌ Expecting BigQuery storage cost to dominate query cost

---

## 🔑 One-line ACE memory hooks

* **GB/month + access = cost**
* **Cold data → cold storage**
* **BigQuery cost = data scanned**
* **HA doubles compute**
* **Egress costs money**

---
 
