### **Section 3.1 – Managing compute resources**

#### **Configuring GKE to access Artifact Registry**

![Image](https://miro.medium.com/v2/resize%3Afit%3A1200/1%2AjKIugGMgZAnd7mC7ufnAMg.png)

![Image](https://media2.dev.to/dynamic/image/width%3D1000%2Cheight%3D420%2Cfit%3Dcover%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9f85c6ib39lxovz81uax.png)

![Image](https://i.sstatic.net/2mAk2.png)

This bullet tests whether you understand **how GKE authenticates to pull container images** and **where permissions must be granted**. On the ACE exam, failures here usually show up as **Pods stuck in `ImagePullBackOff`**.

---

## 1️⃣ What the ACE exam is actually testing

You should be able to:

* Explain **how GKE pulls images** from Artifact Registry
* Identify **which service account needs access**
* Grant the **correct IAM role**
* Diagnose **image pull failures**

> **Exam mindset:**
> *“Which identity is pulling the image, and does it have permission?”*

---

## 2️⃣ How GKE pulls images (MENTAL MODEL)

```
Pod → Node → Node Service Account → Artifact Registry
```

Key points:

* **Pods do NOT authenticate directly**
* **Nodes pull images**
* Permissions must be on the **node’s service account**

> **ACE rule:**
> Image pull permissions belong to the **node**, not the developer.

---

## 3️⃣ Default identities used by GKE (MUST KNOW)

### GKE Standard (most common)

* Uses a **node service account**
* Default:

  ```
  PROJECT_NUMBER-compute@developer.gserviceaccount.com
  ```

### GKE Autopilot

* Google-managed
* Permissions are still enforced via IAM
* Same **Artifact Registry roles** apply

> **Exam signal:**
> “Cluster can’t pull images” → check **node service account IAM**

---

## 4️⃣ Required IAM role (EXAM FAVORITE)

To pull images from Artifact Registry, grant **one of these**:

| Role                            | Purpose                   |
| ------------------------------- | ------------------------- |
| `roles/artifactregistry.reader` | Pull images (most common) |
| `roles/artifactregistry.writer` | Push + pull (CI/CD)       |

> **ACE rule:**
> **Reader is sufficient for GKE runtime**

---

## 5️⃣ Granting access (CLI – exam-relevant)

### Grant Artifact Registry read access to the node service account

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/artifactregistry.reader"
```

> Replace `PROJECT_NUMBER` with the numeric project ID.

---

## 6️⃣ Artifact Registry location awareness (EXAM TRAP)

* Artifact Registry is **regional**
* GKE cluster **can pull cross-region**, but:

  * Latency may increase
  * Best practice: **same region**

> **Exam signal:**
> “Reduce latency / best practice” → same-region registry

---

## 7️⃣ Kubernetes manifests (exam awareness)

When referencing an image:

```yaml
image: us-central1-docker.pkg.dev/my-project/my-repo/my-app:latest
```

Common mistake:

* Wrong registry hostname
* Wrong project or repo name

> **ACE trap:**
> Typo in image path ≠ IAM issue

---

## 8️⃣ Common failure symptoms & causes (VERY EXAM-RELEVANT)

| Symptom                     | Likely Cause                       |
| --------------------------- | ---------------------------------- |
| `ImagePullBackOff`          | Missing IAM permission             |
| `ErrImagePull`              | Wrong image path                   |
| Works locally, fails in GKE | Node SA lacks access               |
| CI works, runtime fails     | Writer role given to CI, not nodes |

---

## 9️⃣ Real ACE exam scenarios

### Scenario 1

> “Pods fail with ImagePullBackOff”

✅ Fix:

* Grant `artifactregistry.reader` to **node service account**

---

### Scenario 2

> “Cluster uses custom node service account”

✅ Fix:

* Grant role to **that service account**, not default

---

### Scenario 3

> “Secure image access, no hardcoded credentials”

✅ Correct approach:

* **IAM-based access via node service account**

---

## 10️⃣ Common ACE exam traps

❌ Granting role to user instead of node SA
❌ Granting writer when reader is sufficient
❌ Forgetting custom node service account
❌ Debugging Pods before checking IAM

---

## 🔑 One-line ACE memory hooks

* **Nodes pull images**
* **Grant IAM to node service account**
* **ImagePullBackOff = IAM or image path**

---
 
