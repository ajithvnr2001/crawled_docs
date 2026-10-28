---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tool-integration-for-ai-coach/
title: Gemini Enterprise for Customer Experience tool integration for AI coach \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:32:16.161916+00:00
---

# Gemini Enterprise for Customer Experience tool integration for AI coach  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tool-integration-for-ai-coach/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Gemini Enterprise for Customer Experience tool integration for AI coach Stay organized with collections  Save and categorize content based on your preferences. 

Use Gemini Enterprise for Customer Experience tools to connect customer service agents to external systems. With tools, virtual agents created within Gemini Enterprise for Customer Experience can interact with other systems to retrieve, update, format, or analyze information. [AI coach](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-overview) can reuse these tools to improve its suggestions.

## Create a tool

Follow these steps to create a tool.

  1. Sign in to the Gemini Enterprise for Customer Experience console and click **Tools**.

[Gemini Enterprise for Customer Experience console](https://ces.cloud.google.com)

  2. Select a tool type.

  3. Fill out the information for the tool.

  4. Enter its name, using lower case and separating each word with an underscore.

  5. Optional: Provide the tool descriptions to agent models.




## Add Gemini Enterprise for Customer Experience tool in AI coach

Add tools while creating AI coach instructions. Follow these steps to add the Gemini Enterprise for Customer Experience tool in AI coach.

  1. Sign in to the Agent Assist console and click AI coach.

[Agent Assist console](https://agentassist.cloud.google.com)

  2. Enter **$** for the **tool** , and select one of the available tools from the list. The console lists only tools that you created in the same project.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
