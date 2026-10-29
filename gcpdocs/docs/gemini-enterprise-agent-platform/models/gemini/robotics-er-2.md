---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/robotics-er-2/
title: Gemini Robotics ER 2 \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:41.940665+00:00
---

# Gemini Robotics ER 2  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/robotics-er-2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini Robotics ER 2 Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is a Generative AI Preview offering, subject to the "Pre-GA Offerings Terms" of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1) and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/terms/genai-preview-products). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

For this Generative AI Preview offering, Customers may elect to use it for production or commercial purposes, or disclose Generated Output to third-parties, and may process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. 

Gemini Robotics ER 2 (`gemini-robotics-er-2-preview`) is a _vision-language model_ (VLM) available on Gemini Enterprise Agent Platform that delivers precise reasoning about a robot's physical environment. Built on Gemini 3.5 Flash, it specializes in embodied reasoning capabilities such as spatial reasoning, pointing, instrument reading, robot video understanding (including moment finding and progress classification), and multi-step robot and tool orchestration.

For setup instructions, code samples, and capability guides, see the [Gemini Robotics ER 2 overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/gemini-robotics-er).

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/multimodal?mode=prompt&model=gemini-robotics-er-2-preview) [View in Model Garden](https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-robotics-er-2-preview-info) [Deploy example app](https://console.cloud.google.com/agent-platform/studio/multimodal?mode=prompt&model=gemini-robotics-er-2-preview&deploy=true) [Developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/gemini-robotics-er) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#gemini-robotics)

Note: "Deploy example app" requires a Google Cloud project with billing and Agent Platform API enabled.Model ID | `gemini-robotics-er-2-preview`  
---|---  
Modalities |  description  Text   
Input and output  photo  Image   
Input only  mic  Audio   
Input only  videocam  Video   
Input only   
Token limits | Input token limit | 131,072  
Output token limit | 65,536  
Capabilities | 

  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)   
Supported
  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)   
Supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Supported
  * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)   
Implicit context caching, explicit context caching  
Supported
  * [RAG Engine ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)   
Not supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models)   
Not supported
  * [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)   
Not supported

  
Tools | 

  * [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)   
Google Search, Google Maps  
Supported
  * [Code execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/code-execution)   
Supported
  * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling)   
Supported
  * [URL context](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/url-context)   
Supported
  * [Computer use](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computer-use) previewPreview feature  
Supported

  
APIs | 

  * [GenerateContent API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference)   
Supported
  * [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions) previewPreview feature  
Not supported
  * [Gemini Live API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api)   
Not supported
  * [Count Tokens API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/get-token-count)   
Supported
  * [Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/overview)   
Not supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Not supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Not supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Standard PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`

  
**[Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) ** | 

  * Global: `global`

  
Quota limits |  250 requests per minute (RPM) default per project (200 to 300 RPM depending on project quota tier)   
Versions | 

  * `gemini-robotics-er-2-preview`
    * Launch stage: Preview
    * Release date: October 27, 2026

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
