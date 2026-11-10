---
url: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/restore-templates/create/
title: gcloud backup-dr restore-templates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:33:36.910489+00:00
---

# gcloud backup-dr restore-templates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/restore-templates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud backup-dr restore-templates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud backup-dr restore-templates create - create a Restore Template 
SYNOPSIS
    

`gcloud backup-dr restore-templates create` (`RESTORE_TEMPLATE` : `--location`=`LOCATION`) `--data-source`=`DATA_SOURCE` `--resource-type`=`RESOURCE_TYPE` `--restore-properties`=`RESTORE_PROPERTIES` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--post-restore-cloud-run-job`=`POST_RESTORE_CLOUD_RUN_JOB` `--post-restore-timeout`=`POST_RESTORE_TIMEOUT`] [`--pre-restore-cloud-run-job`=`PRE_RESTORE_CLOUD_RUN_JOB` `--pre-restore-timeout`=`PRE_RESTORE_TIMEOUT`] [`--verification-cloud-run-job`=`VERIFICATION_CLOUD_RUN_JOB` `--verification-timeout`=`VERIFICATION_TIMEOUT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Restore Template. 
EXAMPLES
     To create a restore template `my-template` in location `us-central1` for a Compute Engine instance, run: 
    
    
    gcloud backup-dr restore-templates create my-template --location=us-central1 --resource-type="compute.googleapis.com/Instance" --data-source="projects/my-project/locations/us-central1/backupVaults/my-vault/dataSources/my-ds" --restore-properties='{"project": "my-project", "zone":
     "us-central1-a", "resource": {"name": "test-vm-{EXECUTION_ID}"}}'

To create a restore template `my-template` from a restore properties file, run: 
    
    
    gcloud backup-dr restore-templates create my-template --location=us-central1 --resource-type="compute.googleapis.com/Instance" --data-source="projects/my-project/locations/us-central1/backupVaults/my-vault/dataSources/my-ds" --restore-properties=path/to/restore_properties.json

POSITIONAL ARGUMENTS
    

Restore Template resource - to create The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `restore_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RESTORE_TEMPLATE`
     ID of the Restore Template or fully qualified identifier for the Restore Template. 

To set the `name` attribute: 

  * provide the argument `restore_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Restore Template. 

To set the `location` attribute: 

  * provide the argument `restore_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--data-source`=`DATA_SOURCE`
     The full resource name of the DataSource from which backups will be selected. Format: projects/{project}/locations/{location}/backupVaults/{vault}/dataSources/{dataSource} 
`--resource-type`=`RESOURCE_TYPE`
     The type of the Google Cloud resource (e.g., compute.googleapis.com/Instance). 
`--restore-properties`=`RESTORE_PROPERTIES`
     Defines the target environment and configuration for restoring the resource. Accepts either an inline JSON or YAML string or a path to a JSON or YAML file containing the properties. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Description of the restore template. 
`--labels`=[`KEY`=`VALUE`,…]
     Optional resource labels to represent metadata provided by the user. 
Post-restore hook configuration. 
`--post-restore-cloud-run-job`=`POST_RESTORE_CLOUD_RUN_JOB`
     The Cloud Run job to execute after the restore operation. Format: projects/{project}/locations/{location}/jobs/{job} 
`--post-restore-timeout`=`POST_RESTORE_TIMEOUT`
     Timeout for the post-restore hook (e.g., 600s). Must be specified with \--post-restore-cloud-run-job. 
Pre-restore hook configuration. 
`--pre-restore-cloud-run-job`=`PRE_RESTORE_CLOUD_RUN_JOB`
     The Cloud Run job to execute before the restore operation. Format: projects/{project}/locations/{location}/jobs/{job} 
`--pre-restore-timeout`=`PRE_RESTORE_TIMEOUT`
     Timeout for the pre-restore hook (e.g., 300s). Must be specified with \--pre-restore-cloud-run-job. 
Verification hook configuration. 
`--verification-cloud-run-job`=`VERIFICATION_CLOUD_RUN_JOB`
     The Cloud Run job to execute to verify the restored workload. Format: projects/{project}/locations/{location}/jobs/{job} 
`--verification-timeout`=`VERIFICATION_TIMEOUT`
     Timeout for the verification hook (e.g., 300s). Must be specified with \--verification-cloud-run-job. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Create a restore template. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha backup-dr restore-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/restore-templates/create)
    
    
    [gcloud beta backup-dr restore-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/restore-templates/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
