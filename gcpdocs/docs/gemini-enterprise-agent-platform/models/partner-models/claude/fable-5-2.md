---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/fable-5-2/
title: Anthropic's Claude Fable 5.2 on Google Cloud \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:35:31.568117+00:00
---

# Anthropic's Claude Fable 5.2 on Google Cloud  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/fable-5-2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Anthropic's Claude Fable 5.2 on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Anthropic's Claude Fable 5.2 on Google Cloud is designed for technical and scientific work, including coding and finance. It can work on ambiguous problems over long periods, verify its own work, and orchestrate subagents.

**Advanced AI Safety Notice:** Anthropic's Claude Fable 5.2 on Google Cloud is within the scope of the [Advanced AI Safety Addendum](https://cloud.google.com/terms/advanced-ai-safety-addendum). All prompts and responses are stored for up to 30 days for the sole purpose of monitoring for potential abuse of relevant terms of service. See [Responsible AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai) and [Abuse Monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring#advanced-ai-safety) to learn more. 

**Retirement date:** No sooner than November 9, 2027.

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-fable-5-2) [View model card in Model Garden](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-fable-5-2)

Model ID | `claude-fable-5-2`  
---|---  
Launch stage | GA  
Supported inputs & outputs | 

  * Inputs: Text, Image, PDF
  * Outputs: Text

  
Token limits | 

  * Maximum input tokens: 1,000,000
  * Maximum output tokens: 128,000

  
Capabilities | 

  * Supported
    * [Fast mode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/fast-mode)
    * [Computer use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
    * [Web search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/web-search)
    * [Batch predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/batch)
    * [Prompt caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/prompt-caching)
    * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/use-claude#tool_use_function_calling)
    * [Count tokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/count-tokens)
    * [Memory tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/memory-tool)
  * Not supported

  
Usage types | 

  * Supported
    * [Shared Model Lineage Quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas)
    * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)
  * Not supported

  
Technical specifications  
Images | 

  * **Limitation and specifications:** See [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision) in Anthropic's documentation

  
Documents | 

  * **Limitation and specifications:** See [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support) in Anthropic's documentation

  
Versions | 

  * `claude-fable-5-2`
    * **Launch stage:** Generally available
    * **Release date:** November 9, 2026
    * **Retirement date not sooner than:** November 9, 2027

  
Supported regions  
Model availability (Includes fixed quota & Provisioned Throughput) | 

  * United States
    * `us (US multi-region)`
  * Europe
    * `eu (Europe multi-region)`
  * Global
    * `global (global endpoint)`

  
ML processing | 

  * United States
    * `Multi-region`
  * Europe
    * `Multi-region`

  
Quota limits |  us (US multi-region): 

  * QPM: Granted upon model enablement ([Shared lineage quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas#shared-lineage-quotas))
  * TPM: Granted upon model enablement ([Shared lineage quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas#shared-lineage-quotas))
  * Context length: 1,000,000

eu (Europe multi-region): 

  * QPM: Granted upon model enablement ([Shared lineage quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas#shared-lineage-quotas))
  * TPM: Granted upon model enablement ([Shared lineage quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas#shared-lineage-quotas))
  * Context length: 1,000,000

global (global endpoint): 

  * QPM: Granted upon model enablement ([Shared lineage quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas#shared-lineage-quotas))
  * TPM: Granted upon model enablement ([Shared lineage quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas#shared-lineage-quotas))
  * Context length: 1,000,000

  
Pricing | See [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).  
  
## Fast mode

Anthropic's Claude Fable 5.2 on Google Cloud supports [fast mode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/fast-mode) to accelerate output token generation for latency-sensitive, interactive workloads. Set `"speed": "fast"` in online prediction requests to `claude-fable-5-2`:

  * **Pricing** : Fast mode is priced at **2x the standard-speed token rates** across all token types (input, output, 5-minute and 1-hour cache write, and cache hit tokens). [Web search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/web-search) tool calls are billed at the standard rate. See the [Agent Platform pricing page](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#partner-models).
  * **Quotas** : On global and multi-region endpoints, fast mode requests draw from a dedicated `anthropic-claude-fable-fast` [shared lineage quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas#shared-lineage-quotas) bucket separate from standard `anthropic-claude-fable` quota.
  * **No Provisioned Throughput** : Fast mode doesn't support [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput). Fast mode requests always use [pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo), and fast mode requests sent with the `X-Vertex-AI-LLM-Request-Type: dedicated` header are throttled with an `HTTP 429` (`RESOURCE_EXHAUSTED`) error.



For code samples, monitoring, and limitations, see [Fast mode with Anthropic Claude models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/fast-mode).

## Enable Anthropic's Claude Fable 5.2 on Google Cloud in your project

Follow these steps to enable Anthropic's Claude Fable 5.2 on Google Cloud in your project:

  * Consent to the [Advanced AI Safety Addendum](https://cloud.google.com/terms/advanced-ai-safety-addendum) in Model Garden (required once per project). See [Abuse Monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring#advanced-ai-safety) to learn more.
  * For online terms customers, click **Enable** on the [Model Garden model card](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-fable-5-2) to: 
    * Answer relevant company and use case questions in Model Garden.
    * Accept Anthropic and Marketplace terms of service in Cloud Marketplace.
  * For Private Offer customers: 
    * [Accept the Private Offer in Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/offers/accepting-private-offer) (required once per Billing Account).
    * Enable the model location using the `enableModel` API.
  * As required by Section F of Anthropic's [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms), enable prompt-response sharing with Anthropic for each model location. See [Request-Response Logging and Sharing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/request-response-logging#share-requests-responses-with-maas-partners) to learn more.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
