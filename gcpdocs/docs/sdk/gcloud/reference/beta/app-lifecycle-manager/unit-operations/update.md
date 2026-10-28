---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/update/
title: gcloud beta app-lifecycle-manager unit-operations update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:55.652389+00:00
---

# gcloud beta app-lifecycle-manager unit-operations update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager unit-operations update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager unit-operations update - update a unit operation 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager unit-operations update` `UNIT_OPERATION` [`--cancel`] [`--location`=`LOCATION`] [`--schedule-start-time`=`SCHEDULE_START_TIME`] [`--clear-parent-unit-operation` | `--parent-unit-operation`=`PARENT_UNIT_OPERATION`] [`--clear-rollout` | `--rollout`=`ROLLOUT`] [`--deprovision` | `--flag-update`=`FLAG_UPDATE` | `--provision` `--clear-provision-release` | `--provision-release`=`PROVISION_RELEASE` `--provision-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`] | `--add-provision-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`] `--clear-provision-input-variables` | `--remove-provision-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`] | `--upgrade` `--clear-upgrade-release` | `--upgrade-release`=`UPGRADE_RELEASE` `--upgrade-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`] | `--add-upgrade-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`] `--clear-upgrade-input-variables` | `--remove-upgrade-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an App Lifecycle Manager unit operation. 

Use `--cancel` to request cancellation of a unit operation. 

EXAMPLES
     To request cancellation of the unit operation named `my-unit-operation` in location `us-central1`, run: 
    
    
    gcloud beta app-lifecycle-manager unit-operations update my-unit-operation --location=us-central1 --cancel

To reschedule the unit operation named `my-unit-operation` to start at `2099-01-02T10:00:00Z` and add or update the label `env=prod`, run: 
    
    
    gcloud beta app-lifecycle-manager unit-operations update my-unit-operation --location=us-central1 --schedule-start-time=2099-01-02T10:00:00Z --update-labels=env=prod

POSITIONAL ARGUMENTS
    

UnitOperation resource - Unit operation to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `unit_operation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `unit_operation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`UNIT_OPERATION`
     ID of the unitOperation or fully qualified identifier for the unitOperation. 

To set the `unit_operation` attribute: 

  * provide the argument `unit_operation` on the command line. 


FLAGS
    

`--cancel`
     Attempt to cancel the operation. Cancellation might fail if the operation is already running. 
`--location`=`LOCATION`
     For resources [flag-update, parent-unit-operation, provision-release, rollout, unit_operation, upgrade-release], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Time specification to schedule the operation. 
`--schedule-start-time`=`SCHEDULE_START_TIME`
     Start time of the operation. If not set, the start of the next maintenance window is used. 
Update parent_unit_operation. 

At most one of these can be specified: 

`--clear-parent-unit-operation`
     Clear parent_unit_operation value and set to null. 
ParentUnitOperation resource - Set parent_unit_operation to new value. 

Parent unit operation. If an operation creates child operations as part of its workflow, set this flag on each child operation to the parent unit operation for tracing. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--parent-unit-operation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--parent-unit-operation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--parent-unit-operation`=`PARENT_UNIT_OPERATION`
     ID of the parentUnitOperation or fully qualified identifier for the parentUnitOperation. 

To set the `unit-operation` attribute: 

  * provide the argument `--parent-unit-operation` on the command line. 


Update rollout. 

At most one of these can be specified: 

`--clear-rollout`
     Clear rollout value and set to null. 
RolloutId resource - Set rollout to new value. 

Rollout that created this unit operation. The rollout cannot be changed after it is set and is used only for filtering. If a dependent unit and unit operation are created as part of another unit operation, they use the same rollout. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--rollout` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--rollout` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--rollout`=`ROLLOUT`
     ID of the rolloutId or fully qualified identifier for the rolloutId. 

To set the `rollout` attribute: 

  * provide the argument `--rollout` on the command line. 


Unit operation type. 

At most one of these can be specified: 

Deprovision operation, which deprovisions the underlying resources represented by the unit. The operation can run only if the unit is provisioned. 
`--deprovision`
     Deprovision the unit. 
Flag update operation, which pushes new flag values to units. 
FlagRelease resource - Flag release applied by the unit operation. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--flag-update` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--flag-update` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--flag-update`=`FLAG_UPDATE`
     ID of the flagRelease or fully qualified identifier for the flagRelease. 

To set the `flag-release` attribute: 

  * provide the argument `--flag-update` on the command line. 


Provision operation, which provisions the underlying resources represented by the unit. The operation can run only if the unit is not provisioned. 
`--provision`
     Provision the unit. 
Update provision_release. 

At most one of these can be specified: 

`--clear-provision-release`
     Clear provision_release value and set to null. 
Release resource - Set provision_release to new value. 

Release to use for the unit. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--provision-release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--provision-release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--provision-release`=`PROVISION_RELEASE`
     ID of the release or fully qualified identifier for the release. 

To set the `release` attribute: 

  * provide the argument `--provision-release` on the command line. 


Update provision_input_variables. 

At most one of these can be specified: 

`--provision-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Set provision_input_variables to new value. Input variables for the provision operation. A maximum of 100 input variables can be specified. 

`type`
     Name of a supported variable type. Supported types are `string`, `int`, `bool`, `struct`, and `list`. 
`value`
     String-encoded value for the variable. Values of type `struct` or `list` must be JSON-encoded strings. 
`variable`
     Required, Name of the variable from the actuation configuration. 
`Shorthand Example:`
    
    
    --provision-input-variables=type=string,value=string,variable=string --provision-input-variables=type=string,value=string,variable=string

`JSON Example:`
    
    
    --provision-input-variables='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --provision-input-variables=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-provision-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Add new value to provision_input_variables list. Input variables for the provision operation. A maximum of 100 input variables can be specified. 

`type`
     Name of a supported variable type. Supported types are `string`, `int`, `bool`, `struct`, and `list`. 
`value`
     String-encoded value for the variable. Values of type `struct` or `list` must be JSON-encoded strings. 
`variable`
     Required, Name of the variable from the actuation configuration. 
`Shorthand Example:`
    
    
    --add-provision-input-variables=type=string,value=string,variable=string --add-provision-input-variables=type=string,value=string,variable=string

`JSON Example:`
    
    
    --add-provision-input-variables='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --add-provision-input-variables=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-provision-input-variables`
     Clear provision_input_variables value and set to empty list. 
`--remove-provision-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Remove existing value from provision_input_variables list. Input variables for the provision operation. A maximum of 100 input variables can be specified. 

`type`
     Name of a supported variable type. Supported types are `string`, `int`, `bool`, `struct`, and `list`. 
`value`
     String-encoded value for the variable. Values of type `struct` or `list` must be JSON-encoded strings. 
`variable`
     Required, Name of the variable from the actuation configuration. 
`Shorthand Example:`
    
    
    --remove-provision-input-variables=type=string,value=string,variable=string --remove-provision-input-variables=type=string,value=string,variable=string

`JSON Example:`
    
    
    --remove-provision-input-variables='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --remove-provision-input-variables=path_to_file.(yaml|json)

Upgrade operation, which upgrades a provisioned unit, possibly including the underlying resources represented by the unit. The operation can run only if the unit is provisioned. 
`--upgrade`
     Upgrade the unit. 
Update upgrade_release. 

At most one of these can be specified: 

`--clear-upgrade-release`
     Clear upgrade_release value and set to null. 
Release resource - Set upgrade_release to new value. 

Release to use for the unit. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--upgrade-release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--upgrade-release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--upgrade-release`=`UPGRADE_RELEASE`
     ID of the release or fully qualified identifier for the release. 

To set the `release` attribute: 

  * provide the argument `--upgrade-release` on the command line. 


Update upgrade_input_variables. 

At most one of these can be specified: 

`--upgrade-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Set upgrade_input_variables to new value. Input variables for the upgrade operation. A maximum of 100 input variables can be specified. 

`type`
     Name of a supported variable type. Supported types are `string`, `int`, `bool`, `struct`, and `list`. 
`value`
     String-encoded value for the variable. Values of type `struct` or `list` must be JSON-encoded strings. 
`variable`
     Required, Name of the variable from the actuation configuration. 
`Shorthand Example:`
    
    
    --upgrade-input-variables=type=string,value=string,variable=string --upgrade-input-variables=type=string,value=string,variable=string

`JSON Example:`
    
    
    --upgrade-input-variables='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --upgrade-input-variables=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-upgrade-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Add new value to upgrade_input_variables list. Input variables for the upgrade operation. A maximum of 100 input variables can be specified. 

`type`
     Name of a supported variable type. Supported types are `string`, `int`, `bool`, `struct`, and `list`. 
`value`
     String-encoded value for the variable. Values of type `struct` or `list` must be JSON-encoded strings. 
`variable`
     Required, Name of the variable from the actuation configuration. 
`Shorthand Example:`
    
    
    --add-upgrade-input-variables=type=string,value=string,variable=string --add-upgrade-input-variables=type=string,value=string,variable=string

`JSON Example:`
    
    
    --add-upgrade-input-variables='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --add-upgrade-input-variables=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-upgrade-input-variables`
     Clear upgrade_input_variables value and set to empty list. 
`--remove-upgrade-input-variables`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Remove existing value from upgrade_input_variables list. Input variables for the upgrade operation. A maximum of 100 input variables can be specified. 

`type`
     Name of a supported variable type. Supported types are `string`, `int`, `bool`, `struct`, and `list`. 
`value`
     String-encoded value for the variable. Values of type `struct` or `list` must be JSON-encoded strings. 
`variable`
     Required, Name of the variable from the actuation configuration. 
`Shorthand Example:`
    
    
    --remove-upgrade-input-variables=type=string,value=string,variable=string --remove-upgrade-input-variables=type=string,value=string,variable=string

`JSON Example:`
    
    
    --remove-upgrade-input-variables='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --remove-upgrade-input-variables=path_to_file.(yaml|json)

Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. Labels on the resource, which can be used for categorization, similar to Kubernetes resource labels. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. Labels on the resource, which can be used for categorization, similar to Kubernetes resource labels. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `saasservicemgmt/v1beta1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/app-lifecycle-manager>
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
