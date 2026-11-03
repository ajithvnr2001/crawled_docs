---
url: https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks/
title: Create enrichment tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T09:44:34.437907+00:00
---

# Create enrichment tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Create enrichment tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knowledge Studio enrichment tasks let you automatically extract business context from your schemas, standard operating procedures (SOPs), code repositories, and query logs. When you create an enrichment task, you configure target resources, knowledge signals, evaluation benchmarks, and a schedule to generate metadata proposals that ground your AI applications.

## Before you begin

Follow these prerequisites before you create an enrichment task.

### Understand the concepts

Before you run an enrichment task, we recommend that you familiarize yourself with the core components of the enrichment architecture:

  * For an overview of how Knowledge Studio agents automate metadata generation, see [About enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks).

  * For an overview of how metadata context grounds AI agents and simplifies data exploration, see [About data context](https://docs.cloud.google.com/knowledge-catalog/docs/about-context).

  * For an overview of the Knowledge Catalog hierarchy, including entry groups, entries, aspects, and entry links, see [About metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).




### Prepare required components

Before you create an enrichment task, ensure that your environment is properly configured for AI enrichment. For setup instructions, see [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites).

Have the following components ready:

  * **Service account** : A dedicated user service account with the required roles. Throughout this documentation, the term _execution service account_ refers to this customer-managed service account to differentiate it from the Google-managed Knowledge Catalog service agents. The enrichment task runs as this service account and uses it to read the sources and write to the context set.

  * **Context set** : A destination context set to save the enriched metadata to. Context sets are regional, multi-regional, or global, and each context set can be enriched by only one enrichment task per region. The context set also serves as the default source of assets to enrich; everything in the context set is enriched by default unless you filter the default resources during setup. You can also create an empty context set during the task setup if one doesn't exist. For more information, see the Create a context set section in [Manage context sets](https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets#create-context-set).

  * **Resources to enrich** (Optional): Additional data assets that you want to enrich that are not already in your destination context set. Adding these additional resources during task creation enriches them and automatically adds them to the destination context set when the run's proposals are approved. Target resources can include BigQuery datasets and tables or Lakehouse catalogs, namespaces, and tables (up to 500 total resources across default and added resources). For information about resource name syntax, see [Full resource names](https://docs.cloud.google.com/iam/docs/full-resource-names).

  * **Knowledge signals** (Optional): If you plan to provide the AI agent with documents, glossaries, or SQL scripts to learn from, ensure that you prepare your Cloud Storage buckets, folders, or files, format your `.jsonl` evaluation datasets, or configure third-party auth providers for third-party source URLs. For third-party connector setup instructions, see [Configure external connectors for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-connectors).

  * **Trace logs** (Optional): If you plan to enable agent self-learning, configure a Gemini Enterprise application (with trace instrumentation and prompt-and-response logging turned on in Cloud Logging) or a BigQuery agent analytics table from which the enrichment agent can learn historical interactions. For more information, see [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings) and the Configure agent traces for self-learning section in [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#configure-agent-traces).

  * **Data profiling and data insights** (Recommended): To improve the quality of generated metadata proposals, enable data profiling and AI data insights on your frequently used target tables before running the task.




### Required roles

Setting up and running enrichment tasks involves three identities, each requiring specific IAM roles:

  * **The end user (your user account)** : Creates, configures, and triggers the enrichment task in Knowledge Studio.
  * **The execution service account (customer-managed)** : Runs the enrichment task, reads your source assets and optional interaction traces, and proposes metadata updates to your context set.
  * **The Knowledge Catalog Service Agent (Google-managed)** : Impersonates your execution service account during a run and executes backend BigQuery sampling, query-history analysis, and validation query jobs.



#### The end user

To get the permissions that you need to create, modify, and run enrichment tasks, ask your administrator to grant you the following IAM roles: 

  * Create, modify, and run enrichment tasks: **Dataplex DataScan Editor** (`roles/dataplex.dataScanEditor`) or **Dataplex Editor** (`roles/dataplex.editor`) on the project 
  * Attach the execution service account to the enrichment task: [**Service Account User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the execution service account 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create, modify, and run enrichment tasks. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create, modify, and run enrichment tasks:

  * Create, view, list, update, delete, and run enrichment tasks: 
    * `dataplex.agentTasks.create`
    * `dataplex.agentTasks.get`
    * `dataplex.agentTasks.getData`
    * `dataplex.agentTasks.list`
    * `dataplex.agentTasks.update`
    * `dataplex.agentTasks.delete`
    * `dataplex.agentTasks.run`
  * Attach the execution service account: `iam.serviceAccounts.actAs`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### The execution service account

The execution service account is the customer-managed identity under which the enrichment task runs and performs all operations.

To ensure that the execution service account has the necessary permissions to run the enrichment task, read target data, and propose metadata updates, ask your administrator to grant the following IAM roles to the execution service account: 

**Important:** You must grant these roles to the execution service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Consume APIs during task execution: [**Service Usage Consumer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on the project that contains the enrichment task 
  * View target BigQuery datasets and tables: [**BigQuery Data Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the target BigQuery datasets and tables 
  * View target Lakehouse assets (when enriching Lakehouse assets): [**BigLake Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the target Lakehouse catalogs, namespaces, and tables 
  * Propose and write metadata into context sets: 
    * [**Dataplex Content Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.contentEditor) (`roles/dataplex.contentEditor`) on the target context set
    * [**Dataplex Catalog Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project
    * [**Dataplex Catalog Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project
  * _(Optional)_ Run BigQuery jobs on the task project (required only if job creation is moved inside a VPC Service Controls perimeter): [**BigQuery Job User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the task project 
  * _(Optional)_ Automatically approve and publish proposed changes (if you enable auto-publish): [**Dataplex Workflow Approver** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowApprover) (`roles/dataplex.workflowApprover`) on the project 
  * _(Optional)_ Learn from existing Logging trace logs (self-learning): [**Private Logs Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`) on the project that owns the Gemini Enterprise app 
  * _(Optional)_ Learn from a BigQuery agent analytics table (self-learning): 
    * [**BigQuery Data Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the agent analytics table (or its dataset)
    * [**BigQuery Job User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project that contains the agent analytics table



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to run the enrichment task, read target data, and propose metadata updates. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to run the enrichment task, read target data, and propose metadata updates:

  * Consume quota and services: `serviceusage.services.use`
  * View BigQuery dataset and table metadata and read table data: 
    * `bigquery.datasets.get`
    * `bigquery.tables.get`
    * `bigquery.tables.getData`
  * View Lakehouse catalogs, namespaces, and tables: 
    * `biglake.catalogs.get`
    * `biglake.namespaces.get`
    * `biglake.tables.get`
    * `biglake.tables.list`
  * View and propose changes to context sets and entries: 
    * `dataplex.entryGroups.getContextSet`
    * `dataplex.entryGroups.requestContextChanges`
    * `dataplex.entries.createContext`
    * `dataplex.entries.updateContext`
    * `dataplex.entries.getContext`
    * `dataplex.entries.listContext`
    * `dataplex.entryLinks.create`
  * Create, update, view, and list catalog entries and entry groups: 
    * `dataplex.entries.create`
    * `dataplex.entries.update`
    * `dataplex.entries.get`
    * `dataplex.entries.list`
    * `dataplex.entryGroups.create`
    * `dataplex.entryGroups.update`
    * `dataplex.entryGroups.requestChanges`
  * _(Optional)_ Run BigQuery jobs (for VPC Service Controls perimeters or BigQuery agent analytics tables): `bigquery.jobs.create`
  * _(Optional)_ Automatically approve change requests: `dataplex.changeRequests.use`
  * _(Optional)_ Read Logging views and log entries: 
    * `logging.views.access`
    * `logging.logEntries.list`



Your administrator might also be able to give the execution service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### The Dataplex Service Agent

The Knowledge Catalog Service Agent is a Google-managed service account that Knowledge Catalog uses to perform backend operations on your behalf, such as impersonating your execution service account during an enrichment run and running BigQuery sampling, query-history analysis, and validation query jobs.

The Knowledge Catalog Service Agent uses the following email format:

`service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`

Replace `PROJECT_NUMBER` with your Google Cloud project number.

Granting query history access (recommended) lets the enrichment agent analyze historical SQL queries (`INFORMATION_SCHEMA.JOBS_BY_PROJECT`) to identify common join keys and filters. If the **BigQuery Resource Viewer** (`roles/bigquery.resourceViewer`) role isn't granted, the agent skips query-history analysis without failing the run.

To ensure that the Knowledge Catalog Service Agent has the necessary permissions to impersonate the execution service account and perform backend BigQuery profiling, ask your administrator to grant the following IAM roles to the Knowledge Catalog Service Agent: 

**Important:** You must grant these roles to the Knowledge Catalog Service Agent, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Impersonate the execution service account to run the task: [**Service Account Token Creator** ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) on the execution service account 
  * Perform backend BigQuery profiling and validation queries: [**BigQuery Data Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the projects or datasets that contain the target tables 
  * _(Recommended)_ Read BigQuery query history at the project level: [**BigQuery Resource Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.resourceViewer) (`roles/bigquery.resourceViewer`) on the projects where queries run 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to impersonate the execution service account and perform backend BigQuery profiling. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to impersonate the execution service account and perform backend BigQuery profiling:

  * Generate tokens and sign payloads for service account impersonation: 
    * `iam.serviceAccounts.getAccessToken`
    * `iam.serviceAccounts.getOpenIdToken`
    * `iam.serviceAccounts.signJwt`
    * `iam.serviceAccounts.signBlob`
  * View BigQuery dataset and table metadata and read table data: 
    * `bigquery.datasets.get`
    * `bigquery.tables.get`
    * `bigquery.tables.getData`
  * _(Recommended)_ List BigQuery jobs and view project metadata: 
    * `bigquery.jobs.listAll`
    * `resourcemanager.projects.get`



Your administrator might also be able to give the Knowledge Catalog Service Agent these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Open the Knowledge Studio workspace

To open the task creation wizard, perform the following steps:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the navigation pane, select **Enrichments**.

  3. Click **\+ Create enrichment task**.




### Name the enrichment task

In the **Define** pane, perform the following steps:

  1. In the **Display name** field, provide a descriptive name for the task (for example, `Finance Dataset enrichment`).
  2. In the **Task ID** field, provide a unique ID or use the auto-generated ID.
  3. In the **Goal** field, describe the objective of the enrichment task to guide the extraction process. Provide natural language guidance detailing the business mission and AI capability goals for this context set.

For example:
         
         Curate and maintain the authoritative context set for the
         `subscription_revenue` domain. Focus on resolving metric discrepancies
         between `gross_sales`, `net_billed_revenue`, and `discount_applied`.
         Ensure all customer join keys (e.g. `customer_id`, `subscription_fk`)
         have explicit column documentation, and establish parameterized query
         templates for Monthly Recurring Revenue (MRR) and Churn Rate calculations.
         

  4. Click **Continue**.




### Configure the enrichment task parameters

The scope specifies what gets enriched and what the agent reads.

In the **Scope** pane, perform the following steps:

  1. In the **Project** field, select the project that contains the context set.

  2. In the **Context set** field, select the context set that the task enriches and to which the task saves its results. If you don't have a context set, click **Create new context set**.

Context sets are regional, multi-regional, or global, and each context set can be enriched by only one enrichment task per region. If you select a context set that is already attached to an existing enrichment task in that region, the wizard displays an error message with a link to the existing task and requires you to select a different context set. After you create an enrichment task, you can't change its context set.

  3. If the context set you selected is located in a multi-region (such as `us` or `eu`) or in `global`, select a single region in the **Enrichment task region** field where the enrichment task runs (for example, `us-central1`). If the context set is located in a single region, the task automatically uses the context set's region.

  4. In the **Resources to enrich** section, review the default resources and optionally add more BigQuery or Lakehouse resources:

     * **Default resources** : Everything in the selected context set is enriched by default. Expand **Default resources** to review or filter the prefilled tables from your context set.
     * **Add more BigQuery or Lakehouse resources** : Add BigQuery datasets or tables or Lakehouse catalogs, namespaces, or tables that you want to enrich in addition to the context set. Adding these resources also adds them to the context set when the run's proposals are approved. An enrichment task supports up to **500 total resources** across default and added resources.

Any resources you add must match the location of your context set. A multi-region context set (such as `us`) matches single regions within that location (such as `us-central1`), and a `global` context set accepts resources from any region. Mismatched regions cause task creation to fail.

If you select an empty context set and don't add any additional resources in this section, Knowledge Studio displays a warning. If you run the task with this configuration, it generates a semantic knowledge base based on your instructions, but it does not enrich any table entries.

To add resources by full resource name, enter the resource name in the text field (use commas to separate multiple resource names):

     * **BigQuery table** : `//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID`

     * **Lakehouse asset** : `//dataplex.googleapis.com/projects/PROJECT_ID/locations/LOCATION/lakes/LAKE_ID/zones/ZONE_ID/assets/ASSET_ID`

Alternatively, to select resources visually, perform the following steps:

     1. Click **Browse** to open the **Select sources** dialog.
     2. To select from recently used resources, click the **Recent** tab and select the resources that you want to add.
     3. To browse or search all resources, click the **All** tab and do the following: 
        1. In the **Search** field, enter a search term for your BigQuery or Lakehouse resource.
        2. In the resource tree, expand the project and dataset hierarchy to locate your resource.
        3. Select the checkbox beside one or more resources. You can preview the schema and details of the selected resource in the details pane.
        4. Click **Confirm**.
  5. Optional: In the **Knowledge signals** section, connect the AI agent to extra sources to read for context. These resources are read-only and are not enriched.

     * **Cloud Storage buckets, folders, or files** : Enter a bucket name, a folder path ending with a slash (such as `bucket-name/folder/`), or an individual path, or click **Browse** to select buckets, folders, or files (up to 1,000 Cloud Storage sources). Press `Enter`, comma, or `Space` after each entry.
     * **Glossaries** : Enter the glossary name, or click **Browse** to search for a glossary. Press `Enter`, comma, or `Space` after each glossary name.

Ensure that any connected glossaries are located in a compatible region or `global` scope.

     * **External sources** : To connect third-party platforms such as Google Workspace, Microsoft SharePoint, GitHub, or Atlassian (Confluence spaces and Jira projects), you can configure them individually or provide a YAML configuration file.

To configure sources using a YAML file:

       1. In the **Source configuration file (optional)** field, click **Browse** and select your YAML file.

To configure a source manually:

       1. Under **Connected sources** , click **Set up** next to the platform you want to configure.
       2. In the **Source URLs** field, enter the URLs for your documents, repositories, spaces, or Jira projects, and then press `Enter` or comma after each URL.
       3. If the platform requires authentication (such as GitHub, Atlassian, or Microsoft), attach your credentials by doing the following:

          1. Click **\+ Add connection**.
          2. In the **New connection** pane, enter the full resource name of your auth provider in the **Auth provider** field. Use the following format:   
`projects/PROJECT_ID/locations/LOCATION/authProviders/PROVIDER_NAME`
          3. Under **URI patterns** , click **\+ Add URI pattern** to specify which URLs this credential has permission to access. You can use asterisks (`*`) as wildcards (for example, `https://github.com/test-org/*`).
          4. Click **Done**.

Google Workspace resources connect directly using your task's execution service account IAM permissions, so they don't require an auth provider connection.

  6. Click **Continue**.




### Configure evaluation and self-learning

The settings in the **Improve** pane are optional. For information on formatting evaluation and curation datasets, see [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#dataset-schema). For information on selecting a model in Gemini Enterprise, see the "Create an agent using the flow builder" section in [Design agents in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/design-agents).

In the **Improve** pane, perform the following steps:

  1. Optional: In the **Evaluation** section, configure the following fields:

     * **Evaluation set** : To measure the impact of proposed context changes, enter a Cloud Storage URI or click **Browse** to select your `.jsonl` file.

     * **Curation set** : To provide a set of seed questions for iterative optimization, enter a Cloud Storage URI or click **Browse** to select your `.jsonl` file.

  2. Optional: In the **Publishing** section, specify the publishing cadence:

When you enable auto-publish, the agent stages proposals as change requests and automatically approves the run if it meets all publishing criteria, leaving an audit record. Deletion proposals are always held for manual review. When you disable auto-publish, a human reviewer must approve the change requests before they are published to the context set.

     * To require human review before metadata is merged into your production context set, clear the **Enable auto-publish** checkbox.

     * To automatically publish runs that meet your quality criteria, select the **Enable auto-publish** checkbox. Use the **Auto-publish above** slider to set the minimum overall confidence score required for a run to publish automatically (default is _85%_). Every proposal must also pass validity checks (such as valid SQL syntax). If an evaluation dataset is configured, you can also use the **Maximum quality drop** slider to restrict publishing when evaluation accuracy drops by more than the specified threshold (default is _5%_). If a run doesn't meet all of these conditions, all proposals remain staged as change requests for manual review.

  3. Optional: To find gaps in real agent conversations and keep your context current, in the **Self-learning** section, select the **Enable self-learning** toggle.

  4. Optional: If you enabled self-learning, under the **Learn from** section, add any of the following sources:

     * **Gemini Enterprise apps** : In the **Project ID** list, select the project. In the **Gemini Enterprise app** list, select the app generating conversation traces, and then click **Done**. You can add multiple Gemini Enterprise apps. To optimize enrichment and self-learning capabilities, we recommend that you specify a Gemini 3.8 Flash or later model in the Gemini Enterprise application.

     * **BigQuery agent analytics** : In the **Table** field, enter the name of the table containing agent chat events or click **Browse** to select it visually, and then click **Done**. You can add multiple tables.

  5. Click **Continue**.




### Configure the run settings

In the **Run** pane, perform the following steps:

  1. In the **Run as** section, click the **Service account** list and select the execution service account that the task uses to read the sources and write to the context set.

When you select a service account, Knowledge Studio automatically runs Policy Troubleshooter to check the execution service account, the Knowledge Catalog service agent, and your target resources:

     * If any required roles are missing and you have permission to modify IAM policies on those resources, click **Grant all** to grant the missing roles automatically.
     * _(Recommended)_ Select **Grant access to BigQuery query history** to grant the **BigQuery Resource Viewer** (`roles/bigquery.resourceViewer`) role (`bigquery.jobs.listAll`), and optionally specify additional project IDs in the **Query history project IDs** field where BigQuery queries run.
  2. Under **Trigger** , select the trigger condition:

     * **On demand** : Runs only when you click **Run**.
     * **Scheduled** : Runs automatically on a repeating schedule (such as daily, weekly, or monthly). All scheduled run times use Coordinated Universal Time (UTC).
  3. Optional: Under **Notifications** , click **\+ Add recipient** to specify up to five email addresses to receive a report after every run.

  4. Verify the parameters in the **Summary** pane, and then click **Create**.




Your new enrichment task is saved. Depending on your trigger settings, the task either awaits its first scheduled execution or is ready to run immediately. Enrichment runs typically take 20 to 60 minutes to complete, or up to several hours for large datasets with curation and evaluation sets enabled. Execution logs can take 20 to 30 minutes to begin appearing while the agent initializes and extracts signals. When the task finishes an execution run, the agent queues the generated AI metadata proposals in one or more change request batches for your review.

## What's next

  * [Manage enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-tasks)
  * [Evaluate and approve enrichment proposals](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
