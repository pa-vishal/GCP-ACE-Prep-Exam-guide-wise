### **Section 2.1 – Installing and configuring the command-line interface (CLI) for Kubernetes (kubectl)**

![Image](https://media.licdn.com/dms/image/v2/D5612AQEISdk5LH2iuA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1703629194162?e=2147483647\&t=GClLzd68uFbvpKqIOaThzKblZIbqN_Zkv5Cy3Zb41Vk\&v=beta)

![Image](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-architecture.svg)

![Image](https://devopscube.com/content/images/2025/05/image-55.png)

This bullet checks whether you understand **how administrators and CI/CD systems talk to Kubernetes**. The ACE exam is not about advanced Kubernetes usage—it’s about **installing kubectl, authenticating correctly, and pointing it at the right cluster**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Install `kubectl`
* Configure it to talk to a **GKE cluster**
* Understand **authentication and context**
* Recognize common misconfigurations

> **Exam mindset:**
> *“Why does kubectl say it can’t connect to the cluster?”*

---

## 2️⃣ What `kubectl` is (exam framing)

`kubectl` is:

* The **official Kubernetes CLI**
* Used to:

  * Deploy workloads
  * Inspect cluster state
  * Manage Kubernetes resources (Pods, Services, Deployments)

In GKE:

* `kubectl` uses **Google Cloud authentication**
* Cluster credentials are stored in a **kubeconfig file**

---

## 3️⃣ Installing kubectl (exam-level)

### Option A: Install via gcloud (MOST COMMON & recommended)

```bash
gcloud components install kubectl
```

Why the exam likes this:

* Simple
* Version-compatible with GKE
* Integrated with Google authentication

---

### Option B: Standalone install (exam awareness only)

* Download from Kubernetes release site
* Used in restricted or custom environments

> ACE exam usually assumes **gcloud-based install**

---

## 4️⃣ Configuring kubectl for a GKE cluster (VERY exam-relevant)

After kubectl is installed, it **does nothing** until configured.

### Get cluster credentials (THIS IS THE KEY COMMAND)

```bash
gcloud container clusters get-credentials my-cluster \
  --region=us-central1
```

What this does:

* Fetches cluster endpoint and certs
* Updates `~/.kube/config`
* Sets the **current context**

> **Exam trap:**
> kubectl installed ≠ kubectl configured

---

## 5️⃣ kubeconfig & context (mental model)

`kubectl` relies on:

* **kubeconfig file** (`~/.kube/config`)
* **context** (which cluster + user you’re talking to)

### View current context

```bash
kubectl config current-context
```

### List all contexts

```bash
kubectl config get-contexts
```

> **Exam signal:**
> “kubectl talks to the wrong cluster” → context issue

---

## 6️⃣ Authentication flow (GKE-specific)

```
kubectl → kubeconfig → gcloud auth → GKE API
```

* Uses your **Google identity**
* Enforced by:

  * IAM
  * Kubernetes RBAC (out of scope for ACE depth)

> **Exam note:**
> You are **not** expected to configure Kubernetes RBAC in detail.

---

## 7️⃣ Common ACE exam scenarios

### Scenario 1

> “kubectl returns connection refused”

✅ Likely cause:

* Cluster credentials not fetched

---

### Scenario 2

> “kubectl works for one cluster but not another”

✅ Likely cause:

* Wrong context

---

### Scenario 3

> “User has GKE permissions but kubectl still fails”

✅ Likely cause:

* Missing `get-credentials` step

---

## 8️⃣ kubectl vs gcloud (exam clarity)

| Tool    | Purpose                      |
| ------- | ---------------------------- |
| gcloud  | Manages GCP resources        |
| kubectl | Manages Kubernetes resources |

> **Exam trap:**
> You cannot create Pods using `gcloud`

---

## 9️⃣ Common ACE exam traps

❌ Forgetting to install kubectl
❌ Forgetting `get-credentials`
❌ Confusing project/region/zone
❌ Assuming kubectl auto-detects clusters

---

## 🔑 One-line ACE memory hook

> **kubectl talks to clusters, gcloud fetches credentials**

--- 
