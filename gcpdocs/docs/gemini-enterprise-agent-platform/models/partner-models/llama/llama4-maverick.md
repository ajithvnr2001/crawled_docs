---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/llama4-maverick/
title: Llama 4 Maverick 17B-128E \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:34:01.780230+00:00
---

# Llama 4 Maverick 17B-128E  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/llama4-maverick/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Llama 4 Maverick 17B-128E Stay organized with collections  Save and categorize content based on your preferences. 

Llama 4 Maverick 17B-128E is the largest Llama 4 model and offers coding, reasoning, and image capabilities. It features Mixture-of-Experts (MoE) architecture with 17 billion active parameters out of 400 billion total parameters and 128 experts. Llama 4 Maverick 17B-128E uses alternating dense and MoE layers, where each token activates a shared expert plus one of the 128 routed experts. The model is pretrained on 200 languages and optimized for high-quality chat interactions through a refined post-training pipeline.

Llama 4 Maverick 17B-128E is multimodal and is suited for image captioning, visual analysis, visual questions and answers, creative text generation, general-purpose AI assistants, and complex chat applications.

## Managed API (MaaS) specifications

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/generative/multimodal/create/text?model=llama-4-maverick-17b-128e-instruct-maas) [View model card in Model Garden](https://console.cloud.google.com/agent-platform/publishers/meta/model-garden/llama-4-maverick-17b-128e-instruct-maas)

Model ID | `llama-4-maverick-17b-128e-instruct-maas`  
---|---  
Launch stage | GA  
Supported inputs & outputs | 

  * Inputs: Text, Code, Images
  * Outputs: Text

  
Capabilities | 

  * Supported
    * [Batch predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/batch-prediction)
    * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/function-calling)
    * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/structured-output)
  * Not supported
    * [Llama Guard](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama)

  
Usage types | 

  * Supported
    * [Standard pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo)
    * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)
  * Not supported
    * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)

  
Knowledge cutoff date | August 2024  
Versions | 

  * `llama-4-maverick-17b-128e-instruct-maas`
    * **Launch stage:** GA
    * **Release date:** April 29, 2025

  
Supported regions  
Model availability | 

  * United States
    * `us-east5`

  
ML processing | 

  * United States
    * `Multi-region`

  
Quota limits |  us-east5: 

  * Max output: 8,192
  * Context length: 524,288

  
Pricing | See [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).  
  
## Deploy as a self-deployed model

To self-deploy the model, navigate to the [Llama 4 Maverick 17B-128E model card](https://console.cloud.google.com/agent-platform/publishers/meta/model-garden/llama4) in the Model Garden console and click **Deploy model**. When you self-deploy from Model Garden, you can select from the following model variants:

  * `llama-4-maverick-17b-128e`: Pretrained model.

  * `llama-4-maverick-17b-128e-instruct`: Instruction-tuned model in BF16 precision.

  * `llama-4-maverick-17b-128e-instruct-fp8`: Instruction-tuned model with FP8 quantization.




For more information about deploying and using partner models, see [Deploy a partner model and make prediction requests](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests).

## Considerations

Keep the following considerations in mind when using Llama 4 Maverick 17B-128E:

  * The managed MaaS endpoint (`llama-4-maverick-17b-128e-instruct-maas`) serves the instruction-tuned model in fixed FP8 precision. You can't change the quantization format on the managed endpoint; to deploy the BF16 or pretrained variant, self-deploy the model from Model Garden.

  * You can include a maximum of three images per request.

  * The MaaS endpoint doesn't use Llama Guard, unlike earlier Llama versions. To use Llama Guard, deploy Llama Guard from Model Garden and then send the prompts and responses to that endpoint. Compared to Llama 4, Llama Guard has a smaller context window (128,000 tokens) and only accepts requests with a single image at the beginning of the prompt.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
