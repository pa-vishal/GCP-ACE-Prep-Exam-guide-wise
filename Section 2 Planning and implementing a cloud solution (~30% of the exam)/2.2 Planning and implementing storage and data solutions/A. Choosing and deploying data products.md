### **Section 2.2 – Choosing and deploying data products**

*(Cloud SQL, BigQuery, Firestore, Spanner, Bigtable, AlloyDB, Dataflow, Pub/Sub, Google Cloud Managed Service for Apache Kafka, Memorystore)*

![Image](https://assets.bytebytego.com/diagrams/0093-cloud-comparison-cheat-sheet.png)

![Image](https://media.licdn.com/dms/image/v2/C5612AQGa9oLcWmMzxQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1575264743959?e=2147483647\&t=TKvajLpxIU8xKsE58LkWTmKS3ebj2crtnSGPohKKacE\&v=beta)

![Image](https://www.xenonstack.com/hubfs/xenonstack-build-stream-analytics-systems.png)

This is a **top-tier ACE decision bullet**. The exam is testing whether you can **map data access patterns and consistency needs to the right managed service**—not whether you can tune schemas or write pipelines.

---

## 1️⃣ What the ACE exam is REALLY testing

You must identify:

* **OLTP vs OLAP**
* **Relational vs NoSQL**
* **Batch vs streaming**
* **In-memory vs durable**
* **Single-region vs global scale**

> **Exam mindset:**
> *“What problem is this data service solving?”*

---

## 2️⃣ Mental model: classify the workload FIRST

Before choosing a product, answer these in order:

1. Is it **transactional** or **analytical**?
2. Is the schema **relational** or **flexible**?
3. Is scale **small/medium** or **massive/global**?
4. Is data **streaming** or **at rest**?
5. Is **low latency** critical?

---

## 3️⃣ Core data products (exam-level understanding)

### 🗄️ **Cloud SQL**

**What it is**

* Managed relational databases (MySQL, PostgreSQL, SQL Server)

**Use when**

* Traditional OLTP
* Small to medium scale
* App needs SQL + ACID

**Exam signals**

* “Relational database”
* “Transactional workload”
* “Lift-and-shift database”

---

### 🧮 **BigQuery**

**What it is**

* Serverless **data warehouse**
* OLAP analytics at massive scale

**Use when**

* Analytics
* Reporting
* Large datasets
* Read-heavy queries

**Exam signals**

* “Analytics”
* “Reporting”
* “Petabytes of data”
* “No infrastructure management”

---

### 📄 **Firestore**

**What it is**

* NoSQL document database
* Serverless
* Strong consistency (in native mode)

**Use when**

* Mobile / web apps
* Flexible schema
* Real-time updates

**Exam signals**

* “Mobile backend”
* “Document-based”
* “No schema migrations”

---

### 🌍 **Spanner**

**What it is**

* Globally distributed relational database
* Strong consistency
* Horizontal scaling

**Use when**

* Global applications
* Relational + massive scale
* Strong consistency across regions

**Exam signals**

* “Global scale”
* “Strong consistency”
* “Mission critical”

---

### 📊 **Bigtable**

**What it is**

* Wide-column NoSQL database
* Extremely high throughput
* Low latency at scale

**Use when**

* Time-series data
* IoT
* Metrics
* Large-scale analytical ingestion

**Exam signals**

* “Billions of rows”
* “Low latency reads/writes”
* “Time-series”

---

### 🐘 **AlloyDB**

**What it is**

* High-performance PostgreSQL-compatible database
* Optimized for analytics + transactions

**Use when**

* PostgreSQL compatibility
* Higher performance than Cloud SQL
* Enterprise workloads

**Exam signals**

* “PostgreSQL compatible”
* “High performance”
* “Enterprise database”

---

### 🔄 **Dataflow**

**What it is**

* Serverless data processing
* Batch + streaming
* Apache Beam-based

**Use when**

* ETL pipelines
* Stream processing
* Transforming data at scale

**Exam signals**

* “Transform data”
* “Streaming pipeline”
* “ETL”

---

### 📣 **Pub/Sub**

**What it is**

* Global messaging service
* Event ingestion and delivery

**Use when**

* Event-driven architectures
* Decoupling producers/consumers
* Streaming ingestion

**Exam signals**

* “Event-driven”
* “Asynchronous messaging”
* “Publish/subscribe”

---

### 🧵 **Google Cloud Managed Service for Apache Kafka**

**What it is**

* Fully managed Kafka
* Compatible with Kafka APIs

**Use when**

* Existing Kafka workloads
* Kafka ecosystem required
* Streaming with Kafka semantics

**Exam signals**

* “Kafka”
* “Existing Kafka clients”
* “Kafka compatibility”

---

### ⚡ **Memorystore**

**What it is**

* In-memory data store (Redis / Memcached)
* Very low latency

**Use when**

* Caching
* Session storage
* Leaderboards

**Exam signals**

* “Cache”
* “Sub-millisecond latency”
* “Reduce database load”

---

## 4️⃣ The ACE decision table (MEMORIZE)

| Requirement                      | Best Choice   |
| -------------------------------- | ------------- |
| Relational OLTP                  | Cloud SQL     |
| Global relational scale          | Spanner       |
| Analytics / OLAP                 | BigQuery      |
| Flexible schema app              | Firestore     |
| Time-series / massive throughput | Bigtable      |
| PostgreSQL, high performance     | AlloyDB       |
| ETL / stream processing          | Dataflow      |
| Event ingestion                  | Pub/Sub       |
| Kafka compatibility              | Managed Kafka |
| Cache / sessions                 | Memorystore   |

---

## 5️⃣ Deployment awareness (ACE-level)

You are expected to know:

* These are **managed services**
* Provisioning is mostly:

  * Choose region
  * Choose capacity/tier
* You are **not** tested on:

  * Schema design
  * Query tuning
  * Pipeline code

---

## 6️⃣ Common ACE exam traps (VERY IMPORTANT)

❌ Using BigQuery for transactions
❌ Using Cloud SQL for analytics
❌ Using Firestore when SQL joins are required
❌ Using Memorystore as a primary database
❌ Choosing Spanner when global scale isn’t needed

> **Exam rule:**
> **Do not over-engineer. Choose the simplest service that meets requirements.**

---

## 7️⃣ Real ACE-style scenarios

### Scenario 1

> “Mobile app backend with flexible schema and real-time updates”

✅ **Firestore**

---

### Scenario 2

> “Company needs analytics on terabytes of log data”

✅ **BigQuery**

---

### Scenario 3

> “Global financial system requiring strong consistency”

✅ **Spanner**

---

### Scenario 4

> “Decouple services using events”

✅ **Pub/Sub**

---

### Scenario 5

> “Reduce database load for read-heavy traffic”

✅ **Memorystore**

---

## 🔑 One-line ACE memory hooks

* **Cloud SQL = traditional SQL**
* **BigQuery = analytics**
* **Firestore = documents**
* **Spanner = global SQL**
* **Bigtable = massive throughput**
* **Dataflow = processing**
* **Pub/Sub = events**
* **Memorystore = cache**

---
 
