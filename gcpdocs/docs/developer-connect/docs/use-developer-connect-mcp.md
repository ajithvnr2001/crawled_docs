---
url: https://docs.cloud.google.com/developer-connect/docs/use-developer-connect-mcp/
title: Use the Developer Connect MCP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:21:43.252987+00:00
---

# Use the Developer Connect MCP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/use-developer-connect-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Use the Developer Connect MCP server Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to use the Developer Connect remote Model Context Protocol (MCP) server to connect with AI applications including Antigravity, ChatGPT, Claude, and custom applications you are developing. You can use the Developer Connect remote Model Context Protocol (MCP) server to connect with AI applications, including Antigravity, ChatGPT, Claude, and custom applications you or your organization are developing. 

The Developer Connect remote MCP server lets your AI applications and coding assistants work with the source code repositories that you've linked to Developer Connect, using one set of tools that works the same way for GitHub, GitHub Enterprise, GitLab, and GitLab Enterprise. Agents can read commits, diffs, blame, and pull requests, and open, comment on, and update pull requests, without requiring SCM credentials. The Developer Connect remote MCP server is enabled when you enable the Developer Connect API. 

[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) standardizes how large language models (LLMs) and AI applications or agents connect to external data sources. MCP servers let you use their tools, resources, and prompts to take actions and get updated data from their backend service.

## What's the difference between local and remote MCP servers?

Local MCP servers
    Typically run on your local machine and use the standard input and output streams (stdio) for communication between services on the same device.
Remote MCP servers
    Run on the service's infrastructure and offer an HTTP endpoint to AI applications for communication between the AI MCP client and the MCP server. For more information about MCP architecture, see [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

## Stateless core

With [MCP version 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28), MCP changes from a bidirectional, stateful protocol to a stateless protocol. Each MCP request is self-describing and can be routed using headers. There isn't a need for the `initialize`/`initialized` handshake or `Mcp-Session-Id` because each request includes all the information needed in HTTP headers or the `_meta` parameter. MCP servers can request additional information required by a tool through [multi-round-trip requests (MRTR)](https://modelcontextprotocol.io/specification/latest/basic/patterns/mrtr).

To help route and process requests without parsing the request body, some MCP headers are required, including the following:

  * Headers that are required by the MCP specification such as the [protocol version header](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#protocol-version-header) and [standard request headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#standard-request-headers).
  * [Custom headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#custom-headers-from-tool-parameters) that are defined by the MCP server. These headers are mirrored into HTTP headers from the tool's input schema using the `x-mcp-header` property. For example, an MCP server might define a custom header to specify the Google Cloud region or project ID.



For more information about MCP architecture, see the MCP version 2026-07-28 [specification](https://modelcontextprotocol.io/specification/2026-07-28) and [key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Google and Google Cloud remote MCP servers

Google and Google Cloud remote MCP servers have the following features and benefits: 

  * Simplified, centralized discovery
  * Managed global or regional HTTP endpoints
  * Fine-grained authorization
  * Optional prompt and response security with Model Armor protection
  * Centralized audit logging



For information about other MCP servers and information about security and governance controls available for Google Cloud MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

## Before you begin

Before you can use the Developer Connect MCP server to work with a repository, you must [have a Developer Connect connection to your source code management (SCM) provider and a Git repository link for the repository](https://docs.cloud.google.com/developer-connect/docs/connect-repo).

**Note:** During Preview, the tools that open and modify pull requests (`open-repo-pull-request`, `modify-repo-pull-request`, `add-repo-pull-request-comment`, and `add-repo-pull-request-review-comment`) are available only to approved projects. For other projects, these tools return a `FAILED_PRECONDITION` error. To request access, contact your Google Cloud account team. The tools that read repositories and pull requests are available to all projects.

### Required roles

To get the permissions that you need to use the Developer Connect MCP server, ask your administrator to grant you the following IAM roles on the project that contains your Developer Connect connections: 

  * Make MCP tool calls: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 
  * List connections and Git repository links: [Developer Connect Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.viewer) (`roles/developerconnect.viewer`) 
  * Read commits, diffs, blame, and pull requests, and open, comment on, and modify pull requests (approved projects only during Preview): [Developer Connect User ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.user) (`roles/developerconnect.user`) 
  * Create connections and Git repository links: [Developer Connect Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.admin) (`roles/developerconnect.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Developer Connect MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Developer Connect MCP server:

  * Make MCP tool calls: `mcp.tools.call`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authentication and authorization

The Developer Connect remote MCP server uses the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers. 

The Developer Connect MCP server requires a principal for Identity and Access Management (IAM) control and doesn't accept API keys. We recommend that you create a separate identity for agents that use MCP tools so that you can control and monitor access to resources.

The MCP server never returns SCM tokens or other credentials to the agent. Developer Connect uses the credentials stored with each connection to call the SCM provider. To limit which repositories an agent can use, grant roles on specific connections, or use [tags and deny policies](https://docs.cloud.google.com/developer-connect/docs/control-repository-access-with-tags).

For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Developer Connect MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine if an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, see [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2).

Developer Connect has the following MCP tool OAuth scopes:

Scope URI for Google Cloud CLI | Description  
---|---  
`https://www.googleapis.com/auth/cloud-platform` | Full access to all Google Cloud resources.  
  
Additional permissions might be required on the resources accessed during a tool call. To view a list of roles and permissions required for Developer Connect, see [Access control with IAM](https://docs.cloud.google.com/developer-connect/docs/access-control).

## Configure an MCP client to use the Developer Connect MCP server

AI applications and agents, such as Claude or Antigravity, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. If your application isn't listed in the [client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance), then you can use the following information to connect from most applications. 

  * **Server name** : Developer Connect MCP server
  * **Server URL** or **Endpoint** : `https://developerconnect.googleapis.com/mcp`. The Developer Connect MCP server is only available on the global endpoint.
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : the [OAuth 2.0 scope](https://developers.google.com/identity/protocols/oauth2/scopes) that you want to use when connecting to the Developer Connect MCP server.

For application-specific guidance about setting up and connecting to MCP server, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance). 

For more general guidance, see the following resources:

  * [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers).
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).



## Available tools

To view details of available MCP tools and their descriptions for the Developer Connect MCP server, see the [Developer Connect MCP reference](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp).

Most tools take the resource name of a Git repository link, in the format `projects/PROJECT_ID/locations/LOCATION/connections/CONNECTION_ID/gitRepositoryLinks/LINK_ID`. An agent can find it with the `list-connections` and `list-repo-links` tools.

The `fetch-repo-commit` and `diff-repo-commit` tools return only file paths and change statuses by default. To also return the line-by-line changes, pass `path_filters`, for example `["**"]` for all files.

### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Developer Connect remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://developerconnect.googleapis.com/mcp \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -d '{
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/list"
        }'
    

## Example use cases

Connecting an AI agent or IDE assistant to the Developer Connect MCP server lets you review and change code across SCM providers using natural language.

You can use the Developer Connect MCP server for the following use cases:

  * **Review changes:** Let an agent read the commits and diffs between two branches or commits, and summarize or review them.
  * **Investigate code history:** Find which commits changed specific lines of a file, and read their commit messages.
  * **Automate pull request workflows:** Open pull requests, add discussion and inline review comments, and update or close pull requests. During Preview, this use case is available only to approved projects.



### Example prompts

The following are example prompts you can use with your connected AI application:

  * **Summarize a change:** "Summarize the diff between `main` and `feature/login` in `https://github.com/my-org/my-repo`."
  * **Review a pull request:** "List the files changed in pull request #42 in `my-repo` and point out any function that's missing error handling."
  * **Trace a line:** "Who last changed lines 10 to 20 of `service.go` on `main`, and why?"



The following prompts use tools that, during Preview, are available only to approved projects:

  * **Open a pull request:** "Open a pull request from `feature/login` to `main` in `my-repo` titled 'Add login page'."
  * **Comment on a pull request:** "Add an inline comment on line 45 of `auth.go` in pull request #42 suggesting better error handling."



## Optional security and safety configurations

MCP introduces new security risks and considerations due to the wide variety of actions that you can do with the MCP tools. To minimize and manage these risks, Google Cloud offers default settings and customizable policies to control the use of MCP tools in your Google Cloud organization or project.

For more information about MCP security and governance, see [AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).

### Use Model Armor

[Model Armor](https://docs.cloud.google.com/model-armor/overview) is a Google Cloud service designed to enhance the security and safety of your AI applications. It works by proactively screening LLM prompts and responses, protecting against various risks and supporting responsible AI practices. Whether you are deploying AI in your cloud environment, or on external cloud providers, Model Armor can help you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce your AI safety and security policies consistently across your diverse AI landscape.

When Model Armor is enabled with [logging enabled](https://docs.cloud.google.com/model-armor/configure-logging), Model Armor logs the entire payload. This might expose sensitive information in your logs.

#### MCP request routing to Model Armor

The Developer Connect MCP server is only available on the global endpoint, which uses [cross-jurisdictional routing](https://docs.cloud.google.com/mcp/model-armor-supported-products#cross-jurisdictional-routing). When you enable Model Armor, the MCP server always sends requests and responses to Model Armor. For more information about the behavior of other MCP servers, see [Model Armor supported products](https://docs.cloud.google.com/mcp/model-armor-supported-products). 

Tool responses often contain source code and diffs. Sensitive Data Protection de-identification can change identifiers in code, which makes diffs invalid. If your agents work with code, consider leaving Sensitive Data Protection off in your Model Armor configuration for Developer Connect, and use prompt injection and jailbreak detection, malicious URL detection, and Responsible AI filters.

#### Enable Model Armor

You must enable Model Armor APIs before you can use Model Armor.

###  Console 

  1. Enable the Model Armor API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=modelarmor.googleapis.com)

  2. Select the project where you want to activate Model Armor.




###  gcloud 

Before you begin, follow these steps using the Google Cloud CLI with the Model Armor API:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command to set the API endpoint for the Model Armor service.
         
         gcloud config set api_endpoint_overrides/modelarmor "https://modelarmor.LOCATION.rep.googleapis.com/"

Replace `LOCATION` with the region where you want to use Model Armor.




#### Configure protection for MCP servers

To help protect your MCP tool calls and responses you can use Model Armor floor settings. A floor setting defines the minimum security filters that apply across the project. This configuration applies a consistent set of filters to all MCP tool calls and responses within the project.

**Tip:** Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data.

Set up a Model Armor floor setting with MCP sanitization enabled. For more information, see [Configure Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings).

**Note:** If the agent and the MCP server are in different projects, you can create floor settings in both projects (the client project and the resource project). In this case, Model Armor is invoked twice, once for each project.

See the following example command:
    
    
    gcloud model-armor floorsettings update \
    --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
    --enable-floor-setting-enforcement=TRUE \
    --add-integrated-services=GOOGLE_MCP_SERVER \
    --google-mcp-server-enforcement-type=INSPECT_AND_BLOCK \
    --enable-google-mcp-server-cloud-logging \
    --malicious-uri-filter-settings-enforcement=ENABLED \
    --add-rai-settings-filters='[{"confidenceLevel": "MEDIUM_AND_ABOVE", "filterType": "DANGEROUS"}]'

Replace `PROJECT_ID` with your Google Cloud project ID.

Note the following settings:

  * `INSPECT_AND_BLOCK`: The enforcement type that inspects content for the Google MCP server and blocks prompts and responses that match the filters.
  * `ENABLED`: The setting that enables a filter or enforcement.
  * `MEDIUM_AND_ABOVE`: The confidence level for the Responsible AI - Dangerous filter settings. You can modify this setting, though lower values might result in more false positives. For more information, see [Model Armor confidence levels](https://docs.cloud.google.com/model-armor/overview#ma-confidence-levels).



#### Disable scanning MCP traffic with Model Armor

To stop Model Armor from automatically scanning traffic to and from Google MCP servers based on the project's floor settings, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
      --remove-integrated-services=GOOGLE_MCP_SERVER
    

Replace `PROJECT_ID` with the Google Cloud project ID. Model Armor doesn't automatically apply the rules defined in this project's floor settings to any Google MCP server traffic.

Model Armor floor settings and general configuration can impact more than just MCP. Because Model Armor integrates with services like Vertex AI, any changes you make to floor settings can affect traffic scanning and safety behaviors across all integrated services, not just MCP.

### Control MCP use with IAM policies

Identity and Access Management (IAM) [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) and [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies) help you secure Google Cloud and Google MCP servers.

You can combine multiple criteria to build customized security and governance policies by allowing or denying access based on the following:

  * The principal.
  * Tool properties like the read-only attribute.
  * The service name or tool name.
  * The application's OAuth client ID.



For more information, see [Control MCP use with Identity and Access Management](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## What's next

  * Review the [Developer Connect MCP reference documentation](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).
  * Learn more about [Access control with IAM](https://docs.cloud.google.com/developer-connect/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
