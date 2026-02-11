Perfect — moving forward in order.

# **Section 4 – Configuring access and security**

## **4.2 Managing service accounts**

### **Creating service accounts**

This is a **very high-frequency ACE topic**. Expect at least 1–2 questions involving service accounts.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain what a service account is
* Create one
* Assign IAM roles to it
* Know when to use it instead of a user
* Avoid overusing service account keys

> **Exam mindset:**
> *“What identity should this application use?”*

---

# 2️⃣ What is a Service Account?

A **service account (SA)** is:

* A **non-human identity**
* Used by:

  * Applications
  * VMs
  * Cloud Run
  * GKE
  * CI/CD systems

It authenticates to Google Cloud APIs.

---

# 3️⃣ Service Account vs User (MUST KNOW)

| Identity Type   | Used For           |
| --------------- | ------------------ |
| User account    | Human access       |
| Service account | Application access |

> **ACE rule:**
> Applications should NEVER use user credentials.

---

# 4️⃣ Creating a Service Account

### Console:

IAM & Admin → Service Accounts → Create

### CLI:

```bash
gcloud iam service-accounts create my-sa \
  --display-name="My Service Account"
```

This creates the identity — it has **no permissions yet**.

> **ACE trap:**
> Creating SA does NOT grant permissions automatically.

---

# 5️⃣ Assigning Roles to a Service Account

After creation, you must grant roles:

```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:my-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

> **ACE rule:**
> Service account permissions are granted via IAM like any member.

---

# 6️⃣ Attaching Service Accounts to Resources

Common use cases:

| Resource       | How SA is used            |
| -------------- | ------------------------- |
| Compute Engine | Attached to VM            |
| Cloud Run      | Assigned to service       |
| GKE            | Node or Workload Identity |
| App Engine     | Default service account   |

> **Exam signal:**
> “Application needs access to BigQuery” → assign role to its service account.

---

# 7️⃣ Default Service Accounts (VERY IMPORTANT)

Each project includes:

| Default SA                 | Purpose            |
| -------------------------- | ------------------ |
| Compute Engine default SA  | Used by VMs        |
| App Engine default SA      | Used by App Engine |
| Cloud Run service identity | Per service        |

⚠️ Default SAs often have broad permissions.

> **ACE trap:**
> Don’t overuse default service accounts in production.

---

# 8️⃣ Service Account Keys (SECURITY ALERT)

Service accounts can use:

* **Attached identity (preferred)**
* **Key files (JSON key)**

### Key files:

* Downloadable credentials
* Risky if leaked
* Should be avoided when possible

> **ACE rule:**
> Avoid long-lived keys. Use attached identity or Workload Identity.

---

# 9️⃣ Common ACE Exam Scenarios

### Scenario 1

> “Cloud Run app needs to read from Cloud Storage”

✅ Assign storage role to Cloud Run service account.

---

### Scenario 2

> “Application running on VM needs Pub/Sub access”

✅ Attach service account to VM with Pub/Sub role.

---

### Scenario 3

> “Developer wants to use JSON key for VM access”

❌ Not recommended
✅ Use attached service account

---

### Scenario 4

> “Application in GKE needs secure API access”

✅ Use Workload Identity (recognition-level)

---

# 🔟 Common ACE Exam Traps

❌ Using user credentials in app
❌ Forgetting to assign IAM role after creating SA
❌ Giving Owner role to service account
❌ Downloading and distributing keys unnecessarily
❌ Confusing service account creation with role assignment

---

# 🔑 One-line ACE Memory Hooks

* **Service accounts = app identities**
* **Create → then grant role**
* **Least privilege**
* **Avoid JSON keys**
* **Attach to resource when possible**

--- 
