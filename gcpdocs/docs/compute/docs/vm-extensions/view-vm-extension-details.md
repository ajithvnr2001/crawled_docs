---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details/
title: View VM extension details and status \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:54:03.349354+00:00
---

# View VM extension details and status  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View VM extension details and status Stay organized with collections  Save and categorize content based on your preferences. 

You install VM extensions on Compute Engine virtual machine (VM) instances by creating global or zonal extension policies at the organization, folder, or project level. A single policy can install multiple extensions on a single VM, and multiple policies can apply to the same VM.

This document describes how to use read-only `get` and `list` methods across your Google Cloud resource hierarchy to perform the following tasks:

  * **View extension policies in your resource hierarchy**. List global or zonal VM extension policies to view policy details and rollout state across your organization, folder, or project.
  * **View VM extensions and versions**. List VM extensions that VM Extension Manager supports or view extension details—including version numbers and support levels—across all zones or in a specific zone in your organization, folder, or project.
  * **View the status of installed extensions on each VM**. List all installed VM extensions and their runtime states on an instance when a policy installs multiple extensions on a VM, or view the final effective configuration and governing policy (`policyId`) when multiple policies apply to the same VM.
  * **Troubleshoot extensions on an instance**. View installation progress, runtime health status, and diagnostic messages when an unexpected extension is installed or an extension fails on a VM instance.



## Before you begin

Before you view VM extension policies, retrieve VM extension details, or inspect extension states on your VM instances, complete the following prerequisites:

  * Read [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager) to understand how extension policies manage guest agent plugins across your VM fleet.
  * If you haven't deployed extensions to your instances yet, create a policy first. For more information, see [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy).
  * Ensure that you have the required Identity and Access Management permissions to view extension policies, retrieve extension details, and inspect instance extension states.



## Policy and extension viewing limitations

When you view VM extension policies, extension details, and instance states, consider the following operational constraints:

  * You can view folder-scoped and organization-scoped VM extension policies only by using the Google Cloud CLI or the Compute Engine REST API.
  * You can retrieve VM extension details and instance extension states only by using the Google Cloud CLI or the Compute Engine REST API. You can't view VM extension details or per-instance extension states in the Google Cloud console.
  * Instance extension state APIs (`getVmExtensionState` and `listVmExtensionStates`) report runtime status only for extensions that VM Extension Manager policies install and manage. These APIs don't report status for standalone agents that you install manually outside of VM Extension Manager.



## View extension policies

You can list VM extension policies or inspect the configuration details of a specific policy at the organization, folder, or project level.

### View global extension policies across all zones in an organization

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list all global VM extension policies in your organization or inspect a specific organization-scoped global policy to audit fleet-wide extension rollouts.

#### Required IAM permissions

To get the permissions that you need to view organization-scoped extension policies, ask your administrator to grant you the [Organization level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyViewer) (`roles/compute.orgVmExtensionPolicyViewer`) or [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view organization-scoped extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view organization-scoped extension policies:

  * List extension policies: `compute.orgVmExtensionPolicies.list`
  * View details of an extension policy: `compute.orgVmExtensionPolicies.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view global extension policies in an organization, select one of the following options:

###  gcloud 

To view all global extension policies in an organization, run the [`gcloud preview compute global-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/list) with the `--organization` flag:
    
    
    gcloud preview compute global-vm-extension-policies list \
      --organization=organizations/ORGANIZATION_ID \
      --page-size=PAGE_SIZE

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific global extension policy in an organization, run the [`gcloud preview compute global-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/describe) with the `--organization` flag:
    
    
    gcloud preview compute global-vm-extension-policies describe POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.



###  REST 

To view all global extension policies in an organization, send a `GET` request to the [`organizationGlobalVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationGlobalVmExtensionPolicies/list):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/global/vmExtensionPolicies
    

To view details of a specific global extension policy in an organization, send a `GET` request to the [`organizationGlobalVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationGlobalVmExtensionPolicies/get):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/global/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.



### View global extension policies across all zones in a folder

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list all global VM extension policies in a folder or inspect a specific folder-scoped global policy to verify which extensions apply across projects in that folder.

#### Required IAM permissions

To get the permissions that you need to view folder-scoped extension policies, ask your administrator to grant you the [Folder level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyViewer) (`roles/compute.folderVmExtensionPolicyViewer`) or [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view folder-scoped extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view folder-scoped extension policies:

  * List extension policies: `compute.folderVmExtensionPolicies.list`
  * View details of an extension policy: `compute.folderVmExtensionPolicies.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view global extension policies in a folder, select one of the following options:

###  gcloud 

To view all global extension policies in a folder, run the [`gcloud preview compute global-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/list) with the `--folder` flag:
    
    
    gcloud preview compute global-vm-extension-policies list \
      --folder=folders/FOLDER_ID \
      --page-size=PAGE_SIZE

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific global extension policy in a folder, run the [`gcloud preview compute global-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/describe) with the `--folder` flag:
    
    
    gcloud preview compute global-vm-extension-policies describe POLICY_NAME \
      --folder=folders/FOLDER_ID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `FOLDER_ID`: the ID of your Google Cloud folder.



###  REST 

To view all global extension policies in a folder, send a `GET` request to the [`folderGlobalVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderGlobalVmExtensionPolicies/list):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/global/vmExtensionPolicies
    

To view details of a specific global extension policy in a folder, send a `GET` request to the [`folderGlobalVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderGlobalVmExtensionPolicies/get):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/global/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `FOLDER_ID`: the ID of your Google Cloud folder.



### View global extension policies across all zones in a project

You can view global VM extension policies in a project to monitor rollout progress and inspect extension configurations across all zones in that project.

#### Required IAM permissions

To get the permissions that you need to view project-scoped extension policies, ask your administrator to grant you the [Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyViewer) (`roles/compute.vmExtensionPolicyViewer`) or [Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view project-scoped extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view project-scoped extension policies:

  * List extension policies: `compute.vmExtensionPolicies.list`
  * View details of an extension policy: `compute.vmExtensionPolicies.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view global extension policies in a project, select one of the following options:

###  Console 

To view global VM extension policies in your project by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Global policies**. This tab lists all the global VM extension policies in your project.



###  gcloud 

To view all global extension policies in a project, run the [`gcloud compute global-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/list):
    
    
    gcloud compute global-vm-extension-policies list \
      --project=PROJECT_ID \
      --page-size=PAGE_SIZE

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific global extension policy in a project, run the [`gcloud compute global-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/describe):
    
    
    gcloud compute global-vm-extension-policies describe POLICY_NAME \
      --project=PROJECT_ID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `PROJECT_ID`: the ID of your Google Cloud project.



###  REST 

To view all global extension policies in a project, send a `GET` request to the [`globalVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/list):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies
    

To view details of a specific global extension policy in a project, send a `GET` request to the [`globalVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `PROJECT_ID`: the ID of your Google Cloud project.



### View zonal extension policies in a zone across an organization

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list organization-scoped VM extension policies in a specific zone or inspect a single policy to audit zone-level enforcement rules across your organization.

#### Required IAM permissions

To get the permissions that you need to view organization-scoped extension policies, ask your administrator to grant you the [Organization level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyViewer) (`roles/compute.orgVmExtensionPolicyViewer`) or [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view organization-scoped extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view organization-scoped extension policies:

  * List extension policies: `compute.orgVmExtensionPolicies.list`
  * View details of an extension policy: `compute.orgVmExtensionPolicies.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view zonal extension policies in an organization, select one of the following options:

###  gcloud 

To view all organization-scoped extension policies in a zone, run the [`gcloud preview compute zone-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/list) with the `--organization` flag:
    
    
    gcloud preview compute zone-vm-extension-policies list \
      --organization=organizations/ORGANIZATION_ID \
      --zone=ZONE \
      --page-size=PAGE_SIZE

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the name of the zone where you want to list VM extension policies.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific organization-scoped zonal extension policy, run the [`gcloud preview compute zone-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/describe) with the `--organization` flag:
    
    
    gcloud preview compute zone-vm-extension-policies describe POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



###  REST 

To view all zonal extension policies in an organization, send a `GET` request to the [`organizationZoneVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationZoneVmExtensionPolicies/list):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/zones/ZONE/vmExtensionPolicies
    

To view details of a specific zonal extension policy in an organization, send a `GET` request to the [`organizationZoneVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationZoneVmExtensionPolicies/get):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



### View zonal extension policies in a zone across a folder

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list folder-scoped VM extension policies in a specific zone or inspect a single policy to verify zone-level extension rules for projects in your folder.

#### Required IAM permissions

To get the permissions that you need to view folder-scoped extension policies, ask your administrator to grant you the [Folder level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyViewer) (`roles/compute.folderVmExtensionPolicyViewer`) or [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view folder-scoped extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view folder-scoped extension policies:

  * List extension policies: `compute.folderVmExtensionPolicies.list`
  * View details of an extension policy: `compute.folderVmExtensionPolicies.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view zonal extension policies in a folder, select one of the following options:

###  gcloud 

To view all folder-scoped extension policies in a zone, run the [`gcloud preview compute zone-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/list) with the `--folder` flag:
    
    
    gcloud preview compute zone-vm-extension-policies list \
      --folder=folders/FOLDER_ID \
      --zone=ZONE \
      --page-size=PAGE_SIZE

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the name of the zone where you want to list VM extension policies.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific folder-scoped zonal extension policy, run the [`gcloud preview compute zone-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/describe) with the `--folder` flag:
    
    
    gcloud preview compute zone-vm-extension-policies describe POLICY_NAME \
      --folder=folders/FOLDER_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



###  REST 

To view all zonal extension policies in a folder, send a `GET` request to the [`folderZoneVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderZoneVmExtensionPolicies/list):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/zones/ZONE/vmExtensionPolicies
    

To view details of a specific zonal extension policy in a folder, send a `GET` request to the [`folderZoneVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderZoneVmExtensionPolicies/get):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



### View zonal extension policies in a zone in a project

You can list project-scoped VM extension policies in a specific zone or inspect a single policy to verify which extensions apply to instances in that zone.

#### Required IAM permissions

To get the permissions that you need to view project-scoped extension policies, ask your administrator to grant you the [Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyViewer) (`roles/compute.vmExtensionPolicyViewer`) or [Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view project-scoped extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view project-scoped extension policies:

  * List extension policies: `compute.vmExtensionPolicies.list`
  * View details of an extension policy: `compute.vmExtensionPolicies.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view zonal extension policies in a project, select one of the following options:

###  Console 

To view zonal VM extension policies in your project by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. To view details of a specific extension policy, click the name of the policy.



###  gcloud 

To view all project-scoped extension policies in a zone, run the [`gcloud compute zone-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/list):
    
    
    gcloud compute zone-vm-extension-policies list \
      --project=PROJECT_ID \
      --zone=ZONE \
      --page-size=PAGE_SIZE

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the name of the zone where you want to list VM extension policies.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific project-scoped zonal extension policy, run the [`gcloud compute zone-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/describe):
    
    
    gcloud compute zone-vm-extension-policies describe POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



###  REST 

To view all zonal extension policies in a project, send a `GET` request to the [`zoneVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/list):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies
    

To view details of a specific zonal extension policy in a project, send a `GET` request to the [`zoneVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



## View VM extensions and versions

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use read-only `get` and `list` methods to view the VM extensions that VM Extension Manager supports across your organization, folder, or project. You can view the extension names, version numbers, and [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels) across all zones or within a specific zone.

### View VM extensions across all zones in an organization

Use read-only `get` and `list` methods to view the VM extensions that VM Extension Manager supports across all zones in your organization, including their version numbers and support levels.

#### Required IAM permissions

To get the permissions that you need to view VM extensions across your organization, ask your administrator to grant you the [Organization level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyViewer) (`roles/compute.orgVmExtensionPolicyViewer`) or [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extensions across your organization. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extensions across your organization:

  * List VM extensions: `compute.orgVmExtensions.list`
  * View details of a VM extension: `compute.orgVmExtensions.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view the VM extensions and versions that VM Extension Manager supports across all zones in your organization, select one of the following options:

###  gcloud 

To list all VM extensions that VM Extension Manager supports and their support levels across all zones in your organization, run the [`gcloud preview compute global-vm-extension-policies extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/list) with the `--organization` flag:
    
    
    gcloud preview compute global-vm-extension-policies extensions list \
      --organization=organizations/ORGANIZATION_ID

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.



The output lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in your organization, run the [`gcloud preview compute global-vm-extension-policies extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/describe) with the `--organization` flag:
    
    
    gcloud preview compute global-vm-extension-policies extensions describe EXTENSION_NAME \
      --organization=organizations/ORGANIZATION_ID

Replace the following:

  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`, `google-cloud-sap-extension`, or `google-cloud-workload-extension`).
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.



###  REST 

To list all VM extensions that VM Extension Manager supports and their support levels across all zones in your organization, send a `GET` request to the [`organizationGlobalVmExtensionPolicies.listVmExtensions` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationGlobalVmExtensionPolicies/listVmExtensions):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/global/vmExtensions
    

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.



The response lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in your organization, send a `GET` request to the [`organizationGlobalVmExtensionPolicies.getVmExtension` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationGlobalVmExtensionPolicies/getVmExtension):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/global/vmExtensions/EXTENSION_NAME
    

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`).



### View VM extensions across all zones in a folder

Use read-only `get` and `list` methods to view the VM extensions that VM Extension Manager supports across all zones in your folder, including their version numbers and support levels.

#### Required IAM permissions

To get the permissions that you need to view VM extensions across your folder, ask your administrator to grant you the [Folder level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyViewer) (`roles/compute.folderVmExtensionPolicyViewer`) or [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extensions across your folder. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extensions across your folder:

  * List VM extensions: `compute.folderVmExtensions.list`
  * View details of a VM extension: `compute.folderVmExtensions.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view the VM extensions and versions that VM Extension Manager supports across all zones in your folder, select one of the following options:

###  gcloud 

To list all VM extensions that VM Extension Manager supports and their support levels across all zones in your folder, run the [`gcloud preview compute global-vm-extension-policies extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/list) with the `--folder` flag:
    
    
    gcloud preview compute global-vm-extension-policies extensions list \
      --folder=folders/FOLDER_ID

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.



The output lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in your folder, run the [`gcloud preview compute global-vm-extension-policies extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/describe) with the `--folder` flag:
    
    
    gcloud preview compute global-vm-extension-policies extensions describe EXTENSION_NAME \
      --folder=folders/FOLDER_ID

Replace the following:

  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`, `google-cloud-sap-extension`, or `google-cloud-workload-extension`).
  * `FOLDER_ID`: the ID of your Google Cloud folder.



###  REST 

To list all VM extensions that VM Extension Manager supports and their support levels across all zones in your folder, send a `GET` request to the [`folderGlobalVmExtensionPolicies.listVmExtensions` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderGlobalVmExtensionPolicies/listVmExtensions):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/global/vmExtensions
    

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.



The response lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in your folder, send a `GET` request to the [`folderGlobalVmExtensionPolicies.getVmExtension` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderGlobalVmExtensionPolicies/getVmExtension):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/global/vmExtensions/EXTENSION_NAME
    

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`).



### View VM extensions across all zones in a project

Use read-only `get` and `list` methods to view the VM extensions that VM Extension Manager supports across all zones in your project, including their version numbers and support levels.

#### Required IAM permissions

To get the permissions that you need to view VM extensions in your project, ask your administrator to grant you the [Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyViewer) (`roles/compute.vmExtensionPolicyViewer`) or [Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extensions in your project. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extensions in your project:

  * List VM extensions: `compute.vmExtensions.list`
  * View details of a VM extension: `compute.vmExtensions.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view the VM extensions and versions that VM Extension Manager supports across all zones in your project, select one of the following options:

###  gcloud 

To list all VM extensions that VM Extension Manager supports and their support levels across all zones in your project, run the [`gcloud preview compute global-vm-extension-policies extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/list):
    
    
    gcloud preview compute global-vm-extension-policies extensions list \
      --project=PROJECT_ID

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.



The output lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in your project, run the [`gcloud preview compute global-vm-extension-policies extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/describe):
    
    
    gcloud preview compute global-vm-extension-policies extensions describe EXTENSION_NAME \
      --project=PROJECT_ID

Replace the following:

  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`, `google-cloud-sap-extension`, or `google-cloud-workload-extension`).
  * `PROJECT_ID`: the ID of your Google Cloud project.



###  REST 

To list all VM extensions that VM Extension Manager supports and their support levels across all zones in your project, send a `GET` request to the [`globalVmExtensionPolicies.listVmExtensions` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/globalVmExtensionPolicies/listVmExtensions):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/projects/PROJECT_ID/global/vmExtensions
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.



The following JSON snippet shows an example response that lists the VM extensions that VM Extension Manager supports and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels):
    
    
    {
      "kind": "compute#globalVmExtensionList",
      "items": [
        {
          "kind": "compute#globalVmExtension",
          "name": "ops-agent",
          "versions": [
            "2.58.0",
            "2.57.0"
          ],
          "supportLevel": "GA",
          "selfLink": "https://www.googleapis.com/compute/2026-10-01-preview/projects/my-project/global/vmExtensions/ops-agent"
        }
      ]
    }
    

To view the details of a specific VM extension in your project, send a `GET` request to the [`globalVmExtensionPolicies.getVmExtension` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/globalVmExtensionPolicies/getVmExtension):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/projects/PROJECT_ID/global/vmExtensions/EXTENSION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`).



### View VM extensions in a zone in an organization

Use read-only `get` and `list` methods to view the VM extensions that VM Extension Manager supports in a specific zone across your organization, including their version numbers and support levels.

#### Required IAM permissions

To get the permissions that you need to view VM extensions in a zone across your organization, ask your administrator to grant you the [Organization level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyViewer) (`roles/compute.orgVmExtensionPolicyViewer`) or [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extensions in a zone across your organization. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extensions in a zone across your organization:

  * List VM extensions: `compute.orgVmExtensions.list`
  * View details of a VM extension: `compute.orgVmExtensions.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view the VM extensions and versions that VM Extension Manager supports in a zone across your organization, select one of the following options:

###  gcloud 

To list all VM extensions that VM Extension Manager supports and their support levels in a specific zone across your organization, run the [`gcloud preview compute zone-vm-extension-policies extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/extensions/list) with the `--organization` flag:
    
    
    gcloud preview compute zone-vm-extension-policies extensions list \
      --organization=organizations/ORGANIZATION_ID \
      --zone=ZONE

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the Google Cloud zone where you want to list VM extensions (for example, `us-central1-a`).



The output lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in a zone across your organization, run the [`gcloud preview compute zone-vm-extension-policies extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/extensions/describe) with the `--organization` flag:
    
    
    gcloud preview compute zone-vm-extension-policies extensions describe EXTENSION_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --zone=ZONE

Replace the following:

  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`).
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the zone where you want to view the extension details.



###  REST 

To list all VM extensions that VM Extension Manager supports and their support levels in a specific zone across your organization, send a `GET` request to the [`organizationZoneVmExtensionPolicies.listVmExtensions` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationZoneVmExtensionPolicies/listVmExtensions):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/zones/ZONE/vmExtensions
    

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the name of the zone (for example, `us-central1-a`).



The response lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in a zone across your organization, send a `GET` request to the [`organizationZoneVmExtensionPolicies.getVmExtension` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationZoneVmExtensionPolicies/getVmExtension):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/zones/ZONE/vmExtensions/EXTENSION_NAME
    

Replace the following:

  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the name of the zone.
  * `EXTENSION_NAME`: the name of the VM extension.



### View VM extensions in a zone in a folder

Use read-only `get` and `list` methods to view the VM extensions that VM Extension Manager supports in a specific zone across your folder, including their version numbers and support levels.

#### Required IAM permissions

To get the permissions that you need to view VM extensions in a zone across your folder, ask your administrator to grant you the [Folder level Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyViewer) (`roles/compute.folderVmExtensionPolicyViewer`) or [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extensions in a zone across your folder. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extensions in a zone across your folder:

  * List VM extensions: `compute.folderVmExtensions.list`
  * View details of a VM extension: `compute.folderVmExtensions.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view the VM extensions and versions that VM Extension Manager supports in a zone across your folder, select one of the following options:

###  gcloud 

To list all VM extensions that VM Extension Manager supports and their support levels in a specific zone across your folder, run the [`gcloud preview compute zone-vm-extension-policies extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/extensions/list) with the `--folder` flag:
    
    
    gcloud preview compute zone-vm-extension-policies extensions list \
      --folder=folders/FOLDER_ID \
      --zone=ZONE

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the Google Cloud zone where you want to list VM extensions (for example, `us-central1-a`).



The output lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in a zone across your folder, run the [`gcloud preview compute zone-vm-extension-policies extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/extensions/describe) with the `--folder` flag:
    
    
    gcloud preview compute zone-vm-extension-policies extensions describe EXTENSION_NAME \
      --folder=folders/FOLDER_ID \
      --zone=ZONE

Replace the following:

  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`).
  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the zone where you want to view the extension details.



###  REST 

To list all VM extensions that VM Extension Manager supports and their support levels in a specific zone across your folder, send a `GET` request to the [`folderZoneVmExtensionPolicies.listVmExtensions` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderZoneVmExtensionPolicies/listVmExtensions):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/zones/ZONE/vmExtensions
    

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the name of the zone (for example, `us-central1-a`).



The response lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in a zone across your folder, send a `GET` request to the [`folderZoneVmExtensionPolicies.getVmExtension` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderZoneVmExtensionPolicies/getVmExtension):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/zones/ZONE/vmExtensions/EXTENSION_NAME
    

Replace the following:

  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the name of the zone.
  * `EXTENSION_NAME`: the name of the VM extension.



### View VM extensions in a zone in a project

Use read-only `get` and `list` methods to view the VM extensions that VM Extension Manager supports in a specific zone in your project, including their version numbers and support levels.

#### Required IAM permissions

To get the permissions that you need to view VM extensions in a zone in your project, ask your administrator to grant you the [Compute VM extension policies viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyViewer) (`roles/compute.vmExtensionPolicyViewer`) or [Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extensions in a zone in your project. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extensions in a zone in your project:

  * List VM extensions: `compute.vmExtensions.list`
  * View details of a VM extension: `compute.vmExtensions.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view the VM extensions and versions that VM Extension Manager supports in a zone in your project, select one of the following options:

###  gcloud 

To list all VM extensions that VM Extension Manager supports and their support levels in a specific zone in your project, run the [`gcloud preview compute zone-vm-extension-policies extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/extensions/list):
    
    
    gcloud preview compute zone-vm-extension-policies extensions list \
      --zone=ZONE \
      --project=PROJECT_ID

Replace the following:

  * `ZONE`: the Google Cloud zone where you want to list VM extensions (for example, `us-central1-a`).
  * `PROJECT_ID`: the ID of your Google Cloud project.



The output lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in a zone in your project, run the [`gcloud preview compute zone-vm-extension-policies extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/extensions/describe):
    
    
    gcloud preview compute zone-vm-extension-policies extensions describe EXTENSION_NAME \
      --zone=ZONE \
      --project=PROJECT_ID

Replace the following:

  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`).
  * `ZONE`: the zone where you want to view the extension details.
  * `PROJECT_ID`: the ID of your Google Cloud project.



###  REST 

To list all VM extensions that VM Extension Manager supports and their support levels in a specific zone in your project, send a `GET` request to the [`zoneVmExtensionPolicies.listVmExtensions` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/zoneVmExtensionPolicies/listVmExtensions):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/projects/PROJECT_ID/zones/ZONE/vmExtensions
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the name of the zone (for example, `us-central1-a`).



The response lists the VM extensions that VM Extension Manager supports, their versions, and their [extension support levels](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#extension-support-levels).

To view the details of a specific VM extension in a zone in your project, send a `GET` request to the [`zoneVmExtensionPolicies.getVmExtension` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/zoneVmExtensionPolicies/getVmExtension):
    
    
    GET https://compute.googleapis.com/compute/2026-10-01-preview/projects/PROJECT_ID/zones/ZONE/vmExtensions/EXTENSION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the name of the zone.
  * `EXTENSION_NAME`: the name of the VM extension.



## View VM extension states on an instance

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You install VM extensions on VMs by creating global or zonal extension policies at the organization, folder, or project level. A single policy can install multiple extensions on a single VM, and multiple policies across your resource hierarchy can apply to the same VM. Use the read-only instance extension state `list` and `get` methods to view the runtime status of installed extensions on each VM without connecting to individual machines. These methods help you see the final effective configuration and governing policy (`policyId`) for each installed extension, or troubleshoot when an unexpected extension is installed or an extension fails on an instance.

### Required IAM permissions

To get the permissions that you need to view VM extension states on an instance, ask your administrator to grant you the [Compute Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`), [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`), or [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extension states on an instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extension states on an instance:

  * List all VM extension states on an instance: `compute.instances.listVmExtensionStates`
  * Get the state of a specific VM extension on an instance: `compute.instances.getVmExtensionState`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### List all VM extension states on an instance

When a policy installs multiple extensions on a VM, when multiple policies apply to the same instance, or when you find an unexpected extension during troubleshooting, list all extension states on the VM to view the final effective configuration and runtime status of every installed extension. The response shows each extension's active version, enforcement state, health status, and governing policy (`policyId`).

To view the states of all installed VM extensions on an instance, select one of the following options:

###  gcloud 

To list all installed VM extensions and view their current states on an instance, run the [`gcloud beta compute instances list-vm-extension-states` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/list-vm-extension-states):
    
    
    gcloud beta compute instances list-vm-extension-states INSTANCE_NAME \
        --zone=ZONE \
        --project=PROJECT_ID

Replace the following variables with values for your environment:

  * `INSTANCE_NAME`: the name of the VM instance.
  * `ZONE`: the zone where the instance is located (for example, `us-central1-a`).
  * `PROJECT_ID`: the ID of your Google Cloud project.



The command returns a table that lists each installed extension's name, enforcement state, and health status:
    
    
    EXTENSION_NAME  ENFORCEMENT_STATE  HEALTH_STATUS
    ops-agent       INSTALLED          RUNNING
    

###  REST 

To list all installed VM extensions and view their current states on an instance, send a `GET` request to the [`instances.listVmExtensionStates` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/listVmExtensionStates):
    
    
    GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/vmExtensionStates
    

Replace the following variables with values for your environment:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the zone where the instance is located.
  * `INSTANCE_NAME`: the name or ID of the VM instance.



The following JSON snippet shows an example response that lists the states of installed extensions on an instance:
    
    
    {
      "kind": "compute#vmExtensionStatesList",
      "items": [
        {
          "name": "ops-agent",
          "version": "2.58.0",
          "healthStatus": "RUNNING",
          "enforcementState": "INSTALLED",
          "healthMsg": "Plugin is running ok",
          "policyId": "projects/my-project/zones/us-central1-a/vmExtensionPolicies/prod-ops-policy"
        }
      ]
    }
    

### View the state of a specific VM extension on an instance

When multiple policies target a VM or an installed extension isn't running as expected, view the state of that specific extension to see its final effective configuration (`policyId` and version) and diagnostic status messages.

To view the effective state and governing policy of a specific VM extension on an instance, select one of the following options:

###  gcloud 

To retrieve the effective state, active version, and governing policy of a specific VM extension on an instance, run the [`gcloud beta compute instances get-vm-extension-state` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/get-vm-extension-state):
    
    
    gcloud beta compute instances get-vm-extension-state INSTANCE_NAME \
        --extension-name=EXTENSION_NAME \
        --zone=ZONE \
        --project=PROJECT_ID

Replace the following variables with values for your environment:

  * `INSTANCE_NAME`: the name of the VM instance.
  * `EXTENSION_NAME`: the name of the extension that you want to inspect (for example, `ops-agent`).
  * `ZONE`: the zone where the instance resides.
  * `PROJECT_ID`: the ID of your Google Cloud project.



###  REST 

To retrieve the effective state, active version, and governing policy of a specific VM extension on an instance, send a `GET` request to the [`instances.getVmExtensionState` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/getVmExtensionState):
    
    
    GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/vmExtensionStates/EXTENSION_NAME
    

Replace the following variables with values for your environment:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the zone where the instance resides.
  * `INSTANCE_NAME`: the name or ID of the VM instance.
  * `EXTENSION_NAME`: the name of the VM extension (for example, `ops-agent`).



The following JSON snippet shows an example response for a single VM extension state on an instance:
    
    
    {
      "name": "ops-agent",
      "version": "2.58.0",
      "healthStatus": "RUNNING",
      "enforcementState": "INSTALLED",
      "enforcementMsg": "",
      "healthMsg": "Plugin is running ok",
      "policyId": "projects/my-project/zones/us-central1-a/vmExtensionPolicies/prod-ops-policy"
    }
    

### Interpret VM extension state fields

When you retrieve the state of a VM extension on an instance, the response includes fields that report the enforced policy, active version, installation progress, and runtime health of the plugin.

The following table describes the fields that a `VmExtensionState` resource returns:

Field | Description  
---|---  
`name` | The identifier of the VM extension (for example, `ops-agent`).  
`version` | The active version of the extension that is installed on the VM instance.  
`policyId` | The identifier of the effective VM extension policy that enforces this extension on the instance. If multiple policies target the VM, this field indicates the winning policy after priority resolution.  
`enforcementState` | The current lifecycle state of the extension enforcement process. Possible values include the following: 

  * `ENFORCEMENT_STATE_UNSPECIFIED`: The enforcement state isn't specified.
  * `INSTALLING`: The guest agent is installing the extension.
  * `INSTALLED`: The extension is installed on the instance.
  * `INSTALL_FAILED`: The installation failed and no previous stable revision is available for rollback.
  * `ROLLING_BACK`: The guest agent is rolling back the extension to the last recorded stable revision.
  * `ROLLED_BACK`: The extension rolled back to the last stable revision.
  * `ROLLBACK_FAILED`: The rollback attempt failed.
  * `INCOMPATIBLE`: None of the available revisions for the extension version are compatible with the VM's operating system or architecture.
  * `REMOVING`: The guest agent is removing the extension from the instance.
  * `SERVICE_DISABLED`: The required service API for this extension is disabled in the project.
  * `APPLYING_CONFIG`: The guest agent is applying a new configuration to the extension, which might involve restarting the plugin.

  
`enforcementMsg` | A diagnostic status message that the guest agent returns if the extension fails to enforce or encounters an installation error.  
`healthStatus` | The runtime health status of the enforced extension plugin. If the extension isn't enforced yet, this value is unspecified. Possible values include the following: 

  * `HEALTH_STATUS_UNSPECIFIED`: The health status isn't specified.
  * `STARTING`: The extension process is starting.
  * `RUNNING`: The extension process is running normally.
  * `STOPPING`: The extension process is stopping.
  * `STOPPED`: The extension process is stopped.
  * `CRASHED`: The extension process started, but unexpectedly stopped running.

  
`healthMsg` | A diagnostic message that the extension reports about its health status (for example, `Plugin is running ok`).  
  
## What's next

  * To diagnose failed rollouts, check running guest processes, or inspect guest agent debug logs, see [Troubleshoot VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions).
  * To query historical enforcement events and audit installation or crash records in Cloud Logging, see [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs).
  * To build Cloud Monitoring dashboards and set up alerts for agent health, CPU, and memory usage, see [Monitor VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/monitor-vm-extensions).
  * To modify configuration settings, change pinned versions, or remove deployed agents, see [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
