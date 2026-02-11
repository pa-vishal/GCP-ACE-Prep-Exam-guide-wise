Excellent — these four bullets are tightly connected.
We’ll handle them cleanly but distinctly under:

# **Section 4 – Configuring access and security**

## **4.2 Managing service accounts**

---

# 1️⃣ Using service accounts in IAM policies with minimum permissions

This is about **least privilege for applications**.

---

## What the exam is testing

You should be able to:

* Grant only required roles to a service account
* Avoid:

  * Owner
  * Editor
* Scope roles correctly:

  * Organization
  * Project
  * Resource level

> **Exam mindset:**
> *“What is the smallest role that allows this workload to function?”*

---

## Correct pattern

Instead of:

❌ `roles/editor`

Use:

✅ `roles/storage.objectViewer`
✅ `roles/pubsub.publisher`
✅ `roles/run.invoker`

---

## Resource-level scoping (VERY TESTED)

If app needs access to one bucket only:

❌ Grant project-level role
✅ Grant role at bucket level

> **ACE rule:**
> Scope as narrowly as possible.

---

## Common exam trap

> “App needs to read BigQuery dataset”

❌ BigQuery Admin
✅ BigQuery Data Viewer

---

# 2️⃣ Assigning service accounts to resources

Creating a service account is not enough — you must **attach it** to the resource.

---

## Where SAs are assigned

| Resource       | How                          |
| -------------- | ---------------------------- |
| Compute Engine | Attach SA to VM              |
| Cloud Run      | Assign SA to service         |
| GKE            | Node SA or Workload Identity |
| App Engine     | Uses default SA              |

---

## Compute Engine example

```bash
gcloud compute instances create vm-1 \
  --service-account=my-sa@project.iam.gserviceaccount.com
```

> **ACE trap:**
> If VM uses default SA, changing another SA won’t affect it.

---

## Cloud Run example

```bash
gcloud run deploy my-service \
  --service-account=my-sa@project.iam.gserviceaccount.com
```

---

## Exam pattern

> “Application running on VM cannot access API”

Check:

* Is correct SA attached?
* Does SA have correct role?

---

# 3️⃣ Managing IAM permissions of a service account

Service accounts are IAM members like users.

---

## What you manage

* What roles the SA has
* At which level
* Whether it needs more or fewer permissions

---

## Example: Add role

```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:my-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

---

## Removing role

Use remove-iam-policy-binding.

---

## Exam scenario

> “Service account over-privileged”

✅ Remove unnecessary roles
✅ Use Recommender (Active Assist)

---

# 4️⃣ Managing service account impersonation

This is advanced but absolutely tested.

---

## What is impersonation?

Impersonation allows:

* A user or service account
* To temporarily act as another service account
* Without downloading keys

> **ACE rule:**
> Impersonation is safer than distributing keys.

---

## Required role

To impersonate a service account:

`roles/iam.serviceAccountTokenCreator`

---

## Use case

CI/CD pipeline:

* Needs temporary access
* Should not store JSON keys

Solution:

* Grant pipeline SA Token Creator role
* Use impersonation

---

## Example CLI

```bash
gcloud auth print-access-token \
  --impersonate-service-account=my-sa@project.iam.gserviceaccount.com
```

---

## Why impersonation is better than keys

| Keys           | Impersonation  |
| -------------- | -------------- |
| Long-lived     | Short-lived    |
| Risk if leaked | Safer          |
| Hard to rotate | No key storage |

> **ACE trap:**
> Prefer impersonation over key files.

---

# Common ACE Exam Scenarios

---

### Scenario 1

> “Application needs read-only storage access”

✅ Grant minimal predefined role
✅ Attach SA to resource

---

### Scenario 2

> “CI system needs temporary permissions”

✅ Use service account impersonation

---

### Scenario 3

> “VM cannot access Pub/Sub”

Check:

* Attached SA?
* SA has correct role?

---

### Scenario 4

> “Security wants to eliminate service account keys”

✅ Use impersonation

---

# 🔑 One-line ACE Memory Hooks

* **Least privilege always**
* **Attach SA to resource**
* **SA permissions = IAM roles**
* **Impersonation > JSON keys**
* **Token Creator enables impersonation**

---
 
