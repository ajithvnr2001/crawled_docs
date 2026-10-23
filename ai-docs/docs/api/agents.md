---
url: https://ai.google.dev/api/agents/
title: Gemini Agents API
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:00:16.098450+00:00
---

# Gemini Agents API

> Source: https://ai.google.dev/api/agents/

Agents are systems that leverage Gemini models, a set of tools, and reasoning capabilities to perform complex, multi-step tasks and achieve specific goals. Unlike a single model call, an agent can plan, execute a series of actions, interact with external systems, and synthesize information to fulfill a user's request.

[View as markdown](https://ai.google.dev/static/api/agents.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)

## CreateAgent

post  https://generativelanguage.googleapis.com/v1beta/agents 

Creates a new Agent (Typed version for SDK).

  * Path / Query parameters
  * Request body
  * Response



### Path / Query Parameters

parent string (required)

Required. The parent resource where this agent will be created. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure:

agent_config AntigravityAgentConfig (optional)

Configuration parameters for the agent.

Configuration for the Antigravity agent runtime. Provides server-side control over the agent's execution environment and tool configuration.

#### Fields

type object (required)

No description provided.

Always set to `"antigravity"`.

model string (optional)

The model to use for agent reasoning.

max_total_tokens string (optional)

Max total tokens for the agent run.

base_environment EnvironmentConfig or string (optional)

The environment configuration for the agent.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

The unique identifier for the agent.

base_agent string (optional)

The base agent to extend.

system_instruction string (optional)

System instruction for the agent.

description string (optional)

Agent description for developers to quickly read and understand.

tools array (AgentTool) (optional)

The tools available to the agent.

A tool that the agent can use.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

Function

A tool that can be used by the model.

type object (required)

No description provided.

Always set to `"function"`.

name string (optional)

The name of the function.

description string (optional)

A description of the function.

parameters object (optional)

The JSON Schema for the function's parameters. Supports a subset of JSON Schema. `minLength`, `maxLength`, `minProperties`, `maxProperties`, `uniqueItems`, `contains`, `minContains`, and `maxContains` are ignored and not enforced.

GoogleSearch

A tool that can be used by the model to search Google.

type object (required)

No description provided.

Always set to `"google_search"`.

search_types array (enum (string)) (optional)

The types of search grounding to enable.

Possible values:

  * `web_search`

Setting this field enables web search. Only text results are returned.

  * `image_search`

Setting this field enables image search. Image bytes are returned.




McpServer

A MCPServer is a server that can be called by the model to perform actions.

type object (required)

No description provided.

Always set to `"mcp_server"`.

url string (optional)

The full URL for the MCPServer endpoint. Example: "https://api.example.com/mcp"

name string (optional)

The name of the MCPServer.

headers object (optional)

Optional: Fields for authentication headers, timeouts, etc., if needed.

allowed_tools array (AllowedTools) (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

mode enum (string) (optional)

The mode of the tool choice.

Possible values:

  * `auto`

Auto tool choice.

  * `any`

Any tool choice.

  * `none`

No tool choice.

  * `validated`

Validated tool choice.




tools array (string) (optional)

The names of the allowed tools.

UrlContext

A tool that can be used by the model to fetch URL context.

type object (required)

No description provided.

Always set to `"url_context"`.

### Response

If successful, the response body contains data with the following structure:

agent_config AntigravityAgentConfig (optional)

Configuration parameters for the agent.

Configuration for the Antigravity agent runtime. Provides server-side control over the agent's execution environment and tool configuration.

#### Fields

type object (required)

No description provided.

Always set to `"antigravity"`.

model string (optional)

The model to use for agent reasoning.

max_total_tokens string (optional)

Max total tokens for the agent run.

base_environment EnvironmentConfig or string (optional)

The environment configuration for the agent.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

The unique identifier for the agent.

base_agent string (optional)

The base agent to extend.

system_instruction string (optional)

System instruction for the agent.

description string (optional)

Agent description for developers to quickly read and understand.

tools array (AgentTool) (optional)

The tools available to the agent.

A tool that the agent can use.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

Function

A tool that can be used by the model.

type object (required)

No description provided.

Always set to `"function"`.

name string (optional)

The name of the function.

description string (optional)

A description of the function.

parameters object (optional)

The JSON Schema for the function's parameters. Supports a subset of JSON Schema. `minLength`, `maxLength`, `minProperties`, `maxProperties`, `uniqueItems`, `contains`, `minContains`, and `maxContains` are ignored and not enforced.

GoogleSearch

A tool that can be used by the model to search Google.

type object (required)

No description provided.

Always set to `"google_search"`.

search_types array (enum (string)) (optional)

The types of search grounding to enable.

Possible values:

  * `web_search`

Setting this field enables web search. Only text results are returned.

  * `image_search`

Setting this field enables image search. Image bytes are returned.




McpServer

A MCPServer is a server that can be called by the model to perform actions.

type object (required)

No description provided.

Always set to `"mcp_server"`.

url string (optional)

The full URL for the MCPServer endpoint. Example: "https://api.example.com/mcp"

name string (optional)

The name of the MCPServer.

headers object (optional)

Optional: Fields for authentication headers, timeouts, etc., if needed.

allowed_tools array (AllowedTools) (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

mode enum (string) (optional)

The mode of the tool choice.

Possible values:

  * `auto`

Auto tool choice.

  * `any`

Any tool choice.

  * `none`

No tool choice.

  * `validated`

Validated tool choice.




tools array (string) (optional)

The names of the allowed tools.

UrlContext

A tool that can be used by the model to fetch URL context.

type object (required)

No description provided.

Always set to `"url_context"`.

### Create Agent

####  Example Response
    
    
    {
      "description": "A helpful research assistant.",
      "base_agent": "antigravity-preview-05-2026",
      "base_environment": "remote",
      "id": "research-assistant-abc123",
      "system_instruction": "You are a helpful research assistant.",
      "tools": [
        {
          "type": "google_search"
        }
      ]
    }

### Agent with Sources

####  Example Response
    
    
    {
      "base_agent": "antigravity-preview-05-2026",
      "base_environment": {
        "type": "remote",
        "sources": [
          {
            "type": "inline",
            "content": "Always use matplotlib for charts. Include a summary table in every report.",
            "target": ".agents/AGENTS.md"
          },
          {
            "type": "repository",
            "source": "https://github.com/my-org/analysis-templates",
            "target": "/workspace/templates"
          }
        ]
      },
      "id": "data-analyst-abc123",
      "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF."
    }

### Agent Forked from Environment

####  Example Response
    
    
    {
      "base_agent": "antigravity-preview-05-2026",
      "base_environment": "env_abc123",
      "id": "my-data-analyst-abc123",
      "system_instruction": "You are a data analyst. Use the template at /workspace/template.py for all reports."
    }

## ListAgents

get  https://generativelanguage.googleapis.com/v1beta/agents 

Lists all Agents.

  * Path / Query parameters
  * Response



### Path / Query Parameters

parent string (required)

Required. The parent resource to list agents from. Format: `projects/{project}/locations/{location}`

page_size integer (optional)

No description provided.

page_token string (optional)

No description provided.

### Response

If successful, the response body contains data with the following structure:

agents array (Agent) (optional)

The list of agents.

next_page_token string (optional)

A token to retrieve the next page of results.

### List Agents

####  Example Response
    
    
    {
      "agents": [
        {
          "description": "A helpful research assistant.",
          "base_agent": "antigravity-preview-05-2026",
          "id": "research-assistant-abc123",
          "system_instruction": "You are a helpful research assistant.",
          "tools": [
            {
              "type": "google_search"
            }
          ]
        }
      ]
    }

## GetAgent

get  https://generativelanguage.googleapis.com/v1beta/agents/{agentsId} 

Gets a specific Agent.

  * Path / Query parameters
  * Response



### Path / Query Parameters

agentsId string (required)

Required. The name of the agent to retrieve.

### Response

If successful, the response body contains data with the following structure:

agent_config AntigravityAgentConfig (optional)

Configuration parameters for the agent.

Configuration for the Antigravity agent runtime. Provides server-side control over the agent's execution environment and tool configuration.

#### Fields

type object (required)

No description provided.

Always set to `"antigravity"`.

model string (optional)

The model to use for agent reasoning.

max_total_tokens string (optional)

Max total tokens for the agent run.

base_environment EnvironmentConfig or string (optional)

The environment configuration for the agent.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

The unique identifier for the agent.

base_agent string (optional)

The base agent to extend.

system_instruction string (optional)

System instruction for the agent.

description string (optional)

Agent description for developers to quickly read and understand.

tools array (AgentTool) (optional)

The tools available to the agent.

A tool that the agent can use.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

Function

A tool that can be used by the model.

type object (required)

No description provided.

Always set to `"function"`.

name string (optional)

The name of the function.

description string (optional)

A description of the function.

parameters object (optional)

The JSON Schema for the function's parameters. Supports a subset of JSON Schema. `minLength`, `maxLength`, `minProperties`, `maxProperties`, `uniqueItems`, `contains`, `minContains`, and `maxContains` are ignored and not enforced.

GoogleSearch

A tool that can be used by the model to search Google.

type object (required)

No description provided.

Always set to `"google_search"`.

search_types array (enum (string)) (optional)

The types of search grounding to enable.

Possible values:

  * `web_search`

Setting this field enables web search. Only text results are returned.

  * `image_search`

Setting this field enables image search. Image bytes are returned.




McpServer

A MCPServer is a server that can be called by the model to perform actions.

type object (required)

No description provided.

Always set to `"mcp_server"`.

url string (optional)

The full URL for the MCPServer endpoint. Example: "https://api.example.com/mcp"

name string (optional)

The name of the MCPServer.

headers object (optional)

Optional: Fields for authentication headers, timeouts, etc., if needed.

allowed_tools array (AllowedTools) (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

mode enum (string) (optional)

The mode of the tool choice.

Possible values:

  * `auto`

Auto tool choice.

  * `any`

Any tool choice.

  * `none`

No tool choice.

  * `validated`

Validated tool choice.




tools array (string) (optional)

The names of the allowed tools.

UrlContext

A tool that can be used by the model to fetch URL context.

type object (required)

No description provided.

Always set to `"url_context"`.

### Get Agent

####  Example Response
    
    
    {
      "created": "2025-11-26T12:25:15Z",
      "display_name": "My Research Agent",
      "id": "ag_abc123",
      "object": "agent",
      "system_instruction": "You are a helpful research assistant.",
      "tools": [
        {
          "type": "google_search"
        }
      ],
      "updated": "2025-11-26T12:25:15Z"
    }

## DeleteAgent

delete  https://generativelanguage.googleapis.com/v1beta/agents/{agentsId} 

Deletes an Agent.

  * Path / Query parameters
  * Response



### Path / Query Parameters

agentsId string (required)

Required. The name of the agent to delete.

### Response

If successful, the response is empty.

### Delete Agent

## Resources

### Agent

An agent definition for the CreateAgent API. This message is the target for annotation-parser-based JSON parsing. New format: { "id": "customer-sentinel", "base_agent": "", "system_instruction": "...", "base_environment": { "type": "remote", "sources": [...] }, "tools": [ {"type": "code_execution"} ] }

#### Fields

agent_config AntigravityAgentConfig (optional)

Configuration parameters for the agent.

Configuration for the Antigravity agent runtime. Provides server-side control over the agent's execution environment and tool configuration.

#### Fields

type object (required)

No description provided.

Always set to `"antigravity"`.

model string (optional)

The model to use for agent reasoning.

max_total_tokens string (optional)

Max total tokens for the agent run.

base_environment EnvironmentConfig or string (optional)

The environment configuration for the agent.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

The unique identifier for the agent.

base_agent string (optional)

The base agent to extend.

system_instruction string (optional)

System instruction for the agent.

description string (optional)

Agent description for developers to quickly read and understand.

tools array (AgentTool) (optional)

The tools available to the agent.

A tool that the agent can use.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

Function

A tool that can be used by the model.

type object (required)

No description provided.

Always set to `"function"`.

name string (optional)

The name of the function.

description string (optional)

A description of the function.

parameters object (optional)

The JSON Schema for the function's parameters. Supports a subset of JSON Schema. `minLength`, `maxLength`, `minProperties`, `maxProperties`, `uniqueItems`, `contains`, `minContains`, and `maxContains` are ignored and not enforced.

GoogleSearch

A tool that can be used by the model to search Google.

type object (required)

No description provided.

Always set to `"google_search"`.

search_types array (enum (string)) (optional)

The types of search grounding to enable.

Possible values:

  * `web_search`

Setting this field enables web search. Only text results are returned.

  * `image_search`

Setting this field enables image search. Image bytes are returned.




McpServer

A MCPServer is a server that can be called by the model to perform actions.

type object (required)

No description provided.

Always set to `"mcp_server"`.

url string (optional)

The full URL for the MCPServer endpoint. Example: "https://api.example.com/mcp"

name string (optional)

The name of the MCPServer.

headers object (optional)

Optional: Fields for authentication headers, timeouts, etc., if needed.

allowed_tools array (AllowedTools) (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

mode enum (string) (optional)

The mode of the tool choice.

Possible values:

  * `auto`

Auto tool choice.

  * `any`

Any tool choice.

  * `none`

No tool choice.

  * `validated`

Validated tool choice.




tools array (string) (optional)

The names of the allowed tools.

UrlContext

A tool that can be used by the model to fetch URL context.

type object (required)

No description provided.

Always set to `"url_context"`.
