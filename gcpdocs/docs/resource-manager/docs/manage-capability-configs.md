---
url: https://docs.cloud.google.com/resource-manager/docs/manage-capability-configs/
title: Configure management boundaries \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:22.319547+00:00
---

# Configure management boundaries  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/manage-capability-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Configure management boundaries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to set up and manage management boundaries and capability configurations using Resource Manager. Management boundaries enable cross-project resource discovery and governance for [Agent Registry](https://docs.cloud.google.com/agent-registry/overview).

## Before you begin

Before configuring boundaries and capability configurations, obtain the required roles and enable the required API.

### Required roles

To get the permissions that you need to configure boundaries and capabilities, ask your administrator to grant you the following IAM roles: 

  * Create, update, and delete boundaries and capability configurations: [Resource Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.editor) (`roles/resourcemanager.editor`) on the target folder or organization (and the management project, if you provide a user-managed management project) 
  * View boundaries and capability configurations: [Resource Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.viewer) (`roles/resourcemanager.viewer`) on the target folder or organization 
  * Attach tags to member projects: 
    * [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the target folder, organization, or member projects
    * [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on the target folder or organization



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable API

  * To enable the Resource Manager API, use the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable):
        
        gcloud services enable cloudresourcemanager.googleapis.com \
          --project=PROJECT_ID
        

Replace `PROJECT_ID` with the ID of your project.




## Set up a management boundary

You can set up a management boundary on a folder or an organization in one of two ways:

  * **Folder-wide or organization-wide boundary (no tag filter)** : Includes all descendant projects in the folder or organization. Skip step 1 and step 4, and complete only Step 2: Create a boundary (without `--tag-key` and `--tag-value`) and Step 3: Create a capability configuration.
  * **Tag-based boundary** : Partitions projects in the folder or organization by tag values. Complete all four steps below.



### Step 1: Configure the partitioning tag key

Skip this step if you are creating a folder-wide or organization-wide boundary without a tag filter. By default, a `BoundaryConfig` resource has no tag key configured.

For tag-based boundaries, a `BoundaryConfig` resource establishes the tag key used to partition projects within a folder or organization. Configure this resource before creating tag-based boundaries.

To set the partitioning tag key, use the [`gcloud resource-manager boundary-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/boundary-configs/update):
    
    
    gcloud resource-manager boundary-configs update \
      --folder=FOLDER_ID \
      --tag-key=TAG_KEY_NAME
    

To configure the tag key on an organization, specify `--organization=ORGANIZATION_ID` instead of `--folder`. If you previously configured a tag key and want to switch to an untagged boundary (when no boundaries exist under the parent), run this command with `--clear-tag-key` instead of `--tag-key`.

Replace the following:

  * `FOLDER_ID`: the ID of the parent folder
  * `TAG_KEY_NAME`: the name of your tag key, formatted as `ORGANIZATION_ID/TAG_KEY_SHORT_NAME`, such as `123456789012/env`



### Step 2: Create a boundary

Create a `Boundary` resource in your folder or organization.

To create a folder-wide boundary without a tag filter (which automatically includes all descendant projects in the folder), use the [`gcloud resource-manager boundaries create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/boundaries/create) without `--tag-key` and `--tag-value`:
    
    
    gcloud resource-manager boundaries create BOUNDARY_ID \
      --folder=FOLDER_ID \
      --display-name="Production Boundary"
    

To create a tag-based boundary after configuring the partitioning tag key in step 1, include the `--tag-key` and `--tag-value` flags:
    
    
    gcloud resource-manager boundaries create BOUNDARY_ID \
      --folder=FOLDER_ID \
      --display-name="Production Boundary" \
      --tag-key=TAG_KEY_NAME \
      --tag-value=TAG_VALUE_SHORT_NAME
    

To create a boundary in an organization, specify `--organization=ORGANIZATION_ID` instead of `--folder`.

Replace the following:

  * `BOUNDARY_ID`: a unique ID for the boundary, such as `prod-boundary`
  * `FOLDER_ID`: the ID of the parent folder
  * `TAG_KEY_NAME`: the tag key that you configured, such as `123456789012/env`
  * `TAG_VALUE_SHORT_NAME`: the tag value that projects must have to join the boundary, such as `prod`



### Step 3: Create a capability configuration

Create a `CapabilityConfig` resource to link your boundary to a management project and declare which services are managed across the boundary.

To create a capability configuration, use the [`gcloud resource-manager capability-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capability-configs/create) and specify `--types=agent-management` for Agent Registry:
    
    
    gcloud resource-manager capability-configs create \
      CAPABILITY_CONFIG_ID \
      --folder=FOLDER_ID \
      --types=agent-management \
      --boundaries=folders/FOLDER_ID/boundaries/BOUNDARY_ID \
      --display-name="DISPLAY_NAME"
    

To create the capability configuration in an organization, specify `--organization=ORGANIZATION_ID` instead of `--folder`.

Replace the following:

  * `CAPABILITY_CONFIG_ID`: a unique ID for the capability configuration, such as `prod-capabilities`
  * `FOLDER_ID`: the ID of the parent folder
  * `BOUNDARY_ID`: the ID of the boundary that you created
  * `DISPLAY_NAME`: a human-readable display name



To enable capabilities on a single standalone project without boundaries, skip steps 1, 2, and 4, and run this command with `--project=PROJECT_NUMBER` and `--management-project=projects/PROJECT_NUMBER` instead of `--folder` and `--boundaries`.

To use an existing project as the management project, pass the `--management-project=projects/PROJECT_NUMBER` flag. The project that you specify must meet the following requirements, or the command fails with an error:

  * Reside directly under the same parent (`folders/FOLDER_ID` or `organizations/ORGANIZATION_ID`) as the `CapabilityConfig` resource.
  * Be in the `ACTIVE` lifecycle state.
  * Not already be designated as a management project.



If you omit `--management-project`, Resource Manager automatically provisions a dedicated management project directly under the parent folder or organization.

Creating a `CapabilityConfig` resource automatically enables the corresponding service APIs on the management project (such as `agentregistry.googleapis.com` when you specify `agent-management`). You don't need to manually enable these APIs on the management project.

**Note:** You can't create a boundary or capability configuration on a folder that already has legacy `app-management` (an [app-enabled folder](https://docs.cloud.google.com/resource-manager/docs/manage-applications)) enabled. 

### Step 4: Attach tags to member projects

Skip this step if you created a folder-wide or organization-wide boundary without a tag filter, because all descendant projects are included automatically.

For tag-based boundaries, projects dynamically join the management boundary when you bind the matching tag value to them.

To attach the tag to each project that belongs in the boundary, use the [`gcloud resource-manager tags bindings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create):
    
    
    gcloud resource-manager tags bindings create \
      --tag-value=TAG_VALUE_NAME \
      --parent=//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER
    

Replace the following:

  * `TAG_VALUE_NAME`: the tag value name, such as `123456789012/env/prod`
  * `PROJECT_NUMBER`: the project number (or project ID) of the project that you want to include in the boundary



## Manage capability configurations

You can list, describe, update, and delete capability configurations. The examples in this section use `--folder=FOLDER_ID`. To manage capability configurations on an organization or a project, specify `--organization=ORGANIZATION_ID` or `--project=PROJECT_NUMBER` instead of `--folder` (boundaries can only be attached to folder-level or organization-level capability configurations).

### List capability configurations

To list all capability configurations in a folder, use the [`gcloud resource-manager capability-configs list` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capability-configs/list):
    
    
    gcloud resource-manager capability-configs list \
      --folder=FOLDER_ID
    

### Describe a capability configuration

To view configuration details and the assigned management project, use the [`gcloud resource-manager capability-configs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capability-configs/describe):
    
    
    gcloud resource-manager capability-configs describe \
      CAPABILITY_CONFIG_ID \
      --folder=FOLDER_ID
    

### Update associated boundaries

To update the boundaries linked to a capability configuration, use the [`gcloud resource-manager capability-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capability-configs/update):
    
    
    gcloud resource-manager capability-configs update \
      CAPABILITY_CONFIG_ID \
      --folder=FOLDER_ID \
      --boundaries=folders/FOLDER_ID/boundaries/BOUNDARY_ID_1,folders/FOLDER_ID/boundaries/BOUNDARY_ID_2
    

The `update` command also accepts the `--types` and `--display-name` flags to update the enabled capability types or display name.

### Delete a capability configuration

A `CapabilityConfig` resource can't be deleted while boundaries are attached to it, and a `Boundary` resource can't be deleted while attached to a `CapabilityConfig` resource.

To delete a capability configuration when cross-project management is no longer required:

  1. To detach the associated boundaries, use the [`gcloud resource-manager capability-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capability-configs/update) with the `--clear-boundaries` flag:
         
         gcloud resource-manager capability-configs update \
           CAPABILITY_CONFIG_ID \
           --folder=FOLDER_ID \
           --clear-boundaries
         

  2. To delete the capability configuration, use the [`gcloud resource-manager capability-configs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capability-configs/delete):
         
         gcloud resource-manager capability-configs delete \
           CAPABILITY_CONFIG_ID \
           --folder=FOLDER_ID
         




## What's next

  * [Learn more about boundaries](https://docs.cloud.google.com/resource-manager/docs/boundaries-and-capabilities-overview)
  * [Learn more about Agent Registry](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
