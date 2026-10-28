---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollout-kinds/create/
title: gcloud beta app-lifecycle-manager rollout-kinds create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:35.182824+00:00
---

# gcloud beta app-lifecycle-manager rollout-kinds create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollout-kinds/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager rollout-kinds create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager rollout-kinds create - create a rollout kind 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager rollout-kinds create` `ROLLOUT_KIND` `--unit-kind`=`UNIT_KIND` [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`] [`--unit-filter`=`UNIT_FILTER`] [`--update-unit-kind-strategy`=`UPDATE_UNIT_KIND_STRATEGY`] [`--error-budget-allowed-count`=`ERROR_BUDGET_ALLOWED_COUNT` `--error-budget-allowed-percentage`=`ERROR_BUDGET_ALLOWED_PERCENTAGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create an App Lifecycle Manager rollout kind. 

A rollout kind describes the settings of rollout execution for the units of a unit kind, such as the orchestration strategy and error budget. 

EXAMPLES
     To create a rollout kind named `my-rollout-kind` for the unit kind `my-unit-kind` in location `us-central1`, run: 
    
    
    gcloud beta app-lifecycle-manager rollout-kinds create my-rollout-kind --location=us-central1 --unit-kind=my-unit-kind

To create a rollout kind named `my-rollout-kind` that rolls out to one location at a time, never updates the unit kind, and has the label `env=prod`, run: 
    
    
    gcloud beta app-lifecycle-manager rollout-kinds create my-rollout-kind --location=us-central1 --unit-kind=my-unit-kind --rollout-orchestration-strategy=Google.Cloud.Simple.OneLocationAtATime --update-unit-kind-strategy=never --labels=env=prod

To create a rollout kind named `my-rollout-kind` that pauses rollouts when more than 2 units fail in a location, run: 
    
    
    gcloud beta app-lifecycle-manager rollout-kinds create my-rollout-kind --location=us-central1 --unit-kind=my-unit-kind --error-budget-allowed-count=2

POSITIONAL ARGUMENTS
    

RolloutKindId resource - Rollout kind to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `rollout_kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `rollout_kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`ROLLOUT_KIND`
     ID of the rolloutKindId or fully qualified identifier for the rolloutKindId. 

To set the `rollout_kind` attribute: 

  * provide the argument `rollout_kind` on the command line. 


REQUIRED FLAGS
    

UnitKind resource - Unit kind that this rollout kind corresponds to. Rollouts stemming from this rollout kind target the units of this unit kind. The unit kind cannot be changed after the rollout kind is created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--unit-kind`=`UNIT_KIND`
     ID of the unitKind or fully qualified identifier for the unitKind. 

To set the `unit_kind` attribute: 

  * provide the argument `--unit-kind` on the command line. 


OPTIONAL FLAGS
    

`--labels`=[`LABELS`,…]
     Labels on the resource, which can be used for categorization, similar to Kubernetes resource labels. 

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

`--location`=`LOCATION`
     For resources [rollout_kind, unit-kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`
     Strategy to use for executing rollouts. Supported values are `Google.Cloud.Simple.AllAtOnce`, `Google.Cloud.Simple.OneLocationAtATime`, `Google.Cloud.Progressive.Gradual.v1`, and `Google.Cloud.Progressive.SingleLocation.v1`. 
`--unit-filter`=`UNIT_FILTER`
     Filter, in Common Expression Language (CEL) format, that selects the eligible units. The filter can only reduce, not expand, the scope of the rollout. For more information about CEL, see <https://github.com/google/cel-spec>. 
`--update-unit-kind-strategy`=`UPDATE_UNIT_KIND_STRATEGY`
     Strategy for updating the unit kind. By default, the unit kind is updated when the rollout starts. `UPDATE_UNIT_KIND_STRATEGY` must be one of: 

`never`
     Never update the unit kind. 
`on-start`
     Update the unit kind when the rollout starts. 
Error budget settings. 
Configuration for the error budget. If the number of failed units in a location exceeds the larger of `--error-budget-allowed-count` and `--error-budget-allowed-percentage` percent of the units, the rollout is paused. If not set, App Lifecycle Manager attempts to update all units, regardless of the number of failures. 
`--error-budget-allowed-count`=`ERROR_BUDGET_ALLOWED_COUNT`
     Maximum number of failed units allowed in a location without pausing the rollout. 
`--error-budget-allowed-percentage`=`ERROR_BUDGET_ALLOWED_PERCENTAGE`
     Maximum percentage of units allowed to fail in a location without pausing the rollout. Must be greater than 0 and at most 100. 
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
