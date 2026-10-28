---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/create/
title: gcloud beta app-lifecycle-manager rollouts create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:57.086464+00:00
---

# gcloud beta app-lifecycle-manager rollouts create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager rollouts create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager rollouts create - create a rollout 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager rollouts create` `ROLLOUT` (`--flag-release`=`FLAG_RELEASE` | `--release`=`RELEASE`) [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--rollout-kind`=`ROLLOUT_KIND`] [`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`] [`--unit-filter`=`UNIT_FILTER`] [`--control-action`=`CONTROL_ACTION` : `--[no-]retry-failed-operations`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create an App Lifecycle Manager rollout. 

A rollout represents a single execution of rolling out a release to the target units, including its results. The rollout follows the settings of the rollout kind that it stems from. 

EXAMPLES
     To create a rollout named `my-rollout` in location `us-central1` that rolls out the release `my-release` according to the rollout kind `my-rollout-kind`, run: 
    
    
    gcloud beta app-lifecycle-manager rollouts create my-rollout --location=us-central1 --release=my-release --rollout-kind=my-rollout-kind

To create a rollout named `my-rollout` that rolls out the release `my-release` only to units that have the label `env=prod`, run: 
    
    
    gcloud beta app-lifecycle-manager rollouts create my-rollout --location=us-central1 --release=my-release --rollout-kind=my-rollout-kind --unit-filter="unit.labels['env'] == 'prod'"

To create a rollout named `my-rollout` that rolls out to all locations at once and has the label `env=prod`, run: 
    
    
    gcloud beta app-lifecycle-manager rollouts create my-rollout --location=us-central1 --release=my-release --rollout-kind=my-rollout-kind --rollout-orchestration-strategy=Google.Cloud.Simple.AllAtOnce --labels=env=prod

POSITIONAL ARGUMENTS
    

RolloutId resource - Rollout to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`ROLLOUT`
     ID of the rolloutId or fully qualified identifier for the rolloutId. 

To set the `rollout` attribute: 

  * provide the argument `rollout` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

FlagRelease resource - Flag release that is rolled out to the target units. The flag release cannot be changed after the rollout is created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--flag-release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--flag-release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--flag-release`=`FLAG_RELEASE`
     ID of the flagRelease or fully qualified identifier for the flagRelease. 

To set the `flag-release` attribute: 

  * provide the argument `--flag-release` on the command line. 


Release resource - Release that is rolled out to the target units. The release cannot be changed after the rollout is created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--release`=`RELEASE`
     ID of the release or fully qualified identifier for the release. 

To set the `release` attribute: 

  * provide the argument `--release` on the command line. 


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
     For resources [flag-release, release, rollout, rollout-kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
RolloutKindId resource - Rollout kind that this rollout stems from and adheres to. The rollout kind cannot be changed after the rollout is created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--rollout-kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--rollout-kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--rollout-kind`=`ROLLOUT_KIND`
     ID of the rolloutKindId or fully qualified identifier for the rolloutKindId. 

To set the `rollout-kind` attribute: 

  * provide the argument `--rollout-kind` on the command line. 


`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`
     Strategy to use for executing this rollout. Supported values are `Google.Cloud.Simple.AllAtOnce`, `Google.Cloud.Simple.OneLocationAtATime`, `Google.Cloud.Progressive.Gradual.v1`, and `Google.Cloud.Progressive.SingleLocation.v1`. If not set, the strategy from the rollout kind is used. 
`--unit-filter`=`UNIT_FILTER`
     Filter, in Common Expression Language (CEL) format, that selects the eligible units. The filter can only reduce, not expand, the scope of the rollout. If empty, the unit filter from the rollout kind is used. For more information about CEL, see <https://github.com/google/cel-spec>. 
Rollout control, which requests a change to the execution of the rollout, such as pausing or canceling it. Requests can only be made when the rollout is in a non-terminal state. 
`--control-action`=`CONTROL_ACTION`
     Action to perform on the rollout. By default, the rollout runs until it naturally reaches a terminal state. `CONTROL_ACTION` must be one of: 

`cancel`
     Cancel the rollout permanently. 
`pause`
     Pause the rollout until it is resumed (that is, until the `run` action is requested). 
`run`
     Run the rollout until it naturally reaches a terminal state. A rollout requested to run progresses through all natural rollout states, such as from running to succeeded or from running to failed. If errors that can be retried occur during the rollout, the rollout is paused by default and can be resumed by requesting the `run` action again. 
This flag argument must be specified if any of the other arguments in this group are specified. 
Action parameters. 
Parameters for the `run` action that control the behavior of the rollout when it is resumed from a paused state. By default, the rollout retries failed operations when resumed. Can be specified only when `--control-action=run`. 
`--[no-]retry-failed-operations`
     Retry failed operations when the rollout is resumed. Applies only if the rollout is paused. Use `--retry-failed-operations` to enable and `--no-retry-failed-operations` to disable. 
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
