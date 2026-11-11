---
url: https://docs.cloud.google.com/gemini/docs/discover/engineer-agentic-prompts/
title: System instructions and prompt engineering for agentic AI \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:28.588922+00:00
---

# System instructions and prompt engineering for agentic AI  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/discover/engineer-agentic-prompts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  System instructions and prompt engineering for agentic AI Stay organized with collections  Save and categorize content based on your preferences. 

To build autonomous AI agents that operate reliably and safely in production on Google Cloud, you can combine structured system instructions, explicit tool schemas, reasoning boundaries, human-in-the-loop (HITL) safety controls, and context hygiene. Unlike interactive chatbots that rely on basic input-output prompting, agentic systems with Gemini perform multi-step planning, invoke external APIs, monitor execution feedback, and maintain working memory across multi-turn workflows.

This document describes architectural patterns and prompt engineering practices for designing autonomous agents. If you're looking for tips on writing interactive prompts for Gemini Cloud Assist or IDE chat, see [Write better prompts for Gemini in Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).

## System instructions

In agentic architectures, you use [system instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction) to define the agent's baseline identity, rules, and permissions. Unlike standard user prompts that change with each turn, you define system instructions once and pass them consistently across execution turns.

System instructions define the following:

  * **Baseline identity and role** : Define the agent's persona and primary function—for example, "You are a database administrator agent."
  * **Behavioral rules** : Establish operational constraints, safety boundaries, and output format requirements—for example, "Never perform a write operation without human approval" or "Return results as JSON."
  * **Tool calling guidelines** : Define tool selection, ordering, and retry rules.



The example in the next section groups each of these into its own XML tag: `<role>`, `<rules>`, and `<tool_usage>`.

System instructions shouldn't contain dynamic runtime inputs, such as user questions, file contents, or tool execution logs. Keep these dynamic values in the content payloads sent during execution turns.

### Structure system instructions with XML tags

Formatting system instructions using an XML structure helps the model accurately segment different types of guidance.

XML tags aren't a hardcoded feature of the Gemini API. Instead, they're a prompt engineering convention. Because Gemini models are trained on structured code and web pages, they parse XML tags to separate instruction types and prevent instruction drift across multi-turn sessions.

When you [pass your system instruction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instructions) to the SDK or API, don't wrap the entire instruction block in an outer tag, such as `<system_instruction>`. The API already processes the entire string as a system instruction. Instead, use individual tags inside the block to group instructions:
    
    
    <role>
      You are an autonomous Cloud Infrastructure Management Agent responsible
      for diagnosing and remediating GKE cluster issues.
    </role>
    
    <rules>
      - Always run diagnostic tools before proposing or applying remediation.
      - Never delete storage volumes, IAM bindings, or database
        instances without explicit human authorization.
      - Verify target cluster and namespace names from diagnostic output before
        proposing changes.
    </rules>
    
    <tool_usage>
      - Call `gke_get_cluster_status` to fetch node pool health.
      - Call `gke_inspect_logs` to retrieve pod error logs.
      - Use strict JSON schemas when supplying tool parameters.
    </tool_usage>
    

When you separate instructions with XML tags such as `<role>`, `<rules>`, and `<tool_usage>`, the model treats each block as a distinct category of guidance.

### Common XML tags for system instructions

While Gemini can parse any custom XML tags that fit your domain, using a set of common tags helps keep instructions consistent and easier to maintain across agents.

The following table lists example tags that you can use to structure system instructions. Tag names are conventions, so you can rename them to suit your agent. For example, the [CX Agent Studio instructions guide](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction#restructure) uses `<constraints>` for the type of guidance that this document places in `<rules>`.

Tag | Description  
---|---  
`<role>` | Defines the agent's core identity, persona, and main function.  
`<rules>` | Lists constraints, formatting rules, and safety boundaries.  
`<tool_usage>` | Outlines policies for choosing and calling tools.  
`<example>` | Contains a [few-shot example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/few-shot-examples) that shows an expected input and output. Use one tag per example.  
  
For more details and prompting patterns, see the following resources:

  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)
  * [Use system instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instructions)
  * [Structure prompts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts)
  * [Get started with Gemini 3](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/get-started-with-gemini-3#prompting-best-practices)



## Tool and function definition best practices

In agentic systems, you use [tools and function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling) to grant agents the ability to interact with Google Cloud APIs, databases, and microservices. Because the model requests execution of client-side code by matching schemas you define, providing clear, unambiguous tool declarations is critical to prevent invocation errors.

### Schema design principles

Follow these principles when you define tool schemas:

  * **Use explicit typing** : Specify precise data types, such as `string`, `integer`, `boolean`, `array`, or `object`, for every parameter in OpenAPI or JSON schemas.
  * **Provide meaningful descriptions** : Explain format requirements, constraints, and valid ranges for each parameter rather than relying on field names alone.
  * **Declare required fields** : Populate the `required` array in JSON schemas so that the model doesn't pass `null` or omit arguments for mandatory fields.
  * **Constrain values with enums** : Use `enum` values for fields with fixed valid inputs, such as environment names or log severity levels.



### Example function declaration schema

The following example defines a function declaration with a JSON schema for a tool that restarts a Google Kubernetes Engine (GKE) deployment:
    
    
    {
      "name": "restart_gke_deployment",
      "description": "Performs a rolling restart of a GKE deployment.",
      "parameters": {
        "type": "object",
        "properties": {
          "cluster_id": {
            "type": "string",
            "description": "Fully qualified GKE cluster resource ID."
          },
          "namespace": {
            "type": "string",
            "description": "Kubernetes namespace containing the deployment."
          },
          "deployment_name": {
            "type": "string",
            "description": "The exact metadata name of the deployment."
          },
          "environment": {
            "type": "string",
            "description": "Target environment for the restart.",
            "enum": ["dev", "staging", "prod"]
          },
          "reason": {
            "type": "string",
            "description": "Brief operational rationale for the restart."
          }
        },
        "required": ["cluster_id", "namespace", "deployment_name", "reason"]
      }
    }
    

## Reasoning and thinking budget control

To perform internal reasoning before taking action in complex workflows, agents use Gemini [thinking capabilities](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking) with the `thinking_config` parameter. This configuration lets agents perform plan-verify-execute loops to validate actions before invoking tools.

### Implement plan-verify-execute loops

A plan-verify-execute loop consists of the following stages:

  1. **Plan** : Analyze the prompt, identify dependencies, and formulate a sequence of tool calls.
  2. **Verify** : Check proposed tool calls against system constraints, safety policies, and required parameters.
  3. **Execute** : Issue tool calls and observe execution feedback.



Built-in thinking runs in an internal channel rather than emitting `<thinking>` XML tags in response text. If you set `include_thoughts=True` in `thinking_config`, you can inspect thought summaries (`part.thought`) before a tool call:
    
    
    1. User requests scaling down node pool 'pool-1' in cluster
       'prod-us-central1'.
    2. Verification: Scaling down production node pools requires checking
       current CPU utilization first.
    3. Plan: Call `get_node_pool_metrics` first. If utilization < 30%, request
       human approval before scaling down.
    

When you configure `thinking_config` in the SDK, set `thinking_level` (for Gemini 3 models) or `thinking_budget` (for Gemini 2.5 models) to balance reasoning depth and latency.

## Context window hygiene and working memory

While flagship Gemini models support a 1-million-token context window, long context sequences can introduce noise, latency, and context degradation. Maintaining working memory hygiene helps ensure that long-running agents remain accurate.

### Strategies for context hygiene

Use the following strategies to manage context in long-running agents:

  * **Subagent delegation** : Delegate isolated subtasks, such as code analysis or log search, to short-lived subagents, returning only synthesized summaries to the main context.
  * **State summarization** : Periodically summarize multi-turn history, discarding transient debug logs and preserving key facts.
  * **Memory files** : Persist structured state, project constraints, and operational context in external Markdown files, such as `GOALS.md` and `MEMORY.md`, rather than keeping entire raw conversation histories in context.



## Human-in-the-loop (HITL) checkpoints

Autonomous agents operating on live Google Cloud environments should enforce approval checkpoints for high-risk operations.

### High-risk operations requiring HITL

Require human approval before an agent performs any of the following operations:

  * **Access and permissions** : Modifying Identity and Access Management (IAM) roles, granting service account access, or making resources publicly accessible, such as by allowing unauthenticated access to a service or opening firewall rules to all IP addresses.
  * **Resource deletion** : Deleting resources such as Cloud SQL databases, Cloud Storage buckets, Pub/Sub topics, or GKE node pools.
  * **Billing and quota** : Provisioning high-cost machine types, such as Cloud TPU pods or multi-GPU instances, or raising quota limits.



### Design approval pauses

Don't rely on prompt instructions alone to gate destructive actions. Because your application code executes tools, enforce approval checks deterministically in your orchestrator by intercepting high-risk `function_call` requests before running them and presenting a confirmation payload to a human reviewer:
    
    
    {
      "action": "delete_cloud_sql_instance",
      "target_resource": "projects/my-prod/instances/user-db-primary",
      "risk_level": "CRITICAL",
      "status": "WAITING_FOR_HUMAN_APPROVAL"
    }
    

## Automated error recovery and retry loops

Tool execution failures are inevitable in distributed cloud environments. Agents should handle transient errors, `PERMISSION_DENIED` status codes, and schema validation failures autonomously.

### Error feedback architecture

When a tool call returns an error, feed the raw error output back into the agent's context alongside retry guidance rather than failing immediately:

  * **Schema mismatches** : If a parameter format is invalid, then return the schema error to the model so that it can correct the tool arguments.
  * **Permission denied errors** : Instruct the agent to check required IAM permissions or fall back to read-only diagnostic tools.
  * **Rate limits and throttling** : Handle transient `429` errors with exponential backoff in your client code, and return persistent quota errors to the model so that it can adjust its plan.



When using function calling, return structured error details in a `FunctionResponse` part (preserving the prior model turn's content and thought signatures) rather than raw text:
    
    
    from google.genai import types
    
    error_part = types.Part.from_function_response(
        name="gke_get_cluster_status",
        response={
            "status": "ERROR",
            "error_code": "PERMISSION_DENIED",
            "message": (
                "Caller lacks permission 'container.clusters.get' on"
                " 'projects/demo/locations/us-central1/clusters/dev'."
            ),
            "remediation_hint": (
                "Verify service account permissions or check another project."
            ),
        },
    )
    

## Before versus after code schema example

The following comparison illustrates shifting from a legacy, unstructured text prompt to an agentic system instruction with structured JSON tool schemas using the Google Gen AI SDK.

### Legacy unstructured text prompt

The following example embeds a shell command inside an unstructured text prompt, which can cause hallucinated tool calls or missing parameters:
    
    
    # Legacy unstructured approach (prone to hallucinated tool calls and missing
    # parameters)
    prompt = """
    You are a Cloud helper. Restart the app deployment in namespace 'prod' for
    cluster 'prod-cluster'.
    Run command: kubectl rollout restart deployment/web-app -n prod
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    

### Agentic system instruction and tool definition schema

The following example separates the system instruction from the user prompt and declares an explicit function schema:
    
    
    from google import genai
    from google.genai import types
    
    # 1. Define explicit function schema with required parameters
    restart_deployment_tool = types.FunctionDeclaration(
        name="restart_gke_deployment",
        description=(
            "Executes a rolling restart for a Kubernetes deployment in Google"
            " Kubernetes Engine."
        ),
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "cluster_id": types.Schema(
                    type=types.Type.STRING,
                    description=(
                        "Fully qualified GKE cluster ID (e.g."
                        " projects/my-project/locations/us-central1/"
                        "clusters/prod-cluster)."
                    ),
                ),
                "namespace": types.Schema(
                    type=types.Type.STRING,
                    description=(
                        "Kubernetes namespace (e.g. default, production)."
                    ),
                ),
                "deployment_name": types.Schema(
                    type=types.Type.STRING,
                    description="Metadata name of the target deployment.",
                ),
            },
            required=["cluster_id", "namespace", "deployment_name"],
        ),
    )
    
    # 2. Configure System Instruction with identity, safety rules, and tools
    system_instruction = """
    <role>You are an autonomous Cloud Infrastructure Remediation Agent.</role>
    <rules>
    - Always validate parameter schemas before invoking tool calls.
    - Require human approval before performing destructive actions.
    - Verify cluster and namespace identifiers before invoking remediation tools.
    </rules>
    """
    
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(function_declarations=[restart_deployment_tool])],
        thinking_config=types.ThinkingConfig(thinking_budget=1024),
    )
    
    client = genai.Client(vertexai=True, project="my-project", location="global")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            "Restart the deployment 'web-app' in namespace 'prod' under"
            " cluster"
            " 'projects/my-proj/locations/us-central1/clusters/prod-cluster'."
        ),
        config=config,
    )
    
    # Inspect response.function_calls, validate arguments, and require human
    # approval in your orchestrator before executing restart_gke_deployment.
    

## What's next

  * To write interactive prompts in the Google Cloud console or IDE chat, see [Write better prompts for Gemini in Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * For more information about Gemini responsible AI principles, see [Google Cloud with Gemini and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).
  * For details about data privacy and governance, see [How Gemini products in Google Cloud use your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
