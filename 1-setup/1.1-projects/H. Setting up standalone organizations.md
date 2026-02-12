
### **Section 1.1 – Setting up standalone organizations**

![Image](https://docs.cloud.google.com/resource-manager/img/multi-orgs.svg)

![Image](https://docs.cloud.google.com/static/resource-manager/img/cloud-hierarchy.svg)

This bullet is **subtle but exam-relevant**. It shows up when the exam wants to test your understanding of **organizations without Google Workspace / Cloud Identity domains**.

---

## 1️⃣ What a “standalone organization” means

A **standalone organization** is a Google Cloud **Organization resource** that is:

* **Not linked** to Google Workspace
* **Not linked** to Cloud Identity
* Owned by a **billing account**, not a domain

In short:

> **You get an Organization, but no managed users or groups**

---

## 2️⃣ When standalone organizations are created

A standalone organization is created when:

* You create projects **without** a Workspace or Cloud Identity domain
* You associate projects only with a **billing account**
* No verified domain exists

Typical users:

* Individuals
* Small teams
* Proof-of-concept environments
* Early-stage startups

---

## 3️⃣ What the ACE exam actually tests here

The exam checks whether you understand:

### ✅ Organizations can exist **without Cloud Identity**

### ✅ Standalone orgs have **limited identity features**

### ✅ Some enterprise features are **not available**

It does **not** test the exact console steps.

---

## 4️⃣ Key differences: standalone vs domain-backed org

| Feature                    | Standalone Org | Domain-backed Org |
| -------------------------- | -------------- | ----------------- |
| Organization resource      | ✅ Yes          | ✅ Yes             |
| Cloud Identity / Workspace | ❌ No           | ✅ Yes             |
| Managed users & groups     | ❌ No           | ✅ Yes             |
| Folder hierarchy           | ✅ Yes          | ✅ Yes             |
| Org policies               | ✅ Yes          | ✅ Yes             |
| IAM (users only)           | ✅ Yes          | ✅ Yes             |
| Groups in IAM              | ❌ No           | ✅ Yes             |

> **Big exam takeaway**:
> **No Cloud Identity → no groups**

---

## 5️⃣ IAM implications (very exam-relevant)

### In a standalone organization:

* IAM members are:

  * Google accounts (`user@gmail.com`)
* You **cannot**:

  * Create groups
  * Sync directories
  * Federate identities

**Result**

* IAM becomes **harder to manage at scale**

---

## 6️⃣ Why standalone orgs are NOT recommended for enterprises

Problems:

* No centralized user lifecycle
* No group-based IAM
* Hard to offboard users
* Manual IAM everywhere

**Exam signal**

> If the question mentions *enterprise*, *employees*, *central governance*
> ❌ Standalone org is the **wrong choice**

---

## 7️⃣ Converting standalone → domain-backed (conceptual)

You can:

* Attach a **Cloud Identity / Workspace domain**
* Migrate projects under it
* Gain:

  * Groups
  * Federation
  * Better IAM

> ACE exam expects you to know **this is possible**, not how to do it step-by-step.

---

## 8️⃣ Real exam-style scenarios

### Scenario 1

> “A single developer wants to use GCP with billing”

✅ Standalone organization is acceptable

---

### Scenario 2

> “Company wants group-based IAM and centralized control”

❌ Standalone organization
✅ Organization with Cloud Identity

---

### Scenario 3

> “IAM becomes unmanageable as team grows”

✅ Root cause:

* Standalone organization
* Missing Cloud Identity

---

## 9️⃣ Common exam traps

❌ Assume organizations require Workspace
❌ Assume standalone orgs support groups
❌ Confuse project-only setup with no organization
❌ Think standalone orgs block org policies

---

## 🔑 One-line exam memory hook

> **Standalone org = organization without identity**
 
