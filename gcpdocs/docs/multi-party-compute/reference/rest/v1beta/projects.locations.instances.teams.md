---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams
title: REST Resource: projects.locations.instances.teams \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:34.449746+00:00
---

# REST Resource: projects.locations.instances.teams  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.teams Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Team
    * JSON representation
  * Methods



## Resource: Team

A Team is a logical group of users used for key share allocation.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Team. Format: projects/{project}/locations/{location}/instances/{instance}/teams/{team}  
`displayName` |  `string` Optional. User-assigned display name for the Team.  
`description` |  `string` Optional. User-provided description of the Team.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Team was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Team was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. The unique server-generated identifier of the Team.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/create)`

|  Creates a new Team in an instance.  
  
### `[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/delete)`

|  Deletes a Team.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/get)`

|  Gets details of a single Team.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/list)`

|  Lists Teams in an instance.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
