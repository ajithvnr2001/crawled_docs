---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/meta/muse-wonder-1-0/
title: Muse Wonder \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:56:32.116595+00:00
---

# Muse Wonder  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/meta/muse-wonder-1-0/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Muse Wonder Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Muse Wonder from Meta is a high-capability reasoning model built for complex software engineering and long-horizon agentic work. In multi-step coding, autonomous agent, and computer-use workflows, it plans tasks, delegates to sub-agents, calls tools in parallel, and recovers from errors. It accepts text, image, and PDF inputs with a 1M-token context window.

Requests on the global `/locations/global/publishers/meta/v1/responses` endpoint pass the bare model ID `muse-wonder-1.0` in the `model` field. For an example request, see [Use Meta models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/meta#use-meta-models).

Model ID | `meta/muse-wonder-1.0`  
---|---  
Launch stage | Preview  
Supported inputs & outputs | 

  * Inputs: Text, Image, PDF
  * Outputs: Text

  
Token limits | 

  * Maximum input tokens: 1,048,576

  
Capabilities | 

  * Supported
    * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/meta#use-meta-models) previewPreview feature
    * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/meta#use-meta-models) previewPreview feature
    * [Reasoning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/meta#use-meta-models) previewPreview feature
  * Not supported
    * [Batch predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/batch-prediction) previewPreview feature

  
Usage types | 

  * Supported
    * [Standard pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) previewPreview feature
    * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas) previewPreview feature
  * Not supported
    * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput) previewPreview feature

  
Versions | 

  * `meta/muse-wonder-1.0`
    * **Launch stage:** Preview
    * **Release date:** November 9, 2026

  
Supported regions  
Model availability | 

  * Global
    * `global endpoint`

  
Quota limits |  global endpoint: 

  * Context length: 1,048,576

  
Pricing | See [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
