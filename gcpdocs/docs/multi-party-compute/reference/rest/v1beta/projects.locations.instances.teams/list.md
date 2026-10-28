---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/list/
title: Method: projects.locations.instances.teams.list \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:36.720801+00:00
---

# Method: projects.locations.instances.teams.list  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.teams.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Teams in an instance.

### HTTP request

`GET https://mpc.googleapis.com/v1beta/{parent=projects/*/locations/*/instances/*}/teams`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent instance. Format: projects/{project}/locations/{location}/instances/{instance} It takes the form `projects/{project}/locations/{location}/instances/{instance}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of Teams to return. The service may return fewer. If unspecified, at most 50 are returned. Values above 1000 are coerced to 1000.  
`pageToken` |  `string` Optional. A page token from a previous `teams.list` call. When paginating, all other parameters must match the call that returned the token.  
  
### Request body

The request body must be empty.

### Response body

Response message for TeamService.ListTeams.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "teams": [
        {
          object ([Team](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams#Team))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`teams[]` |  `object (`[Team](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams#Team)`)` The Teams in the instance.  
`nextPageToken` |  `string` A token to retrieve the next page. Empty if there are no more pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
