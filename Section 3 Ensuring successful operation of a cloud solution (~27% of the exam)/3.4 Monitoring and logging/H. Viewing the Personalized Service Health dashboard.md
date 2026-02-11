### **Section 3.4 – Monitoring and logging**

#### **Viewing the Personalized Service Health dashboard**

This bullet is about **distinguishing between your application’s problems and Google Cloud’s problems**. The ACE exam wants to know if you can identify when an issue is caused by **a Google service outage or degradation**, not your configuration.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain what the **Personalized Service Health dashboard** is
* Know how it differs from:

  * Monitoring alerts
  * Logs
  * Public status page
* Use it to identify service disruptions affecting your project

> **Exam mindset:**
> *“Is this our bug, or is Google having an incident?”*

---

# 2️⃣ What is the Personalized Service Health dashboard?

It is a **project-specific view of Google Cloud service incidents**.

It shows:

* Active incidents
* Service disruptions
* Maintenance events
* Impacted resources

It is different from:

* The public status page (which shows global outages)

---

# 3️⃣ Personalized vs Public Status (VERY IMPORTANT)

| Tool                        | Scope                            |
| --------------------------- | -------------------------------- |
| Public Status Page          | Global service health            |
| Personalized Service Health | Your project’s impacted services |

> **ACE rule:**
> If the question says “affecting my project” → Personalized dashboard.

---

# 4️⃣ What information it provides

* Affected product (e.g., GKE, Cloud SQL)
* Impacted region
* Severity
* Time of incident
* Recommended action

Example:

* “GKE cluster in us-central1 experiencing degraded control plane”

---

# 5️⃣ When to check it (EXAM SCENARIOS)

### Scenario 1

> “Application is down but no errors in logs”

✅ Check:

* Personalized Service Health

---

### Scenario 2

> “Multiple services failing simultaneously”

✅ Likely:

* Regional service disruption

---

### Scenario 3

> “Cloud SQL connection errors across region”

✅ Check:

* Service Health dashboard

---

# 6️⃣ What it does NOT do (EXAM TRAPS)

❌ Does not fix issues automatically
❌ Does not replace Monitoring
❌ Does not show application bugs
❌ Does not show logs

> **ACE trap:**
> Do not confuse service outage with misconfiguration.

---

# 7️⃣ Interaction with Monitoring

Monitoring alerts:

* Tell you something is wrong

Personalized Service Health:

* Tells you if Google Cloud is experiencing an incident

Combined workflow:

```
Alert fires
↓
Check logs
↓
Check metrics
↓
Check Personalized Service Health
```

---

# 8️⃣ IAM awareness (exam level)

To view dashboard:

* Must have appropriate IAM role (e.g., Viewer)

If user cannot see incident:

* Check project permissions

---

# 🔑 One-line ACE memory hooks

* **App issue? → Logs**
* **Metric spike? → Monitoring**
* **Regional outage? → Personalized Service Health**
* **Public page ≠ project-specific view**

---
 
