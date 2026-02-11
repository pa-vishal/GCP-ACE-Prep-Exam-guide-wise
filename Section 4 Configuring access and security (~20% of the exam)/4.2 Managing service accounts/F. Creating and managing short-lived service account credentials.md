Excellent — this is a **security-focused, exam-relevant bullet**.

# **Section 4 – Configuring access and security**

## **4.2 Managing service accounts**

### **Creating and managing short-lived service account credentials**

This topic is about **secure authentication without long-lived keys**.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Distinguish between:

  * Long-lived JSON keys
  * Short-lived access tokens
* Understand how short-lived credentials are generated
* Prefer short-lived credentials for security
* Recognize impersonation as the safer option

> **Exam mindset:**
> *“How do we authenticate securely without exposing credentials?”*

---

# 2️⃣ Long-lived vs Short-lived credentials (MUST KNOW)

| Type              | Risk Level | Recommended? |
| ----------------- | ---------- | ------------ |
| JSON key file     | High       | ❌ Avoid      |
| Short-lived token | Low        | ✅ Yes        |

---

## ❌ Long-lived keys (JSON)

* Downloaded key file
* Valid until manually revoked
* High breach risk if leaked

Example (not recommended):

```bash
gcloud iam service-accounts keys create key.json \
  --iam-account=my-sa@project.iam.gserviceaccount.com
```

> **ACE rule:**
> Avoid service account keys unless absolutely required.

---

# 3️⃣ Short-lived credentials (Recommended)

Short-lived credentials include:

* OAuth 2.0 access tokens
* Identity tokens
* Temporary tokens via impersonation

They:

* Expire automatically
* Reduce security exposure
* Do not require key storage

---

# 4️⃣ Service Account Impersonation (Primary Method)

Impersonation allows:

* A user or service account
* To generate temporary credentials
* For another service account

Requires role:

```
roles/iam.serviceAccountTokenCreator
```

Example:

```bash
gcloud auth print-access-token \
  --impersonate-service-account=my-sa@project.iam.gserviceaccount.com
```

This produces:

* Short-lived access token
* No JSON key file

> **ACE rule:**
> Impersonation = preferred for short-lived credentials.

---

# 5️⃣ Workload Identity (Recognition-level)

Used in:

* GKE
* Kubernetes workloads

Allows:

* Pod → impersonate service account
* No keys stored in containers

> **Exam signal:**
> “Kubernetes workload needs secure access” → Workload Identity

---

# 6️⃣ Identity Tokens vs Access Tokens (Awareness)

| Token Type     | Use                                        |
| -------------- | ------------------------------------------ |
| Access token   | Access Google APIs                         |
| Identity token | Authenticate to services (e.g., Cloud Run) |

Example identity token:

```bash
gcloud auth print-identity-token
```

---

# 7️⃣ Common ACE Exam Scenarios

---

### Scenario 1

> “Security team prohibits service account keys”

✅ Use impersonation
✅ Use Workload Identity

---

### Scenario 2

> “CI/CD pipeline needs temporary access”

✅ Grant Token Creator
✅ Use impersonation

---

### Scenario 3

> “Developer downloaded JSON key for production app”

❌ Not recommended
✅ Replace with attached service account or impersonation

---

### Scenario 4

> “Application running in GKE needs API access securely”

✅ Workload Identity (no key file)

---

# 8️⃣ Why short-lived credentials matter (Exam Framing)

Benefits:

* Reduced attack surface
* Automatic expiration
* No manual key rotation
* Centralized IAM control

> **ACE trap:**
> If question emphasizes security best practice → avoid key files.

---

# 9️⃣ Common ACE Exam Traps

❌ Generating JSON key when impersonation works
❌ Storing key in source code
❌ Not granting Token Creator role
❌ Thinking short-lived tokens require manual revocation

---

# 🔑 One-line ACE Memory Hooks

* **Keys are dangerous**
* **Short-lived > long-lived**
* **Impersonation is preferred**
* **Workload Identity for GKE**
* **Token Creator enables temporary access**

---
 
