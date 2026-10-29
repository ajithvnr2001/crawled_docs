---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:38.238117+00:00
---

# REST Resource: projects.locations.instances  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * State
  * Methods



## Resource: Instance

Represents a geographical MPC instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "etag": string,
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances#State)),
      "stateMessage": string,
      "createTime": string,
      "updateTime": string,
      "uid": string,
      "url": string,
      "adminPrincipals": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the instance. Format: projects/{project}/locations/{location}/instances/{instance}  
`displayName` |  `string` Optional. A human-readable title. Can be changed.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key-value pairs for categorization and billing. Example: {"env": "prod", "cost_center": "treasury"}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Output only. An opaque tag indicating the current version of the resource, used for concurrency control.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances#State)`)` Output only. The current state of the instance.  
`stateMessage` |  `string` Output only. A human-readable explanation of the current state, particularly useful if the instance is in a `FAILED` state.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Instance was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Instance was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. The unique identifier of the instance.  
`url` |  `string` Output only. The data plane URL for interacting with this Instance. Example: "https://my-instance.us-central1.mpc.goog"  
`adminPrincipals[]` |  `string` Required. Input only. Immutable. Principals of the initial administrators for this Instance: each entry is a Google account email address (e.g., "alice@example.com") or a BYOID (workforce/workload identity) principal (e.g., "principal://iam.googleapis.com/locations/global/workforcePools/{pool}/subject/{subject}"). At least 2 distinct administrators must be specified, and the authenticated caller creating the Instance must be included in this list.  
  
## State

The lifecycle state of the MPC Instance. Adheres to AIP-216 definitions.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`CREATING` | The instance is being created and provisioned.  
`ACTIVE` | The instance is fully active and ready to process policies.  
`UPDATING` | The instance is being updated.  
`DELETING` | The instance is being deleted.  
`FAILED` | The instance is in a failed state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/create)`

|  Creates a new Instance in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/delete)`

|  Deletes a single Instance.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/get)`

|  Gets details of a single Instance.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/list)`

|  Lists Instances in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/patch)`

|  Updates the parameters of a single Instance.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
