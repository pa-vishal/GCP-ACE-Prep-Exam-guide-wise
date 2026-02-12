### **Section 2.2 – Choosing and deploying storage products**

*(Cloud Storage, Filestore, Google Cloud NetApp Volumes; Cloud Storage options: Standard, Nearline, Coldline, Archive)*

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/Which-Database_v03-22-23.max-2000x2000.jpg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/new-storage-classes-5ybb1.max-600x600.PNG)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/Storage-to-Use_v04-23-21.max-1600x1600.jpeg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/persistent_disk_sketchnotes.max-900x900.jpeg)

This bullet tests whether you can **separate object storage from file storage**, and then **optimize cost by choosing the correct storage class**. The ACE exam strongly favors **simple, correct choices** over overengineering.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Choose **object vs file storage**
* Pick the **right Cloud Storage class** based on access frequency
* Recognize **enterprise file storage needs**
* Avoid using databases or disks where storage services fit better

> **Exam mindset:**
> *“How is the data accessed, and how often?”*

---

## 2️⃣ Storage type mental model (MUST know)

### Object storage vs File storage

| Storage Type | Used for                        |
| ------------ | ------------------------------- |
| **Object**   | Unstructured data, blobs        |
| **File**     | POSIX-style shared file systems |

---

## 3️⃣ Cloud Storage (OBJECT storage – MOST TESTED)

### What it is

* Global object storage
* HTTP-based access
* Virtually unlimited scale
* Strong consistency

### Use when

* Images, videos, backups
* Static website assets
* Logs and exports
* Data lakes

**Exam signals**

* “Store files”
* “Unstructured data”
* “Global access”
* “Highly durable”

---

### Cloud Storage classes (EXAM FAVORITE)

| Class        | Access Pattern | Cost                           |
| ------------ | -------------- | ------------------------------ |
| **Standard** | Frequent       | Higher storage, low access     |
| **Nearline** | < 1/month      | Lower storage                  |
| **Coldline** | < 1/quarter    | Even lower                     |
| **Archive**  | Rare           | Lowest storage, highest access |

> **Hard rule:**
> Storage class ≠ location (region/multi-region)

---

### Lifecycle rules (exam awareness)

* Automatically transition objects between classes
* Based on age or conditions
* Used for cost optimization

---

## 4️⃣ Filestore (FILE storage)

### What it is

* Managed NFS file system
* Mounted by VMs and GKE
* Low latency, POSIX-compliant

### Use when

* Shared file systems
* Legacy applications
* Lift-and-shift workloads

**Exam signals**

* “Shared filesystem”
* “POSIX”
* “Multiple VMs access same files”

> ❌ Filestore is **not object storage**

---

## 5️⃣ Google Cloud NetApp Volumes (ENTERPRISE file storage)

### What it is

* Fully managed NetApp ONTAP
* Enterprise-grade file storage
* Supports:

  * NFS
  * SMB
  * Multiprotocol access

### Use when

* Enterprise NAS workloads
* SAP
* Large-scale file systems
* Migration from on-prem NetApp

**Exam signals**

* “Enterprise file storage”
* “NetApp”
* “NAS migration”

---

## 6️⃣ Decision table (MEMORIZE)

| Requirement              | Best Choice            |
| ------------------------ | ---------------------- |
| Unstructured objects     | Cloud Storage          |
| Frequently accessed data | Cloud Storage Standard |
| Rarely accessed backups  | Coldline / Archive     |
| Shared POSIX filesystem  | Filestore              |
| Enterprise NAS           | NetApp Volumes         |

---

## 7️⃣ Deployment awareness (ACE-level)

### Cloud Storage

```bash
gcloud storage buckets create gs://my-bucket \
  --location=us-central1
```

### Filestore

* Choose:

  * Region
  * Capacity
  * Performance tier
* Mounted via NFS

> CLI details are **not tested**, only **selection logic**

---

## 8️⃣ Common ACE exam traps

❌ Using Filestore for object storage
❌ Using Cloud Storage as a mounted filesystem
❌ Choosing Archive for frequently accessed data
❌ Confusing storage class with region
❌ Using databases for file storage

---

## 9️⃣ Real ACE-style scenarios

### Scenario 1

> “Store images accessed frequently by a web app”

✅ **Cloud Storage Standard**

---

### Scenario 2

> “Backups kept for years and rarely accessed”

✅ **Archive**

---

### Scenario 3

> “Legacy app needs shared filesystem across VMs”

✅ **Filestore**

---

### Scenario 4

> “Enterprise migrating NetApp workloads”

✅ **Google Cloud NetApp Volumes**

---

## 🔑 One-line ACE memory hooks

* **Cloud Storage = objects**
* **Filestore = shared files**
* **NetApp = enterprise NAS**
* **Archive = cheapest, slowest access**

--- 
