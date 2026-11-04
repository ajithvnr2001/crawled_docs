---
url: https://www.sarvam.ai/token-factory/
title: Sarvam Token Factory | Open models, Indian inference
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:06.043154+00:00
---

# Sarvam Token Factory | Open models, Indian inference

> Source: https://www.sarvam.ai/token-factory/

![Sarvam Motif](https://assets.sarvam.ai/assets/motifs/ui/motif.svg)

# Frontier open models.   
Served with speed, scale and privacy.

Run leading open models on Sarvam’s GPUs in India, with shared or dedicated capacity and zero data retention available on request.

[Get Started](https://indus.sarvam.ai/model-catalogue#:~:text=Try%20model-,LLM,-Sarvam%20105B)[Explore models](https://www.sarvam.ai/token-factory/models)

## Inference that scales with demand

Sarvam runs the serving infrastructure behind your applications so capacity, reliability and integration stay out of your way.

###  Meet changing demand 

Serving capacity scales automatically with your traffic, with dedicated GPUs ready for sustained volume. 

5%  50%  100% 100%

###  Keep production running 

Active fleet monitoring and staged rollouts catch faults early and roll back changes before they hit traffic. 

_client.py_

+from sarvamai import SarvamAI 

+client.chat.completions_v2(...) 

![](https://www.sarvam.ai/assets/token-factory/logos/zai.svg) ![](https://www.sarvam.ai/assets/token-factory/logos/deepseek.svg) ![](https://www.sarvam.ai/assets/token-factory/logos/gemma.svg) ![](https://www.sarvam.ai/assets/brand/sarvam_logo_pack/logomark-dark.svg)

###  Fit your existing tools 

Use your existing tools and frameworks, and switch between models with minimal changes to your application. 

## Speed and reliability   
on one serving fleet.

Speed  Reliability 

Speed

###  Faster inference at every stage of the response. 

Earlier first tokens and faster generation mean less waiting inside your application. 

MetricOutput speed

Output speedTime to first token

![](https://assets.sarvam.ai/assets/token-factory/logos/zai.svg)GLM 5.3![](https://assets.sarvam.ai/assets/token-factory/logos/deepseek.svg)DeepSeek V4.1 Flash 1017![](https://assets.sarvam.ai/assets/token-factory/logos/google.svg)Gemma 4 31B

****

#### 

[Explore models](https://www.sarvam.ai/token-factory/models)

Reliability

###  Reliability backed by an SLA 

Keep critical applications available with 99.95% uptime guaranteed by an SLA. 

SLA-backed

**99.95%**

####  Uptime guaranteed 

Backed by contractual uptime commitments for enterprise deployments. 

[Discuss your SLA](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)

  * ####  SLA-driven scaling 

Workers scale automatically to hold your latency targets. 

  * ####  Continuous monitoring 

Active health checks detect and isolate faults across the fleet. 

  * ####  Staged upgrades 

Rollouts happen in stages with automated checks and instant rollback. 




## Built for real-world workloads

From multi-step code edits to live voice streams, run every workload on one API.

Agent 

router.ts

Tests passed 

###  Coding agents 

Read repo context, reason through bugs and run tools to ship working patches. 

crm.update() 

###  Tool-calling agents 

Connect models to your APIs and business systems with structured JSON outputs. 

1M-token window

###  Million-token context 

Pass whole documents, instructions and chat history together in a 1M-token window. 

###  Document vision 

Read pages, tables and charts alongside text to pull out structured data. 

reasoning_effort

low  high  max 

###  Multi-step reasoning 

Tackle complex analysis and planning with adjustable reasoning effort. 

###  Real-time streaming 

Stream tokens straight into chat UIs and voice pipelines as they generate. 

## Leading models. Ready to use

Explore models for reasoning, coding, vision and Indian languages.

[Compare pricing](https://www.sarvam.ai/token-factory/calculator)[Open model catalogue](https://www.sarvam.ai/token-factory/models)

  * ### [GLM 5.3
    * Z.ai
    * Reasoning and coding
    * 1M context
![](https://assets.sarvam.ai/assets/token-factory/logos/zai.svg)Large-scale reasoning model built for complex software engineering and long-horizon agent tasks.](https://www.sarvam.ai/token-factory/models/glm-5-3)
  * ### [GLM 5.3 Flash
    * Z.ai
    * Reasoning and coding
    * 1M context
![](https://assets.sarvam.ai/assets/token-factory/logos/zai.svg)Faster open-weight reasoning model for agents and image understanding.](https://www.sarvam.ai/token-factory/models/glm-5-3-flash)
  * ### [DeepSeek V4.1 Flash 1017
    * DeepSeek
    * Reasoning and coding
    * 1M context
![](https://assets.sarvam.ai/assets/token-factory/logos/deepseek.svg)General-purpose open-weight model for long-document analysis and agentic workflows.](https://www.sarvam.ai/token-factory/models/deepseek-v4-1-flash-1017)
  * ### [Gemma 4 31B
    * Google DeepMind
    * Vision
    * 256K context
![](https://assets.sarvam.ai/assets/token-factory/logos/google.svg)31B-parameter instruction-tuned model for text and image understanding, with tool calling and optional reasoning.](https://www.sarvam.ai/token-factory/models/gemma-4-31b)
  * ### [Sarvam 105B
    * Sarvam
    * Indian languages
    * 128K context
![](https://assets.sarvam.ai/assets/brand/sarvam_logo_pack/logomark-dark.svg)Flagship 105B Mixture-of-Experts model trained from scratch for Indian-language understanding, complex reasoning, coding and agentic workflows.](https://www.sarvam.ai/token-factory/models/sarvam-105b)
  * ### [Sarvam 105B Conversations
    * Sarvam
    * Indian languages
    * 32K context
![](https://assets.sarvam.ai/assets/brand/sarvam_logo_pack/logomark-dark.svg)Post-trained variant of Sarvam 105B for real-time dialogue, voice agents and multi-turn conversations across Indian languages.](https://www.sarvam.ai/token-factory/models/sarvam-105b-chat)



[Explore the API documentation](https://docs.sarvam.ai/api/token-factory/models)

Show all models 

## Serverless inference. Ready to scale

Run leading models through an OpenAI-compatible API. Sarvam manages the serving infrastructure in India.

GLM-5.3GLM-5.3 FlashGemma 4 31BDeepSeek V4.1 Flash 1017DeepSeek V4 Pro (beta)Kimi K3 (beta)MiMo V2.6 Flash (beta)MiMo V2.6 Pro (beta)

Python

JavaScriptcURL

$`pip install --upgrade sarvamai`V2 · Sarvam SDK · Streaming
    
    
    import osfrom sarvamai import SarvamAI​client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])​stream = client.chat.completions_v2(    model="glm5.3",    messages=[{"role": "user", "content": "Explain serverless inference briefly."}],    max_tokens=8000,    stream=True,)​for chunk in stream:    if not chunk.choices:        continue    text = chunk.choices[0].delta.content    if text:        print(text, end="", flush=True)

V2 Chat Completions. Max reasoning is the default. Reasoning tokens count toward the 8,000-token output budget.

### From first request to production traffic

Access supported models on Sarvam’s GPUs in India, with serving capacity that adapts to your traffic.

  * Model evaluation and prototyping
  * Production applications
  * Variable or unpredictable traffic



[Start building](https://indus.sarvam.ai/token-factory/home)[Read the API guide](https://docs.sarvam.ai/api/token-factory/models)

## Enterprise-grade security.   
Compliance and privacy built in.

  *   * 


### Independently audited

ISO 27001:2022 certified and SOC 2 Type I attested by independent assessors for information security and operational controls.

### Your inference stays in India

Prompts run on Sarvam GPUs in India and are never sent to overseas model providers.

Your prompt

Sarvam GPUs · India

Never to overseas

Your prompt Sarvam GPUs · India Never to overseas

### Enterprise-grade security

Every request is encrypted, isolated to your account and scoped to your team.

  * Encrypted in transit and at rest
  * Workloads isolated by account
  * Role-based access for keys and teams



### Privacy on your terms

Enable zero data retention on request, and set clear rules for logs.

  * Prompts and responses Zero retention Never stored or used to train models On request
  * Operational logs Custom retention



## Questions before you go live

Answers for teams evaluating models, moving applications and planning production.

[Discuss your requirements](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)

### Can we move an existing AI application to Sarvam?

Sarvam supports OpenAI-compatible Chat Completions and Responses APIs. Update your endpoint, key and model, then validate the parameters, tool calls and outputs your application uses. [Read the API guide](https://docs.sarvam.ai/api/token-factory/models)

### How do we know a model will meet our quality requirements?

Leading open models perform competitively on coding, reasoning and other published evaluations. The right choice depends on your workload. Validate answer quality, tool use and response times on representative requests. Compare published scores on [Artificial Analysis](https://artificialanalysis.ai/models).

### Where is our inference processed?

Model inference runs on Sarvam-operated GPUs in India. Sarvam hosts the weights; requests are not forwarded to the original model developer’s overseas API. External tools connected by your application have their own processing locations and data policies.

### What does zero data retention cover?

Zero data retention is available on request. Under an agreed ZDR arrangement, prompts and responses are not retained. Operational logs are scoped separately in the terms for your deployment.

### Is our data used to train models for other customers?

No. Sarvam does not use customer data to train models for other customers. The original model developer does not receive your inference requests. Your data-processing agreement defines the permitted use and handling of your data.

### How will Sarvam handle our traffic and latency targets?

Sarvam manages serving capacity as traffic changes. Share your expected concurrency, prompt lengths, peak traffic and response-time targets so the team can size the deployment. Available capacity and rate limits depend on your model, deployment and account.

### Can we switch models as our needs change?

Yes. Select supported models through the API’s model field. Context limits, input types and tool behaviour vary, so validate your application when changing models. You can use all models listed in the catalogue with a single API key by changing the model name.

### What production support and SLAs are available?

Sarvam’s engineers can support evaluation, integration and migration. For production, discuss the capacity plan, availability targets, support response times and escalation process with the team. Service commitments are agreed for your enterprise deployment. [Discuss SLA](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)

### What can we share with our security and procurement teams?

Request Sarvam’s ISO 27001:2022 certificate, SOC 2 Type I report, penetration-test summary and data-processing documentation through the Trust Center. Some documents are shared under NDA. Your security team can review their scope against the planned deployment. [Visit the Trust Center](https://www.sarvam.ai/trust-center)

Test it on your own traffic. Our engineers help you compare quality, speed and cost before you move. 

Test it on your own traffic.

Our engineers help you compare quality, speed and cost before you move.

[Talk to our team](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)[Read the docs](https://docs.sarvam.ai/api/token-factory/models)
