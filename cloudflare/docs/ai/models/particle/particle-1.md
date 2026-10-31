---
url: https://developers.cloudflare.com/ai/models/particle/particle-1/
title: Particle-1 (particle) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:16.741209+00:00
---

# Particle-1 (particle) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/particle/particle-1/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



p

# Particle-1

Text Generation • particle

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`particle/particle-1`

  * Third-party
  * Zero data retention



Particle-1 is Particle AI's reasoning model for chat, agentic coding, and tool use. It accepts text and images, with a 1,048,576-token context window, streaming responses, and configurable reasoning effort.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,048,576 tokens  
More information| [link ↗](https://docs.particle.ai/models)  
Zero data retention| Yes  
Request formats| Chat Completions  
Pricing| 

  * Input (per 1M tokens)$0.25
  * Cached input (per 1M tokens)$0.03
  * Output (per 1M tokens)$1.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'particle/particle-1',
      {
        messages: [{ role: 'user', content: 'Explain KV caching in two sentences.' }],
        reasoning_effort: 'none',
        max_completion_tokens: 256,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "particle/particle-1",
      "messages": [
        {
          "role": "user",
          "content": "Explain KV caching in two sentences."
        }
      ],
      "reasoning_effort": "none",
      "max_completion_tokens": 256
    }'
    
    
    KV caching stores the key and value tensors computed for each token during transformer attention so they can be reused instead of recomputed at every decoding step. This turns generation from quadratic to roughly linear work per new token, dramatically speeding up autoregressive inference at the cost of extra memory.
    
    
    {
      "id": "e5778c6255f749c6ac49ebfaa882266d",
      "object": "chat.completion",
      "created": 1793303112,
      "model": "particle/particle-1",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "KV caching stores the key and value tensors computed for each token during transformer attention so they can be reused instead of recomputed at every decoding step. This turns generation from quadratic to roughly linear work per new token, dramatically speeding up autoregressive inference at the cost of extra memory.",
            "tool_calls": null,
            "reasoning_content": null
          },
          "finish_reason": "stop",
          "logprobs": null,
          "matched_stop": 1
        }
      ],
      "usage": {
        "prompt_tokens": 64,
        "completion_tokens": 57,
        "total_tokens": 121,
        "completion_tokens_details": {
          "reasoning_tokens": 0
        },
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "reasoning_tokens": 0
      },
      "metadata": null,
      "service_tier": "free"
    }

## Examples

**Streaming chat** — Stream a short explanation of exponential backoff.
    
    
    const response = await env.AI.run(
      'particle/particle-1',
      {
        messages: [{ role: 'user', content: 'Explain exponential backoff in two sentences.' }],
        reasoning_effort: 'none',
        max_completion_tokens: 256,
        stream: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "particle/particle-1",
      "messages": [
        {
          "role": "user",
          "content": "Explain exponential backoff in two sentences."
        }
      ],
      "reasoning_effort": "none",
      "max_completion_tokens": 256,
      "stream": true
    }'
    
    
    Exponential backoff is a strategy where a system retries a failed operation after waiting progressively longer intervals, typically doubling the delay after each attempt. It helps reduce contention and avoid overwhelming a struggling service by spreading out retries over time.
    
    
    [
      {
        "id": "819751464b54400dadedfd50c69e91ca",
        "object": "chat.completion.chunk",
        "created": 1793303113,
        "model": "particle-ai/particle-1",
        "choices": [
          {
            "index": 0,
            "delta": {
              "reasoning_content": null,
              "role": "assistant",
              "content": ""
            },
            "logprobs": null,
            "finish_reason": null,
            "matched_stop": null
          }
        ],
        "service_tier": "free"
      },
      {
        "id": "819751464b54400dadedfd50c69e91ca",
        "object": "chat.completion.chunk",
        "created": 1793303113,
        "model": "particle-ai/particle-1",
        "choices": [
          {
            "index": 0,
            "delta": {
              "reasoning_content": null,
              "content": "Ex"
            },
            "logprobs": null,
            "finish_reason": null,
            "matched_stop": null
          }
        ],
        "service_tier": "free"
      },
      "... 20 more chunks omitted ...",
      {
        "id": "819751464b54400dadedfd50c69e91ca",
        "object": "chat.completion.chunk",
        "created": 1793303113,
        "model": "particle-ai/particle-1",
        "choices": [],
        "usage": {
          "prompt_tokens": 65,
          "total_tokens": 113,
          "completion_tokens": 48,
          "completion_tokens_details": {
            "reasoning_tokens": 0
          },
          "prompt_tokens_details": {
            "cached_tokens": 0
          },
          "reasoning_tokens": 0
        },
        "service_tier": "free"
      }
    ]

**Tool calling** — Ask Particle-1 to call a weather lookup function.
    
    
    const response = await env.AI.run(
      'particle/particle-1',
      {
        messages: [{ role: 'user', content: 'What is the weather in Paris?' }],
        reasoning_effort: 'none',
        max_completion_tokens: 256,
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
      "model": "particle/particle-1",
      "messages": [
        {
          "role": "user",
          "content": "What is the weather in Paris?"
        }
      ],
      "reasoning_effort": "none",
      "max_completion_tokens": 256,
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
      "id": "3831fab494624c51ba5cd542d5b807a6",
      "object": "chat.completion",
      "created": 1793303113,
      "model": "particle/particle-1",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "",
            "tool_calls": [
              {
                "id": "call_b6bcda29bef84dcf80a570a1",
                "type": "function",
                "function": {
                  "name": "get_weather",
                  "arguments": "{\"city\": \"Paris\"}"
                }
              }
            ],
            "reasoning_content": null
          },
          "finish_reason": "tool_calls",
          "logprobs": null,
          "matched_stop": 1
        }
      ],
      "usage": {
        "prompt_tokens": 324,
        "completion_tokens": 39,
        "total_tokens": 363,
        "completion_tokens_details": {
          "reasoning_tokens": 0
        },
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "reasoning_tokens": 0
      },
      "metadata": null,
      "service_tier": "free"
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

Input[](https://developers.cloudflare.com/ai/models/particle/particle-1/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/particle/particle-1/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/particle/particle-1/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/particle/particle-1/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
