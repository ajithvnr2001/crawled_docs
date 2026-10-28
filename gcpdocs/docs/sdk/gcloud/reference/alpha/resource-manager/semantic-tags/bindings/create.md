---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/bindings/create/
title: gcloud alpha resource-manager semantic-tags bindings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:39:03.675760+00:00
---

# gcloud alpha resource-manager semantic-tags bindings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/semantic-tags/bindings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager semantic-tags bindings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager semantic-tags bindings create - create a Semantic Tag Binding 
SYNOPSIS
    

`gcloud alpha resource-manager semantic-tags bindings create` `--semantic-tag-value`=`VALUE` `--target-resource`=`FULL_RESOURCE_URI` [`--async`] [`--location`=`LOCATION`; default="global"] [`--parent`=`PARENT`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha resource-manager semantic-tags bindings create` creates a Semantic Tag Binding attaching a Semantic Tag Value to a target Google Cloud resource under the specified organization or project container. 
EXAMPLES
     To bind a Compute Engine VM instance to a customer-managed Semantic Tag Value under `projects/acme-sec-prod` in `us-central1`, run: 
    
    
    gcloud alpha resource-manager semantic-tags bindings create --target-resource=//compute.googleapis.com/projects/acme-sec-prod/zones/us-central1-a/instances/order-matcher-01 --semantic-tag-value=projects/acme-sec-prod/locations/us-central1/semanticTagValues/pci-dss --location=us-central1 --parent=projects/acme-sec-prod

To bind a Cloud Spanner database to a predefined Semantic Tag Value in the Google Cloud Semantic Tags Catalog, run: 
    
    
    gcloud alpha resource-manager semantic-tags bindings create --target-resource=//spanner.googleapis.com/projects/acme-sec-prod/instances/prod-db/databases/orders --semantic-tag-value=projects/gcp-semantic-tags-catalog/locations/us-central1/semanticTagValues/prod --location=us-central1 --parent=projects/acme-sec-prod

REQUIRED FLAGS
    

`--semantic-tag-value`=`VALUE`
     Resource name of the Semantic Tag Value being bound (for example, `projects/my-proj/locations/global/semanticTagValues/val-1`, `organizations/1001/locations/global/semanticTagValues/val-1`, or `projects/gcp-semantic-tags-catalog/locations/global/semanticTagValues/prod`). 
`--target-resource`=`FULL_RESOURCE_URI`
     Full resource name of the target Google Cloud resource (for example, `//compute.googleapis.com/projects/my-proj/zones/us-central1-a/instances/vm-1` or `//cloudresourcemanager.googleapis.com/projects/123456`). 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`; default="global"
     Location of the Semantic Tag resource (for example, `global` or `us-central1`). 
`--parent`=`PARENT`
     Parent container of the Semantic Tag Binding in the form `organizations/{organization_id}` or `projects/{project_id_or_number}`. For projects and project-scoped subresources, bindings are stored under the project parent (`projects/{project_id_or_number}`). For other Google Cloud resources (such as organizations or folders), bindings are stored under the organization parent (`organizations/{organization_id}`). If not specified, defaults to the active project (`projects/{core/project}`). 
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
