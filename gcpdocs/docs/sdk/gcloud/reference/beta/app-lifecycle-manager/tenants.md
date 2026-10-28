---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/
title: gcloud beta app-lifecycle-manager tenants \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:41:15.672486+00:00
---

# gcloud beta app-lifecycle-manager tenants  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager tenants Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager tenants - manage App Lifecycle Manager tenants 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager tenants` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage App Lifecycle Manager tenants. A tenant represents the service producer side of an instance of the service that is created based on a request from a consumer. A tenant usually maps one-to-one to a resource given out to a service consumer. 
EXAMPLES
     To create a tenant named `my-tenant` for the SaaS offering `my-saas` in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager tenants create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/create) my-tenant --location=us-central1 --saas=my-saas

To list the names of all tenants in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager tenants list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/list) --location=us-central1 --format="value(name)"

To describe the tenant named `my-tenant` in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager tenants describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/describe) my-tenant --location=us-central1

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/create)`
     `(BETA)` Create a tenant. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/delete)`
     `(BETA)` Delete a tenant. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/describe)`
     `(BETA)` Describe a tenant. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/list)`
     `(BETA)` List tenants. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/tenants/update)`
     `(BETA)` Update a tenant. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
