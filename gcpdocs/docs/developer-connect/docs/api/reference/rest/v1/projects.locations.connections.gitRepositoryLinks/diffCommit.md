---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/diffCommit/
title: Method: projects.locations.connections.gitRepositoryLinks.diffCommit \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:05.632215+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.diffCommit  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/diffCommit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.diffCommit Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Diff commits for a GitRepositoryLink.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:diffCommit`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink.  
  
### Query parameters

Parameters  
---  
`baseSha` |  `string` Required. The base commit SHA or ref.  
`headSha` |  `string` Required. The head commit SHA or ref.  
`pathFilters[]` |  `string` Optional. Path patterns or exact paths to filter returned files. When `pathFilters` is specified, `FileDiff.patch` is populated for all matching files (use `["**"]` to include patches for all changed files). When `pathFilters` is omitted or empty, the full list of `FileDiff` is returned without patch diffs (`FileDiff.patch` is empty).  
  
### Request body

The request body must be empty.

### Response body

Response message for gitRepositoryLinks.diffCommit.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "files": [
        {
          object ([FileDiff](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/FileDiff))
        }
      ]
    }  
  
Fields  
---  
`files[]` |  `object (`[FileDiff](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/FileDiff)`)` The file diff extracted from the unified diff.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.diffCommit`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
