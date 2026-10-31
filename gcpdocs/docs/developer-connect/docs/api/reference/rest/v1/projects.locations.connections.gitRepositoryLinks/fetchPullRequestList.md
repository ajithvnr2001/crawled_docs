---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchPullRequestList/
title: Method: projects.locations.connections.gitRepositoryLinks.fetchPullRequestList \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:06.974264+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.fetchPullRequestList  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchPullRequestList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.fetchPullRequestList Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Fetches a list of Pull Requests from the remote repository.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchPullRequestList`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The GitRepositoryLink resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. A filter expression that filters the pull requests returned in the response. Only a single equality comparison on `state` is supported, for example `state = "OPEN"`. Supported values are `OPEN`, `CLOSED`, and `MERGED`. `DECLINED` is only supported for SCM providers that support declining pull requests, and returns `INVALID_ARGUMENT` for GitHub, GitHub Enterprise, GitLab, and GitLab Enterprise. Other values or expressions return `INVALID_ARGUMENT`. Defaults to `state = "OPEN"` if unspecified.  
`pageSize` |  `integer` Optional. Number of results to return in the list. Default is 20. Max is 100. A page may contain fewer than `pageSize` results even when more results are available; use `nextPageToken` to check for more pages.  
`pageToken` |  `string` Optional. A page token, received from a previous `gitRepositoryLinks.fetchPullRequestList` call. Provide this to retrieve the subsequent page.  
  
### Request body

The request body must be empty.

### Response body

Response message for gitRepositoryLinks.fetchPullRequestList.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pullRequests": [
        {
          object ([PullRequest](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`pullRequests[]` |  `object (`[PullRequest](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest)`)` The list of pull requests.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.fetchPullRequestList`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
