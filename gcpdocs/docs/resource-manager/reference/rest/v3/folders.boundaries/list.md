---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries/list/
title: Method: folders.boundaries.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:32.464110+00:00
---

# Method: folders.boundaries.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: folders.boundaries.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists Boundaries that are direct children of the specified organization or folder resource.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/{parent=folders/*}/boundaries`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent resource whose Boundaries are being listed. Format: `organizations/{organizationId}` or `folders/{folder_id}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of Boundaries to return in the response. The service may return fewer Boundaries than requested. If unspecified, at most 100 Boundaries will be returned. The maximum value is 100; values above 100 will be coerced to 100.  
`pageToken` |  `string` Optional. A pagination token received from a previous call to `boundaries.list` that indicates from where listing should continue. Provide this to retrieve the subsequent page.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListBoundariesResponse](https://docs.cloud.google.com/resource-manager/reference/rest/v3/ListBoundariesResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
