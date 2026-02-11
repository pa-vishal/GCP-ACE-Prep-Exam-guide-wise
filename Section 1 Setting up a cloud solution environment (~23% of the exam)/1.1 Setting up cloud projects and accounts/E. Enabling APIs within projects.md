
### **Section 1.1 – Enabling APIs within projects**

![Image](https://docs.cloud.google.com/static/api-gateway/docs/images/concepts-architecure.svg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/image3_CNn09PW.max-2000x2000.png)

This bullet is **simple on the surface but frequently tested indirectly**. Many ACE questions fail candidates because they forget that **services do not work unless their APIs are enabled**.

---

## 1️⃣ What “enabling APIs” actually means

In Google Cloud, **every managed service is exposed via an API**.

If the API is **not enabled** in a project:

* The service **cannot be used**
* CLI / Console / SDK calls **fail**
* IAM permissions alone are **not sufficient**

> **Key rule**
> **IAM grants permission, but APIs grant capability**

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you understand that:

### ✅ APIs are enabled **per project**

* Not per user
* Not per organization
* Not per folder

### ✅ Many failures are due to **missing API enablement**

Typical error patterns in questions:

* “Permission denied”
* “Service not found”
* “API has not been used in project before”

### ❌ What the exam does NOT test

* Low-level API quotas
* Writing custom API clients
* REST endpoint syntax

---

## 3️⃣ Common services that REQUIRE API enablement (exam favorites)

If you see these services mentioned, assume **API enablement is required**:

| Service         | API                             |
| --------------- | ------------------------------- |
| Compute Engine  | `compute.googleapis.com`        |
| Cloud Storage   | `storage.googleapis.com`        |
| GKE             | `container.googleapis.com`      |
| Cloud Run       | `run.googleapis.com`            |
| Cloud SQL       | `sqladmin.googleapis.com`       |
| BigQuery        | `bigquery.googleapis.com`       |
| Pub/Sub         | `pubsub.googleapis.com`         |
| Cloud Functions | `cloudfunctions.googleapis.com` |

---

## 4️⃣ Enabling APIs via CLI (gcloud) — EXAM-READY

### 🔹 Enable a single API

```bash
gcloud services enable compute.googleapis.com \
  --project=my-project
```

---

### 🔹 Enable multiple APIs at once

```bash
gcloud services enable \
  compute.googleapis.com \
  container.googleapis.com \
  iam.googleapis.com \
  --project=my-project
```

---

### 🔹 List enabled APIs in a project

```bash
gcloud services list --enabled --project=my-project
```

---

### 🔹 Check if a specific API is enabled

```bash
gcloud services list \
  --enabled \
  --filter="name:compute.googleapis.com" \
  --project=my-project
```

---

## 5️⃣ Enabling APIs via Console (conceptual flow)

1. Select **Project**
2. Go to **APIs & Services**
3. Click **Enable APIs and Services**
4. Search service
5. Click **Enable**

> Exam will not test UI clicks — only **understanding**.

---

## 6️⃣ IAM + API enablement interaction (very important)

Both are required.

| Condition                 | Result  |
| ------------------------- | ------- |
| IAM granted, API disabled | ❌ Fails |
| API enabled, no IAM       | ❌ Fails |
| Both present              | ✅ Works |

**Exam trap**

> “User has correct role but still cannot use service”
> ✔️ Missing API enablement

---

## 7️⃣ Service accounts & APIs (common confusion)

* APIs are enabled **at project level**
* Service accounts **inherit enabled APIs**
* You do **not** enable APIs per service account

> If a Cloud Run service fails → check **API enablement**, not service account first

---

## 8️⃣ Real exam-style scenarios

### Scenario 1

> “A VM cannot be created despite correct IAM role”

✅ Root cause:

* Compute Engine API not enabled

---

### Scenario 2

> “Deploying GKE fails in a new project”

✅ Fix:

* Enable:

  * `container.googleapis.com`
  * `compute.googleapis.com`
  * `iam.googleapis.com`

---

### Scenario 3

> “Automation pipeline fails on first run”

✅ Explanation:

* APIs must be enabled **before** automation

---

## 9️⃣ Automation & best practice (ACE-level)

In real projects:

* Enable APIs early
* Enable via CLI or IaC
* Avoid enabling unused APIs (security & cost)

---

## 🔑 One-line exam memory hook

> **No API = no service**
> **IAM alone is never enough**

--- 

