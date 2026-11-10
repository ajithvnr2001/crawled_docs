---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy/
title: Install VM extensions by creating extension policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:47:54.578759+00:00
---

# Install VM extensions by creating extension policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install VM extensions by creating extension policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create VM extension policies, which let you automatically install and manage extensions on a fleet of Compute Engine virtual machines (VMs). By defining a policy, you can ensure that specific extensions are installed and maintained on any VMs that match criteria you specify, such as VM labels. You can create zonal or global VM extension policies at the project level, or at the organization and folder levels (available in [Preview](https://cloud.google.com/products#product-launch-stages)).

## Before you begin

  * Review the basics about [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).
  * Review [VM Extension Manager quotas](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#quotas).
  * Review [VM Extension Manager pricing](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#pricing). VM Extension Manager is available at no additional cost, but you might incur charges from using the extensions that your policies install.
  * Enable the Compute Engine API in your Google Cloud project if it's not already enabled. 

[Enable Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)

  * Ensure that your VM runs [the guest agent version `20241209.01` or later](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages).
  * To view debug logs for VM Extension Manager events, [configure the log settings for the guest agent](https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions#debug-guest-agent).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Policy creation limitations

You can create folder-scoped and organization-scoped VM extension policies only by using the Google Cloud CLI or the Compute Engine REST API.

## Policy priority and conflict resolution

When multiple policies across different hierarchy levels (organization, folder, or project) apply to the same VM, hierarchy level doesn't determine precedence. Instead, VM Extension Manager uses policy priority and update timestamps to resolve conflicts.

When two policies conflict for the same extension, the policy with the higher priority takes precedence. Priority values range from `0` to `65535`, where a lower number signifies a higher priority. The default priority is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs. Deleting a policy doesn't remove the extension if a lower-priority policy still applies to the VM.

## Install VM extensions by creating a global VM extension policy

You can create a global VM extension policy to install extensions on VMs across multiple zones according to a rollout plan. You can define a global policy at the project level, or at the folder or organization level (available in [Preview](https://cloud.google.com/products#product-launch-stages)).

VM Extension Manager doesn't apply a global VM extension policy directly to VMs; instead, as the policy rolls out, VM Extension Manager automatically replicates the global definition into corresponding zonal policies in each zone based on the rollout plan. After a replicated policy becomes available in a zone, VM Extension Manager evaluates VMs in that zone against the policy's inclusion labels and installs or updates the designated extensions. When you create new VMs, VM Extension Manager automatically evaluates and configures them.

### Rollout plans for global policies

Global VM extension policies use rollout plans to manage the deployment of extensions across different locations. You can use one of the predefined rollout plans or create a custom rollout plan.

#### Predefined rollout plans

You can select one of the following predefined rollout plans:

  * `slow_rollout`: rolls out the policy over five days. Slow rollout is the default rollout plan.
  * `fast_rollout`: rolls out the policy immediately to all zones.



#### Custom rollout plans

You can create custom rollout plans by using the [`rolloutPlans.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/rolloutPlans/insert). For example, the following JSON defines a rollout plan named `test-rollout-plan` that targets two zones:
    
    
    {
      "name": "test-rollout-plan",
      "waves": [
        {
          "selectors": [
            {
              "locationSelector": {
                "includedLocations": [
                  "us-central1-a",
                  "us-west1-a"
                ]
              }
            }
          ],
          "validation": {
            "type": "time",
            "timeBasedValidationMetadata": {
              "waitDuration": "0s"
            }
          },
          "orchestrationOptions": {
            "maxConcurrentResourcesPerLocation": "10",
            "maxConcurrentLocations": "10"
          }
        }
      ]
    }

You can then use this custom rollout plan when creating a global policy.

### Install VM extensions across all zones in an organization

Create an organization-scoped global extension policy to install and maintain VM extensions across all zones in all descendant projects of your organization.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to create an organization-scoped extension policy, ask your administrator to grant you the [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.orgVmExtensionPolicies.create` permission, which is required to create an organization-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To create an organization-scoped global extension policy, select one of the following options:

###  gcloud 

To create an organization-scoped global VM extension policy, use the [`gcloud preview compute global-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create) with the `--organization` flag:
    
    
    gcloud preview compute global-vm-extension-policies create POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR
    

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `ORGANIZATION_ID`: the organization ID for the organization-scoped policy. The resource format is `organizations/{organization}/global/vmExtensionPolicies/{name}`.
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




#### Example: Create an organization-scoped global policy

The following command creates a high-priority global policy named `prod-frontend-policy` at the organization level (`organizations/123456789`) for production frontend workloads (`env=prod,workload=frontend`), pinning a specific version for the `ops-agent` extension with a slow rollout plan:
    
    
    gcloud preview compute global-vm-extension-policies create prod-frontend-policy \
      --organization=organizations/123456789 \
      --description="Standard monitoring policy for production frontend VMs" \
      --extensions=ops-agent \
      --version=ops-agent=2.58.0 \
      --config=ops-agent="some-monitoring-config" \
      --inclusion-labels="env=prod,workload=frontend" \
      --priority=100 \
      --rollout-predefined-plan=slow_rollout

###  REST 

To create an organization-scoped global VM extension policy, send a `POST` request to the [`organizationGlobalVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationGlobalVmExtensionPolicies/insert):
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/global/vmExtensionPolicies
    
    {
    "name": "POLICY_NAME",
    "description": "DESCRIPTION",
    "extensionPolicies": {
       "EXTENSION_NAME_1": {
         "stringConfig": "EXTENSION_NAME_1_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_1_VERSION"
      },
       "EXTENSION_NAME_2": {
         "stringConfig": "EXTENSION_NAME_2_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_2_VERSION"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "KEY_1": "VALUE_1"
           }
        }
      }
    ],
    "priority": "PRIORITY",
    "rolloutOperation": {
      "rolloutInput": {
        "conflictBehavior": "ROLLOUT_CONFLICT_BEHAVIOR",
        "name": "organizations/ORGANIZATION_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"
      }
    }
    }
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs across all descendant projects and zones under the organization.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. To use a predefined rollout plan, replace the `name` field with `predefinedRolloutPlan` and specify one of the following values: 
    * `SLOW_ROLLOUT`: rolls out the policy over five days. This predefined plan is the default rollout plan if you don't specify a plan.
    * `FAST_ROLLOUT`: rolls out the policy immediately to all zones.



#### Example: Create an organization-scoped global policy

The following example creates a global policy named `org-global-extension-policy` that installs the `ops-agent` extension for organization `123456789` on VMs with label `env=prod`, with priority `100` and a `SLOW_ROLLOUT` predefined rollout plan:
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/organizations/123456789/global/vmExtensionPolicies
    
    {
    "name": "org-global-extension-policy",
    "description": "Standard monitoring policy for organization VMs",
    "extensionPolicies": {
       "ops-agent": {
         "stringConfig": "logging:
          receivers:
            systemd_logs:
              type: systemd_journald
          service:
            pipelines:
              systemd_pipeline:
                receivers: [systemd_logs]",
         "pinnedVersion": "2.58.0"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "env": "prod"
           }
        }
      }
    ],
    "priority": "100",
    "rolloutOperation": {
      "rolloutInput": {
        "predefinedRolloutPlan": "SLOW_ROLLOUT"
      }
    }
    }

### Install VM extensions across all zones in a folder

Create a folder-scoped global extension policy to install and maintain VM extensions across all zones in all descendant projects of your folder.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to create a folder-scoped extension policy, ask your administrator to grant you the [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.folderVmExtensionPolicies.create` permission, which is required to create a folder-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To create a folder-scoped global extension policy, select one of the following options:

###  gcloud 

To create a folder-scoped global VM extension policy, use the [`gcloud preview compute global-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create) with the `--folder` flag:
    
    
    gcloud preview compute global-vm-extension-policies create POLICY_NAME \
      --folder=folders/FOLDER_ID \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR
    

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `FOLDER_ID`: the folder ID for the folder-scoped policy. The resource format is `folders/{folder}/global/vmExtensionPolicies/{name}`.
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




#### Example: Create a folder-scoped global policy

The following command creates a global policy named `folder-global-extension-policy` at the folder level (`folders/123456`) that installs the `ops-agent` extension on VMs with label `env=prod` using a slow rollout plan:
    
    
    gcloud preview compute global-vm-extension-policies create folder-global-extension-policy \
      --folder=folders/123456 \
      --description="Standard monitoring policy for folder VMs" \
      --extensions=ops-agent \
      --version=ops-agent=2.58.0 \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
      --inclusion-labels="env=prod" \
      --priority=100 \
      --rollout-predefined-plan=slow_rollout

###  REST 

To create a folder-scoped global VM extension policy, send a `POST` request to the [`folderGlobalVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderGlobalVmExtensionPolicies/insert):
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/global/vmExtensionPolicies
    
    {
    "name": "POLICY_NAME",
    "description": "DESCRIPTION",
    "extensionPolicies": {
       "EXTENSION_NAME_1": {
         "stringConfig": "EXTENSION_NAME_1_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_1_VERSION"
      },
       "EXTENSION_NAME_2": {
         "stringConfig": "EXTENSION_NAME_2_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_2_VERSION"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "KEY_1": "VALUE_1"
           }
        }
      }
    ],
    "priority": "PRIORITY",
    "rolloutOperation": {
      "rolloutInput": {
        "conflictBehavior": "ROLLOUT_CONFLICT_BEHAVIOR",
        "name": "folders/FOLDER_ID/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"
      }
    }
    }
    

Replace the following:

  * `FOLDER_ID`: your folder ID.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs across all descendant projects and zones within the folder.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. To use a predefined rollout plan, replace the `name` field with `predefinedRolloutPlan` and specify one of the following values: 
    * `SLOW_ROLLOUT`: rolls out the policy over five days. This predefined plan is the default rollout plan if you don't specify a plan.
    * `FAST_ROLLOUT`: rolls out the policy immediately to all zones.



#### Example: Create a folder-scoped global policy

The following example creates a global policy named `folder-global-extension-policy` that installs the `ops-agent` extension for folder `123456` on VMs with label `env=prod`, with priority `500` and a `SLOW_ROLLOUT` predefined rollout plan:
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/folders/123456/global/vmExtensionPolicies
    
    {
    "name": "folder-global-extension-policy",
    "description": "Test extension policy for Ops Agent at folder level",
    "extensionPolicies": {
       "ops-agent": {
         "stringConfig": "logging:
          receivers:
            systemd_logs:
              type: systemd_journald
          service:
            pipelines:
              systemd_pipeline:
                receivers: [systemd_logs]",
         "pinnedVersion": "2.58.0"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "env": "prod"
           }
        }
      }
    ],
    "priority": "500",
    "rolloutOperation": {
      "rolloutInput": {
        "predefinedRolloutPlan": "SLOW_ROLLOUT"
      }
    }
    }

### Install VM extensions across all zones in a project

Create a project-scoped global extension policy to install and maintain VM extensions across all zones in your project.

#### Required IAM permissions

To get the permission that you need to create a project-scoped extension policy, ask your administrator to grant you the [](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin)[Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.vmExtensionPolicies.create` permission, which is required to create a project-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To create a project-scoped global extension policy, select one of the following options:

###  Console 

To create a project-scoped global VM extension policy in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create extension policy**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is `1000`.
  6. In the **Scope** section, select **Global rollout**.
  7. In the **Manage extensions** section, click **Add extension** and do the following for each extension that you want to install on the target VMs: 
     1. From the **Extension** list, select an extension. For more information, see [Supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions).
     2. From the **Version** list, specify the version number of the extension. Leave blank to select the latest version. 
        * For Ops Agent, you can specify version `2.58.0` or later.
        * For Extension for SAP and Extension for Compute Workloads, leave the field blank to select the latest version.
     3. Optional: In the **Config file content** field, enter configuration parameters for the extension.
  8. In the **Rollout plan** field, select a rollout plan from the following options: 
     * **Slow rollout** : installs extensions gradually across your fleet of VMs over a period of time. This rollout plan is the default option.
     * **Fast rollout** : installs extensions to all targeted VMs across all zones and regions immediately.

For more information about rollout plans, see [Rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#rollout-global-policies).

**Note:** The Google Cloud console doesn't support selecting a custom rollout plan. To use a custom rollout plan, use either the gcloud CLI or REST API.
  9. In the **Target VM instances** section, select the VMs for the policy. To select VMs with specific labels, click **Add labels** and add the key-value pair.
  10. Click **Create**.



###  gcloud 

To create a project-scoped global VM extension policy, use the [`gcloud compute global-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create):
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR
    

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `PROJECT_ID`: the project ID for the project-scoped policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension. 

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in your project across all zones.
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




#### Example: Create a project-scoped global policy

The following command creates a policy named `global-test-extension-policy` that installs the `ops-agent` extension for project `test-project`. The `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent, and `--rollout-predefined-plan` specifies the `slow_rollout` plan.
    
    
    gcloud compute global-vm-extension-policies create global-test-extension-policy \
      --project=test-project \
      --extensions=ops-agent \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
      --rollout-predefined-plan=slow_rollout

#### Example: Create a project-scoped global policy with a custom rollout plan

The following command creates a policy named `global-test-extension-policy-2` that installs the `ops-agent` extension for project `test-project` on VMs with label `env=prod`. The policy priority is set to `500`, and the `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent. The `--rollout-custom-plan` flag specifies a custom rollout plan.
    
    
    gcloud compute global-vm-extension-policies create global-test-extension-policy-2 \
      --project=test-project \
      --extensions=ops-agent \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
      --priority=500 \
      --inclusion-labels=env=prod \
      --rollout-custom-plan=projects/12345678/locations/global/rolloutPlans/test-rollout-plan

###  REST 

To create a project-scoped global VM extension policy, send a `POST` request to the [`globalVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies
    
    {
    "name": "POLICY_NAME",
    "description": "DESCRIPTION",
    "extensionPolicies": {
       "EXTENSION_NAME_1": {
         "stringConfig": "EXTENSION_NAME_1_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_1_VERSION"
      },
       "EXTENSION_NAME_2": {
         "stringConfig": "EXTENSION_NAME_2_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_2_VERSION"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "KEY_1": "VALUE_1"
           }
        }
      }
    ],
    "priority": "PRIORITY",
    "rolloutOperation": {
      "rolloutInput": {
        "conflictBehavior": "ROLLOUT_CONFLICT_BEHAVIOR",
        "name": "projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"
      }
    }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in your project across all zones.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.
  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when VM Extension Manager detects a conflict between a zonal policy and a global policy. You can specify one of the following conflict behaviors: 
    * `""` (empty string): the global policy doesn't overwrite conflicting zonal policies that have the same name. This conflict behavior is the default.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more information, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `PROJECT_NUMBER`: the project where the custom rollout plan is defined.
  * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. To use a predefined rollout plan, replace the `name` field with `predefinedRolloutPlan` and specify one of the following values: 
    * `SLOW_ROLLOUT`: rolls out the policy over five days. This predefined plan is the default rollout plan if you don't specify a plan.
    * `FAST_ROLLOUT`: rolls out the policy immediately to all zones.



#### Example: Create a project-scoped global policy

The following example creates a policy named `global-test-extension-policy` that installs the `ops-agent` extension for project `12345678` on VMs with label `env=prod`. The policy priority is set to `500`, and it uses rollout plan `test-rollout-plan`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/12345678/global/vmExtensionPolicies
    
    {
    "name": "global-test-extension-policy",
    "description": "Test extension policy for Ops Agent",
    "extensionPolicies": {
       "ops-agent": {
         "stringConfig": "logging:
          receivers:
            systemd_logs:
              type: systemd_journald
          service:
            pipelines:
              systemd_pipeline:
                receivers: [systemd_logs]",
         "pinnedVersion": "2.58.0"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "env": "prod"
           }
        }
      }
    ],
    "priority": "500",
    "rolloutOperation": {
      "rolloutInput": {
        "name": "projects/12345678/locations/global/rolloutPlans/test-rollout-plan"
      }
    }
    }

## Install VM extensions by creating a zonal VM extension policy

You can create a zonal VM extension policy to define which extensions to install and on which VMs in a specific zone. You can define a zonal policy at the project level, or at the folder or organization level (available in [Preview](https://cloud.google.com/products#product-launch-stages)).

### Install VM extensions in a zone across an organization

Create an organization-scoped zonal extension policy to install and maintain VM extensions in a specific zone across all descendant projects of your organization.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to create an organization-scoped extension policy, ask your administrator to grant you the [Organization level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgVmExtensionPolicyAdmin) (`roles/compute.orgVmExtensionPolicyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.orgVmExtensionPolicies.create` permission, which is required to create an organization-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To create an organization-scoped zonal extension policy, select one of the following options:

###  gcloud 

To create an organization-scoped zonal VM extension policy and roll out the policy to VMs in a specific zone, use the [`gcloud preview compute zone-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/create) with the `--organization` flag:
    
    
    gcloud preview compute zone-vm-extension-policies create POLICY_NAME \
      --organization=organizations/ORGANIZATION_ID \
      --zone=ZONE \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `ORGANIZATION_ID`: the organization ID for the organization-scoped policy. The resource format is `organizations/{organization}/zones/{zone}/vmExtensionPolicies/{name}`.
  * `ZONE`: the zone where this policy applies.
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



The command fails if a policy with the specified name already exists in the zone.

#### Example: Create an organization-scoped zonal policy

The following command creates a zonal policy named `org-test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for organization `organizations/123456789` on VMs with label `env=prod`:
    
    
    gcloud preview compute zone-vm-extension-policies create org-test-extension-policy \
      --organization=organizations/123456789 \
      --zone=us-central1-f \
      --extensions=ops-agent \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
      --priority=100 \
      --inclusion-labels=env=prod

###  REST 

To create an organization-scoped zonal VM extension policy, send a `POST` request to the [`organizationZoneVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationZoneVmExtensionPolicies/insert). This method defines which extensions to install and on which VMs in a specific zone across the organization.
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/organizations/ORGANIZATION_ID/zones/ZONE/vmExtensionPolicies
    
    {
    "name": "POLICY_NAME",
    "description": "DESCRIPTION",
    "extensionPolicies": {
       "EXTENSION_NAME_1": {
         "stringConfig": "EXTENSION_NAME_1_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_1_VERSION"
      },
       "EXTENSION_NAME_2": {
         "stringConfig": "EXTENSION_NAME_2_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_2_VERSION"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "KEY_1": "VALUE_1"
           }
        }
      }
    ],
    "priority": "PRIORITY"
    }
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `ZONE`: the zone where this policy applies.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone across all descendant projects under the organization.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



#### Example: Create an organization-scoped zonal policy

The following example creates a policy named `org-test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for organization `123456789`.
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/organizations/123456789/zones/us-central1-f/vmExtensionPolicies
    
    {
    "name": "org-test-extension-policy",
    "description": "Test extension policy for Ops Agent at organization level",
    "extensionPolicies": {
       "ops-agent": {
         "stringConfig": "logging:
          receivers:
            systemd_logs:
              type: systemd_journald
          service:
            pipelines:
              systemd_pipeline:
                receivers: [systemd_logs]",
         "pinnedVersion": "2.58.0"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "env": "prod"
           }
        }
      }
    ],
    "priority": "100"
    }

### Install VM extensions in a zone across a folder

Create a folder-scoped zonal extension policy to install and maintain VM extensions in a specific zone across all descendant projects of your folder.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Required IAM permissions

To get the permission that you need to create a folder-scoped extension policy, ask your administrator to grant you the [Folder level Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.folderVmExtensionPolicyAdmin) (`roles/compute.folderVmExtensionPolicyAdmin`) IAM role on your folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.folderVmExtensionPolicies.create` permission, which is required to create a folder-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To create a folder-scoped zonal extension policy, select one of the following options:

###  gcloud 

To create a folder-scoped zonal VM extension policy and roll out the policy to VMs in a specific zone, use the [`gcloud preview compute zone-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zone-vm-extension-policies/create) with the `--folder` flag:
    
    
    gcloud preview compute zone-vm-extension-policies create POLICY_NAME \
      --folder=folders/FOLDER_ID \
      --zone=ZONE \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `FOLDER_ID`: the folder ID for the folder-scoped policy. The resource format is `folders/{folder}/zones/{zone}/vmExtensionPolicies/{name}`.
  * `ZONE`: the zone where this policy applies.
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



The command fails if a policy with the specified name already exists in the zone.

#### Example: Create a folder-scoped zonal policy

The following command creates a zonal policy named `folder-test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for folder `folders/123456` on VMs with label `env=prod`:
    
    
    gcloud preview compute zone-vm-extension-policies create folder-test-extension-policy \
      --folder=folders/123456 \
      --zone=us-central1-f \
      --extensions=ops-agent \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
      --priority=500 \
      --inclusion-labels=env=prod

###  REST 

To create a folder-scoped zonal VM extension policy, send a `POST` request to the [`folderZoneVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/folderZoneVmExtensionPolicies/insert). This method defines which extensions to install and on which VMs in a specific zone across the folder.
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/folders/FOLDER_ID/zones/ZONE/vmExtensionPolicies
    
    {
    "name": "POLICY_NAME",
    "description": "DESCRIPTION",
    "extensionPolicies": {
       "EXTENSION_NAME_1": {
         "stringConfig": "EXTENSION_NAME_1_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_1_VERSION"
      },
       "EXTENSION_NAME_2": {
         "stringConfig": "EXTENSION_NAME_2_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_2_VERSION"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "KEY_1": "VALUE_1"
           }
        }
      }
    ],
    "priority": "PRIORITY"
    }
    

Replace the following:

  * `FOLDER_ID`: your folder ID.
  * `ZONE`: the zone where this policy applies.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone across all descendant projects within the folder.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



#### Example: Create a folder-scoped zonal policy

The following example creates a policy named `folder-test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for folder `123456`.
    
    
    POST https://compute.googleapis.com/compute/2026-10-01-preview/folders/123456/zones/us-central1-f/vmExtensionPolicies
    
    {
    "name": "folder-test-extension-policy",
    "description": "Test extension policy for Ops Agent at folder level",
    "extensionPolicies": {
       "ops-agent": {
         "stringConfig": "logging:
          receivers:
            systemd_logs:
              type: systemd_journald
          service:
            pipelines:
              systemd_pipeline:
                receivers: [systemd_logs]",
         "pinnedVersion": "2.58.0"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "env": "test"
           }
        }
      }
    ],
    "priority": "500"
    }
    

### Install VM extensions in a zone in a project

Create a project-scoped zonal extension policy to install and maintain VM extensions in a specific zone in your project.

#### Required IAM permissions

To get the permission that you need to create a project-scoped extension policy, ask your administrator to grant you the [](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin)[Compute VM extension policies admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.vmExtensionPolicies.create` permission, which is required to create a project-scoped extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To create a project-scoped zonal extension policy, select one of the following options:

###  Console 

To create a project-scoped zonal VM extension policy in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create extension policy**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is `1000`.
  6. In the **Scope** section, select **Zonal rollout**.
  7. In the **Region** and **Zone** lists, select the region and zone where your VMs are located. VM Extension Manager applies the policy to the VMs in the selected region and zone.
  8. In the **Manage extensions** section, click **Add extension** and do the following for each extension that you want to install on the target VMs: 
     1. From the **Extension** list, select an extension. For more information, see [Supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions).
     2. From the **Version** list, specify the version number of the extension. Leave blank to select the latest version. 
        * For Ops Agent, you can specify version `2.58.0` or later.
        * For Extension for SAP and Extension for Compute Workloads, leave the field blank to select the latest version.
     3. Optional: In the **Config file content** field, enter configuration parameters for the extension.
  9. In the **Target VM instances** section, select the VMs for the policy. To select VMs with specific labels, click **Add labels** and add the key-value pair.
  10. Click **Create**.



###  gcloud 

To create a project-scoped zonal VM extension policy and roll out the policy to VMs in a specific zone, use the [`gcloud compute zone-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create):
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `PROJECT_ID`: the project ID for the project-scoped policy.
  * `ZONE`: the zone where this policy applies.
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



The command fails if a policy with the specified name already exists in the zone.

#### Example: Create a project-scoped zonal policy

The following command creates a policy named `test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for project `test-project`. The `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent.
    
    
    gcloud compute zone-vm-extension-policies create test-extension-policy \
      --project=test-project \
      --zone=us-central1-f \
      --extensions=ops-agent \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml"

#### Example: Create a project-scoped zonal policy with inclusion labels and priority

The following command creates a policy named `test-extension-policy-2` that installs the `ops-agent` extension in zone `us-central1-f` for project `test-project` on VMs with label `env=prod`. The policy priority is set to `500`, and the `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent.
    
    
    gcloud compute zone-vm-extension-policies create test-extension-policy-2 \
      --project=test-project \
      --zone=us-central1-f \
      --extensions=ops-agent \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
      --priority=500 \
      --inclusion-labels=env=prod

###  REST 

To create a project-scoped zonal VM extension policy, send a `POST` request to the [`zoneVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/insert). This method defines which extensions to install and on which VMs in a specific zone.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies
    
    {
    "name": "POLICY_NAME",
    "description": "DESCRIPTION",
    "extensionPolicies": {
       "EXTENSION_NAME_1": {
         "stringConfig": "EXTENSION_NAME_1_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_1_VERSION"
      },
       "EXTENSION_NAME_2": {
         "stringConfig": "EXTENSION_NAME_2_CONFIG",
         "pinnedVersion": "EXTENSION_NAME_2_VERSION"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "KEY_1": "VALUE_1"
           }
        }
      }
    ],
    "priority": "PRIORITY"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where this policy applies.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. You can specify any of the following supported extensions: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available. **Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, VM Extension Manager supports only the latest version.
  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone within your project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs.



#### Example: Create a project-scoped zonal policy

The following example creates a policy named `test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for `my-project`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/vmExtensionPolicies
    
    {
    "name": "test-extension-policy",
    "description": "Test extension policy for Ops Agent",
    "extensionPolicies": {
       "ops-agent": {
         "stringConfig": "logging:
          receivers:
            systemd_logs:
              type: systemd_journald
          service:
            pipelines:
              systemd_pipeline:
                receivers: [systemd_logs]",
         "pinnedVersion": "2.58.0"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
           "inclusionLabels": {
             "env": "test"
           }
        }
      }
    ],
    "priority": "500"
    }
    

## What's next

  * To inspect rollout progress and extension health status, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).
  * To modify configuration settings, change pinned versions, or remove deployed agents, see [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions).
  * To build Cloud Monitoring dashboards and set up alerts for agent health, CPU, and memory usage, see [Monitor VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/monitor-vm-extensions).
  * To diagnose failed rollouts, check running guest processes, or inspect guest agent debug logs, see [Troubleshoot VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
