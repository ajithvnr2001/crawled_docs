---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/restore-verification-plan-associations/trigger-restore-verification/
title: gcloud alpha backup-dr restore-verification-plan-associations trigger-restore-verification \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:32:07.144248+00:00
---

# gcloud alpha backup-dr restore-verification-plan-associations trigger-restore-verification  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/restore-verification-plan-associations/trigger-restore-verification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha backup-dr restore-verification-plan-associations trigger-restore-verification Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha backup-dr restore-verification-plan-associations trigger-restore-verification - trigger a restore verification for an association 
SYNOPSIS
    

`gcloud alpha backup-dr restore-verification-plan-associations trigger-restore-verification` (`RESTORE_VERIFICATION_PLAN_ASSOCIATION` : `--location`=`LOCATION` `--restore-verification-plan`=`RESTORE_VERIFICATION_PLAN`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Trigger an on-demand restore verification for the specified restore verification plan association. 
EXAMPLES
     To trigger a restore verification for association `sample-association` under restore verification plan `sample-plan` in project `sample-project` and location `us-central1`, run: 
    
    
    [gcloud alpha backup-dr restore-verification-plan-associations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/restore-verification-plan-associations) trigger-restore-verification sample-association --restore-verification-plan=sample-plan --project=sample-project --location=us-central1

POSITIONAL ARGUMENTS
    

Restore Verification Plan Association resource - Name of the restore verification plan association to trigger. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `RESTORE_VERIFICATION_PLAN_ASSOCIATION` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RESTORE_VERIFICATION_PLAN_ASSOCIATION`
     ID of the Restore Verification Plan Association or fully qualified identifier for the Restore Verification Plan Association. 

To set the `name` attribute: 

  * provide the argument `RESTORE_VERIFICATION_PLAN_ASSOCIATION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Restore Verification Plan Association. 

To set the `location` attribute: 

  * provide the argument `RESTORE_VERIFICATION_PLAN_ASSOCIATION` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--restore-verification-plan`=`RESTORE_VERIFICATION_PLAN`
     The ID of the Restore Verification Plan. 

To set the `restore-verification-plan` attribute: 

  * provide the argument `RESTORE_VERIFICATION_PLAN_ASSOCIATION` on the command line with a fully specified name; 
  * provide the argument `--restore-verification-plan` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Trigger a restore verification for an association. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud backup-dr restore-verification-plan-associations](https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/restore-verification-plan-associations) trigger-restore-verification
    
    
    [gcloud beta backup-dr restore-verification-plan-associations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/restore-verification-plan-associations) trigger-restore-verification

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
