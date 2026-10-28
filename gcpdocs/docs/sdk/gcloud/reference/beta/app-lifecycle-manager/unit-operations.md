---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/
title: gcloud beta app-lifecycle-manager unit-operations \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:55.740538+00:00
---

# gcloud beta app-lifecycle-manager unit-operations  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager unit-operations Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager unit-operations - manage App Lifecycle Manager unit operations 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager unit-operations` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage App Lifecycle Manager unit operations. A unit operation encapsulates the intent to change or interact with the service component represented by a specific unit. For example, a unit operation can provision, upgrade, or deprovision the unit. Multiple unit operations can be requested and scheduled, but only one runs at a time. 
EXAMPLES
     To create a unit operation named `my-unit-operation` in location `us-central1` that provisions the unit `my-unit` with the release `my-release`, run: 
    
    
    [gcloud beta app-lifecycle-manager unit-operations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/create) my-unit-operation --location=us-central1 --unit=my-unit --provision --provision-release=my-release

To list the names of all unit operations in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager unit-operations list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/list) --location=us-central1 --format="value(name)"

To describe the unit operation named `my-unit-operation` in location `us-central1`, run: 
    
    
    [gcloud beta app-lifecycle-manager unit-operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/describe) my-unit-operation --location=us-central1

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/create)`
     `(BETA)` Create a unit operation. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/delete)`
     `(BETA)` Delete a unit operation. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/describe)`
     `(BETA)` Describe a unit operation. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/list)`
     `(BETA)` List unit operations. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-operations/update)`
     `(BETA)` Update a unit operation. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
