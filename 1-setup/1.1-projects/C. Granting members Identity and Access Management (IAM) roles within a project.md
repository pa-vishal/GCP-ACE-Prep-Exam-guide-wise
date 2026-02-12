
### **Section 1.1 – Granting members Identity and Access Management (IAM) roles within a project**

![Image](https://d33wubrfki0l68.cloudfront.net/eaddeba5e864fe63444fe247f7a7277b427e42c2/ed88b/gcpimages/02-architecture/resource-hierarchy-overview.png)

![Image](https://docs.cloud.google.com/static/iam/img/iam-overview-basics.svg)

This bullet is **heavily tested** on the ACE exam. You’re expected to choose the **right role**, **right scope**, and **right identity type**—not to design enterprise IAM from scratch.

---

## 1️⃣ What the exam actually tests here

The ACE exam focuses on your ability to:

### ✅ Grant access at the **correct level**

* Project vs folder vs organization
* Project-level IAM is the **most common**

### ✅ Choose the **least-privilege role**

* Prefer **predefined roles**
* Avoid **primitive roles** unless explicitly required

### ✅ Identify **who** gets access

* User
* Group
* Service account

### ❌ What the exam does NOT test

* Writing custom IAM roles in depth
* Complex conditional IAM logic
* Organization-wide IAM strategy

---

## 2️⃣ IAM fundamentals (must be automatic for you)

### IAM = **Who + What + Where**

| Component | Meaning                            |
| --------- | ---------------------------------- |
| Member    | Who (user, group, service account) |
| Role      | What permissions                   |
| Resource  | Where (project in this bullet)     |

**IAM Binding**

```
member → role → project
```

---

## 3️⃣ Types of IAM members (exam-critical)

### 👤 User

* Individual identity
* Example: `user:alice@example.com`

### 👥 Group (**preferred in real life & exams**)

* Managed via Cloud Identity / Workspace
* Example: `group:devs@example.com`

> **Exam hint:**
> “Grant access to multiple users” → **Use a group**

---

### 🤖 Service Account

* Used by applications, VMs, GKE, Cloud Run
* Example: `serviceAccount:my-sa@project.iam.gserviceaccount.com`

> **Exam hint:**
> “Application needs access” → **Service account**

---

## 4️⃣ IAM role types (VERY exam-relevant)

### ❌ Primitive roles (legacy)

* `roles/viewer`
* `roles/editor`
* `roles/owner`

⚠️ **Overly broad**, avoid unless explicitly stated.

---

### ✅ Predefined roles (**exam default choice**)

* Fine-grained
* Service-specific

Examples:

* `roles/compute.admin`
* `roles/storage.objectViewer`
* `roles/logging.viewer`

> **If unsure, choose predefined**

---

### ⚙️ Custom roles

* Defined by admin
* Least privilege but **not common in ACE questions**

---

## 5️⃣ Granting IAM roles via CLI (gcloud)

### 🔹 Grant a role to a user at project level

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:alice@example.com" \
  --role="roles/viewer"
```

---

### 🔹 Grant a role to a group (best practice)

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="group:devs@example.com" \
  --role="roles/compute.admin"
```

---

### 🔹 Grant a role to a service account

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="serviceAccount:my-sa@my-project.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"
```

---

### 🔹 View IAM policy for a project

```bash
gcloud projects get-iam-policy my-project
```

---

## 6️⃣ Granting IAM via Console (exam-safe understanding)

Steps (conceptual):

1. Go to **IAM & Admin → IAM**
2. Select **Project**
3. Click **Grant Access**
4. Add member
5. Choose role
6. Save

> You will **not** be tested on exact UI clicks, only **intent and outcome**.

---

## 7️⃣ Common exam scenarios (with correct answers)

### Scenario 1

> “Grant read-only access to logs for a support engineer”

✅ Correct:

* Member: User or Group
* Role: `roles/logging.viewer`
* Scope: Project

---

### Scenario 2

> “Allow an application running on a VM to write to Cloud Storage”

✅ Correct:

* Member: Service Account
* Role: `roles/storage.objectAdmin`
* Scope: Project

---

### Scenario 3

> “Grant access to 20 developers without managing them individually”

✅ Correct:

* Use a **group**
* Bind role once at project level

---

## 8️⃣ IAM vs Org Policy (quick exam lock-in)

| Question intent     | Use        |
| ------------------- | ---------- |
| Grant permission    | IAM        |
| Restrict capability | Org Policy |

> If the question says **“allow”**, **“grant”**, **“access”** → IAM

---

## 9️⃣ Exam traps & mistakes

❌ Assign `Editor` when a predefined role exists
❌ Grant to users instead of groups
❌ Use service account for humans
❌ Confuse project IAM with folder IAM

---

## 🔑 One-line exam memory hook

> **IAM = who can do what on this project**

--- 
Yes — **identities *can* be granted IAM roles at the resource level**, and this is **explicitly tested on the ACE exam**, usually as a *“least privilege”* decision.

We are **still inside**:
**Section 1.1 → Granting members IAM roles within a project**
This clarification **will be included in the section HTML**.

---

## ✅ Short answer (exam-ready)

> **Yes.**
> IAM roles can be granted at **organization, folder, project, *and individual resource levels*** — **if the resource supports IAM**.

---

## 1️⃣ IAM scope hierarchy (full picture)

IAM can be applied at these levels:

```
Organization
 └── Folder
      └── Project
           └── Resource (bucket, VM, Cloud Run service, BigQuery dataset, etc.)
```

**Inheritance rule**

* Permissions **flow downward**
* Lower-level IAM **adds or narrows scope**, not permissions

---

## 2️⃣ Why resource-level IAM exists (exam logic)

Resource-level IAM is used when:

* You want **least privilege**
* You must **avoid granting access to the whole project**
* Only **one specific resource** should be accessible

> ACE exam keyword: **“only”**

---

## 3️⃣ Common GCP resources that support resource-level IAM

These are **very exam-relevant**:

| Resource                   | Example                |
| -------------------------- | ---------------------- |
| Cloud Storage bucket       | Object-level access    |
| BigQuery dataset/table     | Data access isolation  |
| Cloud Run service          | Invoke permission      |
| Pub/Sub topic/subscription | Publisher / Subscriber |
| Secret Manager secret      | Read/write secrets     |
| Compute Engine instance    | (limited, less common) |

---

## 4️⃣ Concrete examples (with CLI)

### 🪣 Example 1: Grant access to ONE Cloud Storage bucket

**Requirement**

> “Allow a user to read objects in one bucket only”

✅ Correct approach: **Resource-level IAM**

```bash
gcloud storage buckets add-iam-policy-binding my-bucket \
  --member="user:alice@example.com" \
  --role="roles/storage.objectViewer"
```

✔️ No access to other buckets
✔️ No project-wide permission

---

### 🚀 Example 2: Allow invoking ONE Cloud Run service

**Requirement**

> “Allow a service to call a specific Cloud Run service”

```bash
gcloud run services add-iam-policy-binding my-service \
  --member="serviceAccount:caller@project.iam.gserviceaccount.com" \
  --role="roles/run.invoker" \
  --region=us-central1
```

---

### 📊 Example 3: BigQuery dataset access

**Requirement**

> “Grant analytics team access to only one dataset”

```bash
bq add-iam-policy-binding my_dataset \
  --member="group:analytics@example.com" \
  --role="roles/bigquery.dataViewer"
```

---

## 5️⃣ Resource-level vs project-level (exam decision table)

| Requirement                     | Correct Level     |
| ------------------------------- | ----------------- |
| Access to everything in project | Project           |
| Access to one service           | Resource          |
| Least privilege                 | Resource          |
| Many similar resources          | Project or Folder |
| One-off exception               | Resource          |

---

## 6️⃣ ACE exam traps (very important)

❌ “IAM can only be applied at project level” → **False**
❌ “Use project IAM for a single bucket” → **Over-privileged**
❌ “Resource-level IAM replaces project IAM” → **False**

✔️ **Both can coexist**

---

## 7️⃣ How the ACE exam phrases this

Look for phrases like:

* “only this bucket”
* “single service”
* “specific resource”
* “without granting access to other resources”

👉 These phrases **strongly signal resource-level IAM**

---

## 🔑 Final exam memory hook

> **IAM scope answers “HOW MUCH”**
> **Project = broad**
> **Resource = precise**

---

If you have **more IAM counter-questions**, ask now.
Otherwise, give me the **next bullet under Section 1.1** when ready.


