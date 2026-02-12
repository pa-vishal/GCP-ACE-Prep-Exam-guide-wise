Good catch. Missing bullets are how people lose points. Let’s lock this in properly.

---

# **Section 2 – Planning and implementing a cloud solution (~30%)**

## **2.1 Planning and implementing compute resources**

### **Deploying a containerized application to GKE**

This is a **core deployment workflow question**. Expect at least one scenario involving GKE deployment steps, permissions, or image issues.

---

# 1️⃣ What the ACE exam is actually testing

You should be able to:

* Deploy a container image to a GKE cluster
* Understand:

  * Cluster
  * Node pools
  * Deployment
  * Service
* Diagnose:

  * Image pull failures
  * Pending Pods
  * Service exposure issues

> **Exam mindset:**
> *“Given a container image, how do I run it on GKE?”*

---

# 2️⃣ High-Level Deployment Flow

The full deployment pipeline:

```
Build container image
↓
Push to Artifact Registry
↓
Create GKE cluster
↓
Deploy via Kubernetes Deployment
↓
Expose using Service (LoadBalancer/ClusterIP)
```

---

# 3️⃣ Step 1 – Push Image to Artifact Registry

Example:

```bash
docker build -t us-central1-docker.pkg.dev/PROJECT_ID/repo/app:v1 .
docker push us-central1-docker.pkg.dev/PROJECT_ID/repo/app:v1
```

> Exam signal:
> If image is private → ensure node service account has `artifactregistry.reader`.

---

# 4️⃣ Step 2 – Create GKE Cluster

Standard cluster example:

```bash
gcloud container clusters create my-cluster \
  --zone=us-central1-a
```

Autopilot example:

```bash
gcloud container clusters create-auto my-cluster \
  --region=us-central1
```

---

# 5️⃣ Step 3 – Connect to Cluster

```bash
gcloud container clusters get-credentials my-cluster
```

---

# 6️⃣ Step 4 – Create Deployment

Basic Deployment YAML:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: us-central1-docker.pkg.dev/PROJECT_ID/repo/app:v1
```

Apply it:

```bash
kubectl apply -f deployment.yaml
```

---

# 7️⃣ Step 5 – Expose Application

Internal access:

```bash
kubectl expose deployment my-app --type=ClusterIP --port=80
```

External access:

```bash
kubectl expose deployment my-app --type=LoadBalancer --port=80
```

> Exam rule:
> LoadBalancer → external IP
> ClusterIP → internal only

---

# 8️⃣ Standard vs Autopilot (EXAM FAVORITE)

| Feature                  | Standard   | Autopilot      |
| ------------------------ | ---------- | -------------- |
| Node management          | You manage | Google manages |
| Resource limits required | Optional   | Mandatory      |
| Operational overhead     | Higher     | Lower          |

> If question says “reduce operational overhead” → Autopilot.

---

# 9️⃣ Common Deployment Failures (VERY TESTED)

---

### ❌ ImagePullBackOff

Cause:

* Wrong image path
* No permission to Artifact Registry

Fix:

* Grant node SA `roles/artifactregistry.reader`

---

### ❌ Pod Pending

Cause:

* Not enough CPU/memory
* No available nodes
* Wrong region constraints

Fix:

* Increase node pool
* Enable autoscaling

---

### ❌ Service has no external IP

Cause:

* Using ClusterIP instead of LoadBalancer

---

### ❌ Cannot access app externally

Check:

* Service type
* Firewall rules
* Ingress configuration

---

# 🔟 IAM Considerations

For image pulling:

Node service account needs:

```
roles/artifactregistry.reader
```

If app needs API access:

* Use Workload Identity
* Assign GSA with required roles

---

# 11️⃣ Exam Scenario Patterns

---

### Scenario 1

> “Deploy containerized web app with external access”

Steps:

* Deployment
* Service type LoadBalancer

---

### Scenario 2

> “Pods failing to start due to image access”

Fix:

* Grant Artifact Registry Reader to node SA

---

### Scenario 3

> “Minimize cluster management overhead”

Answer:

* Use Autopilot

---

### Scenario 4

> “App needs access to Cloud Storage”

Answer:

* Use Workload Identity
* Assign GSA role

---

# 🔑 One-line ACE Memory Hooks

* **Build → Push → Deploy → Expose**
* **LoadBalancer = external**
* **ImagePullBackOff = permissions**
* **Autopilot = low ops**
* **Pods need image access via node SA**

---
 

