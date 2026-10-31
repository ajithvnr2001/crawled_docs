---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/
title: MCP Reference: developerconnect.googleapis.com \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:10.459502+00:00
---

# MCP Reference: developerconnect.googleapis.com  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  MCP Reference: developerconnect.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

This is an MCP server that provides normalized APIs to 3P source code management systems.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Developer Connect API MCP server has the following global MCP endpoint:

  * https://developerconnect.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The developerconnect.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[fetch-repo-commit](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit)` |  Fetch details of a specific commit from a Git repository. To retrieve line-by-line patch hunks in FULL view, pass path_filters (for example, ['**'] for all files).   
`[fetch-repo-commit-list](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-commit-list)` |  Fetch a list of commits from a Git repository.   
`[diff-repo-commit](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/diff-repo-commit)` |  Get the diff between two commits in a Git repository. To retrieve line-by-line patch hunks, pass path_filters (for example, ['**'] for all files).   
`[open-repo-pull-request](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/open-repo-pull-request)` |  Open a pull request in the remote SCM repository.   
`[add-repo-pull-request-comment](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-comment)` |  Add a comment to a pull request.   
`[add-repo-pull-request-review-comment](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/add-repo-pull-request-review-comment)` |  Add a review comment (inline on diff) to a pull request.   
`[modify-repo-pull-request](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/modify-repo-pull-request)` |  Modify a pull request in the remote SCM repository.   
`[fetch-repo-file-blame](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-file-blame)` |  Fetch blame information for a specific file in a Git repository.   
`[fetch-repo-pull-request](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-pull-request)` |  Fetch details of a specific pull request from a Git repository.   
`[fetch-repo-pull-request-list](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/fetch-repo-pull-request-list)` |  Fetch a list of pull requests from a Git repository.   
`[create-connection](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection)` |  Creates a new Connection in a given project and location.   
`[create-repo-link](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-repo-link)` |  Creates a new GitRepositoryLink in a given project and location.   
`[list-connections](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/list-connections)` |  List connections in a given project and location.   
`[list-repo-links](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/list-repo-links)` |  List Git repository links under a connection.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://developerconnect.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
