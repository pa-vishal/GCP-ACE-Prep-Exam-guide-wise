
### **Section 1.1 – Managing users and groups in Cloud Identity (manually and automated)**

![Image](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/cloud-identity-7.width-500.format-webp.webp)

![Image](https://architecture.learning.sap.com/public-sap-iam-sd-388b51a0bbd83720.svg)

This bullet is about **identity lifecycle**, not permissions. On the ACE exam, Cloud Identity almost always appears as the **correct prerequisite** for IAM at scale.

---

## 1️⃣ What Cloud Identity is (exam framing)

**Cloud Identity** is Google’s **identity management system** for:

* Users (employees, contractors)
* Groups (teams, roles)

It is:

* Separate from Google Cloud projects
* Integrated with IAM
* Required for **Organization-level setups**

> **Exam signal:**
> If you see *company*, *employees*, *centralized user management* → **Cloud Identity**

---

## 2️⃣ What the exam actually tests here

The ACE exam tests whether you can:

### ✅ Recognize WHEN Cloud Identity is needed

* Managing **multiple users**
* Using **groups** instead of individuals
* Centralizing identity outside projects

### ✅ Distinguish manual vs automated management

* Manual → small scale
* Automated → enterprise scale

### ❌ What it does NOT test

* Deep directory sync internals
* Writing identity federation scripts
* Google Workspace administration in depth

---

## 3️⃣ Managing users MANUALLY (small scale)

### Manual user creation (conceptual)

* Create users in **Cloud Identity Admin Console**
* Assign email & basic profile
* Users sign in with Google identity

**When this is acceptable**

* Small teams
* Temporary users
* Labs / learning environments

**Exam tip**

> “A startup with 5 engineers” → Manual is fine

---

## 4️⃣ Managing groups MANUALLY (best practice)

Groups:

* Represent **teams or roles**
* Used in IAM bindings

### Example groups

* `devs@example.com`
* `ops@example.com`
* `security@example.com`

**Why groups matter**

* Add/remove users **once**
* IAM bindings stay untouched

> **Exam gold rule:**
> *Always prefer groups over users*

---

## 5️⃣ Managing users & groups AUTOMATED (enterprise scale)

### A. Directory sync (most common)

* Sync from:

  * Active Directory
  * LDAP
* Users & groups auto-provisioned

**Use case**

> “Company already has on-prem directory”

---

### B. Identity federation (external IdP)

* Users authenticate via:

  * Azure AD
  * Okta
* No Google-managed passwords

**Use case**

> “Do not manage passwords in Google”

---

### C. Programmatic management (API / CLI)

Used when:

* CI/CD pipelines
* HR-driven provisioning

---

## 6️⃣ IAM integration (this is why Cloud Identity exists)

Cloud Identity itself **does not grant permissions**.

Flow:

```
Cloud Identity → Users & Groups
IAM → Permissions
```

**Example**

1. Create group `devs@example.com`
2. Add users to group
3. Grant IAM role to group at project level

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="group:devs@example.com" \
  --role="roles/compute.admin"
```

---

## 7️⃣ Exam scenarios (with correct thinking)

### Scenario 1

> “Grant access to 50 engineers without frequent IAM changes”

✅ Use:

* Cloud Identity group
* Single IAM binding

---

### Scenario 2

> “Automate onboarding/offboarding”

✅ Use:

* Directory sync or federation
* Group-based IAM

---

### Scenario 3

> “Contractor leaves the company”

✅ Action:

* Remove user from group
* IAM remains unchanged

---

## 8️⃣ Common exam traps

❌ Use individual users instead of groups
❌ Manage users inside each project
❌ Confuse Cloud Identity with IAM
❌ Think Cloud Identity assigns permissions

---

## 🔑 One-line exam memory hook

> **Cloud Identity = who exists**
> **IAM = what they can do**

---
 
