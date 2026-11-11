---
url: https://docs.cloud.google.com/agent-registry/register-skills/
title: Register skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:51:16.683064+00:00
---

# Register skills  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/register-skills/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Register skills Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you package and manually register [standalone skills](https://docs.cloud.google.com/agent-registry/skills-architecture). Standalone skills bundle agent instructions with associated metadata assets and optional scripts to extend an agent's reasoning and workflow. By registering your own standalone skills in Agent Registry, you can centrally govern, version, and share reusable capabilities alongside the Google-managed skills that are available when you set up Agent Registry.

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. For a single-project setup, get [the project ID](https://support.google.com/googleapi/answer/7014113) of the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. If you configured a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) for multiple projects, use the ID of your management project for boundary-wide discovery and registration, or specify a member project ID for single-project operations.

  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).




If you want to configure customer-managed encryption keys (CMEK) for skills, you must [enable the Cloud Key Management Service API](https://docs.cloud.google.com/kms/docs/Quickstart), [create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) in the required Cloud KMS multi-region location, and [create a symmetric encryption key](https://docs.cloud.google.com/kms/docs/create-key) before configuring the `SkillEncryptionSpec` resource.

### Required roles

To get the permissions that you need to register skills in Agent Registry, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * Register and manage standalone skills: [Agent Registry User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.user) (`roles/agentregistry.user`) 
  * Register and manage standalone skills and other Agent Registry resources: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 
  * Configure CMEK for skills in a location: [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.admin) (`roles/agentregistry.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to register and manage skills and skill revisions. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

### Ingestion payload constraints

To register a skill, you must package the skill's source files into a ZIP archive. The archive must include a `SKILL.md` instruction file at its root. During the ingestion phase of the skill registration process, Agent Registry validates that the payload complies with the following constraints:

  * **ZIP archive size** : maximum compressed archive size of 1 MB.
  * **Total uncompressed payload size** : maximum uncompressed size of 10 MB when scanning is enabled.
  * **Individual file size** : maximum uncompressed size of 1 MB per file when scanning is enabled.
  * **Deep nesting** : maximum directory nesting depth of 8 levels.
  * **Specification compliance** : the `SKILL.md` file must contain a valid YAML front matter section defining the name, description, and metadata as defined in the [Agent Skills Specification](https://agentskills.io/specification).



When automated scanning is enabled using the `ENABLED_BLOCKING` or `ENABLED_NONBLOCKING` [scanning policy](https://docs.cloud.google.com/agent-registry/skills-architecture#scanning-policies), exceeding the maximum uncompressed size causes revision creation to fail with an `INVALID_ARGUMENT` error or transitions the revision's scan status to `UNSUPPORTED_FORMAT`. If scanning is disabled, Agent Registry bypasses these scanning-specific limits. To configure scanning policies and learn more about payload size constraints, see [Scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills).

## Configure CMEK for skills

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, Agent Registry encrypts skill revision payloads at rest using Google default encryption. Optionally, you can use CMEK to protect payloads before registering skills in Agent Registry.

To protect skill payloads in the `us` or `eu` locations with a customer-managed encryption key (CMEK) in Cloud KMS, configure the `SkillEncryptionSpec` resource for the target location. You must use a symmetric encryption key in the corresponding Cloud KMS multi-region location (`us` or `europe`).

Configure CMEK in a location before registering any skills there, and grant the Cloud KMS CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the key to your project's Agent Registry service agent.

For more information about CMEK architecture, location mappings, limitations, requirements, and Organization Policy Service enforcement, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/agent-registry/skills-architecture#cmek).

### Set or view the skill encryption specification

To configure or view the Cloud KMS key for skills in a location, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page:

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Skills** tab.

  4. In the action bar, click **Key management**.

  5. In the **Key management** panel, click **Add key** , or click edit **Edit** next to a configured location that has no existing skills.

  6. In the **Region** menu, select the skill location: `us` or `eu`.

  7. In the **Select a Cloud KMS key** field, select a key from the required Cloud KMS location. If prompted, grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the Agent Registry service agent.

  8. Click **Save**.




###  gcloud 

To set or update the Cloud KMS key for a skill location before any skills exist in that location, run the [`gcloud alpha agent-registry skill-encryption-spec update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skill-encryption-spec/update) command:
    
    
    gcloud alpha agent-registry skill-encryption-spec update \
        --project=PROJECT_ID \
        --location=SKILL_LOCATION \
        --kms-key=projects/KMS_PROJECT_ID/locations/KMS_LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
    

To view the current skill encryption specification for a location, run the [`gcloud alpha agent-registry skill-encryption-spec describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skill-encryption-spec/describe) command:
    
    
    gcloud alpha agent-registry skill-encryption-spec describe \
        --project=PROJECT_ID \
        --location=SKILL_LOCATION
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud governance project ID.
  * `SKILL_LOCATION`: the skill location: `us` or `eu`.
  * `KMS_PROJECT_ID`: the ID of the project that hosts your Cloud KMS key ring.
  * `KMS_LOCATION`: the Cloud KMS key location corresponding to your skill location, for example, `europe`.
  * `KEY_RING`: the name of your Cloud KMS key ring.
  * `KEY_NAME`: the name of your Cloud KMS symmetric encryption key.



###  REST 

To set or update the `SkillEncryptionSpec` resource for a location, send a `PATCH` request:
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "cryptoKeyName": "projects/KMS_PROJECT_ID/locations/KMS_LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
        }' \
        "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/SKILL_LOCATION/skillEncryptionSpec?updateMask=cryptoKeyName"
    

This request returns a long-running operation (`Operation`) resource.

To retrieve the current `SkillEncryptionSpec` resource for a location, send a `GET` request:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/SKILL_LOCATION/skillEncryptionSpec"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud governance project ID.
  * `SKILL_LOCATION`: the skill location: `us` or `eu`.
  * `KMS_PROJECT_ID`: the ID of the project that hosts your Cloud KMS key ring.
  * `KMS_LOCATION`: the Cloud KMS key location corresponding to your skill location, for example, `europe`.
  * `KEY_RING`: the name of your Cloud KMS key ring.
  * `KEY_NAME`: the name of your Cloud KMS symmetric encryption key.



## Register a skill

You can manually register your own skills in Agent Registry. For information about pricing and feature costs for skills, see [Agent Registry pricing](https://docs.cloud.google.com/agent-registry/pricing).

To register your skills, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page:

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select your Google Cloud project.

  3. Select the **Skills** tab.

  4. In the **Skills** tab, the **Add skill** button displays two options to create a skill container and import your initial skills package. Choose one of the following:

     * **Add skill** : create a new skill container in the registry. You can optionally upload a skill package to create the first revision.
     * **Import skill** : register a new custom skills package by uploading a ZIP bundle containing your `SKILL.md` instructions file and optional scripts, or a standalone `SKILL.md` file.
  5. In the **Create skill** or **Import skill** panel, specify the following details:

     * **Display name** : enter a user-friendly name for the skill.
     * **Description** : enter a brief summary explaining the skill capabilities.
     * **Location** : select the geographic region, for example, `global`, `us`, or `eu`.
  6. In the **Payload source** section, choose one of the following:

     * **File** : upload your packaged skill ZIP archive or a standalone `SKILL.md` file in the **Upload package or file** field. The maximum upload size is 1 MB. You can browse the file from your local directory.
     * **GCS bucket** : enter the path to your ZIP archive stored in a Cloud Storage bucket in the **Cloud Storage URI** field. The maximum upload size is 1 MB. The path must be in the format `gs://BUCKET_NAME/SKILL_PACKAGE.zip`.

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, such as when you have never created a skill, trigger its creation for the Agent Registry API. For instructions, see [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting Identity and Access Management (IAM) permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).
  7. Click **Create**.

Your skill is created in the **Disabled** (`DISABLED`) state. For all subsequent skill operations, refer to your skill as `private-SKILL_ID`, as displayed in the Google Cloud console.

  8. To make the skill available for agent discovery, set its [default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) and update the [target state](https://docs.cloud.google.com/agent-registry/skills-architecture#lifecycle) to **Active**. For instructions, see [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).




###  gcloud 

  1. Create the skill container and upload its initial revision payload with the [`gcloud agent-registry skills create`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/create) command. You can upload either a local ZIP file or import a package stored in Cloud Storage:

     * **Upload a local ZIP file** : to register a skill using a local ZIP payload:
           
           gcloud agent-registry skills create SKILL_ID \
               --project=PROJECT_ID \
               --location=LOCATION \
               --display-name="DISPLAY_NAME" \
               --description="DESCRIPTION" \
               --target-state=disabled \
               --payload="LOCAL_ZIP_PATH"
           

Replace `LOCAL_ZIP_PATH` with the path to your packaged skill archive on your local machine, for example, `./workspace-docs-skill.zip`.

     * **Import from a Cloud Storage bucket** : to register a skill using a ZIP archive hosted in a Cloud Storage bucket:
           
           gcloud agent-registry skills create SKILL_ID \
               --project=PROJECT_ID \
               --location=LOCATION \
               --display-name="DISPLAY_NAME" \
               --description="DESCRIPTION" \
               --target-state=disabled \
               --gcs-source-uri="gs://BUCKET_NAME/SKILL_PACKAGE.zip"
           

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, such as when you have never created a skill, trigger its creation for the Agent Registry API. For instructions, see [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting IAM permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

Replace the following:

       * `BUCKET_NAME`: the Cloud Storage bucket name that contains the ZIP bundle.
       * `SKILL_PACKAGE`: the name of the skill package containing the skill payload.

Replace the following in either command:

     * `SKILL_ID`: the resource ID of the skill, for example, `workspace-docs-skill`. After creation, the registry automatically prepends the `private-` prefix. You must use the prefixed ID in all subsequent skill commands, for example, `private-workspace-docs-skill`.
     * `PROJECT_ID`: the project ID.
     * `LOCATION`: the geographic region, for example, `global`, `us`, or `eu`.
     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
  2. When you create a skill without an initial revision, you can only set the [target state](https://docs.cloud.google.com/agent-registry/skills-architecture#lifecycle) (`--target-state`) to `draft` or `disabled`.

When you create a skill with an initial revision, such as with `--gcs-source-uri` or `--payload`, Agent Registry sets the initial revision as the skill's [default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill). You can set the target state to one of the following values, depending on the [scanning policy](https://docs.cloud.google.com/agent-registry/skills-architecture#scanning-policies):

     * If `--target-state=active` and the scanning policy is `disabled` or `enabled-nonblocking`, the skill transitions to the **Active** (`STATE_ACTIVE`) state when the creation operation completes.
     * If `--target-state=active` and the scanning policy is `enabled-blocking` (default), the skill enters the **Draft** (`STATE_DRAFT`) state when the creation operation completes. In the background, when the security scan completes, the parent skill transitions to **Active** (`STATE_ACTIVE`) only if the scan produces no findings and the parent skill is in the **Draft** state with the default revision still pointing to the initial revision.
     * If `--target-state=disabled` or `--target-state=draft`, you can later make it available for agent discovery by setting a valid default revision and updating the target state to **Active**. For instructions, see [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).



###  REST 

  1. Create the skill container with an initial revision inline:

#### HTTP method and URL
         
         POST https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills?skillId=SKILL_ID
         

Replace the following:

     * `PROJECT_ID`: the project ID.
     * `LOCATION`: the registry location.
     * `SKILL_ID`: a unique identifier for the skill container.

#### Request JSON body (local file upload)

To create a skill by uploading local ZIP archive bytes directly, use the `archiveUploadSource` payload in the initial revision (`initialRevision`). When you provide an initial revision, Agent Registry sets that revision as the skill's [default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill). You can set the [target state](https://docs.cloud.google.com/agent-registry/skills-architecture#lifecycle) to `TARGET_STATE_DRAFT`, `TARGET_STATE_DISABLED`, or `TARGET_STATE_ACTIVE`. Without an initial revision, only `TARGET_STATE_DRAFT` and `TARGET_STATE_DISABLED` are supported as target states:
    
    {
      "displayName": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "type": "SIMPLE",
      "targetState": "TARGET_STATE_DISABLED",
      "initialRevision": {
        "archiveUploadSource": {
          "archiveContent": "BASE64_ZIP_BYTES"
        }
      }
    }
    

Replace the following:

     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
     * `BASE64_ZIP_BYTES`: the base64-encoded string representation of your local ZIP archive.

#### Request JSON body (import from Cloud Storage)

Alternatively, to create a skill using an archive stored in a Cloud Storage bucket, use `gcsSource`:
    
    {
      "displayName": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "type": "SIMPLE",
      "targetState": "TARGET_STATE_DISABLED",
      "initialRevision": {
        "gcsSource": {
          "uri": "gs://BUCKET_NAME/SKILL_PACKAGE.zip"
        }
      }
    }
    

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, such as when you have never created a skill, trigger its creation for the Agent Registry API. For instructions, see [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting IAM permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

Replace the following:

     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
     * `BUCKET_NAME`: the Cloud Storage bucket name that contains the ZIP bundle.
     * `SKILL_PACKAGE`: the name of the skill package containing the skill payload.

#### `curl` command (local file upload)
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "displayName": "DISPLAY_NAME",
          "description": "DESCRIPTION",
          "type": "SIMPLE",
          "targetState": "TARGET_STATE_DISABLED",
          "initialRevision": {
            "archiveUploadSource": {
              "archiveContent": "'"$(base64 -w0 local_skill.zip)"'"
            }
          }
        }' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills?skillId=SKILL_ID"
    

Replace the following:

     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
     * `PROJECT_ID`: the project ID.
     * `LOCATION`: the registry location.
     * `SKILL_ID`: a unique identifier for the skill container.

For a Cloud Storage bucket file upload, replace the request JSON body with the corresponding fields and values.

  2. When you create a skill with an initial revision, Agent Registry sets the initial revision as the parent skill's [default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) and transitions the skill's state based on the [target state](https://docs.cloud.google.com/agent-registry/skills-architecture#lifecycle) and [scanning policy](https://docs.cloud.google.com/agent-registry/skills-architecture#scanning-policies):

     * If the target state is `TARGET_STATE_ACTIVE` and the scanning policy is `DISABLED` or `ENABLED_NONBLOCKING`, the skill enters the `STATE_ACTIVE` state when the long-running operation (LRO) completes.
     * If the target state is `TARGET_STATE_ACTIVE` and the scanning policy is `ENABLED_BLOCKING` (default), the skill enters the `STATE_DRAFT` state when the LRO completes. In the background, when the security scan completes, the parent skill transitions to `STATE_ACTIVE` only if the scan produces no findings and the parent skill is still in `STATE_DRAFT` with the default revision still pointing to the initial revision.
     * If the target state is `TARGET_STATE_DISABLED` or `TARGET_STATE_DRAFT`, the skill starts in `STATE_DISABLED` or `STATE_DRAFT`. To make the skill available for agent discovery later, you must set the default revision and update the target state to `TARGET_STATE_ACTIVE`. For instructions, see [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).



The skills that you or other users create are automatically assigned to the default `private` publisher to avoid name collisions with Google-managed skills. For that reason, the published ID of a particular skill becomes `private-SKILL_ID`. You can't specify a custom publisher during skill creation.

For example, if you create a skill with the ID `workspace-tools`, the [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) is created as `projects/PROJECT_NUMBER/locations/LOCATION/skills/private-workspace-tools`. The [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) is assigned as `urn:skill:projects-PROJECT_NUMBER:locations:LOCATION:private-workspace-tools`. You must use the `private-workspace-tools` published ID for all subsequent skill operations.

When you create a skill, Agent Registry automatically configures a resource-level IAM allow policy on the new `Skill` resource:

  * Your principal is granted the Agent Registry API Admin (`roles/agentregistry.admin`) role on the skill.
  * If the project belongs to an organization, the principal set representing your agent workloads in the project is granted the Agent Registry API Viewer (`roles/agentregistry.viewer`) role on the skill.



To share a skill with other users, groups, service accounts, or agent workloads, see [Manage access to a skill](https://docs.cloud.google.com/agent-registry/manage-skills#manage-skill-access).

## What's next

  * Learn how to [manage your registered skills](https://docs.cloud.google.com/agent-registry/manage-skills).
  * Learn how to [add and manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * Learn how to [scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills).
  * Review [verified publisher details](https://docs.cloud.google.com/agent-registry/review-publishers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
