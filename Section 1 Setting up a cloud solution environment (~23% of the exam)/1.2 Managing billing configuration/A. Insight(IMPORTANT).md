Excellent question. This is **exactly how the ACE exam is structured**: same symptom, different root causes. The exam is really testing whether you can **mentally triage failures in the correct order**.

We are still inside **Section 1.2 → Creating one or more billing accounts**, and this clarification **will be included in the Section HTML**.

---

## 🎯 The ACE Failure-Diagnosis Mental Model (ORDER MATTERS)

When the exam says something like:

> “A new project is created but resources fail to start / deploy / work”

You should **mentally run this checklist in order**. This order reflects **how often the exam expects each cause**.

---

## 🥇 1. Billing account NOT linked (MOST COMMON)

### Symptom

* VM won’t start
* GKE / Cloud Run deployment fails immediately
* Error mentions billing or payment

### Root cause

* Project exists
* APIs enabled
* IAM correct
* **But no billing account linked**

### Why this is #1

* New projects **do not auto-link billing**
* Exam loves this trap

### Exam phrasing clues

* “New project”
* “Resources fail immediately”
* “Everything seems configured”

👉 **First thing to check: Billing**

---

## 🥈 2. Required API NOT enabled

### Symptom

* Permission-like errors
* “API has not been used in project”
* Service-specific failure

### Root cause

* Billing linked
* IAM correct
* **Service API disabled**

### Examples

* VM creation → Compute Engine API disabled
* GKE → Container API disabled
* Cloud Run → Run API disabled

### Exam phrasing clues

* Mentions a **specific service**
* Mentions “first time” or “new project”

👉 **Second thing to check: APIs**

---

## 🥉 3. IAM permissions missing or wrong

### Symptom

* Explicit “permission denied”
* User/service account cannot perform action

### Root cause

* Billing linked
* API enabled
* **IAM role missing / wrong scope**

### Examples

* User lacks `compute.admin`
* Service account lacks `storage.objectAdmin`

### Exam phrasing clues

* Mentions **who** is performing the action
* Mentions “access denied”

👉 **Third thing to check: IAM**

---

## 🟦 4. Quota exhausted (VERY common after scaling)

### Symptom

* Deployment worked before
* Suddenly fails when scaling
* Error mentions “quota exceeded” or “resource exhausted”

### Root cause

* Everything configured correctly
* **Quota limit hit**

### Examples

* CPU quota per region
* IP address quota
* Load balancer quota

### Exam phrasing clues

* “After scaling”
* “Suddenly fails”
* “Limit reached”

👉 **Fourth thing to check: Quotas**

---

## 🟪 5. Location / availability mismatch

### Symptom

* Service cannot be created in selected region
* “Service not available in this region”

### Root cause

* Service does not exist in that region
* Zonal vs regional mismatch

### Examples

* Trying to deploy a service in unsupported region
* Expecting zonal HA behavior

### Exam phrasing clues

* Mentions **region or zone**
* Mentions availability or locality

👉 **Fifth thing to check: Region / scope**

---

## 🟥 6. Organization Policy restriction (advanced but tested)

### Symptom

* Action denied despite correct IAM
* No obvious permission error
* Consistent failure across projects

### Root cause

* Org Policy blocks the configuration

### Examples

* External IPs blocked
* Restricted regions
* Restricted machine types

### Exam phrasing clues

* “Company-wide restriction”
* “Security policy”
* “Prevent creation”

👉 **Sixth thing to check: Org Policies**

---

## 🧠 MASTER EXAM ORDER (MEMORIZE THIS)

When **resources fail**, check in this order:

```
1. Billing
2. API enabled
3. IAM
4. Quotas
5. Region / availability
6. Org Policy
```

This order will correctly answer **~90% of ACE failure scenarios**.

---

## 🔑 One-line ACE memory hook

> **Money → API → Permission → Capacity → Location → Policy**

---

If you want, next we can:

* Do **5 exam-style questions** where you practice identifying the root cause
  or
* Move on to the **next bullet under Section 1.2**

Just tell me how you want to proceed.

