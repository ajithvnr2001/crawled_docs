---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/
title: gcloud beta app-lifecycle-manager unit-kinds \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:56.348534+00:00
---

# gcloud beta app-lifecycle-manager unit-kinds  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager unit-kinds Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager unit-kinds - manage App Lifecycle Manager unit kinds 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager unit-kinds` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage App Lifecycle Manager unit kinds. A unit kind defines a type of managed component (unit) within a SaaS offering. Units of the same unit kind are managed together; for example, they follow the same release model and are typically rolled out together. 
EXAMPLES
     To create a unit kind named `my-unit-kind` for the SaaS offering `my-saas` in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager unit-kinds create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/create) my-unit-kind --location=us-central1 --saas=my-saas

To list the names of all unit kinds in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager unit-kinds list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/list) --location=us-central1 --format="value(name)"

To describe the unit kind named `my-unit-kind` in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager unit-kinds describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/describe) my-unit-kind --location=us-central1

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/create)`
     `(BETA)` Create a unit kind. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/delete)`
     `(BETA)` Delete a unit kind. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/describe)`
     `(BETA)` Describe a unit kind. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/list)`
     `(BETA)` List unit kinds. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/update)`
     `(BETA)` Update a unit kind. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
