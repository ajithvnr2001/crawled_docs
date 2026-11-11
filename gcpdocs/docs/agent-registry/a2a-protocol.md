---
url: https://docs.cloud.google.com/agent-registry/a2a-protocol/
title: A2A protocol \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:38:35.094378+00:00
---

# A2A protocol  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/a2a-protocol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  A2A protocol Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry indexes [Agent2Agent (A2A) Agent Cards](https://agent2agent.info/docs/concepts/agentcard/), transport interfaces, and inline skills so you and your orchestrator agents can discover and call agents across your Google Cloud environment. Autonomous AI agents can use the [A2A protocol](https://a2a-protocol.org/) to exchange messages and delegate tasks without sharing their internal state, prompts, or tools.

## Relationship between AI agents, A2A, and MCP

Multi-agent architectures can combine the following open standards that Agent Registry catalogs:

  * **Agent2Agent (A2A) protocol** : standardizes peer-to-peer communication between an A2A client, such as an orchestrator agent or user-facing application, and a remote A2A agent. The client sends natural language or structured messages and receives stateful task updates or artifacts without requiring visibility into the remote agent's underlying model, memory substrate, or internal reasoning loop. Agent Registry catalogs both built-in Google agents exposed by Google Cloud APIs and custom A2A agents that you deploy in your own environment. For an architectural example of hosting custom A2A agents, see [Overview of A2A agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai/a2a-agents).
  * **Model Context Protocol (MCP)** : standardizes client-to-server tool execution, where an agent connects to an [MCP server](https://docs.cloud.google.com/mcp/overview#how-mcp-works) to call deterministic tools and read structured data resources.



In Agent Registry, your orchestrator agent can query a single registry to discover specialist A2A subagents for multi-step delegation, alongside MCP servers and standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture) for direct tool use.

## Protocol versions and Agent Card discovery

Every A2A-compliant agent describes its identity, endpoints, and capabilities in a JSON metadata document called the [Agent Card](https://agent2agent.info/docs/concepts/agentcard/) (`agent-card.json`).

Agent Registry supports versions `1.0` (recommended) and `0.3` of the [A2A protocol specification](https://a2a-protocol.org/latest/specification/). For information about specific Agent Card fields and structures of these versions, see [Agent Card schema](https://docs.cloud.google.com/agent-registry/json-schemas#agent-card).

### How Agent Registry indexes Agent Cards

Whether an A2A agent is ingested through [automatic registration](https://docs.cloud.google.com/agent-registry/automatic-registration) or added through [manual registration](https://docs.cloud.google.com/agent-registry/manual-registration), Agent Registry validates its Agent Card and creates a read-only `Agent` discovery resource with the following information:

  * **Agent Card payload** : Agent Registry stores the full JSON payload in the `card` field of the `Agent` resource with `type` set to `A2A_AGENT_CARD`.
  * **Discovery fields** : Agent Registry extracts the agent's `displayName`, `description`, `version`, transport `protocols`, and inline `skills` from the Agent Card and stores them in the `Agent` resource. You can search and filter these capabilities without fetching individual `/.well-known/agent-card.json` endpoints across services.



Google Cloud services and governed runtimes don't always expose a public `/.well-known/agent-card.json` URL. Instead, you and your client applications retrieve the Agent Card directly from Agent Registry. Some agents also provide an extended Agent Card with additional details that are available only to authenticated clients. If an Agent Card sets `capabilities.extendedAgentCard` to `true`, authenticated clients can get the extended Agent Card on the agent's runtime endpoint to retrieve those details.

## Transport bindings and core operations

A transport binding defines how a client formats and sends requests to an A2A agent over the network. The A2A protocol supports the following transport options so agents built on different platforms can communicate:

  * **HTTP+JSON** : HTTPS requests that send and receive JSON payloads.
  * **JSON-RPC** : HTTPS requests that wrap the operation name and parameters inside a JSON-RPC message.
  * **gRPC** : binary gRPC calls over TLS for low-latency communication between services.



Agent Registry records each agent's supported transport types and the agent's endpoint URLs on the `Agent` resource. Because endpoint URLs vary across Google Cloud services and deployments, avoid hardcoding URLs in your code. Instead, look up the agent's endpoint URL and transport from Agent Registry at runtime.

Regardless of which transport an agent uses, clients interact with the agent through the same core A2A operations:

Operation | Description  
---|---  
`SendMessage` | Sends a message to start a new task or continue a conversation. The agent returns either an immediate reply or a task that you can track.  
`SendStreamingMessage` | Sends a message and streams live status updates, partial replies, and results as the agent works, when the agent supports streaming.  
`GetTask` | Checks the current status and retrieves any outputs for an existing task.  
`ListTasks` | Lists tasks in a conversation or project, when supported by the agent.  
`SubscribeToTask` | Reconnects to a running task to stream live updates until the task pauses or finishes.  
`CancelTask` | Requests that the agent stop an in-progress task, when cancellation is supported.  
`GetExtendedAgentCard` | Retrieves the agent's extended Agent Card with additional details available only to authenticated clients.  
  
## Task lifecycle and multi-turn state

A2A separates conversational continuity from individual units of execution using two identifiers:

  * **Context ID (`contextId`)**: groups related multi-turn interactions within a shared session so the remote agent can preserve conversational context across sequential requests.
  * **Task ID (`taskId`)**: identifies a specific asynchronous or synchronous unit of work created when an A2A client sends a message.



As a remote agent processes a request, the task transitions through the following A2A lifecycle states:

State | Category | Description  
---|---|---  
`TASK_STATE_SUBMITTED` | Active | The remote agent has accepted the request and queued the task for execution.  
`TASK_STATE_WORKING` | Active | The remote agent is actively reasoning, calling tools, or generating artifacts for the task.  
`TASK_STATE_INPUT_REQUIRED` | Paused | Execution is paused waiting for follow-up input, clarification, or human-in-the-loop confirmation on the same `taskId` and `contextId`.  
`TASK_STATE_AUTH_REQUIRED` | Paused | Execution is paused until the client completes authentication or a user consent flow for a downstream resource.  
`TASK_STATE_COMPLETED` | Terminal | The task finished successfully and returned its final response or output artifacts.  
`TASK_STATE_FAILED` | Terminal | The task stopped because of an execution or downstream service error.  
`TASK_STATE_CANCELED` | Terminal | The task was canceled before completion.  
`TASK_STATE_REJECTED` | Terminal | The remote agent declined to execute the requested task.  
  
## A2A skills, standalone skills, and MCP tools

Agent Registry indexes three distinct capability mechanisms so you can choose the right integration pattern for each workflow:

  * **Inline A2A skills** : the `skills` field in an agent's `Agent` discovery resource contains JSON metadata, including `id`, `name`, `description`, `tags`, and `examples`, embedded inside the Agent Card. Inline A2A skills advertise what high-level tasks an orchestrator agent can delegate to that remote agent over an A2A transport.
  * **Standalone skills** : independent `Skill` and `SkillRevision` top-level resources in Agent Registry contain versioned ZIP archives with instructions in a `SKILL.md` file and optional scripts. An agent downloads a standalone skill into its own context rather than delegating execution to another agent. For a full comparison between inline A2A skills and standalone skills, see [Differences between standalone and A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a).
  * **MCP tools** : the `tools` field in an `McpServer` discovery resource contains structured function schemas exposed by a registered [MCP server](https://docs.cloud.google.com/agent-registry/manage-mcp-tools) that an agent calls directly to query data or run deterministic operations.



## Runtime security, governance, and agent calls

Agent Registry serves as the catalog for discovering A2A agents. Runtime authentication, authorization, content inspection, audit logging, and quota enforcement occur when your client or orchestrator agent calls the target agent:

  * **Target agent endpoint lookup and calls** : look up target A2A agent endpoints and send messages using Agent Development Kit (ADK) or standard HTTP and Python clients. For more information, see [Build multi-agent systems and call A2A agents](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators).
  * **Authentication and credential scoping** : configure OAuth 2.0 access tokens, OpenID Connect (OIDC) ID tokens, [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), or [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/auth-manager-overview) [bindings](https://docs.cloud.google.com/agent-registry/authenticate-toolsets) for agent-to-agent calls.
  * **Access control and deny policies** : enforce runtime access permissions, Identity and Access Management (IAM) deny policies, and Identity-Aware Proxy (IAP) egress policies. For more information, see [Roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions#resource-access-control).
  * **Prompt and response inspection** : inspect supported A2A prompt and response payloads to help detect prompt injection and sensitive data exposure by configuring [Model Armor integration with Agent Gateway](https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration) and [service extension bindings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/extension-bindings-overview).
  * **Audit logging and quotas** : inspect audit records for A2A calls in [Agent Registry audit logging](https://docs.cloud.google.com/agent-registry/audit-logging) and plan for target agent and downstream service rate quotas in [Quotas and system limits](https://docs.cloud.google.com/agent-registry/quotas#agentic-quotas).



## What's next

  * [Search for agents, tools, and skills](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) across Agent Cards and inline A2A skills.
  * [Build multi-agent systems and call A2A agents](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators) using ADK or A2A clients.
  * Review [JSON schemas](https://docs.cloud.google.com/agent-registry/json-schemas#agent-card) for A2A Agent Cards.
  * Compare [standalone and inline A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
