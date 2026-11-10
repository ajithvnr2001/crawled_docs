---
url: https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/
title: gcloud app-lifecycle-manager units \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:32:58.457925+00:00
---

# gcloud app-lifecycle-manager units  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud app-lifecycle-manager units Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud app-lifecycle-manager units - manage App Lifecycle Manager units 
SYNOPSIS
    

`gcloud app-lifecycle-manager units` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage App Lifecycle Manager units. A unit is an instance of a unit kind whose lifecycle is managed through an actuation engine, for example, one based on Terraform. Units are the building blocks of a tenant. Use unit operations to provision, upgrade, or deprovision a unit. 
EXAMPLES
     To create a unit named `my-unit` of the unit kind `my-unit-kind` in location `us-central1`, run: 
    
    
    [gcloud app-lifecycle-manager units create](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/create) my-unit --location=us-central1 --unit-kind=my-unit-kind

To list the names of all units in location `us-central1`, run: 
    
    
    [gcloud app-lifecycle-manager units list](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/list) --location=us-central1 --format="value(name)"

To describe the unit named `my-unit` in location `us-central1`, run: 
    
    
    [gcloud app-lifecycle-manager units describe](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/describe) my-unit --location=us-central1

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/create)`
     Create a unit. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/delete)`
     Delete a unit. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/describe)`
     Describe a unit. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/list)`
     List units. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/app-lifecycle-manager/units/update)`
     Update a unit. 
NOTES
     This variant is also available: 
    
    
    [gcloud beta app-lifecycle-manager units](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/units)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
