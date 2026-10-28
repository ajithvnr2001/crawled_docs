---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/update/
title: gcloud beta app-lifecycle-manager rollouts update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:56.818894+00:00
---

# gcloud beta app-lifecycle-manager rollouts update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager rollouts update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager rollouts update - update a rollout 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager rollouts update` (`ROLLOUT` : `--location`=`LOCATION`) [`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`] [`--unit-filter`=`UNIT_FILTER`] [`--clear-control` `--control-action`=`CONTROL_ACTION` `--[no-]retry-failed-operations`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an App Lifecycle Manager rollout. 

Use `--control-action` to pause, resume, or cancel a rollout. 

EXAMPLES
     To pause the rollout named `my-rollout` in location `us-central1`, run: 
    
    
    gcloud beta app-lifecycle-manager rollouts update my-rollout --location=us-central1 --control-action=pause

To resume the paused rollout named `my-rollout` without retrying its failed operations, run: 
    
    
    gcloud beta app-lifecycle-manager rollouts update my-rollout --location=us-central1 --control-action=run --no-retry-failed-operations

To cancel the rollout named `my-rollout` permanently, run: 
    
    
    gcloud beta app-lifecycle-manager rollouts update my-rollout --location=us-central1 --control-action=cancel

POSITIONAL ARGUMENTS
    

RolloutId resource - Rollout to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ROLLOUT`
     ID of the rolloutId or fully qualified identifier for the rolloutId. 

To set the `rollout` attribute: 

  * provide the argument `rollout` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location ID 

To set the `location` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`
     Strategy to use for executing this rollout. Supported values are `Google.Cloud.Simple.AllAtOnce`, `Google.Cloud.Simple.OneLocationAtATime`, `Google.Cloud.Progressive.Gradual.v1`, and `Google.Cloud.Progressive.SingleLocation.v1`. If not set when the rollout is created, the strategy from the rollout kind is used. 
`--unit-filter`=`UNIT_FILTER`
     Filter, in Common Expression Language (CEL) format, that selects the eligible units. The filter can only reduce, not expand, the scope of the rollout. If empty, the unit filter from the rollout kind is used. For more information about CEL, see <https://github.com/google/cel-spec>. 
Rollout control, which requests a change to the execution of the rollout, such as pausing or canceling it. Requests can only be made when the rollout is in a non-terminal state. 
`--clear-control`
     Set rollout.control back to default value. 
`--control-action`=`CONTROL_ACTION`
     Action to perform on the rollout. If no action is set, the rollout runs until it naturally reaches a terminal state. `CONTROL_ACTION` must be one of: 

`cancel`
     Cancel the rollout permanently. 
`pause`
     Pause the rollout until it is resumed (that is, until the `run` action is requested). 
`run`
     Run the rollout until it naturally reaches a terminal state. A rollout requested to run progresses through all natural rollout states, such as from running to succeeded or from running to failed. If errors that can be retried occur during the rollout, the rollout is paused by default and can be resumed by requesting the `run` action again. 
Action parameters. 
Parameters for the `run` action that control the behavior of the rollout when it is resumed from a paused state. By default, the rollout retries failed operations when resumed. Can be specified only when `--control-action=run`. 
`--[no-]retry-failed-operations`
     Retry failed operations when the rollout is resumed. Applies only if the rollout is paused. Use `--retry-failed-operations` to enable and `--no-retry-failed-operations` to disable. 
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
