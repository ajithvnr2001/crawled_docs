---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/create/
title: Method: projects.locations.instances.create \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:38:58.576343+00:00
---

# Method: projects.locations.instances.create  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new Instance in a given project and location.

### HTTP request

`POST https://mpc.googleapis.com/v1beta/{parent=projects/*/locations/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Value for parent. It takes the form `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`instanceId` |  `string` Required. The ID to use for the instance. The ID must be 1-63 characters long, start with a lowercase letter, end with a lowercase letter or number, and contain only lowercase letters, numbers, and hyphens.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Must be a valid UUID4.  
  
### Request body

The request body contains an instance of `[Instance](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances#Instance)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
