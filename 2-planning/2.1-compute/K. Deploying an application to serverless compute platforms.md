Good catch again. This one is **extremely high-yield** on the ACE exam.

---

# **Section 2 – Planning and implementing a cloud solution (~30%)**

## **2.1 Planning and implementing compute resources**

### **Deploying an application to serverless compute platforms**

This bullet is about deploying workloads to:

* **Cloud Run**
* **Cloud Run functions (Cloud Functions Gen 2)**
* (Recognition-level) App Engine

The exam tests whether you know:

* When to choose serverless
* How deployment works
* How scaling behaves
* IAM + access configuration

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Deploy a container to Cloud Run
* Deploy function code to Cloud Run functions
* Configure:

  * IAM
  * Region
  * Scaling
* Choose serverless over VM/GKE when appropriate

> **Exam mindset:**
> *“We want minimal infrastructure management — what’s the fastest way to deploy this app?”*

---

# 2️⃣ What Counts as Serverless Compute

| Service             | Use Case                      |
| ------------------- | ----------------------------- |
| Cloud Run           | Containerized HTTP workloads  |
| Cloud Run functions | Event-driven functions        |
| App Engine          | PaaS apps (recognition-level) |

---

# 3️⃣ Deploying to Cloud Run (Container-based)

Cloud Run runs containers.

---

## Step 1 – Build and push image

```bash
docker build -t us-central1-docker.pkg.dev/PROJECT_ID/repo/app:v1 .
docker push us-central1-docker.pkg.dev/PROJECT_ID/repo/app:v1
```

---

## Step 2 – Deploy

```bash
gcloud run deploy my-service \
  --image=us-central1-docker.pkg.dev/PROJECT_ID/repo/app:v1 \
  --region=us-central1 \
  --platform=managed
```

You can configure:

* Memory
* CPU
* Min instances
* Max instances
* Service account

---

# 4️⃣ Deploying to Cloud Run functions (Event-driven)

Used when:

* Triggered by:

  * Pub/Sub
  * Cloud Storage
  * HTTP
  * Firestore
* Small logic units

Example:

```bash
gcloud functions deploy my-function \
  --runtime=python311 \
  --trigger-http \
  --region=us-central1
```

---

# 5️⃣ Cloud Run vs Cloud Run functions (MUST KNOW)

| Feature     | Cloud Run   | Cloud Run functions |
| ----------- | ----------- | ------------------- |
| Input       | Container   | Source code         |
| Use case    | Web APIs    | Event-driven        |
| Scaling     | Per request | Per event           |
| Flexibility | Higher      | Simpler             |

> **ACE rule:**
> Containerized microservice → Cloud Run
> Simple event trigger → Cloud Run functions

---

# 6️⃣ IAM for Serverless (VERY TESTED)

Two identities involved:

### 1️⃣ Service Identity (Outbound access)

* Assigned service account
* Used to access other GCP APIs

### 2️⃣ Invoker Permission (Inbound access)

Role:

```
roles/run.invoker
```

If public:

```
allUsers
```

> **ACE trap:**
> Forgetting invoker role = 403 error.

---

# 7️⃣ Scaling Behavior (EXAM FAVORITE)

Cloud Run:

* Scales to zero
* Scales based on request count
* Configurable concurrency

Cloud Run functions:

* Auto-scales based on events

> **Exam signal:**
> “Traffic spikes unpredictably” → serverless good fit.

---

# 8️⃣ Serverless vs GKE vs VM (Decision Logic)

| Requirement           | Best Option         |
| --------------------- | ------------------- |
| Full control over OS  | VM                  |
| Complex orchestration | GKE                 |
| Minimal ops           | Cloud Run           |
| Event-driven          | Cloud Run functions |

> **ACE rule:**
> Lowest operational overhead wins if requirements allow.

---

# 9️⃣ Common ACE Exam Scenarios

---

### Scenario 1

> “Deploy REST API with minimal infrastructure”

✅ Cloud Run

---

### Scenario 2

> “Trigger processing when file uploaded to Cloud Storage”

✅ Cloud Run functions

---

### Scenario 3

> “Application must scale to zero”

✅ Serverless

---

### Scenario 4

> “Users get 403 when calling Cloud Run”

✅ Grant `roles/run.invoker`

---

### Scenario 5

> “Cloud Run app cannot access Pub/Sub”

Check:

* Assigned service account
* IAM role granted

---

# 🔟 Common ACE Exam Traps

❌ Using GKE for simple HTTP API
❌ Forgetting region selection
❌ Forgetting invoker role
❌ Confusing scaling model with VM autoscaling
❌ Assigning overly broad service account roles

---

# 🔑 One-line ACE Memory Hooks

* **Serverless = minimal ops**
* **Cloud Run = containers**
* **Functions = events**
* **Invoker role controls access**
* **Scales to zero**

---
 
