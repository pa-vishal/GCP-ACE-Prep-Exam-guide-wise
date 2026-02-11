### **Section 3.2 – Managing storage resources**

#### **Backing up and restoring database instances**

*(Cloud SQL, Firestore, Spanner, AlloyDB, Bigtable)*

![Image](https://docs.cloud.google.com/static/sql/images/restore-rate-tokens.png)

![Image](https://estuary.dev/static/b0682e82e4befbac75f90333ac2e5334/09e10/01_Firestore_To_JSON_What_Is_Firestore_aad8bc0a94.png)

![Image](https://docs.cloud.google.com/static/spanner/docs/images/databoost-architecture.png)

![Image](https://docs.cloud.google.com/static/spanner/docs/images/spanner-graph-example-graph.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/bigquery_sketch.max-2000x2000.png)

This bullet tests whether you understand **service-specific backup mechanisms**, **what backups protect against**, and **how restores are performed**. The ACE exam emphasizes **choosing the correct native backup feature**, not scripting custom solutions.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify **native backup options** for each database
* Distinguish **automatic vs manual** backups
* Restore data **to the same or a new instance**
* Avoid confusing **backups with high availability**

> **Exam mindset:**
> *“How do I recover data after deletion or corruption?”*

---

## 2️⃣ Core rule (MUST MEMORIZE)

> **Backups protect data.
> Replicas / HA protect availability.
> They solve different problems.**

This distinction is a **frequent exam trap**.

---

## 3️⃣ Cloud SQL

### Backup options

* **Automated backups** (recommended)
* **On-demand backups**
* **Binary logs** (point-in-time recovery)

### What you can do

* Restore to:

  * Same instance
  * New instance
* Restore to a **specific point in time**

### Exam signals

* “Accidental data deletion”
* “Restore to yesterday”
* “Point-in-time recovery”

> **ACE rule:**
> Cloud SQL PITR requires **binary logging enabled**.

---

## 4️⃣ AlloyDB

### Backup model

* **Automated backups** (continuous)
* **Manual backups**

### Restore options

* Restore to:

  * New AlloyDB cluster
  * New instance

### Exam awareness

* PostgreSQL-compatible
* Backup behavior similar in concept to Cloud SQL

> **ACE signal:**
> “Enterprise PostgreSQL backup” → **AlloyDB automated backups**

---

## 5️⃣ Firestore

### Backup model

* **Export / Import** to Cloud Storage
* No automatic point-in-time restore

### How it works

```
Firestore → Export → Cloud Storage
Cloud Storage → Import → Firestore
```

### Exam signals

* “Recover documents”
* “Export data”
* “Cross-project restore”

> **ACE rule:**
> Firestore backups are **file exports**, not snapshots.

---

## 6️⃣ Spanner

### Backup model

* **Managed backups**
* Independent backup resources
* Configurable retention

### Restore options

* Restore to:

  * New database
  * New instance

### Exam signals

* “Mission-critical”
* “Global relational database”
* “Strong consistency + backups”

> **ACE awareness:**
> Spanner backups are **separate resources** and incur cost.

---

## 7️⃣ Bigtable

### Backup model

* **Bigtable backups**
* Cluster-level
* Stored independently

### Restore options

* Restore to:

  * Same cluster
  * Different cluster

### Exam signals

* “Time-series data recovery”
* “Large-scale NoSQL restore”

> **ACE rule:**
> Bigtable backups are **fast and incremental**, but not cross-row-atomic.

---

## 8️⃣ Comparison table (VERY IMPORTANT)

| Service   | Backup method         | Point-in-time         | Restore target       |
| --------- | --------------------- | --------------------- | -------------------- |
| Cloud SQL | Automated + on-demand | ✅                     | Same / new instance  |
| AlloyDB   | Automated + manual    | ⚠️ (engine-dependent) | New cluster/instance |
| Firestore | Export to GCS         | ❌                     | Same / new project   |
| Spanner   | Managed backups       | ❌ (backup time only)  | New database         |
| Bigtable  | Bigtable backups      | ❌                     | Same / new cluster   |

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Recover Cloud SQL data from 3 hours ago”

✅ **Point-in-time restore (Cloud SQL)**

---

### Scenario 2

> “Back up Firestore nightly for compliance”

✅ **Scheduled exports to Cloud Storage**

---

### Scenario 3

> “Restore Spanner data after accidental deletion”

✅ **Restore from Spanner backup**

---

### Scenario 4

> “Protect Bigtable data from corruption”

✅ **Bigtable backups**

---

## 🔟 Common ACE exam traps

❌ Using replicas as backups
❌ Expecting Firestore PITR
❌ Forgetting backups incur storage cost
❌ Assuming backups provide high availability
❌ Choosing manual scripts over native backups

---

## 🔑 One-line ACE memory hooks

* **Backups ≠ HA**
* **Cloud SQL = PITR**
* **Firestore = export/import**
* **Spanner = managed backups**
* **Bigtable = cluster backups**

---
 
