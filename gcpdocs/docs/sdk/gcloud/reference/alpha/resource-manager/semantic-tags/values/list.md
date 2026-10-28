---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/values/list/
title: gcloud alpha resource-manager semantic-tags values list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:39:11.804124+00:00
---

# gcloud alpha resource-manager semantic-tags values list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/values/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager semantic-tags values list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager semantic-tags values list - list Semantic Tag Values 
SYNOPSIS
    

`gcloud alpha resource-manager semantic-tags values list` [`--key`=`KEY`] [`--location`=`LOCATION`; default="global"] [`--parent`=`PARENT`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha resource-manager semantic-tags values list` lists Semantic Tag Values under the specified organization or project container. Results can be filtered by `semanticTagKey` using `--filter` (or `--key`). 
EXAMPLES
     To list all Semantic Tag Values under `organizations/1001` in `global`, run: 
    
    
    gcloud alpha resource-manager semantic-tags values list --location=global --parent=organizations/1001

To list predefined Semantic Tag Values in the Google Cloud Semantic Tags Catalog for the `environment` key, run: 
    
    
    gcloud alpha resource-manager semantic-tags values list --location=global --parent=projects/gcp-semantic-tags-catalog --key=environment

To list Semantic Tag Values under `organizations/1001` filtered to a specific Semantic Tag Key, run: 
    
    
    gcloud alpha resource-manager semantic-tags values list --location=global --parent=organizations/1001 --filter="semanticTagKey=projects/gcp-semantic-tags-catalog/locations/global/semanticTagKeys/costcenter.allocation"

FLAGS
    

`--key`=`KEY`
     Filter results to Semantic Tag Values associated with the specified Semantic Tag Key. Accepts the full resource name (`projects/gcp-semantic-tags-catalog/locations/{location}/semanticTagKeys/{key}`) or the key ID shorthand (for example, `costcenter.allocation`). 
`--location`=`LOCATION`; default="global"
     Location of the Semantic Tag resource (for example, `global` or `us-central1`). 
`--parent`=`PARENT`
     Parent container of the Semantic Tag Value in the form `organizations/{organization_id}` or `projects/{project_id_or_number}`. If not specified, defaults to the active project (`projects/{core/project}`). 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
