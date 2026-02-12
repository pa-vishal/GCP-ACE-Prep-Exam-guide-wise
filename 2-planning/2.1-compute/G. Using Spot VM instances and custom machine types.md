### **Section 2.1 – Using Spot VM instances and custom machine types**

![Image](https://media.licdn.com/dms/image/v2/C4E12AQEY-g214ga-bw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1520106422614?e=2147483647\&t=H66wEmsmyoFmkZrtaunW5WQVDuvkCXi0JhR79NCSvO8\&v=beta)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2A7ZOGlBdDTipma35E.jpg)

![Image](https://media2.dev.to/dynamic/image/width%3D800%2Cheight%3D%2Cfit%3Dscale-down%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fami5022dotytt5g3eeo2.png)

This bullet tests whether you can **optimize cost without breaking workloads**. The ACE exam checks that you understand **when interruption is acceptable** and **how to right-size VMs** instead of overpaying.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify **workloads that tolerate interruption** → Spot VMs
* Identify **workloads that need precise sizing** → Custom machine types
* Avoid using these options in **the wrong scenarios**

> **Exam mindset:**
> *“Can this workload stop unexpectedly?”* and *“Am I paying for unused CPU/RAM?”*

---

## 2️⃣ Spot VM instances (formerly Preemptible)

### What they are

* Deeply discounted VMs
* Can be **terminated at any time** by Google
* No SLA
* Maximum lifetime (can end sooner)

### Key characteristics

* Much cheaper than regular VMs
* Not suitable for stateful or critical workloads
* You **must expect interruption**

### Use when

* Batch jobs
* CI/CD workers
* Data processing
* Fault-tolerant workloads
* Stateless services behind autoscaling

### Exam signals

* “Cost-sensitive”
* “Fault-tolerant”
* “Batch processing”
* “Can retry jobs”

---

### CLI example (Spot VM)

```bash
gcloud compute instances create my-spot-vm \
  --zone=us-central1-a \
  --provisioning-model=SPOT
```

---

## 3️⃣ When NOT to use Spot VMs (exam traps)

❌ Production databases
❌ Stateful applications without replication
❌ Workloads requiring guaranteed uptime
❌ Anything that cannot handle sudden termination

> **Exam rule:**
> If the question says **“must not be interrupted”** → **NOT Spot**

---

## 4️⃣ Custom machine types

### What they are

* You choose:

  * Exact number of vCPUs
  * Exact amount of memory
* Instead of fixed shapes (e2-medium, n2-standard-4, etc.)

### Why they exist

* Avoid overpaying for unused resources
* Match workload requirements precisely

### Use when

* Workload needs:

  * More memory than standard shapes provide
  * Less CPU than a standard VM includes
* Cost optimization through right-sizing

### Exam signals

* “Overprovisioned”
* “Needs specific CPU/memory ratio”
* “Reduce cost without changing workload”

---

### CLI example (custom machine type)

```bash
gcloud compute instances create custom-vm \
  --zone=us-central1-a \
  --machine-type=custom-4-12288
```

*(4 vCPU, 12 GB RAM)*

---

## 5️⃣ Spot VMs + MIGs (important ACE pattern)

Spot VMs are commonly used with:

* **Managed Instance Groups**
* **Autoscaling**
* **Autohealing**

Why?

* Failed or preempted VMs are automatically replaced

> **Exam signal:**
> “Cheap, scalable, fault-tolerant” → **Spot VMs in a MIG**

---

## 6️⃣ Spot VMs vs Regular VMs (exam comparison)

| Feature              | Spot VM  | Regular VM |
| -------------------- | -------- | ---------- |
| Cost                 | Very low | Normal     |
| Interruption         | Anytime  | Rare       |
| SLA                  | ❌ No     | ✅ Yes      |
| Suitable for prod DB | ❌        | ✅          |

---

## 7️⃣ Custom machine types vs predefined (exam comparison)

| Requirement         | Best Choice |
| ------------------- | ----------- |
| Simple workload     | Predefined  |
| Exact sizing needed | Custom      |
| Cost optimization   | Custom      |
| Unsure requirements | Predefined  |

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Batch processing that can restart on failure and must be cheap”

✅ **Spot VM**

---

### Scenario 2

> “VM is underutilized; reduce cost without changing app”

✅ **Custom machine type**

---

### Scenario 3

> “Production workload must always be available”

❌ Spot
✅ Regular VM or MIG

---

## 9️⃣ Common ACE exam traps

❌ Using Spot VMs for stateful production workloads
❌ Assuming Spot VMs behave like regular VMs
❌ Overcomplicating with custom types when predefined fits
❌ Ignoring interruption risk

---

## 🔑 One-line ACE memory hooks

* **Spot = cheap but interruptible**
* **Custom = right-sized**

---
 
