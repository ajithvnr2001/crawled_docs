---
url: https://www.sarvam.ai/token-factory/models/gemma-4-31b/
title: Gemma 4 31B | Sarvam Token Factory
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:08.567881+00:00
---

# Gemma 4 31B | Sarvam Token Factory

> Source: https://www.sarvam.ai/token-factory/models/gemma-4-31b/

[ Token Factory ](https://www.sarvam.ai/token-factory) / [ Models ](https://www.sarvam.ai/token-factory/models) / Gemma 4 31B

[ ![](https://assets.sarvam.ai/assets/token-factory/logos/google.svg)Google DeepMind ](https://www.sarvam.ai/token-factory/models)

# Gemma 4 31B

Process images and text with Google DeepMind’s 31B model, served by Sarvam for conversation and tool use. Direct answers suit workflows that do not need a separate reasoning trace.

  * Vision 
  * Tool calling 
  * Chat 
  * Extraction 



[Try in playground](https://indus.sarvam.ai/api-playground/chat-completions?model=gemma4)[View API reference](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)

## Token pricing

[ Compare all model pricing ](https://www.sarvam.ai/token-factory/pricing)

Input
    Tokens sent to the model.

₹35.00 per 1M tokens

Cached input
    Eligible tokens reused from a cached prefix.

₹10.00 per 1M tokens

Output
    Generated tokens, including reasoning.

₹90.00 per 1M tokens

Excluding GST

API model ID  ` gemma4 `

Provider 
     [ Google DeepMind ](https://www.sarvam.ai/token-factory/models)

Context window 
     256K tokens 

Input types 
     Text + image 

Response style 
     Direct answers 

Deployment 
     Serverless · India 

## Best suited for

  1. 01 

###  Visual document extraction 

Combine page images and text instructions to extract fields, interpret layouts and prepare information for downstream systems. 

  2. 02 

###  High-volume conversations 

Generate direct responses for chat and support workflows without a separate reasoning step. 

  3. 03 

###  Image-grounded tool use 

Use visual context alongside function calling to turn information from images into application actions. 




Build with the Sarvam SDK

PythonJavaScriptcURL

Copy

$`pip install --upgrade sarvamai`V2 · Sarvam SDK · Streaming
    
    
    import osfrom sarvamai import SarvamAI​client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])​stream = client.chat.completions_v2(    model="gemma4",    messages=[{"role": "user", "content": "Explain why time to first token matters for a chat application briefly."}],    max_tokens=8000,    stream=True,)​for chunk in stream:    if not chunk.choices:        continue    text = chunk.choices[0].delta.content    if text:        print(text, end="", flush=True)

  1. 01 **Install the Sarvam SDK**

Install `sarvamai` for Python or JavaScript. Store your key in `SARVAM_API_KEY`.

  2. 02 **Choose your model**

Use model ID `gemma4`. The SDK calls `https://api.sarvam.ai/v2` for this example.

V2 Chat Completions. Thinking is off by default, so this example returns a direct answer.

  3. 03 **Validate your application**

Check output quality, supported parameters and tool behaviour on representative requests before moving production traffic.


[ Model API Reference ](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)

##  Frequently Asked  
Questions 

### What is Gemma 4 31B on Sarvam?

It is Google DeepMind’s 31B-parameter model, served by Sarvam for conversation and tool use. The Sarvam endpoint accepts text and images and returns text directly.

### What is the served context window?

Sarvam serves a 262,144-token (256K) context window. Input and generated output share this allowance. Size requests against this served limit rather than a different provider’s advertised context window.

### Does this endpoint generate a reasoning trace?

No. The Sarvam endpoint returns direct answers without a separate reasoning pass.

### Does it support tools and streaming?

Yes. Use OpenAI-compatible tool definitions and stream answer tokens as they arrive. Call the v2 Chat Completions endpoint with model ID gemma4. [Read the model guide](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)

### Is it specifically tuned for Indian languages?

No. Gemma 4 31B is not specifically tuned for Indian languages. For native-script, romanised and code-mixed Indian-language workloads, compare it with Sarvam 105B on your own evaluation set. [See Sarvam 105B](https://www.sarvam.ai/token-factory/models/sarvam-105b)

### How is Gemma 4 31B priced?

The rates per million tokens are ₹35.00 for input, ₹10.00 for eligible cached input and ₹90.00 for output, excluding GST.

### Where does inference run, and what SLA is available?

Inference runs on Sarvam-operated GPUs in India. Token Factory guarantees 99.95% uptime, backed by an SLA. Discuss your traffic, latency targets and support requirements with the Sarvam team. [Discuss SLA](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)

## Explore other models

[ View catalogue ](https://www.sarvam.ai/token-factory/models)

### [GLM 5.3

  * Z.ai
  * Reasoning and coding
  * 1M context

![](https://assets.sarvam.ai/assets/token-factory/logos/zai.svg)Large-scale reasoning model built for complex software engineering and long-horizon agent tasks.](https://www.sarvam.ai/token-factory/models/glm-5-3)### [DeepSeek V4.1 Flash 1017

  * DeepSeek
  * Reasoning and coding
  * 1M context

![](https://assets.sarvam.ai/assets/token-factory/logos/deepseek.svg)General-purpose open-weight model for long-document analysis and agentic workflows.](https://www.sarvam.ai/token-factory/models/deepseek-v4-1-flash-1017)### [Sarvam 105B

  * Sarvam
  * Indian languages
  * 128K context

![](https://assets.sarvam.ai/assets/brand/sarvam_logo_pack/logomark-dark.svg)Flagship 105B Mixture-of-Experts model trained from scratch for Indian-language understanding, complex reasoning, coding and agentic workflows.](https://www.sarvam.ai/token-factory/models/sarvam-105b)

From model choice to production. Bring your workload, traffic expectations and latency targets. Build on Sarvam’s serving stack in India. 

From model choice to production.

Bring your workload, traffic expectations and latency targets. Build on Sarvam’s serving stack in India.

[Talk to our team](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)[Read the API guide](https://docs.sarvam.ai/api/token-factory/models)
