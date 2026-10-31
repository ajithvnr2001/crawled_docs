---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestComment/
title: Method: projects.locations.connections.gitRepositoryLinks.addPullRequestComment \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:06.372665+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.addPullRequestComment  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestComment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.addPullRequestComment Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Add a comment to a Pull Request.

### HTTP request

`POST https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:addPullRequestComment`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pullRequestId": string,
      "comment": {
        object ([PullRequestComment](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestComment#body.PullRequestComment))
      }
    }  
  
Fields  
---  
`pullRequestId` |  `string` Required. The ID of the Pull Request.  
`comment` |  `object (`[PullRequestComment](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestComment#body.PullRequestComment)`)` Required. The comment to add.  
  
### Response body

Message representing a SCM Pull Request Comment.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "id": string,
      "body": string,
      "author": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`id` |  `string` Output only. The ID of the comment.  
`body` |  `string` Required. The body of the comment.  
`author` |  `string` Output only. The username of the author.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.addPullRequestComment`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
