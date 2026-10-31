---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/modifyPullRequest/
title: Method: projects.locations.connections.gitRepositoryLinks.modifyPullRequest \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:10.387448+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.modifyPullRequest  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/modifyPullRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.modifyPullRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * State
  * Try it!



Modifies a Pull Request in the remote SCM repository associated with a GitRepositoryLink.

### HTTP request

`POST https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:modifyPullRequest`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The GitRepositoryLink resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pullRequestId": string,
      "title": string,
      "body": string,
      "baseRef": string,
      "state": enum ([State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/modifyPullRequest#State))
    }  
  
Fields  
---  
`pullRequestId` |  `string` Required. The SCM-specific pull request identifier (for example, "45").  
`title` |  `string` Optional. The title of the Pull Request.  
`body` |  `string` Optional. The body description of the Pull Request.  
`baseRef` |  `string` Optional. The target branch to merge into.  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/modifyPullRequest#State)`)` Optional. The state of the Pull Request.  
  
### Response body

If successful, the response body contains an instance of `[PullRequest](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.modifyPullRequest`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## State

State represents the state of the pull request.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`OPEN` | The pull request is open.  
`CLOSED` | The pull request is closed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
