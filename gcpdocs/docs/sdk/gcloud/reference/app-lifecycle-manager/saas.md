---
url: https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/
title: gcloud app-lifecycle-manager saas \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:33:34.248785+00:00
---

# gcloud app-lifecycle-manager saas  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud app-lifecycle-manager saas Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud app-lifecycle-manager saas - manage App Lifecycle Manager SaaS offerings 
SYNOPSIS
    

`gcloud app-lifecycle-manager saas` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage App Lifecycle Manager SaaS offerings. A SaaS offering (also called an app offering) represents a SaaS product managed by the service producer. It defines the locations in which the product is available. 
EXAMPLES
     To create a SaaS offering named `my-saas` in location `us-central1` that is available in `us-central1`, run: 
    
    
    [gcloud app-lifecycle-manager saas create](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/create) my-saas --location=us-central1 --locations=name=us-central1

To list the names of all SaaS offerings in location `us-central1`, run: 
    
    
    [gcloud app-lifecycle-manager saas list](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/list) --location=us-central1 --format="value(name)"

To describe the SaaS offering named `my-saas` in location `us-central1`, run: 
    
    
    [gcloud app-lifecycle-manager saas describe](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/describe) my-saas --location=us-central1

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/create)`
     Create a SaaS offering. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/delete)`
     Delete a SaaS offering. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/describe)`
     Describe a SaaS offering. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/list)`
     List SaaS offerings. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/saas/update)`
     Update a SaaS offering. 
NOTES
     This variant is also available: 
    
    
    [gcloud beta app-lifecycle-manager saas](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/saas)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
