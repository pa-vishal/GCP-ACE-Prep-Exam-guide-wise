### **Section 2.1 – Choosing the appropriate storage for Compute Engine**

*(zonal Persistent Disk, regional Persistent Disk, Google Cloud Hyperdisk)*

![Image](https://docs.cloud.google.com/static/compute/images/repd-chart.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/AI-Hypercomputer-Architecture.max-2000x2000.jpg)

![Image](https://media2.dev.to/dynamic/image/width%3D800%2Cheight%3D%2Cfit%3Dscale-down%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fngvseqw4438j99isv2m5.png)

This bullet tests whether you can **match VM storage to availability, performance, and cost needs**. The ACE exam focuses on **zonal vs regional behavior** and **when higher-performance disks are justified**—not on deep IOPS math.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Choose **zonal vs regional** disks correctly
* Understand **availability implications** during zone failures
* Recognize **performance tiers** (standard vs balanced vs SSD vs Hyperdisk)
* Avoid overengineering

> **Exam mindset:**
> *“If this VM or zone fails, what happens to the data—and how fast does it need to be?”*

---

## 2️⃣ Zonal Persistent Disk (PD)

### What it is

* Disk lives in **one zone**
* Attached to VMs in the **same zone**
* Most common and **default choice**

### Characteristics

* Lowest cost
* High reliability within a zone
* Not automatically available if the **zone fails**

### Use when

* Single VM
* Non-critical workloads
* Can recreate data or restore from backup

### Exam signals

* “Single VM”
* “Cost-sensitive”
* “No strict HA requirement”

---

## 3️⃣ Regional Persistent Disk (PD)

### What it is

* Disk synchronously replicated across **two zones in a region**
* Can attach to VMs in either zone (typically via MIG failover)

### Characteristics

* Higher availability
* Higher cost than zonal PD
* Protects against **zone failure**

### Use when

* Stateful workload
* Requires **zone-level HA**
* Used with **regional MIGs**

### Exam signals

* “Survive zone failure”
* “Stateful production workload”
* “High availability within a region”

---

## 4️⃣ Google Cloud Hyperdisk (performance-focused)

### What it is

* Next-generation block storage
* Designed for **very high IOPS and throughput**
* Decouples performance from disk size

### Characteristics

* Extremely high performance
* More expensive
* Best for performance-critical databases

### Use when

* Latency-sensitive or I/O-heavy workloads
* Databases with unpredictable spikes

### Exam reality

> Hyperdisk is **rarely the default answer** unless performance is explicitly mentioned.

### Exam signals

* “High IOPS”
* “Low latency storage”
* “Performance spikes”

---

## 5️⃣ Disk choice decision table (MEMORIZE)

| Requirement             | Best Choice             |
| ----------------------- | ----------------------- |
| Cheapest, simple VM     | Zonal PD                |
| Survive zone failure    | Regional PD             |
| Stateful production VM  | Regional PD             |
| Extreme I/O performance | Hyperdisk               |
| General purpose         | Zonal PD (balanced/SSD) |

---

## 6️⃣ Attaching disks (CLI awareness)

### Create a VM with a zonal PD

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --boot-disk-size=100GB \
  --boot-disk-type=pd-balanced
```

---

### Create a regional PD

```bash
gcloud compute disks create my-regional-disk \
  --region=us-central1 \
  --replica-zones=us-central1-a,us-central1-b \
  --size=200GB
```

---

## 7️⃣ Availability implications (exam favorite)

* **Zonal PD** + VM failure → data unavailable until zone recovers
* **Regional PD** + zone failure → VM can fail over and reattach
* **Disk ≠ backup** → snapshots are still required

---

## 8️⃣ Common ACE exam traps

❌ Using zonal PD for stateful HA workloads
❌ Assuming regional PD protects against region failure
❌ Choosing Hyperdisk without performance justification
❌ Forgetting cost differences

---

## 🔑 One-line ACE memory hooks

* **Zonal PD = cheap & simple**
* **Regional PD = zone-level HA**
* **Hyperdisk = performance**

--- 
