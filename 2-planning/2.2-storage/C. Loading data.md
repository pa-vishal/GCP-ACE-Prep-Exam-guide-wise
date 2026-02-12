### **Section 2.2 – Loading data**

*(command-line upload, load data from Cloud Storage, Storage Transfer Service)*

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/BigQuery_ingest_6.max-1000x1000.png)

![Image](https://www.netapp.com/media/netapp22_tcm19-127873.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/BigQuery_ingest_3.max-800x800.png)

![Image](https://docs.cloud.google.com/static/workflows/images/serverless-orchestration-loading-data-from-cloud-storage-to-biquery-using-workflows-1-architecture.svg)

This bullet tests whether you can **choose the correct ingestion method based on data size, source, and frequency**. The ACE exam is not about tuning pipelines—it’s about **picking the simplest, correct loading mechanism**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Choose **manual vs automated** data loading
* Load data **into the right destination** (Cloud Storage, BigQuery)
* Select **Storage Transfer Service** for large or recurring moves
* Avoid overengineering with Dataflow when not required

> **Exam mindset:**
> *“Where is the data coming from, how big is it, and how often does it move?”*

---

## 2️⃣ Command-line uploads (small, ad-hoc data)

### Tools

* `gcloud storage` (modern)
* `gsutil` (legacy but still common on exams)

### Use when

* Small datasets
* One-time or ad-hoc uploads
* Developer-driven actions

### Exam signals

* “Upload a file”
* “Quickly move data”
* “One-time import”

### Example (Cloud Storage)

```bash
gcloud storage cp local-file.csv gs://my-bucket/
```

> **ACE note:**
> CLI uploads are **not** ideal for large-scale or recurring transfers.

---

## 3️⃣ Loading data from Cloud Storage (MOST TESTED)

### Key pattern

```
Source → Cloud Storage → Target service
```

Many Google Cloud services **load from Cloud Storage**, not directly from your laptop.

---

### A. BigQuery load jobs

**Use when**

* Structured or semi-structured data
* Batch analytics

**Exam signals**

* “Load CSV/JSON/Avro into BigQuery”
* “Analytics dataset”

```bash
bq load \
  --source_format=CSV \
  my_dataset.my_table \
  gs://my-bucket/data.csv
```

---

### B. Cloud SQL imports

**Use when**

* Importing SQL dumps
* Migrating small to medium databases

**Exam signals**

* “Import database”
* “SQL dump”

Flow:

```
Dump → Cloud Storage → Cloud SQL
```

---

## 4️⃣ Storage Transfer Service (LARGE or RECURRING data)

### What it is

* Fully managed bulk data transfer service

### Sources

* On-premises
* Other cloud providers (AWS S3, Azure Blob)
* Another Cloud Storage bucket

### Use when

* Large datasets (TBs+)
* Scheduled or recurring transfers
* Minimal operational effort

### Exam signals

* “Terabytes of data”
* “Recurring transfer”
* “Migrate from on-prem or AWS”

> **ACE rule:**
> **Large + recurring = Storage Transfer Service**

---

## 5️⃣ Choosing the right loading method (DECISION TABLE)

| Scenario                 | Best Choice                       |
| ------------------------ | --------------------------------- |
| One-time small upload    | CLI (gcloud/gsutil)               |
| Load analytics data      | Cloud Storage → BigQuery          |
| Import database          | Cloud Storage → Cloud SQL         |
| Large recurring transfer | Storage Transfer Service          |
| Transform during load    | Dataflow (if explicitly required) |

---

## 6️⃣ What NOT to choose (exam traps)

❌ Use Dataflow for simple uploads
❌ Upload TBs via `gsutil`
❌ Load directly from laptop to BigQuery
❌ Use Storage Transfer for tiny one-time files

---

## 7️⃣ Real ACE-style scenarios

### Scenario 1

> “Upload a CSV file to analyze in BigQuery”

✅ **Upload to Cloud Storage, then BigQuery load**

---

### Scenario 2

> “Migrate TBs of data nightly from on-prem”

✅ **Storage Transfer Service**

---

### Scenario 3

> “Quickly upload a log file for testing”

✅ **CLI upload**

---

## 8️⃣ One-line ACE memory hooks

* **Small & manual → CLI**
* **Analytics → Cloud Storage → BigQuery**
* **Big & recurring → Storage Transfer Service**

--- 
