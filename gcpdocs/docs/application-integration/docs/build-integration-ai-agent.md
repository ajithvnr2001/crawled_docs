---
url: https://docs.cloud.google.com/application-integration/docs/build-integration-ai-agent/
title: Build an integration with an AI agent \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T11:13:36.195494+00:00
---

# Build an integration with an AI agent  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/build-integration-ai-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build an integration with an AI agent

This page shows you how to build an integration by prompting an AI coding agent. You describe what the integration should do, and the agent writes the integration, uploads and publishes it with the Application Integration REST API, runs it, and helps you troubleshoot it. As an example, you build a simple insurance claims-adjudication integration.

The agent gets its Application Integration knowledge from three public [agent skills](https://agentskills.io/home) in the [`google/skills`](https://github.com/google/skills) repository:

  * [`application-integration-basics`](https://github.com/google/skills/tree/main/skills/cloud/application-integration-basics): concepts, enabling APIs, provisioning a region, IAM roles and run-as service accounts, and limits.
  * [`application-integration-authoring`](https://github.com/google/skills/tree/main/skills/cloud/application-integration-authoring): writing integration versions as JSON, and uploading, publishing, and running them.
  * [`application-integration-troubleshooting`](https://github.com/google/skills/tree/main/skills/cloud/application-integration-troubleshooting): diagnosing failed, stuck, or silent runs.



For each skill's reference files, see [Application Integration agent skills](https://docs.cloud.google.com/application-integration/docs/agent-skills-overview).

## Before you begin

  1. Use a Google Cloud project where you can safely experiment, not a production project. Billing must be enabled for the project.
  2. [Set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration) in the project, in a [supported region](https://docs.cloud.google.com/application-integration/docs/locations). Setting up Application Integration needs its own roles, which are listed on that page.
  3. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) and sign in with `gcloud auth login`. The agent calls the REST API as you, with your gcloud credentials or, if it uses a client library, Application Default Credentials. If the agent uses a client library, it might ask you to run `gcloud auth application-default login`.
  4. Use an AI coding agent that supports agent skills.



### Required roles

After Application Integration is set up, you need the following roles to build and run integrations.

To get the permissions that you need to upload, publish, and run integrations and view their executions, ask your administrator to grant you the following IAM roles: 

  * [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) on your project
  * If the integration has a run-as service account: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the run-as service account 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For who needs Service Account User and how to grant it, see [Grant Service Account User for run-as service accounts](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access).

## Install the agent skills

In your terminal, run the following commands to install the three skills:
    
    
    npx skills add google/skills --skill application-integration-basics
    npx skills add google/skills --skill application-integration-authoring
    npx skills add google/skills --skill application-integration-troubleshooting
    

When prompted, choose the agents to configure and the installation scope. If your agent isn't listed, the default Universal option installs to `.agents/skills`. The installer might also offer other skills, such as `find-skills`; you don't need them for this page. Some agents load skills from a project folder only after you trust that folder. If `npx` isn't available, install [Node.js](https://nodejs.org/en/download), which includes it. To update the skills later, run `npx skills update`.

## Describe your integration

Start your agent in an empty working directory and describe the integration. Be specific about the trigger, the inputs and outputs, the rules, and where to deploy it. For example:
    
    
    Using the Application Integration skills, build an integration named
    claims-adjudication in project PROJECT_ID, region LOCATION.
    
    - Start it with an API trigger named adjudicate_claim.
    - Inputs: claimId (string), claimAmount (double), policyActive (boolean).
    - Outputs: decision (string) and reason (string).
    - Rules: if policyActive is false, return DENY. If claimAmount is 1000 or less,
      return APPROVE. Otherwise, return REVIEW. Set reason to a short explanation.
    - Save the integration version JSON in this directory so I can review it.
    - Show me every command before you run it, then upload, publish, and run it
      once with a sample claim.

Replace `PROJECT_ID` with your project ID and `LOCATION` with the region where you set up Application Integration.

## Review the plan and approve commands

The agent writes an integration version file, for example `claims-adjudication.json`. It contains the trigger (`triggerConfigs`), the tasks (`taskConfigs`), and the variables (`integrationParameters`). Read it before you continue, and ask the agent to explain anything you don't expect. For example, check whether the agent turned on Cloud Logging (`cloudLoggingDetails.enableCloudLogging`), which can add cost. To turn it off, set `enableCloudLogging` to `false` and remove `cloudLoggingSeverity`.

The skills tell the agent to run read-only checks freely, such as listing integrations or executions, but to show you the exact command or request and wait for your approval before it changes anything. That includes enabling APIs, changing IAM policies, and uploading, publishing, or running an integration. If the agent asks for approval without showing the exact command or request, ask it to show them. Your agent's own permission settings might also ask you to approve each command, including read-only ones. Check the project, region, and integration name in each command before you approve it.

## Upload, publish, and run the integration

After you approve, the agent makes the following Application Integration API calls:

  1. [`versions.upload`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/upload) uploads the JSON file as a new version of the integration.
  2. [`versions.publish`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/publish) publishes that version. A published version is `ACTIVE`, and any previously published version is unpublished.
  3. [`integrations.execute`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations/execute) runs the published integration synchronously through its API trigger.



You can also run the published integration yourself:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "triggerId": "api_trigger/adjudicate_claim",
          "inputParameters": {
            "claimId": {"stringValue": "CLM-1001"},
            "claimAmount": {"doubleValue": 2500},
            "policyActive": {"booleanValue": true}
          }
        }' \
        "https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/claims-adjudication:execute"
    

The response contains an `executionId` and the integration's output variables in `outputParameters`.

**Tip:** To route high-value claims to a person, ask the agent to add an [Approval task](https://docs.cloud.google.com/application-integration/docs/configure-approval-task). Approvers need the Application Integration Approver role (`roles/integrations.suspensionResolver`). If the integration has a run-as service account, also grant them Service Account User (`roles/iam.serviceAccountUser`) on it; this requirement takes effect as the rollout described in [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) proceeds. The rest of a run resumes asynchronously after an approval, so its result isn't returned to `integrations.execute`. After the request is approved or rejected, check the execution record for the outcome: `executionDetails.state`, and the variable values in `executionDetails.executionSnapshots`.

## Check the execution and troubleshoot

A successful response from `integrations.execute` doesn't always mean that every task did what you expected. A task's [retry strategy](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy#type) can let the run continue after the task fails: with **Ignore** , the integration treats the failed task as succeeded, and with **None** , the integration can still end as succeeded through an alternate path. Also, if a request sets `doNotPropagateError` to `true`, errors are returned in the response instead of as an error status. Ask the agent to check the execution, for example:
    
    
    Check execution EXECUTION_ID of claims-adjudication. Did every task
    succeed? If anything failed, tell me why and propose a fix.

The agent reads the execution record with the [`executions.list`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions/list) method, filtered by execution ID:
    
    
    curl -G \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data-urlencode 'filter=execution_id="EXECUTION_ID"' \
        "https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/claims-adjudication/executions"
    

The record shows the [execution state](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions#Execution.State), such as `SUCCEEDED`, `FAILED`, or `SUSPENDED`, and the state of each task. You can also open the [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) in the Google Cloud console. Cloud Logging is disabled for integrations by default; to use it, see [View integration logs in Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging).

Applying a fix means uploading and publishing a new version, so the skills tell the agent to ask for your approval again first. After you publish, the previous version can keep running for up to 10 minutes, so wait before you test the fix. Publishing also cancels the previous version's suspended runs, such as runs waiting for an approval.

## Best practices

  * **Start outside production.** Build and test in a non-production project, then promote the reviewed JSON file. See [Upload and download integrations](https://docs.cloud.google.com/application-integration/docs/upload-download-integrations).
  * **Use a dedicated run-as service account.** Use a dedicated, minimally scoped service account for each integration. See [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as).
  * **Keep secrets out of config variables.** Config variables are stored and exported in plain text. Use an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles) or the Secret Manager access task instead.
  * **Review the generated JSON.** Keep it in source control and review changes before you upload them. Authentication profiles aren't included in the file, so configure them in each project.



## Clean up

To remove the example integration, ask the agent:
    
    
    Unpublish claims-adjudication, then delete every version of it.

After you approve, the agent calls [`versions.unpublish`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/unpublish) on the published version and [`versions.delete`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/delete) on each version. When no versions are left, the integration no longer appears in your list of integrations. Deleting the integration itself needs a role such as Application Integration Admin; the Editor role can't.

## What's next

  * Read the skills on GitHub: [basics](https://github.com/google/skills/blob/main/skills/cloud/application-integration-basics/SKILL.md), [authoring](https://github.com/google/skills/blob/main/skills/cloud/application-integration-authoring/SKILL.md), and [troubleshooting](https://github.com/google/skills/blob/main/skills/cloud/application-integration-troubleshooting/SKILL.md).
  * Learn about [API triggers](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger).
  * Learn about [integration versions](https://docs.cloud.google.com/application-integration/docs/integration-versions).
  * [Build integrations with Gemini Code Assist](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini) in the Google Cloud console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
