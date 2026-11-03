---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations.boundaries
title: REST Resource: organizations.boundaries \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:38.999714+00:00
---

# REST Resource: organizations.boundaries  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations.boundaries

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: organizations.boundaries Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Boundary
    * JSON representation
  * Methods



## Resource: Boundary

A Boundary is a collection of projects defined by a filtering criteria on an organization or a folder.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "managementProject": string,
      "resourceFilter": {
        object ([ResourceFilter](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries#Boundary.ResourceFilter))
      },
      "state": enum ([State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries#Boundary.State)),
      "etag": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique resource name of the Boundary. Format: - `organizations/{organizationId}/boundaries/{boundaryId}` \- `folders/{folder_id}/boundaries/{boundaryId}` Example: `folders/123456789/boundaries/my-boundary`  
`displayName` |  `string` Optional. Human-readable display name of the Boundary. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `My Production Boundary`  
`managementProject` |  `string` Output only. The Management Project of the CapabilityConfig this Boundary is associated with. Will be empty if the Boundary is not associated with any CapabilityConfig. Format: `projects/{projectNumber}` Example: `projects/123456789012`  
`resourceFilter` |  `object (`[ResourceFilter](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries#Boundary.ResourceFilter)`)` Optional. The filter defining the criteria for descendant projects to be included in the Boundary. Descendant projects are dynamically included in the Boundary based on this filter.  
`state` |  `enum (`[State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries#Boundary.State)`)` Output only. The lifecycle state of the Boundary.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the Boundary.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time this Boundary was modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations.boundaries/create)`

|  Creates a Boundary under a parent Folder or Organization.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations.boundaries/delete)`

|  Deletes the Boundary identified by the specified `name` (for example, `folders/123456789/boundaries/my-boundary`).  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations.boundaries/get)`

|  Retrieves the Boundary identified by the specified `name` (for example, `folders/123456789/boundaries/my-boundary`).  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations.boundaries/list)`

|  Lists Boundaries that are direct children of the specified organization or folder resource.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations.boundaries/patch)`

|  Updates the `display_name` and `resource_filter.tag_filter.tag_value` of the Boundary identified by the specified `name` (for example, `folders/123456789/boundaries/my-boundary`).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
