### **Section 3.2 – Managing storage resources**

#### **Managing and securing objects in Cloud Storage buckets**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/GCS_Folders_Product_Slides.max-2200x2200.jpg)

![Image](https://media.licdn.com/dms/image/v2/D4D12AQFfAXD1WFNkvA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1727723095239?e=2147483647\&t=R6O7JADgRyndbAQr2xX-mBbQmTjnpsxKeVJ1vXKPyjo\&v=beta)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/architecture_with_GCP_services.max-1100x1100.png)

![Image](https://miro.medium.com/1%2AlSHH8XPviwVQkSOXstVRUA.png)

This bullet is **very high-yield**. The ACE exam tests whether you can **secure data at rest and in access paths**, choose **the right access control model**, and **avoid legacy or insecure patterns**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Manage **objects inside buckets**
* Control **who can access what**
* Choose **IAM vs ACLs** correctly
* Secure access **without making buckets public**
* Recognize **best practices** vs legacy patterns

> **Exam mindset:**
> *“Who can access this object, how, and for how long?”*

---

## 2️⃣ Cloud Storage hierarchy (foundation)

```
Project
 └── Bucket
      └── Object(s)
```

Key facts:

* Buckets are **globally unique**
* Objects inherit **bucket-level permissions**
* Security is usually enforced at the **bucket level**, not per object

---

## 3️⃣ Access control models (MUST KNOW)

### ✅ A. IAM (RECOMMENDED & EXAM DEFAULT)

**How it works**

* Grant roles to:

  * Users
  * Groups
  * Service accounts
* Permissions apply at:

  * Project
  * Bucket

**Common roles**

| Role                    | Purpose                      |
| ----------------------- | ---------------------------- |
| `storage.objectViewer`  | Read objects                 |
| `storage.objectCreator` | Upload objects               |
| `storage.objectAdmin`   | Full object control          |
| `storage.admin`         | Full bucket + object control |

> **ACE rule:**
> If the question says *secure*, *recommended*, or *best practice* → **IAM**

---

### ⚠️ B. ACLs (LEGACY – recognition only)

**How they work**

* Per-object permissions
* Fine-grained but **hard to manage**

**Exam expectation**

* Know ACLs exist
* Know they are **not recommended**

> **ACE trap:**
> Do **not** choose ACLs unless the question explicitly requires them.

---

## 4️⃣ Uniform bucket-level access (VERY IMPORTANT)

### What it does

* **Disables ACLs completely**
* Forces **IAM-only access**
* Simplifies security model

### Enable it (best practice)

```bash
gcloud storage buckets update gs://my-bucket \
  --uniform-bucket-level-access
```

> **ACE rule:**
> Uniform bucket-level access = **modern, secure default**

---

## 5️⃣ Object-level operations (exam-relevant)

### Upload objects

```bash
gcloud storage cp local.txt gs://my-bucket/
```

### List objects

```bash
gcloud storage ls gs://my-bucket/
```

### Delete objects

```bash
gcloud storage rm gs://my-bucket/local.txt
```

> **Exam note:**
> You are tested on **what is possible**, not CLI memorization.

---

## 6️⃣ Securing object access (KEY EXAM SCENARIOS)

### 🔐 A. Private buckets (default & preferred)

* No public access
* IAM-controlled

**Exam signal**

* “Sensitive data”
* “Internal access only”

---

### 🔗 B. Signed URLs (TEMPORARY ACCESS – EXAM FAVORITE)

**What they are**

* Time-limited URLs
* Grant access **without changing IAM**
* Ideal for:

  * Downloads
  * External users
  * Temporary sharing

**Exam signals**

* “Temporary access”
* “No IAM changes”
* “External client”

> **ACE rule:**
> Temporary access → **Signed URL**

---

### 🌍 C. Public access (USE WITH CAUTION)

* Makes objects publicly readable
* Not secure for sensitive data

**Exam signal**

* “Public website assets”
* “Images accessible by anyone”

> **Exam trap:**
> Never make a bucket public unless explicitly stated.

---

## 7️⃣ Encryption (exam awareness)

### Default behavior

* All objects are **encrypted at rest by Google**

### Optional

* Customer-managed keys (CMEK)

**ACE expectation**

* Know encryption is **on by default**
* CMEK only if explicitly required

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Securely store files and allow only a service account to read them”

✅ **IAM role: storage.objectViewer**

---

### Scenario 2

> “Grant a customer access to a file for 10 minutes”

✅ **Signed URL**

---

### Scenario 3

> “Simplify access control and remove ACL complexity”

✅ **Enable uniform bucket-level access**

---

### Scenario 4

> “Host public images for a website”

✅ **Public access (only if explicitly stated)**

---

## 9️⃣ Common ACE exam traps

❌ Using ACLs instead of IAM
❌ Making buckets public unnecessarily
❌ Granting `storage.admin` when `objectViewer` is enough
❌ Forgetting uniform bucket-level access
❌ Assuming signed URLs require IAM changes

---

## 🔑 One-line ACE memory hooks

* **IAM > ACLs**
* **Uniform access = best practice**
* **Signed URL = temporary access**
* **Private by default**

---
 
