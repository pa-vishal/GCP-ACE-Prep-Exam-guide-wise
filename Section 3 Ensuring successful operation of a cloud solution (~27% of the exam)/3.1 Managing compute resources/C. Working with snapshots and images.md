### **Section 3.1 – Managing compute resources**

#### **Working with snapshots and images**

*(create, view, delete images or snapshots; schedule a snapshot)*

![Image](https://docs.cloud.google.com/compute/docs/images/vm2.png)

![Image](https://docs.cloud.google.com/static/compute/images/creating-snapshot.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A2000/1%2A2W92T4KKoiE84Xk4F97Upg.jpeg)

This bullet is about **backup, reuse, and recovery** for Compute Engine. The ACE exam focuses on **knowing when to use snapshots vs images**, **how they’re used**, and **how to automate protection**—not on low-level disk mechanics.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Distinguish **snapshots vs images**
* Create, view, and delete each
* Choose **snapshot schedules** for automation
* Avoid confusing backups with high availability

> **Exam mindset:**
> *“Am I backing up data, or creating a reusable VM template?”*

---

## 2️⃣ Snapshots vs Images (MUST KNOW)

### 📸 **Snapshots**

**What they are**

* Incremental backups of **Persistent Disks**
* Stored in Cloud Storage (managed by Google)
* Can be **zonal or regional** (based on source disk)

**Use when**

* Backup and restore
* Point-in-time recovery
* Disaster recovery

**Exam signals**

* “Backup”
* “Restore disk”
* “Recover data”
* “Automate backups”

> **Key rule:**
> **Snapshots are for backup, not for standardizing builds**

---

### 🧱 **Images**

**What they are**

* Full VM disk templates
* Used to **create new VMs**
* Can be:

  * Public
  * Custom
  * Shared across projects

**Use when**

* Standardizing VM builds
* Creating many identical VMs
* Golden images

**Exam signals**

* “Reusable VM template”
* “Standard OS image”
* “Create many identical VMs”

> **Key rule:**
> **Images are for provisioning, not backups**

---

## 3️⃣ Creating snapshots (CLI – exam-relevant)

### Create a snapshot from a disk

```bash
gcloud compute disks snapshot my-disk \
  --snapshot-names=my-disk-snap-001 \
  --zone=us-central1-a
```

---

### View snapshots

```bash
gcloud compute snapshots list
```

---

### Delete a snapshot

```bash
gcloud compute snapshots delete my-disk-snap-001
```

> **Exam note:**
> Snapshots are **incremental**, but deletion does not break other snapshots.

---

## 4️⃣ Snapshot schedules (AUTOMATION – EXAM FAVORITE)

### What they are

* Policies that automatically create snapshots
* Attached to disks
* Support:

  * Daily / hourly schedules
  * Retention rules
  * Labels

**Use when**

* Production workloads
* Compliance requirements
* Regular backups

---

### Create a snapshot schedule (conceptual CLI)

```bash
gcloud compute resource-policies create snapshot-schedule daily-backups \
  --region=us-central1 \
  --daily-schedule \
  --start-time=01:00 \
  --retention-policy max-retention-days=7
```

Attach it to a disk:

```bash
gcloud compute disks add-resource-policies my-disk \
  --resource-policies=daily-backups \
  --zone=us-central1-a
```

> **ACE signal:**
> “Automate backups” → **Snapshot schedule**

---

## 5️⃣ Creating images (CLI – exam-relevant)

### Create an image from a disk

```bash
gcloud compute images create my-custom-image \
  --source-disk=my-disk \
  --source-disk-zone=us-central1-a
```

---

### List images

```bash
gcloud compute images list
```

---

### Delete an image

```bash
gcloud compute images delete my-custom-image
```

---

## 6️⃣ Restore scenarios (exam logic)

### Restore from snapshot

* Create a new disk from snapshot
* Attach disk to VM

### Create VM from image

* Use image during VM creation
* Often paired with:

  * Instance templates
  * MIGs

---

## 7️⃣ Snapshots & availability (IMPORTANT EXAM TRAP)

❌ Snapshots do **not** provide high availability
❌ Snapshots are **not live replicas**
❌ Restoring from snapshot requires time

> **Exam rule:**
> Backups ≠ availability

---

## 8️⃣ Decision table (MEMORIZE)

| Requirement            | Best Choice       |
| ---------------------- | ----------------- |
| Backup data            | Snapshot          |
| Point-in-time recovery | Snapshot          |
| Automate backups       | Snapshot schedule |
| Reusable VM template   | Image             |
| Standardize VM builds  | Image             |

---

## 9️⃣ Common ACE exam traps

❌ Using images as backups
❌ Forgetting snapshot automation
❌ Assuming snapshots replace regional disks
❌ Thinking deleting a snapshot deletes the disk

---

## 🔑 One-line ACE memory hooks

* **Snapshot = backup**
* **Image = template**
* **Schedule = automation**
* **Backups ≠ HA**

---
 
