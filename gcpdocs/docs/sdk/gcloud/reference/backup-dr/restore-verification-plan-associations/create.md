---
url: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/restore-verification-plan-associations/create/
title: gcloud backup-dr restore-verification-plan-associations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:32:15.562221+00:00
---

# gcloud backup-dr restore-verification-plan-associations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/restore-verification-plan-associations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud backup-dr restore-verification-plan-associations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud backup-dr restore-verification-plan-associations create - create a new restore verification plan association 
SYNOPSIS
    

`gcloud backup-dr restore-verification-plan-associations create` (`RESTORE_VERIFICATION_PLAN_ASSOCIATION` : `--location`=`LOCATION` `--restore-verification-plan`=`RESTORE_VERIFICATION_PLAN`) `--resource-type`=`RESOURCE_TYPE` `--restore-template`=`RESTORE_TEMPLATE` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new restore verification plan association in the project. 
EXAMPLES
     To create a new restore verification plan association `sample-association` under restore verification plan `sample-plan` in project `sample-project` and location `us-central1` for resource type `compute.googleapis.com/Instance` with restore template `projects/sample-project/locations/us-central1/restoreTemplates/sample-template`, run: 
    
    
    gcloud backup-dr restore-verification-plan-associations create sample-association --restore-verification-plan=sample-plan --project=sample-project --location=us-central1 --resource-type=compute.googleapis.com/Instance --restore-template=projects/sample-project/locations/us-central1/restoreTemplates/sample-template

POSITIONAL ARGUMENTS
    

Restore Verification Plan Association resource - Name of the restore verification plan association to be created. Once created, this name can't be changed. The name must be unique for a restore verification plan. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

`--resource-type`=`RESOURCE_TYPE`
     Type of the Google Cloud resource to associate. 

For example: 

  * `compute.<UNIVERSE_DOMAIN>/Instance` for Compute Engine instances. 


Restore Template resource - The Restore Template to associate with the workload. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--restore-template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--restore-template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--restore-template`=`RESTORE_TEMPLATE`
     ID of the Restore Template or fully qualified identifier for the Restore Template. 

To set the `name` attribute: 

  * provide the argument `--restore-template` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     The description of the restore verification plan association. 
`--labels`=[`KEY`=`VALUE`,…]
     Optional resource labels to represent metadata provided by the user. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Creates a new restore verification plan association. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha backup-dr restore-verification-plan-associations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/restore-verification-plan-associations) create
    
    
    [gcloud beta backup-dr restore-verification-plan-associations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/restore-verification-plan-associations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
