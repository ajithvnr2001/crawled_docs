---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/
title: gcloud beta app-lifecycle-manager rollouts \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:35.281520+00:00
---

# gcloud beta app-lifecycle-manager rollouts  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager rollouts Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager rollouts - manage App Lifecycle Manager rollouts 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager rollouts` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage App Lifecycle Manager rollouts. A rollout represents a single execution of rolling out a release to the target units, including its results. The rollout follows the settings of the rollout kind that it stems from. 
EXAMPLES
     To create a rollout named `my-rollout` in location `us-central1` that rolls out the release `my-release` according to the rollout kind `my-rollout-kind`, run: 
    
    
    [gcloud beta app-lifecycle-manager rollouts create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/create) my-rollout --location=us-central1 --release=my-release --rollout-kind=my-rollout-kind

To list the names of all rollouts in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager rollouts list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/list) --location=us-central1 --format="value(name)"

To pause the rollout named `my-rollout` in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager rollouts update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/update) my-rollout --location=us-central1 --control-action=pause

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/create)`
     `(BETA)` Create a rollout. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/delete)`
     `(BETA)` Delete a rollout. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/describe)`
     `(BETA)` Describe a rollout. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/list)`
     `(BETA)` List rollouts. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/update)`
     `(BETA)` Update a rollout. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
