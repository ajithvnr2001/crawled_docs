---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestReviewComment/
title: Method: projects.locations.connections.gitRepositoryLinks.addPullRequestReviewComment \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:02.878447+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.addPullRequestReviewComment  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestReviewComment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.addPullRequestReviewComment Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * DiffSide
  * Try it!



Add a review comment (inline on diff) to a Pull Request.

### HTTP request

`POST https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:addPullRequestReviewComment`

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
        object ([PullRequestReviewComment](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestReviewComment#body.PullRequestReviewComment))
      },
      "commitId": string
    }  
  
Fields  
---  
`pullRequestId` |  `string` Required. The ID of the Pull Request.  
`comment` |  `object (`[PullRequestReviewComment](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestReviewComment#body.PullRequestReviewComment)`)` Required. The review comment to add.  
`commitId` |  `string` Optional. The commit SHA to comment on. If not specified, defaults to the HEAD commit of the Pull Request.  
  
### Response body

Message representing a SCM Pull Request Review Comment (inline on diff).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "id": string,
      "body": string,
      "path": string,
      "firstLine": integer,
      "lastLine": integer,
      "side": enum ([DiffSide](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestReviewComment#DiffSide)),
      "author": string,
      "createTime": string,
      "updateTime": string,
      "commitId": string
    }  
  
Fields  
---  
`id` |  `string` Output only. The ID of the comment.  
`body` |  `string` Required. The body of the comment.  
`path` |  `string` Required. The file path to comment on.  
`firstLine` |  `integer` Optional. The first line of the comment range (inclusive). If not specified, the comment applies only to the `lastLine`.  
`lastLine` |  `integer` Required. The last line of the comment range (inclusive). If `firstLine` is not specified, the comment applies only to this line.  
`side` |  `enum (`[DiffSide](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/addPullRequestReviewComment#DiffSide)`)` Optional. The side of the diff to comment on. Defaults to HEAD.  
`author` |  `string` Output only. The username of the author.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commitId` |  `string` Output only. The commit SHA the comment was actually applied to.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.addPullRequestReviewComment`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## DiffSide

DiffSide represents which side of the diff the comment is on.

Enums  
---  
`DIFF_SIDE_UNSPECIFIED` | Default value. This value is unused.  
`BASE` | The side of the diff before changes (deleted or modified lines).  
`HEAD` | The side of the diff after changes (added or modified lines).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
