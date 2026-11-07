---
url: https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites/
title: Configure prerequisites for enrichment tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:44:57.231316+00:00
---

# Configure prerequisites for enrichment tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Configure prerequisites for enrichment tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To run enrichment tasks in Knowledge Studio, you can configure customer-managed service accounts, third-party authentication providers, Cloud Storage buckets, and Cloud Logging views. Setting up these prerequisite components lets enrichment agents securely access your target data sources, ingest unstructured knowledge signals, and learn from historical agent interactions.

The following table describes the prerequisite configurations and when you need to configure them:

Configuration feature | When to configure  
---|---  
**Google Cloud APIs** | Required. You must enable the underlying Google Cloud APIs to run enrichment workflows. For details, see the Before you begin section of this document.  
**Customer-managed service account** | Required. You use a dedicated service account to restrict read and write access on your target datasets and context sets. For details, see the Configure a customer-managed service account section of this document.  
**User Identity and Access Management (IAM) roles** | Required. You grant workflow managers and reviewers permissions to generate and approve metadata. For details, see the Grant required IAM roles to users section of this document.  
**Third-party auth providers** | Optional. You're connecting to third-party knowledge sources (such as Microsoft SharePoint, Atlassian Confluence, or GitHub). For details, see the Configure third-party auth providers section of this document.  
**Cloud Storage buckets** | Optional. You're ingesting unstructured business context (such as PDFs, Markdown, and CSV) and evaluation datasets. For details, see the Prepare Cloud Storage buckets section of this document.  
**Evaluation datasets** | Optional. You want to provide seed queries and benchmark datasets to actively track agent accuracy. For details, see the Format evaluation datasets section of this document.  
**Agent traces for self-learning** | Optional. You want the enrichment agent to automatically analyze downstream agent interactions from Gemini Enterprise applications or BigQuery agent analytics tables. For details, see the Configure agent traces for self-learning section of this document.  
**Data profiling and data insights** | Recommended. You want to improve enrichment quality by generating statistical profiles and baseline AI insights on frequently used tables. For details, see the Enable data profiling and data insights section of this document.  
  
## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataplex, Data Lineage, BigQuery, Cloud Storage, and IAM Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,datalineage.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataplex, Data Lineage, BigQuery, Cloud Storage, and IAM Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,datalineage.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required APIs details

To configure and run enrichment tasks, the enabled APIs perform the following functions:

API Name | Service Identifier | Purpose in Enrichment workflows  
---|---|---  
Dataplex API | `dataplex.googleapis.com` | Primary control plane API. Manages `EnrichmentTask`, `EnrichmentRun`, context sets, Change Requests, and the EnrichmentChatService.  
BigQuery API | `bigquery.googleapis.com` | Required for scanning table schemas, ingesting SQL execution history, and querying BigQuery agent analytics trace tables.  
Cloud Storage API | `storage.googleapis.com` | Required for ingesting evaluation sets and managing evaluation dataset samples.  
IAM Service Account Credentials API | `iamcredentials.googleapis.com` | Required for securely authenticating the execution agent and granting Short-Lived Credentials (SLC) during tasks.  
  
## Configure a customer-managed service account

Enrichment tasks use a customer-managed service account to run operations. Using a dedicated service account lets you restrict read and write access on your target datasets and context sets.

**Tip:** When you select an execution service account in the **Run** step of the task creation wizard in the Google Cloud console, Knowledge Studio automatically checks for missing permissions using Policy Troubleshooter. If you have permission to modify IAM policies on the target resources, you can click **Grant all** in the wizard to grant the missing roles automatically, or you can pre-configure the service account using the steps in this section.

  1. Create the service account.

To create a service account, you must have the **Owner** (`roles/owner`), **Editor** (`roles/editor`), or **Service Account Admin** (`roles/iam.serviceAccountAdmin`) role on the project.

A dedicated service account isolates your enrichment operations, letting you grant only the specific read and write permissions needed for these tasks without affecting other workloads.

To create a service account, follow these steps:

### Google Cloud CLI

To create a service account, use the [`gcloud iam service-accounts create` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
        --description="Service Account for Dataplex Knowledge Catalog enrichment agent execution" \
        --display-name="Knowledge Catalog enrichment agent SA"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME `
        --description="Service Account for Dataplex Knowledge Catalog enrichment agent execution" `
        --display-name="Knowledge Catalog enrichment agent SA"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME ^
        --description="Service Account for Dataplex Knowledge Catalog enrichment agent execution" ^
        --display-name="Knowledge Catalog enrichment agent SA"

### REST

Before using any of the request data, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID

HTTP method and URL: 
    
    POST https://iam.googleapis.com/v1/projects/TARGET_PROJECT_ID/serviceAccounts

Request JSON body: 
    
    {
       "accountId": "SERVICE_ACCOUNT_NAME",
       "serviceAccount": {
        "displayName": "Knowledge Catalog enrichment agent SA",
        "description": "Service Account for Dataplex Knowledge Catalog enrichment agent execution"
       }
      }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/projects/TARGET_PROJECT_ID/serviceAccounts"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://iam.googleapis.com/v1/projects/TARGET_PROJECT_ID/serviceAccounts" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

  2. Grant the necessary resource-level IAM roles to the execution service account on your target scopes:

     * **Dataplex Content Editor** (`roles/dataplex.contentEditor`) on the target context set (or **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) on the project): Lets the agent read context set entries, create and update context entries and `reference` entry links, and submit change requests (`dataplex.entryGroups.getContextSet`, `dataplex.entryGroups.requestContextChanges`, `dataplex.entries.*Context`, and `dataplex.entryLinks.create`).
     * **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) and **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`) on the project (or target catalog resources): Lets the agent inspect catalog metadata, read connected business glossaries, and stage working entries.
     * **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) on the target datasets and tables: Lets the agent list tables and read table schemas and agent analytics trace tables.
     * **BigLake Viewer** (`roles/biglake.viewer`) on target Lakehouse catalogs, namespaces, or tables: Required when enriching Lakehouse assets.
     * _(Optional)_ **BigQuery Job User** (`roles/bigquery.jobUser`) on the project (`bigquery.jobs.create`): Required on the project that contains the BigQuery agent analytics table if you learn from agent analytics traces, or on the task project if BigQuery job creation is moved inside a VPC Service Controls perimeter. By default, target-table BigQuery query jobs (sampling, query-history analysis, and validation checks) run as the Knowledge Catalog service agent in a Google-managed project.
     * _(Optional)_ **Dataplex Workflow Approver** (`roles/dataplex.workflowApprover`): Required only if you enable **Auto-publish** on your task. Lets the agent automatically approve and publish its own metadata change requests.

**Note** : The following code samples grant these roles at the **project level** for ease of setup. For production systems, we strongly recommend that you grant these roles at the resource level on your specific target context sets and datasets.

To grant these standard roles, follow these steps:

To add an IAM policy binding to a project, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/dataplex.contentEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/dataplex.catalogEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/dataplex.catalogViewer"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/bigquery.dataViewer"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/dataplex.contentEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/dataplex.catalogEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/dataplex.catalogViewer"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/bigquery.dataViewer"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/dataplex.contentEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/dataplex.catalogEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/dataplex.catalogViewer"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/bigquery.dataViewer"

  3. Grant users permission to impersonate the service account by granting them the **Service Account User** (`roles/iam.serviceAccountUser`) role:

Users who create the enrichment tasks in the console must have this permission so that they can specify and attach this service account to the task.

To grant users the **Service Account User** (`roles/iam.serviceAccountUser`) role, follow these steps:

To add an IAM policy binding to a service account, use the [`gcloud iam service-accounts add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID
     * `USER_EMAIL`: the user's email address

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com \
        --member="user:USER_EMAIL@domain.com" \
        --role="roles/iam.serviceAccountUser"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com `
        --member="user:USER_EMAIL@domain.com" `
        --role="roles/iam.serviceAccountUser"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com ^
        --member="user:USER_EMAIL@domain.com" ^
        --role="roles/iam.serviceAccountUser"

  4. Allow the internal Knowledge Catalog service agent to impersonate this service account by granting it the **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) role:

This role lets the underlying Knowledge Catalog service assume this dedicated service account's identity and its restricted permissions when it runs the background enrichment operations on your behalf.

To authorize the agent to assume the service account identity, follow these steps:

To add an IAM policy binding to a service account, use the [`gcloud iam service-accounts add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID
     * `TARGET_PROJECT_NUMBER`: your Google Cloud project number

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com \
        --member="serviceAccount:service-TARGET_PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
        --role="roles/iam.serviceAccountTokenCreator"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com `
        --member="serviceAccount:service-TARGET_PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" `
        --role="roles/iam.serviceAccountTokenCreator"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com ^
        --member="serviceAccount:service-TARGET_PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" ^
        --role="roles/iam.serviceAccountTokenCreator"

  5. Allow the Knowledge Catalog service agent (`service-<var>PROJECT_NUMBER</var>@gcp-sa-dataplex.iam.gserviceaccount.com`) to run backend BigQuery query jobs (sampling, query-history analysis, and validation checks) from a Google-managed project:

     * **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) on your target datasets or projects: Lets the service agent sample table data and run validation checks.
     * _(Recommended)_ **BigQuery Resource Viewer** (`roles/bigquery.resourceViewer`) on the projects whose BigQuery query history the agent reads (`bigquery.jobs.listAll`, which must be granted at the project level, not on individual datasets): Lets the service agent analyze historical SQL queries to discover common joins and filters. If this role isn't granted, the agent skips query-history analysis without failing the run.



## Grant required IAM roles to users

To ensure that your team can manage enrichment workflows and review AI-generated proposals, grant the appropriate IAM roles to your users. For instructions on how to grant these roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Workflow managers** (such as data stewards) who create, configure, and monitor tasks require the following roles:

  * **Dataplex DataScan Editor** (`roles/dataplex.dataScanEditor`) or **Dataplex Editor** (`roles/dataplex.editor`): Lets users create, modify, and trigger enrichment tasks.
  * **Service Account User** (`roles/iam.serviceAccountUser`) on the customer-managed service account: Required to attach the service account as the task's execution identity. For setup details, see the Configure a customer-managed service account section of this document.



**Change reviewers** (such as domain owners or subject matter experts) who inspect, approve, and publish AI-generated metadata proposals to the catalog require the following roles:

  * **Dataplex Content Editor** (`roles/dataplex.contentEditor`) (or **Dataplex Content User** (`roles/dataplex.contentUser`) for read-only inspection) on the context set, along with **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) and **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`) on the project: Required to open change requests, inspect side-by-side proposal diffs, and edit descriptions inline.
  * **Dataplex Workflow Approver** (`roles/dataplex.workflowApprover`): Required to approve and publish change requests to the live context set.
  * **Dataplex DataScan Viewer** (`roles/dataplex.dataScanViewer`) or **Dataplex Viewer** (`roles/dataplex.viewer`): Required to review per-proposal confidence scores, test failure diagnosis, and downstream evaluation scorecards.



## Configure third-party auth providers

When you connect the enrichment agent to third-party knowledge sources (such as Microsoft SharePoint, Atlassian Confluence and Jira, or GitHub), you must configure an Auth Provider using Google Cloud's Agent Identity service.

Agent Identity acts as a secure credentials manager that encrypts your third-party tokens inside your project, ensuring that human operators never have to handle raw client secrets during task execution.

For step-by-step instructions on generating the required tokens and configuring the auth provider for specific external platforms, see [Configure external connectors for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-connectors).

### Set up IAM permissions for auth providers

To allow the enrichment agent to securely retrieve your auth provider credentials dynamically during an active run, you must grant the **Agent Identity Admin** (`roles/agentidentity.admin`) role to the managed **Knowledge Catalog Service Agent** (`service-<var>PROJECT_NUMBER</var>@gcp-sa-dataplex.iam.gserviceaccount.com`). You can grant this role at either the auth provider resource level or the project level.

Additionally, the human user who attaches the auth provider to the task in the Google Cloud console must have the `agentidentity.authProviders.get` permission (included in **Agent Identity Viewer** (`roles/agentidentity.viewer`)) on the auth provider.

## Prepare Cloud Storage buckets

Cloud Storage serves as the primary file-based staging, context ingestion, and artifact export layer for knowledge enrichment workflows.

You can configure the agent to ingest files from one or more input buckets, folder paths, or individual files to ground its reasoning in your enterprise domain knowledge. Supported context types include:

  * **Domain documentation and data dictionaries** : Markdown, plain text, PDF, HTML, or CSV files containing table definitions, business glossaries, Standard Operating Procedures (SOPs), data pipeline architectures, or column naming guidelines. The **Knowledge signals** configuration supports whole buckets, folder paths (such as `bucket-name/folder/`), or individual file paths. We recommend that you organize these documents in a dedicated Cloud Storage bucket or folder separate from your evaluation datasets and unrelated files.

  * **Evaluation datasets** : JSONL files storing seed queries and held-out validation query sets. For more information, see the Format evaluation datasets section of this document.

  * **Reference SQL and transformation scripts** : Saved SQL scripts, dbt model definitions, or ETL transformation logic that provide contextual signals regarding table join patterns and business calculations.




When you configure an output bucket, the enrichment agent can also export structured bundles and run artifacts to that bucket. Supported output artifacts include:

  * **Detailed evaluation reports** : Comprehensive scorecards showing per-query accuracy deltas, test failure diagnosis, and confidence distribution metrics.



To ensure that the enrichment agent can work out of the bucket, make sure that your execution service account has the necessary permissions:

  * Grant the **Storage Object Viewer** (`roles/storage.objectViewer`) role on the input buckets so the agent can read staged documents and configuration files.
  * _(Optional)_ Grant the **Storage Object Creator** (`roles/storage.objectCreator`) role on the output bucket if you want the agent to save execution artifacts and validation logs.



To grant the service account access to the Cloud Storage buckets, follow these steps:

To add an IAM policy binding to a storage bucket, use the [`gcloud storage buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

  * `CUSTOMER_BUCKET`: the name of your Cloud Storage bucket
  * `SERVICE_ACCOUNT_NAME`: the name of your service account
  * `TARGET_PROJECT_ID`: your Google Cloud project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud storage buckets add-iam-policy-binding gs://CUSTOMER_BUCKET \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/storage.objectViewer"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud storage buckets add-iam-policy-binding gs://CUSTOMER_BUCKET `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/storage.objectViewer"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud storage buckets add-iam-policy-binding gs://CUSTOMER_BUCKET ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/storage.objectViewer"

## Format evaluation datasets

Enrichment workflows can automatically extract information without examples. However, providing evaluation datasets lets the agent test itself and improve its accuracy.

You can provide two types of datasets:

  * **Curation set** : A list of sample user questions and the expected SQL queries. The agent uses this list to practice and write better table summaries.

  * **Evaluation set** : A separate list of questions used to grade the agent's performance. If the agent performs poorly, this evaluation set prevents poor updates from being published to your catalog.




Alternatively, you can provide a single consolidated dataset. The enrichment service automatically partitions the data into a curation set and an evaluation set.

### Dataset schema requirements

Evaluation datasets must be formatted as JSONL files and stored in Cloud Storage. Each line in the file must contain a natural language question paired with the expected ground truth SQL query. The following table shows the accepted formatting fields:

Field name | Type | Description  
---|---|---  
`display_name` | `STRING` | Optional. An identifier or name for the evaluation request.  
`evaluation_request.prompt.text` | `STRING` | The natural language question or user prompt.  
`evaluation_request.golden_response.candidate` | `STRING` | Identifies the golden response. Set to `golden`.  
`evaluation_request.golden_response.text` | `STRING` | The ground truth, validated SQL query that answers the question. The autorater compares the agent's SQL to this query.  
  
**How evaluation results are graded** : A Gemini-based autorater checks whether the agent's final SQL is semantically equivalent to the ground truth SQL, meaning it returns the same answer. Formatting and alias differences aren't penalized. Each question passes or fails, and the quality score is the pass rate. Ground truth must be a SQL query. Custom metrics aren't supported.

The following snippet shows a valid `.jsonl` evaluation file:
    
    
    {"display_name": "revenue-2026", "evaluation_request": {"prompt": {"text": "What is total revenue for customer C100 in 2026?"}, "golden_response": {"candidate": "golden", "text": "SELECT SUM(amount) FROM `project.dataset.orders` WHERE customer_id = 'C100' AND EXTRACT(YEAR FROM order_date) = 2026;"}}}
    {"display_name": "monthly-subscribers", "evaluation_request": {"prompt": {"text": "List active subscribers on monthly billing"}, "golden_response": {"candidate": "golden", "text": "SELECT user_id, email FROM `project.dataset.subscriptions` WHERE status = 'ACTIVE' AND plan_type = 'MONTHLY';"}}}
    

## Configure agent traces for self-learning

To let the enrichment agent automatically analyze downstream Gemini Enterprise agent interactions or BigQuery agent analytics tables, you can optionally provide it with read access to your application's interaction traces.

Ingesting these traces enables the agent to perform _trajectory mining_. The agent discovers where downstream agents struggled due to missing context, clusters frequent user questions into high-impact query classes, and automatically curates the exact table summaries, column semantics, and business glossary terms needed to resolve those gaps.

Depending on your enterprise architecture, choose one of the following two setup methods:

  * **Direct Logging using scoped log views (Recommended)** : Create a log view restricted to only the application's telemetry to grant least-privilege read access. For instructions, see the Direct Logging using scoped log views section of this document.
  * **BigQuery agent analytics** : Grant read access to an exported BigQuery dataset if your organization natively routes interaction logs to a BigQuery log sink. For instructions, see the BigQuery agent analytics section of this document.



### Direct Logging using scoped log views (Recommended)

When interaction logging is enabled for an application, execution logs stream directly into Logging. You can create a dedicated log view restricted to your Gemini Enterprise application's usage audit logs and grant the execution service account access to that view. Because the enrichment service issues project-scoped log reads (`projects/<var>TARGET_PROJECT_ID</var>`), a view-level grant alone isn't sufficient—the execution service account must also have the `logging.logEntries.list` and `logging.views.access` permissions on the project that owns the Gemini Enterprise application. For instructions on turning on trace instrumentation and prompt-and-response logging for your Gemini Enterprise application, see [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).

  1. Create a scoped log view to isolate the logs. A scoped log view ensures that the view only exposes usage audit and inference telemetry from your Gemini Enterprise applications (by filtering on `logName="projects/<var>TARGET_PROJECT_ID</var>/logs/discoveryengine.googleapis.com%2Fgemini_enterprise_user_activity" OR logName=~"projects/<var>TARGET_PROJECT_ID</var>/logs/discoveryengine.googleapis.com%2Fgen_ai.*"`). For more information, see [Access Gemini Enterprise usage audit logs with Cloud Logging](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs).

### gcloud CLI

To create a scoped log view, use the [`gcloud logging views create` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/views/create):

Before using any of the command data below, make the following replacements: 

     * `LOG_VIEW_NAME`: the name of your log view
     * `TARGET_PROJECT_ID`: the ID of the Google Cloud project that owns your Gemini Enterprise application

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views create LOG_VIEW_NAME \
        --project=TARGET_PROJECT_ID \
        --location=global \
        --bucket=_Default \
        --log-filter='logName="projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgemini_enterprise_user_activity" OR logName=~"projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgen_ai.*"'

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views create LOG_VIEW_NAME `
        --project=TARGET_PROJECT_ID `
        --location=global `
        --bucket=_Default `
        --log-filter='logName="projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgemini_enterprise_user_activity" OR logName=~"projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgen_ai.*"'

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). **Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    gcloud logging views create LOG_VIEW_NAME ^
        --project=TARGET_PROJECT_ID ^
        --location=global ^
        --bucket=_Default ^
        --log-filter='logName="projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgemini_enterprise_user_activity" OR logName=~"projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgen_ai.*"'

### REST

Before using any of the request data, make the following replacements: 

     * `LOG_VIEW_NAME`: the name of your log view
     * `TARGET_PROJECT_ID`: the ID of the Google Cloud project that owns your Gemini Enterprise application

HTTP method and URL: 
    
    POST https://logging.googleapis.com/v2/projects/TARGET_PROJECT_ID/locations/global/buckets/_Default/views?viewId=LOG_VIEW_NAME

Request JSON body: 
    
    {
     "filter": "logName=\"projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgemini_enterprise_user_activity\" OR logName=~\"projects/TARGET_PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgen_ai.*\""
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://logging.googleapis.com/v2/projects/TARGET_PROJECT_ID/locations/global/buckets/_Default/views?viewId=LOG_VIEW_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://logging.googleapis.com/v2/projects/TARGET_PROJECT_ID/locations/global/buckets/_Default/views?viewId=LOG_VIEW_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

  2. After you create the log view, grant the execution service account the **Logs View Accessor** (`roles/logging.viewAccessor`) role on the view, and ensure that the service account also has the `logging.logEntries.list` permission on the project that owns the Gemini Enterprise application.

To add an IAM policy binding to a log view, use the [`gcloud logging views add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/views/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `LOG_VIEW_NAME`: the name of your log view
     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views add-iam-policy-binding LOG_VIEW_NAME \
        --location=global \
        --bucket=_Default \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/logging.viewAccessor"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views add-iam-policy-binding LOG_VIEW_NAME `
        --location=global `
        --bucket=_Default `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/logging.viewAccessor"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views add-iam-policy-binding LOG_VIEW_NAME ^
        --location=global ^
        --bucket=_Default ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/logging.viewAccessor"


**Note:** If your organization doesn't use custom log views, or to satisfy the project-level pre-flight check in the Google Cloud console wizard, grant the **Private Logs Viewer** (`roles/logging.privateLogViewer`) role to the execution service account on the project that owns the Gemini Enterprise application.

For more information, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

### BigQuery agent analytics

If your organization streams interaction logs into BigQuery using a Logging log sink or writes directly to BigQuery agent analytics tables, you can grant access to the dataset instead.

Ensure that the interaction logs are configured to stream to a designated BigQuery dataset, and verify that the execution service account is granted the **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) role on the agent analytics table (or its dataset) and the **BigQuery Job User** (`roles/bigquery.jobUser`) role on the project that contains that table. These roles let the agent run query jobs and read the exported telemetry directly from BigQuery.

For more information on exporting logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export).

## Enable data profiling and data insights

Before you run an enrichment task, we recommend that you enable data profiling and AI data insights on your frequently used target tables. Data profiling provides statistical characteristics—such as common values, data distributions, and null counts—and data insights generate baseline table descriptions and sample queries. Providing these signals helps the enrichment agent generate more accurate metadata proposals.

  * For more information about configuring data profile scans, see [Create and use data profile scans](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).
  * For more information about generating AI data insights, see [Use data insights for structured data](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-insights-structured-data).



## What's next

  * [Create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
