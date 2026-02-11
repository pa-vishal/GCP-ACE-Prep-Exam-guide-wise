### **Section 3.2 – Managing storage resources**

#### **Executing queries to retrieve data from data instances**

*(Cloud SQL, BigQuery, Bigtable, Spanner, Firestore, AlloyDB)*

![Image](https://miro.medium.com/v2/resize%3Afit%3A1200/1%2A5eQzpHBB_bmrY5B1IVuN8g.png)

![Image](https://docs.cloud.google.com/static/bigquery/images/console-tabs.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/1_4.max-1600x1600.JPG)

This bullet is about **how you read data**, not how you design schemas. The ACE exam checks whether you can **identify the correct query interface and query model for each service**, and avoid mixing OLTP and OLAP patterns.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Match each data service to **its query model**
* Know **where queries are executed** (console, CLI, client)
* Recognize **SQL vs NoSQL** access patterns
* Avoid using the wrong service for the workload

> **Exam mindset:**
> *“What’s the correct way to read data from THIS service?”*

---

## 2️⃣ High-level mapping (MEMORIZE)

| Service       | Query model       | Typical interface    |
| ------------- | ----------------- | -------------------- |
| **Cloud SQL** | SQL (OLTP)        | SQL client / Console |
| **AlloyDB**   | SQL (PostgreSQL)  | SQL client           |
| **BigQuery**  | SQL (OLAP)        | BigQuery UI / `bq`   |
| **Spanner**   | SQL (distributed) | Console / client     |
| **Firestore** | Document queries  | SDK / Console        |
| **Bigtable**  | Key/row-based     | SDK / CLI            |

> **ACE rule:**
> SQL ≠ universal. Each service has a **designed query pattern**.

---

## 3️⃣ Cloud SQL (relational OLTP)

### Query model

* Standard SQL (MySQL / PostgreSQL / SQL Server)

### How queries are executed

* Cloud Console (Query editor)
* SQL clients (psql, mysql)
* Applications

### Example (conceptual)

```sql
SELECT * FROM orders WHERE status = 'OPEN';
```

**Exam signals**

* “Transactional queries”
* “Relational schema”
* “Small to medium dataset”

> **Exam trap:**
> Don’t use Cloud SQL for large analytics queries.

---

## 4️⃣ AlloyDB (high-performance PostgreSQL)

### Query model

* PostgreSQL-compatible SQL
* Optimized for performance

### How queries are executed

* PostgreSQL clients
* Applications

**Exam signals**

* “PostgreSQL compatible”
* “High performance queries”

> **ACE note:**
> Treat AlloyDB like **Cloud SQL with more performance**, not BigQuery.

---

## 5️⃣ BigQuery (analytics / OLAP)

### Query model

* ANSI SQL
* Columnar, read-heavy

### How queries are executed

* BigQuery web UI
* `bq query` CLI
* BI tools

### Example

```sql
SELECT country, COUNT(*) 
FROM `mydataset.users`
GROUP BY country;
```

**Exam signals**

* “Analytics”
* “Reporting”
* “Large datasets”
* “Aggregations”

> **ACE rule:**
> BigQuery = **scan & aggregate**, not row-by-row lookups.

---

## 6️⃣ Spanner (distributed relational)

### Query model

* SQL with strong consistency
* Horizontally scalable

### How queries are executed

* Cloud Console
* Client libraries
* Applications

**Exam signals**

* “Global database”
* “Strong consistency”
* “Relational at scale”

> **Exam trap:**
> Spanner is chosen for **scale + consistency**, not simplicity.

---

## 7️⃣ Firestore (NoSQL document database)

### Query model

* Structured queries on:

  * Collections
  * Documents
  * Fields
* No joins

### How queries are executed

* Console
* SDKs (Java, Node, Python, etc.)

**Example (conceptual)**

```text
Query collection "users" where status == "active"
```

**Exam signals**

* “Mobile/web app”
* “Document-based”
* “Flexible schema”

> **ACE rule:**
> If you need joins → Firestore is the wrong choice.

---

## 8️⃣ Bigtable (wide-column, key-based)

### Query model

* Row key lookups
* Range scans
* No SQL

### How queries are executed

* Client libraries
* `cbt` CLI (recognition-level)

**Exam signals**

* “Time-series data”
* “Massive throughput”
* “Low-latency reads by key”

> **Exam trap:**
> Bigtable ≠ BigQuery. No ad-hoc SQL.

---

## 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Run an aggregation over terabytes of data”

✅ **BigQuery**

---

### Scenario 2

> “Retrieve a user profile by ID in a mobile app”

✅ **Firestore**

---

### Scenario 3

> “Execute transactional SQL queries”

✅ **Cloud SQL or AlloyDB**

---

### Scenario 4

> “Low-latency reads on time-series metrics”

✅ **Bigtable**

---

### Scenario 5

> “Globally consistent relational reads”

✅ **Spanner**

---

## 🔟 Common ACE exam traps

❌ Using BigQuery for OLTP queries
❌ Expecting SQL joins in Firestore
❌ Running analytics on Cloud SQL
❌ Expecting ad-hoc queries in Bigtable

---

## 🔑 One-line ACE memory hooks

* **Cloud SQL / AlloyDB = OLTP SQL**
* **BigQuery = analytics SQL**
* **Spanner = global SQL**
* **Firestore = document queries**
* **Bigtable = key-based reads**

--- 
