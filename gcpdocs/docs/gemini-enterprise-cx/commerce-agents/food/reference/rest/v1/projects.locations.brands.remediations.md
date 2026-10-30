---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations
title: REST Resource: projects.locations.brands.remediations \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:18.854359+00:00
---

# REST Resource: projects.locations.brands.remediations  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  REST Resource: projects.locations.brands.remediations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Remediation
    * JSON representation
  * State
  * Methods



## Resource: Remediation

Represents a persistent remediation applied to a brand.

JSON representation  
---  
      
    
    {
      "name": string,
      "targetEntityId": string,
      "targetEntityType": enum ([EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/EntityType)),
      "remediationAction": {
        object ([RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/RemediationAction))
      },
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations#State)),
      "targetStores": [
        string
      ],
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name. Format: projects/{project}/locations/{location}/brands/{brand}/remediations/{remediation}  
`targetEntityId` |  `string` Required. The ID of the menu entity this remediation targets.  
`targetEntityType` |  `enum (`[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/EntityType)`)` Required. The type of the menu entity this remediation targets.  
`remediationAction` |  `object (`[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/RemediationAction)`)` Required. The underlying remediation action to be executed during ingestion.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations#State)`)` Output only. The current state of this remediation.  
`targetStores[]` |  `string` Optional. If empty, this remediation applies to all stores within the brand. If populated, it only applies to the specific stores listed here.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this remediation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this remediation was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The lifecycle state of the remediation.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | The remediation is actively being applied during ingestion.  
`SUSPENDED` | The remediation is temporarily suspended.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations/create)`

|  Creates a remediation.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations/delete)`

|  Deletes a remediation.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations/get)`

|  Gets a remediation.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations/list)`

|  Lists remediations.  
  
### `[resume](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations/resume)`

|  Resumes a suspended remediation.  
  
### `[suspend](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.remediations/suspend)`

|  Suspends a remediation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
