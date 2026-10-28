---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/salesforce/
title: Salesforce tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:35:46.719393+00:00
---

# Salesforce tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/salesforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Salesforce tools Stay organized with collections  Save and categorize content based on your preferences. 

This tool is used to connect to a Salesforce instance. When you first create the tool, you provide:

  * **Name** : Tool name
  * **Server** : Salesforce server instance
  * **Authentication** : See [OpenAPI tool API authentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api#openapi-authentication)



Once you have provided that info, you can view or update the generated [OpenAPI schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api) and provide advanced settings:

  * **Asynchronous execution** : When enabled, the agent will continue the session while the tool runs in the background.
  * **Schema fields** : Hide unspecified tool output fields in the OpenAPI schema from the model prompt.
  * **Custom TLS certificate authorities** : Optionally upload a custom certificate.
  * **Service Directory** : Optionally provide the name of a service directory.



When you add the tool to an agent, you can select from a list of predefined entities and operations in order to filter how an agent uses the tool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
