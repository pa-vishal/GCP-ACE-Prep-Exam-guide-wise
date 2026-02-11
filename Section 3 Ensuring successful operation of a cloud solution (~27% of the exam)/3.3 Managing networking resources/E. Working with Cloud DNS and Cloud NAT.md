### **Section 3.3 – Managing networking resources**

#### **Working with Cloud DNS and Cloud NAT**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/image2_YjKkxEG.max-2000x2000.jpg)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AeLbxLVIfRIhsJau70AvtiA.png)

![Image](https://miro.medium.com/0%2Ad-i2Mnpi1iMgQbgA.png)

This bullet is **very high-yield** because it tests two things the ACE exam loves:

* **Name resolution (Cloud DNS)**
* **Outbound internet access without public IPs (Cloud NAT)**

Most exam questions here are framed as *“it can’t resolve a name”* or *“private VMs can’t reach the internet”*.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **what Cloud DNS does vs what Cloud NAT does**
* Know **when each is required**
* Recognize **private network scenarios**
* Avoid confusing **inbound vs outbound connectivity**

> **Exam mindset:**
> *“Is this a name-resolution problem or an internet-egress problem?”*

---

## 2️⃣ Cloud DNS (NAME RESOLUTION)

### What Cloud DNS is

* A **managed DNS service**
* Translates **names → IP addresses**
* Can be used for:

  * Public DNS
  * Private DNS inside a VPC

> **ACE rule:**
> Cloud DNS solves **“how do I find it?”**, not **“how do I reach it?”**

---

### Types of Cloud DNS zones (MUST KNOW)

#### 🌍 Public DNS zones

* Internet-facing
* Used for websites and public APIs

**Exam signals**

* “Public domain”
* “Website”
* “External users”

---

#### 🔒 Private DNS zones (VERY IMPORTANT)

* Only visible **inside a VPC**
* Used for:

  * Internal services
  * Private IP name resolution
  * Hybrid environments

**Exam signals**

* “Internal hostname”
* “Private service”
* “Not resolvable from internet”

> **ACE rule:**
> Internal-only names → **Private DNS zone**

---

### Cloud DNS common operations (exam awareness)

* Create DNS zone
* Add record sets (A, CNAME, etc.)
* Associate private zone with VPC

> You are **not tested** on record syntax—only **when to use DNS**.

---

## 3️⃣ Cloud NAT (OUTBOUND INTERNET ACCESS)

### What Cloud NAT is

* Provides **outbound internet access**
* For resources **without external IPs**
* Uses **private IP → shared public IP translation**

```
Private VM → Cloud NAT → Internet
```

> **ACE rule:**
> Cloud NAT = **egress only**, never inbound access.

---

### When Cloud NAT is required (EXAM FAVORITE)

Use Cloud NAT when:

* VMs have **no external IPs**
* VMs must:

  * Download packages
  * Call external APIs
  * Reach the internet
* You want **better security**

**Exam signals**

* “No public IPs”
* “Private VM”
* “Outbound internet access required”

---

## 4️⃣ What Cloud NAT does NOT do (EXAM TRAP)

❌ Does NOT allow inbound traffic
❌ Does NOT provide DNS
❌ Does NOT replace firewall rules

> **ACE trap:**
> You still need **firewall rules** to allow egress traffic.

---

## 5️⃣ Cloud DNS vs Cloud NAT (MUST MEMORIZE)

| Problem                          | Solution                    |
| -------------------------------- | --------------------------- |
| Name not resolving               | **Cloud DNS**               |
| Private VM can’t reach internet  | **Cloud NAT**               |
| External users can’t access VM   | External IP / Load Balancer |
| Internal service name resolution | Private DNS zone            |

---

## 6️⃣ How they work together (EXAM AWARENESS)

Very common architecture:

```
Private VM
 ├── Uses Private DNS to resolve names
 └── Uses Cloud NAT to reach internet
```

> **Exam signal:**
> “Private VMs with no external IPs need updates” → **DNS + NAT**

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “VM has no external IP and cannot download updates”

✅ **Cloud NAT**

---

### Scenario 2

> “Internal services need name resolution using private IPs”

✅ **Cloud DNS (private zone)**

---

### Scenario 3

> “Public website domain not resolving”

✅ **Cloud DNS (public zone)**

---

### Scenario 4

> “User expects Cloud NAT to allow inbound traffic”

❌ Wrong
✅ Use Load Balancer or external IP

---

## 8️⃣ Common ACE exam traps

❌ Using Cloud NAT for inbound access
❌ Expecting DNS to enable connectivity
❌ Forgetting firewall egress rules
❌ Using public DNS for internal services
❌ Assigning external IPs when NAT is required

---

## 🔑 One-line ACE memory hooks

* **DNS = names**
* **NAT = outbound internet**
* **Private VM + internet = NAT**
* **Internal names = private DNS**
* **NAT is outbound only**

---
 
