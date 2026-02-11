### **Section 2.3 – Creating and applying Cloud Next Generation Firewall (Cloud NGFW) policies**

*(ingress & egress rules; action, source, destination, targets, protocols, ports)*

![Image](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-e-i.svg)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AGBHxqzbxkey7OgJTncZF7g.png)

![Image](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-11.svg)

This bullet is **heavily tested** because firewall rules are the **most common root cause of “it doesn’t work” networking questions**. The ACE exam checks that you understand **how rules are evaluated, what they apply to, and where to place them**—not advanced threat inspection.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Create **ingress vs egress** rules correctly
* Understand **rule components** (action, source, target, protocol, ports)
* Know **where rules apply** (VPC-wide vs targeted)
* Recognize **priority and default behavior**

> **Exam mindset:**
> *“Why is traffic blocked or allowed?”*

---

## 2️⃣ Core firewall concepts (must be automatic)

### 🔥 Cloud NGFW (VPC firewall rules)

* **Stateful** firewall
* Evaluated at the **VPC level**
* Apply to **VM network interfaces**
* Traffic is **denied by default** unless allowed

> **Exam trap:**
> “Internal traffic just works” → ❌ False without an allow rule

---

## 3️⃣ Ingress vs Egress (EXAM FAVORITE)

### ⬅️ Ingress rules

* Control **incoming** traffic to VMs
* Most commonly tested

**Example use cases**

* Allow SSH (tcp:22)
* Allow HTTP/HTTPS (tcp:80, 443)

---

### ➡️ Egress rules

* Control **outgoing** traffic from VMs
* Often forgotten but tested

**Example use cases**

* Restrict internet access
* Force traffic through NAT/proxy

> **Exam signal:**
> “VM cannot reach the internet” → egress rule or NAT

---

## 4️⃣ Firewall rule components (you must know all)

Every firewall rule has:

| Component             | Meaning                                  |
| --------------------- | ---------------------------------------- |
| **Direction**         | Ingress or Egress                        |
| **Action**            | Allow or Deny                            |
| **Priority**          | Lower number = higher priority           |
| **Source**            | (Ingress) CIDR / tags / service accounts |
| **Destination**       | (Egress) CIDR                            |
| **Target**            | Which VMs the rule applies to            |
| **Protocols / Ports** | tcp, udp, icmp, specific ports           |

> **Priority rule:**
> The **first matching rule wins**

---

## 5️⃣ Targets: tags vs service accounts (IMPORTANT)

### Network tags

* String labels on VMs
* Simple, common

### Service accounts

* Identity-based targeting
* More secure and auditable

**Exam signals**

* “Apply rule to a specific workload” → service account
* “Simple VM grouping” → network tags

---

## 6️⃣ Creating firewall rules (CLI – exam-relevant)

### Allow SSH (ingress)

```bash
gcloud compute firewall-rules create allow-ssh \
  --network=my-vpc \
  --direction=INGRESS \
  --priority=1000 \
  --action=ALLOW \
  --rules=tcp:22 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=ssh-enabled
```

---

### Allow outbound internet (egress)

```bash
gcloud compute firewall-rules create allow-egress-internet \
  --network=my-vpc \
  --direction=EGRESS \
  --priority=1000 \
  --action=ALLOW \
  --rules=all \
  --destination-ranges=0.0.0.0/0
```

---

## 7️⃣ Default firewall behavior (EXAM GOLD)

By default:

* **Ingress**: Denied
* **Egress**: Allowed (default rule exists)

> **Exam trap:**
> Deleting default egress rule can break internet access

---

## 8️⃣ Rule evaluation order (VERY IMPORTANT)

1. Lowest priority number first
2. First matching rule applies
3. If no rule matches → **deny**

> **Exam signal:**
> “Traffic unexpectedly blocked” → priority issue

---

## 9️⃣ Hierarchical firewall policies (exam awareness)

* Can be applied at:

  * Organization
  * Folder
  * Project
* Inherit downward
* Centralized control for enterprises

> ACE expects **recognition**, not deep configuration.

---

## 10️⃣ Common ACE exam scenarios

### Scenario 1

> “VM exists but cannot be reached via SSH”

✅ Check:

* Ingress rule
* Port 22
* Target tag or service account

---

### Scenario 2

> “Only one set of VMs should accept HTTP traffic”

✅ Use:

* Targeted firewall rule (tags or service account)

---

### Scenario 3

> “Traffic allowed despite deny rule”

✅ Cause:

* Lower-priority allow rule matched first

---

## 11️⃣ Common ACE exam traps

❌ Forgetting firewall rules are VPC-wide
❌ Using wrong direction (ingress vs egress)
❌ Ignoring priority
❌ Assuming internal traffic is allowed
❌ Confusing firewall rules with routes

---

## 🔑 One-line ACE memory hooks

* **Ingress = incoming**
* **Egress = outgoing**
* **Lowest priority number wins**
* **No rule = deny**

---
 
