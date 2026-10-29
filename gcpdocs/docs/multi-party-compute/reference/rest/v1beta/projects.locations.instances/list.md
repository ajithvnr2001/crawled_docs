---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/list/
title: Method: projects.locations.instances.list \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:10.665265+00:00
---

# Method: projects.locations.instances.list  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Instances in a given project and location.

### HTTP request

`GET https://mpc.googleapis.com/v1beta/{parent=projects/*/locations/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListInstancesRequest It takes the form `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results  
`orderBy` |  `string` Optional. Hint for how to order the results  
  
### Request body

The request body must be empty.

### Response body

Response message for listing Instances.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instances": [
        {
          object ([Instance](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances#Instance))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`instances[]` |  `object (`[Instance](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances#Instance)`)` The list of Instance  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached. For example, if a request is fanned out to multiple locations and one is unavailable, it will be listed here. This list might expand in the future to include other resources.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
