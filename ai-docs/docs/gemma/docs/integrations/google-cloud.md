---
url: https://ai.google.dev/gemma/docs/integrations/google-cloud/
title: Deploy Gemma with Google Cloud \u00a0|\u00a0 Google AI for Developers
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-15T19:19:16.694240+00:00
---

# Deploy Gemma with Google Cloud  |  Google AI for Developers

> Source: https://ai.google.dev/gemma/docs/integrations/google-cloud/

[ Skip to main content ](https://ai.google.dev/gemma/docs/integrations/google-cloud/#main-content)
[ ![Google AI for Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/googledevai/images/lockup-new.svg) ](https://ai.google.dev/)
`/`
  * [English](https://ai.google.dev/gemma/docs/integrations/google-cloud/)
  * [Deutsch](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=de)
  * [Español – América Latina](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=es-419)
  * [Français](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=fr)
  * [Indonesia](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=id)
  * [Italiano](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=it)
  * [Polski](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=pl)
  * [Português – Brasil](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=pt-br)
  * [Shqip](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=sq)
  * [Tiếng Việt](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=vi)
  * [Türkçe](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=tr)
  * [Русский](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=ru)
  * [עברית](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=he)
  * [العربيّة](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=ar)
  * [فارسی](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=fa)
  * [हिंदी](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=hi)
  * [বাংলা](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=bn)
  * [ภาษาไทย](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=th)
  * [中文 – 简体](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=zh-cn)
  * [中文 – 繁體](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=zh-tw)
  * [日本語](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=ja)
  * [한국어](https://ai.google.dev/gemma/docs/integrations/google-cloud/?hl=ko)

Sign in
  * [ Gemma ](https://ai.google.dev/gemma)


  * On this page
  * [Gemini Enterprise Agent Platform](https://ai.google.dev/gemma/docs/integrations/google-cloud/#model-garden)
  * [Cloud Run](https://ai.google.dev/gemma/docs/integrations/google-cloud/#cloud-run)
  * [Google Kubernetes Engine (GKE)](https://ai.google.dev/gemma/docs/integrations/google-cloud/#gke)
  * [Agent Development Kit (ADK)](https://ai.google.dev/gemma/docs/integrations/google-cloud/#adk)
  * [Gemini Enterprise Agent Platform Training Clusters](https://ai.google.dev/gemma/docs/integrations/google-cloud/#training-clusters)
  * [vLLM with TPUs](https://ai.google.dev/gemma/docs/integrations/google-cloud/#vllm-tpu)
  * [MaxText](https://ai.google.dev/gemma/docs/integrations/google-cloud/#maxtext)
  * [Sovereign Cloud](https://ai.google.dev/gemma/docs/integrations/google-cloud/#sovereign-cloud)


**Gemma 4** released with text, audio and image input and long up to 256K context window! [**Learn more**](https://ai.google.dev/gemma/docs/core)
  * [ Home ](https://ai.google.dev/)
  * [ Gemma ](https://ai.google.dev/gemma)
  * [ Models ](https://deepmind.google/models/gemma)
  * [ Docs ](https://ai.google.dev/gemma/docs)


Send feedback 
#  Deploy Gemma with Google Cloud
  * On this page
  * [Gemini Enterprise Agent Platform](https://ai.google.dev/gemma/docs/integrations/google-cloud/#model-garden)
  * [Cloud Run](https://ai.google.dev/gemma/docs/integrations/google-cloud/#cloud-run)
  * [Google Kubernetes Engine (GKE)](https://ai.google.dev/gemma/docs/integrations/google-cloud/#gke)
  * [Agent Development Kit (ADK)](https://ai.google.dev/gemma/docs/integrations/google-cloud/#adk)
  * [Gemini Enterprise Agent Platform Training Clusters](https://ai.google.dev/gemma/docs/integrations/google-cloud/#training-clusters)
  * [vLLM with TPUs](https://ai.google.dev/gemma/docs/integrations/google-cloud/#vllm-tpu)
  * [MaxText](https://ai.google.dev/gemma/docs/integrations/google-cloud/#maxtext)
  * [Sovereign Cloud](https://ai.google.dev/gemma/docs/integrations/google-cloud/#sovereign-cloud)


The Google Cloud platform provides many options for deploying, serving, and fine-tuning Gemma 4 open models, including the following:
  * [Gemini Enterprise Agent Platform](https://ai.google.dev/gemma/docs/integrations/google-cloud/#model-garden)
  * [Cloud Run](https://ai.google.dev/gemma/docs/integrations/google-cloud/#cloud-run)
  * [Google Kubernetes Engine (GKE)](https://ai.google.dev/gemma/docs/integrations/google-cloud/#gke)
  * [Agent Development Kit (ADK)](https://ai.google.dev/gemma/docs/integrations/google-cloud/#adk)
  * [Gemini Enterprise Agent Platform Training Clusters](https://ai.google.dev/gemma/docs/integrations/google-cloud/#training-clusters)
  * [MaxText](https://ai.google.dev/gemma/docs/integrations/google-cloud/#maxtext)
  * [vLLM with TPUs](https://ai.google.dev/gemma/docs/integrations/google-cloud/#vllm-tpu)
  * [Sovereign Cloud](https://ai.google.dev/gemma/docs/integrations/google-cloud/#sovereign-cloud)


## Gemini Enterprise Agent Platform
[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-gemma) is a Google Cloud platform for rapidly building and scaling machine learning projects. Gemma 4 is available in [Model Garden](https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemma4), a curated collection of models on Gemini Enterprise Agent Platform. You can test and deploy models directly from the console.
To learn more, refer to the following pages:
  * [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): Get started with Gemini Enterprise Agent Platform.
  * [Gemma with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-gemma): Use Gemma open models with Gemini Enterprise Agent Platform.


## Cloud Run
[Cloud Run](https://cloud.google.com/run) is a fully managed platform to run your code or containers on top of Google's highly scalable infrastructure. [Deploy Gemma 4 on Cloud Run](https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run) using GPUs for scale-to-zero, pay-per-use inference.
For larger mode sizes, [leverage advanced configurations](https://codelabs.developers.google.com/codelabs/cloud-run/cloud-run-gpu-rtx-pro-6000-gemma4-vllm) with RTX 6000 Pro GPUs and Model Streaming.
## Google Kubernetes Engine (GKE)
[Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE) is a managed Kubernetes service from Google Cloud. [Run Gemma 4 on GKE](https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm) for enterprise-grade container orchestration. Use TPUs and GPUs to serve models with high throughput and low latency.
## Agent Development Kit (ADK)
Build and orchestrate AI agents with Gemma 4 and the [Agent Development Kit (ADK)](https://adk.dev/agents/models/google-gemma/). Gemma 4's strong reasoning and function-calling capabilities make it ideal for agentic workflows.
## Gemini Enterprise Agent Platform Training Clusters
[Fine-tune Gemma 4 using Gemini Enterprise Agent Platform Training Clusters](https://discuss.google.dev/t/end-to-end-guide-fine-tuning-and-serving-gemma-4-on-vertex-ai/345865). Training Clusters provides optimized infrastructure for large-scale training and fine-tuning of open models.
## vLLM with TPUs
[Serve Gemma 4 on Google Cloud TPUs](https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#cloud-tpu-deployment-via-docker) for state-of-the-art serving performance.
## MaxText
Gemma 4 is supported in [MaxText](https://github.com/google/maxtext), a high-performance, arbitrary-sized JAX LLM implementation for Google Cloud TPUs.
## Sovereign Cloud
Gemma 4 is available on [Sovereign Cloud](https://cloud.google.com/sovereign-cloud) solutions, providing enhanced control and compliance for sensitive workloads.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-07-02 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-02 UTC."],[],[]] 
