
### **Section 1.1 – Applying organizational policies to the resource hierarchy**

![Image](https://docs.cloud.google.com/resource-manager/img/org-policy-inheritance.svg)

![Image](https://docs.cloud.google.com/resource-manager/img/org-policy-concepts.svg)

This bullet is about **preventing bad things from ever being created**, not granting access. On the exam, this is often confused with IAM—**they are different**.

---

## 1️⃣ What are Organization Policies?

**Organization Policies (Org Policies)** are **guardrails** that:

* Restrict **what configurations are allowed**
* Apply across **Organization → Folder → Project**
* Enforce **compliance, security, and cost controls**

> **Think:** “What is allowed or denied?”
> Not “Who can do it?”

---

## 2️⃣ How Org Policies work (core mechanics)

### Policy structure

* Defined using **constraints**
* Applied at:

  * Organization
  * Folder
  * Project

### Inheritance model

* Policies **inherit downward**
* **More restrictive** policies override less restrictive ones

```
Org Policy
 └── Folder Policy (stricter)
      └── Project Policy (strictest wins)
```

---

## 3️⃣ Types of constraints (VERY exam-relevant)

### **A. Boolean constraints**

On / Off rules

**Examples**

* Disable external IPs on VMs
* Disable service account key creation
* Disable serial port access

**Example logic**

> “Do not allow external IPs on any VM in prod”

---

### **B. List constraints**

Allow or deny **specific values**

**Examples**

* Allowed regions
* Allowed machine types
* Allowed load balancer types

**Example**

> Only allow deployments in `us-central1` and `us-east1`

---

## 4️⃣ Where policies are applied (decision logic)

| Requirement           | Apply Policy At |
| --------------------- | --------------- |
| Company-wide rule     | Organization    |
| Environment-specific  | Folder          |
| Exception for one app | Project         |

**Exam pattern**

> “Enforce security for all projects except one”
> ✔️ Apply at **folder**, override at **project**

---

## 5️⃣ Common high-value org policy use cases

### 🔒 Security

* Block external IPs
* Prevent public Cloud Storage buckets
* Restrict service account key creation

### 💰 Cost control

* Limit regions
* Limit machine families
* Prevent large GPU types

### 📜 Compliance

* Restrict data residency
* Enforce CMEK usage

---

## 6️⃣ How this differs from IAM (frequent exam trap)

| IAM                | Org Policy          |
| ------------------ | ------------------- |
| WHO can act        | WHAT is allowed     |
| Identity-based     | Configuration-based |
| Grants permissions | Restricts behavior  |

> **If the question says “prevent” or “restrict” → Org Policy**

---

## 7️⃣ Real-world scenario

**Scenario**

> A company must ensure that **production workloads never have public IPs**, but dev teams can experiment.

**Correct solution**

* Org → no policy
* Dev folder → allow external IPs
* Prod folder → **deny external IPs**

This avoids manual policing and mistakes.

---

## 8️⃣ Exam traps & misconceptions

❌ “Org policies replace IAM” → False
❌ “Org policies only work at org level” → False
❌ “Project policy can loosen an org restriction” → False

✔️ **Stricter always wins**

---

## 9️⃣ One-line exam memory hook

> **Org Policies = guardrails**
> **IAM = keys to the car**

---
Great questions. These are **exactly** the angles the ACE exam tests on this bullet. I’ll answer them **explicitly in exam terms**, then give you **real policy samples + CLI**, and finally **lock the folder vs project behavior** so there’s no ambiguity. Everything below will be included in the **Section 1 HTML**.

We are still inside:  
**Section 1.1 → Applying organizational policies to the resource hierarchy**

----------

## 1️⃣ What does the ACE exam _actually_ test here?

The ACE exam does **NOT** test:

-   Writing complex YAML from memory
    
-   Memorizing constraint names
    

The ACE exam **DOES** test whether you can:

### ✅ Identify WHEN to use Org Policies (vs IAM)

Typical exam phrasing:

-   “Ensure resources **cannot** be created with X”
    
-   “Prevent users from deploying Y”
    
-   “Enforce company-wide restriction”
    

👉 Correct mental trigger: **This is not IAM → this is Org Policy**

----------

### ✅ Choose the CORRECT LEVEL (org vs folder vs project)

This is the **core tested skill**.

Question wording

Correct level

“Across the entire company”

Organization

“Only for production”

Folder

“Exception for one workload”

Project

“Without changing each project individually”

Folder or Org

----------

### ✅ Understand inheritance & override behavior

Exam will test statements like:

-   “Can a project loosen an org restriction?” → **NO**
    
-   “Can a project be more restrictive?” → **YES**
    

If you understand **stricter always wins**, you will get these right.

----------

### ❌ What the exam will NOT do

-   Ask you to remember exact constraint IDs
    
-   Ask you to debug complex policy YAML
    
-   Ask you to chain multiple policies
    

----------

## 2️⃣ Real organization policy sample (concrete)

### Example requirement

> “Prevent all VMs from having external IPs in production”

This uses a **Boolean constraint**.

### Example policy (conceptual)

```yaml
constraint: compute.vmExternalIpAccess
booleanPolicy:
  enforced: true

```

Meaning:

-   `true` = external IPs are **blocked**
    
-   Applies to **all child resources**
    

----------

## 3️⃣ Applying Org Policy via CLI (gcloud)

### 🔹 Step 1: Identify the resource

You must know **where** you are applying it.

Examples:

-   Organization: `organizations/123456789`
    
-   Folder: `folders/456789012`
    
-   Project: `projects/my-prod-project`
    

----------

### 🔹 Step 2: Create policy file (example)

```yaml
constraint: constraints/compute.vmExternalIpAccess
booleanPolicy:
  enforced: true

```

Save as: `deny-external-ip.yaml`

----------

### 🔹 Step 3: Apply using gcloud

#### Apply at folder level (most common exam answer)

```bash
gcloud org-policies set-policy deny-external-ip.yaml \
  --folder=456789012

```

#### Apply at project level

```bash
gcloud org-policies set-policy deny-external-ip.yaml \
  --project=my-prod-project

```

#### Apply at organization level

```bash
gcloud org-policies set-policy deny-external-ip.yaml \
  --organization=123456789

```

----------

### 🔹 Step 4: Verify

```bash
gcloud org-policies list --folder=456789012

```

----------

## 4️⃣ List constraint example (regions)

### Requirement

> “Only allow deployments in us-central1 and us-east1”

### Policy example

```yaml
constraint: constraints/gcp.resourceLocations
listPolicy:
  allowedValues:
    - in:us-central1
    - in:us-east1

```

Apply using the **same `gcloud org-policies set-policy` command**.

----------

## 5️⃣ How Org Policies interact with folders vs projects (EXAM GOLD)

### Inheritance rule (absolute)

-   Policies flow **downward**
    
-   **Stricter always wins**
    
-   You can **add restrictions**, not remove them
    

----------

### Scenario walkthrough (very exam-like)

```
Organization
 └── Prod Folder
      └── prod-project-1

```

#### Org level

-   Allows all regions
    

#### Folder level (Prod)

-   Restricts to `us-central1`
    

#### Project level

-   Tries to allow `europe-west1`
    

👉 **Result**:  
❌ `europe-west1` is still **blocked**

----------

### Can a project override?

Override type

Allowed?

Loosen restriction

❌ No

Make stricter

✅ Yes

Add exception

❌ No

> **Exam phrase to remember**:  
> _“Projects cannot escape parent policies.”_

----------

## 6️⃣ IAM vs Org Policy (one last exam lock-in)

If the question says:

Wording

Answer

“Prevent creation”

Org Policy

“Restrict configuration”

Org Policy

“Allow user to access”

IAM

“Grant permission”

IAM

----------

## 7️⃣ Final exam-ready mental model

> **Org Policies define what is POSSIBLE**  
> **IAM defines who is ALLOWED**

---------- 
