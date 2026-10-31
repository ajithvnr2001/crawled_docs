---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/diff-repo-commit/
title: MCP Tools Reference: developerconnect.googleapis.com \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:06.462035+00:00
---

# MCP Tools Reference: developerconnect.googleapis.com  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/diff-repo-commit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  MCP Tools Reference: developerconnect.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `diff-repo-commit`

Get the diff between two commits in a Git repository. To retrieve line-by-line patch hunks, pass path_filters (for example, ['**'] for all files).

The following code sample shows how to use `curl` to call the `diff-repo-commit` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://developerconnect.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "diff-repo-commit",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for DiffGitRepositoryLinkCommit.

### DiffGitRepositoryLinkCommitRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "baseSha": string,
      "headSha": string,
      "pathFilters": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink.  
`baseSha` |  `string` Required. The base commit SHA or ref.  
`headSha` |  `string` Required. The head commit SHA or ref.  
`pathFilters[]` |  `string` Optional. Path patterns or exact paths to filter returned files. When `path_filters` is specified, `FileDiff.patch` is populated for all matching files (use `["**"]` to include patches for all changed files). When `path_filters` is omitted or empty, the full list of `FileDiff` is returned without patch diffs (`FileDiff.patch` is empty).  
  
## Output Schema

Response message for DiffGitRepositoryLinkCommit.

### DiffGitRepositoryLinkCommitResponse

JSON representation  
---  
      
    
    {
      "files": [
        {
          object ([FileDiff](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit#Output.Schema.FileDiff))
        }
      ]
    }  
  
Fields  
---  
`files[]` |  `object (`[FileDiff](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit#Output.Schema.FileDiff)`)` The file diff extracted from the unified diff.  
  
### FileDiff

JSON representation  
---  
      
    
    {
      "path": string,
      "status": string,
      "patch": string
    }  
  
Fields  
---  
`path` |  `string` Relative path to the file in the repository.  
`status` |  `string` Status of change: "ADDED", "MODIFIED", "REMOVED", "RENAMED".  
`patch` |  `string` Standard unified diff patch hunk for the file. Only populated when `path_filters` is specified in the request; otherwise empty.  
  
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
