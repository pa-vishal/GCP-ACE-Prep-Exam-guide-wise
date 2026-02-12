### **Section 3.4 – Monitoring and logging**

#### **Configuring audit logs**

This is a **high-confidence ACE topic**. Audit logs are about **who did what, when, and where** in your Google Cloud environment.

The exam tests whether you understand:

* The types of audit logs
* Which are enabled by default
* How to enable/disable certain types
* How to use them for security and compliance

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify the **four types of audit logs**
* Know which ones are always enabled
* Enable Data Access logs when required
* Use audit logs to investigate IAM or resource changes

> **Exam mindset:**
> *“Who changed this configuration?”*

---

# 2️⃣ The Four Types of Audit Logs (MUST MEMORIZE)

| Type           | Purpose                        | Default State     |
| -------------- | ------------------------------ | ----------------- |
| Admin Activity | Configuration changes          | Always enabled    |
| Data Access    | Data read/write operations     | Disabled (mostly) |
| System Event   | Google internal system actions | Always enabled    |
| Policy Denied  | Access denied events           | Always enabled    |

---

## 1️⃣ Admin Activity Logs (VERY IMPORTANT)

Tracks:

* Creating/deleting resources
* IAM role changes
* Firewall rule updates
* Service enable/disable

These:

* Cannot be disabled
* Are free

> **ACE signal:**
> “Who deleted this VM?” → Admin Activity logs.

---

## 2️⃣ Data Access Logs (COMMON EXAM TRAP)

Tracks:

* Reading data
* Writing data
* Calling APIs that access data

Examples:

* Reading BigQuery table
* Accessing Cloud Storage object
* Querying Cloud SQL

By default:

* Often disabled
* Must be explicitly enabled

> **ACE rule:**
> Need visibility into data reads → enable Data Access logs.

---

## 3️⃣ System Event Logs

Tracks:

* System-generated events
* Google-managed operations
* Failover events

Always enabled.

---

## 4️⃣ Policy Denied Logs

Tracks:

* IAM permission denials
* Access denied attempts

Useful for:

* Security investigations

---

# 3️⃣ Enabling Data Access Logs (Exam Awareness)

You enable Data Access logs at:

* Organization
* Folder
* Project level

Through:

* IAM policy configuration

Conceptually:

```bash
gcloud projects get-iam-policy PROJECT_ID
```

(You’re not tested on exact CLI syntax — just where it's configured.)

---

# 4️⃣ Cost Awareness (EXAM FAVORITE)

Admin Activity logs:

* Free

Data Access logs:

* May incur charges

> **ACE trap:**
> Don’t enable Data Access logs everywhere unless required.

---

# 5️⃣ Audit Logs vs Regular Logs (IMPORTANT DISTINCTION)

| Feature            | Audit Logs | Application Logs |
| ------------------ | ---------- | ---------------- |
| Tracks IAM changes | Yes        | No               |
| Tracks API calls   | Yes        | No               |
| Tracks app output  | No         | Yes              |

> **ACE rule:**
> Governance issue → Audit Logs
> Application issue → Logs Explorer

---

# 6️⃣ Common ACE Exam Scenarios

### Scenario 1

> “Find who modified firewall rule”

✅ Admin Activity logs

---

### Scenario 2

> “Audit which user read sensitive BigQuery table”

✅ Enable Data Access logs

---

### Scenario 3

> “User receives permission denied”

✅ Check Policy Denied logs

---

### Scenario 4

> “Security requires logging all data reads”

✅ Enable Data Access logs (project/org level)

---

# 7️⃣ Audit Logs Flow

```
API call
↓
Cloud Audit Logging
↓
Log bucket
↓
Logs Explorer / Export / Alert
```

You can:

* Export audit logs using log sinks
* Query them using Log Analytics
* Create log-based metrics

---

# 8️⃣ Common ACE exam traps

❌ Thinking audit logs are disabled by default
❌ Forgetting Data Access logs must be enabled
❌ Confusing Admin Activity with Data Access
❌ Ignoring IAM scope (org vs project)
❌ Expecting audit logs to fix issues

---

# 🔑 One-line ACE memory hooks

* **Who did what? → Admin Activity**
* **Who accessed data? → Data Access**
* **Denied access? → Policy Denied**
* **Admin logs always on**
* **Data Access may cost money**

---

