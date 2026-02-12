### **Section 3.2 – Managing storage resources**

#### **Reviewing job status**

*(Dataflow, BigQuery)*

![Image](https://docs.cloud.google.com/static/dataflow/images/cpu-utilization.gif)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2Aa02o2O0NTcFqHamk)

![Image](https://docs.cloud.google.com/static/dataflow/images/execution-graph.png)

This bullet is about **operational visibility**. The ACE exam checks whether you can **find running/completed/failed jobs**, **interpret basic states**, and **know where to look**—not how to debug pipelines deeply.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Locate **job history** for Dataflow and BigQuery
* Identify **job states** (running, failed, done)
* Take the **next logical action** (wait, retry, inspect logs)
* Avoid confusing **jobs** with **resources**

> **Exam mindset:**
> *“Did the job run? Is it still running? Did it fail?”*

---

## 2️⃣ BigQuery job status (VERY COMMON)

### What counts as a “job”

* Queries
* Load jobs
* Export jobs
* Copy jobs

### Where to check

* **Cloud Console → BigQuery → Job history**
* Project-level scope

### Common job states

| State       | Meaning                   |
| ----------- | ------------------------- |
| **RUNNING** | Query or load in progress |
| **DONE**    | Completed successfully    |
| **FAILED**  | Error occurred            |

### CLI (exam-aware)

```bash
bq ls -j
```

> **Exam signal:**
> “Query didn’t produce results” → check **job status**

---

## 3️⃣ BigQuery failure patterns (exam-level)

Common reasons jobs fail:

* SQL syntax errors
* Permission denied
* Exceeded **maximum bytes billed**
* Dataset/table not found

> **ACE trap:**
> A query can fail **after starting**—always check job details.

---

## 4️⃣ Dataflow job status (FOUNDATIONAL)

### What counts as a job

* Batch pipeline
* Streaming pipeline

### Where to check

* **Cloud Console → Dataflow → Jobs**

### Common Dataflow job states

| State         | Meaning                  |
| ------------- | ------------------------ |
| **Running**   | Actively processing      |
| **Draining**  | Finishing in-flight work |
| **Done**      | Completed successfully   |
| **Failed**    | Pipeline error           |
| **Cancelled** | Stopped by user          |

> **Exam signal:**
> “Pipeline stuck” → check **job state**

---

## 5️⃣ Batch vs Streaming (EXAM FAVORITE DISTINCTION)

| Type          | Expected behavior     |
| ------------- | --------------------- |
| **Batch**     | Eventually → **Done** |
| **Streaming** | Stays **Running**     |

> **ACE trap:**
> A streaming job running for days is **normal**, not a failure.

---

## 6️⃣ What you do AFTER checking status (exam logic)

### If job is RUNNING

* Wait
* Monitor metrics/logs

### If job FAILED

* Inspect error message
* Fix input, permissions, or config
* Rerun job

### If job DONE but output missing

* Check destination
* Check permissions
* Check filters/conditions

---

## 7️⃣ Permissions awareness (exam-level)

To view job status, you need:

* BigQuery:

  * `bigquery.jobs.list`
* Dataflow:

  * `dataflow.jobs.get`

> **Exam signal:**
> “User can’t see job history” → IAM issue

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Analytics query seems stuck”

✅ Check:

* **BigQuery job status**

---

### Scenario 2

> “Dataflow streaming job hasn’t finished”

✅ Expected:

* Streaming jobs **run continuously**

---

### Scenario 3

> “Load job failed unexpectedly”

✅ Action:

* Inspect **job error details**

---

### Scenario 4

> “Pipeline output missing”

✅ Action:

* Verify job **completed successfully**
* Check destination permissions

---

## 9️⃣ Common ACE exam traps

❌ Expecting streaming jobs to complete
❌ Checking datasets instead of job history
❌ Ignoring error details
❌ Assuming no output means no job ran

---

## 🔑 One-line ACE memory hooks

* **BigQuery = job history**
* **Dataflow batch ends, streaming runs**
* **Failed ≠ never started**
* **Check status before retrying**

--- 
