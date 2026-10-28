---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/values/create/
title: gcloud alpha resource-manager semantic-tags values create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:39:04.643435+00:00
---

# gcloud alpha resource-manager semantic-tags values create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/values/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager semantic-tags values create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager semantic-tags values create - create a Semantic Tag Value 
SYNOPSIS
    

`gcloud alpha resource-manager semantic-tags values create` `VALUE_ID` `--key`=`KEY` (`--value`=`STRING` | `--value-field`=`FIELD`=`VALUE`,[`FIELD`=`VALUE`,…] | `--value-file`=`FILE`) [`--async`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--location`=`LOCATION`; default="global"] [`--parent`=`PARENT`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha resource-manager semantic-tags values create` creates a Semantic Tag Value under the specified organization or project container. 
EXAMPLES
     To create a composite Semantic Tag Value `cc-01` under `organizations/1001` using inline `--value-field` flags, run: 
    
    
    gcloud alpha resource-manager semantic-tags values create cc-01 --key=projects/gcp-semantic-tags-catalog/locations/global/semanticTagKeys/costcenter.allocation --parent=organizations/1001 --value-field=sre=40,infra=60 --display-name="Core Payments Allocation" --description="Cost allocation for core payments services"

To create a composite Semantic Tag Value `Trading` under `organizations/123456789012` from a YAML file `trading_value.yaml`, run: 
    
    
    gcloud alpha resource-manager semantic-tags values create Trading --key=placement.latency --parent=organizations/123456789012 --value-file=trading_value.yaml

To create a Semantic Tag Value `eng` under `projects/my-project` for key `costcenter.department`, run: 
    
    
    gcloud alpha resource-manager semantic-tags values create eng --key=projects/gcp-semantic-tags-catalog/locations/global/semanticTagKeys/costcenter.department --parent=projects/my-project --value=engineering --display-name="Engineering" --description="Engineering department tag value"

POSITIONAL ARGUMENTS
    

`VALUE_ID`
     ID of the Semantic Tag Value to create, or its full resource name. 
REQUIRED FLAGS
    

`--key`=`KEY`
     Semantic Tag Key associated with the value. Accepts the full resource name (`projects/gcp-semantic-tags-catalog/locations/{location}/semanticTagKeys/{key}`) or the key ID shorthand (for example, `costcenter.allocation`). 
Value payload for the Semantic Tag Value. 

Exactly one of these must be specified: 

`--value`=`STRING`
     Scalar string value for the Semantic Tag Value. 
`--value-field`=`FIELD`=`VALUE`,[`FIELD`=`VALUE`,…]
     Key-value pairs for a composite Semantic Tag Value (for example, `--value-field=sre=40,infra=60` or `--value-field=sre=40 --value-field=infra=60`). 
`--value-file`=`FILE`
     Path to a YAML or JSON file defining a Semantic Tag Value payload (containing `compositeValue`, and optionally `displayName` and `description`). 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-assigned description of the Semantic Tag Value. 
`--display-name`=`DISPLAY_NAME`
     User-friendly display name for the Semantic Tag Value. 
`--location`=`LOCATION`; default="global"
     Location of the Semantic Tag resource (for example, `global` or `us-central1`). 
`--parent`=`PARENT`
     Parent container of the Semantic Tag Value in the form `organizations/{organization_id}` or `projects/{project_id_or_number}`. If not specified, defaults to the active project (`projects/{core/project}`). 
`--validate-only`
     Validate the create request without actually performing the operation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
