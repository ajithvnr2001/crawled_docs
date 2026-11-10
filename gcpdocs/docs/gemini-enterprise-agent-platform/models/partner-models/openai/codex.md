---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai/codex/
title: Connect OpenAI Codex to Google Cloud \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:35:47.793053+00:00
---

# Connect OpenAI Codex to Google Cloud  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai/codex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Connect OpenAI Codex to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

**Private Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can configure the OpenAI Codex CLI and Codex Desktop App to route model requests through your Google Cloud project on Agent Platform.

Codex runs locally on your development workstation while authenticating through Google Cloud Identity and Access Management (IAM) and using your approved Marketplace quotas.

## Before you begin

To use OpenAI Codex with Gemini Enterprise Agent Platform, you must complete the following steps. The Gemini Enterprise Agent Platform API (`aiplatform.googleapis.com`) must be enabled on your Google Cloud project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  8. Complete the onboarding steps in [OpenAI GPT Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai#preview-access), including purchasing the product through Google Cloud Marketplace and enabling the model in Model Garden.

  9. If your organization's policy restricts model access, [allow the model in that policy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access).

  10. Install the Google Cloud CLI and configure Application Default Credentials (ADC):
         
         gcloud auth application-default login

  11. Install the OpenAI Codex CLI or Codex Desktop App on your workstation.




### Required roles

To get the permissions that you need to connect Codex to OpenAI partner models, ask your administrator to grant you the [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Interactive setup

You can configure Codex interactively using the built-in sign-in flow.

### Codex CLI

  1. Start `codex` in your terminal:
         
         codex

  2. Select **Sign in another way** , then choose **Use Google Cloud** (displayed as **Use Google Cloud Vertex AI** in the CLI).

  3. Enter your Google Cloud project ID.

  4. Enter the location, or press Enter to accept `global`.

  5. Press Enter to use Application Default Credentials on your computer, or enter an absolute path to a service account credential JSON file.




### Codex Desktop App

  1. Open the Codex Desktop App.
  2. Select **Sign in another way** , then choose **Use Google Cloud**.
  3. Enter your Google Cloud project ID.
  4. Enter the location, or leave it blank to accept `global`.
  5. Leave the credential path blank to use Application Default Credentials, or select a service account key JSON file.
  6. Select **Continue** , then verify the connection.



## Configure Codex manually

To configure Codex without the interactive prompt, add the provider settings to `~/.codex/config.toml`. Place the top-level `model_provider` setting before any table headers:
    
    
    model_provider = "gcp"
    
    [model_providers.gcp]
    project_id = "PROJECT_ID"
    location = "global"

Replace the following:

  * `<var>PROJECT_ID</var>`: Your Google Cloud project ID (for example, `my-project-123`).



If you use a service account key file rather than Application Default Credentials, specify `credential_file`:
    
    
    credential_file = "CREDENTIAL_FILE_PATH"

Replace the following:

  * `<var>CREDENTIAL_FILE_PATH</var>`: The absolute path to your downloaded service account key JSON file (for example, `/Users/myuser/.config/gcloud/sa-key.json`).

**Caution:** Service account keys can pose security risks if compromised. Whenever possible, use Application Default Credentials or short-lived tokens instead of storing service account keys on your local workstation. For more information, see [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

### Environment variables

You can also use environment variables on the Codex host machine to configure or override your settings:

  * `GOOGLE_CLOUD_PROJECT`: Sets your Google Cloud project ID, allowing you to omit `project_id` from `config.toml`.
  * `GOOGLE_CLOUD_LOCATION`: Overrides the endpoint location (defaults to `global`).



## Select models and verify access

After setup, verify your connection and model access:

  1. Start a new session with `codex` or create a new task in Codex Desktop.
  2. Run `/model` in the CLI or open the model picker in Codex Desktop.
  3. Select an enabled model for your workload: 
     * `gpt-6.1-sol`: Flagship partner model for coding and agentic workflows.
     * `gpt-6-luna`: Low-latency partner model for fast interactive assistance.
     * `gpt-6-astra`: Highest-capability partner model for complex multi-step reasoning.
     * `gpt-6.1-terra`: Balanced partner model for high-throughput automation.
  4. Send a test prompt (such as "List the files in the current directory") to confirm that authentication and request processing succeed.



## Feature support in Codex

When connected to Agent Platform, Codex uses the OpenAI Responses API. The following table outlines supported and unsupported features:

Feature | Support status | Description  
---|---|---  
Local shell and bash execution | Supported | Codex runs shell commands locally on your development machine within approved terminal boundaries.  
File editing and patching | Supported | Codex reads and modifies files locally on your workstation.  
Local Model Context Protocol (MCP) | Supported | Local MCP servers configured in `~/.codex/config.toml` run on your workstation.  
Client-side function calling | Supported | Model tool requests are evaluated and executed locally by the Codex client.  
Hosted web search and file search | Not supported | Hosted OpenAI search tools aren't available on Agent Platform endpoints during Private Preview.  
Hosted Code Interpreter | Not supported | Remote cloud sandboxes hosted by OpenAI aren't available. Code execution runs locally using local tools.  
  
## What's next

  * Explore programmatic SDK integration in [Responses API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai/responses).
  * Review model capabilities and specifications in [OpenAI GPT Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai).
  * Learn about [Abuse monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring) and [Zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
