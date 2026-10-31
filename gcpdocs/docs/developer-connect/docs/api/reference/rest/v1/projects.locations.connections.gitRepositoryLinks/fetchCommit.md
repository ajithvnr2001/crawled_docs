---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchCommit/
title: Method: projects.locations.connections.gitRepositoryLinks.fetchCommit \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:05.043430+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.fetchCommit  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchCommit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.fetchCommit Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Fetch Commit details from a Git repository link.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchCommit`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Query parameters

Parameters  
---  
`commitSha` |  `string` Required. The commit SHA, or symbolic revision (for example, branch name, tag, or Git reference).  
`view` |  `enum (`[CommitView](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/CommitView)`)` Optional. The level of commit details to return in the response. Defaults to `FULL` if unspecified. In `FULL` view, `files` metadata (paths and statuses) are returned; `pathFilters` must also be specified to populate line patch hunks.  
`pathFilters[]` |  `string` Optional. Path patterns or exact paths to filter returned files (only applicable in `FULL` view). When `pathFilters` is specified, `FileDiff.patch` is populated for all matching files (use `["**"]` to include patches for all changed files). When `pathFilters` is omitted or empty, the full list of `FileDiff` is returned without patch diffs (`FileDiff.patch` is empty).  
  
### Request body

The request body must be empty.

### Response body

Response message for gitRepositoryLinks.fetchCommit.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "commit": {
        object ([SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit))
      },
      "files": [
        {
          object ([FileDiff](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/FileDiff))
        }
      ]
    }  
  
Fields  
---  
`commit` |  `object (`[SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit)`)` The commit metadata.  
`files[]` |  `object (`[FileDiff](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/FileDiff)`)` List of file changes and patch diffs. Omitted when view is `BASIC`. Patch diffs (`FileDiff.patch`) are only populated when `pathFilters` is specified in the request.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.fetchCommit`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
