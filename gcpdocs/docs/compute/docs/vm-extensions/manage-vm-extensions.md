---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions/
title: Manage VM extensions by using extension policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:47:56.580056+00:00
---

# Manage VM extensions by using extension policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage VM extensions by using extension policies Stay organized with collections  Save and categorize content based on your preferences. 

VM Extension Manager uses extension policies to manage your VM extensions at scale. For more information, see [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager). This document describes how to update and delete global and zonal VM extension policies at the project level, or at the folder and organization levels (available in [Preview](https://docs.cloud.google.com/products#product-launch-stages)). To view extension policies, VM extensions and versions, and runtime extension states on VM instances, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details). To diagnose installation or runtime issues, see [Troubleshoot VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions).

## Policy management limitations

You can update and delete folder-scoped and organization-scoped VM extension policies only by using the Google Cloud CLI or the Compute Engine REST API. You can't manage folder-scoped or organization-scoped policies in the Google Cloud console.

## Modify extensions by updating a VM extension policy

When you update a policy, VM Extension Manager rolls out the changes to all applicable VMs, typically within one minute. If you modify inclusion labels, extensions might be installed on new VMs or uninstalled from existing VMs based on whether they match the updated labels.

### Modify VM extensions across all zones in an organization

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to update an organization-scoped extension policy, ask your administrator to grant you the [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.orgVmExtensionPolicies.update` permission, which is required to update an organization-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To update an organization-scoped global extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute global-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/update) with the `--organization` flag to modify an existing organization-scoped global VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update an organization-scoped global VM extension policy, run the following command:
    
    
    gcloud preview compute global-vm-extension-policies update POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR \
      --rollout-retry-uuid=RETRY_UUID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `ORGANIZATION_ID`: your Google Cloud organization ID.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension. 

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs across all descendant projects and zones under the organization.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, specify the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` using the following format: 
        
        --rollout-custom-plan=organizations/ORGANIZATION_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME

Replace the following:

    * `ORGANIZATION_ID`: the organization where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined.

If you don't specify a rollout plan flag, VM Extension Manager uses `slow_rollout`.

  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `RETRY_UUID`: a UUID that identifies a retry attempt for a policy update rollout. This UUID lets you retry an update without changes. An error occurs if you set this flag and the policy is modified. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



#### Example: Update an organization-scoped global policy

The following command updates the policy `prod-frontend-policy` in organization `123456789` to add the `google-cloud-workload-extension` extension and unpin `ops-agent` so that it tracks the latest version using a fast rollout plan:
    
    
    gcloud preview compute global-vm-extension-policies update prod-frontend-policy \
      --organization=organizations/123456789 \
      --description="Updated policy: ops-agent + workload extension, unpinned" \
      --extensions=ops-agent,google-cloud-workload-extension \
      --config=ops-agent="updated-monitoring-config" \
      --inclusion-labels="env=prod,workload=frontend" \
      --priority=100 \
      --rollout-predefined-plan=fast_rollout

###  REST 

To update an organization-scoped global extension policy, make a `PATCH` request to the [`organizationGlobalVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationGlobalVmExtensionPolicies/update). When you update a policy by using REST, you only need to provide the fields that you want to update. Any fields that you omit retain their existing values.
    
    
    PATCH https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/global/vmExtensionPolicies/POLICY_NAME
    
    {
    "description": "DESCRIPTION",
    "extensionPolicies": {
      "EXTENSION_NAME": {
        "pinnedVersion": "EXTENSION_NAME_VERSION",
        "stringConfig": "EXTENSION_NAME_CONFIG"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
          "inclusionLabels": {
            "KEY_1": "VALUE_1",
            "KEY_2": "VALUE_2"
          }
        }
      }
    ],
    "priority": PRIORITY,
    "rolloutOperation": {
      "rolloutInput": {
        "conflictBehavior": "ROLLOUT_CONFLICT_BEHAVIOR",
        "retryUuid": "RETRY_UUID",
        "name": "organizations/ORGANIZATION_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"
      }
    }
    }
    

Replace the following:

  * `ORGANIZATION_ID`: your Google Cloud organization ID.
  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `EXTENSION_NAME`: the name of the extension to update, used as a key in the `extensionPolicies` map. To update multiple extensions, include multiple entries in the `extensionPolicies` map.
  * `EXTENSION_NAME_VERSION`: the version of the VM extension.
  * `EXTENSION_NAME_CONFIG`: configuration settings for the VM extension, as an inline string.
  * `KEY_1:VALUE_1`, `KEY_2:VALUE_2`: key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. To specify multiple selectors, include multiple objects in the `instanceSelectors` array, each with a `labelSelector` field. In that case, VM Extension Manager targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs across all descendant projects and zones under the organization.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. To use a predefined rollout plan, replace the `name` field with `predefinedRolloutPlan` and specify one of the following values: 
    * `SLOW_ROLLOUT`: rolls out the policy over five days. This predefined plan is the default rollout plan if you don't specify a plan.
    * `FAST_ROLLOUT`: rolls out the policy immediately to all zones.
  * `RETRY_UUID`: a UUID that identifies a retry attempt for a policy update rollout.



### Modify VM extensions across all zones in a folder

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to update a folder-scoped extension policy, ask your administrator to grant you the [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.folderVmExtensionPolicies.update` permission, which is required to update a folder-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To update a folder-scoped global extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute global-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/update) with the `--folder` flag to modify an existing folder-scoped global VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update a folder-scoped global VM extension policy, run the following command:
    
    
    gcloud preview compute global-vm-extension-policies update POLICY_NAME \
      --folder=folders/FOLDER_ID \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR \
      --rollout-retry-uuid=RETRY_UUID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `FOLDER_ID`: your Google Cloud folder ID.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension. 

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs across all descendant projects and zones within the folder.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, specify the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` using the following format: 
        
        --rollout-custom-plan=folders/FOLDER_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME

Replace the following:

    * `FOLDER_ID`: the folder where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined.

If you don't specify a rollout plan flag, VM Extension Manager uses `slow_rollout`.

  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `RETRY_UUID`: a UUID that identifies a retry attempt for a policy update rollout. This UUID lets you retry an update without changes. An error occurs if you set this flag and the policy is modified. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



###  REST 

To update a folder-scoped global extension policy, make a `PATCH` request to the [`folderGlobalVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderGlobalVmExtensionPolicies/update). When you update a policy by using REST, you only need to provide the fields that you want to update. Any fields that you omit retain their existing values.
    
    
    PATCH https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/global/vmExtensionPolicies/POLICY_NAME
    
    {
    "description": "DESCRIPTION",
    "extensionPolicies": {
      "EXTENSION_NAME": {
        "pinnedVersion": "EXTENSION_NAME_VERSION",
        "stringConfig": "EXTENSION_NAME_CONFIG"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
          "inclusionLabels": {
            "KEY_1": "VALUE_1",
            "KEY_2": "VALUE_2"
          }
        }
      }
    ],
    "priority": PRIORITY,
    "rolloutOperation": {
      "rolloutInput": {
        "conflictBehavior": "ROLLOUT_CONFLICT_BEHAVIOR",
        "retryUuid": "RETRY_UUID",
        "name": "folders/FOLDER_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"
      }
    }
    }
    

Replace the following:

  * `FOLDER_ID`: your Google Cloud folder ID.
  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `EXTENSION_NAME`: the name of the extension to update, used as a key in the `extensionPolicies` map. To update multiple extensions, include multiple entries in the `extensionPolicies` map.
  * `EXTENSION_NAME_VERSION`: the version of the VM extension.
  * `EXTENSION_NAME_CONFIG`: configuration settings for the VM extension, as an inline string.
  * `KEY_1:VALUE_1`, `KEY_2:VALUE_2`: key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. To specify multiple selectors, include multiple objects in the `instanceSelectors` array, each with a `labelSelector` field. In that case, VM Extension Manager targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs across all descendant projects and zones within the folder.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. To use a predefined rollout plan, replace the `name` field with `predefinedRolloutPlan` and specify one of the following values: 
    * `SLOW_ROLLOUT`: rolls out the policy over five days. This predefined plan is the default rollout plan if you don't specify a plan.
    * `FAST_ROLLOUT`: rolls out the policy immediately to all zones.
  * `RETRY_UUID`: a UUID that identifies a retry attempt for a policy update rollout.



### Modify VM extensions across all zones in a project

#### Required IAM permissions

To get the permission that you need to update a project-scoped extension policy, ask your administrator to grant you the [](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin)[Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.vmExtensionPolicies.update` permission, which is required to update a project-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To update a project-scoped global extension policy, select one of the following options:

###  Console 

To update a project-scoped global VM extension policy in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Global policies** , and then select the policy that you want to edit.
  3. Click **Edit**.
  4. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  5. In the **Manage extensions** section, do the following: 
     * To add more extensions, click **Add extension** and select the extension and version.
     * To delete an extension managed by this policy, click the **Delete** button next to the extension name.
  6. If you want to apply labels, add labels for the target VMs in the **Target VM instances** section.
  7. Click **Save**.

**Note:** The Google Cloud console doesn't support editing a rollout. To edit a rollout, use either the gcloud CLI or REST API.

###  gcloud 

Use the [`gcloud compute global-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) to modify an existing project-scoped global VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update a project-scoped global VM extension policy, run the following command:
    
    
    gcloud compute global-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR \
      --rollout-retry-uuid=RETRY_UUID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension. 

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in all zones in the project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, specify the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` using the following format: 
        
        --rollout-custom-plan=projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME

Replace the following:

    * `PROJECT_NUMBER`: the project where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined.

If you don't specify a rollout plan flag, VM Extension Manager uses `slow_rollout`.

  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `RETRY_UUID`: a UUID that identifies a retry attempt for a policy update rollout. This UUID lets you retry an update without changes. An error occurs if you set this flag and the policy is modified. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



###  REST 

To update a project-scoped global extension policy, make a `PATCH` request to the [`globalVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/update). When you update a policy by using REST, you only need to provide the fields that you want to update. Any fields that you omit retain their existing values.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies/POLICY_NAME
    
    {
    "description": "DESCRIPTION",
    "extensionPolicies": {
      "EXTENSION_NAME": {
        "pinnedVersion": "EXTENSION_NAME_VERSION",
        "stringConfig": "EXTENSION_NAME_CONFIG"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
          "inclusionLabels": {
            "KEY_1": "VALUE_1",
            "KEY_2": "VALUE_2"
          }
        }
      }
    ],
    "priority": PRIORITY,
    "rolloutOperation": {
      "rolloutInput": {
        "conflictBehavior": "ROLLOUT_CONFLICT_BEHAVIOR",
        "retryUuid": "RETRY_UUID",
        "name": "projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"
      }
    }
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `EXTENSION_NAME`: the name of the extension to update, used as a key in the `extensionPolicies` map. To update multiple extensions, include multiple entries in the `extensionPolicies` map.
  * `EXTENSION_NAME_VERSION`: the version of the VM extension.
  * `EXTENSION_NAME_CONFIG`: configuration settings for the VM extension, as an inline string.
  * `KEY_1:VALUE_1`, `KEY_2:VALUE_2`: key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. To specify multiple selectors, include multiple objects in the `instanceSelectors` array, each with a `labelSelector` field. In that case, VM Extension Manager targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs across all zones in the project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `PROJECT_NUMBER`: the project where the custom rollout plan is defined.
  * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. To use a predefined rollout plan, replace the `name` field with `predefinedRolloutPlan` and specify one of the following values: 
    * `SLOW_ROLLOUT`: rolls out the policy over five days. This predefined plan is the default rollout plan if you don't specify a plan.
    * `FAST_ROLLOUT`: rolls out the policy immediately to all zones.
  * `RETRY_UUID`: a UUID that identifies a retry attempt for a policy update rollout.



### Modify VM extensions in a zone across an organization

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to update an organization-scoped extension policy, ask your administrator to grant you the [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.orgVmExtensionPolicies.update` permission, which is required to update an organization-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To update an organization-scoped zonal extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute zone-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/update) with the `--organization` flag to modify an existing organization-scoped zonal VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update an organization-scoped zonal VM extension policy, run the following command:
    
    
    gcloud preview compute zone-vm-extension-policies update POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --zone=ZONE \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `ORGANIZATION_ID`: your Google Cloud organization ID.
  * `ZONE`: the Google Cloud zone where the policy applies.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension. 

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in the specified zone across all descendant projects under the organization.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



###  REST 

To update an organization-scoped zonal extension policy, make a `PATCH` request to the [`organizationZoneVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationZoneVmExtensionPolicies/update). When you update a policy by using REST, you only need to provide the fields that you want to update. Any fields that you omit retain their existing values.
    
    
    PATCH https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    
    {
    "description": "DESCRIPTION",
    "extensionPolicies": {
      "EXTENSION_NAME": {
        "pinnedVersion": "EXTENSION_NAME_VERSION",
        "stringConfig": "EXTENSION_NAME_CONFIG"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
          "inclusionLabels": {
            "KEY_1": "VALUE_1",
            "KEY_2": "VALUE_2"
          }
        }
      }
    ],
    "priority": PRIORITY
    }
    

Replace the following:

  * `ORGANIZATION_ID`: your Google Cloud organization ID.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.
  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `EXTENSION_NAME`: the name of the extension to update, used as a key in the `extensionPolicies` map. To update multiple extensions, include multiple entries in the `extensionPolicies` map.
  * `EXTENSION_NAME_VERSION`: the version of the VM extension.
  * `EXTENSION_NAME_CONFIG`: configuration settings for the VM extension, as an inline string.
  * `KEY_1:VALUE_1`, `KEY_2:VALUE_2`: key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. To specify multiple selectors, include multiple objects in the `instanceSelectors` array, each with a `labelSelector` field. In that case, VM Extension Manager targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone across all descendant projects under the organization.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



### Modify VM extensions in a zone across a folder

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to update a folder-scoped extension policy, ask your administrator to grant you the [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.folderVmExtensionPolicies.update` permission, which is required to update a folder-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To update a folder-scoped zonal extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute zone-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/update) with the `--folder` flag to modify an existing folder-scoped zonal VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update a folder-scoped zonal VM extension policy, run the following command:
    
    
    gcloud preview compute zone-vm-extension-policies update POLICY_NAME \
      --folder=folders/FOLDER_ID \
      --zone=ZONE \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `FOLDER_ID`: your Google Cloud folder ID.
  * `ZONE`: the Google Cloud zone where the policy applies.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension. 

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in the specified zone across all descendant projects within the folder.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



###  REST 

To update a folder-scoped zonal extension policy, make a `PATCH` request to the [`folderZoneVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderZoneVmExtensionPolicies/update). When you update a policy by using REST, you only need to provide the fields that you want to update. Any fields that you omit retain their existing values.
    
    
    PATCH https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    
    {
    "description": "DESCRIPTION",
    "extensionPolicies": {
      "EXTENSION_NAME": {
        "pinnedVersion": "EXTENSION_NAME_VERSION",
        "stringConfig": "EXTENSION_NAME_CONFIG"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
          "inclusionLabels": {
            "KEY_1": "VALUE_1",
            "KEY_2": "VALUE_2"
          }
        }
      }
    ],
    "priority": PRIORITY
    }
    

Replace the following:

  * `FOLDER_ID`: your Google Cloud folder ID.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.
  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `EXTENSION_NAME`: the name of the extension to update, used as a key in the `extensionPolicies` map. To update multiple extensions, include multiple entries in the `extensionPolicies` map.
  * `EXTENSION_NAME_VERSION`: the version of the VM extension.
  * `EXTENSION_NAME_CONFIG`: configuration settings for the VM extension, as an inline string.
  * `KEY_1:VALUE_1`, `KEY_2:VALUE_2`: key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. To specify multiple selectors, include multiple objects in the `instanceSelectors` array, each with a `labelSelector` field. In that case, VM Extension Manager targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone across all descendant projects within the folder.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



### Modify VM extensions in a zone in a project

#### Required IAM permissions

To get the permission that you need to update a project-scoped extension policy, ask your administrator to grant you the [](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin)[Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.vmExtensionPolicies.update` permission, which is required to update a project-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To update a project-scoped zonal extension policy, select one of the following options:

###  Console 

To update a project-scoped zonal VM extension policy in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Select the policy that you want to update.
  3. Click **Edit**.
  4. Modify the **Description** , **Priority** , **Extensions** , or **Target VM instances**.
  5. Click **Save**.



###  gcloud 

Use the [`gcloud compute zone-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) to modify an existing project-scoped zonal VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update a project-scoped zonal VM extension policy, run the following command:
    
    
    gcloud compute zone-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone where the policy applies.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension. 

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in the specified zone within your project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



###  REST 

To update a project-scoped zonal extension policy, make a `PATCH` request to the [`zoneVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/update). When you update a policy by using REST, you only need to provide the fields that you want to update. Any fields that you omit retain their existing values.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    
    {
    "description": "DESCRIPTION",
    "extensionPolicies": {
      "EXTENSION_NAME": {
        "pinnedVersion": "EXTENSION_NAME_VERSION",
        "stringConfig": "EXTENSION_NAME_CONFIG"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
          "inclusionLabels": {
            "KEY_1": "VALUE_1",
            "KEY_2": "VALUE_2"
          }
        }
      }
    ],
    "priority": PRIORITY
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.
  * `POLICY_NAME`: the name of the VM extension policy to update.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `EXTENSION_NAME`: the name of the extension to update, used as a key in the `extensionPolicies` map. To update multiple extensions, include multiple entries in the `extensionPolicies` map.
  * `EXTENSION_NAME_VERSION`: the version of the VM extension.
  * `EXTENSION_NAME_CONFIG`: configuration settings for the VM extension, as an inline string.
  * `KEY_1:VALUE_1`, `KEY_2:VALUE_2`: key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. To specify multiple selectors, include multiple objects in the `instanceSelectors` array, each with a `labelSelector` field. In that case, VM Extension Manager targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone within your project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



## Uninstall extensions by deleting a VM extension policy

When you delete a policy, VM Extension Manager uninstalls the extensions from any VMs managed by that policy. However, if another active, lower-priority policy applies to a VM and declares the same extension, the extension remains installed on that VM based on the lower-priority policy.

VM Extension Manager removes extensions from all accessible VMs within one minute of policy deletion. If a VM is inaccessible because the guest agent is removed or the VM is deleted, VM Extension Manager skips deletion of the extension. If such a VM becomes available again, VM Extension Manager removes the extensions at that time.

### Uninstall VM extensions across all zones in an organization

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to delete an organization-scoped extension policy, ask your administrator to grant you the [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.orgVmExtensionPolicies.delete` permission, which is required to delete an organization-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete an organization-scoped global extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute global-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/delete) with the `--organization` flag to delete an existing organization-scoped global VM extension policy:
    
    
    gcloud preview compute global-vm-extension-policies delete POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-retry-uuid=RETRY_UUID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, specify the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` using the following format: 
        
        --rollout-custom-plan=organizations/ORGANIZATION_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME

Replace the following:

    * `ORGANIZATION_ID`: the organization where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined.

If you don't specify a rollout plan flag, VM Extension Manager uses `slow_rollout`.

  * `RETRY_UUID`: a UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



###  REST 

To delete an organization-scoped global extension policy, make a `POST` request to the [`organizationGlobalVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationGlobalVmExtensionPolicies/delete).
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/global/vmExtensionPolicies/POLICY_NAME/delete
    
    {
    "retryUuid": "RETRY_UUID",
    "predefinedRolloutPlan": "ROLLOUT_PLAN"
    }
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `ORGANIZATION_ID`: your Google Cloud organization ID.
  * `ROLLOUT_PLAN`: specify `SLOW_ROLLOUT` or `FAST_ROLLOUT`. To use a custom rollout plan, replace `predefinedRolloutPlan` with `"name": "organizations/ORGANIZATION_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"`.
  * `RETRY_UUID`: a UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



### Uninstall VM extensions across all zones in a folder

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to delete a folder-scoped extension policy, ask your administrator to grant you the [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.folderVmExtensionPolicies.delete` permission, which is required to delete a folder-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete a folder-scoped global extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute global-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/delete) with the `--folder` flag to delete an existing folder-scoped global VM extension policy:
    
    
    gcloud preview compute global-vm-extension-policies delete POLICY_NAME \
      --folder=folders/FOLDER_ID \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-retry-uuid=RETRY_UUID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, specify the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` using the following format: 
        
        --rollout-custom-plan=folders/FOLDER_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME

Replace the following:

    * `FOLDER_ID`: the folder where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined.

If you don't specify a rollout plan flag, VM Extension Manager uses `slow_rollout`.

  * `RETRY_UUID`: a UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



###  REST 

To delete a folder-scoped global extension policy, make a `POST` request to the [`folderGlobalVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderGlobalVmExtensionPolicies/delete).
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/global/vmExtensionPolicies/POLICY_NAME/delete
    
    {
    "retryUuid": "RETRY_UUID",
    "predefinedRolloutPlan": "ROLLOUT_PLAN"
    }
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `FOLDER_ID`: your Google Cloud folder ID.
  * `ROLLOUT_PLAN`: specify `SLOW_ROLLOUT` or `FAST_ROLLOUT`. To use a custom rollout plan, replace `predefinedRolloutPlan` with `"name": "folders/FOLDER_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"`.
  * `RETRY_UUID`: a UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



### Uninstall VM extensions across all zones in a project

#### Required IAM permissions

To get the permission that you need to delete a project-scoped extension policy, ask your administrator to grant you the [](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin)[Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.vmExtensionPolicies.delete` permission, which is required to delete a project-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete a project-scoped global extension policy, select one of the following options:

###  Console 

To delete a project-scoped global VM extension policy in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Global policies** , and then select the policy you want to delete.
  3. Click **Delete**.
  4. In the confirmation dialog, enter the policy name, and then click **Delete**.



###  gcloud 

Use the [`gcloud compute global-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/delete) to delete an existing project-scoped global VM extension policy:
    
    
    gcloud compute global-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-retry-uuid=RETRY_UUID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, specify the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` using the following format: 
        
        --rollout-custom-plan=projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME

Replace the following:

    * `PROJECT_NUMBER`: the project where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined.

If you don't specify a rollout plan flag, VM Extension Manager uses `slow_rollout`.

  * `RETRY_UUID`: a UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



###  REST 

To delete a project-scoped global extension policy, make a `POST` request to the [`globalVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/delete).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies/POLICY_NAME/delete
    
    {
    "retryUuid": "RETRY_UUID",
    "predefinedRolloutPlan": "ROLLOUT_PLAN"
    }
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ROLLOUT_PLAN`: specify `SLOW_ROLLOUT` or `FAST_ROLLOUT`. To use a custom rollout plan, replace `predefinedRolloutPlan` with `"name": "projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"`.
  * `RETRY_UUID`: a UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



### Uninstall VM extensions in a zone across an organization

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to delete an organization-scoped extension policy, ask your administrator to grant you the [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.orgVmExtensionPolicies.delete` permission, which is required to delete an organization-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete an organization-scoped zonal extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute zone-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/delete) with the `--organization` flag to delete an existing organization-scoped zonal VM extension policy:
    
    
    gcloud preview compute zone-vm-extension-policies delete POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `ORGANIZATION_ID`: the ID of your Google Cloud organization.
  * `ZONE`: the Google Cloud zone where the policy is located.



###  REST 

To delete an organization-scoped zonal extension policy, make a `DELETE` request to the [`organizationZoneVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationZoneVmExtensionPolicies/delete).
    
    
    DELETE https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `ORGANIZATION_ID`: your Google Cloud organization ID.
  * `ZONE`: the Google Cloud zone where the policy is located.



### Uninstall VM extensions in a zone across a folder

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to delete a folder-scoped extension policy, ask your administrator to grant you the [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.folderVmExtensionPolicies.delete` permission, which is required to delete a folder-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete a folder-scoped zonal extension policy, select one of the following options:

###  gcloud 

Use the [`gcloud preview compute zone-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/delete) with the `--folder` flag to delete an existing folder-scoped zonal VM extension policy:
    
    
    gcloud preview compute zone-vm-extension-policies delete POLICY_NAME \
      --folder=folders/FOLDER_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `FOLDER_ID`: the ID of your Google Cloud folder.
  * `ZONE`: the Google Cloud zone where the policy is located.



###  REST 

To delete a folder-scoped zonal extension policy, make a `DELETE` request to the [`folderZoneVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderZoneVmExtensionPolicies/delete).
    
    
    DELETE https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `FOLDER_ID`: your Google Cloud folder ID.
  * `ZONE`: the Google Cloud zone where the policy is located.



### Uninstall VM extensions in a zone in a project

#### Required IAM permissions

To get the permission that you need to delete a project-scoped extension policy, ask your administrator to grant you the [](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin)[Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.vmExtensionPolicies.delete` permission, which is required to delete a project-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete a project-scoped zonal extension policy, select one of the following options:

###  Console 

To delete a project-scoped zonal VM extension policy in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Select the policy that you want to delete.
  3. Click **Delete**.
  4. In the confirmation dialog, click **Delete**.



###  gcloud 

Use the [`gcloud compute zone-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/delete) to delete an existing project-scoped zonal VM extension policy:
    
    
    gcloud compute zone-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the Google Cloud zone where the policy is located.



###  REST 

To delete a project-scoped zonal extension policy, make a `DELETE` request to the [`zoneVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone where the policy is located.



## What's next

  * To inspect rollout progress and extension health status, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).
  * To diagnose failed rollouts, check running guest processes, or inspect guest agent debug logs, see [Troubleshoot VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions).
  * To build Cloud Monitoring dashboards and set up alerts for agent health, CPU, and memory usage, see [Monitor VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/monitor-vm-extensions).
  * To query historical enforcement events and audit installation or crash records in Cloud Logging, see [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
