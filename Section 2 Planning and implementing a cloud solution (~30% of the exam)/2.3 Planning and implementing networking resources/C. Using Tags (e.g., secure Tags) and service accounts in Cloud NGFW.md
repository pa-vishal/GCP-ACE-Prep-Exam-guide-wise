### **Section 2.3 – Using Tags (e.g., secure tags) and service accounts in Cloud NGFW policy rules**

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AT154Nb_X3YJYdzo9GDppJA.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AIJ-olSALfKlw5XWmuvUOEQ.png)

This bullet is about **how you target firewall rules correctly**. The ACE exam often hides the right answer in *who the rule applies to*, not in ports or protocols.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Decide **how to target** firewall rules
* Choose between:

  * **Network tags**
  * **Service accounts**
  * **Secure tags** (recognition-level)
* Avoid over-permissive, brittle rules

> **Exam mindset:**
> *“Which VMs should this rule apply to—and how do I express that safely?”*

---

## 2️⃣ Targeting options overview (must know)

Cloud NGFW rules can target VMs by:

| Targeting method | Based on                        |
| ---------------- | ------------------------------- |
| Network tags     | VM metadata (strings)           |
| Service accounts | VM identity                     |
| Secure tags      | Centralized, policy-driven tags |

> **Key idea:**
> Targeting determines **which VMs the rule affects**, not who can connect.

---

## 3️⃣ Network tags (MOST COMMON on ACE)

### What they are

* Simple string labels on VMs (e.g., `web`, `ssh-enabled`)
* Firewall rules match **tags**, not VM names

### Use when

* Simple grouping
* Small to medium environments
* Quick, clear targeting

### Exam signals

* “Apply rule to a set of VMs”
* “Web servers”
* “Tag-based access”

---

### Example: Allow HTTP only to tagged VMs

```bash
gcloud compute firewall-rules create allow-http \
  --network=my-vpc \
  --direction=INGRESS \
  --action=ALLOW \
  --rules=tcp:80 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=web
```

And on the VM:

```bash
gcloud compute instances add-tags my-vm \
  --tags=web \
  --zone=us-central1-a
```

---

### Limitations (exam awareness)

❌ Tags are easy to misuse
❌ Anyone with VM edit permission can add a tag
❌ No identity or security context

---

## 4️⃣ Service accounts as firewall targets (SECURE & EXAM-FAVORITE)

### What this means

* Firewall rule applies to **VMs running as a specific service account**
* Ties network access to **workload identity**

### Use when

* Security matters
* You want **identity-based control**
* Multiple VMs share the same workload role

### Exam signals

* “Apply rule to a workload”
* “More secure than tags”
* “Identity-based control”

---

### Example: Allow SSH only to VMs with a specific service account

```bash
gcloud compute firewall-rules create allow-ssh-sa \
  --network=my-vpc \
  --direction=INGRESS \
  --action=ALLOW \
  --rules=tcp:22 \
  --source-ranges=10.0.0.0/8 \
  --target-service-accounts=vm-admin@my-project.iam.gserviceaccount.com
```

> **ACE rule:**
> If the question mentions *security* or *least privilege* → **service account targeting**

---

## 5️⃣ Secure tags (recognition-level for ACE)

### What secure tags are

* Centrally managed tags
* Applied via IAM-controlled policies
* Harder to spoof than network tags

### Use when

* Large organizations
* Central security teams
* Strong governance requirements

### ACE exam expectation

* **Know they exist**
* **Know they’re more secure**
* **Not tested on configuration details**

> **Exam signal:**
> “Enterprise-scale governance” → secure tags

---

## 6️⃣ Comparison table (MEMORIZE)

| Requirement            | Best choice      |
| ---------------------- | ---------------- |
| Simple grouping        | Network tags     |
| Secure, identity-based | Service accounts |
| Enterprise governance  | Secure tags      |
| Fast setup             | Network tags     |
| Least privilege        | Service accounts |

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “Only web servers should receive HTTP traffic”

✅ **Network tags** (web)

---

### Scenario 2

> “Apply firewall rules based on workload identity”

✅ **Service account targeting**

---

### Scenario 3

> “Prevent developers from bypassing firewall intent”

✅ **Service accounts or secure tags**

---

## 8️⃣ Common ACE exam traps

❌ Confusing IAM service accounts with firewall access
❌ Thinking tags are secure by default
❌ Forgetting to apply the tag to the VM
❌ Using broad rules instead of targeted ones

---

## 🔑 One-line ACE memory hooks

* **Tags = simple**
* **Service accounts = secure**
* **Secure tags = enterprise control**

---
 
