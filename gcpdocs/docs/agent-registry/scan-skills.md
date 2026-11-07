---
url: https://docs.cloud.google.com/agent-registry/scan-skills/
title: Scan skills for security issues \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:40:13.558080+00:00
---

# Scan skills for security issues  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/scan-skills/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Scan skills for security issues Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you configure automated security scanning for [standalone skills](https://docs.cloud.google.com/agent-registry/skills-architecture), enforce [scanning policies](https://docs.cloud.google.com/agent-registry/skills-architecture#scanning-policies) across your organization using Organization Policy Service, and triage security findings so that you can prevent compromised skills from reaching your agents.

When you upload a [skill revision](https://docs.cloud.google.com/agent-registry/skills-architecture#skill-revision), Agent Registry scans the `SKILL.md` instruction file, optional scripts, and supporting assets for security risks such as unauthorized data exfiltration, exposed credentials, and prompt injection.

Skill security scanning uses large language models (LLMs) to evaluate instructions, code logic, and semantic intent. Because LLM analysis is probabilistic, scans might produce false positives or false negatives, and results might vary across runs. Additionally, details about findings might be approximate and subject to hallucination. Developers must review and verify scan findings before applying remediation changes.

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. For a single-project setup, get [the project ID](https://support.google.com/googleapi/answer/7014113) of the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. If you configured a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) for multiple projects, use the ID of your management project for boundary-wide discovery and registration, or specify a member project ID for single-project operations.

  3. [Register a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills) in Agent Registry.

  4. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).




### Required roles

To get the permissions that you need to configure scanning and triage findings in Agent Registry, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * Configure skill scanning: [Agent Registry User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.user) (`roles/agentregistry.user`) 
  * View skills and skill revisions: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * View and list security findings: [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.admin) (`roles/agentregistry.admin`) 
  * Enforce scanning policies at the organization or folder level: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to configure scanning and view skills. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

### Uncompressed payload size constraints

To ensure optimal performance and accommodate processing token limits for underlying LLM scanners, Agent Registry enforces strict uncompressed size limits when scanning is active:

  * **Total uncompressed skill size** : maximum of 10 MB for the extracted archive.
  * **Per-file uncompressed size** : maximum of 1 MB for any individual file within the skill package.



If a skill has scanning enabled and exceeds these limits, creating a skill revision fails with an `INVALID_ARGUMENT` error or the revision's scan status resolves to `UNSUPPORTED_FORMAT`.

If scanning is explicitly disabled, Agent Registry bypasses these scanning-specific size bounds, but general system limits still apply. For more information about system limits, see [Quotas and system limits](https://docs.cloud.google.com/agent-registry/quotas).

## Configure a scanning policy for a skill

By default, skills use the **Enabled (Blocking)** (`ENABLED_BLOCKING`) [scanning policy](https://docs.cloud.google.com/agent-registry/skills-architecture#scanning-policies), which automatically scans uploaded skill revisions for security risks such as unauthorized data exfiltration, exposed credentials, and prompt injection. Detected issues are exposed as read-only `Finding` resources in your governance project: `projects/PROJECT_NUMBER/locations/LOCATION/findings/FINDING_ID`.

With **Enabled (Blocking)** , Agent Registry blocks downloading revisions with security findings and prevents promoting revisions with findings or pending scans as the skill's [default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).

You can also configure scanning policies for non-blocking audit mode (`ENABLED_NONBLOCKING`) or disable scanning (`DISABLED`). For more information about supported scanning policies, see [Scanning policies](https://docs.cloud.google.com/agent-registry/skills-architecture#scanning-policies).

### Set or update skill scan settings

Enabling or updating scanning on an existing skill applies _only_ to skill revisions created after the configuration change. Scanning isn't retroactively triggered for revisions that were already created. To scan skill contents uploaded when scanning was disabled, you must [create a new skill revision](https://docs.cloud.google.com/agent-registry/manage-skill-revisions#create-revision).

To configure scanning settings when creating or updating a skill, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page:

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.

  3. Click **Add skill** or select an existing skill and click edit **Edit**.

  4. In the **Security scanning** section, select the scanning policy you want.

  5. Click **Save** or **Create**.




###  gcloud 

  * **Create a skill with scanning enabled (blocking)** : run the [`gcloud agent-registry skills create`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/create) command with the `--scanning-policy` flag set to `enabled-blocking`. For example, if you [register a skill](https://docs.cloud.google.com/agent-registry/register-skills#register-skill) using a ZIP archive from a Cloud Storage bucket:
        
        gcloud agent-registry skills create SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --target-state=disabled \
            --scanning-policy=enabled-blocking \
            --gcs-source-uri="gs://BUCKET_NAME/SKILL_PACKAGE.zip"
        

  * **Create a skill with scanning enabled (non-blocking)** : run the [`gcloud agent-registry skills create`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/create) command with the `--scanning-policy` flag set to `enabled-nonblocking`. For example, if you [register a skill](https://docs.cloud.google.com/agent-registry/register-skills#register-skill) using a ZIP archive from a Cloud Storage bucket:
        
        gcloud agent-registry skills create SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --target-state=disabled \
            --scanning-policy=enabled-nonblocking \
            --gcs-source-uri="gs://BUCKET_NAME/SKILL_PACKAGE.zip"
        

  * **Update scanning policy on an existing skill** : run the [`gcloud agent-registry skills update`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/update) command with the `--scanning-policy` flag set to the selected policy, for example `enabled-nonblocking`:
        
        gcloud agent-registry skills update SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --scanning-policy=enabled-nonblocking
        

  * **Disable scanning on a skill** : run the [`gcloud agent-registry skills update`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/update) command with the `--scanning-policy` flag set to `disabled`:
        
        gcloud agent-registry skills update SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --scanning-policy=disabled
        

  * **Describe scan configuration on an existing skill** : run the [`gcloud agent-registry skills describe`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/describe) command with the `--format` flag set to `value(scanningConfig.policy)`:
        
        gcloud agent-registry skills describe SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --format="value(scanningConfig.policy)"
        




Replace the following:

  * `SKILL_ID`: the ID of the skill. When updating or describing an existing manually registered skill, include the `private-` prefix, such as `private-my-skill`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `BUCKET_NAME`: the Cloud Storage bucket name that contains the ZIP bundle. Before importing from a bucket, ensure that the Agent Registry service agent has the `storage.objects.get` permission on the bucket. For more information, see [Register a skill](https://docs.cloud.google.com/agent-registry/register-skills#register-skill).
  * `SKILL_PACKAGE`: the name of the skill package containing the skill payload.



###  REST 

To configure scanning using the REST API, include the `scanningConfig` object in your request body:
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
            "scanningConfig": {
              "policy": "ENABLED_BLOCKING"
            }
          }' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID?updateMask=scanningConfig"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `SKILL_ID`: the ID of the skill. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.



## Enforce scanning using Organization Policy Service

You can enforce organization-wide scanning policies by defining a custom Organization Policy Service constraint on the `Skill` resource that evaluates the scanning policy, with optional Resource Manager tag exemptions.

For information about organization policy enforcement in Agent Registry, capabilities, and limitations, see [Organization policy enforcement](https://docs.cloud.google.com/agent-registry/skills-architecture#org-policy).

### Define the custom constraint

Create a YAML file named `skills-scan-constraint.yaml` with the following specification:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.skillsScanningEnforcement
    resourceTypes:
    - agentregistry.googleapis.com/Skill
    methodTypes:
    - CREATE
    - UPDATE
    condition: resource.scanningConfig.policy == "DISABLED"
    actionType: DENY
    displayName: Prevent Disabling Skills Scanning
    description: Prevents creating or updating skills with scanning disabled.
    

Replace `ORGANIZATION_ID` with your numerical organization ID.

To require blocking mode across all skills and prevent both `DISABLED` and `ENABLED_NONBLOCKING` scanning policies, you can alternatively set `condition: resource.scanningConfig.policy == "ENABLED_BLOCKING"` and `actionType: ALLOW`.

### Set the custom constraint

Upload and register the custom constraint in your organization with the [`gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command:
    
    
    gcloud org-policies set-custom-constraint skills-scan-constraint.yaml
    

### Apply the policy with conditional exemptions

Create a policy definition file named `skills-scan-policy.yaml` that enforces the constraint across all standard projects while, for example, exempting testing projects that you tagged with `exempt-scanning-enforcement: true`:
    
    
    name: organizations/ORGANIZATION_ID/policies/custom.skillsScanningEnforcement
    spec:
      rules:
      # Enforce scanning on all standard projects
      - enforce: true
        condition:
          expression: "!resource.matchTag('ORGANIZATION_ID/exempt-scanning-enforcement', 'true')"
          title: "Enforce Scanning"
          description: "Enforce scanning on all non-exempt projects"
      # Bypass enforcement for tagged projects
      - enforce: false
        condition:
          expression: "resource.matchTag('ORGANIZATION_ID/exempt-scanning-enforcement', 'true')"
          title: "Exempt Testing Projects"
          description: "Allow scanning to be disabled for testing projects"
    

Replace `ORGANIZATION_ID` with your numerical organization ID.

Apply the policy to your organization with the [`gcloud org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command:
    
    
    gcloud org-policies set-policy skills-scan-policy.yaml
    

### Verify policy

Verify that the policy is active on a project with the [`gcloud org-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe) command:
    
    
    gcloud org-policies describe custom.skillsScanningEnforcement \
        --project=PROJECT_ID \
        --effective
    

Replace `PROJECT_ID` with your project ID.

## Review scan results and revision status

When you publish a skill revision, the scanner runs asynchronously in the background. To inspect the revision metadata and verify the scan outcome, run the [`gcloud agent-registry skills revisions describe`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/revisions/describe) command:
    
    
    gcloud agent-registry skills revisions describe REVISION_ID \
        --skill=SKILL_ID \
        --project=PROJECT_ID \
        --location=LOCATION
    

Replace the following:

  * `REVISION_ID`: the ID of the skill revision.
  * `SKILL_ID`: the ID of the skill container. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.



The output contains the `scanResult` block that looks like the following example:
    
    
    name: projects/my-project/locations/us-central1/skills/private-my-skill/revisions/rev-v1
    createTime: '2026-08-10T09:15:00.000000Z'
    state: ACTIVE
    scanResult:
      scanState: SUCCEEDED
      scanTime: '2026-08-10T09:16:22.000000Z'
      findings:
      - projects/my-project/locations/us-central1/findings/b9a8c7d6-e5f4-4321-89ab-cdef01234567
    

Possible values for `scanResult.scanState` are:

  * **`SUCCEEDED`** : the scan completed execution. If security issues are detected, their resource names are listed in the `scanResult.findings` array. If no issues are detected, `scanResult.findings` is empty.
  * **`RUNNING`** : the scan is actively executing.
  * **`DISABLED`** : scanning is bypassed because the skill's scanning policy is set to `DISABLED` at the time the skill revision is created.
  * **`UNSUPPORTED_FORMAT`** : the uploaded archive can't be analyzed by the scanner, for example, because its uncompressed size exceeded the scanning limits or its archive format is unsupported. Details are provided in `scanResult.errorMessage`.
  * **`FAILED`** : the scan can't complete due to an internal error. Details are provided in `scanResult.errorMessage`.



A revision's scan status reflects the scanning configuration active at the time the revision was created. Enabling or updating scanning on a skill applies only to revisions created after the change and doesn't retroactively trigger a scan for existing revisions. To scan skill contents uploaded when scanning was disabled, you must [create a new skill revision](https://docs.cloud.google.com/agent-registry/manage-skill-revisions#create-revision).

## Triage security findings

When a scan detects security issues, detailed telemetry is published to Agent Registry as `Finding` resources scoped to your project and location. Viewing findings requires the Agent Registry API Admin (`roles/agentregistry.admin`) role.

  * **List all findings for a skill revision** : run the [`gcloud agent-registry findings list`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/findings/list) command:
        
        gcloud agent-registry findings list \
            --project=PROJECT_ID \
            --location=LOCATION \
            --filter="resource=\"projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID\""
        

Replace the following:

    * `PROJECT_ID`: the project ID.
    * `LOCATION`: the registry location.
    * `SKILL_ID`: the ID of the skill container, such as `private-my-skill`.
    * `REVISION_ID`: the ID of the skill revision.

The output is similar to the following:
    
    NAME                                                                                  SEVERITY           FINDING_CLASS  CREATE_TIME
    projects/my-project/locations/us-central1/findings/FINDING_ID  SEVERITY_CRITICAL  VULNERABILITY  2026-08-10T09:16:22.104Z
    

  * **Describe finding details** : run the [`gcloud agent-registry findings describe`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/findings/describe) command:
        
        gcloud agent-registry findings describe FINDING_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --format=json
        

Replace the following:

    * `FINDING_ID`: the ID of the `Finding` resource.
    * `PROJECT_ID`: the project ID.
    * `LOCATION`: the registry location.

Sample finding output:
    
    {
      "name": "projects/my-project/locations/us-central1/findings/FINDING_ID",
      "uid": "FINDING_ID",
      "createTime": "2026-08-10T09:16:22.104Z",
      "updateTime": "2026-08-10T09:16:22.104Z",
      "resource": "projects/my-project/locations/us-central1/skills/private-my-skill/revisions/rev-v1",
      "severity": "SEVERITY_CRITICAL",
      "findingClass": "VULNERABILITY",
      "files": [
        {
          "path": "resources/helper.py",
          "lineNumber": "12"
        }
      ],
      "detail": "Involves unauthorized outbound network requests transmitting sensitive local files or environment variables. Detected inside resources/helper.py at line 12."
    }
    

Each `Finding` resource includes the following key fields:

    * `resource`: the full [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) of the skill revision associated with the finding.
    * `severity`: the severity level. Allowed values are: 
      * `SEVERITY_CRITICAL`
      * `SEVERITY_HIGH`
      * `SEVERITY_MEDIUM`
      * `SEVERITY_LOW`
      * `SEVERITY_UNSPECIFIED`
    * `findingClass`: the type of finding: 
      * `VULNERABILITY`: a software or instruction weakness.
      * `SECRET`: exposed plaintext credentials, keys, or tokens.
    * `files`: the list of affected files in the skill archive, including the relative `path` and `lineNumber`. A value of `0` indicates that the finding applies to the entire file.
    * `detail`: a detailed explanation of the detected security issue.



## Remediate findings and update skills

To resolve security findings on a skill, follow these steps:

  1. Review the `detail` field of the finding and inspect the offending file `path` and `lineNumber` in the `files` array. Because automated scanning uses LLMs to inspect semantic code and instructions, verify the reported line numbers and findings before modifying your files.
  2. Update your source files in your local development environment to resolve the finding. For example, remove unauthorized network calls, remove exposed credentials, or eliminate prompt injection patterns.
  3. Package the updated files into a new ZIP archive.
  4. [Create a new skill revision](https://docs.cloud.google.com/agent-registry/manage-skill-revisions#create-revision).
  5. Verify that the new revision's `scanResult.scanState` resolves to `SUCCEEDED` with no findings listed.
  6. [Update the default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) of the skill to point to the verified revision.



## What's next

  * Learn about [skills architecture](https://docs.cloud.google.com/agent-registry/skills-architecture).
  * Learn how to [register skills](https://docs.cloud.google.com/agent-registry/register-skills).
  * Learn how to [manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * Review [quotas and system limits](https://docs.cloud.google.com/agent-registry/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
