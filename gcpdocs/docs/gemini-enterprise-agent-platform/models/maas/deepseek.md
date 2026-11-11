---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/deepseek/
title: DeepSeek models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:51:20.376225+00:00
---

# DeepSeek models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/deepseek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  DeepSeek models Stay organized with collections  Save and categorize content based on your preferences. 

DeepSeek models are available for use as managed APIs and self-deployed models on Gemini Enterprise Agent Platform. You can stream your responses to reduce the end-user latency perception. A streamed response uses _server-sent events_ (SSE) to incrementally stream the response.

## Managed DeepSeek models

**Note:** DeepSeek models are not Google products, and their availability in Gemini Enterprise Agent Platform is subject to the terms for "Separate Offerings" in the AI/ML Services section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms), and separate terms found in the relevant model card.

DeepSeek models offer fully managed and serverless models as APIs. To use a DeepSeek model on Agent Platform, send a request directly to the Agent Platform API endpoint. When using DeepSeek models as a managed API, there's no need to provision or manage infrastructure.

The following models are available from DeepSeek to use in Gemini Enterprise Agent Platform. To access a DeepSeek model, go to its Model Garden model card.

### DeepSeek-V4.1-Flash

DeepSeek-V4.1-Flash is a multimodal Mixture-of-Experts (MoE) model from DeepSeek built for agentic and coding tasks. It accepts text and image input and has a context window of up to 1M tokens. 

[ Go to the DeepSeek-V4.1-Flash model card ](https://console.cloud.google.com/agent-platform/publishers/deepseek-ai/model-garden/deepseek-v4.1-flash-maas)

## Use DeepSeek models

For managed models, you can use curl commands to send requests to the Gemini Enterprise Agent Platform endpoint using the following model names: 

  * For DeepSeek-V4.1-Flash, use `deepseek-v4.1-flash-maas`



To learn how to make streaming and non-streaming calls to DeepSeek models, see [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

To use a self-deployed Gemini Enterprise Agent Platform model:

  1. Navigate to the [Model Garden console](https://console.cloud.google.com/agent-platform/model-garden).
  2. Find the relevant Gemini Enterprise Agent Platform model.
  3. Click **Enable** and complete the provided form to get the necessary commercial use licenses.



For more information about deploying and using partner models, see [ Deploy a partner model and make prediction requests ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests). 

## DeepSeek model region availability

DeepSeek models are available in the following regions: 

Model | Regions  
---|---  
DeepSeek-V4.1-Flash | 

  * `global`

  
  
## What's next

Learn how to [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
