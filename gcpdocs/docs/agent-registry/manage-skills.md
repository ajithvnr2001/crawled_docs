---
url: https://docs.cloud.google.com/agent-registry/manage-skills/
title: Manage skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:29:38.902621+00:00
---

# Manage skills  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manage-skills/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Manage skills Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you inspect, update, and govern standalone skills so that you can control which skill versions and lifecycle states are available to your agents. After you [register a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills), you can view its details, update its description or default revision, transition its lifecycle state, manage resource-level access policies, or delete it from Agent Registry. You can also list and view Google-managed skills, which are available as soon as you set up Agent Registry.

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. For a single-project setup, get [the project ID](https://support.google.com/googleapi/answer/7014113) of the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. If you configured a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) for multiple projects, use the ID of your management project for boundary-wide discovery and registration, or specify a member project ID for single-project operations.

  3. [Register a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills).

  4. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).




### Required roles

To get the permissions that you need to manage skills in Agent Registry, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * List and view skills: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * Update, transition lifecycle states, and delete skills: [Agent Registry User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.user) (`roles/agentregistry.user`) 
  * Manage skills and other Agent Registry resources: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 
  * Manage Identity and Access Management (IAM) policies on skills: [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.admin) (`roles/agentregistry.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to view, update, and delete skills. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

## List and view skills

You can browse all registered skills or search for specific capabilities:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click any skill name to open its **Skill Details** page, which displays the name, description, active version, [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers), last updated, custom metadata, and revision history.



###  gcloud 

To list all skills in a location, use the [`gcloud agent-registry skills list`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/list) command:
    
    
    gcloud agent-registry skills list \
        --project=PROJECT_ID \
        --location=LOCATION
    

To view details of a specific skill, use the [`gcloud agent-registry skills describe`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/describe) command:
    
    
    gcloud agent-registry skills describe SKILL_ID \
        --project=PROJECT_ID \
        --location=LOCATION
    

Replace the following:

  * `SKILL_ID`: the ID of the skill you want to review. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.



###  REST 

To retrieve the list of all skills, send a `GET` request:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills"
    

To retrieve a single skill container, send a `GET` request:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `SKILL_ID`: the ID of the skill you want to review. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.



## Update skill metadata or default revision

You can modify a skill's display name, description, scanning configuration, or manually change the default revision pointer to deploy a different version.

If your skill is configured with the `ENABLED_BLOCKING` [scanning policy](https://docs.cloud.google.com/agent-registry/skills-architecture#scanning-policies), attempting to set the default revision to a revision that has security findings or pending scan results fails with a `FAILED_PRECONDITION` error. Similarly, you can't update a skill's scanning policy to `ENABLED_BLOCKING` if its current default revision has security findings or pending scan results. Enabling or updating scanning on a skill applies only to revisions created after that change and doesn't retroactively scan existing revisions. For more information, see [Scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills). To create new skill revisions, see [Manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).

To update skill metadata or the default revision of a particular skill, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click any skill name to open its **Skill Details** page, which displays the name, description, active version, [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers), last updated, custom metadata, and revision history.
  5. Choose between the following options:

     * **Update skill metadata** :

       1. Click edit **Edit**.
       2. In the **Edit skill** panel, update the display name or description of your skill.
       3. Click **Save**.
     * **Update the default revision** :

       1. Locate the **Version history** table.
       2. Find the revision you want to set as active.
       3. In the **Actions** column, click **Activate version**.



###  gcloud 

  * To update a skill's metadata, use the [`gcloud agent-registry skills update`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/update) command:
        
        gcloud agent-registry skills update SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --display-name="DISPLAY_NAME" \
            --description="DESCRIPTION"
        

  * To update a skill's default serving revision, use the [`gcloud agent-registry skills update`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/update) command and specify the target revision's [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names):
        
        gcloud agent-registry skills update SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --default-revision="projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID"
        




Replace the following:

  * `SKILL_ID`: the ID of the skill you want to update. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `DISPLAY_NAME`: the updated display name.
  * `DESCRIPTION`: the updated description.
  * `REVISION_ID`: the ID of the skill revision you want to set as default.



###  REST 

Send a `PATCH` request specifying the fields you want to update:
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
            "displayName": "DISPLAY_NAME",
            "description": "DESCRIPTION",
            "defaultRevision": "projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID"
          }' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID?updateMask=displayName,description,defaultRevision"
    

Replace the following:

  * `DISPLAY_NAME`: the updated display name of the skill.
  * `DESCRIPTION`: the updated description of the skill.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `SKILL_ID`: the ID of the skill you want to update. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.
  * `REVISION_ID`: the ID of the skill revision you want to activate.



## Manage skill lifecycle states

To control how a skill is served at runtime, you can change the skill's [target state](https://docs.cloud.google.com/agent-registry/skills-architecture#lifecycle) for lifecycle transitions.

To transition a skill's lifecycle state:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click any skill name to open its **Skill Details** page, which displays the name, description, active version, [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers), last updated, custom metadata, and revision history.
  5. Use the status control buttons to transition the target state. The buttons that the page displays depend on the current state of the skill, for example, **Enable** , **Disable** , **Deprecate** , or **Decommission**.



###  gcloud 

Update the skill container with the [`gcloud agent-registry skills update`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/update) command and the `--target-state` flag:
    
    
    gcloud agent-registry skills update SKILL_ID \
        --project=PROJECT_ID \
        --location=LOCATION \
        --target-state=DISABLED
    

Replace the following:

  * `SKILL_ID`: the ID of the skill you want to update. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.



Allowed values for the target state are:

  * `DRAFT`
  * `ACTIVE`
  * `DISABLED`
  * `DEPRECATED`
  * `DECOMMISSIONED`



###  REST 

Send a `PATCH` request specifying the `targetState` in the body and in the update mask:
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "targetState": "TARGET_STATE_DISABLED"
        }' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID?updateMask=targetState"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `SKILL_ID`: the ID of the skill you want to update. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.



Allowed values for the target state are:

  * `TARGET_STATE_DRAFT`
  * `TARGET_STATE_ACTIVE`
  * `TARGET_STATE_DISABLED`
  * `TARGET_STATE_DEPRECATED`
  * `TARGET_STATE_DECOMMISSIONED`



## Manage access to a skill

When you [register a skill](https://docs.cloud.google.com/agent-registry/register-skills), Agent Registry automatically configures a resource-level IAM allow policy on the `Skill` resource that grants your principal the Agent Registry API Admin (`roles/agentregistry.admin`) role. If your project belongs to an organization, Agent Registry also grants the Agent Registry API Viewer (`roles/agentregistry.viewer`) role to your agent workloads in the project.

To share a skill with other users, groups, service accounts, or agent identities without granting project-wide access, you can manage the resource-level IAM policy on the `Skill` resource. For example, you can grant the Agent Registry API Viewer role so a principal can view, search, and download the skill, or the Agent Registry API Editor role so a principal can update the skill and upload new revisions. You can also configure [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) on project-level IAM bindings to restrict access to specific `Skill` and `SkillRevision` resources.

To view or update the IAM policy on a skill, do the following:

###  gcloud 

  * To view the current IAM policy on a skill, run the [`gcloud agent-registry skills get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/get-iam-policy) command:
        
        gcloud agent-registry skills get-iam-policy SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION
        

  * To grant a role on a skill to a principal, run the [`gcloud agent-registry skills add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/add-iam-policy-binding) command:
        
        gcloud agent-registry skills add-iam-policy-binding SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --member="PRINCIPAL" \
            --role="ROLE"
        

  * To revoke a role on a skill from a principal, run the [`gcloud agent-registry skills remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/remove-iam-policy-binding) command:
        
        gcloud agent-registry skills remove-iam-policy-binding SKILL_ID \
            --project=PROJECT_ID \
            --location=LOCATION \
            --member="PRINCIPAL" \
            --role="ROLE"
        

  * To replace the IAM policy on a skill using a local JSON or YAML policy file, run the [`gcloud agent-registry skills set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/set-iam-policy) command:
        
        gcloud agent-registry skills set-iam-policy SKILL_ID POLICY_FILE \
            --project=PROJECT_ID \
            --location=LOCATION
        




Replace the following:

  * `SKILL_ID`: the ID of the skill, including the `private-` prefix, such as `private-my-skill`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `PRINCIPAL`: the principal identifier, such as `user:user@example.com` or `serviceAccount:my-sa@example-project.iam.gserviceaccount.com`.
  * `ROLE`: the Agent Registry role to grant or revoke, such as `roles/agentregistry.viewer` or `roles/agentregistry.editor`.
  * `POLICY_FILE`: the path to a JSON or YAML file containing the IAM policy definition.



###  REST 

  * To retrieve the current IAM policy on a skill, send a `GET` request to the [`skills:getIamPolicy`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.skills/getIamPolicy) endpoint:
        
        curl -X GET \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID:getIamPolicy"
        

  * To update the IAM policy on a skill, send a `POST` request to the [`skills:setIamPolicy`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.skills/setIamPolicy) endpoint, including the `etag` from the existing policy:
        
        curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -d '{
              "policy": {
                "bindings": [
                  {
                    "role": "ROLE",
                    "members": [
                      "PRINCIPAL"
                    ]
                  }
                ],
                "etag": "ETAG"
              }
            }' \
            "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID:setIamPolicy"
        




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `SKILL_ID`: the ID of the skill, including the `private-` prefix, such as `private-my-skill`.
  * `ROLE`: the Agent Registry role to grant, such as `roles/agentregistry.viewer` or `roles/agentregistry.editor`.
  * `PRINCIPAL`: the principal identifier, such as `user:user@example.com` or `serviceAccount:my-sa@example-project.iam.gserviceaccount.com`.
  * `ETAG`: the `etag` string returned by `skills:getIamPolicy`.



## Delete a skill

Deleting a skill container permanently deletes the `Skill` resource and all associated immutable `SkillRevision` resources. Agents attempting to resolve the deleted [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) fail at runtime.

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click the name of the skill you want to delete.
  5. In the **Skill Details** page, click delete **Delete**.
  6. In the confirmation dialog, enter `DELETE` and click **Delete**.



###  gcloud 

To delete a skill, use the [`gcloud agent-registry skills delete`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/delete) command:
    
    
    gcloud agent-registry skills delete SKILL_ID \
        --project=PROJECT_ID \
        --location=LOCATION
    

Replace the following:

  * `SKILL_ID`: the ID of the skill you want to delete. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.



###  REST 

To delete a skill, send a `DELETE` request:
    
    
    curl -X DELETE \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID?force=true"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `SKILL_ID`: the ID of the skill you want to delete. For manually registered skills, include the `private-` prefix, such as `private-my-skill`.



## What's next

  * Learn how to [upload new revisions and download packages](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * Learn how to [scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills).
  * Understand [roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions) for governing skills.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
