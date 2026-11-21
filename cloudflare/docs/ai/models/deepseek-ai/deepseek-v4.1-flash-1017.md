---
url: https://developers.cloudflare.com/ai/models/deepseek-ai/deepseek-v4.1-flash-1017/
title: DeepSeek V4.1 Flash (DeepSeek) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:30.470367+00:00
---

# DeepSeek V4.1 Flash (DeepSeek) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/deepseek-ai/deepseek-v4.1-flash-1017/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![DeepSeek logo](https://developers.cloudflare.com/_astro/deepseek.CkzAgvN6.svg)

# DeepSeek V4.1 Flash

Text Generation • DeepSeek

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`deepseek-ai/deepseek-v4.1-flash-1017`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



DeepSeek V4.1 Flash is a language model from DeepSeek, available through Cloudflare Workers AI and Subconscious, with PrimaLabs as a fallback.

Model Info|   
---|---  
More information| [link ↗](https://api-docs.deepseek.com/)  
Request formats| Chat Completions, Responses  
Pricing| 

  * Input (per 1M tokens)$0.30
  * Cached input (per 1M tokens)$0.007
  * Output (per 1M tokens)$1.20

  
  
## Usage
    
    
    export interface Env {
      AI: Ai;
    }
    
    export default {
      async fetch(request, env): Promise<Response> {
    
        const messages = [
          { role: "system", content: "You are a friendly assistant" },
          {
            role: "user",
            content: "What is the origin of the phrase Hello, World",
          },
        ];
    
        const stream = await env.AI.run("deepseek-ai/deepseek-v4.1-flash-1017", {
          messages,
          stream: true,
        });
    
        return new Response(stream, {
          headers: { "content-type": "text/event-stream" },
        });
      },
    } satisfies ExportedHandler<Env>;
    
    
    export interface Env {
      AI: Ai;
    }
    
    export default {
      async fetch(request, env): Promise<Response> {
    
        const messages = [
          { role: "system", content: "You are a friendly assistant" },
          {
            role: "user",
            content: "What is the origin of the phrase Hello, World",
          },
        ];
        const response = await env.AI.run("deepseek-ai/deepseek-v4.1-flash-1017", { messages });
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    prompt = "Tell me all about PEP-8"
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/deepseek-ai/deepseek-v4.1-flash-1017",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
          "messages": [
            {"role": "system", "content": "You are a friendly assistant"},
            {"role": "user", "content": prompt}
          ]
        }
    )
    result = response.json()
    print(result)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/deepseek-ai/deepseek-v4.1-flash-1017 \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{ "messages": [{ "role": "system", "content": "You are a friendly assistant" }, { "role": "user", "content": "Why is pizza so good" }]}'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/) . 

## Parameters

Schema variant

Chat CompletionsResponses

▶messages[]

`array`required

temperature

`number`minimum: 0maximum: 2

max_tokens

`number`exclusiveMinimum: 0

max_completion_tokens

`number`exclusiveMinimum: 0

top_p

`number`minimum: 0maximum: 1

frequency_penalty

`number`minimum: -2maximum: 2

presence_penalty

`number`minimum: -2maximum: 2

stream

`boolean`

▶stream_options{}

`object`

▶tools[]

`array`

tool_choice

``

response_format

``

▶modalities[]

`array`

▶audio{}

`object`

reasoning_effort

`string`Optional reasoning control; availability and accepted values are model-dependent.

▶input

`one of`required

instructions

`string`

temperature

`number`minimum: 0maximum: 2

max_output_tokens

`number`exclusiveMinimum: 0

top_p

`number`minimum: 0maximum: 1

stream

`boolean`

▶tools[]

`array`

tool_choice

``

▶text{}

`object`

▶reasoning{}

`object`

id

`string`

object

`string`

created

`number`

model

`string`

▶choices[]

`array`

▶usage{}

`object`

id

`string`

object

`string`const: response

created_at

`number`

model

`string`

▶output[]

`array`

output_text

`string`

status

`string`enum: in_progress, completed, failed, incomplete

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/deepseek-ai/deepseek-v4.1-flash-1017/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/deepseek-ai/deepseek-v4.1-flash-1017/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/deepseek-ai/deepseek-v4.1-flash-1017/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/deepseek-ai/deepseek-v4.1-flash-1017/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
