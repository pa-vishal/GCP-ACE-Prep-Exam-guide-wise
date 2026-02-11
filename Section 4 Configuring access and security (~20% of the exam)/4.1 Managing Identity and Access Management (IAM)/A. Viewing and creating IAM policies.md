Perfect. We are now in:

# **Section 4 – Configuring access and security (~20%)**

## **4.1 Managing Identity and Access Management (IAM)**

### **Viewing and creating IAM policies**

This is **core ACE territory**. IAM is everywhere. Expect multiple questions from this subsection.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* View IAM policies at:

  * Organization
  * Folder
  * Project
  * Resource level
* Create or modify IAM bindings
* Understand:

  * Members
  * Roles
  * Bindings
* Apply **least privilege**

> **Exam mindset:**
> *“Who can do what on which resource?”*

---

# 2️⃣ IAM Policy Structure (MUST MEMORIZE)

An IAM policy consists of:

```
Policy
 └── Bindings
      ├── Role
      └── Members
```

### Binding format

```yaml
bindings:
- role: roles/storage.objectViewer
  members:
  - user:alice@example.com
  - serviceAccount:my-sa@project.iam.gserviceaccount.com
```

---

# 3️⃣ Members (Who)

IAM members can be:

* `user:`
* `group:`
* `serviceAccount:`
* `domain:`
* `allUsers`
* `allAuthenticatedUsers`

> **ACE trap:**
> `allUsers` = public access

---

# 4️⃣ Roles (What)

Three categories:

### 1️⃣ Basic roles (avoid in production)

* Owner
* Editor
* Viewer

### 2️⃣ Predefined roles (preferred)

* `roles/compute.admin`
* `roles/storage.objectViewer`
* `roles/run.invoker`

### 3️⃣ Custom roles (advanced; recognition-level)

> **ACE rule:**
> Use predefined roles for least privilege.

---

# 5️⃣ Viewing IAM policies

### Console:

IAM & Admin → IAM

### CLI:

```bash
gcloud projects get-iam-policy PROJECT_ID
```

For specific resource:

```bash
gcloud storage buckets get-iam-policy gs://my-bucket
```

> **Exam note:**
> You’re tested on **where policies live**, not CLI memorization.

---

# 6️⃣ Creating or Modifying IAM Policies

Conceptually, you:

* Add a binding:

  * Member + Role

CLI example:

```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:alice@example.com" \
  --role="roles/storage.objectViewer"
```

---

# 7️⃣ Policy Hierarchy (VERY IMPORTANT)

IAM follows inheritance:

```
Organization
  ↓
Folder
  ↓
Project
  ↓
Resource
```

Permissions granted higher up:

* Apply downward
* Cannot be removed at lower level (only overridden via deny policy)

> **ACE trap:**
> Project-level policy does not override Org-level grants.

---

# 8️⃣ Common ACE Exam Scenarios

### Scenario 1

> “User cannot access resource”

Check:

* IAM policy at project level
* Resource-level policy
* Inherited roles

---

### Scenario 2

> “Grant read access to one bucket only”

✅ Apply IAM at **bucket level**, not project level.

---

### Scenario 3

> “Multiple users need same permissions”

✅ Use **group** instead of individual users.

---

### Scenario 4

> “Prevent over-privileged users”

✅ Use predefined roles
❌ Avoid Owner/Editor

---

# 9️⃣ IAM Policy vs Role vs Member (COMMON TRAP)

| Term    | Meaning                   |
| ------- | ------------------------- |
| Policy  | Entire set of bindings    |
| Binding | Role + Members            |
| Role    | Collection of permissions |
| Member  | Identity                  |

---

# 🔟 Common ACE exam traps

❌ Granting Owner unnecessarily
❌ Using user accounts instead of groups
❌ Forgetting inheritance
❌ Granting at project when resource-level is safer
❌ Confusing IAM with Organization Policy

---

# 🔑 One-line ACE memory hooks

* **Member + Role = Binding**
* **Policy = list of bindings**
* **Hierarchy inherits downward**
* **Least privilege wins**
* **Groups over users**

---
 
