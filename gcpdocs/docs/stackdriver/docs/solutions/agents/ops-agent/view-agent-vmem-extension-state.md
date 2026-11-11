---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/view-agent-vmem-extension-state/
title: View details and status of extensions on a VM \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:45:21.261180+00:00
---

# View details and status of extensions on a VM  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/view-agent-vmem-extension-state/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  View details and status of extensions on a VM Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use the read-only extension-state `list` and `get` methods to view the runtime status of installed extensions on each VM instance without connecting to each machine. When you use extension policies, one VM might have multiple extensions installed by different policies. The extension-state methods let you see the final effective configuration and governing policy for each installed extension and help you troubleshoot when an unexpected extension is installed or an extension fails on an instance.

## About extension details and status information

You install VM extensions on VMs by creating global or zonal extension policies at the organization, folder, or project level. A single policy can install multiple extensions on a single VM, and multiple policies across your resource hierarchy can apply to the same VM.

The read-only extension-state methods let you list the states of all extensions on the VM to view the final effective configuration and runtime status of every installed extension. The returned information shows each extension's active version, enforcement state, health status, and identifier of the governing policy.

## View VM extensions and versions

You can use the Google Cloud CLI or the Compute Engine API to view the details about installed VM extensions. This document describes how to use gcloud. For information about using the Compute Engine API to view extension states, see [View MV extension states on an instance](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-extension-states).

### IAM permissions required to view extension details

To see the roles required to view information about installed extensions and their versions from the project, folder, or organization level, select one of the levels:

###  Project 

To get the permissions that you need to view zonal or global VM extension policies at the project level, ask your administrator to grant you the [Compute VM extension policy viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyViewer) (`roles/compute.vmExtensionPolicyViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view zonal or global VM extension policies at the project level. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view zonal or global VM extension policies at the project level:

  * Describe a specific VM extension on an instance: `compute.vmExtensions.get`
  * List all VM extensions on an instance: `compute.vmExtensions.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

###  Folder 

Folder-level extension policies are available in [Preview](https://cloud.google.com/products#product-launch-stages).

To get the permissions that you need to view zonal or global VM extension policies at the folder level, ask your administrator to grant you the [Folder level Compute VM extension policies viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyViewer) (`roles/compute.folderVmExtensionPolicyViewer`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view zonal or global VM extension policies at the folder level. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view zonal or global VM extension policies at the folder level:

  * Describe a specific VM extension on an instance: `compute.folderVmExtensions.get`
  * List all VM extensions on an instance: `compute.folderVmExtensions.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

###  Organization 

Organization-level extension policies are available in [Preview](https://cloud.google.com/products#product-launch-stages).

To get the permissions that you need to view zonal or global VM extension policies at the organization level, ask your administrator to grant you the [Organization level Compute VM extension policies viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyViewer) (`roles/compute.orgVmExtensionPolicyViewer`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view zonal or global VM extension policies at the organization level. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view zonal or global VM extension policies at the organization level:

  * Describe a specific VM extension on an instance: `compute.orgVmExtensions.get`
  * List all VM extensions on an instance: `compute.orgVmExtensions.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about IAM roles and permissions in Compute Engine, see [Compute Engine roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/compute).

### List VM extensions and versions

To list the VM extensions and versions that are managed by VM Extension Manager across zones or globally in your project, folder, or organization, select one of the following options:

###  Zonal 

Use the [ `gcloud preview compute zone-vm-extension-policies` `extensions` `list`](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/vm-extension-policies/extensions/list") command to list the VM extensions in a zone within your project, folder, or organization:

**Project level**
    
    
    gcloud preview compute zone-vm-extension-policies extensions list \
      --project=PROJECT_ID \
      --zone=ZONE
    

Replace the following variables in the command:

  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.

**Folder and organization levels**

To perform the preceding task at the folder or organization level, use the same command with one of the following changes:

  * For folder-level information, replace the  `--project=PROJECT_ID` option with  `--folder=folders/FOLDER_ID`, where FOLDER_ID is the numeric ID of your folder.
  * For organization-level information, replace the  `--project=PROJECT_ID` option with  `--organization=organizations/ORGANIZATION_ID`, where ORGANIZATION_ID is the numeric ID of your organization.



###  Global 

Use the [ `gcloud preview compute global-vm-extension-policies` `extensions` `list`](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/list") command to list the VM extensions in all zones within your project, folder, or organization:

**Project level**
    
    
    gcloud preview compute global-vm-extension-policies extensions list \
      --project=PROJECT_ID
    

Replace the following variable in the command:

  * PROJECT_ID: The identifier of the project.

**Folder and organization levels**

To perform the preceding task at the folder or organization level, use the same command with one of the following changes:

  * For folder-level information, replace the  `--project=PROJECT_ID` option with  `--folder=folders/FOLDER_ID`, where FOLDER_ID is the numeric ID of your folder.
  * For organization-level information, replace the  `--project=PROJECT_ID` option with  `--organization=organizations/ORGANIZATION_ID`, where ORGANIZATION_ID is the numeric ID of your organization.



### View information about a specific VM extension

To view the details of a specific VM extension across a single zone or globally in your in your project, folder, or organization, select one of the following options:

###  Zonal 

Use the [ `gcloud preview compute zone-vm-extension-policies` `extensions` `describe`](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/vm-extension-policies/extensions/describe") command to view the details of a specific VM extension in a zone within your project, folder, or organization:

**Project level**
    
    
    gcloud preview compute zone-vm-extension-policies extensions describe EXTENSION_NAME \
      --project=PROJECT_ID \
      --zone=ZONE
    

Replace the following variables in the command:

  * EXTENSION_NAME: One of the VM Extension Manager [supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions); for example, `ops-agent`.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.

**Folder and organization levels**

To perform the preceding task at the folder or organization level, use the same command with one of the following changes:

  * For folder-level information, replace the  `--project=PROJECT_ID` option with  `--folder=folders/FOLDER_ID`, where FOLDER_ID is the numeric ID of your folder.
  * For organization-level information, replace the  `--project=PROJECT_ID` option with  `--organization=organizations/ORGANIZATION_ID`, where ORGANIZATION_ID is the numeric ID of your organization.



###  Global 

Use the [ `gcloud preview compute global-vm-extension-policies` `extensions` `describe`](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions/describe") command to view the details of a specific VM extension across all zones within your project, folder, or organization:

**Project level**
    
    
    gcloud preview compute global-vm-extension-policies extensions describe EXTENSION_NAME \
      --project=PROJECT_ID
    

Replace the following variables in the command:

  * EXTENSION_NAME: One of the VM Extension Manager [supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions); for example, `ops-agent`.
  * PROJECT_ID: The identifier of the project.

**Folder and organization levels**

To perform the preceding task at the folder or organization level, use the same command with one of the following changes:

  * For folder-level information, replace the  `--project=PROJECT_ID` option with  `--folder=folders/FOLDER_ID`, where FOLDER_ID is the numeric ID of your folder.
  * For organization-level information, replace the  `--project=PROJECT_ID` option with  `--organization=organizations/ORGANIZATION_ID`, where ORGANIZATION_ID is the numeric ID of your organization.



## View the states of VM extensions on an instance

Extension policies might install multiple extensions on a single VM. To determine the status of each extension, including its effective configuration, runtime status, and other information, you can examine the state of the extensions on a specific VM.

The extension-state methods return information only about Ops Agent instances that are installed and managed by VM Extension Manager policies. If some VMs are running agents that were installed by other means, there is no extension information to report for those agents.

You can use the Google Cloud CLI or the Compute Engine API to view the state of extensions installed on VMs. This document describes how to use gcloud. For information about using the Compute Engine API to view extension states, see [View MV extension states on an instance](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-extension-states).

### IAM permissions required to view extension state

To get the permissions that you need to view VM extension states on an instance, ask your administrator to grant you the [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view VM extension states on an instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view VM extension states on an instance:

  * List states of all VM extensions on an instance: `compute.instances.listVmExtensionStates`
  * Get the state of a specific VM extension on an instance: `compute.instances.getVmExtensionState`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### List extensions installed on a VM instance

To list all VM extensions installed on an instance and view their current states by using gcloud, run the [ `gcloud beta compute instances` `list-vm-extension-states`](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions//list-vm-extension-states) command:
    
    
    gcloud beta compute instances list-vm-extension-states INSTANCE_NAME \
        --project=PROJECT_ID \
        --zone=ZONE
    

Replace the following variables in the command:

  * INSTANCE_NAME: The name of the VM instance.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The zone where the instance resides; for example, `us-central1-f`.



The command returns each installed extension's name, enforcement state, and health status. For information about the values returned when viewing extension states, see [Interpret VM extension state fields](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#interprret-stat-fields).

For more information about viewing information about the state of extensions on your VMs, including information about using the Compute Engine API, see [View MV extension states on an instance](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-extension-states).

### View the state of a specific VM extension on an instance

To get status information about a specific VM extension installed on a VM by using gcloud, run the [ `gcloud beta compute instances` `get-vm-extension-state`](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/extensions//get-vm-extension-states) command:
    
    
    gcloud beta compute instances get-vm-extension-state INSTANCE_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --extension-name=EXTENSION_NAME
    

Replace the following variables in the command:

  * INSTANCE_NAME: The name of the VM instance.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The zone where the instance resides; for example, `us-central1-f`.
  * EXTENSION_NAME: One of the VM Extension Manager [supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions); for example, `ops-agent`.



The command returns the extension's name, active version, health information, enforcement information, and the ID of the governing policy. For information about the values returned when viewing extension states, see [Interpret VM extension state fields](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#interprret-stat-fields).

For more information about viewing information about the state of extensions on your VMs, including information about using the Compute Engine API, see [View MV extension states on an instance](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-extension-states).

## What's next

  * Learn more about retrieving and interpreting extension-state information in [ View extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).
  * Troubleshoot extension policies: 
    * [For the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-agent-vmem-policies)
    * [Troubleshoot VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
