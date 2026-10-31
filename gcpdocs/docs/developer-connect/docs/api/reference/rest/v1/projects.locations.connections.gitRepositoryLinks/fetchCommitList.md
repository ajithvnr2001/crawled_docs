---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchCommitList/
title: Method: projects.locations.connections.gitRepositoryLinks.fetchCommitList \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:39:59.828668+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.fetchCommitList  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchCommitList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.fetchCommitList Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Fetch a list of Commits from a Git repository link.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchCommitList`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Query parameters

Parameters  
---  
`ref` |  `string` Optional. The commit SHA, or symbolic revision (for example, branch name, tag, or Git reference) from which to start listing commits.  
`pageSize` |  `integer` Optional. Number of results to return in the list. Default is 50. Max is 100.  
`pageToken` |  `string` Optional. A page token, received from a previous `gitRepositoryLinks.fetchCommitList` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `gitRepositoryLinks.fetchCommitList` must match the call that provided the page token.  
`view` |  `enum (`[CommitView](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/CommitView)`)` Optional. The level of commit details to return in the response. Only `BASIC` is supported; `FULL` returns `INVALID_ARGUMENT`. Defaults to `BASIC` if unspecified. Use `gitRepositoryLinks.fetchCommit` to get file diffs for a single commit.  
  
### Request body

The request body must be empty.

### Response body

Response message for gitRepositoryLinks.fetchCommitList.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "commits": [
        {
          object ([SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`commits[]` |  `object (`[SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit)`)` The list of commit metadata.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.fetchCommitList`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
