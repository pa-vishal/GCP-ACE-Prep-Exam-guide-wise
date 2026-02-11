Excellent — this is a **very exam-relevant bullet**, especially because it connects IAM + Kubernetes + secure workload identity.

# **Section 4 – Configuring access and security**

## **4.2 Managing service accounts**

### **Using a Google Cloud service account with a GKE application**

This is about **how a Pod in GKE securely authenticates to Google Cloud APIs**.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain how GKE workloads authenticate to GCP
* Understand:

  * Node service account (legacy)
  * Workload Identity (modern, preferred)
* Avoid using service account keys in containers

> **Exam mindset:**
> *“How does this Pod securely call Cloud Storage / Pub/Sub / BigQuery?”*

---

# 2️⃣ Two Ways GKE Can Use Service Accounts

There are **two models**:

| Method               | Recommended?      |
| -------------------- | ----------------- |
| Node service account | ⚠️ Legacy / broad |
| Workload Identity    | ✅ Preferred       |

---

# 3️⃣ ❌ Node Service Account (Older Model)

How it works:

* All Pods on a node inherit the node’s service account
* Node’s SA has IAM roles
* Any Pod can access those permissions

Problem:

* Over-permissioned
* Poor isolation

> **ACE trap:**
> If question mentions security best practice → avoid node SA method.

---

# 4️⃣ ✅ Workload Identity (Modern & Preferred)

Workload Identity:

* Maps:

  * Kubernetes Service Account (KSA)
  * To Google Service Account (GSA)
* Allows:

  * Pod-level identity
  * Least privilege
* No JSON keys required

---

# 5️⃣ Workload Identity Flow (High-Level)

```
Pod
 ↓
Kubernetes Service Account (KSA)
 ↓
Mapped to
 ↓
Google Service Account (GSA)
 ↓
Access Google APIs
```

Each Pod can have:

* Its own GSA
* Different IAM roles

> **ACE rule:**
> Workload Identity = fine-grained, secure access.

---

# 6️⃣ Steps Conceptually (Exam Awareness)

1. Create Google Service Account (GSA)
2. Grant IAM roles to GSA
3. Create Kubernetes Service Account (KSA)
4. Bind KSA → GSA
5. Deploy Pod using KSA

You are NOT tested on full YAML — just the concept.

---

# 7️⃣ Example Scenario

### Scenario:

> “GKE application needs to read from Cloud Storage”

Correct approach:

* Create GSA
* Grant `roles/storage.objectViewer`
* Use Workload Identity
* Attach KSA to Pod

---

# 8️⃣ Why Not Use JSON Keys in GKE?

Using JSON keys in Pods:

❌ Requires storing secrets
❌ Risk of leakage
❌ Hard to rotate

> **ACE rule:**
> Never embed service account keys in containers.

---

# 9️⃣ Common ACE Exam Scenarios

---

### Scenario 1

> “Multiple Pods need different permissions”

✅ Workload Identity

---

### Scenario 2

> “Security wants least privilege for each workload”

✅ Workload Identity

---

### Scenario 3

> “Application cannot access Pub/Sub from GKE”

Check:

* Is Workload Identity enabled?
* Does GSA have correct IAM role?
* Is KSA mapped correctly?

---

### Scenario 4

> “Developer wants to mount JSON key file in Pod”

❌ Not recommended
✅ Use Workload Identity

---

# 🔟 Node SA vs Workload Identity (MUST MEMORIZE)

| Feature     | Node SA    | Workload Identity |
| ----------- | ---------- | ----------------- |
| Granularity | Node-level | Pod-level         |
| Security    | Lower      | Higher            |
| Key files   | Possible   | Not required      |
| Recommended | No         | Yes               |

---

# 🔑 One-line ACE Memory Hooks

* **GKE Pod identity = Workload Identity**
* **No JSON keys**
* **Map KSA → GSA**
* **Least privilege per workload**
* **Node SA is legacy**

---
 Good — this is exactly the kind of thing the ACE exam likes to test at a **conceptual + operational level**.

You do NOT need to memorize every flag, but you must understand the flow.

---

# How Workload Identity Is Created (Step-by-Step)

We’ll break this into **5 logical steps**.

---

# 🧠 Big Picture

Workload Identity connects:

```
Kubernetes Service Account (KSA)
            ↓
Google Service Account (GSA)
            ↓
Google Cloud APIs
```

You are mapping Kubernetes identity → Google IAM identity.

---

# Step 1️⃣ Enable Workload Identity on the Cluster

When creating a GKE cluster (or updating it), you enable Workload Identity.

Example (conceptual):

```bash
gcloud container clusters create my-cluster \
  --workload-pool=PROJECT_ID.svc.id.goog
```

If cluster already exists:

```bash
gcloud container clusters update my-cluster \
  --workload-pool=PROJECT_ID.svc.id.goog
```

> Exam insight:
> If question says “secure GKE workload identity” → ensure Workload Identity is enabled.

---

# Step 2️⃣ Create a Google Service Account (GSA)

This is the GCP identity.

```bash
gcloud iam service-accounts create my-gsa
```

---

# Step 3️⃣ Grant IAM Roles to the GSA

Give it only required permissions:

```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:my-gsa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

> Remember: Least privilege always.

---

# Step 4️⃣ Create a Kubernetes Service Account (KSA)

Inside the cluster:

```bash
kubectl create serviceaccount my-ksa
```

This is the identity the Pod will use.

---

# Step 5️⃣ Bind KSA → GSA

This is the key mapping step.

You allow the Kubernetes SA to impersonate the Google SA:

```bash
gcloud iam service-accounts add-iam-policy-binding \
  my-gsa@PROJECT_ID.iam.gserviceaccount.com \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/my-ksa]" \
  --role="roles/iam.workloadIdentityUser"
```

Then annotate the KSA:

```bash
kubectl annotate serviceaccount my-ksa \
  iam.gke.io/gcp-service-account=my-gsa@PROJECT_ID.iam.gserviceaccount.com
```

Now they are linked.

---

# Step 6️⃣ Use the KSA in Your Pod

In your Pod spec:

```yaml
spec:
  serviceAccountName: my-ksa
```

Now the Pod can access GCP APIs using the mapped GSA.

No keys. No secrets.

---

# 🔐 What Actually Happens Under the Hood

When the Pod calls Google APIs:

1. It uses KSA token.
2. GKE exchanges it for a Google access token.
3. Google IAM verifies mapping.
4. Temporary credentials are issued.

All short-lived. No JSON keys.

---

# 🎯 What the ACE Exam Actually Cares About

You must know:

* Workload Identity replaces JSON keys.
* KSA maps to GSA.
* `roles/iam.workloadIdentityUser` enables impersonation.
* It provides Pod-level isolation.
* It’s more secure than node-level service accounts.

You are NOT expected to memorize the exact flags.

---

# 🚨 Common Exam Traps

❌ Using default node service account
❌ Mounting JSON key in container
❌ Forgetting to grant workloadIdentityUser role
❌ Granting permissions to wrong service account
❌ Forgetting to enable workload pool on cluster

---

# 🧠 Decision Pattern (Exam Shortcut)

If the question says:

* “Securely allow GKE workload to access GCP API”
* “Avoid storing credentials”
* “Least privilege per workload”

→ **Workload Identity**

---

# 🔑 One-line Memory Hook

**Enable cluster → Create GSA → Grant role → Create KSA → Bind → Deploy Pod**

---
 
