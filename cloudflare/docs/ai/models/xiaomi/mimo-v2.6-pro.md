---
url: https://developers.cloudflare.com/ai/models/xiaomi/mimo-v2.6-pro/
title: MiMo-V2.6-Pro (xiaomi) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.920680+00:00
---

# MiMo-V2.6-Pro (xiaomi) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/xiaomi/mimo-v2.6-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



x

# MiMo-V2.6-Pro

Text Generation • xiaomi

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`xiaomi/mimo-v2.6-pro`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Xiaomi MiMo-V2.6-Pro is a reasoning model served by PrimaLabs. It thinks before it answers, supports tool calling and prompt caching, and has a context window of about 1M tokens through an OpenAI-compatible Chat Completions API.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,048,576 tokens  
More information| [link ↗](https://docs.primalabs.ai/inference/models.md)  
Request formats| Chat Completions  
Pricing| 

  * Input (per 1M tokens)$4.00
  * Output (per 1M tokens)$8.00
  * Cached input (per 1M tokens)$0.036

  
  
## Usage
    
    
    const response = await env.AI.run(
      'xiaomi/mimo-v2.6-pro',
      {
        messages: [{ role: 'user', content: 'Explain KV caching in two sentences.' }],
        max_completion_tokens: 2048,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xiaomi/mimo-v2.6-pro",
      "messages": [
        {
          "role": "user",
          "content": "Explain KV caching in two sentences."
        }
      ],
      "max_completion_tokens": 2048
    }'
    
    
    KV caching stores the key and value tensors computed at each layer during the autoregressive generation of a transformer so that, on the next token prediction, the model only needs to compute attention for the new token against the cached keys and values rather than reprocessing the entire sequence from scratch. This avoids redundant computation across decoding steps, reducing time complexity from O(n²) to O(n) per new token and making text generation significantly faster.
    
    
    {
      "id": "chatcmpl-b690f48c7de59601",
      "object": "chat.completion",
      "created": 1794584767,
      "model": "xiaomi/mimo-v2.6-pro",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "KV caching stores the key and value tensors computed at each layer during the autoregressive generation of a transformer so that, on the next token prediction, the model only needs to compute attention for the new token against the cached keys and values rather than reprocessing the entire sequence from scratch. This avoids redundant computation across decoding steps, reducing time complexity from O(n²) to O(n) per new token and making text generation significantly faster.",
            "reasoning_content": "The user wants a concise two-sentence explanation of KV caching.",
            "provider_specific_fields": {
              "refusal": null,
              "reasoning": "The user wants a concise two-sentence explanation of KV caching."
            }
          },
          "finish_reason": "stop",
          "provider_specific_fields": {
            "token_ids": null,
            "routed_experts": null
          }
        }
      ],
      "usage": {
        "prompt_tokens": 15,
        "completion_tokens": 103,
        "total_tokens": 118,
        "completion_tokens_details": {
          "reasoning_tokens": 13
        },
        "prompt_tokens_details": {
          "cached_tokens": 0,
          "created_cache_tokens": 0
        }
      }
    }

## Examples

**Streaming chat** — Stream a short explanation of exponential backoff.
    
    
    const response = await env.AI.run(
      'xiaomi/mimo-v2.6-pro',
      {
        messages: [{ role: 'user', content: 'Explain exponential backoff in two sentences.' }],
        max_completion_tokens: 2048,
        stream: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xiaomi/mimo-v2.6-pro",
      "messages": [
        {
          "role": "user",
          "content": "Explain exponential backoff in two sentences."
        }
      ],
      "max_completion_tokens": 2048,
      "stream": true
    }'
    
    
    Exponential backoff is a retry strategy where the wait time between successive attempts increases exponentially (e.g., 1s, 2s, 4s, 8s…) rather than remaining constant. This prevents overwhelming a struggling service or network with rapid repeated requests and gives it time to recover before the next attempt.
    
    
    [
      {
        "id": "chatcmpl-b41c1b2c54f92779",
        "object": "chat.completion.chunk",
        "created": 1794584769,
        "model": "primalabs-ai/MiMo-V2.6-Pro-cloudflare",
        "choices": [
          {
            "index": 0,
            "delta": {
              "role": "assistant",
              "content": ""
            }
          }
        ]
      },
      {
        "id": "chatcmpl-b41c1b2c54f92779",
        "created": 1794584769,
        "model": "primalabs-ai/MiMo-V2.6-Pro-cloudflare",
        "object": "chat.completion.chunk",
        "choices": [
          {
            "index": 0,
            "delta": {
              "reasoning_content": "The user wants a concise two-sentence explanation of exponential backoff."
            }
          }
        ]
      },
      "... 27 more chunks omitted ...",
      {
        "id": "chatcmpl-b41c1b2c54f92779",
        "created": 1794584769,
        "model": "primalabs-ai/MiMo-V2.6-Pro-cloudflare",
        "object": "chat.completion.chunk",
        "choices": [
          {
            "index": 0,
            "delta": {}
          }
        ],
        "usage": {
          "completion_tokens": 82,
          "prompt_tokens": 16,
          "total_tokens": 98,
          "completion_tokens_details": {
            "reasoning_tokens": 14
          },
          "prompt_tokens_details": {
            "cached_tokens": 0,
            "created_cache_tokens": 16
          },
          "cost": 0.00072
        }
      }
    ]

**Tool calling** — Ask MiMo-V2.6-Pro to call a weather lookup function.
    
    
    const response = await env.AI.run(
      'xiaomi/mimo-v2.6-pro',
      {
        messages: [{ role: 'user', content: 'What is the weather in Paris?' }],
        max_completion_tokens: 2048,
        tools: [
          {
            type: 'function',
            function: {
              name: 'get_weather',
              description: 'Get the current weather for a city.',
              parameters: {
                type: 'object',
                properties: { city: { type: 'string' } },
                required: ['city'],
              },
            },
          },
        ],
        tool_choice: { type: 'function', function: { name: 'get_weather' } },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xiaomi/mimo-v2.6-pro",
      "messages": [
        {
          "role": "user",
          "content": "What is the weather in Paris?"
        }
      ],
      "max_completion_tokens": 2048,
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
              "type": "object",
              "properties": {
                "city": {
                  "type": "string"
                }
              },
              "required": [
                "city"
              ]
            }
          }
        }
      ],
      "tool_choice": {
        "type": "function",
        "function": {
          "name": "get_weather"
        }
      }
    }'
    
    
    {
      "id": "chatcmpl-8692555c2e4e4ec8",
      "object": "chat.completion",
      "created": 1794584770,
      "model": "xiaomi/mimo-v2.6-pro",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "",
            "tool_calls": [
              {
                "function": {
                  "arguments": "{\"city\": \"Paris\"}",
                  "name": "get_weather"
                },
                "id": "chatcmpl-tool-85225333bedb366a",
                "type": "function"
              }
            ],
            "reasoning_content": "The user wants weather in Paris.",
            "provider_specific_fields": {
              "refusal": null,
              "reasoning": "The user wants weather in Paris."
            }
          },
          "finish_reason": "tool_calls",
          "provider_specific_fields": {
            "token_ids": null,
            "routed_experts": null
          }
        }
      ],
      "usage": {
        "prompt_tokens": 90,
        "completion_tokens": 27,
        "total_tokens": 117,
        "completion_tokens_details": {
          "reasoning_tokens": 7
        },
        "prompt_tokens_details": {
          "cached_tokens": 16,
          "created_cache_tokens": 64
        }
      }
    }

## Parameters

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

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/xiaomi/mimo-v2.6-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/xiaomi/mimo-v2.6-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/xiaomi/mimo-v2.6-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/xiaomi/mimo-v2.6-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
