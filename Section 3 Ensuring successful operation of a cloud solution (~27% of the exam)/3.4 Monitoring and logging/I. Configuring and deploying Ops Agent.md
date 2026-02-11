### **Section 3.4 – Monitoring and logging**

#### **Configuring and deploying Ops Agent**

This bullet is about **collecting metrics and logs from Compute Engine VMs**.
The ACE exam tests whether you understand:

* Why the Ops Agent exists
* What it collects
* When it’s required
* How it differs from legacy agents

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain what the **Ops Agent** does
* Know when to install it
* Distinguish it from:

  * Built-in GCP metrics
  * Legacy monitoring agents
* Understand that it runs on **Compute Engine VMs**

> **Exam mindset:**
> *“Why are VM logs or metrics missing?”*

---

# 2️⃣ What is the Ops Agent?

The **Ops Agent** is a single unified agent that:

* Collects **metrics**
* Collects **logs**
* Sends them to:

  * Cloud Monitoring
  * Cloud Logging

It replaces:

* Stackdriver Monitoring Agent
* Stackdriver Logging Agent

> **ACE rule:**
> Modern VMs → use **Ops Agent**, not legacy agents.

---

# 3️⃣ When do you need Ops Agent?

### You need it when:

* Collecting:

  * Guest OS metrics (CPU inside OS, memory)
  * Application logs from VM
* Monitoring on-prem VMs via hybrid setup
* Collecting custom log files

---

### You do NOT need it for:

* Cloud Run
* GKE managed nodes
* Managed services (Cloud SQL, BigQuery)

> **ACE trap:**
> Ops Agent is for **Compute Engine VMs**, not serverless.

---

# 4️⃣ What it collects (MUST KNOW)

### Metrics:

* CPU usage (inside OS)
* Memory usage
* Disk usage
* Network metrics
* Custom application metrics (if configured)

### Logs:

* Syslog
* Application logs
* Custom file paths

---

# 5️⃣ Deployment methods (Exam Awareness)

Common ways to deploy:

* Install manually on VM
* Use:

  * Startup scripts
  * VM templates
  * Instance groups
  * Automation tools

You’re not tested on exact install commands — just awareness.

---

# 6️⃣ Configuration

Ops Agent uses configuration files to:

* Define log collection paths
* Define metric sources
* Enable/disable integrations

Example scenarios:

* Collect `/var/log/app.log`
* Monitor NGINX metrics

> **ACE rule:**
> Without configuration, custom logs won’t be collected.

---

# 7️⃣ Common ACE exam scenarios

### Scenario 1

> “Memory metrics not visible for VM”

✅ Likely:

* Ops Agent not installed

---

### Scenario 2

> “Application logs from VM not appearing in Cloud Logging”

✅ Check:

* Ops Agent installed?
* Log file path configured?

---

### Scenario 3

> “Monitoring CPU for Cloud Run”

❌ No Ops Agent needed
✅ Built-in metrics

---

# 8️⃣ Ops Agent vs Built-in Monitoring (IMPORTANT DISTINCTION)

| Service        | Needs Ops Agent?             |
| -------------- | ---------------------------- |
| Compute Engine | Yes (for guest metrics/logs) |
| GKE            | No (managed)                 |
| Cloud Run      | No                           |
| Cloud SQL      | No                           |

> **ACE trap:**
> Don’t install Ops Agent on services that don’t support it.

---

# 9️⃣ Common ACE exam traps

❌ Installing legacy Stackdriver agent
❌ Expecting VM logs without agent
❌ Trying to install Ops Agent on Cloud Run
❌ Confusing Monitoring metrics with OS-level metrics

---

# 🔑 One-line ACE memory hooks

* **Ops Agent = VM telemetry**
* **Compute Engine only**
* **Serverless doesn’t use it**
* **Guest metrics require agent**

---
 
