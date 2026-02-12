### **Section 3.4 – Monitoring and logging**

#### **Using Cloud Diagnostics to research an application issue**

This bullet is about **application-level troubleshooting**, not infrastructure debugging.
The ACE exam tests whether you understand how to use **Cloud Operations (formerly Stackdriver) tools together** to investigate an issue.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify which Cloud Diagnostics tool to use
* Correlate logs, metrics, traces, and errors
* Investigate latency, crashes, and performance problems
* Avoid using the wrong tool

> **Exam mindset:**
> *“The application is misbehaving — which diagnostic tool do I open first?”*

---

# 2️⃣ What “Cloud Diagnostics” includes

Cloud Diagnostics refers to a group of tools within **Cloud Operations Suite**:

| Tool             | Purpose                      |
| ---------------- | ---------------------------- |
| Cloud Logging    | View logs                    |
| Cloud Monitoring | View metrics                 |
| Error Reporting  | Aggregate application errors |
| Cloud Trace      | Analyze request latency      |
| Cloud Profiler   | CPU/memory profiling         |
| Cloud Debugger   | Snapshot application state   |

You do NOT need deep syntax knowledge — just **when to use what**.

---

# 3️⃣ Error Reporting (VERY EXAM FAVORITE)

### What it does

* Aggregates application exceptions
* Groups identical stack traces
* Shows frequency trends

### Use when

* App crashes
* Exceptions occur
* Want to see error frequency

> **ACE signal:**
> “Application throwing exceptions” → Error Reporting

---

# 4️⃣ Cloud Trace (Latency analysis)

### What it does

* Shows request flow
* Identifies slow components
* Breaks down latency

### Use when

* App is slow
* Requests time out
* Need latency breakdown

> **ACE rule:**
> Slow app → Trace
> Crashing app → Error Reporting

---

# 5️⃣ Cloud Profiler (Performance tuning)

### What it does

* Analyzes CPU usage
* Memory allocation
* Performance bottlenecks

### Use when

* High CPU
* Memory leaks
* Performance inefficiency

> **ACE awareness:**
> Profiler is deeper performance analysis.

---

# 6️⃣ Cloud Debugger (Live debugging)

### What it does

* Captures application snapshots
* No need to restart app
* Inspect variables at runtime

### Use when

* Need to inspect app state
* Hard-to-reproduce bugs

> Not heavily tested, but must recognize purpose.

---

# 7️⃣ Typical diagnostic workflow (EXAM LOGIC)

### Scenario: App is failing

1. Check **Error Reporting**
2. Review logs in **Cloud Logging**
3. Look at resource metrics in **Monitoring**

---

### Scenario: App is slow

1. Check **Monitoring metrics**
2. Use **Cloud Trace**
3. Investigate CPU/memory via Profiler

---

# 8️⃣ Logs + Metrics + Diagnostics (Integration)

Example troubleshooting chain:

```
User reports slowness
↓
Monitoring shows high latency
↓
Trace identifies slow DB call
↓
Logs show connection errors
↓
Error Reporting groups stack traces
```

> **ACE rule:**
> Diagnostics tools complement each other.

---

# 9️⃣ Common ACE exam scenarios

### Scenario 1

> “Application latency spikes”

✅ Cloud Trace

---

### Scenario 2

> “App crashes intermittently”

✅ Error Reporting

---

### Scenario 3

> “CPU utilization unusually high”

✅ Monitoring → possibly Profiler

---

### Scenario 4

> “Need to inspect variable value without redeploying”

✅ Cloud Debugger

---

# 🔟 Common ACE exam traps

❌ Using Monitoring to find stack traces
❌ Using Logs when Error Reporting is better
❌ Expecting Trace to show logs
❌ Confusing infrastructure issue with app issue

---

# 🔑 One-line ACE memory hooks

* **Crashes → Error Reporting**
* **Slow → Trace**
* **CPU/memory tuning → Profiler**
* **Logs = raw events**
* **Monitoring = metrics**

---
 
