Got it — thanks for calling that out 👍
You’re right to expect the **full content** here. Let’s **cleanly and completely redo** the bullet so it’s safely captured for your Section 3 HTML.

---

### **Section 3.3 – Managing networking resources**

## **Adding custom static routes in a VPC**

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/2-vpcdefault-route.max-2200x2200.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/1-packet-next-hop-overview_v1.max-2200x2200.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A2000/1%2AxWnqlECbCkgVER7wlCUBNQ.png)

This bullet is about **controlling how traffic flows inside a VPC when the default routes are not enough**. On the ACE exam, this usually appears as *“traffic is going to the wrong place”* or *“send traffic through VPN / appliance”*.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **what a custom static route is**
* Know **when default routes are insufficient**
* Choose the correct **next hop**
* Understand **CIDR matching and priority**
* Distinguish **routes vs firewall rules**

> **Exam mindset:**
> *“Where should this traffic go next?”*

---

## 2️⃣ VPC routing basics (MUST KNOW)

When a VPC is created, Google Cloud automatically provides:

* **Subnet routes** (local traffic)
* **Default internet route**

  ```
  0.0.0.0/0 → default internet gateway
  ```

These are enough **until** you need:

* On-prem connectivity
* Traffic inspection
* Forced paths

---

## 3️⃣ What a custom static route is

A **custom static route**:

* Is **manually defined**
* Applies at the **VPC level**
* Overrides default routing behavior
* Decides **where traffic goes**, not whether it’s allowed

Each route has:

* **Destination CIDR**
* **Next hop**
* **Priority**
* (Optional) **Network tags**

> **ACE rule:**
> **Routes = path**, **firewall = allow/deny**

---

## 4️⃣ When you need custom static routes (EXAM SCENARIOS)

You add custom static routes when:

* Sending traffic to **on-premises networks**
* Routing through a **VPN tunnel**
* Forcing traffic through a **NAT / firewall appliance VM**
* Overriding the default internet gateway

**Exam signals**

* “On-prem CIDR”
* “Traffic must go through VPN”
* “Security appliance”
* “Custom routing”

---

## 5️⃣ Route matching rules (VERY IMPORTANT)

Google Cloud evaluates routes in this order:

### 1. **Longest prefix match**

* More specific CIDR wins
  (`10.0.0.0/8` beats `0.0.0.0/0`)

### 2. **Priority**

* Lower number = higher priority
* Used **only if CIDR length is equal**

> **ACE trap:**
> Priority does **not** override CIDR specificity.

---

## 6️⃣ Common next-hop types (MUST RECOGNIZE)

| Next hop                     | Typical use               |
| ---------------------------- | ------------------------- |
| **Default internet gateway** | Internet access           |
| **VPN tunnel**               | On-prem connectivity      |
| **VM instance**              | NAT / firewall appliance  |
| **Internal Load Balancer**   | Advanced routing patterns |

> **ACE rule:**
> On-prem traffic → **VPN tunnel next hop**

---

## 7️⃣ Creating a custom static route (CLI – exam-relevant)

### Example: route on-prem traffic through a VPN

```bash
gcloud compute routes create onprem-route \
  --network=my-vpc \
  --destination-range=192.168.0.0/16 \
  --next-hop-vpn-tunnel=my-vpn-tunnel \
  --priority=1000
```

What this does:

* Matches traffic destined for `192.168.0.0/16`
* Sends it through the VPN tunnel
* Overrides the default internet route

---

## 8️⃣ Scoping routes with network tags (exam awareness)

Routes can:

* Apply to **all VMs** (default), or
* Apply only to VMs with **specific network tags**

Use tags when:

* Only certain workloads should follow the route

> **Exam signal:**
> “Only backend VMs should use this path” → **use tags**

---

## 9️⃣ Routes vs firewall rules (COMMON EXAM TRAP)

| Component         | Controls                   |
| ----------------- | -------------------------- |
| **Route**         | Where traffic goes         |
| **Firewall rule** | Whether traffic is allowed |

> **ACE trap:**
> Traffic can be routed correctly and still be **blocked**.

---

## 🔟 Common ACE exam scenarios

### Scenario 1

> “Traffic to on-prem is going to the internet”

✅ **Add a custom static route with VPN tunnel as next hop**

---

### Scenario 2

> “Traffic must pass through a security appliance VM”

✅ **Custom route with next hop = VM instance**

---

### Scenario 3

> “Route exists but traffic still doesn’t flow”

✅ Check:

* CIDR specificity
* Priority
* Network tags
* Firewall rules

---

## 11️⃣ Common ACE exam traps

❌ Thinking routes replace firewall rules
❌ Using priority instead of CIDR specificity
❌ Creating a new VPC unnecessarily
❌ Forgetting routes are VPC-wide
❌ Expecting firewall rules to auto-update

---

## 🔑 One-line ACE memory hooks

* **Routes decide path**
* **Firewall decides allow/deny**
* **Longest prefix wins**
* **On-prem → VPN route**
* **Same CIDR → lower priority wins**

--- 
