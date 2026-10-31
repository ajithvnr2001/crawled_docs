---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment/
title: MCP Tools Reference: developerconnect.googleapis.com \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:06.082788+00:00
---

# MCP Tools Reference: developerconnect.googleapis.com  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  MCP Tools Reference: developerconnect.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `add-repo-pull-request-review-comment`

Add a review comment (inline on diff) to a pull request.

The following code sample shows how to use `curl` to call the `add-repo-pull-request-review-comment` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://developerconnect.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "add-repo-pull-request-review-comment",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for AddGitRepositoryLinkPullRequestReviewComment.

### AddGitRepositoryLinkPullRequestReviewCommentRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "pullRequestId": string,
      "comment": {
        object ([PullRequestReviewComment](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment#Input.Schema.PullRequestReviewComment))
      },
      "commitId": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
`pullRequestId` |  `string` Required. The ID of the Pull Request.  
`comment` |  `object (`[PullRequestReviewComment](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment#Input.Schema.PullRequestReviewComment)`)` Required. The review comment to add.  
`commitId` |  `string` Optional. The commit SHA to comment on. If not specified, defaults to the HEAD commit of the Pull Request.  
  
### PullRequestReviewComment

JSON representation  
---  
      
    
    {
      "id": string,
      "body": string,
      "path": string,
      "firstLine": integer,
      "lastLine": integer,
      "side": enum ([DiffSide](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment#Input.Schema.DiffSide)),
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
`firstLine` |  `integer` Optional. The first line of the comment range (inclusive). If not specified, the comment applies only to the `last_line`.  
`lastLine` |  `integer` Required. The last line of the comment range (inclusive). If `first_line` is not specified, the comment applies only to this line.  
`side` |  `enum (`[DiffSide](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment#Input.Schema.DiffSide)`)` Optional. The side of the diff to comment on. Defaults to HEAD.  
`author` |  `string` Output only. The username of the author.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commitId` |  `string` Output only. The commit SHA the comment was actually applied to.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### DiffSide

DiffSide represents which side of the diff the comment is on.

Enums  
---  
`DIFF_SIDE_UNSPECIFIED` | Default value. This value is unused.  
`BASE` | The side of the diff before changes (deleted or modified lines).  
`HEAD` | The side of the diff after changes (added or modified lines).  
  
## Output Schema

Message representing a SCM Pull Request Review Comment (inline on diff).

### PullRequestReviewComment

JSON representation  
---  
      
    
    {
      "id": string,
      "body": string,
      "path": string,
      "firstLine": integer,
      "lastLine": integer,
      "side": enum ([DiffSide](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment#Input.Schema.DiffSide)),
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
`firstLine` |  `integer` Optional. The first line of the comment range (inclusive). If not specified, the comment applies only to the `last_line`.  
`lastLine` |  `integer` Required. The last line of the comment range (inclusive). If `first_line` is not specified, the comment applies only to this line.  
`side` |  `enum (`[DiffSide](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment#Input.Schema.DiffSide)`)` Optional. The side of the diff to comment on. Defaults to HEAD.  
`author` |  `string` Output only. The username of the author.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the comment was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commitId` |  `string` Output only. The commit SHA the comment was actually applied to.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### DiffSide

DiffSide represents which side of the diff the comment is on.

Enums  
---  
`DIFF_SIDE_UNSPECIFIED` | Default value. This value is unused.  
`BASE` | The side of the diff before changes (deleted or modified lines).  
`HEAD` | The side of the diff after changes (added or modified lines).  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
