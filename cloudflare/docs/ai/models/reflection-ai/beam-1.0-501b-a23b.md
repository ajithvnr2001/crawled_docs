---
url: https://developers.cloudflare.com/ai/models/reflection-ai/beam-1.0-501b-a23b/
title: Beam 1.0 501B A23B (reflection-ai) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:59.158129+00:00
---

# Beam 1.0 501B A23B (reflection-ai) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/reflection-ai/beam-1.0-501b-a23b/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



r

# Beam 1.0 501B A23B

Text Generation • reflection-ai

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`reflection-ai/beam-1.0-501b-a23b`

  * Third-party



Beam-1.0-501B-A23B is Reflection AI's open-weights mixture-of-experts model with 501B total parameters and 23B active parameters, built for coding, reasoning, and agentic workloads.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 262,144 tokens  
Terms and License| [link ↗](https://developers.reflection.ai/introduction)  
More information| [link ↗](https://developers.reflection.ai/models)  
Request formats| Chat Completions  
Pricing| 

  * Input (per 1M tokens)$0.00
  * Cached input (per 1M tokens)$0.00
  * Output (per 1M tokens)$0.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'reflection-ai/beam-1.0-501b-a23b',
      {
        messages: [{ role: 'user', content: 'Explain why the sky is blue in one sentence.' }],
        max_completion_tokens: 256,
        reasoning_effort: 'low',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "messages": [
        {
          "role": "user",
          "content": "Explain why the sky is blue in one sentence."
        }
      ],
      "max_completion_tokens": 256,
      "reasoning_effort": "low"
    }'
    
    
    The sky is blue because sunlight undergoes Rayleigh scattering in the atmosphere, which preferentially redirects shorter blue wavelengths toward your eyes.
    
    
    {
      "id": "chatcmpl-002d24bd-de9c-4bab-947d-47f77166eb5c",
      "object": "chat.completion",
      "created": 1792089654,
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "The sky is blue because sunlight undergoes Rayleigh scattering in the atmosphere, which preferentially redirects shorter blue wavelengths toward your eyes.",
            "refusal": null,
            "reasoning_content": "The user asks: \"Explain why the sky is blue in one sentence.\" Straightforward. Need one sentence. Ensure accuracy: Rayleigh scattering scatters shorter blue wavelengths more. Provide concise. No safety issues."
          },
          "finish_reason": "stop",
          "logprobs": null
        }
      ],
      "usage": {
        "prompt_tokens": 506,
        "completion_tokens": 79,
        "total_tokens": 585,
        "prompt_tokens_details": {
          "cached_tokens": 448
        },
        "completion_tokens_details": {
          "reasoning_tokens": 50
        }
      }
    }

## Examples

**Structured project status** — Return a typed project status summary using structured output
    
    
    const response = await env.AI.run(
      'reflection-ai/beam-1.0-501b-a23b',
      {
        messages: [
          {
            role: 'user',
            content:
              'Summarize this project update: API integration is complete, security review is scheduled for Friday, and the mobile client is blocked on final design assets.',
          },
        ],
        max_completion_tokens: 512,
        response_format: {
          type: 'json_schema',
          json_schema: {
            name: 'project_status',
            strict: true,
            schema: {
              type: 'object',
              properties: {
                overall_status: { type: 'string', enum: ['on_track', 'at_risk', 'blocked'] },
                completed: { type: 'array', items: { type: 'string' } },
                next_steps: { type: 'array', items: { type: 'string' } },
                blockers: { type: 'array', items: { type: 'string' } },
              },
              required: ['overall_status', 'completed', 'next_steps', 'blockers'],
              additionalProperties: false,
            },
          },
        },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "messages": [
        {
          "role": "user",
          "content": "Summarize this project update: API integration is complete, security review is scheduled for Friday, and the mobile client is blocked on final design assets."
        }
      ],
      "max_completion_tokens": 512,
      "response_format": {
        "type": "json_schema",
        "json_schema": {
          "name": "project_status",
          "strict": true,
          "schema": {
            "type": "object",
            "properties": {
              "overall_status": {
                "type": "string",
                "enum": [
                  "on_track",
                  "at_risk",
                  "blocked"
                ]
              },
              "completed": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "next_steps": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "blockers": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            },
            "required": [
              "overall_status",
              "completed",
              "next_steps",
              "blockers"
            ],
            "additionalProperties": false
          }
        }
      }
    }'
    
    
    {"overall_status": "on_track",
    "completed": ["API integration"],
    "next_steps": ["Security review scheduled for Friday"],
    "blockers": ["Mobile client awaiting final design assets"]}
    
    
    {
      "id": "chatcmpl-781353f2-706b-4d56-b771-c785968bbf97",
      "object": "chat.completion",
      "created": 1792089661,
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "{\"overall_status\": \"on_track\",\n\"completed\": [\"API integration\"],\n\"next_steps\": [\"Security review scheduled for Friday\"],\n\"blockers\": [\"Mobile client awaiting final design assets\"]}",
            "refusal": null,
            "reasoning_content": "The user wants a summary of a project update. Straightforward. Just summarize."
          },
          "finish_reason": "stop",
          "logprobs": null
        }
      ],
      "usage": {
        "prompt_tokens": 527,
        "completion_tokens": 64,
        "total_tokens": 591,
        "prompt_tokens_details": {
          "cached_tokens": 512
        },
        "completion_tokens_details": {
          "reasoning_tokens": 18
        }
      }
    }

**Weather tool call** — Choose a weather lookup function and supply its arguments
    
    
    const response = await env.AI.run(
      'reflection-ai/beam-1.0-501b-a23b',
      {
        messages: [{ role: 'user', content: 'What is the weather in Lisbon today?' }],
        max_completion_tokens: 256,
        tool_choice: 'required',
        tools: [
          {
            type: 'function',
            function: {
              name: 'get_weather',
              description: 'Look up the current weather for a city.',
              parameters: {
                type: 'object',
                properties: {
                  city: { type: 'string' },
                  units: { type: 'string', enum: ['celsius', 'fahrenheit'] },
                },
                required: ['city', 'units'],
                additionalProperties: false,
              },
            },
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "messages": [
        {
          "role": "user",
          "content": "What is the weather in Lisbon today?"
        }
      ],
      "max_completion_tokens": 256,
      "tool_choice": "required",
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_weather",
            "description": "Look up the current weather for a city.",
            "parameters": {
              "type": "object",
              "properties": {
                "city": {
                  "type": "string"
                },
                "units": {
                  "type": "string",
                  "enum": [
                    "celsius",
                    "fahrenheit"
                  ]
                }
              },
              "required": [
                "city",
                "units"
              ],
              "additionalProperties": false
            }
          }
        }
      ]
    }'
    
    
    {
      "id": "chatcmpl-fda9d6ad-dcb0-4b60-9e5a-4d78f406ecc1",
      "object": "chat.completion",
      "created": 1792089672,
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": null,
            "tool_calls": [
              {
                "id": "call-c105de7f-4e34-4ce9-bab9-ef2e6a89b645",
                "type": "function",
                "function": {
                  "name": "get_weather",
                  "arguments": "{\"city\": \"Lisbon\", \"units\": \"celsius\"}"
                }
              }
            ],
            "refusal": null,
            "reasoning_content": "The user is asking about the weather in Lisbon today. I have a tool to get weather. Let me call it with city Lisbon and units... the user didn't specify units. Celsius is reasonable default, but maybe I should pick. Let me use celsius as default. Actually, let me just call."
          },
          "finish_reason": "tool_calls",
          "logprobs": null
        }
      ],
      "usage": {
        "prompt_tokens": 544,
        "completion_tokens": 92,
        "total_tokens": 636,
        "prompt_tokens_details": {
          "cached_tokens": 512
        },
        "completion_tokens_details": {
          "reasoning_tokens": 69
        }
      }
    }

**Scheduling reasoning** — Reason through a scheduling constraint with system guidance
    
    
    const response = await env.AI.run(
      'reflection-ai/beam-1.0-501b-a23b',
      {
        messages: [
          {
            role: 'system',
            content: 'Answer concisely and show the scheduling logic in two bullet points.',
          },
          {
            role: 'user',
            content:
              'Maya is available Monday and Wednesday. Theo is available Wednesday and Thursday. Priya is available Monday, Wednesday, and Friday. Which day should they schedule a 90-minute meeting, and why?',
          },
          { role: 'user', content: 'The meeting must include all three attendees.' },
          { role: 'user', content: 'Please give the recommendation.' },
        ],
        max_completion_tokens: 384,
        reasoning_effort: 'medium',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "messages": [
        {
          "role": "system",
          "content": "Answer concisely and show the scheduling logic in two bullet points."
        },
        {
          "role": "user",
          "content": "Maya is available Monday and Wednesday. Theo is available Wednesday and Thursday. Priya is available Monday, Wednesday, and Friday. Which day should they schedule a 90-minute meeting, and why?"
        },
        {
          "role": "user",
          "content": "The meeting must include all three attendees."
        },
        {
          "role": "user",
          "content": "Please give the recommendation."
        }
      ],
      "max_completion_tokens": 384,
      "reasoning_effort": "medium"
    }'
    
    
    - All three must attend, so the meeting day must be in the intersection of Maya's (Mon, Wed), Theo's (Wed, Thu), and Priya's (Mon, Wed, Fri) calendars; only Wednesday appears for all three.
    - Therefore, schedule the 90-minute meeting on Wednesday, since it is the only day all attendees are available.
    
    
    {
      "id": "chatcmpl-26cd51e7-33f7-4048-93f0-69f51b1c66cc",
      "object": "chat.completion",
      "created": 1792089681,
      "model": "reflection-ai/beam-1.0-501b-a23b",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "- All three must attend, so the meeting day must be in the intersection of Maya's (Mon, Wed), Theo's (Wed, Thu), and Priya's (Mon, Wed, Fri) calendars; only Wednesday appears for all three.\n- Therefore, schedule the 90-minute meeting on Wednesday, since it is the only day all attendees are available.",
            "refusal": null,
            "reasoning_content": "The user asks: Maya available Mon/Wed, Theo available Wed/Thu, Priya available Mon/Wed/Fri. Meeting must include all three. Need schedule 90-min meeting. Which day should schedule and why? Concise, two bullet points showing scheduling logic. Constraints: all three must attend. Intersection: Maya ∩ Theo = Wed; Priya ∩ {Wed} = Wed. So Wednesday is common day. Need 90-minute meeting—presumably available all day? No time specifics. So recommend Wednesday; only day all three available. Answer with two bullet points.\n\nNeed ensure not violate policy. Fine.\n\nLet's craft concise."
          },
          "finish_reason": "stop",
          "logprobs": null
        }
      ],
      "usage": {
        "prompt_tokens": 572,
        "completion_tokens": 218,
        "total_tokens": 790,
        "prompt_tokens_details": {
          "cached_tokens": 448
        },
        "completion_tokens_details": {
          "reasoning_tokens": 138
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

Input[](https://developers.cloudflare.com/ai/models/reflection-ai/beam-1.0-501b-a23b/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/reflection-ai/beam-1.0-501b-a23b/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/reflection-ai/beam-1.0-501b-a23b/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/reflection-ai/beam-1.0-501b-a23b/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
