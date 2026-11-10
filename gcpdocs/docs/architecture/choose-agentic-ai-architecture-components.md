---
url: https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components/
title: Choose your agentic AI architecture components \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:33:35.189191+00:00
---

# Choose your agentic AI architecture components  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Choose your agentic AI architecture components Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-11-05 UTC

This document provides guidance to help you choose architectural components for your agentic AI applications in Google Cloud. It describes how to evaluate the characteristics of your application and workload to choose an appropriate product or service that best suits your needs. The process to design an agentic AI architecture is iterative. You should periodically reassess your architecture as your workload characteristics change, as your requirements evolve, or as new Google Cloud products and features become available.

AI agents are effective for applications that solve open-ended problems, which might require autonomous decision-making and complex multi-step workflow management. Agents excel at solving problems in real-time by using external data and they excel at automating knowledge-intensive tasks. These capabilities enable agents to provide more business value than the assistive and generative capabilities of an AI model.

## Agent architecture overview

An [agent](https://docs.cloud.google.com/docs/ai-ml/generative-ai/glossary#ai-agents) is an application that achieves a goal by processing input, performing reasoning with available tools, and taking actions based on its decisions. An agent uses an AI model as its core reasoning engine to automate complex tasks. The agent uses a set of tools that let the AI model interact with external systems and data sources. An agent can use a memory system to maintain context and learn from interactions. The goal of an agentic architecture is to create an autonomous system that can understand a user's intent, create a multi-step plan, and execute that plan by using the available tools.

The following diagram shows a high-level overview of an agentic system's architecture components:

![The architecture components of an agentic system.](https://docs.cloud.google.com/static/architecture/images/choose-agentic-ai-architecture-components.svg)![](https://docs.cloud.google.com/static/architecture/images/choose-agentic-ai-architecture-components.svg)

The agentic system architecture includes the following components:

  * **Agent development framework** : The frameworks and libraries that you use to build and structure your agent's logic.
  * **Frontend framework** : A collection of prebuilt components, libraries, and tools that you use to build the user interface (UI) for your application.
  * **Agent security and governance** : The controls and policies that secure agent identities, ingress and egress traffic, tools, and model interactions.
  * **Agent tools** : The collection of tools, such as APIs, services, and functions, that fetch data and perform actions or transactions.
  * **Agent memory** : The system that your agent uses to store and recall information.
  * **Agent design patterns** : Common architectural approaches for structuring your agentic application.
  * **Agent runtime** : The compute environment where your agent's application logic runs.
  * **AI models** : The core reasoning engine that powers your agent's decision-making capabilities.
  * **Model runtime** : The infrastructure that hosts and serves your AI model.



The following sections provide a detailed analysis of the components to help you make decisions about how to build your architecture. The components that you choose will influence your agent's performance, scalability, cost, and security.

## Agent development frameworks

_Agent development frameworks_ are libraries that simplify the process of building, testing, and deploying agentic AI applications. These development tools provide prebuilt components and abstractions for core agent capabilities, including reasoning loops, memory, and tool integration.

To accelerate agent development in Google Cloud, we recommend that you use [ADK](https://adk.dev/). ADK is an open-source, opinionated, and modular framework that provides a high-level of abstraction for building and orchestrating workflows from simple tasks to complex, multi-agent systems. ADK is optimized for Gemini models and Google Cloud, but it's built for compatibility with other frameworks. ADK supports other AI models and runtimes, so you can use it with any model or deployment method.

To help you get started quickly, ADK provides [code samples](https://github.com/google/adk-recipes) that demonstrate a variety of use cases across multiple industries. Although many of these samples highlight conversational flows, ADK is also well-suited for building autonomous agents that perform backend tasks. For these non-interactive use cases, choose an agent design pattern that excels in processing a single, self-contained request and that implements robust error handling.

To build a custom agent architecture, you can also use a general-purpose AI framework like [Genkit](https://genkit.dev/). Genkit provides primitives that let you have fine-grain control over your [agent logic](https://genkit.dev/docs/js/agentic-patterns/) without the high-level abstraction that ADK offers. However, a dedicated agent framework like ADK provides specialized tools for developing agentic applications.

## Frontend framework

The _frontend framework_ is a collection of prebuilt components, libraries, and tools that you use to build the UI for your agentic application. The frontend framework that you choose defines the requirements for your backend. A basic interface for an internal demo might only require a synchronous HTTP API, while a production-grade application requires a backend that supports streaming protocols and robust state management.

Consider the following categories of frameworks:

  * **Prototyping and internal tool frameworks** : For rapid development, internal demos, and proof-of-concept applications, choose frameworks that prioritize developer experience and velocity. These frameworks typically favor a direct, synchronous model that's called a _request-response model_. A request-response model lets you build a functional UI with minimal code and less backend complexity compared to a production framework. This approach is ideal for quickly testing agent logic and tool integrations, but it might not be suitable for highly scalable, public-facing applications that require real-time interactions. Common options in this category include the built-in [Agent Development Kit (ADK) web interface](https://adk.dev/runtime/web-interface/) and [Gradio](https://gradio.app/).
  * **Production frameworks** : For scalable, responsive, and feature-rich applications for external users, choose a framework that allows for custom components. These frameworks require a backend architecture that can support a modern user experience. A production framework should include support for streaming protocols, a stateless API design, and a robust, externalized memory system to manage conversation state across multiple user sessions. Common frameworks for production applications include [Streamlit](https://streamlit.io/), [React](https://react.dev/), and the [Flutter AI Toolkit](https://docs.flutter.dev/ai/ai-toolkit).



To manage the communication between these frameworks and your AI agent, you can use open agent-frontend protocols:

  * [ Agent–User Interaction (AG-UI) protocol](https://docs.ag-ui.com/introduction): An open, event-based protocol that enables backend AI agents to interact with your frontend framework. AG-UI tells the frontend framework when to render the agent's response, update application state, or trigger a client-side action. For more information, see [AG-UI with ADK](https://adk.dev/integrations/ag-ui/).
  * [ Agent-to-UI (A2UI)](https://a2ui.org/): An open format and protocol that lets backend agents stream declarative, structured UI components to the client application. For more information, see [A2UI in ADK](https://adk.dev/integrations/a2ui/).



## Agent security and governance

AI agents introduce certain unique and critical security risks that conventional, deterministic security practices might not be able to mitigate adequately. Google recommends an [approach for securing AI](https://cloud.google.com/security/securing-ai) that combines deterministic security controls with dynamic, reasoning-based defenses across every boundary of your architecture.

To enforce security and governance across your agentic AI workload in Google Cloud, use the following products and services:

  * [ Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview): A service that provides a secure and scalable way to connect your agents to external tools and services. 
    * In Client-to-Agent (ingress) mode, you deploy [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-gateway-runtime-deploy) in front of your agent runtime to authenticate callers, enforce authorization policies, and inspect inbound prompts in real time.
    * In Agent-to-Anywhere (egress) mode, you route outbound agent-to-agent and agent-to-tool requests through Agent Gateway. Agent Gateway helps prevent data exfiltration, indirect prompt injection, and tool misuse by enforcing default-deny access policies.
  * [ Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview): A managed service that provides a secure and scalable way to manage the identities of your agents. You can use Agent Identity when you deploy agents to authenticate agent calls to Google Cloud APIs, tools, and other agents. When agents need to authenticate to external tools or third-party APIs, you can use the [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager) to centrally control OAuth tokens and API keys instead of embedding credentials in agent code or prompts.
  * [ Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry): A service that provides a centralized inventory and catalog for your organization's AI agents, MCP servers, agent skills, and tools and helps ensure that only verified tools and subagents are used. When you [register MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers) and [A2A agents](https://docs.cloud.google.com/agent-registry/register-agents) in Agent Registry and combine it with Agent Gateway, you restrict agents to discovering and connecting only to approved endpoints instead of unmanaged or public URLs.
  * [Identity and Access Management (IAM) access policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap) and [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/agent-overview): Access control services that enforce fine-grained, least-privilege authorization across agents, tools, and resources. You use IAM access policies and [IAP](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp) to grant each agent identity only the permissions that it needs to perform its tasks and to invoke registered MCP servers or A2A subagents. To further isolate each agent and limit the potential impact of a security breach, you can bind [Principal Access Boundary (PAB)](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) policies to the agent identity.
  * [ Model Armor](https://cloud.google.com/security/products/model-armor): A service that provides protection for your generative and agentic AI resources against prompt injection, sensitive data leaks, and harmful content. You can use Model Armor for direct model API calls and attach it to [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor) to enforce safety and security policies consistently across inbound and outbound agent traffic.



## Agent tools

An agent's ability to interact with external systems through tools defines its effectiveness. _Agent tools_ are functions or APIs that are available to the AI model and that the agent uses to enhance output and allow for task automation. When you connect an AI agent to external systems, tools transform the agent from a standalone text generator into a system that can automate complex, multi-step tasks.

To enable tool interactions, choose from the following tool use patterns:

Use case | Tool use pattern  
---|---  
You need to perform a common task like completing a web search, running a calculation, or executing code, and you want to accelerate initial development. | Built-in tools  
You want to build a modular or multi-agent system that requires interoperable and reusable tools. | Model Context Protocol (MCP)  
You need to manage, secure, and monitor a large number of API-based tools at an enterprise scale. | API management platform  
You need to integrate with a specific internal or third-party API that doesn't have an MCP server. | Custom function tools  
  
When you select tools for your agent, evaluate them on their functional capabilities and their operational reliability. Prioritize tools that are observable, easy to debug, and that include robust error handling. These capabilities help to ensure that you can trace actions and resolve failures quickly. In addition, evaluate the agent's ability to select the right tool to successfully complete its assigned tasks.

### Built-in tools

ADK provides several [built-in tools](https://adk.dev/integrations/) that are integrated directly into the agent's runtime. You can call these tools as [functions](https://adk.dev/tools-custom/function-tools/) without configuring external communication protocols. These tools provide common functionalities, including accessing real-time information from the web, executing code programmatically in a secure environment, retrieving information from private enterprise data to implement RAG, and interacting with structured data in cloud databases. The built-in tools work alongside any custom tools that you create.

### MCP

To enable the components of your agentic system to interact, you need to establish clear communication protocols. [MCP](https://modelcontextprotocol.io/docs/) is an open protocol that provides a standardized interface for agents to access and use the necessary tools, data, and other services.

MCP decouples the agent's core reasoning logic from the specific implementation of its tools, similar to how a standard hardware port allows different peripherals to connect to a device.

MCP provides the following benefits:

  * Simplifies tool integration by providing prebuilt connectors. When more tools are added to an MCP server, the agent discovers the tools without additional configuration.
  * Provides a consistent way to build custom integrations.
  * Provides flexibility and promotes interoperability across different models and tools.



You can implement MCP servers within your agentic AI system by using the following methods:

  * [**Google Cloud MCP servers**](https://docs.cloud.google.com/mcp/overview): To connect to Google and Google Cloud services, connect to remote MCP servers that are fully-managed by Google. These servers enhance your existing infrastructure by providing a unified layer across all of the Google and Google Cloud services that you use. These servers provide stateless scaling and integration with IAM and Cloud Audit Logs. For a list of Google Cloud MCP servers, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).
  * **Remote MCP servers** : To connect to external APIs, connect to a remote MCP server that is hosted and managed by a third party.
  * **Self-hosted MCP servers** : To implement your own agent logic and custom tools, host your own MCP server. You have full control over how you expose proprietary or third-party APIs to your agents. To host your own custom MCP server, deploy it as a containerized application on Cloud Run or Google Kubernetes Engine (GKE).



### API management platform

An _API management platform_ is a centralized system that lets you secure, monitor, and control internal or external services through APIs. An API management platform provides a centralized location to catalog all of your organization's APIs, simplifies how you expose data, and provides observability through usage monitoring.

To manage and govern your agent's API-based tools at an enterprise scale on Google Cloud, combine the following services:

  * **Catalog and discovery** : To centrally catalog and govern your organization's APIs, MCP servers, and agentic skills, use [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub). API hub exposes an MCP server so that agents and developers can discover registered tools, and it synchronizes MCP metadata with Agent Registry.
  * **Runtime policy enforcement** : To enforce authentication, fine-grained authorization, token and rate limiting, semantic caching, and monitoring for API endpoints and MCP servers, use [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/ai-capabilities) or [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) as an API and AI gateway.
  * **Prebuilt data and enterprise connectors** : To connect agents to enterprise applications and Google Cloud data sources without building custom integration pipelines, use [Application Integration and Integration Connectors](https://adk.dev/integrations/application-integration/) or [MCP Toolbox for Databases](https://adk.dev/integrations/mcp-toolbox-for-databases/).



An API management platform and a communication protocol like MCP solve different architectural problems. A communication protocol standardizes the interaction format between the agent and the tool, which helps ensure that components are reusable and can be swapped. By contrast, an API management platform governs the lifecycle and security of the API endpoint, handling tasks like authentication, rate limiting, and monitoring. These patterns are complementary. For example, an agent can use MCP to communicate with a tool, and that tool can, in turn, be a secure API endpoint that API hub catalogs and that Apigee or Agent Gateway manages and protects.

### Custom function tool

A [function tool](https://adk.dev/tools-custom/function-tools/#function-tool) gives an agent new capabilities. You can write a custom function tool to give your agent specialized capabilities, such as to integrate with an external API or a proprietary business system. Writing a custom function tool is the most common pattern for extending an agent's abilities beyond what built-in tools can offer.

To create a custom function tool, you write a function in your preferred programming language and then provide a clear, natural-language description of its purpose, parameters, and return values. The agent's model uses this description to reason about when the tool is needed, what inputs to provide, and how to interpret the output to complete a user's request.

You can also create a custom function tool that implements an [agent-as-a-tool function](https://adk.dev/tools-custom/function-tools/#agent-tool). An agent-as-a-tool function exposes one agent as a callable function that another agent can invoke. This technique lets you build complex, multi-agent systems where an agent can coordinate and delegate specialized tasks to other, specialized agents. For more information about agent design patterns and coordinating multi-agent orchestration, see the section on agent design patterns later in this document.

### Tool bloat

_Tool bloat_ occurs when you provide too many tool definitions in the system prompt of an AI model. A model can be overwhelmed by an excessive number of tools, complex parameters, or detailed descriptions in the model's context window.

When an AI agent is overloaded with tool bloat, the following problems can occur:

  * **Decreased accuracy** : Irrelevant tokens dilute the model's attention across the context window. When the model's attention is diluted, it's difficult for the model to accurately distinguish the correct tool from noise.
  * **Increased costs and latency** : A single user request can trigger multiple hidden reasoning loops and tool executions. An increase in the number of loops and executions causes a corresponding increase in cost and tool response times.



To mitigate tool bloat, you can implement the following strategies:

  * **Limit tool complexity** : The following are recommendations to write concise tool definitions: 
    * Use primitive data types instead of complex nested objects.
    * Limit tools to fewer than five parameters.
    * Constrain the model's decision path by using `enums` instead of free-text strings.
  * **Provide granular toolsets** : Unbundle monolithic servers into granular, focused toolsets that are based on specific user journeys. For example, a massive Cloud SQL server can be segregated into an administrator toolset for DevOps agents and a data toolset for app agents.
  * **Implement progressive disclosure** : Design systems to dynamically unlock relevant context and capabilities only when they are needed, rather than loading everything in advance. To implement a progressive disclosure approach, use the following strategies: 
    * **Search tool pattern** : To reduce token consumption, implement an agent that uses a single search tool to dynamically load only the relevant tool schema.
    * **Agent Skills** : [Agent Skills](https://agentskills.io/home) are an open standard format that enables progressive discovery of instructions, scripts, and other resources. To minimize context bloat, define [skills in ADK](https://adk.dev/skills/) that direct the agent to load specialized instructions and resources on demand, or discover and load governed enterprise skills from [Skill Registry](https://adk.dev/integrations/skills-registry/).
    * **Multi-agent delegation** : To reduce an agent's context window, implement a multi-agent system that uses a coordinator agent to delegate a specific task to a specialized subagent. This approach helps ensure that only relevant tools are loaded and it keeps the coordinator agent's context window concise.



These strategies aren't mutually exclusive and they should be combined based on your architecture and workload requirements.

## Agent memory

An agent's ability to remember past interactions is fundamental to provide a coherent and useful conversational experience. To create stateful, context-aware agents, you must implement mechanisms for short-term memory and long-term memory. The following sections explore the design choices and Google Cloud services that you can use to implement both short-term and long-term memory for your agent.

### Short-term memory

Short-term memory enables an agent to maintain context within a single, ongoing conversation. To implement short-term memory, you must manage both the session and its associated state.

  * [**Session**](https://adk.dev/sessions/session/): A session is the conversational thread between a user and the agent, from the initial interaction to the end of the dialogue.
  * [**State**](https://adk.dev/sessions/state/): State is the data that the agent uses and collects within a specific session. The state data that's collected includes the history of messages that the user and agent exchanged, the results of any tool calls, and other variables that the agent needs in order to understand the context of the conversation.



The following are options for [implementing short-term memory with ADK](https://adk.dev/sessions/session/#sessionservice-implementations):

  * **In-memory storage** : For development, testing, or small-scale applications that run on a single instance, you can store the session state directly in your application's memory. The agent uses a data structure, such as a dictionary or an object, to store a [list of key-value pairs](https://adk.dev/sessions/state/#key-characteristics-of-state) and it updates these values throughout the session. However, when you use in-memory storage, session state isn't persistent. If the application restarts, it loses all conversation history.
  * **External state management** : For production applications that require scalability and reliability, we recommend that you build a stateless agent application and manage the session state in an external storage service. In this architecture, each time the agent application receives a request, it retrieves the current conversation state from the external store, processes the new turn, and then saves the updated state back to the store. This design lets you scale your application horizontally because any instance can serve any user's request. Common choices for external state management include [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview), [Firestore](https://docs.cloud.google.com/firestore/native/docs/overview), or [Gemini Enterprise Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions).

If you use ADK, the [`DatabaseSessionService`](https://adk.dev/sessions/session/#databasesessionservice) requires a relational database, such as [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction).




### Long-term memory

[Long-term memory](https://adk.dev/sessions/memory/) provides the agent with a persistent knowledge base that exists across all conversations for individual users. Long-term memory lets the agent retrieve and use external information, learn from past interactions, and provide more accurate and relevant responses.

The following are options for implementing long-term memory with ADK:

  * **In-memory storage** : For development and testing, you can store long-term memory entries directly in your application's memory and perform basic keyword matching across stored entries. This approach requires minimal setup, but it isn't persistent. If the application restarts, it loses all stored memory entries. You typically implement this pattern by using an in-memory provider within a development framework, such as the [`InMemoryMemoryService`](https://adk.dev/sessions/memory/#inmemorymemoryservice) that's included in ADK for prototyping and testing.
  * **External storage** : For production applications, manage your agent's knowledge base in an external, persistent storage service. An external storage service helps ensure that your agent's knowledge is durable, scalable, and accessible across multiple application instances. Use [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) for long-term storage with any agent runtime on Google Cloud.



## Agent design patterns

Agent design patterns are common architectural approaches to build agentic applications. These patterns offer a distinct framework for organizing a system's components, integrating the AI model, and orchestrating a single agent or multiple agents to accomplish a workflow. To determine which approach is best for your workflow, you must consider the complexity and workflow of your tasks, latency, performance, and cost requirements.

A [single-agent system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#single-agent-system) relies on one model's reasoning capabilities to interpret a user's request, plan a sequence of steps, and decide which tools to use. This approach is an effective starting point that lets you focus on refining the core logic, prompts, and tool definitions before you add architectural complexity. However, a single agent's performance can degrade as tasks and the number of tools grow in complexity.

For complex problems, a [multi-agent system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#multi-agent-systems) orchestrates multiple specialized agents to achieve a goal that a single agent can't easily manage. This modular design can improve the scalability, reliability, and maintainability of the system. However, it also introduces additional evaluation, security, and cost considerations compared to a single-agent system.

To implement single-agent and multi-agent patterns, ADK provides a [workflow runtime](https://adk.dev/workflows/) that supports the following orchestration workflows:

  * **[Graph-based workflows](https://adk.dev/graphs/)** : Define agent logic as a graph of execution nodes and edges that combines AI-assisted reasoning with deterministic code and tools. Graph-based workflows provide predictable execution paths with explicit state transitions, conditional routing, parallel branches, and human-in-the-loop checkpoints.
  * **[Dynamic workflows](https://adk.dev/graphs/dynamic/)** : Build workflows programmatically in your chosen programming language instead of using static graph structures. Dynamic workflows let you invoke workflow nodes as functions, define complex control flow by using loops, conditionals, and recursion, and automatically checkpoint node executions so that workflows are durable and resumable.
  * **[Collaborative workflows](https://adk.dev/workflows/collaboration/)** : Coordinate multiple specialized agents that delegate tasks and share context to solve complex problems.



When you develop a multi-agent system, you must implement precise access controls for each specialized agent, design a robust orchestration system to ensure reliable inter-agent communication, and manage the increased operational costs from the computational overhead of running multiple agents. To facilitate communication between agents, use [Agent2Agent (A2A) protocol with ADK](https://adk.dev/a2a/). A2A is an open standard protocol that enables AI agents to communicate and collaborate across different platforms and frameworks, regardless of their underlying technologies.

For more information about common agent design patterns and how to select a pattern based on your workload requirements, see [Choose a design pattern for your agentic AI system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system).

## AI models

Agentic applications depend on the reasoning and understanding capabilities of a model to act as the primary task orchestrator. For this core agent role, we recommend that you use [Gemini Pro](https://deepmind.google/models/gemini/pro/).

Google models, like Gemini, provide access to the latest and most capable proprietary models through a managed API. This approach is ideal for minimizing operational overhead. In contrast, an open, self-hosted model provides the deep control that's required when you fine-tune on proprietary data. Workloads with strict security and data residency requirements also require a self-hosted model, because it lets you run the model within your own network.

To improve agent performance, you can adjust the model's reasoning capabilities. Models such as the latest [Gemini models](https://deepmind.google/models/gemini/) feature a built-in thinking process that improves reasoning and multi-step planning. For debugging and refinement, you can review the model's [thought summaries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking#thought-summaries), or synthesized versions of its internal thoughts, to understand its reasoning path. You can [control model thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking#configure-thinking) based on task complexity and the model version. A higher thinking level or thinking budget lets the model perform more detailed reasoning and planning before it provides an answer, which can improve response quality, but it might also increase latency and cost.

To optimize for performance and cost, implement [model routing](https://adk.dev/agents/models/routing/) to dynamically select the most appropriate model for each task based on the task's complexity, cost, or latency requirements. For example, you can route simple requests to a small language model (SLM) for structured tasks like code generation or text classification, and reserve a more powerful and expensive model for complex reasoning. If you implement model routing in your agentic application, you can create a cost-effective system that maintains high performance.

Google Cloud provides access to a wide selection of Google models, partner models, and open models that you can use in your agentic architecture. For more information on the models that are available and how to choose a model to fit your needs, see [Model Garden on Gemini Enterprise Agent Platform](https://cloud.google.com/model-garden#choose-a-model-that-fits-your-needs).

## Model runtime

A model runtime is the environment that hosts and serves your AI model and that makes its reasoning capabilities available to your agent.

### Choose a model runtime

To select the appropriate runtime for your AI model, use the following guidance:

Use case | Model runtime  
---|---  
You need a fully managed API to serve Gemini models, partner models, open models, or custom models with enterprise-grade security, scaling, and generative AI tools. | Agent Platform  
You need to deploy an open or custom containerized model and prioritize minimal operational overhead and cost-efficiency for variable traffic. | Cloud Run  
You need maximum control over the infrastructure to run an open or custom containerized model on specialized hardware or to meet complex security and networking requirements. | GKE  
  
The following sections provide an overview of the preceding model runtimes, including key features and design considerations.

#### Agent Platform

[Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models) provides a fully managed, serverless environment that hosts your AI models. You can serve and fine-tune Google models, partner models, and open models through a secure and scalable API. This approach abstracts away infrastructure management, and it lets you focus on integrating model intelligence into your applications.

When you use Agent Platform as a model runtime, the key features and considerations include the following:

  * **Infrastructure control** : A fully managed API for your models. Google manages the underlying infrastructure.
  * **Security** : Managed security defaults and standard compliance certifications are sufficient for your needs. To provide prompt and response protection and to ensure responsible AI practices, you can integrate [Model Armor](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration) into Agent Platform.
  * **Model availability** : Access to a wide selection of models, including the latest Gemini models, through a managed API.
  * **Cost** : Pay-per-use pricing model that scales with your application's traffic. For more information, see [Cost of building and deploying AI models in Agent Platform](https://cloud.google.com/model-garden/pricing).



#### Cloud Run

Cloud Run provides a serverless runtime that hosts your models inside custom containers. Cloud Run offers a balance between the fully managed experience of Agent Platform and the deep infrastructure control of GKE. This approach is ideal when you need the flexibility to run your model in a containerized environment without managing servers or clusters.

When you use Cloud Run as a model runtime, the key features and considerations include the following:

  * **Infrastructure control** : Run any model in a custom container, which provides full control over the software environment, while the platform manages the underlying serverless infrastructure.
  * **Security** : Provides security through ephemeral, isolated compute instances and allows for secure connections to private resources by using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) or a [Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors). For more information, see [Private networking and Cloud Run](https://docs.cloud.google.com/run/docs/securing/private-networking#from-vpc).
  * **Model availability** : Serve open models such as Gemma or serve your own custom models. You can't host or serve Gemini models on Cloud Run.
  * **Cost** : Features a pay-per-use, request-based pricing model that scales to zero, which makes it highly cost-effective for models with sporadic or variable traffic. For more information, see [Cloud Run pricing](https://cloud.google.com/run/pricing).



#### GKE

GKE provides the most control and flexibility for hosting your AI models. To use this approach, you run your models in containers on a GKE cluster that you configure and manage. GKE is the ideal choice when you need to run models on specialized hardware, colocate them with your applications for minimal latency, or require granular control over every aspect of the serving environment.

When you use GKE as a model runtime, the key features and considerations include the following:

  * **Infrastructure control** : Provides maximum, granular control over the entire serving environment, including node configurations, specialized machine accelerators, and the specific model serving software.
  * **Security** : Provides granular control over security and data isolation because it lets you run models entirely within your network and apply fine-grained Kubernetes security policies. To screen traffic to and from a GKE cluster and to help protect interactions with the AI models, you can integrate [Model Armor](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations#ai-safety-checks) with GKE.
  * **Model availability** : Serve open models such as Gemma, or serve your own custom models. You can't host or serve Gemini models on GKE.
  * **Cost** : Features a cost model that's based on the underlying compute and cluster resources that you consume, which makes it highly optimized for predictable, high-volume workloads when you use [committed use discounts (CUDs)](https://docs.cloud.google.com/kubernetes-engine/cud). For more information, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).



This document focuses on Agent Platform, Cloud Run, and GKE. If you require a model runtime that combines performance-optimized hardware (GPUs and TPUs), open software, and flexible consumption models for large-scale model training, fine-tuning, and inference workloads, use [AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/overview).

## Agent runtime

To host and deploy your agentic application, you must choose an agent runtime. This service runs your application code, the business logic, and orchestration that you write when you use an agent development framework. From this runtime, your application makes API calls to the models that your chosen model runtime hosts and manages.

### Choose an agent runtime

Google Cloud offers agent hosting options from fully managed, low-overhead environments to full-control infrastructure. Agent Platform is architected for flexibility so that you can choose the runtime layer and service layer that fits your needs. To select the runtime for your AI agents, use the following guidance:

Use case | Agent runtime  
---|---  
You require an opinionated, managed runtime that includes integrations for memory, evaluation, identity, governance, and observability. | Agent Runtime on Gemini Enterprise Agent Platform  
You require a container deployment and portability with a balance of flexibility and control to run your containerized agents like any other service. | Cloud Run  
You require full control, with fine-grained control over the underlying infrastructure. Your platform team manages its own DevOps, Kubernetes APIs, or strict compliance and data residency requirements. | GKE  
  
If you already manage applications on Cloud Run or on GKE, you can accelerate development and simplify long-term operations by using the same platform for your agentic workload.

The following sections provide an overview of each agent runtime, including key features and design considerations.

###  Agent Runtime 

[Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) is a fully-managed, opinionated runtime that you can use to deploy, operate, and scale agentic applications. Agent Runtime abstracts away the underlying infrastructure, which lets you focus on agent logic instead of operations.

The following are features and considerations for Agent Runtime:

  * **Programming language and framework flexibility** : Develop agents with any [supported frameworks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/quickstart).
  * **Communication protocols** : Orchestrate agents and tools that use MCP and A2A. Agent Runtime efficiently manages the runtime for these components, but it doesn't support the hosting of custom MCP servers.
  * **Memory** : Provides built-in, managed memory capabilities, which removes the need to configure external databases for core agent memory.

    * For short-term memory storage, use [Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions).
    * For long-term memory storage, use [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank).
    * For database search and retrieval, use [Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/introduction) or [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview).
  * **Scalability** : Automatically scales to meet the demands of your agentic workload, which removes the need for manual configuration.
  * **Observability** : Provides integrated logging, monitoring, and tracing through [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability) services.
  * **Security** : Provides the following enterprise-level capabilities: 
    * Built-in service identity and [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) for secure, authenticated calls to Google Cloud APIs, other agents, and tools.
    * Run code in a secure, isolated, and managed sandbox with [Gemini Enterprise Agent Platform Code Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-overview).
    * Protect your data with your own [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/cmek) in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service).
    * Restrict [IAM permissions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control) and [use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls) to help prevent unauthorized network calls.



Agent Runtime accelerates the path to production because it provides a managed environment with integrations for memory, agent evaluations, agent identity, governance, security, and observability. For workloads that have strict security requirements for private dependency management, Cloud Run and GKE offer IAM-based configuration path.

### Cloud Run

[Cloud Run](https://cloud.google.com/run) is a fully managed, serverless platform that lets you run your agent application code in a stateless container. Cloud Run is ideal when you want to deploy the entire agent application, individual components, or custom tools as scalable HTTP endpoints without needing to manage the underlying infrastructure.

The following are features and considerations for Cloud Run:

  * **Programming language and framework flexibility** : When you package your application in a container, you can develop and deploy containerized services in any programming language and with any agent framework.
  * **Communication protocols** : Supports gRPC, HTTPS, streaming HTTP responses, and WebSockets, and orchestrates agents and tools that use MCP and A2A. [Host MCP clients and servers](https://docs.cloud.google.com/run/docs/host-mcp-servers) with streamable HTTP transport on Cloud Run.
  * **Memory** : Cloud Run instances are stateless, which means that an instance loses any in-memory data after it terminates. To implement persistent memory, connect your service to a managed Google Cloud storage service: 
    * For short-term memory, consider the following products and services:

      * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run)
      * [Agent Platform Sessions with Cloud Run](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/cloud_run/agents_with_memory/get_started_with_memory_for_adk_in_cloud_run.ipynb)
      * [Firestore](https://docs.cloud.google.com/firestore/native/docs/overview)
      * [ADK's `DatabaseSessionService`](https://adk.dev/sessions/session/#databasesessionservice) with [Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/introduction)
    * For long-term memory, consider the following products:

      * Firestore
      * [Memory Bank with Cloud Run](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/cloud_run/agents_with_memory/get_started_with_memory_for_adk_in_cloud_run.ipynb)
    * For database search and retrieval, consider the following products:

      * Cloud SQL
      * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview)
  * **Scalability** : [Automatically scales the number of instances](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) based on incoming traffic, and also scales instances down to zero. This feature helps make Cloud Run cost-effective for applications that have variable workloads.
  * **Observability** : Provides integrated logging, monitoring, and tracing through [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability) services. For more information, see [Monitoring and logging overview](https://docs.cloud.google.com/run/docs/monitoring-overview).
  * **Security** : Provides the following security controls for your agents: 
    * Built-in service identity and integration with [Agent Identity and Agent Registry](https://docs.cloud.google.com/run/docs/ai/agent-platform-features) for cryptographically verifiable agent identity, discovery, and authenticated calls to Google Cloud APIs, other agents, and tools.
    * Run untested code in a secure environment with [Cloud Run sandboxes](https://docs.cloud.google.com/run/docs/code-execution) or with [Agent Platform Code Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-overview).
    * Store sensitive data that Cloud Run uses by [configuring secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets) in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs).
    * Help prevent unauthorized network calls by restricting [IAM permissions](https://docs.cloud.google.com/run/docs/securing/managing-access) and using [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).



Cloud Run reduces operational overhead and improves cost-effectiveness because it removes the need to manage underlying infrastructure. However, the stateless nature of Cloud Run requires you to use a storage service to manage context across a multi-step workflow. Additionally, the maximum request timeout for Cloud Run services is up to one hour, which might constrain long-running agentic tasks.

### GKE

[GKE](https://cloud.google.com/kubernetes-engine) is a managed container orchestration service that provides granular control over your agentic application's architecture and infrastructure. GKE is suitable for complex agentic systems that require robust, production-grade capabilities or if you are already a GKE customer and you want to implement an agentic workflow on top of your existing application.

The following are features and considerations that are available on GKE:

  * **Programming language and framework flexibility** : When you package your application in a container, you can develop agents in any programming language and with any framework.
  * **Communication protocols** : Orchestrate agents and tools that use MCP and A2A. Host MCP clients and servers on GKE when you package them as containers.
  * **Memory** : GKE pods are ephemeral. However, you can build stateful agents with persistent memory by using in-cluster resources or by connecting to external services. 
    * For short-term memory, consider the following products and services:

      * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gke)
      * [Agent Platform Sessions with GKE](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/gke/agents_with_memory/get_started_with_memory_for_adk_in_gke.ipynb)
      * [Firestore](https://docs.cloud.google.com/firestore/native/docs/overview)
      * [ADK's `DatabaseSessionService`](https://adk.dev/sessions/session/#databasesessionservice) with [Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/introduction)
    * For long-term memory, consider the following products:

      * Firestore
      * [Memory Bank with GKE](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/gke/agents_with_memory/get_started_with_memory_for_adk_in_gke.ipynb)
    * For database search and retrieval, consider the following products:

      * [StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) and [Persistent Volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) for durable storage within your cluster.
      * Cloud SQL
      * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview)
  * **Scalability** : GKE clusters [automatically provision](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) and [scale](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) your node pools to meet the requirements of your workload.
  * **Observability** : Provides integrated logging, monitoring, and tracing at the cluster, node, and pod levels with Google Cloud Observability. To collect configured third-party and user-defined metrics and then send them to Cloud Monitoring, you can also use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus). For more information, see [Overview of GKE observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).
  * **Security** : Provides fine-grained security controls for your agents: 
    * Use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) for secure authentication to Google Cloud APIs.
    * Isolate untrusted code with [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).
    * [Store sensitive data that your GKE clusters use](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component) in Secret Manager.
    * Restrict [IAM permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam) and use [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) and [Network Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) to help prevent unauthorized network calls.



GKE provides maximum control and flexibility, which lets you run complex, stateful agents. However, this control introduces significant operational overhead and complexity. You must configure and manage the Kubernetes cluster, including node pools, networking, and scaling policies, which requires more expertise and development effort than a serverless platform requires.

## What's next

  * Agent tools: 
    * [Build custom tools for agents in ADK](https://adk.dev/tools-custom/).
    * [Tools and integrations for ADK agents](https://adk.dev/integrations/).
    * [Evaluate agents in ADK](https://adk.dev/evaluate/).
    * [How to deploy a secure MCP server on Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run/how-to-deploy-a-secure-mcp-server-on-cloud-run).
  * Agent memory: 
    * [Memory Bank quickstart with ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/adk-quickstart).
    * [Session, state, and memory in ADK](https://adk.dev/sessions/).
  * Agent design patterns: 
    * [Choose a design pattern for your agentic AI system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system).
    * [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system).
    * [Workflows in ADK](https://adk.dev/workflows/).
    * [Common agentic patterns in ADK](https://adk.dev/workflows/patterns/).
  * Agent runtime: 
    * [Develop and deploy agents on Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/quickstart-adk).
    * [Host AI apps and agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Other agentic AI resources on Google Cloud: 
    * [Agents and application security controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/agents-applications).
    * [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview).
    * [Agent Identity overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview).
    * [The Agent Factory playlist](https://www.youtube.com/embed/playlist?list=PLIivdWyY5sqLXR1eSkiM5bE6pFlXC-OSs).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer

Other contributors: 

  * [Amina Mansour](https://www.linkedin.com/in/aminamansour/) | Tech Lead, Global Developer Relations & Strategic Content
  * [Amit Maraj](https://www.linkedin.com/in/amit-maraj) | Developer Relations Engineer
  * [Casey West](https://www.linkedin.com/in/caseywest) | Architecture Advocate, Google Cloud
  * [Jack Wotherspoon](https://www.linkedin.com/in/jack-wotherspoon) | Developer Advocate
  * [Joe Fernandez](https://www.linkedin.com/in/joefernandez007/) | Staff Technical Writer
  * [Joe Shirey](https://www.linkedin.com/in/jshirey) | Cloud Developer Relations Manager
  * [Karl Weinmeister](https://www.linkedin.com/in/karlweinmeister/) | Director of Cloud Product Developer Relations
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Kurtis Van Gent](https://www.linkedin.com/in/kurtisvg) | Staff Software Engineer
  * [Lisa Shen](https://www.linkedin.com/in/lisa-shen-6167241/) | Senior Outbound Product Manager, Google Cloud
  * [Mandy Grover](https://www.linkedin.com/in/mandygrovermatc/) | Head of Architecture Center
  * [Megan O'Keefe](https://www.linkedin.com/in/askmeegs) | Developer Advocate
  * [Olivier Bourgeois](https://www.linkedin.com/in/olivi-eh/) | Developer Relations Engineer
  * [Polong Lin](https://www.linkedin.com/in/polonglin) | Developer Relations Engineering Manager
  * [Ryan Pei](https://www.linkedin.com/in/ryanpei/) | Product Manager, Google Cloud
  * [Shir Meir Lador](https://www.linkedin.com/in/shirmeirlador) | Developer Relations Engineering Manager
  * [Vlad Kolesnikov](https://www.linkedin.com/in/vkolesnikov) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
