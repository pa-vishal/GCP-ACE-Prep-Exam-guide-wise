### **Section 3.1 – Managing compute resources**

#### **Deploying new versions of a Cloud Run application**

![Image](https://miro.medium.com/v2/resize%3Afit%3A1200/0%2A_RHjDg-9VHr4egOR.png)

![Image](https://docs.cloud.google.com/static/run/docs/images/manage-traffic-tags.png)

![Image](https://miro.medium.com/1%2AHK-6wZeDBt0AnQog5VQpJg.png)

This bullet is **very high-yield**. The ACE exam tests whether you understand **how Cloud Run handles versions (revisions)** and **how traffic is safely moved between them**—not advanced CI/CD.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **what a revision is**
* Deploy a **new version safely**
* Control **traffic routing**
* Roll back **without redeploying**

> **Exam mindset:**
> *“How do I update a serverless app without downtime?”*

---

## 2️⃣ Core Cloud Run concepts (MUST KNOW)

### Revisions

* **Immutable versions** of a Cloud Run service
* Created on **every deploy** (code or config change)
* Multiple revisions can exist at once

```
Cloud Run Service
 ├── Revision v1
 ├── Revision v2
 └── Revision v3 (latest)
```

> **ACE rule:**
> You never “edit” a revision—you create a new one.

---

## 3️⃣ Deploying a new version (CLI – exam-relevant)

### Basic deploy (creates a new revision)

```bash
gcloud run deploy my-service \
  --image=us-central1-docker.pkg.dev/my-project/my-repo/my-app:v2 \
  --region=us-central1
```

What happens:

* New revision is created
* By default, **100% traffic** goes to the latest revision

> **Exam signal:**
> “Deploy new version” → **new revision**

---

## 4️⃣ Traffic management (VERY IMPORTANT)

Cloud Run supports **traffic splitting** across revisions.

### Split traffic during deploy

```bash
gcloud run deploy my-service \
  --image=... \
  --traffic=LATEST=90,REVISION=v1=10
```

### Update traffic only (no redeploy)

```bash
gcloud run services update-traffic my-service \
  --to-revisions=rev-v2=100
```

**Use cases**

* Canary deployments
* Gradual rollouts
* Instant rollback

> **ACE rule:**
> Traffic control ≠ redeploy

---

## 5️⃣ Rollbacks (EXAM FAVORITE)

### How rollback works

* Redirect traffic back to a **previous revision**
* No new build required

```bash
gcloud run services update-traffic my-service \
  --to-revisions=rev-v1=100
```

> **Exam signal:**
> “Rollback quickly” → **change traffic**

---

## 6️⃣ Blue/Green & Canary (conceptual)

* **Blue/Green**

  * Old revision (blue)
  * New revision (green)
  * Switch traffic instantly
* **Canary**

  * Small % to new revision
  * Monitor, then increase

> ACE expects **recognition**, not pipeline design.

---

## 7️⃣ What causes a new revision (EXAM TRAP)

A new revision is created if you change:

* Container image
* Environment variables
* Memory / CPU
* Concurrency
* Secrets or configs

> **Exam trap:**
> Even config-only changes create a new revision.

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Deploy a new version with zero downtime”

✅ **Deploy new revision + traffic control**

---

### Scenario 2

> “Roll back after errors are detected”

✅ **Shift traffic to previous revision**

---

### Scenario 3

> “Test new version with 10% of users”

✅ **Traffic splitting**

---

## 9️⃣ Common ACE exam traps

❌ Thinking Cloud Run overwrites the existing version
❌ Redeploying just to roll back
❌ Assuming only one version can exist
❌ Forgetting traffic defaults to latest

---

## 🔑 One-line ACE memory hooks

* **Deploy = new revision**
* **Revisions are immutable**
* **Traffic controls versions**
* **Rollback = traffic shift**

---

