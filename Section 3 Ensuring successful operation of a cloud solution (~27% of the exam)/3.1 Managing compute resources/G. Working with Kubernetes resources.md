### **Section 3.1 – Managing compute resources**

#### **Working with Kubernetes resources**

*(Pods, Services, StatefulSets)*

![Image](https://media.licdn.com/dms/image/v2/C5612AQEN5ubgCt9TcA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1622268066370?e=2147483647\&t=X_NxUJ9xekdEojlymt3jR67Iiv2CPJCn0vOlQKuBDl8\&v=beta)

![Image](https://yqintl.alicdn.com/667b84088637bc056ce3df67d71b76fd06ba703f.png)

![Image](https://assets.bytebytego.com/diagrams/0005-4-k8s-service-types.png)

This bullet checks whether you can **identify, inspect, and reason about core Kubernetes objects** and understand **which object solves which problem**. The ACE exam stays at a **foundational level**—you’re not expected to design complex manifests, but you *are* expected to pick the right resource.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Identify **Pods**, **Services**, and **StatefulSets**
* Know **when each is appropriate**
* Use `kubectl` to **view status**
* Avoid confusing stateless vs stateful workloads

> **Exam mindset:**
> *“Is this workload stateless or stateful, and how is it exposed?”*

---

## 2️⃣ Pods (the smallest unit)

### What a Pod is

* The **smallest deployable unit** in Kubernetes
* One or more containers that:

  * Share networking (IP/ports)
  * Share storage volumes
* Pods are **ephemeral**

### Key properties (exam-relevant)

* Pod IPs change when recreated
* Pods are **not self-healing by themselves**
* Usually managed by higher-level controllers

### View Pods

```bash
kubectl get pods
kubectl get pods --all-namespaces
```

**Common Pod states**

* `Running`
* `Pending`
* `CrashLoopBackOff`
* `ImagePullBackOff`

> **Exam trap:**
> Don’t deploy standalone Pods for production—use controllers.

---

## 3️⃣ Services (stable networking)

### What a Service is

* A **stable virtual IP** in front of Pods
* Load-balances traffic to matching Pods
* Decouples networking from Pod lifecycle

### Why Services exist

* Pods come and go
* Services provide **stable access**

### View Services

```bash
kubectl get services
```

---

### Service types (VERY exam-relevant)

| Type             | Use when                       |
| ---------------- | ------------------------------ |
| **ClusterIP**    | Internal-only access (default) |
| **NodePort**     | Expose via node IPs (basic)    |
| **LoadBalancer** | External access via cloud LB   |

> **ACE rule:**
> “Expose app externally” → **Service type LoadBalancer**

---

## 4️⃣ StatefulSets (STATEFUL workloads – HIGH-YIELD)

### What a StatefulSet is

* Controller for **stateful applications**
* Guarantees:

  * Stable Pod names
  * Stable network identities
  * Stable storage

### Key characteristics

* Pods are created **in order**
* Each Pod gets its **own PersistentVolume**
* Pods are not interchangeable

### Use when

* Databases
* Stateful services
* Ordered startup/shutdown matters

### View StatefulSets

```bash
kubectl get statefulsets
```

> **ACE rule:**
> If the workload needs stable identity or storage → **StatefulSet**

---

## 5️⃣ Pods vs Services vs StatefulSets (MUST MEMORIZE)

| Resource    | Solves                      |
| ----------- | --------------------------- |
| Pod         | Runs containers             |
| Service     | Stable access to Pods       |
| StatefulSet | Stateful Pods with identity |

---

## 6️⃣ Typical ACE exam scenarios

### Scenario 1

> “Application Pods restart and lose IPs”

✅ Expected:

* Use a **Service**

---

### Scenario 2

> “Database Pods need persistent identity and storage”

✅ Expected:

* **StatefulSet**

---

### Scenario 3

> “Check why application is unreachable”

✅ Steps:

1. `kubectl get pods`
2. `kubectl get services`
3. Verify Service type

---

### Scenario 4

> “Pods are running but app is not accessible externally”

✅ Likely cause:

* Service type is **ClusterIP**, not **LoadBalancer**

---

## 7️⃣ Common ACE exam traps

❌ Using Pods directly instead of controllers
❌ Expecting Pods to keep IPs
❌ Using Deployment for databases
❌ Forgetting Services are required for networking
❌ Debugging networking before checking Pod status

---

## 🔑 One-line ACE memory hooks

* **Pod = runs containers**
* **Service = stable access**
* **StatefulSet = state + identity**
* **External access = LoadBalancer Service**

--- 
