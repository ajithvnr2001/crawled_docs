---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/update/
title: gcloud beta app-lifecycle-manager unit-kinds update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:56.147654+00:00
---

# gcloud beta app-lifecycle-manager unit-kinds update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager unit-kinds update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager unit-kinds update - update a unit kind 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager unit-kinds update` `UNIT_KIND` [`--location`=`LOCATION`] [`--saas`=`SAAS`] [`--app-params-group`=`APP_PARAMS_GROUP` `--clear-app-params` `--scope-type`=`SCOPE_TYPE`] [`--clear-default-release` | `--default-release`=`DEFAULT_RELEASE`] [`--dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`] | `--add-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`] `--clear-dependencies` | `--remove-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]] [`--input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] | `--add-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] `--clear-input-variable-mappings` | `--remove-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] | `--add-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] `--clear-output-variable-mappings` | `--remove-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an App Lifecycle Manager unit kind. 
EXAMPLES
     To set the default release of the unit kind named `my-unit-kind` in location `us-central1` to `my-release`, run: 
    
    
    gcloud beta app-lifecycle-manager unit-kinds update my-unit-kind --location=us-central1 --default-release=my-release

To add or update the label `env=prod` on the unit kind named `my-unit-kind` and remove its default release, run: 
    
    
    gcloud beta app-lifecycle-manager unit-kinds update my-unit-kind --location=us-central1 --update-labels=env=prod --clear-default-release

POSITIONAL ARGUMENTS
    

UnitKind resource - Unit kind to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `unit_kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `unit_kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`UNIT_KIND`
     ID of the unitKind or fully qualified identifier for the unitKind. 

To set the `unit_kind` attribute: 

  * provide the argument `unit_kind` on the command line. 


FLAGS
    

`--location`=`LOCATION`
     For resources [default-release, saas, unit_kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Saas resource - SaaS offering that defines the product (managed service) that the service producer manages with App Lifecycle Manager. The SaaS offering cannot be changed after it is set. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--saas` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--saas` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--saas`=`SAAS`
     ID of the saas or fully qualified identifier for the saas. 

To set the `saas` attribute: 

  * provide the argument `--saas` on the command line. 


Parameters for creating an App Hub application. 
`--app-params-group`=`APP_PARAMS_GROUP`
     Grouping used to construct the name of the App Hub application. Multiple unit kinds can specify the same group to use the same application across their respective units. Corresponds to `app_boundary_id` in the Application Design Center composite application template. Defaults to the name of the unit kind. 
`--clear-app-params`
     Set unitKind.appParams back to default value. 
Scope of the application. 
`--scope-type`=`SCOPE_TYPE`
     Scope type of the application. Corresponds to `scope` in the Application Design Center composite application template. Defaults to `type-regional`. `SCOPE_TYPE` must be one of: 

`type-global`
     Global scope. 
`type-regional`
     Regional scope. 
Update default_release. 

At most one of these can be specified: 

`--clear-default-release`
     Clear default_release value and set to null. 
Release resource - Set default_release to new value. 

Release to use by default when creating new units of this unit kind. If not specified, each new unit must explicitly reference the release to use for its creation. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--default-release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--default-release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--default-release`=`DEFAULT_RELEASE`
     ID of the release or fully qualified identifier for the release. 

To set the `release` attribute: 

  * provide the argument `--default-release` on the command line. 


Update dependencies. 

At most one of these can be specified: 

`--dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]
     Set dependencies to new value. Other unit kinds that this unit kind depends on. Dependencies are automatically provisioned if not found. A maximum of 10 dependencies can be specified. Dependencies cannot be changed after the unit kind is created. 

`alias`
     Alias for the dependency, used for input variable mapping. 
`unitKind`
     Unit kind of the dependency. 
`Shorthand Example:`
    
    
    --dependencies=alias=string,unitKind=string --dependencies=alias=string,unitKind=string

`JSON Example:`
    
    
    --dependencies='[{"alias": "string", "unitKind": "string"}]'

`File Example:`
    
    
    --dependencies=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]
     Add new value to dependencies list. Other unit kinds that this unit kind depends on. Dependencies are automatically provisioned if not found. A maximum of 10 dependencies can be specified. Dependencies cannot be changed after the unit kind is created. 

`alias`
     Alias for the dependency, used for input variable mapping. 
`unitKind`
     Unit kind of the dependency. 
`Shorthand Example:`
    
    
    --add-dependencies=alias=string,unitKind=string --add-dependencies=alias=string,unitKind=string

`JSON Example:`
    
    
    --add-dependencies='[{"alias": "string", "unitKind": "string"}]'

`File Example:`
    
    
    --add-dependencies=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-dependencies`
     Clear dependencies value and set to empty list. 
`--remove-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]
     Remove existing value from dependencies list. Other unit kinds that this unit kind depends on. Dependencies are automatically provisioned if not found. A maximum of 10 dependencies can be specified. Dependencies cannot be changed after the unit kind is created. 

`alias`
     Alias for the dependency, used for input variable mapping. 
`unitKind`
     Unit kind of the dependency. 
`Shorthand Example:`
    
    
    --remove-dependencies=alias=string,unitKind=string --remove-dependencies=alias=string,unitKind=string

`JSON Example:`
    
    
    --remove-dependencies='[{"alias": "string", "unitKind": "string"}]'

`File Example:`
    
    
    --remove-dependencies=path_to_file.(yaml|json)

Update input_variable_mappings. 

At most one of these can be specified: 

`--input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Set input_variable_mappings to new value. Input variables of this unit kind that are either retrieved from the output variables of a dependency or passed on to the input variables of a dependency. A maximum of 100 mappings can be specified. 

`from`
     Output variable of a dependency from which the variable gets its value. 

`dependency`
     Required, Alias of the dependency. 
`outputVariable`
     Required, Name of the output variable on the dependency. 
`to`
     Input variable of a dependency to which the value of the variable is passed on. 

`dependency`
     Required, Alias of the dependency that the variable passes its value to. 
`ignoreForLookup`
     If true, App Lifecycle Manager does not use the input variable as a lookup key when looking for an existing dependency unit. 
`inputVariable`
     Required, Name of the input variable on the dependency. 
`variable`
     Required, Name of the variable. 
`Shorthand Example:`
    
    
    --input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --input-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --input-variable-mappings=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Add new value to input_variable_mappings list. Input variables of this unit kind that are either retrieved from the output variables of a dependency or passed on to the input variables of a dependency. A maximum of 100 mappings can be specified. 

`from`
     Output variable of a dependency from which the variable gets its value. 

`dependency`
     Required, Alias of the dependency. 
`outputVariable`
     Required, Name of the output variable on the dependency. 
`to`
     Input variable of a dependency to which the value of the variable is passed on. 

`dependency`
     Required, Alias of the dependency that the variable passes its value to. 
`ignoreForLookup`
     If true, App Lifecycle Manager does not use the input variable as a lookup key when looking for an existing dependency unit. 
`inputVariable`
     Required, Name of the input variable on the dependency. 
`variable`
     Required, Name of the variable. 
`Shorthand Example:`
    
    
    --add-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --add-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --add-input-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --add-input-variable-mappings=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-input-variable-mappings`
     Clear input_variable_mappings value and set to empty list. 
`--remove-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Remove existing value from input_variable_mappings list. Input variables of this unit kind that are either retrieved from the output variables of a dependency or passed on to the input variables of a dependency. A maximum of 100 mappings can be specified. 

`from`
     Output variable of a dependency from which the variable gets its value. 

`dependency`
     Required, Alias of the dependency. 
`outputVariable`
     Required, Name of the output variable on the dependency. 
`to`
     Input variable of a dependency to which the value of the variable is passed on. 

`dependency`
     Required, Alias of the dependency that the variable passes its value to. 
`ignoreForLookup`
     If true, App Lifecycle Manager does not use the input variable as a lookup key when looking for an existing dependency unit. 
`inputVariable`
     Required, Name of the input variable on the dependency. 
`variable`
     Required, Name of the variable. 
`Shorthand Example:`
    
    
    --remove-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --remove-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --remove-input-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --remove-input-variable-mappings=path_to_file.(yaml|json)

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

Update output_variable_mappings. 

At most one of these can be specified: 

`--output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Set output_variable_mappings to new value. Output variables of this unit kind that are passed to the output variables of the unit. A maximum of 100 mappings can be specified. 

`from`
     Output variable of a dependency from which the variable gets its value. 

`dependency`
     Required, Alias of the dependency. 
`outputVariable`
     Required, Name of the output variable on the dependency. 
`to`
     Input variable of a dependency to which the value of the variable is passed on. 

`dependency`
     Required, Alias of the dependency that the variable passes its value to. 
`ignoreForLookup`
     If true, App Lifecycle Manager does not use the input variable as a lookup key when looking for an existing dependency unit. 
`inputVariable`
     Required, Name of the input variable on the dependency. 
`variable`
     Required, Name of the variable. 
`Shorthand Example:`
    
    
    --output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --output-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --output-variable-mappings=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Add new value to output_variable_mappings list. Output variables of this unit kind that are passed to the output variables of the unit. A maximum of 100 mappings can be specified. 

`from`
     Output variable of a dependency from which the variable gets its value. 

`dependency`
     Required, Alias of the dependency. 
`outputVariable`
     Required, Name of the output variable on the dependency. 
`to`
     Input variable of a dependency to which the value of the variable is passed on. 

`dependency`
     Required, Alias of the dependency that the variable passes its value to. 
`ignoreForLookup`
     If true, App Lifecycle Manager does not use the input variable as a lookup key when looking for an existing dependency unit. 
`inputVariable`
     Required, Name of the input variable on the dependency. 
`variable`
     Required, Name of the variable. 
`Shorthand Example:`
    
    
    --add-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --add-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --add-output-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --add-output-variable-mappings=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-output-variable-mappings`
     Clear output_variable_mappings value and set to empty list. 
`--remove-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Remove existing value from output_variable_mappings list. Output variables of this unit kind that are passed to the output variables of the unit. A maximum of 100 mappings can be specified. 

`from`
     Output variable of a dependency from which the variable gets its value. 

`dependency`
     Required, Alias of the dependency. 
`outputVariable`
     Required, Name of the output variable on the dependency. 
`to`
     Input variable of a dependency to which the value of the variable is passed on. 

`dependency`
     Required, Alias of the dependency that the variable passes its value to. 
`ignoreForLookup`
     If true, App Lifecycle Manager does not use the input variable as a lookup key when looking for an existing dependency unit. 
`inputVariable`
     Required, Name of the input variable on the dependency. 
`variable`
     Required, Name of the variable. 
`Shorthand Example:`
    
    
    --remove-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --remove-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --remove-output-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --remove-output-variable-mappings=path_to_file.(yaml|json)

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
