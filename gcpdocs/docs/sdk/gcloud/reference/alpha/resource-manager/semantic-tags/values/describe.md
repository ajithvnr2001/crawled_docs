---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/values/describe/
title: gcloud alpha resource-manager semantic-tags values describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:38:48.584775+00:00
---

# gcloud alpha resource-manager semantic-tags values describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/values/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager semantic-tags values describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager semantic-tags values describe - describe a Semantic Tag Value 
SYNOPSIS
    

`gcloud alpha resource-manager semantic-tags values describe` `VALUE_ID` [`--location`=`LOCATION`; default="global"] [`--parent`=`PARENT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha resource-manager semantic-tags values describe` describes a Semantic Tag Value given its ID, location, and parent, or its full resource name. When `--parent` is omitted with a short ID, it defaults to the Google Cloud Semantic Tags Catalog container (`projects/gcp-semantic-tags-catalog`). 
EXAMPLES
     To describe a Google Cloud predefined Semantic Tag Value `prod` in `us-central1`, run: 
    
    
    gcloud alpha resource-manager semantic-tags values describe prod --location=us-central1

To describe a customer Semantic Tag Value `Trading` under `organizations/1001` in `us-central1`, run: 
    
    
    gcloud alpha resource-manager semantic-tags values describe Trading --location=us-central1 --parent=organizations/1001

To describe a Semantic Tag Value by its full resource name, run: 
    
    
    gcloud alpha resource-manager semantic-tags values describe projects/my-project/locations/us-central1/semanticTagValues/eng

POSITIONAL ARGUMENTS
    

`VALUE_ID`
     ID of the Semantic Tag Value to describe, or its full resource name. 
FLAGS
    

`--location`=`LOCATION`; default="global"
     Location of the Semantic Tag resource (for example, `global` or `us-central1`). 
`--parent`=`PARENT`
     Parent container of the Semantic Tag Value in the form `organizations/{organization_id}` or `projects/{project_id_or_number}`. Defaults to `projects/gcp-semantic-tags-catalog` when omitted. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
