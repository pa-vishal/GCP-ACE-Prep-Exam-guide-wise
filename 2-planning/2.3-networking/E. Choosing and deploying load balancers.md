
### **Section 2.3 – Choosing and deploying load balancers**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/Figure_3._Network_Load_Balancing.max-1800x1800.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/GCLB_7.max-1300x1300.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/image001rx5.max-700x700.PNG)

This bullet is **very high-yield**. The ACE exam mostly tests **which load balancer to choose**, not how to tune it. If you identify **traffic type (HTTP vs TCP)** and **scope (internal vs external, global vs regional)** correctly, you’ll get these questions right.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Pick the **correct load balancer type**
* Know **global vs regional** behavior
* Distinguish **internal vs external**
* Avoid overengineering

> **Exam mindset:**
> *“What kind of traffic is this, and who needs to reach it?”*

---

## 2️⃣ The load balancer families (lock this in)

Google Cloud load balancers fall into **two big buckets**:

| Category                  | Used for        |
| ------------------------- | --------------- |
| **Application (Layer 7)** | HTTP/HTTPS      |
| **Network (Layer 4)**     | TCP / UDP / SSL |

---

## 3️⃣ HTTP(S) Load Balancer (MOST TESTED)

### What it is

* Global, Layer-7 load balancer
* Routes traffic based on:

  * URL paths
  * Hostnames
* Terminates TLS

### Key characteristics

* **Global anycast IP**
* Built-in CDN
* Cross-region failover

### Use when

* Web applications
* REST APIs
* Global users

### Exam signals

* “HTTP/HTTPS traffic”
* “Global users”
* “URL-based routing”
* “High availability across regions”

✅ **Default answer for internet-facing web apps**

---

## 4️⃣ Internal HTTP(S) Load Balancer

### What it is

* Layer-7
* **Internal IP only**
* Regional

### Use when

* Internal microservices
* East-west traffic inside VPC

### Exam signals

* “Internal services”
* “Private access only”
* “No public exposure”

---

## 5️⃣ TCP/UDP Network Load Balancer

### What it is

* Layer-4
* Regional
* Pass-through load balancing

### Use when

* Non-HTTP traffic
* Legacy protocols
* Low latency

### Exam signals

* “TCP traffic”
* “UDP”
* “Non-HTTP workload”

---

## 6️⃣ Internal TCP/UDP Load Balancer

### What it is

* Private, regional
* Layer-4

### Use when

* Internal databases
* Backend services
* Private workloads

---

## 7️⃣ SSL Proxy / TCP Proxy Load Balancers (recognition-level)

### What they do

* Terminate SSL (SSL Proxy)
* Proxy TCP connections

### Exam expectation

* **Know they exist**
* Rarely the best ACE answer unless explicitly mentioned

---

## 8️⃣ Decision table (MEMORIZE)

| Requirement             | Best Choice           |
| ----------------------- | --------------------- |
| Internet-facing web app | HTTP(S) Load Balancer |
| Global users            | HTTP(S) Load Balancer |
| Internal web services   | Internal HTTP(S) LB   |
| TCP/UDP traffic         | Network Load Balancer |
| Internal TCP services   | Internal TCP/UDP LB   |

---

## 9️⃣ Deployment awareness (ACE-level)

### Typical backend types

* Managed Instance Groups
* GKE services
* Cloud Run services (via serverless NEG)

> **Exam note:**
> You are **not** tested on full LB configuration steps—only **selection logic**.

---

## 🔟 Common ACE exam scenarios

### Scenario 1

> “Serve HTTPS traffic to users worldwide with high availability”

✅ **HTTP(S) Load Balancer**

---

### Scenario 2

> “Expose internal microservices over HTTP”

✅ **Internal HTTP(S) Load Balancer**

---

### Scenario 3

> “Load balance TCP traffic to VMs”

✅ **Network Load Balancer**

---

## 11️⃣ Common ACE exam traps

❌ Using Network LB for HTTP apps
❌ Forgetting internal vs external distinction
❌ Assuming all load balancers are global
❌ Choosing complex proxies when HTTP(S) LB fits

---

## 🔑 One-line ACE memory hooks

* **HTTP traffic → HTTP(S) LB**
* **Global users → HTTP(S) LB**
* **Internal only → Internal LB**
* **Non-HTTP → Network LB**

--- 
