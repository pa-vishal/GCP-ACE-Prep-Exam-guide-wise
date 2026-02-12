### **Section 2.3 – Establishing network connectivity**

*(Cloud VPN, VPC Network Peering, Cloud Interconnect)*

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/Decision-Tree-Network-Connectivity_v09-18-.max-2000x2000.jpg)

![Image](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/cloud-vpn-overview-01.svg)

![Image](https://docs.aws.amazon.com/images/prescriptive-guidance/latest/integrate-third-party-services/images/p2_vpc-peering.png)

![Image](https://docs.aws.amazon.com/images/vpc/latest/peering/images/peering-intro-diagram.png)

This bullet tests whether you can **connect networks correctly based on distance, performance, cost, and reliability**. The ACE exam is decision-heavy here: **pick the simplest option that meets the requirements**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Choose **VPN vs Peering vs Interconnect**
* Understand **latency, bandwidth, and SLA tradeoffs**
* Avoid overengineering
* Recognize **when connectivity is NOT required**

> **Exam mindset:**
> *“What is being connected, how far apart are they, and how reliable must it be?”*

---

## 2️⃣ The three connectivity options (high-level)

| Option                 | Connects          | Over the internet?   | SLA          | Typical bandwidth        |
| ---------------------- | ----------------- | -------------------- | ------------ | ------------------------ |
| **Cloud VPN**          | On-prem ↔ GCP     | Yes (encrypted)      | Yes (HA VPN) | Up to ~3 Gbps per tunnel |
| **VPC Peering**        | GCP VPC ↔ GCP VPC | No (Google backbone) | No           | High (no hard cap)       |
| **Cloud Interconnect** | On-prem ↔ GCP     | No (private link)    | Yes          | 10–100 Gbps              |

---

## 3️⃣ Cloud VPN (MOST COMMON ACE ANSWER)

### What it is

* Encrypted IPSec tunnels over the public internet
* Quick to set up
* Two main types:

  * **Classic VPN** (legacy)
  * **HA VPN** (recommended)

### Use when

* Connecting **on-premises** to GCP
* Moderate bandwidth
* Cost-sensitive
* Fast setup required

### Exam signals

* “Hybrid connectivity”
* “On-premises to cloud”
* “Encrypted”
* “Quick setup”

> **ACE rule:**
> On-prem + simple + secure → **Cloud VPN**

---

### Exam awareness: HA VPN

* Uses **two tunnels**
* Requires **two external IPs**
* Provides **99.99% SLA**

---

## 4️⃣ VPC Network Peering (GCP ↔ GCP)

### What it is

* Private connectivity between **two VPCs**
* Uses Google’s internal backbone
* No encryption needed (private network)

### Use when

* Connecting **projects or VPCs inside GCP**
* Low latency, high bandwidth
* No transitive routing

### Exam signals

* “Two GCP projects”
* “Private communication”
* “No on-premises”

> **Exam trap:**
> VPC Peering does **not** support:
>
> * Transitive peering
> * Overlapping CIDR ranges

---

## 5️⃣ Cloud Interconnect (HIGH-END OPTION)

### What it is

* Dedicated private physical connection to Google
* Two flavors:

  * **Dedicated Interconnect**
  * **Partner Interconnect**

### Use when

* Very high bandwidth
* Low latency
* Mission-critical workloads
* Long-term hybrid connectivity

### Exam signals

* “High throughput”
* “Low latency”
* “Enterprise”
* “Dedicated connection”

> **ACE rule:**
> Only choose Interconnect when the question **explicitly demands** performance or SLA beyond VPN.

---

## 6️⃣ Decision table (MEMORIZE)

| Requirement                   | Best Choice        |
| ----------------------------- | ------------------ |
| On-prem ↔ GCP, simple         | Cloud VPN          |
| On-prem ↔ GCP, high bandwidth | Cloud Interconnect |
| GCP ↔ GCP private             | VPC Peering        |
| Fast, low cost                | Cloud VPN          |
| Enterprise, mission-critical  | Interconnect       |

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “Company wants secure connectivity from on-prem to GCP quickly”

✅ **Cloud VPN**

---

### Scenario 2

> “Two projects must communicate privately within GCP”

✅ **VPC Network Peering**

---

### Scenario 3

> “Low-latency, high-throughput hybrid connectivity required”

✅ **Cloud Interconnect**

---

## 8️⃣ Common ACE exam traps

❌ Using VPC Peering for on-prem
❌ Using Interconnect when VPN is sufficient
❌ Expecting peering to be transitive
❌ Overlooking CIDR overlap issues

---

## 🔑 One-line ACE memory hooks

* **On-prem → VPN or Interconnect**
* **GCP ↔ GCP → Peering**
* **High performance → Interconnect**
* **Simple & fast → VPN**

---
 
