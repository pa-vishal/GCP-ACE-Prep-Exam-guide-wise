Excellent — this is a **very testable IAM concept**.

# **Section 4 – Configuring access and security**

## **4.1 Managing Identity and Access Management (IAM)**

### **Managing the various role types and defining custom IAM roles (basic, predefined, custom)**

This bullet tests whether you understand **role selection strategy**, not how to write YAML.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Differentiate:

  * Basic roles
  * Predefined roles
  * Custom roles
* Choose the safest option
* Apply **least privilege**
* Recognize when custom roles are appropriate

> **Exam mindset:**
> *“What is the safest role that satisfies this requirement?”*

---

# 2️⃣ The Three Role Types (MUST MEMORIZE)

| Role Type  | Scope            | Recommended?   |
| ---------- | ---------------- | -------------- |
| Basic      | Project-wide     | ❌ Avoid        |
| Predefined | Service-specific | ✅ Preferred    |
| Custom     | User-defined     | ⚠️ When needed |

---

# 3️⃣ Basic Roles (Legacy – High Risk)

### Examples:

* Owner
* Editor
* Viewer

### Why they are risky:

* Broad permissions
* Apply to entire project
* Not granular

> **ACE rule:**
> Avoid basic roles unless question explicitly says “full project control.”

---

### Exam trap:

If question says:

> “Grant access to manage Cloud Run only”

❌ Editor
✅ `roles/run.admin`

---

# 4️⃣ Predefined Roles (DEFAULT ANSWER)

Predefined roles:

* Created and maintained by Google
* Service-specific
* Granular

### Examples:

| Service   | Role Example                   |
| --------- | ------------------------------ |
| Compute   | `roles/compute.admin`          |
| Storage   | `roles/storage.objectViewer`   |
| Cloud Run | `roles/run.invoker`            |
| IAM       | `roles/iam.serviceAccountUser` |

> **ACE rule:**
> Use predefined roles unless explicitly limited.

---

# 5️⃣ Custom Roles (When to Use)

Custom roles:

* Created by organization
* Combine selected permissions
* Used when predefined roles are too broad

### Example use case:

User needs:

* Compute start/stop
* No ability to delete

No predefined role fits → create custom role.

---

# 6️⃣ Custom Role Characteristics (Exam Awareness)

Custom roles:

* Created at:

  * Organization level
  * Project level
* Contain:

  * Specific permissions
* Do NOT automatically update when Google adds new permissions

> **ACE trap:**
> Custom roles require maintenance.

---

# 7️⃣ Choosing the Right Role (Decision Logic)

### Step 1:

Is there a predefined role that fits?

→ YES → Use predefined

### Step 2:

Is predefined too broad?

→ YES → Consider custom role

### Step 3:

Does user need full project control?

→ Rare → Basic role

---

# 8️⃣ Organization vs Project-level Custom Roles

| Scope         | Visibility               |
| ------------- | ------------------------ |
| Org-level     | Usable across projects   |
| Project-level | Only within that project |

> **ACE signal:**
> “Used across multiple projects” → Org-level custom role

---

# 9️⃣ Common ACE Exam Scenarios

### Scenario 1

> “User needs to invoke Cloud Run service only”

✅ `roles/run.invoker`

---

### Scenario 2

> “User should manage Compute but not IAM”

❌ Editor
✅ `roles/compute.admin`

---

### Scenario 3

> “Predefined role gives too many permissions”

✅ Create custom role

---

### Scenario 4

> “Security team wants standardized roles across org”

✅ Org-level custom roles

---

# 🔟 Common ACE Exam Traps

❌ Defaulting to Editor
❌ Granting Owner for convenience
❌ Creating custom role unnecessarily
❌ Forgetting custom roles don’t auto-update
❌ Granting project-level when resource-level is enough

---

# 🔑 One-line ACE Memory Hooks

* **Basic = broad**
* **Predefined = preferred**
* **Custom = precise**
* **Least privilege always**
* **Avoid Editor unless absolutely necessary**

---
 
