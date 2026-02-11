### **Section 2.1 – Configuring OS Login**

![Image](https://docs.cloud.google.com/static/compute/docs/connect/ssh-best-practices/flowchart.svg)

![Image](https://miro.medium.com/1%2A_jSrb1-26iNlGRLU7gC81A.png)

This bullet is **high-yield for the ACE exam** because it tests whether you can **replace SSH key sprawl with IAM-based access** and understand **where OS Login is configured and enforced**.

---

## 1️⃣ What OS Login is (exam framing)

**OS Login** lets users **SSH into Compute Engine VMs using IAM**, instead of managing SSH keys manually.

**What changes**

* SSH access is controlled by **IAM roles**
* SSH keys are **not stored** in project or instance metadata
* Access is **centralized, auditable, and revocable**

> **Exam rule to memorize:**
> **OS Login = IAM controls SSH**

---

## 2️⃣ What the ACE exam actually tests

You should be able to:

### ✅ Identify when OS Login is the **best practice**

* Centralized access
* Auditable SSH
* Easy onboarding/offboarding

### ✅ Know **how OS Login is enabled**

* Project-level metadata
* Instance-level override (rare)

### ❌ What it does NOT test

* Linux user management details
* PAM / NSS internals
* Custom OS Login troubleshooting

---

## 3️⃣ How OS Login works (mental model)

```
User → IAM Role → OS Login → VM SSH Access
```

* IAM decides **who can SSH**
* OS Login maps IAM users → Linux users
* SSH keys are **ephemeral**

---

## 4️⃣ IAM roles used with OS Login (VERY exam-relevant)

| Role                         | What it allows                   |
| ---------------------------- | -------------------------------- |
| `roles/compute.osLogin`      | SSH access (non-root)            |
| `roles/compute.osAdminLogin` | SSH access with sudo             |
| `roles/compute.admin`        | Does NOT automatically grant SSH |

> **Exam trap:**
> Compute Admin ≠ SSH access unless OS Login role is present

---

## 5️⃣ Enabling OS Login (CLI – exam-relevant)

### Enable at **project level** (recommended)

```bash
gcloud compute project-info add-metadata \
  --metadata enable-oslogin=TRUE
```

This applies to **all VMs** in the project.

---

### Enable at **instance level** (override)

```bash
gcloud compute instances add-metadata my-vm \
  --zone=us-central1-a \
  --metadata enable-oslogin=TRUE
```

> Use instance-level only for **exceptions**.

---

## 6️⃣ Disabling legacy SSH keys (important exam nuance)

When OS Login is enabled:

* Project-wide SSH keys are **ignored**
* Instance SSH keys are **ignored**
* Access is **only via IAM**

> **Exam clue:**
> “User added SSH key but still can’t log in” → OS Login enabled

---

## 7️⃣ OS Login + SSH workflow (what actually happens)

1. User authenticates with Google account
2. IAM role is evaluated
3. OS Login provisions Linux user
4. Temporary SSH key is injected
5. User logs in

---

## 8️⃣ Common ACE exam scenarios

### Scenario 1

> “Centralized SSH access with easy revocation”

✅ **Enable OS Login**

---

### Scenario 2

> “User removed from IAM should immediately lose SSH”

✅ **OS Login**

---

### Scenario 3

> “User has Compute Admin but cannot SSH”

✅ Missing:

* `roles/compute.osLogin` or `roles/compute.osAdminLogin`

---

## 9️⃣ OS Login vs SSH keys (exam comparison)

| Feature         | OS Login | SSH Keys |
| --------------- | -------- | -------- |
| Centralized     | ✅        | ❌        |
| Auditable       | ✅        | ❌        |
| IAM-based       | ✅        | ❌        |
| Manual key mgmt | ❌        | ✅        |

---

## 10️⃣ Common ACE exam traps

❌ Assuming SSH works because user is Project Owner
❌ Forgetting OS Login ignores metadata SSH keys
❌ Granting Compute Admin instead of OS Login role
❌ Enabling OS Login on one VM but expecting project-wide effect

---

## 🔑 One-line ACE memory hook

> **If the question says “centralized SSH” → OS Login**

--- 
