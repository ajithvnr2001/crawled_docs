---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-mcp-architecture/
title: Bring your own MCP server to kagent reference architecture \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:51:14.170647+00:00
---

# Bring your own MCP server to kagent reference architecture  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-mcp-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Bring your own MCP server to kagent reference architecture Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This solution addresses the need for a standardized, secure, and scalable mechanism for integrating [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) servers into Google Distributed Cloud software only (GDC) environments with [kagent](https://kagent.dev/) deployed as the agentic AI platform.

The core problem being addressed is the lack of a unified interface for connecting large language model (LLM) applications to localized data sources and tools within regulated GDC clusters. This architecture provides a Bring Your Own (BYO) framework that lets developers deploy custom MCP servers that expose specific enterprise capabilities as tools for AI agents.

This architecture covers the communication protocols between kagent and MCP servers and the component topology on GDC. It excludes the internal logic of third-party MCP servers.

The target audience for this document includes GDC platform administrators, AI application developers, and security reviewers responsible for approving external tool integrations.

### Features and capabilities

kagent provides a flexible framework that lets organizations use BYO MCP servers to integrate LLMs with local or proprietary tools. With this capability, agents can interact with specialized data sources and perform complex tasks within the perimeter of a GDC cluster.

### Functional components and responsibilities

The architecture includes the following functional components:

  * **AI agent platform (kagent):** Acts as the central orchestrator. It manages the lifecycle of the agentic session, routes user queries to the LLM, and coordinates tool execution through the MCP client.
  * **LLM:** Handles natural language understanding and reasoning. It determines when a specific tool is required to fulfill a request and generates the parameters needed to call that tool.
  * **MCP server:** Exposes specific tools through MCP as a standalone service. It handles the low-level logic of interacting with backend enterprise systems or data repositories.



### Interfaces and data flow

The end-to-end architecture relies on standardized interfaces to maintain interoperability and security:

  * **MCP transport:** kagent communicates with the MCP server using standardized JSON-RPC over a supported MCP transport, such as Streamable HTTP (or HTTP with SSE) or `stdio`. This interface defines how tools are discovered, described, and invoked.
  * **Data flow:** The request lifecycle follows these steps: 
    1. The user sends a prompt to kagent.
    2. kagent forwards the prompt to the LLM.
    3. The LLM identifies a tool call and returns it to kagent.
    4. kagent forwards the request to the MCP server.
    5. The MCP server runs the tool against the local data source and returns the result.
    6. kagent sends the result back to the LLM to generate the final response.



## Architecture

To demonstrate how to deploy and use a BYO MCP server, this reference architecture uses the open source [Nextcloud](https://nextcloud.com/) application, its MCP server, and the Nextcloud agent on [Solo Enterprise for kagent](https://www.solo.io/products/kagent-enterprise).

This example serves the Gemma 4 model using vLLM.

The architecture connects Nextcloud, kagent, and the Gemma 4 model within the GDC environment. In this configuration, kagent uses Nextcloud as a data repository so that the Gemma 4 model can access and process information in Nextcloud through standardized MCP interfaces.

Nextcloud is an open source, self-hosted collaboration and cloud storage platform that supports on-premises deployment to help you maintain control and privacy over user data. It's a component of openDesk.

Nextcloud includes the following features:

  * **File sync and share:** Store files, sync them across desktop and mobile devices through dedicated apps, and share them using links.
  * **Productivity tools:** Use built-in calendar, contacts, task management, and email clients.
  * **Collaboration:** Integrate office suites, such as Collabora Online or ONLYOFFICE, directly into Nextcloud to co-edit documents, spreadsheets, and presentations in real time.
  * **Extensibility:** Install plugins from the app store to add features such as password managers, Kanban boards, or music players.



This solution requires GDC with kagent and vLLM serving the Gemma 4 model. The following diagram illustrates the validation setup:

![Validation setup with GDC, kagent, Nextcloud, and vLLM serving Gemma 4.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/byo-mcp-server-kagent-diagram.png)

## Additional materials

  * [Deploy Solo Enterprise for kagent on Google Distributed Cloud software only reference implementation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-deployment-implementation)
  * [Bring your own MCP server to kagent reference implementation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-mcp-implementation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
