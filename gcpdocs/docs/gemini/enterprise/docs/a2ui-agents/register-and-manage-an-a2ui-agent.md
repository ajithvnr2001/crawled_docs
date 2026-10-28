---
url: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent/
title: Register and manage agents using A2UI and A2A \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:26:55.312527+00:00
---

# Register and manage agents using A2UI and A2A  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Register and manage agents using A2UI and A2A Stay organized with collections  Save and categorize content based on your preferences. 

A Gemini Enterprise administrator can register an agent that uses [Agent to UI (A2UI)](https://a2ui.org/introduction/what-is-a2ui/) to build custom interfaces and the [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) for communication with Gemini Enterprise.

Gemini Enterprise supports all the standard A2UI components. These components render using Gemini Enterprise's built-in styling. For information and examples using the basic catalog, see the [A2UI components basic catalog](https://a2ui-composer.ag-ui.com/basic-catalog) and the [A2UI components custom catalog](https://a2ui-composer.ag-ui.com/custom-catalog). For information on material catalog components, see [Material catalog components](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference#material_catalog_components)

**Note:** Gemini Enterprise supports A2UI versions v0.9 and v0.8. For more information about A2UI versions, see [Specification Versions](https://a2ui.org/#specification-versions) in the A2UI documentation.

## Register an agent using A2UI and A2A

To register your agent and enable it to interact with Gemini Enterprise using A2UI and the A2A Protocol, follow these steps:

![Diagram illustrating the steps to register an agent using A2UI and A2A, including configuring the agent, hosting it, and registering it with Gemini Enterprise.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/a2ui-agent/overview-a2ui-agents.png)

### Configure your agent to use A2UI and the A2A protocols

Implement the specifications and libraries provided by [Agent to UI (A2UI)](https://a2ui.org/introduction/what-is-a2ui/) for building interactive user interfaces and the [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) for secure and standardized communication. This ensures that your agent can render user interfaces and communicate effectively with Gemini Enterprise.

### Host your agent

Deploy your configured agent to a publicly accessible endpoint. You can use Google Cloud resources for hosting, such as:

  * **Agent Runtime on Gemini Enterprise Agent Platform** : A fully managed service designed for deploying and scaling AI agents.

  * **Cloud Run** : A serverless compute platform that lets you run containerized applications, which provides flexibility and automatic scaling.




Your agent must be accessible to Gemini Enterprise for A2A Protocol communication.

**Tip:** You must host and maintain your agents for them to function within Gemini Enterprise.

### Register the agent as an A2A agent with Gemini Enterprise

After your agent is hosted and accessible, a Gemini Enterprise administrator must register it with Gemini Enterprise as an A2A agent. For more information, see [Register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent).

### Manage agents

After registering your agents with Gemini Enterprise, a Gemini Enterprise administrator can view and manage the agents on the **Agents** page. For more information, see [Agents overview](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview).

## What's next

  * For a reference of available A2UI components, see [A2UI component gallery reference](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
