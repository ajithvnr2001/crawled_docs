---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request/
title: MCP Tools Reference: developerconnect.googleapis.com \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:00.747645+00:00
---

# MCP Tools Reference: developerconnect.googleapis.com  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  MCP Tools Reference: developerconnect.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `open-repo-pull-request`

Open a pull request in the remote SCM repository.

The following code sample shows how to use `curl` to call the `open-repo-pull-request` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://developerconnect.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "open-repo-pull-request",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Message for opening SCM Pull Request.

### OpenGitRepositoryLinkPullRequestRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "pullRequest": {
        object ([PullRequest](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.PullRequest))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The GitRepositoryLink resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
`pullRequest` |  `object (`[PullRequest](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.PullRequest)`)` Required. The Pull Request details to open. Input fields used: title, body, head_ref, base_ref.  
  
### PullRequest

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
      "body": string,
      "headRef": string,
      "baseRef": string,
      "author": string,
      "createTime": string,
      "updateTime": string,
      "mergeTime": string,
      "closeTime": string,
      "declineTime": string,
      "state": enum ([State](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.State)),
      "mergeability": enum ([Mergeability](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.Mergeability)),
      "htmlUrl": string
    }  
  
Fields  
---  
`id` |  `string` Required. The ID of the PR.  
`title` |  `string` Required. The title of the PR.  
`body` |  `string` Optional. The body description of the PR.  
`headRef` |  `string` Required. The source commit SHA of the head branch.  
`baseRef` |  `string` Required. The target commit SHA of the base branch.  
`author` |  `string` Output only. The username of the author.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mergeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was merged.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`closeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was closed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`declineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was declined. Only set for SCM providers that support declining pull requests. Never set for GitHub, GitHub Enterprise, GitLab, or GitLab Enterprise, where a pull request closed without being merged is `CLOSED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.State)`)` Output only. The current state of the PR.  
`mergeability` |  `enum (`[Mergeability](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.Mergeability)`)` Output only. The mergeability state of the pull request.  
`htmlUrl` |  `string` Output only. The HTML URL of the pull request on the SCM provider.  
  
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
  
### State

The state of the PR.

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`OPEN` | The PR is open.  
`CLOSED` | The PR is closed.  
`MERGED` | The PR is merged.  
`DECLINED` | The PR is declined. Only used by SCM providers that support declining pull requests. Never used for GitHub, GitHub Enterprise, GitLab, or GitLab Enterprise, where a pull request closed without being merged is `CLOSED`.  
  
### Mergeability

The mergeability state of a pull request.

Enums  
---  
`MERGEABILITY_UNSPECIFIED` | Mergeability state is unspecified.  
`MERGEABLE` | The pull request can be merged cleanly without Git conflicts.  
`CONFLICTING` | The pull request has merge conflicts and cannot be merged cleanly.  
`COMPUTING` | The mergeability state is currently being computed asynchronously by the upstream SCM provider.  
  
## Output Schema

Message representing a SCM Pull Request.

### PullRequest

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
      "body": string,
      "headRef": string,
      "baseRef": string,
      "author": string,
      "createTime": string,
      "updateTime": string,
      "mergeTime": string,
      "closeTime": string,
      "declineTime": string,
      "state": enum ([State](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.State)),
      "mergeability": enum ([Mergeability](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.Mergeability)),
      "htmlUrl": string
    }  
  
Fields  
---  
`id` |  `string` Required. The ID of the PR.  
`title` |  `string` Required. The title of the PR.  
`body` |  `string` Optional. The body description of the PR.  
`headRef` |  `string` Required. The source commit SHA of the head branch.  
`baseRef` |  `string` Required. The target commit SHA of the base branch.  
`author` |  `string` Output only. The username of the author.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mergeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was merged.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`closeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was closed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`declineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was declined. Only set for SCM providers that support declining pull requests. Never set for GitHub, GitHub Enterprise, GitLab, or GitLab Enterprise, where a pull request closed without being merged is `CLOSED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.State)`)` Output only. The current state of the PR.  
`mergeability` |  `enum (`[Mergeability](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request#Input.Schema.Mergeability)`)` Output only. The mergeability state of the pull request.  
`htmlUrl` |  `string` Output only. The HTML URL of the pull request on the SCM provider.  
  
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
  
### State

The state of the PR.

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`OPEN` | The PR is open.  
`CLOSED` | The PR is closed.  
`MERGED` | The PR is merged.  
`DECLINED` | The PR is declined. Only used by SCM providers that support declining pull requests. Never used for GitHub, GitHub Enterprise, GitLab, or GitLab Enterprise, where a pull request closed without being merged is `CLOSED`.  
  
### Mergeability

The mergeability state of a pull request.

Enums  
---  
`MERGEABILITY_UNSPECIFIED` | Mergeability state is unspecified.  
`MERGEABLE` | The pull request can be merged cleanly without Git conflicts.  
`CONFLICTING` | The pull request has merge conflicts and cannot be merged cleanly.  
`COMPUTING` | The mergeability state is currently being computed asynchronously by the upstream SCM provider.  
  
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
