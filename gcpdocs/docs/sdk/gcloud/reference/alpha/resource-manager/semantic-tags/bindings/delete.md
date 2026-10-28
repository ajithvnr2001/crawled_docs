---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/bindings/delete/
title: gcloud alpha resource-manager semantic-tags bindings delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:38:53.141853+00:00
---

# gcloud alpha resource-manager semantic-tags bindings delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/bindings/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager semantic-tags bindings delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager semantic-tags bindings delete - delete a Semantic Tag Binding 
SYNOPSIS
    

`gcloud alpha resource-manager semantic-tags bindings delete` `BINDING_NAME` [`--async`] [`--location`=`LOCATION`; default="global"] [`--parent`=`PARENT`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha resource-manager semantic-tags bindings delete` deletes a Semantic Tag Binding by its full resource name or binding ID. 
EXAMPLES
     To delete a Semantic Tag Binding by its full resource name, run: 
    
    
    gcloud alpha resource-manager semantic-tags bindings delete projects/acme-sec-prod/locations/us-central1/semanticTagBindings/stb-bk3v7q2m6x4t5p2c6r5n7w

To delete a Semantic Tag Binding by its short ID under `organizations/1001` in `us-central1`, run: 
    
    
    gcloud alpha resource-manager semantic-tags bindings delete stb-bk3v7q2m6x4t5p2c6r5n7w --parent=organizations/1001 --location=us-central1

POSITIONAL ARGUMENTS
    

`BINDING_NAME`
     Resource name or short ID of the Semantic Tag Binding to delete. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`; default="global"
     Location of the Semantic Tag resource (for example, `global` or `us-central1`). 
`--parent`=`PARENT`
     Parent container of the Semantic Tag Binding in the form `organizations/{organization_id}` or `projects/{project_id_or_number}`. For projects and project-scoped subresources, bindings are stored under the project parent (`projects/{project_id_or_number}`). For other Google Cloud resources (such as organizations or folders), bindings are stored under the organization parent (`organizations/{organization_id}`). If not specified, defaults to the active project (`projects/{core/project}`). 
`--validate-only`
     Validate the delete request without actually performing the operation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
