
### **Section 1.1 – Confirming availability of products in geographical locations (e.g., regional, global)**

![Image](https://docs.cloud.google.com/static/docs/images/overview/regions-zones.svg)

![Image](https://www.economize.cloud/resources/images/gcp-regions-zones.webp)

This bullet is **quietly critical for the ACE exam**. Many questions hinge on whether you understand **where a service lives geographically** and what that implies for **latency, availability, and design choices**.

---

## 1️⃣ What this bullet really means (exam framing)

“Confirming availability of products” means:

* Knowing whether a service is:

  * **Global**
  * **Regional**
  * **Zonal**
* Making sure the service:

  * Exists in the required **region**
  * Matches **data residency** or **HA** requirements

> **Exam mindset:**
> *“Can this service run where I want it to run?”*

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you can:

### ✅ Identify the **scope** of a service

(Global vs Regional vs Zonal)

### ✅ Choose a service that meets **availability & locality requirements**

### ❌ What it does NOT test

* Exact region lists from memory
* Rare or newly launched regions
* Edge-case regional outages

---

## 3️⃣ The three location scopes (must be automatic)

### 🌍 Global services

* No region selection
* Automatically span Google’s global infrastructure
* High availability by design

**Examples**

* VPC networks
* Cloud Load Balancing (HTTP(S))
* Cloud IAM
* Cloud DNS (public)
* Artifact Registry (multi-region configs)

> **Exam clue:**
> If no region is mentioned in setup → likely **global**

---

### 📍 Regional services

* Deployed in **one region**
* High availability **within that region**
* Must choose region explicitly

**Examples**

* Cloud Run
* Cloud SQL (regional HA)
* GKE regional clusters
* Pub/Sub (regional)
* Subnets

> **Exam clue:**
> “Highly available within a region” → **Regional**

---

### 🧱 Zonal services

* Run in **one zone**
* Lower availability unless replicated

**Examples**

* Compute Engine VMs
* GKE zonal clusters
* Persistent Disk (zonal)

> **Exam clue:**
> “Single VM” or “single zone” → **Zonal**

---

## 4️⃣ Why this matters (exam logic)

### A. High availability questions

> “Service must survive a zone failure”

❌ Zonal service alone
✅ Regional or multi-zone setup

---

### B. Data residency questions

> “Data must remain in Europe”

✅ Choose a **region in Europe**
❌ Global service that stores data unpredictably

---

### C. Latency questions

> “Users in Asia need low latency”

✅ Deploy in Asia region
❌ Assume global service fixes latency automatically

---

## 5️⃣ How to confirm availability (practical ACE knowledge)

### 🔹 Via documentation / console (conceptual)

* Service creation screen shows:

  * Region selector
  * “Not available in this region” message

### 🔹 Via CLI (example for Compute Engine regions)

```bash
gcloud compute regions list
```

---

### 🔹 Check zones in a region

```bash
gcloud compute zones list --filter="region:us-central1"
```

---

### 🔹 Check service availability (conceptual)

* Some services:

  * Are **not available in all regions**
  * Have **limited regional rollout**

> ACE exam expects you to **recognize the need to check**, not memorize the list.

---

## 6️⃣ Common service-location pairings (exam favorites)

| Service       | Scope                                  |
| ------------- | -------------------------------------- |
| VPC Network   | Global                                 |
| Subnet        | Regional                               |
| VM            | Zonal                                  |
| Cloud Run     | Regional                               |
| Cloud SQL HA  | Regional                               |
| GKE Autopilot | Regional                               |
| BigQuery      | Multi-region or regional               |
| Cloud Storage | Multi-region, dual-region, or regional |

---

## 7️⃣ Real exam-style scenarios

### Scenario 1

> “A workload must survive a zone failure”

✅ Correct:

* Regional Cloud Run
* Regional GKE
* Multi-zone MIG

---

### Scenario 2

> “Application deployed without choosing region”

✅ Explanation:

* Global service (e.g., VPC, IAM)

---

### Scenario 3

> “Service not available in desired region”

✅ Correct action:

* Choose another region
* Or choose another service with wider availability

---

## 8️⃣ Common exam traps

❌ Assume all services are global
❌ Confuse zonal with regional HA
❌ Forget subnets are regional
❌ Think global means zero latency everywhere

---

## 🔑 One-line exam memory hook

> **VPC is global**
> **Subnets & Cloud Run are regional**
> **VMs are zonal**

---
 
