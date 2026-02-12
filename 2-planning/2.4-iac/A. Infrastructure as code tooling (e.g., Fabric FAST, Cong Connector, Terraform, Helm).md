### **Section 2.4 – Infrastructure as code (IaC) tooling**

*(Fabric FAST, Config Connector, Terraform, Helm)*

![Image](https://www.altexsoft.com/static/blog-post/2023/11/243035af-1e47-41ca-8b2d-43f42d3de5b9.jpg)

![Image](https://docs.cloud.google.com/static/docs/terraform/images/managing-infrastructure-as-code-infrastructure.svg)

![Image](https://miro.medium.com/1%2AdV7Kec1af1Y1W250Z9FtIA.jpeg)

![Image](https://media.licdn.com/dms/image/v2/D5612AQFsMQUvk0qEcQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1714535117772?e=2147483647\&t=lRLPNDI58CR3D67FLMTOf3E6fOf97nBRK_9gDguG5tY\&v=beta)

This bullet is about **tool selection**, not syntax mastery. The ACE exam checks whether you can **identify the right IaC tool for the environment and workflow** and understand **what each tool manages best**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Recognize **why IaC is used** (repeatability, versioning)
* Choose the **right IaC tool** based on:

  * Scope (cloud-wide vs Kubernetes)
  * Team workflow
  * Existing tooling
* Avoid mixing tools unnecessarily

> **Exam mindset:**
> *“What’s the simplest, standard tool to manage this infrastructure declaratively?”*

---

## 2️⃣ Why Infrastructure as Code matters (exam framing)

IaC allows you to:

* Define infrastructure **declaratively**
* Version infrastructure changes (Git)
* Reproduce environments reliably
* Automate deployments and rollbacks

> **ACE signal:**
> “Repeatable”, “automated”, “consistent environments” → **IaC**

---

## 3️⃣ The four IaC tools you must recognize

### 🧱 **Terraform** (MOST TESTED)

**What it is**

* Declarative IaC tool by HashiCorp
* Uses `.tf` files
* Manages **Google Cloud resources directly**

**Best for**

* Projects, networks, IAM
* Compute, GKE, Cloud SQL
* Cross-cloud infrastructure

**Exam signals**

* “Industry standard IaC”
* “Manage GCP resources”
* “Multi-cloud”

> **ACE default choice:**
> If no constraint is given → **Terraform**

---

### ☸️ **Helm**

**What it is**

* Package manager for Kubernetes
* Deploys applications **into clusters**
* Uses Helm charts (YAML templates)

**Best for**

* Kubernetes applications
* Reusable app deployments
* Managing releases in GKE

**Exam signals**

* “Deploy applications to Kubernetes”
* “Reusable Kubernetes templates”

> **Important:**
> Helm does **not** create GCP infrastructure like VPCs.

---

### 🔗 **Config Connector**

**What it is**

* Kubernetes-native IaC for Google Cloud
* GCP resources defined as **Kubernetes CRDs**
* Managed via `kubectl`

**Best for**

* Teams already using Kubernetes
* Managing GCP resources *from inside* GKE

**Exam signals**

* “Manage GCP resources using Kubernetes”
* “Kubernetes-native approach”

> **ACE expectation:**
> Recognition-level understanding (not deep usage).

---

### 🧩 **Fabric FAST** (recognition-level)

**What it is**

* Opinionated **Terraform-based framework**
* Provides pre-built modules
* Accelerates enterprise GCP deployments

**Best for**

* Large organizations
* Standardized environments
* Faster, consistent rollouts

**Exam signals**

* “Enterprise standards”
* “Pre-built Terraform modules”

---

## 4️⃣ Decision table (MEMORIZE)

| Requirement                 | Best Tool        |
| --------------------------- | ---------------- |
| Manage GCP infrastructure   | Terraform        |
| Deploy apps to GKE          | Helm             |
| Kubernetes-native GCP mgmt  | Config Connector |
| Enterprise standardized IaC | Fabric FAST      |
| Multi-cloud IaC             | Terraform        |

---

## 5️⃣ Tool boundaries (VERY exam-relevant)

| Tool             | Manages                      |
| ---------------- | ---------------------------- |
| Terraform        | GCP infrastructure           |
| Helm             | Kubernetes applications      |
| Config Connector | GCP infra via Kubernetes     |
| Fabric FAST      | Terraform modules & patterns |

> **Exam trap:**
> Helm ≠ infrastructure provisioning for VPCs or projects

---

## 6️⃣ IaC state & lifecycle (exam awareness)

### Terraform state

* Tracks:

  * What exists
  * What needs to change
* Stored locally or remotely (e.g., Cloud Storage)

### Why state matters

* Prevents drift
* Enables safe updates

> ACE expects **conceptual awareness**, not backend config.

---

## 7️⃣ Real ACE-style scenarios

### Scenario 1

> “Provision VPCs, subnets, and IAM in a repeatable way”

✅ **Terraform**

---

### Scenario 2

> “Deploy the same app to multiple GKE clusters”

✅ **Helm**

---

### Scenario 3

> “Manage Cloud SQL and Pub/Sub using Kubernetes manifests”

✅ **Config Connector**

---

### Scenario 4

> “Enterprise wants standardized GCP landing zones quickly”

✅ **Fabric FAST**

---

## 8️⃣ Common ACE exam traps

❌ Using Helm to create GCP networks
❌ Choosing Config Connector without Kubernetes
❌ Overcomplicating with multiple IaC tools
❌ Forgetting IaC implies version control

---

## 🔑 One-line ACE memory hooks

* **Terraform = infra**
* **Helm = apps**
* **Config Connector = Kubernetes-native infra**
* **Fabric FAST = enterprise Terraform**

---
 
