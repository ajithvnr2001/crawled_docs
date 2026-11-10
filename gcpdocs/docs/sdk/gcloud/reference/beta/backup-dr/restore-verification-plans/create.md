---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/restore-verification-plans/create/
title: gcloud beta backup-dr restore-verification-plans create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:33:29.878501+00:00
---

# gcloud beta backup-dr restore-verification-plans create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/restore-verification-plans/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta backup-dr restore-verification-plans create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta backup-dr restore-verification-plans create - create a Restore Verification Plan 
SYNOPSIS
    

`gcloud beta backup-dr restore-verification-plans create` (`RESTORE_VERIFICATION_PLAN` : `--location`=`LOCATION`) `--schedule`=`SCHEDULE` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--time-zone`=`TIME_ZONE`; default="UTC"] [`--failure-cleanup-delay`=`FAILURE_CLEANUP_DELAY` | `--skip-failure-cleanup`] [`--skip-success-cleanup` | `--success-cleanup-delay`=`SUCCESS_CLEANUP_DELAY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Restore Verification Plan. 
EXAMPLES
     To create a restore verification plan with id `sample-plan` in location `us-central1`, run: 
    
    
    gcloud beta backup-dr restore-verification-plans create sample-plan --location=us-central1 --schedule="0 1 * * *" --time-zone="America/New_York"

POSITIONAL ARGUMENTS
    

Restore Verification Plan resource - to create The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `restore_verification_plan` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RESTORE_VERIFICATION_PLAN`
     ID of the Restore Verification Plan or fully qualified identifier for the Restore Verification Plan. 

To set the `name` attribute: 

  * provide the argument `restore_verification_plan` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Restore Verification Plan. 

To set the `location` attribute: 

  * provide the argument `restore_verification_plan` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--schedule`=`SCHEDULE`
     Cron schedule for the restore verification plan. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Description of the restore verification plan. 
`--labels`=[`KEY`=`VALUE`,…]
     Optional resource labels to represent metadata provided by the user. 
`--time-zone`=`TIME_ZONE`; default="UTC"
     Time zone for the schedule (e.g., America/New_York). 
At most one of these can be specified: 

`--failure-cleanup-delay`=`FAILURE_CLEANUP_DELAY`
     Delay before cleaning up restored resources upon failed verification (e.g., 24h, 0s). 
`--skip-failure-cleanup`
     If set, restored resources will not be cleaned up upon failed verification. 
At most one of these can be specified: 

`--skip-success-cleanup`
     If set, restored resources will not be cleaned up upon successful verification. 
`--success-cleanup-delay`=`SUCCESS_CLEANUP_DELAY`
     Delay before cleaning up restored resources upon successful verification (e.g., 1h, 0s). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Create a restore verification plan. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud backup-dr restore-verification-plans create](https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/restore-verification-plans/create)
    
    
    [gcloud alpha backup-dr restore-verification-plans create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/restore-verification-plans/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
