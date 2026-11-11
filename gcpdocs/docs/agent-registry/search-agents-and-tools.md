---
url: https://docs.cloud.google.com/agent-registry/search-agents-and-tools/
title: Search for agents, tools, and skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:37:38.423470+00:00
---

# Search for agents, tools, and skills  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/search-agents-and-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Search for agents, tools, and skills Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you search across registered agents, Agent2Agent (A2A) skills, standalone skills, and Model Context Protocol (MCP) servers by keyword, prefix, or natural language. You can run searches in the Google Cloud console, the Google Cloud CLI, or the Agent Registry API. Keyword and prefix searches help you find resources by name, identifier, or metadata. Semantic search finds conceptually related capabilities across natural language instructions and descriptions based on intent.

Search queries evaluate agent, MCP server, and skill capability descriptions, tool schemas, and skill instructions. You can't use search queries to discover endpoints. To list and filter endpoints by metadata, see Discover endpoints and filter components by metadata.

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. For a single-project setup, get [the project ID](https://support.google.com/googleapi/answer/7014113) of the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. If you configured a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) for multiple projects, use the ID of your management project for boundary-wide discovery and registration, or specify a member project ID for single-project operations.

  3. [Register an agent](https://docs.cloud.google.com/agent-registry/register-agents), an [MCP server](https://docs.cloud.google.com/agent-registry/register-mcp-servers), or a [skill](https://docs.cloud.google.com/agent-registry/register-skills) in Agent Registry.

  4. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).




### Required roles

To get the permissions that you need to search for agents, tools, and skills in Agent Registry, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * Search for agents, tools, and skills: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * Search for and view standalone skills: [Agent Registry User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.user) (`roles/agentregistry.user`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Search for agents and tools

To discover capabilities in your registry, you can search for registered agents and MCP servers in the Google Cloud console, gcloud CLI, or the Agent Registry API.

Depending on the component type, you can search by the following fields:

  * **Agents** : search by the agent's name, description, or [agent identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers). You can also search by the names, descriptions, tags, and example prompts of the inline [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a) in the agent's [Agent Card](https://docs.cloud.google.com/agent-registry/a2a-protocol).
  * **MCP servers** : search by the server's name, description, or [MCP server identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers). You can also search by the names and descriptions of the MCP server's tools.



To find built-in Google agents, Google and Google Cloud remote MCP servers, or project-scoped components by source prefix, see Find components by source prefix. To find by protocol type or inspect an agent's full Agent Card JSON file, filter by metadata.

### Search fields

When you search by keyword, Agent Registry checks all indexed fields on the agentic component's [discovery resource](https://docs.cloud.google.com/agent-registry/data-model#service-resources), including inline A2A skills on agents and tool names and descriptions on MCP servers. To narrow your search to a specific field, use the `:` operator, for example, `skills.tags:incident`:

Field filter | Agentic component | Prefix search supported | Description  
---|---|---|---  
`displayName` | Agents and MCP servers | Yes | Display name of the agent or MCP server.  
`name` | Agents and MCP servers | Yes |  [Resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) of the agent or MCP server.   
`agentId` | Agents | Yes |  [Agent identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers) URN (also supports exact matches with `=`).   
`mcpServerId` | MCP servers | No |  [MCP server identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers) URN (also supports exact matches with `=`).   
`description` | Agents | No | Description of the agent.  
`skills` | Agents | No | Searches across all inline A2A skill fields extracted from the Agent Card.  
`skills.id`, `skills.name`, `skills.description`, `skills.tags`, `skills.examples` | Agents | No | Targets a specific inline A2A skill field extracted from the Agent Card.  
  
Custom fields inside the Agent Card and transport `protocols` aren't indexed for search. Instead, you can inspect that information by using filters for metadata when you list or describe agents. For more information, see Discover endpoints and filter components by metadata.

### Search by keywords

You can perform a keyword search to find resources that contain specific terms across their capabilities, such as an agent's A2A skill or an MCP server's tool. To understand how these capabilities are structured in the registry, see [JSON schemas](https://docs.cloud.google.com/agent-registry/json-schemas). For a complete list of searchable fields, see the [API reference](https://docs.cloud.google.com/agent-registry/reference/rest).

Keyword queries accept free-text strings and support the logical operators `AND`, `OR`, and `NOT`:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select your Google Cloud project.

  3. In the **Search your registry** bar at the top of the page, enter a keyword query of at least three characters, such as `flight` or `database`, or a field filter, such as `Name:booking`, and then press `Enter`.

The **Search results** table displays matching agents, MCP servers, and standalone skills across your selected locations.




###  gcloud 

Provide the `--search-string` flag to the [`gcloud agent-registry agents search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/search) or [`gcloud agent-registry mcp-servers search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/mcp-servers/search) command, for example:

  * Search for an agent that can handle flight bookings:
        
        gcloud agent-registry agents search \
            --project=PROJECT_ID \
            --location=REGION \
            --search-string="flight OR booking"
        

  * Search for an agent by its A2A skill tags or example prompts:
        
        gcloud agent-registry agents search \
            --project=PROJECT_ID \
            --location=REGION \
            --search-string='skills.tags:incident OR skills.examples:"rollout"'
        

  * Search for an MCP server that provides database tools:
        
        gcloud agent-registry mcp-servers search \
            --project=PROJECT_ID \
            --location=REGION \
            --search-string="database"
        




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Send a `POST` request to the [`agents:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents/search) or [`mcpServers:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/search) endpoint with the `searchString` field in the request body.

For example, search for an agent that can handle flight bookings:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"searchString": "flight OR booking"}' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/agents:search"
    

Search for an MCP server that provides database tools:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"searchString": "database"}' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/mcpServers:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



### Search by prefix

Prefix searches are optimized for low latency, letting your applications retrieve relevant agents and tools dynamically as a user types.

If you are building an orchestrator interface or an autocomplete feature, you can perform prefix searches in Agent Registry to find results that start with a given string. Prefix searches use the `*` suffix wildcard symbol to search for the beginning of a word:

###  gcloud 

Run the [`gcloud agent-registry agents search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/search) or [`gcloud agent-registry mcp-servers search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/mcp-servers/search) command with a prefix expression.

For example, search for agents whose display name begins with `Best_A2A_*`:
    
    
    gcloud agent-registry agents search \
        --project=PROJECT_ID \
        --location=REGION \
        --search-string="displayName:Best_A2A_*"
    

Similarly, search for MCP servers whose display name begins with `Prod_Server_*`:
    
    
    gcloud agent-registry mcp-servers search \
        --project=PROJECT_ID \
        --location=REGION \
        --search-string="displayName:Prod_Server_*"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Pass the prefix expression in the `searchString` field of the request body:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"searchString": "displayName:Best_A2A_*"}' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/agents:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



### Find components by source prefix

Every agent and MCP server includes a source prefix in its [registry identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers):

  * **Built-in Google agents and Google and Google Cloud remote MCP servers** : use `urn:agent:googleapis.com:` or `urn:mcp:googleapis.com:`.
  * **Project-scoped components** : use `urn:agent:projects-` or `urn:mcp:projects-`, followed by the project number, for example, `urn:agent:projects-PROJECT_NUMBER:`.



For example, you can search by these source prefixes to find only built-in Google agents, all project-scoped agents, or agents from a specific project:

###  gcloud 

Include a source prefix in the `--search-string` flag of the [`gcloud agent-registry agents search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/search) command. Use the `agentId` field to search by agent identifier:

  * **Built-in Google agents** : include the `urn:agent:googleapis.com:*` prefix:
        
        gcloud agent-registry agents search \
            --project=PROJECT_ID \
            --location=REGION \
            --search-string='agentId:"urn:agent:googleapis.com:*"'
        

  * **Project-scoped agents** : use `urn:agent:projects-*` to match all project-scoped agents, or `urn:agent:projects-PROJECT_NUMBER:*` to target a specific project:

    * Search for all project-scoped agents:
          
          gcloud agent-registry agents search \
              --project=PROJECT_ID \
              --location=REGION \
              --search-string='agentId:"urn:agent:projects-*"'
          

    * Search for agents in a specific project:
          
          gcloud agent-registry agents search \
              --project=PROJECT_ID \
              --location=REGION \
              --search-string='agentId:"urn:agent:projects-PROJECT_NUMBER:*"'
          




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry location, such as a region like `us-central1`, a multi-region like `us` or `eu`, or `global`.
  * `PROJECT_NUMBER`: the project number for a specific project's agents.



###  REST 

Send a `POST` request to the [`agents:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents/search) endpoint with an `agentId` prefix in `searchString`:

  * **Built-in Google agents** : include the `urn:agent:googleapis.com:*` prefix:
        
        curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -d '{"searchString": "agentId:\"urn:agent:googleapis.com:*\""}' \
            "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/agents:search"
        

  * **Project-scoped agents** : use `urn:agent:projects-*` to match all project-scoped agents, or `urn:agent:projects-PROJECT_NUMBER:*` to target a specific project:
        
        curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -d '{"searchString": "agentId:\"urn:agent:projects-*\""}' \
            "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/agents:search"
        




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry location, such as a region like `us-central1`, a multi-region like `us` or `eu`, or `global`.



You can also [filter registered agents](https://docs.cloud.google.com/agent-registry/manage-agents#filter-agents) and [filter registered MCP servers](https://docs.cloud.google.com/agent-registry/manage-mcp-tools#filter-servers) by source prefix when listing them in a specific project.

### Search across a management boundary

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you configured a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology), you can search for all agents and MCP servers in a location across all member projects in that boundary from your [management project](https://docs.cloud.google.com/agent-registry/boundaries-and-topology#management-project):
    
    
    gcloud agent-registry agents search \
        --project=MANAGEMENT_PROJECT_ID \
        --location=LOCATION \
        --search-string="analytics"
    

To narrow search results on the management project to agents in a specific member project, filter by that member project's number using the [agent identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers) in the `--search-string` flag:
    
    
    gcloud agent-registry agents search \
        --project=MANAGEMENT_PROJECT_ID \
        --location=LOCATION \
        --search-string='agentId:"urn:agent:projects-MEMBER_PROJECT_NUMBER:*"'
    

Replace the following:

  * `MANAGEMENT_PROJECT_ID`: the ID of your management project. To search exclusively within a single member project without cross-project rollup, specify that member project's ID in the `--project` flag instead.
  * `LOCATION`: the [location](https://docs.cloud.google.com/agent-registry/locations) to search across the management boundary, such as a region like `us-central1`, a multi-region like `us` or `eu`, or `global`. Agent Registry aggregates resources in that same location across the management project and all member projects in the boundary.
  * `MEMBER_PROJECT_NUMBER`: the project number of the member project.



You can filter MCP servers by member project using the [MCP server identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers) when listing MCP servers. For more information, see [Filter registered MCP servers](https://docs.cloud.google.com/agent-registry/manage-mcp-tools#filter-servers).

When you search from the management project:

  * **Aggregated auto-discovered resources** : Agent Registry searches across auto-discovered agents and MCP servers in the specified location from all member projects in the management boundary, alongside any registered `Service` resources created in that location in the management project.
  * **Request-scoped resource names** : in search results, each [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) of a returned agent or MCP server uses the project specified in the request URL, and preserves the ID that Agent Registry assigned when the component was registered. The [registry identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers) retains the member project.
  * **Project-scoped registered resources** : manually registered `Service` resources and `Binding` resources created in a member project remain scoped to that member project and don't appear in management project search results. To make them visible across the management boundary, create them in the management project.



## Search for standalone skills

You can search for standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture) registered in Agent Registry. This feature lets you discover reusable capabilities to attach to your agents.

When you search for skills, you search for the default [skill revision](https://docs.cloud.google.com/agent-registry/skills-architecture#skill-revision). To update the default revision of a skill, see [Update skill metadata or default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).

Agent Registry filters skill search results based on your Identity and Access Management (IAM) permissions. A search request returns only the skills for which you have the `agentregistry.skills.get` permission, whether granted at the project level or through a [resource-level IAM policy on the skill](https://docs.cloud.google.com/agent-registry/manage-skills#manage-skill-access).

### Search modes

You can use two search modes for skills based on your requirements:

  * **Keyword search** : scans only basic metadata attributes such as the display name, description, [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names), and [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers). This mode is optimized for low-latency searches, exact lookups, and name autocomplete. For an example, see Search for skills by keyword or expression.
  * **Semantic search** : automatically indexes the complete contents of the `SKILL.md` payload, including natural language instructions, scripts, and metadata assets. This mode identifies conceptual themes and is optimized for orchestrator agents discovering relevant capability bundles dynamically, based on your intent. For an example, see Search for skills by semantic meaning.



### Search fields and syntax

When searching by metadata or keyword strings, the following fields are indexed:

Field name | Case behavior | Prefix search | All-fields search | Description  
---|---|---|---|---  
`displayName` | Case insensitive | Yes | Yes | The display name of the skill. Use this field to search for common names.  
`description` | Case insensitive | No | Yes | The detailed description of the skill's purpose and functionality. Use this field to search for keywords.  
`name` | Case insensitive | Yes | Yes | The [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) of the skill. Use this field to search by resource name.  
`skillId` | Case insensitive | Yes | Yes | The [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) of the skill. Use this field to find a specific publisher's assets. For example, the format for Google-managed skills is `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`.   
`publisher` | Case insensitive | Yes | No | The publisher associated with the skill. Use this field to filter by the publishing organization.  
`frontmatter.name` | Case insensitive | No | No | The name of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.description` | Case insensitive | No | No | The description of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.compatibility` | Case insensitive | No | No | The compatibility of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.license` | Case insensitive | No | No | The license of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.allowed_tools` | Case insensitive | No | No | The allowed tools of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.metadata.KEY` | Case insensitive | No | No | A custom metadata key-value entry defined in `metadata` in the front matter of the `SKILL.md` file. Supports the `:` operator in search queries and exact matches (`=` and `!=`) in filters.  
`state` | Case insensitive | No | No | The current [lifecycle state](https://docs.cloud.google.com/agent-registry/skills-architecture#lifecycle) of the skill, such as `ACTIVE`, `DRAFT`, `DISABLED`, `DEPRECATED`, or `DECOMMISSIONED`. This field is only available in filters and supports exact matches (`=` and `!=`).  
`targetState` | Case insensitive | No | No | The target [lifecycle state](https://docs.cloud.google.com/agent-registry/skills-architecture#lifecycle) of the skill, such as `ACTIVE`, `DRAFT`, `DISABLED`, `DEPRECATED`, or `DECOMMISSIONED`. This field is only available in filters and supports exact matches (`=` and `!=`).  
`defaultRevisionFindingCount` | Not applicable | No | No | The number of [security findings](https://docs.cloud.google.com/agent-registry/scan-skills) detected in the skill's default revision. This field is only available in filters and supports exact matches (`=` and `!=`) and range operators (`<`, `<=`, `>`, and `>=`), such as `defaultRevisionFindingCount = 0` or `defaultRevisionFindingCount > 0`.  
`createTime` | Not applicable | No | No | The timestamp when the skill was created. This field is only available in filters. Supports range operators, such as `<`, `>`, and exact matches.  
`updateTime` | Not applicable | No | No | The timestamp when the skill was last updated. This field is only available in filters. Supports range operators, such as `<`, `>`, and exact matches.  
  
To search for skills, provide a query string using the `--query` flag in gcloud CLI or the `searchString` field in the request body of the REST API. You can use the following syntax elements in your search requests:

  * **Boolean operators** : include `AND`, `OR`, or `NOT` operators to chain requirements.
  * **Field-specific filters** : target a field using the `:` operator, for example, `displayName:database`.
  * **Prefix search** : use the `*` suffix wildcard symbol to find values starting with a specific prefix, for example, `displayName:cloud-*`.



### Search for skills by keyword or expression

Search for skills that have a specific display name prefix and description keyword:

###  gcloud 

Run the [`gcloud agent-registry skills search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/search) command with `--search-type=keyword`:
    
    
    gcloud agent-registry skills search \
        --project=PROJECT_ID \
        --location=REGION \
        --query="displayName:cloud-* AND description:database" \
        --search-type=keyword
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Send a `POST` request to the [`skills:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.skills/search) endpoint with the `searchString` and `searchType` fields in the request body:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "searchString": "displayName:cloud-* AND description:database",
          "searchType": "KEYWORD"
        }' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/skills:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



### Search for skills by semantic meaning

Find skills related to managing relational databases by using semantic search:

###  gcloud 

Run the [`gcloud agent-registry skills search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/skills/search) command with `--search-type=semantic`:
    
    
    gcloud agent-registry skills search \
        --project=PROJECT_ID \
        --location=REGION \
        --query="manage and configure relational databases" \
        --search-type=semantic
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Send a `POST` request to the [`skills:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.skills/search) endpoint with the `searchString` and `searchType` fields in the request body:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "searchString": "manage and configure relational databases",
          "searchType": "SEMANTIC"
        }' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/skills:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



### Google-managed skills

Google-managed skills are discoverable from any project. For a list of available Google-managed skills, see the [`google/skills` repository](https://github.com/google/skills/tree/main) on GitHub.

To search for skills from a verified Google-managed [publisher](https://docs.cloud.google.com/agent-registry/review-publishers), filter on the `publisher` field:
    
    
    gcloud agent-registry skills search \
        --project=PROJECT_ID \
        --location=REGION \
        --query="publisher:cloud.google.com" \
        --search-type=keyword
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry location, such as a region like `us-central1`, a multi-region like `us` or `eu`, or `global`.



## Discover endpoints and filter components by metadata

You can also discover any component in Agent Registry, including registered [endpoints](https://docs.cloud.google.com/agent-registry/register-endpoints), by listing the corresponding collection and filtering on structured metadata fields:

  * **Discover endpoints** : because `Endpoint` resources don't support search queries, you discover them by browsing the **Endpoints** tab in the Google Cloud console, running `gcloud agent-registry endpoints list --filter`, or calling the [`endpoints.list`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/list) REST method. For complete instructions, see [Manage and discover endpoints](https://docs.cloud.google.com/agent-registry/manage-endpoints#discover-endpoints).
  * **Filter agents, MCP servers, and skills** : when you know a component's [registry identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers) (URN), display name, protocol type, or attribute, you can filter the list in the Google Cloud console or include the `--filter` flag in `gcloud agent-registry agents list`, `gcloud agent-registry mcp-servers list`, or `gcloud agent-registry skills list` commands. For example, include `--filter='protocols.type="A2A_AGENT"'` to the `gcloud agent-registry agents list` command to show only A2A agents, and run `gcloud agent-registry agents describe` to view an agent's full Agent Card and `protocols` endpoints. For details, see [Manage agents](https://docs.cloud.google.com/agent-registry/manage-agents), [Manage MCP servers and tools](https://docs.cloud.google.com/agent-registry/manage-mcp-tools), and [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
