---
url: https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators/
title: Build multi-agent systems and call A2A agents \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:37:38.611159+00:00
---

# Build multi-agent systems and call A2A agents  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Build multi-agent systems and call A2A agents Stay organized with collections  Save and categorize content based on your preferences. 

In multi-agent systems, an orchestrator agent delegates tasks to specialized target agents and tools. Those target agents become subagents of the multi-agent system or application.

With Agent Registry, your orchestrator agent can look up [Agent2Agent (A2A)](https://docs.cloud.google.com/agent-registry/a2a-protocol) and Model Context Protocol (MCP) endpoints dynamically at runtime without hardcoding service URLs in your application code. You can retrieve [registered agents](https://docs.cloud.google.com/agent-registry/register-agents) and [MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers) to build orchestrator agents by using either the `AgentRegistry` client in [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) or standard HTTP and `google-auth` libraries.

When an orchestrator agent calls the endpoint of a target agent, it sends the request directly to the target agent runtime or MCP server. To enforce security policies, perform protocol mediation, and apply content filtering on your target agent endpoints, you can route agent calls through [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview).

## Before you begin

Before you look up target agent endpoint URLs or call A2A agents through Agent Registry, complete the following steps:

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. For a single-project setup, get [the project ID](https://support.google.com/googleapi/answer/7014113) of the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. If you configured a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) for multiple projects, use the ID of your management project for boundary-wide discovery and registration, or specify a member project ID for single-project operations.

  3. Install the client dependencies for your framework:

###  ADK (pip) 
         
         pip install --upgrade "google-adk[a2a,agent-identity,mcp]"
         

You must install at least `google-adk>=1.29.0`.

###  ADK (uv) 
         
         uv add "google-adk[a2a,agent-identity,mcp]"
         

You must install at least `google-adk>=1.29.0`.

###  Non-ADK Python 
         
         pip install --upgrade google-auth requests httpx
         

  4. Configure [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for local development. Otherwise, attach a service account or [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) credential configuration in external environments:
         
         gcloud auth application-default login
         

  5. Set up the following environment variables:
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         export GOOGLE_CLOUD_LOCATION=LOCATION
         

Replace the following:

     * `PROJECT_ID`: the project ID of your [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project).
     * `LOCATION`: the [Agent Registry location](https://docs.cloud.google.com/agent-registry/locations) where your agents and MCP servers are registered, such as `global` or `us-central1`.



### Required roles

You can use your user account for local development, or you can use a service account or agent principal for your orchestrator agent to discover registered components and call target A2A agents. The user account, service account, or agent principal must have appropriate roles to discover components and call target A2A agents.

To ensure that your user account, service account, or agent principal has the necessary permissions to discover registered components and call target A2A agents, ask your administrator to grant the following IAM roles to your user account, service account, or agent principal on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * To discover registered agents and MCP servers: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * To call a target A2A agent at runtime: The runtime or gateway role for the service that hosts the target agent, required to call that agent. For example, if the target agent runs on Cloud Run, the account or principal must have the Cloud Run Invoker role (`roles/run.invoker`). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give your user account, service account, or agent principal the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Choose credentials for target A2A agent endpoints

Looking up a component in Agent Registry and calling its target A2A agent endpoint require separate authentication tokens. When your orchestrator agent calls a target A2A agent endpoint, it must attach the bearer token type expected by that endpoint:

Target A2A agent endpoint | Required bearer token | Credential source and guides  
---|---|---  
**Google Cloud API agent endpoints** (`https://*.googleapis.com`) | [OAuth 2.0 access token](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) with the `https://www.googleapis.com/auth/cloud-platform` scope or a narrower service scope. When using Application Default Credentials (ADC) that don't have a default [quota project](https://docs.cloud.google.com/docs/quotas/quota-project) configured, include the `X-Goog-User-Project` header to specify the project billed for API quota. For details, see [Set the quota project with a REST request](https://docs.cloud.google.com/docs/authentication/rest#set-billing-project). | `google.auth.default()` using [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc), an attached service account, or a [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) credential configuration. To restrict permissions per call, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).  
**Cloud Run or Identity-Aware Proxy (IAP) HTTPS agent endpoints** (`https://*.run.app` or custom domains) | [ID token](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) whose `aud` claim matches the target service URL or the IAP OAuth 2.0 client ID. | `google.oauth2.id_token.fetch_id_token()` using a service account or the compute metadata server. For setup instructions, see [Get an ID token](https://docs.cloud.google.com/docs/authentication/get-id-token), [Service-to-service authentication on Cloud Run](https://docs.cloud.google.com/run/docs/authenticating/service-to-service), and [Programmatic authentication for IAP](https://docs.cloud.google.com/iap/docs/authentication-howto).  
**OAuth-bound external or SaaS agents** | [2-legged OAuth 2.0 token](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2), [3-legged OAuth 2.0 token](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2), or [API key](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2). | Managed automatically in ADK when an [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/auth-manager-overview) binding is attached to the agent. For setup instructions, see [Authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets).  
  
## Initialize the `AgentRegistry` client in ADK

To interact with Agent Registry through ADK, initialize the `AgentRegistry` client in your Python code with your governance project ID and Agent Registry location:
    
    
    import os
    from google.adk.integrations.agent_registry import AgentRegistry
    
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")
    
    registry = AgentRegistry(
        project_id=project_id,
        location=location,
    )
    

After you initialize the ADK `AgentRegistry` client, you can retrieve remote A2A agents and remote MCP tools from Agent Registry. In ADK, registered A2A agents are wrapped as `RemoteA2aAgent` instances. These instances are referred to as _remote agents_ because ADK delegates tasks to them over the network rather than running them in the local process. Similarly, registered remote MCP servers are wrapped as `McpToolset` instances.

## Compose a multi-agent system with ADK

To retrieve remote A2A subagents and remote MCP toolsets from Agent Registry and include them in an `LlmAgent` orchestrator agent definition, use the initialized `AgentRegistry` client:

  * **To retrieve a remote A2A agent** : call `registry.get_remote_a2a_agent()` with the subagent's relative resource name. This resource name can be either a relative resource name in the format `agents/AGENT_ID`, which uses the project ID and location configured on the `AgentRegistry` client, or the full resource name in the format `projects/PROJECT_ID/locations/LOCATION/agents/AGENT_ID`. When an [auth manager](https://docs.cloud.google.com/iam/docs/auth-manager-overview) `Binding` exists for the agent, `get_remote_a2a_agent()` configures request credentials automatically. When no `Binding` exists, pass a custom `httpx_client` configured with an `httpx.Auth` handler.
  * **To retrieve a remote MCP toolset** : call `registry.get_mcp_toolset()` with the MCP server's relative resource name (`mcpServers/SERVER_ID`) or full resource name (`projects/PROJECT_ID/locations/LOCATION/mcpServers/SERVER_ID`).



The following example shows how to define an orchestrator agent in an ADK `agent.py` file. In this sample consider the following:

  * The `GoogleApiAuth` class implements an `httpx.Auth` handler for calling a Google Cloud API (`https://*.googleapis.com`) A2A subagent. It uses `google.auth.default()` to load your Application Default Credentials, Attached Service Account, or Workload Identity Federation credentials and sets the `Authorization` and `X-Goog-User-Project` headers on each request.

**Note:** The `https://www.googleapis.com/auth/cloud-platform` scope is the standard OAuth 2.0 scope required by Google Cloud APIs while fine-grained access is controlled by IAM roles. To restrict scopes or impersonate a dedicated service account per subagent, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation). If your target subagent runs on Cloud Run or behind IAP, attach an OIDC ID token instead, as described in Choose credentials for target A2A agent endpoints.
  * The `registry` client retrieves the remote A2A subagent and the remote MCP toolset from Agent Registry and passes them to `LlmAgent` through the `sub_agents` and `tools` parameters.



    
    
    import httpx
    import google.auth
    from google.auth.transport.requests import Request
    from google.adk.agents.llm_agent import LlmAgent
    
    class GoogleApiAuth(httpx.Auth):
        def __init__(self, user_project_id: str):
            self.user_project_id = user_project_id
            self.creds, _ = google.auth.default(
                scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
    
        def auth_flow(self, request):
            if not self.creds.valid:
                self.creds.refresh(Request())
            request.headers["Authorization"] = f"Bearer {self.creds.token}"
            request.headers["X-Goog-User-Project"] = self.user_project_id
            yield request
    
    quota_project_id = "QUOTA_PROJECT_ID"
    agent_name = "agents/AGENT_ID"
    httpx_client = httpx.AsyncClient(
        auth=GoogleApiAuth(quota_project_id),
        timeout=httpx.Timeout(60.0),
    )
    my_remote_agent = registry.get_remote_a2a_agent(
        agent_name=agent_name,
        httpx_client=httpx_client,
    )
    
    mcp_server_name = "mcpServers/SERVER_ID"
    my_mcp_toolset = registry.get_mcp_toolset(mcp_server_name=mcp_server_name)
    
    root_agent = LlmAgent(
        model="MODEL_ID",
        name="travel_orchestrator",
        instruction=(
            "You are a travel coordinator. Use your subagents to book travel "
            "and your tools to query historical travel data."
        ),
        tools=[my_mcp_toolset],
        sub_agents=[my_remote_agent],
    )
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID used for [quota and billing attribution](https://docs.cloud.google.com/docs/quotas/quota-project) on requests to Google Cloud API agent endpoints.
  * `AGENT_ID`: the ID of the registered A2A subagent that you want your orchestrator agent to call, for example, `agentregistry-01234456-7890-abcd-1234-567890abcdef`.
  * `SERVER_ID`: the ID of the registered MCP server that you want your orchestrator agent to use.
  * `MODEL_ID`: the model ID for your orchestrator agent, for example, `gemini-2.5-flash`.



After saving `root_agent` in your ADK project's `agent.py` file, you can test and run your orchestrator agent locally using the `adk run` or `adk web` CLI commands, or deploy it to Agent Runtime on Gemini Enterprise Agent Platform. For complete project structure and execution instructions, see the [ADK Python quickstart](https://google.github.io/adk-docs/get-started/quickstart/) and the [ADK Agent Registry sample on GitHub](https://github.com/google/adk-python/tree/main/contributing/samples/integrations/agent_registry_agent).

**Note:** To design and orchestrate agents visually without writing code, you can also configure registered subagents in the Agent Studio on Gemini Enterprise Agent Platform canvas. For more information, see [Design agents in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/design-agents).

## Call an A2A agent from a non-ADK client

If you build a custom orchestrator agent or client without ADK, your application performs two authenticated steps:

  1. **Discovery** : authenticate to the Agent Registry API with an OAuth 2.0 access token to retrieve the target subagent's `Agent` resource and inspect its Agent Card.
  2. **Runtime call** : attach the bearer token required by the target agent endpoint, which is an OAuth 2.0 access token for `*.googleapis.com` agent endpoints or an OIDC ID token for Cloud Run and IAP agent endpoints. Then, send an A2A [`SendMessage`](https://docs.cloud.google.com/agent-registry/a2a-protocol#transports-and-operations) request. The output returns a `SendMessageResponse` JSON object, which contains a `task` or `message` field in the format `{"task": ...}` or `{"message": ...}`. This field contains the subagent's response, which your orchestrator agent can parse and use in its workflow.



To look up and call a registered A2A subagent using `google-auth` and `httpx`, complete the following steps:

  1. Authenticate to Agent Registry with an OAuth 2.0 access token and fetch the subagent's `Agent` resource from the Agent Registry API:
         
         import os
         import uuid
         from urllib.parse import urlparse
         import google.auth
         from google.auth.transport.requests import Request
         from google.oauth2 import id_token
         import httpx
         
         project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
         location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
         agent_id = "AGENT_ID"
         
         creds, _ = google.auth.default(
             scopes=["https://www.googleapis.com/auth/cloud-platform"]
         )
         creds.refresh(Request())
         
         registry_url = (
             f"https://agentregistry.googleapis.com/v1/projects/{project_id}"
             f"/locations/{location}/agents/{agent_id}"
         )
         client = httpx.Client(timeout=60.0)
         reg_response = client.get(
             registry_url,
             headers={
                 "Authorization": f"Bearer {creds.token}",
                 "X-Goog-User-Project": project_id,
             },
         )
         reg_response.raise_for_status()
         agent_resource = reg_response.json()
         

Replace `AGENT_ID` with the ID of the registered A2A subagent that you want to call, for example, `agentregistry-01234456-7890-abcd-1234-567890abcdef`.

  2. Extract the HTTP-based A2A interface from the Agent Card in the `Agent` resource:
         
         card = agent_resource.get("card", {}).get("content", {})
         interfaces = card.get("supportedInterfaces") or (
             (agent_resource.get("protocols") or [{}])[0].get("interfaces", [])
         )
         iface = next(
             i for i in interfaces
             if i.get("protocolBinding", "HTTP+JSON")
             in ("HTTP+JSON", "HTTP_JSON", "JSONRPC")
         )
         endpoint_url = iface["url"]
         binding = iface.get("protocolBinding", "HTTP+JSON")
         tenant = iface.get("tenant", "")
         

  3. Prepare the request headers with an OAuth 2.0 access token for `*.googleapis.com` agent endpoints or an OIDC ID token for Cloud Run or IAP agent endpoints:
         
         host = urlparse(endpoint_url).hostname or ""
         headers = {"Content-Type": "application/json", "A2A-Version": "1.0"}
         if host == "googleapis.com" or host.endswith(".googleapis.com"):
             headers["Authorization"] = f"Bearer {creds.token}"
             headers["X-Goog-User-Project"] = project_id
         else:
             oidc_audience = f"https://{host}"
             oidc_jwt = id_token.fetch_id_token(Request(), oidc_audience)
             headers["Authorization"] = f"Bearer {oidc_jwt}"
         

**Note:** Calling `id_token.fetch_id_token()` requires service account credentials, an attached compute metadata server, or service account impersonation. For local testing with user credentials against an OIDC-protected agent endpoint, run `gcloud auth print-identity-token` with `--audiences` set to your target host.
  4. Format and send the A2A `SendMessage` request using the protocol binding from the Agent Card, and parse the response from the subagent:
         
         message = {
             "messageId": str(uuid.uuid4()),
             "role": "ROLE_USER",
             "parts": [{"text": "Summarize recent deployment status."}],
         }
         if binding == "JSONRPC":
             params = {"message": message}
             if tenant:
                 params["tenant"] = tenant
             payload = {
                 "jsonrpc": "2.0",
                 "id": str(uuid.uuid4()),
                 "method": "SendMessage",
                 "params": params,
             }
             target_url = endpoint_url
         else:
             payload = {"message": message}
             prefix = f"/{tenant.strip('/')}" if tenant else ""
             target_url = f"{endpoint_url.rstrip('/')}{prefix}/message:send"
         
         response = client.post(target_url, headers=headers, json=payload)
         response.raise_for_status()
         body = response.json()
         if binding == "JSONRPC":
             if "error" in body:
                 raise RuntimeError(f"JSON-RPC error: {body['error']}")
             send_message_response = body["result"]
         else:
             send_message_response = body
         print(send_message_response)
         client.close()
         

This step formats a `SendMessage` request for A2A version `1.0`. If you need to negotiate between A2A protocol versions `1.0` and `0.3` automatically, use ADK or the [`a2a-sdk` Python client](https://github.com/a2aproject/a2a-python).




## Reuse remote agents across orchestrator agents in ADK

To minimize network latency, retrieve your remote agents and toolsets from Agent Registry once at application startup instead of calling `get_remote_a2a_agent()` on every request.

In ADK, a `RemoteA2aAgent` instance can only have one parent orchestrator agent at a time. Continuing from the initialization setup, call `.clone()` to create an independent copy for each parent orchestrator agent:
    
    
    agent_path = (
        f"projects/{project_id}/locations/{location}"
        "/agents/AGENT_ID"
    )
    base_remote_agent = registry.get_remote_a2a_agent(
        agent_name=agent_path,
        httpx_client=httpx_client,
    )
    
    flight_orchestrator = LlmAgent(
        model="gemini-2.5-flash",
        name="flight_orchestrator",
        sub_agents=[base_remote_agent.clone()],
    )
    
    hotel_orchestrator = LlmAgent(
        model="gemini-2.5-flash",
        name="hotel_orchestrator",
        sub_agents=[base_remote_agent.clone()],
    )
    

Replace `AGENT_ID` with the ID of the registered A2A subagent that you want your orchestrator agents to call.

## What's next

  * Review [A2A protocol](https://docs.cloud.google.com/agent-registry/a2a-protocol) for transport bindings and task lifecycle states.
  * Learn how to [set up Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) to route and govern traffic for your target agent endpoints.
  * Learn how to [authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets) and scope credentials across agent calls.
  * Learn how to [register skills](https://docs.cloud.google.com/agent-registry/register-skills) and [manage skills](https://docs.cloud.google.com/agent-registry/manage-skills) in Agent Registry.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
