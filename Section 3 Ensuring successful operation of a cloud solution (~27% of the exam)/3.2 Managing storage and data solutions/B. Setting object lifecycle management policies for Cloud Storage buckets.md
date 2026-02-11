### **Section 3.2 – Managing storage resources**

#### **Setting object lifecycle management policies for Cloud Storage buckets**

![Image](https://cms.cloudoptimo.com/uploads/S3_Lifecycle_Transitions_dfffc45147.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/new-storage-classes-5ybb1.max-600x600.PNG)

![Image](https://miro.medium.com/1%2A7_SIMpU3Z2ucOH1oIQaKIQ.png)

This bullet is **cost-optimization + governance focused**. The ACE exam checks whether you can **automate object transitions and deletions** based on **age, state, or conditions**—instead of relying on manual cleanup.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **what lifecycle rules do**
* Choose **transition vs delete** actions
* Apply rules at the **bucket level**
* Use lifecycle policies to **reduce storage cost automatically**

> **Exam mindset:**
> *“How do I keep storage costs low without manual intervention?”*

---

## 2️⃣ What lifecycle management is (foundation)

**Lifecycle management** lets you define **rules** that automatically:

* **Transition** objects to cheaper storage classes
* **Delete** objects when they’re no longer needed

Rules are:

* Applied at the **bucket level**
* Evaluated **daily**
* Non-destructive until conditions are met

---

## 3️⃣ Actions you can take (MUST KNOW)

### 🔄 A. Transition storage class

Move objects to a cheaper class as they age.

**Common transitions**

* Standard → Nearline
* Nearline → Coldline
* Coldline → Archive

**Exam signals**

* “Reduce storage cost”
* “Infrequently accessed data”
* “Long-term retention”

---

### 🗑️ B. Delete objects

Automatically remove objects.

**Use when**

* Temporary data
* Compliance retention windows
* Log cleanup

**Exam signals**

* “Delete after X days”
* “No longer needed”

---

## 4️⃣ Conditions you can match on (EXAM FAVORITE)

Lifecycle rules trigger based on conditions like:

| Condition             | Meaning                        |
| --------------------- | ------------------------------ |
| `age`                 | Days since object creation     |
| `createdBefore`       | Objects created before a date  |
| `isLive`              | Current vs noncurrent versions |
| `matchesStorageClass` | Apply only to certain classes  |
| `numNewerVersions`    | Versioned object cleanup       |

> **ACE rule:**
> Age-based rules are the **most common and expected**.

---

## 5️⃣ Example lifecycle policy (VERY EXAM-RELEVANT)

### Policy example (JSON)

```json
{
  "rule": [
    {
      "action": { "type": "SetStorageClass", "storageClass": "COLDLINE" },
      "condition": { "age": 30 }
    },
    {
      "action": { "type": "Delete" },
      "condition": { "age": 365 }
    }
  ]
}
```

**Meaning**

* After 30 days → move to Coldline
* After 1 year → delete

---

## 6️⃣ Applying a lifecycle policy (CLI – exam-aware)

```bash
gcloud storage buckets update gs://my-bucket \
  --lifecycle-file=lifecycle.json
```

### View lifecycle rules

```bash
gcloud storage buckets describe gs://my-bucket
```

> **Exam note:**
> You’re tested on **what lifecycle policies do**, not JSON syntax memorization.

---

## 7️⃣ Lifecycle vs Versioning (IMPORTANT DISTINCTION)

* **Versioning**

  * Keeps older versions of objects
* **Lifecycle**

  * Manages what happens to those versions

**Common pattern**

* Enable versioning
* Use lifecycle rules to delete older versions

> **Exam signal:**
> “Clean up old versions automatically” → **Lifecycle + versioning**

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Reduce cost for logs older than 90 days”

✅ **Lifecycle rule: transition to Coldline**

---

### Scenario 2

> “Delete backup files after 7 years”

✅ **Lifecycle rule: delete after age condition**

---

### Scenario 3

> “Automate storage management without scripts”

✅ **Lifecycle management**

---

## 9️⃣ Common ACE exam traps

❌ Using cron jobs instead of lifecycle rules
❌ Thinking lifecycle rules apply per object manually
❌ Forgetting lifecycle rules are bucket-wide
❌ Using Archive for frequently accessed data
❌ Expecting instant transitions (rules run daily)

---

## 🔑 One-line ACE memory hooks

* **Lifecycle = automation**
* **Transition = cheaper storage**
* **Delete = cleanup**
* **Bucket-level rules**

---
 
