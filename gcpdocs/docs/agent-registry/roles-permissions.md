---
url: https://docs.cloud.google.com/agent-registry/roles-permissions/
title: Roles and permissions \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:37:37.837694+00:00
---

# Roles and permissions  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) roles and permissions let you control who can view, register, and manage agents, Model Context Protocol (MCP) servers, tools, standalone skills, endpoints, and bindings in Agent Registry.

To grant Agent Registry IAM roles to users or groups on your [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) or your [management project](https://docs.cloud.google.com/agent-registry/boundaries-and-topology#management-project), use the IAM page in the Google Cloud console or the Google Cloud CLI. For details, see [Access control with IAM](https://docs.cloud.google.com/agent-registry/access-control) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Agent Registry roles

The following table describes Agent Registry IAM roles and their typical responsibilities:

**Caution:** Grant the **Agent Registry API Admin** (`roles/agentregistry.admin`) or **Agent Registry API Editor** (`roles/agentregistry.editor`) roles only to trusted administrators who manage the registry. Avoid granting these roles directly to agents. These roles contain permissions to create, delete, and update services, including modifying critical agent metadata and [tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) such as `readOnlyHint` or `destructiveHint`. Malicious changes to metadata and annotations can cause unintended and destructive consequences when an orchestrator agent uses the modified tool. Additionally, an agent with these permissions can explicitly enroll a malicious external agent into the registry.**Role** | **Description** | **Purpose**  
---|---|---  
**Agent Registry API Admin** (`roles/agentregistry.admin`) |  Full access to all Agent Registry resources, including agents, MCP servers, tools, endpoints, standalone skills, skill revisions, security findings, skill encryption specifications, bindings, and skill IAM policies. | 

  * Register and manage agents, MCP servers, tools, and endpoints.
  * Create, update, and delete standalone skills and skill revisions.
  * View and list security findings for skill revisions.
  * Configure customer-managed encryption keys (CMEK) for skills.
  * Create and manage bindings and skill IAM policies.

  
**Agent Registry API Editor** (`roles/agentregistry.editor`) |  Edit access to Agent Registry resources, including agents, MCP servers, tools, endpoints, standalone skills, and skill revisions. | 

  * Register and manage agents and MCP servers.
  * Update tool definitions and endpoints.
  * Create, update, and delete standalone skills and skill revisions.

  
**Agent Registry API Viewer** (`roles/agentregistry.viewer`) |  Read-only access to view and search agents, MCP servers, tools, standalone skills, skill revisions, publishers, skill encryption specifications, endpoints, and bindings. | 

  * Discover available agents, MCP servers, and tools.
  * View A2A skills, standalone skills, skill revisions, publishers, skill encryption specifications, endpoints, and bindings for integration.

  
**Agent Registry User** (`roles/agentregistry.user`) |  Read-only access to Agent Registry resources, plus access to create, update, and delete standalone skills, skill revisions, and scanning settings. | 

  * Create, update, and delete standalone skills and skill revisions without edit access to agents, MCP servers, or endpoints.
  * Keep version control for skill revisions, configure automated security scanning, and centrally manage active states of skills.

  
  
## Agent Registry permissions

The following table lists the permissions that each Agent Registry IAM role has:

Agent Registry API AdminAgent Registry API EditorAgent Registry API ViewerAgent Registry UserClear all

#### Agent Registry API Admin 

(`roles/agentregistry.admin`) Full access to Agent Registry API resources.  |  `agentregistry.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`
  * `agentregistry.aiApplications.get`
  * `agentregistry.aiApplications.getIamPolicy`
  * `agentregistry.aiApplications.list`
  * `agentregistry.aiApplications.setIamPolicy`
  * `agentregistry.bindings.create`
  * `agentregistry.bindings.delete`
  * `agentregistry.bindings.fetchAvailable`
  * `agentregistry.bindings.get`
  * `agentregistry.bindings.list`
  * `agentregistry.bindings.update`
  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`
  * `agentregistry.locations.get`
  * `agentregistry.locations.list`
  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`
  * `agentregistry.operations.cancel`
  * `agentregistry.operations.delete`
  * `agentregistry.operations.get`
  * `agentregistry.operations.list`
  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`
  * `agentregistry.services.create`
  * `agentregistry.services.delete`
  * `agentregistry.services.get`
  * `agentregistry.services.list`
  * `agentregistry.services.update`
  * `agentregistry.skillRevisions.create`
  * `agentregistry.skillRevisions.delete`
  * `agentregistry.skillRevisions.get`
  * `agentregistry.skillRevisions.list`
  * `agentregistry.skills.create`
  * `agentregistry.skills.delete`
  * `agentregistry.skills.get`
  * `agentregistry.skills.getIamPolicy`
  * `agentregistry.skills.list`
  * `agentregistry.skills.search`
  * `agentregistry.skills.setIamPolicy`
  * `agentregistry.skills.update`

  
---|---  
  
#### Agent Registry API Editor 

(`roles/agentregistry.editor`) Edit access to Agent Registry API resources.  |  `agentregistry.agents.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`

`agentregistry.aiApplications.get` `agentregistry.aiApplications.list` `agentregistry.bindings.fetchAvailable` `agentregistry.bindings.get` `agentregistry.bindings.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.locations.*`

  * `agentregistry.locations.get`
  * `agentregistry.locations.list`

`agentregistry.mcpServers.*`

  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`

`agentregistry.operations.*`

  * `agentregistry.operations.cancel`
  * `agentregistry.operations.delete`
  * `agentregistry.operations.get`
  * `agentregistry.operations.list`

`agentregistry.publishers.*`

  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`

`agentregistry.services.*`

  * `agentregistry.services.create`
  * `agentregistry.services.delete`
  * `agentregistry.services.get`
  * `agentregistry.services.list`
  * `agentregistry.services.update`

`agentregistry.skillRevisions.*`

  * `agentregistry.skillRevisions.create`
  * `agentregistry.skillRevisions.delete`
  * `agentregistry.skillRevisions.get`
  * `agentregistry.skillRevisions.list`

`agentregistry.skills.create` `agentregistry.skills.delete` `agentregistry.skills.get` `agentregistry.skills.list` `agentregistry.skills.search` `agentregistry.skills.update`  
  
#### Agent Registry API Viewer 

(`roles/agentregistry.viewer`) Readonly access to Agent Registry API resources.  |  `agentregistry.agents.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`

`agentregistry.aiApplications.get` `agentregistry.aiApplications.list` `agentregistry.bindings.fetchAvailable` `agentregistry.bindings.get` `agentregistry.bindings.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.locations.*`

  * `agentregistry.locations.get`
  * `agentregistry.locations.list`

`agentregistry.mcpServers.*`

  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`

`agentregistry.operations.get` `agentregistry.operations.list` `agentregistry.publishers.*`

  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`

`agentregistry.services.get` `agentregistry.services.list` `agentregistry.skillRevisions.get` `agentregistry.skillRevisions.list` `agentregistry.skills.get` `agentregistry.skills.list` `agentregistry.skills.search`  
  
#### Agent Registry User Beta

(`roles/agentregistry.user`) Create, update, and delete skills and skill revisions.  |  `agentregistry.agents.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`

`agentregistry.aiApplications.get` `agentregistry.aiApplications.list` `agentregistry.bindings.fetchAvailable` `agentregistry.bindings.get` `agentregistry.bindings.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.locations.*`

  * `agentregistry.locations.get`
  * `agentregistry.locations.list`

`agentregistry.mcpServers.*`

  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`

`agentregistry.operations.get` `agentregistry.operations.list` `agentregistry.publishers.*`

  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`

`agentregistry.services.get` `agentregistry.services.list` `agentregistry.skillRevisions.*`

  * `agentregistry.skillRevisions.create`
  * `agentregistry.skillRevisions.delete`
  * `agentregistry.skillRevisions.get`
  * `agentregistry.skillRevisions.list`

`agentregistry.skills.create` `agentregistry.skills.delete` `agentregistry.skills.get` `agentregistry.skills.list` `agentregistry.skills.search` `agentregistry.skills.update`  
  
For more information about IAM permissions, see [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) and [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Roles for cross-project management boundaries

When you configure a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) for your agentic components in Agent Registry, you must grant IAM roles to users or services at the following levels:

  * **Management project** : grant Agent Registry roles on the [management project](https://docs.cloud.google.com/agent-registry/boundaries-and-topology#management-project) to users or services that discover and manage agents across the boundary. Users with viewer access on the management project can discover and search agents and MCP servers from all member projects across every boundary attached to that management project without needing explicit viewer permissions granted in each individual member project. If a team must not view assets from other boundaries, assign that boundary to a separate `CapabilityConfig` resource and management project.
  * **Member projects** : grant Agent Registry roles on specific member projects to developers who build, register, or maintain agents and tools within those specific projects.
  * **Boundary configuration** : creating and managing boundary configuration resources requires administrative roles on the enclosing folder or organization. For more information, see the required roles in [Configure management boundaries](https://docs.cloud.google.com/resource-manager/docs/manage-capability-configs#roles) in the Resource Manager documentation.



### Restrict local registrations in member projects

Because manually registered `Service` and `Binding` resources created in a member project don't roll up to the management project, security administrators can enforce centralized registration in the management project in either of the following ways:

  * **Block`agentregistry.googleapis.com` in member projects**: when developers don't need to query Agent Registry directly in a member project, apply the `constraints/gcp.restrictServiceUsage` [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) on the parent folder or organization to deny `agentregistry.googleapis.com`, and override the policy on the management project. Blocking `agentregistry.googleapis.com` on member projects doesn't affect automatic discovery of runtime workloads from member projects into the management project.
  * **Allow read-only discovery in member projects and deny local writes** : to keep `agentregistry.googleapis.com` enabled in member projects for local read-only discovery while requiring all `Service` and `Binding` resources to be registered in the management project, grant developers **Agent Registry API Viewer** (`roles/agentregistry.viewer`) on the member project and attach an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) that denies the following write permissions in member projects:

    * `agentregistry.googleapis.com/services.create`
    * `agentregistry.googleapis.com/services.update`
    * `agentregistry.googleapis.com/services.delete`
    * `agentregistry.googleapis.com/bindings.create`
    * `agentregistry.googleapis.com/bindings.update`
    * `agentregistry.googleapis.com/bindings.delete`



## Access control for registered resources

Agent Registry roles govern who can manage and discover resources in the registry itself. To control who can view or update a standalone skill without granting project-wide access, configure a resource-level IAM policy on the `Skill` resource, or use [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) on project-level bindings. For instructions, see [Manage access to a skill](https://docs.cloud.google.com/agent-registry/manage-skills#manage-skill-access).

Agent Registry roles don't grant permission to call an agent's runtime endpoint. When an orchestrator agent or client calls a discovered [Agent2Agent (A2A)](https://docs.cloud.google.com/agent-registry/a2a-protocol) agent, MCP server, or endpoint, authorization occurs on the target service or gateway.

### Permissions to call A2A agents

Grant the calling user, service account, or [agent principal](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals) (`principal://` or `principalSet://`) the role required to call the target API, runtime, or gateway:

  * **Built-in Google agents exposed by Google Cloud APIs** : grant the IAM role required by the target API service that exposes the agent. For a list of predefined roles by service, see the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions).
  * **Custom A2A agents hosted on Google Cloud runtimes or gateways** : grant the role required by the runtime or gateway that hosts the agent, for example: 
    * **Agent Runtime on Gemini Enterprise Agent Platform** : see [Grant access for A2A delegation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity#a2a-delegation), [Share an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/share-agent), and [Gemini Enterprise Agent Platform roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user).
    * **Cloud Run** : see [Authenticate your AI agents](https://docs.cloud.google.com/run/docs/ai/authenticate-agents) and [Cloud Run IAM roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker).
    * **Agent Gateway and Identity-Aware Proxy (IAP)** : see [Create IAM Unified Access Policies (UAPs)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies-uap) and [IAP roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/iap).



In UAP Common Expression Language (CEL) conditions for [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview), target a registered agent using its [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) rather than its registry identifier. For administrative roles and policy configuration steps, see [Create IAM UAPs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies-uap).

### Deny policies and content security

Combine identity-based deny policies with payload inspection controls to govern A2A communication across your organization:

  * **IAM deny policies** : attach [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to projects, folders, or your organization using an [agent principal](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals) (`principal://` or `principalSet://`) or service account as the denied principal. You can block permissions to call agents or downstream resource permissions that appear in [Permissions supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).
  * **Content security with Model Armor** : inspect supported A2A prompt and response payloads to help detect prompt injection and sensitive data exposure by configuring [Model Armor integration with Agent Gateway](https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration) and [service extension bindings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/extension-bindings-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
