---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/build-context-sets/
title: Build and optimize context sets with the context engineering agent \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:23:33.415863+00:00
---

# Build and optimize context sets with the context engineering agent  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/build-context-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Build and optimize context sets with the context engineering agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To achieve high QueryData query accuracy and low online latency in your data agent applications, you can use the context engineering agent to build, evaluate, and optimize context sets. By automating context creation, upload, and optimization, the agent helps your applications return fast, deterministic, and explainable answers to natural language questions.

To learn about context sets and QueryData, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/context-sets-overview) and [QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/data-agent-overview).

By providing [QueryData](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/data-agent-overview) with context tailored to your business application, you supply the precise business rules that the system needs to resolve nuanced user intent and deliver near-100% query quality. As you work in your CLI or IDE, the context engineering agent automatically uploads your context sets to Google Cloud while saving local files in your workspace for version control.

## Context engineering agent

The context engineering agent acts as your design-time assistant directly in your CLI or IDE. Manual context authoring requires writing detailed query patterns by hand, anticipating every phrasing variation, and manually diagnosing query failures across iterations. The context engineering agent eliminates this overhead by bootstrapping baseline context, curating ground-truth evaluation datasets, iteratively hill-climbing to fix accuracy gaps, and proving that your context generalizes across new questions.

You converse with the agent by using natural language to drive the optimization workflow. Start with a prompt like _"Optimize the context set against my application requirements."_

## Before you begin

Before you use the context engineering agent, complete the prerequisites in the following sections. You can create and store context sets in the `us-central1`, `us-east1`, `europe-west4`, and `asia-southeast1` regions, even if your database instance is in a different region.

### Enable required services

Enable the following services for your project:

  * [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com)
  * [Gemini for Google Cloud API](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com)
  * [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)



### Prepare your database

Prepare your Cloud SQL for PostgreSQL instance and configure access for the agent:

  * Create a [Cloud SQL for PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance) and [create a database on the Cloud SQL for PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases#create), or use an existing instance and database.
  * Enable Data API access on your Cloud SQL for PostgreSQL instance. Set the Data API access (`data_api_access`) setting to `ALLOW_DATA_API` on your instance so that the agent can inspect schemas and validate queries. For instances created without Data API access enabled, see [Enable Data API access](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp#execute-sql) or configure it in the Google Cloud console.



### Required roles and permissions

To get the permissions that you need to use the context engineering agent and manage context sets, configure the following Identity and Access Management (IAM) roles and database privileges:

  * Add an IAM user or service account to the instance. For more information, see [Manage users with IAM database authentication for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users).
  * Grant the `roles/cloudsql.instanceUser` (or `roles/cloudsql.studioUser` if you also test queries in Cloud SQL Studio), `roles/serviceusage.serviceUsageConsumer`, `roles/geminidataanalytics.queryDataUser`, and `roles/mcp.toolUser` roles to the IAM user or service account at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
  * To create, upload, and manage context sets, grant the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role to the IAM user or service account at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).
  * If you use semantic value searches (`google_ml.embedding`), enable the Vertex AI API and grant the `roles/aiplatform.user` role to the Cloud SQL for PostgreSQL instance's service account.
  * Grant read-only database privileges to an IAM user or service account by signing in as a user with superuser privileges, such as the `postgres` user:
        
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO "USER_NAME";
        

Replace `USER_NAME` with the email address for the user (for a service account, omit the `.gserviceaccount.com` suffix). You must use quotes around the username because it contains special characters (`@` and `.`). If your tables are in a custom schema other than `public`, also run `GRANT USAGE ON SCHEMA SCHEMA_NAME TO "USER_NAME";` and `GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "USER_NAME";`. For more information, see [Grant database privileges to an individual IAM user or service account](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#grant-db-privileges).




## Prepare your environment

You can build and optimize context sets from your local development environment or IDE.

### Install uv

The context engineering agent requires `uv` to manage underlying Python packages:

  1. Install `uv` by following the instructions in [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/).

  2. Verify that `uv` is installed and accessible from your command line:
         
         uv --version




### Install the context engineering agent

Install the context engineering agent plugin in your preferred development environment:

### Antigravity CLI

  1. Install the Antigravity CLI. See [Get started with Antigravity CLI](https://antigravity.google/docs/getting-started?tab=cli).
  2. Install the context engineering agent plugin: 
         
         agy plugin install https://github.com/GoogleCloudPlatform/db-context-enrichment/tree/main/plugin

  3. Start the Antigravity CLI: 
         
         agy




To update the plugin later, run `agy plugin uninstall db-context-engineering` followed by `agy plugin install https://github.com/GoogleCloudPlatform/db-context-enrichment/tree/main/plugin`.

### Claude Code

  1. Add the plugin marketplace: 
         
         /plugin marketplace add https://github.com/GoogleCloudPlatform/db-context-enrichment.git

  2. Install the plugin: 
         
         /plugin install db-context-engineering@db-context-enrichment-marketplace

  3. Reload plugins to activate the changes: 
         
         /reload-plugins




To update the plugin later, run `/plugin update db-context-engineering@db-context-enrichment-marketplace`.

### Gemini CLI (Deprecated)

**Note:** Gemini CLI support is deprecated. If you are using Gemini CLI, migrate to the Antigravity CLI. For more information, see [Migrating from Gemini CLI](https://antigravity.google/docs/cli/gcli-migration).

  1. Install the Gemini CLI. See [Get Started with Gemini CLI](https://geminicli.com/docs/get-started/).
  2. Install the extension: 
         
         gemini extensions install https://github.com/GoogleCloudPlatform/db-context-enrichment




To update the extension later, run `gemini extensions update google-cloud-db-context-engineering`.

### Authenticate with Google Cloud

  1. Configure [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) to authenticate your development environment:
         
         gcloud auth application-default login

  2. Set the quota project for your credentials so that the Model Context Protocol (MCP) tools can use your Google Cloud project:
         
         gcloud auth application-default set-quota-project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project ID.




### Connect to your database

  1. Start your agent environment and ask the agent to establish the database connection (for example, _"Help me set up the database connection"_). The agent guides you through creating the `.context-engineering/tools.yaml` configuration file so that it can read schemas and validate SQL. (Before `.context-engineering/tools.yaml` is created, an initial `toolbox` MCP server connection warning on startup is expected.)

  2. Reload the MCP server connection to apply the `.context-engineering/tools.yaml` configuration:

     * Antigravity CLI: Run `/mcp` and select `toolbox` (or `db-context-engineering_toolbox`) to restart.
     * Claude Code: Run `/mcp`, select `toolbox`, and select `Reconnect`.
     * Gemini CLI: Run `/mcp refresh` (or `/mcp reload`).



## Build and optimize context

The context engineering agent guides your context set through an end-to-end lifecycle, from initial bootstrapping to verified generalizability.

### Bootstrap a baseline context set

To avoid creating context from a blank page, the agent inspects your database schema along with any available application artifacts, such as business requirements, documentation, or sample SQL queries. The agent derives an initial baseline context set containing foundational query templates and query facets grounded in your database model.

After generating and validating the baseline context, the agent uploads it directly to Google Cloud and returns the context set resource name.

### Create evaluation and held-out datasets from application artifacts

To systematically improve accuracy, you need ground-truth questions paired with verified SQL queries. If you don't already have an evaluation benchmark, the agent can generate one by extracting business scenarios from your application code, historical queries, and database schema.

During dataset generation, the agent creates two distinct sets:

  * Training benchmark: A collection of representative question-SQL pairs used during iterative optimization.
  * Held-out dataset: A separate set of questions similar in domain to your training benchmark, reserved for testing for generalizability.



### Optimize accuracy with hill-climbing

In hill-climbing optimization, the agent iteratively refines your context set to drive QueryData accuracy toward near-100%:

  * Evaluate: The agent tests your current context set against the training benchmark by using the QueryData API and scores accuracy.
  * Diagnose gaps: The agent analyzes query failures, identifies their root causes (such as missing table joins, unlinked private entities, or complex filter conditions), and formulates targeted fixes.
  * Refine and upload: The agent adds or improves query templates, query facets, and value searches to resolve the gaps, and automatically uploads the updated context set to Google Cloud from your CLI.
  * Iterate: The agent repeats this cycle across rounds until accuracy converges on the optimal score.



The following diagram shows the systematic hill-climbing workflow:

![Workflow for iteratively building context.](https://docs.cloud.google.com/static/docs/databases/images/context-engineering-agent-hillclimb.png)

### Prove generalizability with the held-out dataset

Achieving high accuracy on a training benchmark is necessary, but production traffic includes phrasing variations and complex compound questions that were never seen during development.

After hill-climbing optimization converges, the agent tests the resulting context set against the held-out dataset. This step verifies that the context set generalizes cleanly to new user inputs without overfitting to the initial benchmark. The agent produces a generalizability report showing accuracy across unseen question variations and composite filters (such as _"Find me homes near good schools in Del Mar for a starter family with an ocean view"_).

## On-demand authoring and reasoning

In addition to full optimization runs, you can converse with the agent for targeted updates as business requirements evolve:

  * Targeted authoring: Describe a specific business requirement in natural language, and the agent formats the context item and uploads it directly from your CLI without manual editing:

    * _"Create a template for: 'Find me homes near good schools in Del Mar' with SQL:`SELECT p.property_id, p.address FROM properties AS p JOIN schools AS s ON p.school_id = s.school_id WHERE p.city = 'Del Mar' AND s.rating >= 7`."_
    * _"Create a facet for the filter`properties.bedrooms BETWEEN 3 AND 4 AND properties.square_feet BETWEEN 1500 AND 2500` labeled 'for a starter family'."_
    * _"Create a value search for`properties.city`."_
  * Bulk updates across a context set: If database columns are renamed or table structures change, the agent can update all affected context items simultaneously without modifying unrelated entries:

    * _"In my context set, replace`properties.property_type = 'SFR'` with `properties.property_type = 'Single Family Residential'` for any item referencing single-family homes. Leave unrelated items alone."_



## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/context-sets-overview).
  * Learn how to [test QueryData in Cloud SQL Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent).
  * Learn how to [integrate QueryData with an application](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/integrate-applications-data-agent).
  * Learn how to [create or delete a context set in Cloud SQL Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/manage-data-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
