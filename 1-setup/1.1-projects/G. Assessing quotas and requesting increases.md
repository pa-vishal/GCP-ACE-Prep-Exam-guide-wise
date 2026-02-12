
### **Section 1.1 – Assessing quotas and requesting increases**

![Image](https://docs.cloud.google.com/static/monitoring/images/quota-filter-by-quota-metric-region.png)

![Image](https://i.sstatic.net/PIsxL.png)

This bullet is **quietly high-value on the ACE exam**. Quotas are a **very common root cause** in scenario questions where “everything is configured correctly but still fails.”

---

## 1️⃣ What quotas are (exam framing)

**Quotas** are **hard limits** Google Cloud enforces to:

* Prevent accidental overuse
* Protect shared infrastructure
* Control cost and abuse

They apply to:

* API requests
* Resources (VMs, CPUs, IPs)
* Regional or global usage

> **Exam mindset:**
> If deployment fails **without a permission error**, think **quota**.

---

## 2️⃣ What the ACE exam actually tests here

The exam checks whether you can:

### ✅ Identify a quota-related failure

Typical phrases:

* “Quota exceeded”
* “Limit reached”
* “Request cannot be fulfilled”
* “Resource exhausted”

### ✅ Know **where quotas are applied**

* Project level
* Often **per region**
* Sometimes global

### ❌ What it does NOT test

* Exact numeric limits
* Negotiation timelines
* Advanced quota automation

---

## 3️⃣ Common quota types (exam favorites)

### 🔹 Compute Engine

* CPUs per region
* VM instances per region
* Static IP addresses

### 🔹 GKE

* Node pool limits (CPU-based)
* Regional resource limits

### 🔹 Networking

* Load balancers
* Forwarding rules
* VPN tunnels

### 🔹 APIs

* Requests per minute/day

---

## 4️⃣ How to assess quotas (CLI + console)

### 🔹 View project quotas (CLI)

```bash
gcloud compute project-info describe \
  --project=my-project
```

Look for:

* `quotas`
* `usage` vs `limit`

---

### 🔹 View quotas for a specific region

```bash
gcloud compute regions describe us-central1 \
  --project=my-project
```

---

### 🔹 View enabled API quotas

```bash
gcloud services list --enabled --project=my-project
```

(API-specific quotas are viewed in the API’s quota page)

---

## 5️⃣ Requesting quota increases (how it works)

### 🔹 Request via Console (exam-level understanding)

Flow:

1. Go to **IAM & Admin → Quotas**
2. Filter by service & region
3. Select quota
4. Click **Edit Quotas**
5. Submit request

> **Important exam fact**
> Quota increases are **not instant** and **require billing account**.

---

### 🔹 Requesting quota increases via CLI?

❌ **Not supported directly**

This is an exam trick:

> If asked “use CLI to request quota increase” → **Incorrect**

---

## 6️⃣ Quotas vs limits vs budgets (exam clarity)

| Term   | Meaning                         |
| ------ | ------------------------------- |
| Quota  | Hard enforced limit             |
| Limit  | General term (often quota)      |
| Budget | Cost alert, **not enforcement** |

❌ Budget alerts **do not stop resource creation**

---

## 7️⃣ Regional vs global quotas (VERY exam-relevant)

### Example

> “VM creation fails in us-central1 but works in us-east1”

✅ Correct explanation:

* **Regional quota exhausted**

---

### Compute Engine CPU quota example

* 24 CPUs allowed in `us-central1`
* Try to create 8 more → fails
* Create in another region → works

---

## 8️⃣ Real exam-style scenarios

### Scenario 1

> “All permissions correct, API enabled, still cannot create VM”

✅ Root cause:

* CPU quota exhausted

---

### Scenario 2

> “Load balancer creation fails unexpectedly”

✅ Root cause:

* Networking quota reached

---

### Scenario 3

> “Project suddenly fails after scaling”

✅ Root cause:

* Autoscaling hit quota limit

---

## 9️⃣ Best practices (ACE-level)

* Check quotas **before scaling**
* Request increases early
* Spread workloads across regions if needed

---

## 10️⃣ Common exam traps

❌ Confuse IAM errors with quota errors
❌ Assume quota increases are automatic
❌ Think budgets enforce limits
❌ Ignore regional nature of quotas

---

## 🔑 One-line exam memory hook

> **If it fails without a permission error → check quota**

--- 
