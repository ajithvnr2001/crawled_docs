---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/folder-rollout-plans/describe/
title: gcloud preview compute folder-rollout-plans describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:39:12.781741+00:00
---

# gcloud preview compute folder-rollout-plans describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/folder-rollout-plans/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute folder-rollout-plans describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute folder-rollout-plans describe - describe a folder rollout plan 
SYNOPSIS
    

`gcloud preview compute folder-rollout-plans describe` (`NAME` : `--folder`=`FOLDER`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Describe a folder rollout plan. 
EXAMPLES
     To describe a folder rollout plan named 'my-folder-rollout-plan' in folder '123456789', run: 
    
    
    gcloud preview compute folder-rollout-plans describe my-folder-rollout-plan --folder=123456789

POSITIONAL ARGUMENTS
    

Folder rollout plan resource - Name of the folder rollout plan you want to inspect. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`NAME`
     ID of the folder rollout plan or fully qualified identifier for the folder rollout plan. 

To set the `name` attribute: 

  * provide the argument `name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     The Google Cloud folder ID. 

To set the `folder` attribute: 

  * provide the argument `name` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud alpha compute folder-rollout-plans describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/folder-rollout-plans/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
