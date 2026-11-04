---
url: https://www.sarvam.ai/token-factory/models/sarvam-105b-chat/
title: Sarvam 105B Conversations | Sarvam Token Factory
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:09.399127+00:00
---

# Sarvam 105B Conversations | Sarvam Token Factory

> Source: https://www.sarvam.ai/token-factory/models/sarvam-105b-chat/

[ Token Factory ](https://www.sarvam.ai/token-factory) / [ Models ](https://www.sarvam.ai/token-factory/models) / Sarvam 105B Conversations

[ ![](https://assets.sarvam.ai/assets/brand/sarvam_logo_pack/logomark-dark.svg)Sarvam ](https://www.sarvam.ai/token-factory/models)

# Sarvam 105B Conversations

Power the language-model step in real-time conversations with a variant tuned for dialogue in Indian languages and English.

  * Indian languages 
  * Chat 
  * Streaming 
  * Voice agents 



[Try in playground](https://indus.sarvam.ai/api-playground/chat-completions?model=sarvam-105b-conversations)[View API reference](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)

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

API model ID  ` sarvam-105b-conversations `

Provider 
     [ Sarvam ](https://www.sarvam.ai/token-factory/models)

Context window 
     32K tokens 

Input types 
     Text 

Response style 
     Conversational variant 

Deployment 
     Serverless · India 

## Best suited for

  1. 01 

###  Streaming chat 

Display tokens as they arrive to keep conversational interfaces responsive throughout generation. 

  2. 02 

###  Voice-agent reasoning 

Use the model between transcription and speech synthesis to generate the next turn in a conversation. 

  3. 03 

###  Code-mixed dialogue 

Handle conversations that move between Indian languages, romanised text and English. 




## Benchmarks

Evaluate the conversational variant on the work it will do.

### A separate Chat evaluation is not published on Artificial Analysis.

Sarvam 105B Chat is distinct from the flagship reasoning model. The flagship comparison page also has no published quality scores. Compare Chat on your conversations, languages and response-time targets.

[ See the flagship model page ](https://www.sarvam.ai/token-factory/models/sarvam-105b#benchmarks)

Build with the Sarvam SDK

PythonJavaScriptcURL

Copy

$`pip install --upgrade sarvamai`V1 · Sarvam SDK · Streaming
    
    
    import osfrom sarvamai import SarvamAI​client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])​stream = client.chat.completions(    model="sarvam-105b-conversations",    messages=[{"role": "user", "content": "Explain how solar panels work in Hindi briefly."}],    max_tokens=8000,    reasoning_effort=None,    stream=True,)​for chunk in stream:    if not chunk.choices:        continue    text = chunk.choices[0].delta.content    if text:        print(text, end="", flush=True)

  1. 01 **Install the Sarvam SDK**

Install `sarvamai` for Python or JavaScript. Store your key in `SARVAM_API_KEY`.

  2. 02 **Choose your model**

Use model ID `sarvam-105b-conversations`. The SDK calls `https://api.sarvam.ai/v1` for this example.

V1 Chat Completions. Thinking is disabled for this short reply.

  3. 03 **Validate your application**

Check output quality, supported parameters and tool behaviour on representative requests before moving production traffic.


[ Model API Reference ](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)

##  Frequently Asked  
Questions 

### When should I use Sarvam 105B Chat?

Choose the conversational variant for real-time chat, multi-turn dialogue and voice-agent applications where natural Indian-language responses matter. Evaluate the flagship Sarvam 105B for tasks that need deeper reasoning.

### Does the model handle speech input and output itself?

No. This is the text-generation step in a voice pipeline. Use a speech-to-text component to transcribe input and a text-to-speech component to turn its generated response into audio.

### How much conversation history can I send?

The Chat variant has a 32K-token context window. Fit system instructions, conversation history and the generated response within that allowance; summarise or trim older turns as needed.

### Can I stream its responses?

Yes. Set stream to true to receive generated tokens incrementally. Your application can display them in a chat interface or pass text to the next component in a voice pipeline.

### Which API route does this variant use?

Use the v1 Chat Completions endpoint with model ID sarvam-105b-conversations. This differs from the v2 endpoint shown for the flagship model; the migration snippets on this page use the correct v1 base URL.

### Are the flagship model’s AA scores applicable to Chat?

No. Artificial Analysis does not publish a separate evaluation for this conversational variant. The flagship model’s reasoning scores are not transferred to Chat. Evaluate conversational quality and response times on your own tasks.

### How is Sarvam 105B Conversations priced?

The rates per million tokens are ₹15.00 for input, ₹5.00 for eligible cached input and ₹60.00 for output, excluding GST.

### Where does inference run, and what SLA is available?

Inference runs on Sarvam-operated GPUs in India. Token Factory guarantees 99.95% uptime, backed by an SLA. Discuss your traffic, latency targets and support requirements with the Sarvam team. [Discuss SLA](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)

## Explore other models

[ View catalogue ](https://www.sarvam.ai/token-factory/models)

### [Sarvam 105B

  * Sarvam
  * Indian languages
  * 128K context

![](https://assets.sarvam.ai/assets/brand/sarvam_logo_pack/logomark-dark.svg)Flagship 105B Mixture-of-Experts model trained from scratch for Indian-language understanding, complex reasoning, coding and agentic workflows.](https://www.sarvam.ai/token-factory/models/sarvam-105b)### [GLM 5.3 Flash

  * Z.ai
  * Reasoning and coding
  * 1M context

![](https://assets.sarvam.ai/assets/token-factory/logos/zai.svg)Faster open-weight reasoning model for agents and image understanding.](https://www.sarvam.ai/token-factory/models/glm-5-3-flash)### [Gemma 4 31B

  * Google DeepMind
  * Vision
  * 256K context

![](https://assets.sarvam.ai/assets/token-factory/logos/google.svg)31B-parameter instruction-tuned model for text and image understanding, with tool calling and optional reasoning.](https://www.sarvam.ai/token-factory/models/gemma-4-31b)

From model choice to production. Bring your workload, traffic expectations and latency targets. Build on Sarvam’s serving stack in India. 

From model choice to production.

Bring your workload, traffic expectations and latency targets. Build on Sarvam’s serving stack in India.

[Talk to our team](https://www.sarvam.ai/contact-us?product=token-factory&request=inference)[Read the API guide](https://docs.sarvam.ai/api/token-factory/models)
