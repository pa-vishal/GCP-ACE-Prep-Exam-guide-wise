### **Section 2.1 – Selecting appropriate compute choices for a given workload**

*(Compute Engine, GKE, Cloud Run, Cloud Run functions, Knative serving)*

![Image](https://media.licdn.com/dms/image/v2/C5612AQHSUWNe_5LTXA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1627360695999?e=2147483647\&t=J9zZi8Pkcjig4cHyaePknZoDFTvVVYOHjQ2xN9ag9jo\&v=beta)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/CvKvRvF_v10-07-21.max-2000x2000.jpg)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/Choosing_between_Cloud_Functions_and_Cloud.max-1500x1500.jpg)

This is **one of the most heavily tested bullets in the entire ACE exam**.
The exam is not testing *how* to deploy yet — it’s testing whether you can **choose the right compute abstraction** given workload requirements.

---

## 1️⃣ What the ACE exam is REALLY testing here

The exam wants to see if you can map:

* **Workload characteristics**
  → to
* **Correct compute service**

This bullet is about **decision-making**, not configuration.

> **If you pick the wrong compute option, everything else is wrong.**

---

## 2️⃣ The five compute options (exam-level definitions)

### 🖥️ **Compute Engine (VMs)**

**What it is**

* Raw virtual machines
* Full OS control
* You manage patching, scaling, availability

**Key traits**

* Zonal or regional (with MIG)
* Long-running
* Stateful workloads allowed

**Use when**

* You need OS-level control
* Legacy applications
* Custom software not containerized

**Exam signals**

* “Custom OS”
* “Install custom software”
* “Lift-and-shift”
* “Persistent disk attached”

---

### ☸️ **Google Kubernetes Engine (GKE)**

**What it is**

* Managed Kubernetes
* You manage containers and cluster behavior
* Google manages control plane

**Key traits**

* High flexibility
* Supports complex microservices
* Steeper operational overhead than serverless

**Variants (exam awareness)**

* **Standard** → more control
* **Autopilot** → Google manages nodes

**Use when**

* Microservices
* Multiple containers
* Advanced orchestration
* Need portability across environments

**Exam signals**

* “Kubernetes”
* “Pods / services”
* “Microservices platform”
* “Container orchestration”

---

### 🚀 **Cloud Run**

**What it is**

* Fully managed **container-based serverless**
* You deploy a container
* Google manages everything else

**Key traits**

* Scales to zero
* Stateless
* HTTP-driven
* No cluster management

**Use when**

* Containerized app
* Event-driven or web APIs
* Want minimal ops

**Exam signals**

* “Containerized application”
* “HTTP endpoint”
* “Scale to zero”
* “No infrastructure management”

---

### ⚡ **Cloud Run functions** *(formerly Cloud Functions)*

**What it is**

* Function-as-a-Service (FaaS)
* Single-purpose code
* Triggered by events

**Key traits**

* No container management
* Short-lived execution
* Strong event integration

**Use when**

* Small pieces of logic
* Event-driven workloads
* Glue code

**Exam signals**

* “Triggered by Pub/Sub”
* “Triggered by Cloud Storage”
* “Single-purpose function”
* “Minimal code”

---

### 🔗 **Knative serving**

**What it is**

* Open-source serverless layer
* Underlies Cloud Run
* Often runs on GKE

**Key traits**

* Kubernetes-native serverless
* More control than Cloud Run
* More ops than Cloud Run

**Use when**

* You want Cloud Run–like behavior
* But need Kubernetes integration or customization

**Exam reality**

> **Rarely the best ACE answer unless explicitly mentioned**

---

## 3️⃣ The ACE decision table (MEMORIZE THIS)

| Requirement                  | Best Choice         |
| ---------------------------- | ------------------- |
| Full OS control              | Compute Engine      |
| Legacy app                   | Compute Engine      |
| Containers + orchestration   | GKE                 |
| Containers + no ops          | Cloud Run           |
| Event-driven small logic     | Cloud Run functions |
| Kubernetes-native serverless | Knative serving     |

---

## 4️⃣ The MOST IMPORTANT exam pattern

> **Default to the HIGHEST abstraction that meets requirements**

Meaning:

* Don’t choose GKE if Cloud Run works
* Don’t choose VMs if serverless works

---

## 5️⃣ Real ACE-style scenarios (with reasoning)

### Scenario 1

> “A legacy app needs a custom OS and runs continuously”

✅ **Compute Engine**

---

### Scenario 2

> “A REST API packaged as a container, low traffic, minimal ops”

✅ **Cloud Run**

---

### Scenario 3

> “Event-driven image processing when files are uploaded”

✅ **Cloud Run functions**

---

### Scenario 4

> “Dozens of microservices with service mesh requirements”

✅ **GKE**

---

### Scenario 5

> “Serverless containers tightly integrated with Kubernetes”

✅ **Knative serving**

---

## 6️⃣ Common ACE traps (VERY IMPORTANT)

❌ Choosing GKE “because it’s powerful”
❌ Using VMs when serverless fits
❌ Using Cloud Functions for long-running jobs
❌ Forgetting Cloud Run supports containers
❌ Ignoring operational overhead

---

## 7️⃣ One-line ACE memory hooks

* **VM = control**
* **GKE = orchestration**
* **Cloud Run = containers without ops**
* **Functions = events**
* **Knative = Kubernetes serverless**

---

## 8️⃣ How this bullet expands later in Section 2.1

This bullet is the **decision foundation** for upcoming bullets:

* Launching compute instances
* GKE cluster deployment
* Serverless event processing

If you get this wrong, everything else cascades.

---
 
