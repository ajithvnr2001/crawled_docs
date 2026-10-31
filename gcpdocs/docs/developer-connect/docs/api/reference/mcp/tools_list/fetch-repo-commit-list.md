---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit-list/
title: MCP Tools Reference: developerconnect.googleapis.com \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:08.267536+00:00
---

# MCP Tools Reference: developerconnect.googleapis.com  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  MCP Tools Reference: developerconnect.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `fetch-repo-commit-list`

Fetch a list of commits from a Git repository.

The following code sample shows how to use `curl` to call the `fetch-repo-commit-list` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://developerconnect.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "fetch-repo-commit-list",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for FetchGitRepositoryLinkCommitList.

### FetchGitRepositoryLinkCommitListRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "ref": string,
      "pageSize": integer,
      "pageToken": string,
      "view": enum ([CommitView](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit#Input.Schema.CommitView))
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
`ref` |  `string` Optional. The commit SHA, or symbolic revision (for example, branch name, tag, or Git reference) from which to start listing commits.  
`pageSize` |  `integer` Optional. Number of results to return in the list. Default is 50. Max is 100.  
`pageToken` |  `string` Optional. A page token, received from a previous `FetchGitRepositoryLinkCommitList` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `FetchGitRepositoryLinkCommitList` must match the call that provided the page token.  
`view` |  `enum (`[CommitView](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit#Input.Schema.CommitView)`)` Optional. The level of commit details to return in the response. Only `BASIC` is supported; `FULL` returns `INVALID_ARGUMENT`. Defaults to `BASIC` if unspecified. Use `FetchGitRepositoryLinkCommit` to get file diffs for a single commit.  
  
### CommitView

The level of commit details to return in the response.

Enums  
---  
`COMMIT_VIEW_UNSPECIFIED` | Unspecified, defaults to BASIC.  
`BASIC` | Basic view, returns commit metadata but no file diffs.  
`FULL` | Full view, returns commit metadata and file diffs.  
  
## Output Schema

Response message for FetchGitRepositoryLinkCommitList.

### FetchGitRepositoryLinkCommitListResponse

JSON representation  
---  
      
    
    {
      "commits": [
        {
          object ([SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit#Output.Schema.SCMCommit))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`commits[]` |  `object (`[SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit#Output.Schema.SCMCommit)`)` The list of commit metadata.  
`nextPageToken` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### SCMCommit

JSON representation  
---  
      
    
    {
      "sha": string,
      "message": string,
      "author": string,
      "authorEmail": string,
      "commitTime": string,
      "url": string
    }  
  
Fields  
---  
`sha` |  `string` Full 40-character SCM commit SHA.  
`message` |  `string` Commit message text.  
`author` |  `string` The author's display name.  
`authorEmail` |  `string` The author's email address.  
`commitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the commit was authored.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`url` |  `string` The SCM provider's HTML URL link for this commit.  
  
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
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
