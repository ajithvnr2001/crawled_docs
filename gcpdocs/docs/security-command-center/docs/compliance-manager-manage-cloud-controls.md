---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls/
title: Manage cloud controls \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T06:14:26.454201+00:00
---

# Manage cloud controls  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Manage cloud controls Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Compliance Manager includes many built-in cloud controls that you can add to frameworks and deploy in your environment. If required, you can create and manage your own custom cloud controls and update built-in cloud controls.

**Note:** Custom cloud controls are exclusive to Premium and Enterprise [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers). 

## Before you begin

Complete these tasks before you complete the remaining tasks on this page.

### Set up permissions

  * To get the permissions that you need to manage cloud controls frameworks, ask your administrator to grant you the following IAM roles on your organization or project: 

    * [Compliance Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.admin) (`roles/cloudsecuritycompliance.admin`)
    * To create or modify cloud controls that are based on organization policies, one of: 
      * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
      * [Assured Workloads Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)
      * [Assured Workloads Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)
    * To create or modify cloud controls that are based on project policies: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Set up Google Cloud CLI

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

To set up the gcloud CLI to use service account impersonation to authenticate to Google APIs, rather than your user credentials, run the following command: 
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL

For more information, see [Service account impersonation](https://docs.cloud.google.com/security-command-center/docs/reference/authentication#sa-impersonation). 

## View cloud controls

Complete the following steps to view built-in cloud controls and any custom cloud controls that you already created.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The available cloud controls display.

The dashboard includes information about which frameworks include the cloud control and the number of resources (organization, folders, and projects) that the cloud control is applied to.

  4. To view details about a cloud control, click the control name.




###  CLI 

You can see information about a specific cloud control or list all the cloud controls in your organization.

### See details about a cloud control

To see details about a specific cloud control, run the `gcloud compliance-manager cloud-controls describe` command:
    
    
    gcloud compliance-manager cloud-controls describe CLOUD_CONTROL \
       --location=LOCATION \
       --organization=ORGANIZATION \
       [--major-revision-id=MAJOR_REVISION_ID]
    

Replace the following values:

  * `CLOUD_CONTROL`: the name of the cloud control

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud control is stored in

  * `MAJOR_REVISION_ID` is an optional flag that specifies which version of the cloud control to view. If you don't include the flag, the latest version is returned.




For example, to view a cloud control with the name `builtin-block-external-ip-addresses-for-vm-access` and the major revision number `1`, run the following:
    
    
    gcloud compliance-manager cloud-controls describe \
       builtin-block-external-ip-addresses-for-vm-access \
       --organization=3589215982 \
       --location=global \
       --major-revision-id=1
    

For more information, see [gcloud compliance-manager cloud-controls describe](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/describe).

### Get list of cloud controls

To get the list of cloud controls in your organization, run the `gcloud compliance-manager cloud-controls list` command:
    
    
    gcloud compliance-manager cloud-controls list \
       --location=LOCATION \
       --organization=ORGANIZATION
    

Replace the following values:

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud controls are stored in




For example, to view all cloud controls within organization `3589215982` and stored in the global location, run the following:
    
    
    gcloud compliance-manager cloud-controls list \
       --organization=3589215982 \
       --location=global
    

For information about optional flags, see [gcloud compliance-manager cloud-controls list](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/list).

## Create a custom cloud control

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When you create a custom cloud control, you apply a rule to any Cloud Asset Inventory [resource type](https://docs.cloud.google.com/asset-inventory/docs/asset-types#resource-types).

###  Console 

When using the console, you can create custom cloud controls with one rule that applies to one Cloud Asset Inventory resource type.

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The list of available cloud controls are displayed.

  4. Create a cloud control, either with Gemini or manually:




###  Use Gemini 

  1. Ask Gemini to generate a cloud control for you. Based on your prompt, Gemini provides a unique identifier, a name, associated detection logic, and possible remediation steps.

  2. Review the recommendations and make any required changes.

  3. Save your custom cloud control.




###  Create manually 

  1. In **Cloud control ID** , provide a unique identifier for your control.

  2. Enter a name and description to help users in your organization understand the purpose of the custom cloud control.

  3. Optional: Select the categories for the control. Click **Continue**.

  4. Select an available resource type for your custom cloud control. Compliance Manager supports all resource types. To find the name for a resource, see [Asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types).

  5. Provide the detection logic for your cloud control, in Common Expression Language (CEL) format.

CEL expressions let you define how you want to evaluate the properties of a resource. For more information and examples, see [Write rules for custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions). Click **Continue**.

If your evaluation rule isn't valid, an error is displayed.

  6. Select an appropriate findings severity.

  7. Write your remediation instructions so that incident responders and administrators in your organization can resolve any findings for the cloud control. Click **Continue**.

  8. Review your entries, and then click **Create**.




###  CLI 

When using the gcloud CLI, you can create a custom cloud control with a maximum of three rules. Each rule can apply to only one resource type.

To create a custom cloud control, run the `gcloud compliance-manager cloud-controls create` command:
    
    
    gcloud compliance-manager cloud-controls create CLOUD_CONTROL \
       --location=LOCATION \
       --organization=ORGANIZATION \
       [--display-name=DISPLAY_NAME] \
       [--description=DESCRIPTION] \
       [--categories=[CATEGORIES,...]] \
       [--finding-category=FINDING_CATEGORY] \
       [--parameter-spec=[defaultValue=DEFAULTVALUE],[description=DESCRIPTION],[displayName=DISPLAYNAME],[isRequired=ISREQUIRED],[name=NAME],[substitutionRules=SUBSTITUTIONRULES],[validation=VALIDATION],[valueType=VALUETYPE]] \
       [--remediation-steps=REMEDIATION_STEPS] \
       [--rules=[celExpression=CELEXPRESSION],[description=DESCRIPTION],[ruleActionTypes=RULEACTIONTYPES]] \
       [--severity=SEVERITY] \
       [--supported-cloud-providers=[SUPPORTED_CLOUD_PROVIDERS,…]] \
       [--supported-target-resource-types=[SUPPORTED_TARGET_RESOURCE_TYPES,…]]
    

Replace the following values:

  * `CLOUD_CONTROL`: a unique alphanumeric name for the cloud control

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud control is stored in

  * `DISPLAY_NAME`: a human-readable name for the cloud control

  * `DESCRIPTION`: an optional description of the purpose of the cloud control

  * `CATEGORIES,…`: an optional parameter that defines the categories that the cloud control is part of. For a list of permitted categories, see [gcloud compliance-manager cloud-controls create](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/create).

  * `FINDING_CATEGORY`: the value that shows in the Security Command Center findings dashboard when the cloud control generates a finding

  * --parameter-spec=[defaultValue=DEFAULTVALUE], \
         [description=DESCRIPTION], \
         [displayName= DISPLAYNAME], \
         [isRequired=ISREQUIRED], \
         [name=NAME], \
         [substitutionRules=SUBSTITUTIONRULES], \
         [validation=VALIDATION], \
         [valueType=VALUETYPE]...]
        

is the optional parameter information for the cloud control, in the following format:

    * `DEFAULTVALUE`: the data that is applied if a user doesn't customize the parameter when deploying a framework. Supported value types are `boolValue`, `numberValue`, `stringListValue`, or `stringValue`.

    * `DESCRIPTION`: an optional description of the control

    * `ISREQUIRED`: `true` if the control requires a parameter to be set

    * `NAME`: the name of the parameter

    * `SUBSTITUTIONRULES`: how and where Compliance Manager injects the custom value for the parameter. Specify the targeted path inside the rule using a proto dot notation (for example, `rules[0].org_policy_constraint...`) Choose one of the following options:

      * `attributeSubstitutionRule` when you want to inject the parameter value directly into a structural field of your rule (for example, filling a list of restricted values inside an organization policy constraint rule template).

      * `placeholderSubstitutionRule` when your rule uses a text string (or CEL expression). The string must contain a placeholder variable that's prefixed with `$` (for example, `$deniedServices`), and this rule tells the compiler to map the parameter to that placeholder.

The following example creates a list parameter named `deniedServices` with the `STRINGLIST` type. It uses `attributeSubstitutionRule` to add user-provided service names (such as `compute.googleapis.com`) directly into a structural custom organization policy rule (`denied_values`) when deployed:
    
    --parameter-spec='name=deniedServices,isRequired=true,valueType=STRINGLIST,substitutionRules=[{attributeSubstitutionRule={attribute="rules[0].org_policy_constraint.policy_rules[0].values.denied_values"}}]'

    * `VALIDATION` is the permitted set of values. Choose one of the following options:

      * Use `allowedValues` to enforce a static allowlist—for example, limit location parameters to specific string fields: `validation={allowedValues={values=[{stringValue=us-central1},{stringValue=us-west1}]}}`

      * Use `intRange` to enforce numeric bounds on integers—for example, set a retention period between 1 and 365: `validation={intRange={min=1,max=365}}`

      * Use `regexpPattern` to enforce regular expression matching on string text—for example, require strict alphanumeric naming: `validation={regexpPattern={pattern="^[a-z][-a-z0-9]*$"}}`

    * `VALUETYPE`: the data type or format of the value that a user provides for this parameter. Supported value types are `STRING`, `BOOLEAN`, `STRINGLIST`, `NUMBER`, and `ONEOF`.

Alternatively, you can specify a JSON or YAML file that defines the parameters. For example, `--parameter-spec=path_to_file.(yaml|json)`. Expand the following section to view example JSON and YAML files.

#### Example JSON file
    
    [
        {
          "name": "deniedServices",
          "displayName": "Services Requiring CMEK",
          "description": "List of service names that must use Customer-Managed Encryption Keys.",
          "isRequired": true,
          "valueType": "STRINGLIST",
          "substitutionRules": [
            {
              "attributeSubstitutionRule": {
                "attribute": "rules[0].org_policy_constraint.policy_rules[0].values.denied_values"
              }
            }
          ]
        }
      ]
          

#### Example YAML file
    
    - name: deniedServices
        displayName: "Services Requiring CMEK"
        description: "List of service names that must use Customer-Managed Encryption Keys."
        isRequired: true
        valueType: STRINGLIST
        substitutionRules:
        - attributeSubstitutionRule:
            attribute: "rules[0].org_policy_constraint.policy_rules[0].values.denied_values"
          

  * REMEDIATION_STEPS: the steps required to resolve any findings. This string is limited to 400 characters.

  * `--rules=[celExpression=CELEXPRESSION],[description=DESCRIPTION],[ruleActionTypes=RULEACTIONTYPES]` is the rule that you want to enforce, in the following format:

    * `CELEXPRESSION`: the common expression language (CEL) expression of the rule. For information about writing CEL expressions, see [Write rules for custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions). Include the following:

      * `expression`: the CEL expression, with a maximum of 1000 characters

      * `resourceTypesValues`: the name of the resources, in the format `SERVICE_NAME/type`. Use a `values` array to list all your resource types that you want to apply the rule to—for example, `values=[compute.googleapis.com/Instance]`.

    * `DESCRIPTION`: a description of the rule

    * `RULEACTIONTYPES`: the action that the rule performs. Supported values are `rule-action-type-detective`, `rule-action-type-preventive`, and `rule-action-type-audit`.

For example, to check the Cloud Key Management Service key rotation period, enter the following:
    
    --rules="[
      {
        \"celExpression\": {
          \"expression\": \"has(resource.data.rotationPeriod) && resource.data.rotationPeriod < duration('60h')\",
          \"resourceTypesValues\": {
            \"values\": [
              \"cloudkms.googleapis.com/CryptoKey\"
            ]
          }
        },
        \"description\": \"Check KMS key rotation period\",
        \"ruleActionTypes\": [
          \"rule-action-type-detective\"
        ]
      }
    ]"
    

Alternatively, you can specify a JSON or YAML file that defines the rule. For example, `--rules=path_to_file.(yaml|json)`. Expand the following section to view example JSON and YAML files.

#### Example JSON file
    
    [
        {
          "celExpression": {
            "expression": "has(resource.data.rotationPeriod) && resource.data.rotationPeriod < duration('60h')",
            "resourceTypesValues": {
              "values": [
                "cloudkms.googleapis.com/CryptoKey"
              ]
            }
          },
          "description": "Check KMS key rotation period to ensure it is under 60 hours.",
          "ruleActionTypes": [
            "rule-action-type-detective"
          ]
        }
      ]
          

#### Example YAML file
    
    - celExpression:
          expression: "has(resource.data.rotationPeriod) && resource.data.rotationPeriod < duration('60h')"
          resourceTypesValues:
            values:
            - cloudkms.googleapis.com/CryptoKey
        description: "Check KMS key rotation period to ensure it is under 60 hours."
        ruleActionTypes:
        - rule-action-type-detective
          

  * `SEVERITY`: the criticality level for the cloud control. Supported values are `critical`, `high`, `medium`, and `low`.

  * `SUPPORTED_CLOUD_PROVIDERS,…`: the cloud providers that this cloud control applies to. The only supported value is `gcp`.

  * `SUPPORTED_TARGET_RESOURCE_TYPES,…`: the resource types (organization, folder, project, or app-enabled folder in App Hub) that the cloud control supports. Supported values are `target-resource-crm-type-folder`, `target-resource-crm-type-org`, `target-resource-crm-type-project`, and `target-resource-type-application`.




For example, to create a cloud control that enforces resource locations, run the following command:
    
    
      gcloud compliance-manager cloud-controls create \
         restrict-resource-locations \
         --organization=3589215982 \
         --location=global \
         --display-name="Restrict Resource Locations" \
         --description="Enforces checks to ensure resources are only deployed in approved cloud regions." \
         --severity=high \
         --finding-category="LOCATION_VIOLATION" \
         --supported-cloud-providers="gcp" \
         --supported-target-resource-types="target-resource-crm-type-project" \
         --parameter-spec='name=allowedLocations,isRequired=true,valueType=STRINGLIST,substitutionRules=[{placeholderSubstitutionRule={attribute="rules[0].cel_expression.expression"}}]' \
         --rules="[{\"celExpression\": {\"expression\": \"resource.location in \$allowedLocations\", \"resourceTypesValues\": {\"values\": [\"compute.googleapis.com/Instance\"]}}, \"description\": \"Check Compute Engine instance locations\", \"ruleActionTypes\": [\"rule-action-type-detective\"]}]"
    

To create the same control but use YAML files to define the parameters and rules, run:
    
    
         gcloud compliance-manager cloud-controls create \
         restrict-resource-locations \
         --organization=3589215982 \
         --location=global \
         --display-name="Restrict Resource Locations" \
         --description="Enforces checks to ensure resources are only deployed in approved cloud regions." \
         --severity=high \
         --finding-category="LOCATION_VIOLATION" \
         --supported-cloud-providers="gcp" \
         --supported-target-resource-types="target-resource-crm-type-project" \
         --parameter-spec=parameters.yaml \
         --rules=rules.yaml
    

For more information, see [gcloud compliance-manager cloud-controls create](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/create).

###  Terraform 

When using Terraform, you can create a custom cloud control with a maximum of three rules. Each rule can apply to only one resource type.

The following sample shows how you can create a custom cloud control using Terraform.
    
    
    resource "google_cloud_security_compliance_cloud_control" "example" {
      parent              = "organizations/123456789"
      location            = "global"
      cloud_control_id    = "example-cloudcontrol"
    
      display_name      = "TF test CloudControl Name"
      description       = "A test cloud control for security compliance"
      categories        = ["CC_CATEGORY_INFRASTRUCTURE"]
      severity          = "HIGH"
      finding_category  = "SECURITY_POLICY"
      remediation_steps = "Review and update the security configuration according to best practices."
    
      supported_cloud_providers        = ["GCP"]
    
      rules {
        description         = "Ensure compute instances have secure boot enabled"
        rule_action_types   = ["RULE_ACTION_TYPE_DETECTIVE"]
    
        cel_expression {
          expression = "resource.data.shieldedInstanceConfig.enableSecureBoot == true"
          resource_types_values {
            values = ["compute.googleapis.com/Instance"]
          }
        }
      }
    
      parameter_spec {
        name         = "location"
        display_name = "Resource Location"
        description  = "The location where the resource should be deployed"
        value_type   = "STRING"
        is_required  = true
    
        default_value {
          string_value = "us-central1"
        }
    
        validation {
          regexp_pattern {
            pattern = "^[a-z]+-[a-z]+[0-9]$"
          }
        }
      }
    
      parameter_spec {
        name         = "enable_secure_boot"
        display_name = "Enable Secure Boot"
        description  = "Whether to enable secure boot for instances"
        value_type   = "BOOLEAN"
        is_required  = true
    
        default_value {
          bool_value = true
        }
    
        substitution_rules {
          attribute_substitution_rule {
            attribute = "rules[0].cel_expression.expression"
          }
        }
    
        validation {
          allowed_values {
            values {
              bool_value = true
            }
          }
        }
      }
    
      parameter_spec {
        name         = "max_instances"
        display_name = "Maximum Instances"
        description  = "Maximum number of instances allowed"
        value_type   = "NUMBER"
        is_required  = false
    
        default_value {
          number_value = 10
        }
    
        substitution_rules {
          placeholder_substitution_rule {
            attribute = "rules[0].description"
          }
        }
    
        validation {
          int_range {
            min = "1"
            max = "100"
          }
        }
      }
    
      parameter_spec {
        name         = "allowed_regions"
        display_name = "Allowed Regions"
        description  = "List of regions where resources can be deployed"
        value_type   = "STRINGLIST"
        is_required  = true
    
        default_value {
          string_list_value {
            values = ["us-central1", "us-east1", "us-west1"]
          }
        }
    
        validation {
          allowed_values {
            values {
              string_list_value {
                values = ["us-central1", "us-east1"]
              }
            }
            values {
              string_list_value {
                values = ["us-west1", "us-west2"]
              }
            }
          }
        }
      }
    
      parameter_spec {
        name         = "environment_type"
        display_name = "Environment Type"
        description  = "The type of environment"
        value_type   = "STRING"
        is_required  = true
    
        default_value {
          string_value = "production"
        }
    
        validation {
          allowed_values {
            values {
              string_value = "production"
            }
            values {
              string_value = "staging"
            }
            values {
              number_value = 1
            }
          }
        }
      }
    }
    

## Edit a custom cloud control

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

After you create a cloud control, you can change its name, description, rules, remediation steps, and severity level. You can't change the cloud control category.

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The list of available cloud controls display.

  4. Click the cloud control that you want to edit.

  5. In the **Cloud controls details** page, verify that the cloud control isn't included in a framework. If required, [edit the framework to remove the cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#update-custom-framework).

  6. Click **Edit**.

  7. In the **Edit custom cloud control** page, change the name and description as required. Click **Continue**.

  8. Update the rules, finding severity, and remediation steps. Click **Continue**.

  9. Review your changes and click **Save**.




## Update a built-in cloud control to a newer release

Google publishes regular updates to its built-in cloud controls as services deploy new features or as new best practices emerge. Updates can include new controls or changes to existing controls.

You can view the releases of built-in cloud controls in the cloud controls dashboard in the **Configure** tab or in the cloud control details page.

To update a cloud control after you receive a notification, you must update the deployed frameworks that include the cloud control. For instructions, see [Update a built-in framework to a newer release](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#update-framework-version).

## Delete a custom cloud control

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Delete a cloud control when it's no longer required. You can only delete cloud controls that you create. You can't delete built-in cloud controls.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The list of available cloud controls display.

  4. Click the cloud control that you want to delete.

  5. In the **Cloud controls details** page, verify that the cloud control isn't included in a framework. If required, [edit the framework to remove the cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#update-custom-framework).

  6. Click **Delete**.

  7. In the **Delete** window, review the message. Type `Delete` and click **Confirm**.




###  CLI 

To delete a custom cloud control, run the `gcloud compliance-manager cloud-controls delete` command:
    
    
    gcloud compliance-manager cloud-controls delete CLOUD_CONTROL \
       --location=LOCATION \
       --organization=ORGANIZATION
    

Replace the following values:

  * `CLOUD_CONTROL`: the name of the cloud control

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud control is stored in




For example, to delete a cloud control with the name `restrict-resource-locations`, run the following:
    
    
    gcloud compliance-manager cloud-controls delete \
       restrict-resource-locations \
       --organization=3589215982 \
       --location=global
    

For more information, see [gcloud compliance-manager cloud-controls delete](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/delete).

## Mapping of Security Health Analytics detectors to cloud controls

The following table shows how Compliance Manager cloud controls map to Security Health Analytics detectors.

Finding category in Security Health Analytics | Cloud control name in Compliance Manager  
---|---  
`ACCESS_TRANSPARENCY_DISABLED` | [Enable Access Transparency](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-access-transparency)  
`ADMIN_SERVICE_ACCOUNT` | [Block Administrator Roles from Service Accounts](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-admin-roles-from-service-accounts)  
`ALLOWED_INGRESS_ORG_POLICY` | [Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-cloud-run-ingress-settings-org-policy)  
`ALLOWED_VPC_EGRESS_ORG_POLICY` | [Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-cloud-run-egress-settings-org-policy)  
`ALLOYDB_AUTO_BACKUP_DISABLED` | [Enable AlloyDB Automated Backups on Cluster](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-alloydb-automated-backups)  
`ALLOYDB_BACKUPS_DISABLED` | [Enable AlloyDB Backups on Cluster](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-continuous-automated-backups)  
`ALLOYDB_CMEK_DISABLED` | [Enable CMEK for AlloyDB Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-cmek-for-alloydb-cluster)  
`ALLOYDB_LOG_ERROR_VERBOSITY` | [Set Log Error Verbosity Flag for AlloyDB Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-alloydb-log-error-verbosity-flag)  
`ALLOYDB_LOG_MIN_ERROR_STATEMENT_SEVERITY` | [Set Log Min Error Statement Flag for AlloyDB Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-alloydb-log-min-error-statement-flag)  
`ALLOYDB_LOG_MIN_MESSAGES` | [Set Log Min Messages Flag for AlloyDB Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-alloydb-log-min-messages-flag)  
`ALLOYDB_PUBLIC_IP` | [Block Public IP Addresses for AlloyDB Cluster Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-alloydb-public-ip-addresses)  
`ALLOYDB_SSL_NOT_ENFORCED` | [Enable SSL Encryption On AlloyDB Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-alloydb-ssl-encryption)  
`ALPHA_CLUSTER_ENABLED` | [Disable Alpha Features on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-alpha-features)  
`API_KEY_APIS_UNRESTRICTED` | [Restrict API Keys for Required APIs Only](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-api-keys-for-required-apis-only)  
`API_KEY_APPS_UNRESTRICTED` | [Set Application Restriction on API Keys](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-applications-api-keys)  
`API_KEY_EXISTS` | [Require API Key Exists](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#api-key-exists)  
`API_KEY_NOT_ROTATED` | [Require Rotation of API Key](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-api-key-rotation)  
`AUDIT_CONFIG_NOT_MONITORED` | [Configure Log Metrics and Alerts for Audit Logging Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metrics-for-audit-logging-changes)  
`AUDIT_LOGGING_DISABLED` | [Implement Event Logging for Google Cloud Services](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#implement-event-logging)  
`AUTO_BACKUP_DISABLED` | [Enable Automatic Backups for Cloud SQL Databases](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-automatic-backups-cloud-sql)  
`AUTO_REPAIR_DISABLED` | [Enable Auto Repair for GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-auto-repair)  
`AUTO_UPGRADE_DISABLED` | [Enable Auto Upgrade on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-auto-upgrade)  
`BIGQUERY_TABLE_CMEK_DISABLED` | [Enable CMEK for BigQuery Tables](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#cmek-key-in-use-for-bigquery-table)  
`BINARY_AUTHORIZATION_DISABLED` | [Require Binary Authorization on a Cluster](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-binary-authorization)  
`BUCKET_CMEK_DISABLED` | [Enable CMEK for Cloud Storage Buckets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-cmek-on-bucket)  
`BUCKET_IAM_NOT_MONITORED` | [Configure Log Metrics and Alerts for Cloud Storage IAM Policy Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metrics-for-bucket-iam-changes)  
`BUCKET_LOGGING_DISABLED` | [Require Cloud Storage Bucket Logging](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-bucket-logging)  
`BUCKET_POLICY_ONLY_DISABLED` | [Enable Uniform Bucket-Level Access on Cloud Storage Buckets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-uniform-bucket-level-access)  
`CLOUD_ASSET_API_DISABLED` | [Enable Cloud Asset Inventory Service](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-cloud-asset-api)  
`CLUSTER_LOGGING_DISABLED` | [Enable Cloud Logging on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-cluster-cloud-logging)  
`CLUSTER_MONITORING_DISABLED` | [Enable Cloud Monitoring on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-cluster-cloud-monitoring)  
`CLUSTER_PRIVATE_GOOGLE_ACCESS_DISABLED` | [Enable Private Google Access on an instance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-private-google-access)  
`CLUSTER_SECRETS_ENCRYPTION_DISABLED` | [Enable Encryption on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-encryption-gke-cluster)  
`CLUSTER_SHIELDED_NODES_DISABLED` | [Enable Shielded GKE Nodes on a Cluster](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-shielded-nodes)  
`COMPUTE_PROJECT_WIDE_SSH_KEYS_ALLOWED` | [Block Project-Wide SSH Keys on Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-project-wide-ssh-keys)  
`COMPUTE_SECURE_BOOT_DISABLED` | [Enable Secure Boot on Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-secure-boot-on-compute-engine-instances)  
`COMPUTE_SERIAL_PORTS_ENABLED` | [Block Serial Ports for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-serial-ports-on-compute-engine-instances)  
`CONFIDENTIAL_COMPUTING_DISABLED` | [Enable Confidential Computing for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-confidential-computing)  
`COS_NOT_USED` | [Require Container-Optimized OS for a GKE Cluster](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-container-optimized-os)  
`CUSTOM_ORG_POLICY_VIOLATION` | [Enforce Custom Organization Policy](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#custom-org-policy-violation-config)  
`CUSTOM_ROLE_NOT_MONITORED` | [Configure Log Metrics and Alerts for Custom Role Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metrics-for-custom-role-changes)  
`DATAPROC_CMEK_DISABLED` | [Require CMEK on Dataproc Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-cmek-on-dataproc-cluster)  
`DATAPROC_IMAGE_OUTDATED` | [Use Latest Image Versions on Dataproc Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-latest-image-version-on-dataproc-cluster)  
`DATASET_CMEK_DISABLED` | [Enable CMEK for BigQuery Datasets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-cmek-on-bigquery-datasets)  
`DEFAULT_NETWORK` | [Use Networks with Custom Firewall Rules](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-network-with-custom-firewall-rules)  
`DEFAULT_SERVICE_ACCOUNT_USED` | [Use Custom Service Accounts for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-non-default-service-account)  
`DISABLE_VPC_EXTERNAL_IP_V6_ORG_POLICY` | [Configure the Disable VPC External IPv6 Usage Organization Policy](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-external-ipv6-addresses-org-policy)  
`DISABLE_VPC_INTERNAL_IP_V6_ORG_POLICY` | [Configure the Disable VPC External IPv6 Usage Organization Policy](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-external-ipv6-addresses-org-policy)  
`DISABLED_SERIAL_PORT_ACCESS_ORG_POLICY` | [Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-serial-ports-logging-org-policy)  
`DISK_CMEK_DISABLED` | [Enable CMEK on Compute Engine Persistent Disks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-cmek-on-disk)  
`DISK_CSEK_DISABLED` | [Enable CSEK On Compute Engine Persistent Disks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-csek-on-disk)  
`DNS_LOGGING_DISABLED` | [Enable Cloud DNS Logs Monitoring](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-cloud-dns-logging)  
`DNSSEC_DISABLED` | [Enable DNSSEC for Cloud DNS](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-dnssec-for-cloud-dns)  
`EGRESS_DENY_RULE_NOT_SET` | [Enforce Deny All Egress Firewall Rule](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-deny-all-egress-firewall-policy)  
`ESSENTIAL_CONTACTS_NOT_CONFIGURED` | [Define Essential Contacts](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-essential-contacts)  
`FIREWALL_NOT_MONITORED` | [Configure Log Metrics and Alerts for VPC Network Firewall Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metrics-for-firewall-changes)  
`FIREWALL_RULE_LOGGING_DISABLED` | [Enable Firewall Rule Logging](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-firewall-rule-logging)  
`FLOW_LOGS_DISABLED` | [Enable Subnet Flow Logs](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-subnet-flowlogs)  
`FULL_API_ACCESS` | [Restrict API Access to Google Cloud APIs for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-access-to-cloud-apis)  
`HTTP_LOAD_BALANCER` | [Enforce HTTPS Traffic Only](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-https-traffic-only-policy)  
`INSTANCE_OS_LOGIN_DISABLED` | [Require OS Login on Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-instance-os-login)  
`INTEGRITY_MONITORING_DISABLED` | [Enable Integrity Monitoring on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-integrity-monitoring)  
`INTRANODE_VISIBILITY_DISABLED` | [Enable Intranode Visibility for GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-intranode-visibility)  
`IP_ALIAS_DISABLED` | [Enable IP Alias Range for GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-cluster-ip-alias-range)  
`IP_FORWARDING_ENABLED` | [Prevent IP Forwarding on Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#prevent-ip-forwarding)  
`KMS_KEY_NOT_ROTATED` | [Define Rotation Period for Cloud KMS Keys](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-cloud-kms-key-rotation-period)  
`KMS_PROJECT_HAS_OWNER` | Not available  
`KMS_PUBLIC_KEY` | [Block Public Access to Cloud KMS Keys](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-cloud-kms-cryptokeys-public-access)  
`KMS_ROLE_SEPARATION` | [Enforce Separation of Duties](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-separation-of-duties)  
`LEGACY_AUTHORIZATION_ENABLED` | [Block Legacy Authorization on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-legacy-authorization)  
`LEGACY_METADATA_ENABLED` | [Disable Legacy Metadata Server Endpoints on Compute Engine](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-legacy-metadata-endpoints)  
`LEGACY_NETWORK` | [Don't Use Legacy Networks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#delete-legacy-network)  
`LOAD_BALANCER_LOGGING_DISABLED` | [Enable Load Balancer Logging](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-load-balancer-logging)  
`LOCKED_RETENTION_POLICY_NOT_SET` | [Lock Storage Bucket Retention Policies](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-storage-bucket-locked-retention-policy)  
`LOG_NOT_EXPORTED` | [Configure Log Sinks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#configure-log-sinks)  
`MASTER_AUTHORIZED_NETWORKS_DISABLED` | [Enable Control Plane Authorized Networks on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-control-plane-authorized-networks)  
`MFA_NOT_ENFORCED` | [Enforce Two-Step Verification](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-mfa)  
`NETWORK_NOT_MONITORED` | [Configure Log Metrics and Alerts for VPC Network Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metrics-for-network-changes)  
`NETWORK_POLICY_DISABLED` | [Enable Network Policy on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-cluster-network-policy)  
`NODEPOOL_BOOT_CMEK_DISABLED` | [Enable CMEK on GKE Node Pool Boot Disks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-cmek-nodepool-boot-disk)  
`NODEPOOL_SECURE_BOOT_DISABLED` | [Enable Secure Boot for Shielded GKE Nodes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-nodepool-secure-boot)  
`NON_ORG_IAM_MEMBER` | [Block IAM Permissions for External Users](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-non-organization-users-iam-permissions)  
`OBJECT_VERSIONING_DISABLED` | [Enable Object Versioning on Buckets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-object-versioning-on-buckets)  
`OPEN_CASSANDRA_PORT` | [Block Generic Access to Cassandra Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-cassandra-ports)  
`OPEN_CISCOSECURE_WEBSM_PORT` | [Block Generic Access to CiscoSecure/WebSM Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-ciscosecure-websm-ports) Addresses   
`OPEN_DIRECTORY_SERVICES_PORT` | [Block Generic Access to Directory Services Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-directory-services-ports) Addresses   
`OPEN_DNS_PORT` | [Block Generic Access to DNS Ports from All IP Addresses](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-dns-ports)  
`OPEN_ELASTICSEARCH_PORT` | [Block Generic Access to Elasticsearch Ports from All IP Addresses](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-elasticsearch-ports)  
`OPEN_FIREWALL` | [Block Overly Permissive Firewall Rules](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-firewall-all-ip-addresses)  
`OPEN_FTP_PORT` | [Block Generic Access to FTP Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-ftp-ports)  
`OPEN_GROUP_IAM_MEMBER` | [Restrict Open Google Group Accounts](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-open-group-iam-roles)  
`OPEN_HTTP_PORT` | [Block Generic Access to HTTP Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-http-ports)  
`OPEN_LDAP_PORT` | [Block Generic Access to LDAP Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-ldap-ports)  
`OPEN_MEMCACHED_PORT` | [Block Generic Access to Memcached Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-memcached-ports)  
`OPEN_MONGODB_PORT` | [Block Generic Access to MongoDB Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-mongodb-ports)  
`OPEN_MYSQL_PORT` | [Block Generic Access to MySQL Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-mysql-ports)  
`OPEN_NETBIOS_PORT` | [Block Generic Access to NetBIOS Ports from All IP Addresses](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-netbios-ports)  
`OPEN_ORACLEDB_PORT` | [Block Generic Access to Oracle Database Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-oracle-db-ports)  
`OPEN_POP3_PORT` | [Block Generic Access to POP3 Server Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-pop3-server-ports)  
`OPEN_POSTGRESQL_PORT` | [Block Generic Access to PostgreSQL Server Ports from All IP Addresses](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-postgresql-ports)  
`OPEN_RDP_PORT` | [Block Generic Access to RDP Port](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-access-to-rdp-port)  
`OPEN_REDIS_PORT` | [Block Generic Access to Redis Server Ports from All IP Addresses](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-redis-server-ports)  
`OPEN_SMTP_PORT` | [Block Generic Access to SMTP Server Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-smtp-server-ports)  
`OPEN_SSH_PORT` | [Block Generic Access to SSH Port](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-access-to-ssh-port)  
`OPEN_TELNET_PORT` | [Block Generic Access to Telnet Server Ports](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-telnet-server-ports)  
`ORG_POLICY_CONFIDENTIAL_VM_POLICY` | [Enable the Confidential VM Organization Policy Constraint](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-confidential-vm-service)  
`ORG_POLICY_LOCATION_RESTRICTION` | [Enforce Location Restriction](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#location-restriction-orgpolicy-not-enforced)  
`OS_LOGIN_DISABLED` | [Enable OS Login for All Instances at Project Level](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-os-login-all-instances-project-level)  
`OVER_PRIVILEGED_ACCOUNT` | [Use Least Privilege Service Accounts for GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#use-least-privileges-service-accounts-gke)  
`OVER_PRIVILEGED_SCOPES` | [Create GKE Clusters with Limited Privileges](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#create-kubernetes-clusters-limited-service-account-scopes)  
`OVER_PRIVILEGED_SERVICE_ACCOUNT_USER` | [Block Administrator Roles from Service Accounts](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-admin-roles-from-service-accounts)  
`OWNER_NOT_MONITORED` | [Configure Log Metrics and Alerts for Project Owner Role Assignments and Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metric-alerts-for-ownership-changes)  
`POD_SECURITY_POLICY_DISABLED` | [Enable PodSecurityPolicies for GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-pod-security-policy-gke-cluster)  
`PRIMITIVE_ROLES_USED` | [Restrict Legacy IAM Roles](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-legacy-iam-roles)  
`PRIVATE_CLUSTER_DISABLED` | [Enable Private Clusters for GKE](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-private-clusters-kubernetes)  
`PRIVATE_GOOGLE_ACCESS_DISABLED` | [Enable Private Google Access for VPC Subnets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-private-google-access-subnets-vpc)  
`PUBLIC_BUCKET_ACL` | [Restrict Public Access to Cloud Storage Buckets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-cloud-storage-buckets)  
`PUBLIC_COMPUTE_IMAGE` | [Restrict Public Access to Compute Images](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-to-compute-images)  
`PUBLIC_DATASET` | [Restrict Public Access to BigQuery Datasets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-bigquery-datasets)  
`PUBLIC_IP_ADDRESS` | [Restrict Public IP Addresses to Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-compute-instances-public-ip-addresses)  
`PUBLIC_LOG_BUCKET` | [Restrict Public Access to Cloud Storage Buckets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-cloud-storage-buckets)  
`PUBLIC_SQL_INSTANCE` | [Restrict Public Access to Cloud SQL Database Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-cloud-sql-instance)  
`PUBSUB_CMEK_DISABLED` | [Encrypt Pub/Sub topic with CMEK](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#encrypt-pubsub-topic-cmek)  
`REDIS_ROLE_USED_ON_ORG` | [Assign Redis Role at Project Level](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#assign-redis-role-project-lvl)  
`RELEASE_CHANNEL_DISABLED` | [Subscribe a GKE Cluster to a Release Channel](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#subscribe-release-channel-gke-cluster)  
`REQUIRE_OS_LOGIN_ORG_POLICY` | [Enable OS Login](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-os-login)  
`REQUIRE_VPC_CONNECTOR_ORG_POLICY` | [Define VPC Connector Egress For Cloud Run Functions](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-vpc-connector-for-cloud-functions)  
`RESTRICT_AUTHORIZED_NETWORKS_ORG_POLICY` | [Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-restrict-authorised-networks-org-policy)  
`ROUTE_NOT_MONITORED` | [Configure Log Metrics and Alerts for VPC Route Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metrics-for-network-route-changes)  
`RSASHA1_FOR_SIGNING` | [Avoid RSASHA1 for DNSSEC Signing](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#avoid-rsasha1-cloud-dns)  
`S3_BUCKET_ACCESS_LOGGING_ENABLED_CLOUDTRAIL_S3_BUCKET` | Not available  
`S3_BUCKETS_CONFIGURED_BLOCK_PUBLIC_ACCESS_BUCKET_AND_ACCOUNT_SETTINGS` | Not available  
`SERVICE_ACCOUNT_KEY_NOT_ROTATED` | [Require Service Account Key Rotation](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-service-account-key-rotation)  
`SERVICE_ACCOUNT_ROLE_SEPARATION` | [Enforce Separation of Duties](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-separation-of-duties)  
`SHIELDED_VM_DISABLED` | [Enable Shielded VM for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-shielded-vm-compute-instances)  
`SKIP_DEFAULT_NETWORK_CREATION_ORG_POLICY` | [Restrict Default Network Creation for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-default-network-creation-for-compute-engine)  
`SQL_CMEK_DISABLED` | [Enable CMEK for Cloud SQL Databases](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#configure-cmek-cloud-sql-database)  
`SQL_CONTAINED_DATABASE_AUTHENTICATION` | [Turn Off Contained Database Authentication Flag for SQL Server](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#turn-off-contained-db-authentication-flag-sql-server)  
`SQL_CROSS_DB_OWNERSHIP_CHAINING` | [Turn Off Cross Database Ownership Chaining Flag for SQL Server](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-cross-db-ownership-chaining-sql-server)  
`SQL_EXTERNAL_SCRIPTS_ENABLED` | [Turn Off External Scripts Flag for SQL Server](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-external-scripts-db-flag-sql-server)  
`SQL_INSTANCE_NOT_MONITORED` | [Configure Log Metrics and Alerts for Cloud SQL Configuration Changes](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-log-metrics-for-sql-config-changes)  
`SQL_LOCAL_INFILE` | [Turn Off Local Infile Flag for MySQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-local-infile-db-flag-mysql)  
`SQL_LOG_CHECKPOINTS_DISABLED` | [Enable Log Checkpoints Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-checkpoint-db-flag-postgresql)  
`SQL_LOG_CONNECTIONS_DISABLED` | [Enable Log Connections Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-connections-db-flag-postgres)  
`SQL_LOG_DISCONNECTIONS_DISABLED` | [Enable Log Disconnections Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-disconnections-db-flag-postgres)  
`SQL_LOG_DURATION_DISABLED` | [Enable Log Duration Flag for PostgreSQL instance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-duration-db-flag-postgresql)  
`SQL_LOG_ERROR_VERBOSITY` | [Enable Log Error Verbosity Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-error-verbosity-db-flag-postgres)  
`SQL_LOG_EXECUTOR_STATS_ENABLED` | [Turn Off Log Executor Stats Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#turn-off-log-executor-stats-db-flag-postgresql)  
`SQL_LOG_HOSTNAME_ENABLED` | [Turn off Log Hostname Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#turn-off-log-hostname-db-flag-postgresql)  
`SQL_LOG_LOCK_WAITS_DISABLED` | [Enable Log Locks Wait Flag for PostgreSQL instance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-locks-wait-db-flag-postgresql)  
`SQL_LOG_MIN_DURATION_STATEMENT_ENABLED` | [Turn Off Log Min Duration Statement Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-log-min-duration-statement-db-flag-postgresql)  
`SQL_LOG_MIN_ERROR_STATEMENT` | [Enable Log Min Error Statement Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-min-error-statement-db-flag-postgres)  
`SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY` | [Enable Log Min Error Statement Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-min-error-statement-db-flag-postgres)  
`SQL_LOG_MIN_MESSAGE` | [Enable Log Min Messages Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-min-messages-db-flag-postgres)  
`SQL_LOG_PARSER_STATS_ENABLED` | [Turn off Log Parser Stats Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#turn-off-log-parser-stats-db-flag-postgresql)  
`SQL_LOG_PLANNER_STATS_ENABLED` | [Turn off Log Planner Stats Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#turn-off-log-planner-stats-flag-postgresql)  
`SQL_LOG_STATEMENT` | [Enable Log Statement Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-statement-db-flag-postgres)  
`SQL_LOG_STATEMENT_STATS_ENABLED` | [Turn off Log Statement Stats Flag for PostgreSQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#turn-off-log-statement-stats-db-flag-postgresql)  
`SQL_LOG_TEMP_FILES` | [Enable Log Temp Files Flag for PostgreSQL instance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-log-temp-files-db-flag-postgresql)  
`SQL_NO_ROOT_PASSWORD` | [Enforce Password for MySQL Database](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-password-mysql-db)  
`SQL_PUBLIC_IP` | [Block Public IP Addresses for Cloud SQL Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-cloud-sql-public-ip-addresses)  
`SQL_REMOTE_ACCESS_ENABLED` | [Turn Off Remote Access Flag for SQL Server](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-remote-access-db-flag-sql-server)  
`SQL_SKIP_SHOW_DATABASE_DISABLED` | [Enable Skip Show Database Flag for MySQL](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-skip-show-db-flag-mysql)  
`SQL_TRACE_FLAG_3625` | [Enable 3625 Trace Database Flag for SQL Server](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-3625-trace-db-flag-sql-server)  
`SQL_USER_CONNECTIONS_CONFIGURED` | [Don't Use User Connections Flag for SQL Server](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#dont-use-user-connections-db-flag-sql-server)  
`SQL_USER_OPTIONS_CONFIGURED` | [Don't Use User Options Flag for SQL Server](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#dont-use-user-options-db-flag-sql-server)  
`SQL_WEAK_ROOT_PASSWORD` | [Enforce Strong Passwords for Cloud SQL Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#sql-weak-root-password)  
`SSL_NOT_ENFORCED` | [Enforce SSL for all Incoming Database Connections](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-ssl-incoming-connections-database)  
`TOO_MANY_KMS_USERS` | [Limit KMS Crypto Keys Users to Three](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#limit-kms-crypto-keys-users)  
`UNIFORM_BUCKET_LEVEL_ACCESS_ORG_POLICY` | [Set Uniform Bucket Level Access for Cloud Storage Buckets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#set-uniform-bucket-level-access-cloud-storage-buckets)  
`USER_MANAGED_SERVICE_ACCOUNT_KEY` | [Restrict User Managed Service Account Keys](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-user-managed-service-account-keys)  
`VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED` | [Enable Flow Logs for VPC Subnet](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-vpc-flow-logs)  
`WEAK_SSL_POLICY` | [Restrict Insecure SSL Policies for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-insecure-ssl-policies-compute)  
`WEB_UI_ENABLED` | [Don't Use Kubernetes Web UI](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#disable-gke-web-ui)  
`WORKLOAD_IDENTITY_DISABLED` | [Enable Workload Identity Federation for GKE on clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-workload-identity-gke)  
  
## What's next

  * [Write rules for custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
