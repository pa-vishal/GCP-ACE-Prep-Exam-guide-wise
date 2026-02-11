### **Section 2.2 – Maintaining multi-region redundancy across data solutions**

![Image](https://docs.cloud.google.com/static/architecture/images/multiregional-ra-gclb.svg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/image1_bgyltjy.max-1900x1900.png)

![Image](https://docs.cloud.google.com/static/sql/images/post-ha.svg)

![Image](https://docs.cloud.google.com/static/solutions/images/cloud-sql-mysql-disaster-recovery-complete-failover-fallback-basic-architecture.png)

This bullet tests whether you understand **how Google Cloud protects data from failures beyond a single zone or region**, and—crucially—**which services do this automatically vs which require explicit configuration**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Distinguish **zonal**, **regional**, and **multi-region/global** redundancy
* Choose the **right service configuration** to meet availability requirements
* Avoid assuming backups = high availability

> **Exam mindset:**
> *“If a zone or region fails, is my data still available?”*

---

## 2️⃣ Redundancy levels (lock this in)

| Level                 | Protects against  | Typical scope    |
| --------------------- | ----------------- | ---------------- |
| Zonal                 | VM / disk failure | One zone         |
| Regional              | Zone failure      | One region       |
| Multi-region / Global | Region failure    | Multiple regions |

> **Exam trap:**
> Zonal ≠ HA. Backups ≠ HA.

---

## 3️⃣ How major data services handle redundancy

### 🗄️ **Cloud Storage** (MOST tested here)

#### Options

* **Regional** bucket → replicated within one region
* **Dual-region** bucket → replicated across two regions
* **Multi-region** bucket → replicated across multiple regions automatically

#### Use when

* Need durability + availability
* Want Google to manage replication

**Exam signals**

* “Highly durable object storage”
* “Cross-region availability”
* “No manual replication”

> **Exam rule:**
> If multi-region durability is required → **Cloud Storage multi-region**

---

### 🐘 **Cloud SQL**

#### What it supports

* **Regional HA configuration**

  * Primary + standby in different zones
* Automatic failover

#### What it does NOT do

* Native multi-region writes
* Global active-active

**Exam signals**

* “Survive zone failure”
* “Relational database with HA”

> **Important:**
> Cloud SQL HA = **regional**, not multi-region

---

### 🌍 **Spanner**

#### What it provides

* Native **multi-region / global replication**
* Strong consistency
* Automatic failover across regions

#### Use when

* Mission-critical
* Global users
* Zero-downtime requirements

**Exam signals**

* “Global database”
* “Strong consistency across regions”
* “High availability at global scale”

---

### 📊 **BigQuery**

#### Redundancy model

* Data automatically replicated
* Regional or multi-region datasets
* No user-managed replication

**Exam signals**

* “Analytics with high availability”
* “No infrastructure management”

---

### 📄 **Firestore**

#### Native behavior

* Multi-region replication (in multi-region mode)
* Automatic failover

**Exam signals**

* “Highly available NoSQL”
* “Global app backend”

---

### 📊 **Bigtable**

#### Redundancy options

* Single-cluster (regional)
* Multi-cluster routing (cross-region)

**Exam signals**

* “High throughput”
* “Cross-region reads”

---

## 4️⃣ Redundancy ≠ Backup (VERY important)

| Concept    | Purpose                                |
| ---------- | -------------------------------------- |
| Redundancy | Availability during failures           |
| Backup     | Data recovery from corruption/deletion |

> **Exam trap:**
> Backups help you recover data, **not** keep apps running during outages.

---

## 5️⃣ Decision table (MEMORIZE)

| Requirement                         | Best Choice                  |
| ----------------------------------- | ---------------------------- |
| Object storage, global availability | Cloud Storage (multi-region) |
| Relational DB, zone HA              | Cloud SQL (regional HA)      |
| Relational DB, global HA            | Spanner                      |
| Analytics with built-in HA          | BigQuery                     |
| Global NoSQL                        | Firestore (multi-region)     |
| Massive scale, cross-region reads   | Bigtable (multi-cluster)     |

---

## 6️⃣ Real ACE-style scenarios

### Scenario 1

> “Store user uploads with automatic cross-region redundancy”

✅ **Cloud Storage multi-region**

---

### Scenario 2

> “Relational database must survive a zone outage”

✅ **Cloud SQL with regional HA**

---

### Scenario 3

> “Financial system requiring global availability and consistency”

✅ **Spanner**

---

### Scenario 4

> “Analytics platform with built-in durability and availability”

✅ **BigQuery**

---

## 7️⃣ Common ACE exam traps

❌ Assuming zonal disks are highly available
❌ Assuming Cloud SQL is multi-region by default
❌ Using backups as an HA strategy
❌ Overengineering with Spanner when regional HA is enough

---

## 🔑 One-line ACE memory hooks

* **Regional HA = zone failure**
* **Multi-region = region failure**
* **Backups ≠ availability**

---
 
