---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-templates/
title: Use prompt templates \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:27:47.031515+00:00
---

# Use prompt templates  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Use prompt templates Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use prompt templates. A prompt template is a prompt that includes replaceable variables. Prompt templates enable you to test how different prompt formats perform with different prompt data, without requiring you to write multiple individual prompts.

Prompt template variables must meet the following requirements:

  * Variables must be wrapped in curly-braces.
  * Variable names must not contain spaces.



For example, consider the following prompts and their corresponding system instructions:

  * **System instructions** : Respond to the question concisely.
  * **Prompts** : 
    * Do coyotes eat berries?
    * Do eagles swim?
    * Do squirrels dig holes?



The corresponding prompt template would be similar to the following:

  * **Prompt template** : `Do {animal_name} {animal_activity}?`
  * **Variable replacements** :

`animal_name` replacements | `animal_activity` replacements  
---|---  
Coyotes | eat berries  
Eagles | swim  
Squirrels | dig holes  



## Limitations

  * System instructions are not supported as a replaceable variable in prompt templates.
  * Prompt templates don't support multimodal prompts.



## What's next

  * Start prompting in the [Vertex AI Studio](https://console.cloud.google.com/agent-platform/studio/multimodal;mode=prompt).
  * Learn more about [prompting strategies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies).
  * Learn about [responsible AI best practices and Agent Platform's safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
