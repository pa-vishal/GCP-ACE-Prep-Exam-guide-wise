
# **Section 3.4 – Monitoring and logging**

## **Viewing and filtering logs in Cloud Logging**

## **Viewing specific log message details in Cloud Logging**

These bullets test whether you can:

* Find relevant logs quickly
* Use filters correctly
* Inspect structured log fields
* Identify root cause from a log entry

This is **operational troubleshooting**, not architecture.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Navigate **Logs Explorer**
* Apply **basic filters**
* Identify severity levels
* Expand a log entry and interpret fields
* Distinguish between:

  * Resource type
  * Log name
  * Severity
  * Payload

> **Exam mindset:**
> *“The system failed — can I find the evidence?”*

---

# 2️⃣ Viewing logs in Logs Explorer

Path:

```
Cloud Logging → Logs Explorer
```

By default, you can:

* Select resource type (e.g., gce_instance, cloud_run_revision)
* Select log name (e.g., stdout, stderr, audit logs)
* Choose time range

---

# 3️⃣ Filtering logs (VERY EXAM RELEVANT)

Filtering is done using:

* Severity
* Resource type
* Labels
* Text search
* Structured fields

### Common filters

#### Filter by severity

```
severity>=ERROR
```

#### Filter by resource

```
resource.type="gce_instance"
```

#### Filter by log name

```
logName="projects/my-project/logs/cloudaudit.googleapis.com%2Factivity"
```

> **ACE rule:**
> Filtering reduces noise — always narrow scope.

---

# 4️⃣ Severity levels (MUST KNOW)

| Severity | Meaning           |
| -------- | ----------------- |
| DEBUG    | Low-level details |
| INFO     | Informational     |
| WARNING  | Potential issue   |
| ERROR    | Failure occurred  |
| CRITICAL | Severe failure    |

> **Exam signal:**
> “Find error logs” → filter by severity.

---

# 5️⃣ Viewing specific log message details

When you expand a log entry, you’ll see:

* Timestamp
* Resource type
* Severity
* Insert ID
* Labels
* Payload

Payload may be:

| Type         | Meaning          |
| ------------ | ---------------- |
| textPayload  | Unstructured log |
| jsonPayload  | Structured log   |
| protoPayload | Audit log format |

---

# 6️⃣ Structured log details (VERY IMPORTANT)

If the app writes structured JSON logs:

You can filter like:

```
jsonPayload.status="FAILED"
```

> **ACE signal:**
> Structured logging allows precise filtering.

---

# 7️⃣ Audit logs (COMMON EXAM TOPIC)

Audit logs appear under:

```
cloudaudit.googleapis.com/activity
cloudaudit.googleapis.com/data_access
```

Used to track:

* IAM changes
* Resource creation/deletion
* API calls

> **Exam trap:**
> IAM changes → check **audit logs**, not VM logs.

---

# 8️⃣ Common ACE exam scenarios

### Scenario 1

> “VM unexpectedly stopped”

✅ Filter:

* resource.type="gce_instance"
* severity>=ERROR

---

### Scenario 2

> “Who deleted this bucket?”

✅ Check:

* Audit logs
* protoPayload.authenticationInfo

---

### Scenario 3

> “Application logs contain ‘PaymentFailed’”

✅ Use text filter or structured filter.

---

### Scenario 4

> “Logs are overwhelming”

✅ Narrow by:

* Time range
* Severity
* Resource type

---

# 9️⃣ Logs vs Metrics (REMINDER)

| If you need…           | Use               |
| ---------------------- | ----------------- |
| CPU usage              | Monitoring metric |
| Specific error text    | Logs Explorer     |
| Alert on error pattern | Log-based metric  |

> **ACE trap:**
> Logs do not trigger alerts unless converted into a metric.

---

# 🔑 One-line ACE Memory Hooks

* **Logs Explorer = investigation**
* **severity>=ERROR**
* **Audit logs = who did what**
* **Structured logs = powerful filters**
* **Metrics ≠ logs**

---

## Direct answer to your question

Yes — these two bullets are logically connected and should be studied together.
But for your final Markdown ZIP, I will keep them as **two headings within one file**, since the operational workflow is continuous:

> Filter → Locate → Expand → Analyze

---
 
