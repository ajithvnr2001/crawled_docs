---
url: https://www.sarvam.ai/token-factory/models/sarvam-105b/
title: Sarvam 105B | Sarvam Token Factory
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:08.988067+00:00
---

# Sarvam 105B | Sarvam Token Factory

> Source: https://www.sarvam.ai/token-factory/models/sarvam-105b/

[ Token Factory ](https://www.sarvam.ai/token-factory) / [ Models ](https://www.sarvam.ai/token-factory/models) / Sarvam 105B

[ ![](https://assets.sarvam.ai/assets/brand/sarvam_logo_pack/logomark-dark.svg)Sarvam ](https://www.sarvam.ai/token-factory/models)

# Sarvam 105B

Build applications that work across native-script, romanised and code-mixed text, with a 128K context window and hybrid reasoning.

  * Indian languages 
  * Reasoning 
  * Coding 
  * Tool calling 



[Try in playground](https://indus.sarvam.ai/api-playground/chat-completions?model=sarvam-105b)[View API reference](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)

## Token pricing

[ Compare all model pricing ](https://www.sarvam.ai/token-factory/pricing)

Input
    Tokens sent to the model.

₹15.00 per 1M tokens

Cached input
    Eligible tokens reused from a cached prefix.

₹5.00 per 1M tokens

Output
    Generated tokens, including reasoning.

₹60.00 per 1M tokens

Excluding GST

API model ID  ` sarvam-105b `

Provider 
     [ Sarvam ](https://www.sarvam.ai/token-factory/models)

Context window 
     128K tokens 

Input types 
     Text 

Response style 
     Hybrid reasoning 

Deployment 
     Serverless · India 

## Best suited for

  1. 01 

###  Multilingual business workflows 

Process instructions and business content across Indian languages, English and code-mixed conversations. 

  2. 02 

###  Language-aware agents 

Connect multilingual reasoning to your application tools for workflows that require structured actions. 

  3. 03 

###  Flexible reasoning depth 

Use hybrid reasoning to match the depth of analysis to the task, from direct responses to more involved problem solving. 




## Benchmarks

Artificial Analysis does not currently publish quality scores for Sarvam 105B.

### The Sarvam 105B comparison page has no Intelligence Index result.

The page compares Sarvam 105B (High) with GPT-5.4 Pro (Xhigh) on price, speed and context. It does not include an Intelligence Index or exam score.

[ See GLM 5.3 benchmarks ](https://www.sarvam.ai/token-factory/models/glm-5-3#benchmarks)

Build with the Sarvam SDK

PythonJavaScriptcURL

Copy

$`pip install --upgrade sarvamai`V2 · Sarvam SDK · Streaming
    
    
    import osfrom sarvamai import SarvamAI​client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])​stream = client.chat.completions_v2(    model="sarvam-105b",    messages=[{"role": "user", "content": "Explain how solar panels work in Hindi briefly."}],    max_tokens=8000,    reasoning_effort="low",    stream=True,)​for chunk in stream:    if not chunk.choices:        continue    text = chunk.choices[0].delta.content    if text:        print(text, end="", flush=True)

  1. 01 **Install the Sarvam SDK**

Install `sarvamai` for Python or JavaScript. Store your key in `SARVAM_API_KEY`.

  2. 02 **Choose your model**

Use model ID `sarvam-105b`. The SDK calls `https://api.sarvam.ai/v2` for this example.

V2 Chat Completions. Low reasoning effort is selected for this example. Reasoning and answer tokens share the 8,000-token output budget.

  3. 03 **Validate your application**

Check output quality, supported parameters and tool behaviour on representative requests before moving production traffic.


[ Model API Reference ](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)

##  Frequently Asked  
Questions 

### What is Sarvam 105B?

Sarvam 105B is Sarvam’s flagship model for reasoning, coding and agentic tasks. It supports English and Indian-language applications, with a 128K context window and hybrid reasoning.

### Which language formats does it support?

It supports native-script, romanised and code-mixed Indian-language text alongside English. Evaluate the languages, scripts and domain terminology used by your customers rather than relying only on general-purpose benchmark scores.

### How is it different from Sarvam 105B Chat?

The flagship variant is designed for complex reasoning and agentic tasks with 128K context. Sarvam 105B Chat is tuned for real-time dialogue and voice-agent conversations with a smaller 32K context window.

### How much context is available to an application?

The model has a 128K-token context window. Conversation history, instructions and generated output must fit within the request’s available context allowance.

### Can it power agents and stream responses?

Yes. It supports tool calling for agent workflows and streaming for incremental responses. Your application defines the tools, validates arguments and executes the requested actions.

### Which model ID and endpoint should I use?

Install the Sarvam SDK, set your API key and use model ID sarvam-105b with v2 Chat Completions. Validate parameters, tool calls and outputs before moving production traffic.

### How is Sarvam 105B priced?

The rates per million tokens are ₹15.00 for input, ₹5.00 for eligible cached input and ₹60.00 for output, excluding GST. Reasoning tokens are billed at the output rate.

### Where does inference run, and what SLA is available?

Inference runs on Sarvam-operated GPUs in India. Token Factory guarantees 99.95% uptime, backed by an SLA. Discuss your traffic, latency targets and support requirements with the Sarvam team. [Discuss SLA](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)

## Explore other models

[ View catalogue ](https://www.sarvam.ai/token-factory/models)

### [GLM 5.3

  * Z.ai
  * Reasoning and coding
  * 1M context

![](https://assets.sarvam.ai/assets/token-factory/logos/zai.svg)Large-scale reasoning model built for complex software engineering and long-horizon agent tasks.](https://www.sarvam.ai/token-factory/models/glm-5-3)### [GLM 5.3 Flash

  * Z.ai
  * Reasoning and coding
  * 1M context

![](https://assets.sarvam.ai/assets/token-factory/logos/zai.svg)Faster open-weight reasoning model for agents and image understanding.](https://www.sarvam.ai/token-factory/models/glm-5-3-flash)### [DeepSeek V4.1 Flash 1017

  * DeepSeek
  * Reasoning and coding
  * 1M context

![](https://assets.sarvam.ai/assets/token-factory/logos/deepseek.svg)General-purpose open-weight model for long-document analysis and agentic workflows.](https://www.sarvam.ai/token-factory/models/deepseek-v4-1-flash-1017)

From model choice to production. Bring your workload, traffic expectations and latency targets. Build on Sarvam’s serving stack in India. 

From model choice to production.

Bring your workload, traffic expectations and latency targets. Build on Sarvam’s serving stack in India.

[Talk to our team](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)[Read the API guide](https://docs.sarvam.ai/api/token-factory/models)
