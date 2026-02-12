### **Section 1.1 – Creating a resource hierarchy**

![Image](https://d33wubrfki0l68.cloudfront.net/eaddeba5e864fe63444fe247f7a7277b427e42c2/ed88b/gcpimages/02-architecture/resource-hierarchy-overview.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/cloud-hierarchy-1omgk.max-700x700.PNG)

This is a **foundational ACE topic**. Many IAM, billing, and policy questions assume you _already understand this structure_.

----------

## 1️⃣ What is a resource hierarchy?

In **Google Cloud**, every resource lives in a **tree-like hierarchy** that defines:

-   **Ownership**
    
-   **Policy inheritance**
    
-   **Billing scope**
    
-   **Access control**
    

The hierarchy (top → bottom):

```
Organization
 └── Folder(s)
      └── Project(s)
           └── Resources (VMs, GKE, Cloud SQL, Buckets, etc.)

```

> **Key exam idea:**  
> Policies (IAM, org policies, budgets) **flow downward** unless explicitly overridden.

----------

## 2️⃣ The hierarchy components (one by one)

### **A. Organization**

-   Represents a **company or institution**
    
-   Created automatically when:
    
    -   You use **Cloud Identity / Google Workspace**
        
-   Acts as the **root node**
    

**Why it matters**

-   Central place for:
    
    -   Organization Policies
        
    -   Centralized IAM
        
    -   Folder structure
        
    -   Audit visibility
        

**Exam tip**

> If a question mentions _enterprise_, _company-wide policy_, or _central governance_ → **Organization level**

----------

### **B. Folders**

-   Optional but **strongly recommended**
    
-   Used to group projects logically
    

**Common folder strategies**

-   By environment: `prod / staging / dev`
    
-   By department: `finance / engineering / marketing`
    
-   By compliance boundary
    

**Why folders exist**

-   Apply IAM and org policies **once** to many projects
    
-   Delegate control safely
    

**Example**

```
Organization
 └── Engineering
      ├── Dev
      │    └── dev-project-1
      └── Prod
           └── prod-project-1

```

**Exam trap**

> Folders are **not required**, but **best practice** in almost all real setups.

----------

### **C. Projects**

-   **Mandatory**
    
-   Every GCP resource lives in **exactly one project**
    
-   Acts as:
    
    -   Billing boundary
        
    -   API enablement boundary
        
    -   IAM boundary
        

**Project contains**

-   Compute Engine
    
-   GKE
    
-   Cloud SQL
    
-   Buckets
    
-   APIs
    
-   Logs & metrics
    

**Important**

-   Projects **cannot contain other projects**
    
-   Projects **inherit** from folder/org
    

----------

### **D. Resources**

-   Actual services you deploy
    
-   Always belong to **one project only**
    

----------

## 3️⃣ How hierarchy affects IAM (very exam-relevant)

IAM roles can be granted at:

-   Organization level
    
-   Folder level
    
-   Project level
    
-   Resource level
    

**Inheritance rule**

-   Permissions granted **higher** apply **lower**
    

**Example**

-   IAM at folder → applies to all projects in that folder
    
-   IAM at org → applies to everything
    

**ACE exam pattern**

> “Grant access to many projects without repeating configuration”  
> ✔️ Use **Folder-level IAM**

----------

## 4️⃣ How hierarchy affects Organization Policies

Organization Policies:

-   Restrict behavior (e.g., no external IPs, allowed regions)
    
-   Can be applied at:
    
    -   Org
        
    -   Folder
        
    -   Project
        

**Inheritance**

-   More restrictive policy wins
    

**Example**

-   Org policy: allow all regions
    
-   Folder policy: only `us-central1`  
    → Projects under folder limited to `us-central1`
    

----------

## 5️⃣ Billing & hierarchy (quick clarity)

-   **Billing account** is **linked to projects**
    
-   Folder/org does **not directly bill**
    
-   But hierarchy helps:
    
    -   Budget visibility
        
    -   Cost allocation
        
    -   Access control
        

----------

## 6️⃣ Real-world use case

**Scenario**

> A company wants:
> 
> -   Central security rules
>     
> -   Separate dev/prod billing
>     
> -   Delegated team access
>     

**Correct setup**

```
Organization
 └── Engineering
      ├── Dev (folder)
      │    └── dev-project (linked to dev billing)
      └── Prod (folder)
           └── prod-project (linked to prod billing)

```

----------

## 7️⃣ Exam traps & misconceptions

❌ “Folders are required” → **False**  
❌ “Projects can exist outside organization” → **Rare, standalone only**  
❌ “Billing is applied at folder” → **Incorrect**  
✔️ Projects are the **unit of billing**

----------

## 8️⃣ One-line exam memory hook

> **Organization = governance**  
> **Folder = grouping & delegation**  
> **Project = billing + IAM + APIs**  
> **Resources = actual services**

----------

When you’re ready, give me **the next bullet under Section 1.1**.
