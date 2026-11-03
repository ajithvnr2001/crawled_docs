---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects.capabilityConfigs
title: REST Resource: projects.capabilityConfigs \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:07.770469+00:00
---

# REST Resource: projects.capabilityConfigs  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects.capabilityConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: projects.capabilityConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CapabilityConfig
    * JSON representation
  * Methods



## Resource: CapabilityConfig

A CapabilityConfig allows managing experiences like applications and agents on a logical administrative perimeter of Projects (Boundary).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "types": [
        enum ([Type](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilityConfigs#CapabilityConfig.Type))
      ],
      "managementProject": string,
      "boundaries": [
        string
      ],
      "state": enum ([State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilityConfigs#CapabilityConfig.State)),
      "etag": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique resource name of the CapabilityConfig. Format: `organizations/{organization}/capabilityConfigs/{capabilityConfig}` or, `folders/{folder}/capabilityConfigs/{capabilityConfig}` or, `projects/{project}/capabilityConfigs/{capabilityConfig}`  
`displayName` |  `string` Optional. Human-readable non-unique display name of the CapabilityConfig. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `My CapabilityConfig`  
`types[]` |  `enum (`[Type](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilityConfigs#CapabilityConfig.Type)`)` Required. The CapabilityConfig types.  
`managementProject` |  `string` Optional. Immutable. The Management Project associated with this CapabilityConfig. If not provided during creation, a management project will be automatically created. Cannot be modified after creation. Format: `projects/{projectNumber}` Example: `projects/123456789012`  
`boundaries[]` |  `string` Optional. The list of Boundaries associated with this CapabilityConfig. Format: `organizations/{organization}/boundaries/{boundary}` or, `folders/{folder}/boundaries/{boundary}` or, `projects/{project}/boundaries/{boundary}`  
`state` |  `enum (`[State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilityConfigs#CapabilityConfig.State)`)` Output only. The lifecycle state of the CapabilityConfig.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the CapabilityConfig.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time this CapabilityConfig was modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects.capabilityConfigs/create)`

|  Creates a CapabilityConfig under a parent Organization, Folder or Project.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects.capabilityConfigs/delete)`

|  Deletes the CapabilityConfig identified by the specified `name` (for example, `folders/123456789/capabilityConfigs/my-capability-config`).  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects.capabilityConfigs/get)`

|  Retrieves the CapabilityConfig identified by the specified `name` (for example, `folders/123456789/capabilityConfigs/my-capability-config`).  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects.capabilityConfigs/list)`

|  Lists CapabilityConfigs that are direct children of the specified organization, folder or project resource.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects.capabilityConfigs/patch)`

|  Updates the `display_name`, `types` and `boundaries` of the CapabilityConfig identified by the specified `name` (for example, `folders/123456789/capabilityConfigs/my-capability-config`).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
