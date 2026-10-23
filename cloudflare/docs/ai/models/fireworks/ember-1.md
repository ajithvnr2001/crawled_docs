---
url: https://developers.cloudflare.com/ai/models/fireworks/ember-1/
title: Ember-1 (Fireworks) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:04.737591+00:00
---

# Ember-1 (Fireworks) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/fireworks/ember-1/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Fireworks logo](https://developers.cloudflare.com/_astro/fireworks.CeRQXhcu.svg)

# Ember-1

Text Generation • Fireworks

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`fireworks/ember-1`

  * Third-party
  * Zero data retention



Fireworks' Ember-1 is a specialized long-context multimodal reasoning model built on Kimi K3. It produces shorter reasoning traces using approximately 40% fewer tokens while maintaining comparable quality across Fireworks' evaluations.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,040,000 tokens  
Terms and License| [link ↗](https://fireworks.ai/terms)  
More information| [link ↗](https://fireworks.ai/models/fireworks/ember-1)  
Zero data retention| Yes  
Request formats| Chat Completions, Responses  
Pricing| 

  * Input (per 1M tokens)$3.00
  * Cached input (per 1M tokens)$0.30
  * Output (per 1M tokens)$15.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'fireworks/ember-1',
      {
        messages: [
          {
            content:
              'A library has 240 books. One quarter are checked out, and one third of the remaining books are reserved. How many books are available for browsing? Show the calculation briefly.',
            role: 'user',
          },
        ],
        max_tokens: 256,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "fireworks/ember-1",
      "messages": [
        {
          "content": "A library has 240 books. One quarter are checked out, and one third of the remaining books are reserved. How many books are available for browsing? Show the calculation briefly.",
          "role": "user"
        }
      ],
      "max_tokens": 256
    }'
    
    
    **Solution:**
    
    - Checked out: 240 × ¼ = 60 books
    - Remaining: 240 − 60 = 180 books
    - Reserved: 180 × ⅓ = 60 books
    - Available: 180 − 60 = **120 books**
    
    
    {
      "id": "chatcmpl-6f6f6ab7d28e4ec78bac38d4c6f595b8",
      "object": "chat.completion",
      "created": 1790686126,
      "model": "accounts/fireworks/models/ember-1",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "**Solution:**\n\n- Checked out: 240 × ¼ = 60 books\n- Remaining: 240 − 60 = 180 books\n- Reserved: 180 × ⅓ = 60 books\n- Available: 180 − 60 = **120 books**",
            "reasoning_content": "Total books: 240\nChecked out: 1/4 × 240 = 60\nRemaining: 240 - 60 = 180\nReserved: 1/3 × 180 = 60\nAvailable: 180 - 60 = 120",
            "tools": null
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 124,
        "total_tokens": 249,
        "completion_tokens": 125,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 54
        },
        "output_tokens_details": {
          "reasoning_tokens": 54
        }
      }
    }

## Examples

**Function Calling** — Use a function tool to produce structured arguments
    
    
    const response = await env.AI.run(
      'fireworks/ember-1',
      {
        messages: [
          { content: 'Schedule a 30-minute meeting with Alex tomorrow at 10 AM.', role: 'user' },
        ],
        tool_choice: 'required',
        tools: [
          {
            function: {
              description: 'Schedule a calendar meeting',
              name: 'schedule_meeting',
              parameters: {
                additionalProperties: false,
                properties: {
                  duration_minutes: { type: 'integer' },
                  participant: { type: 'string' },
                  start_time: { type: 'string' },
                },
                required: ['participant', 'start_time', 'duration_minutes'],
                type: 'object',
              },
              strict: true,
            },
            type: 'function',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "fireworks/ember-1",
      "messages": [
        {
          "content": "Schedule a 30-minute meeting with Alex tomorrow at 10 AM.",
          "role": "user"
        }
      ],
      "tool_choice": "required",
      "tools": [
        {
          "function": {
            "description": "Schedule a calendar meeting",
            "name": "schedule_meeting",
            "parameters": {
              "additionalProperties": false,
              "properties": {
                "duration_minutes": {
                  "type": "integer"
                },
                "participant": {
                  "type": "string"
                },
                "start_time": {
                  "type": "string"
                }
              },
              "required": [
                "participant",
                "start_time",
                "duration_minutes"
              ],
              "type": "object"
            },
            "strict": true
          },
          "type": "function"
        }
      ]
    }'
    
    
    I'll schedule that meeting for you.
    
    
    {
      "id": "chatcmpl-3ad7285ed64246499743d8485debc15f",
      "object": "chat.completion",
      "created": 1790686129,
      "model": "accounts/fireworks/models/ember-1",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "I'll schedule that meeting for you.",
            "reasoning_content": "The user wants to schedule a 30-minute meeting with Alex tomorrow at 10 AM. However, I don't know today's date. The schedule_meeting function requires a start_time in a specific format, but I don't know the current date.\n\nI need to figure out what \"tomorrow\" means. Since I don't have access to the current date, I should probably make a reasonable assumption or ask. But the tool_choice=required means I must call tools.\n\nWait, let me think about this. The instruction says I MUST call tools in the next message. The schedule_meeting tool needs start_time. I don't know the exact date. \n\nI could provide a start_time like \"tomorrow at 10 AM\" but the parameter likely expects a datetime string. Without knowing today's date, I cannot accurately compute tomorrow's date.\n\nHowever, given the constraint that I must call tools, I'll need to make my best guess. But guessing a date could be wrong. Let me consider: the system prompt doesn't give me a current date. \n\nGiven the requirement to call tools, I should attempt the call. But what start_time? I genuinely don't know today's date. \n\nHmm, but maybe the environment expects me to just pass a relative description or a plausible ISO date. Since I have no date context, the safest approach that still calls the tool would be to use a placeholder? That seems bad.\n\nActually, in these kinds of tasks, often the expectation is to call the tool with the given parameters. The start_time could be expressed as \"tomorrow 10:00 AM\". But the schema says string, no format specified. So I can pass a natural language string like \"tomorrow at 10:00 AM\". That satisfies the string type and conveys the intent. The backend may parse it.\n\nLet me call schedule_meeting with participant \"Alex\", start_time \"tomorrow at 10:00 AM\", duration_minutes 30.\n\nActually, to be more useful, maybe I should use a concrete date. But I don't know it. I'll pass the relative expression since format isn't specified. That's the most faithful to the user's request without inventing a wrong date.\n\nLet me make the call.",
            "tool_calls": [
              {
                "index": 0,
                "id": "schedule_meeting_0",
                "type": "function",
                "function": {
                  "name": "schedule_meeting",
                  "arguments": "{\"participant\": \"Alex\", \"start_time\": \"tomorrow at 10:00 AM\", \"duration_minutes\": 30}"
                },
                "name": null
              }
            ],
            "tools": null
          },
          "finish_reason": "tool_calls"
        }
      ],
      "usage": {
        "prompt_tokens": 241,
        "total_tokens": 781,
        "completion_tokens": 540,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 443
        },
        "output_tokens_details": {
          "reasoning_tokens": 443
        }
      }
    }

**Visual Understanding** — Analyze a visual scene
    
    
    const response = await env.AI.run(
      'fireworks/ember-1',
      {
        messages: [
          {
            content: [
              {
                image_url: { url: 'https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png' },
                type: 'image_url',
              },
              {
                text: 'Describe the main subject and setting in this image in two sentences.',
                type: 'text',
              },
            ],
            role: 'user',
          },
        ],
        max_tokens: 256,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "fireworks/ember-1",
      "messages": [
        {
          "content": [
            {
              "image_url": {
                "url": "https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png"
              },
              "type": "image_url"
            },
            {
              "text": "Describe the main subject and setting in this image in two sentences.",
              "type": "text"
            }
          ],
          "role": "user"
        }
      ],
      "max_tokens": 256
    }'
    
    
    A woman with dark hair pulled back, wearing a chunky navy sweater, gold chain, and several rings, holds a small microphone with a fuzzy windscreen while smiling at the camera. She is in a warmly lit indoor space with cream walls, a framed grid of black-and-white photos, a glowing lamp, and a white stair railing in the background.
    
    
    {
      "id": "chatcmpl-0e5b73a799f84182b41ccd83872ebc33",
      "object": "chat.completion",
      "created": 1790686138,
      "model": "accounts/fireworks/models/ember-1",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "A woman with dark hair pulled back, wearing a chunky navy sweater, gold chain, and several rings, holds a small microphone with a fuzzy windscreen while smiling at the camera. She is in a warmly lit indoor space with cream walls, a framed grid of black-and-white photos, a glowing lamp, and a white stair railing in the background.",
            "reasoning_content": "The user wants a two-sentence description of the main subject and setting. I can describe the image without identifying the person. Main subject: a woman with dark hair pulled back, wearing a navy blue chunky knit sweater, white undershirt, gold chain necklace, multiple rings, pale yellow nail polish, holding a small microphone with a furry windscreen. Setting: indoors, cozy room with cream walls, framed black-and-white photo grid, warm lamp, stair railing, artwork. Need exactly two sentences. Ensure no sensitive identification. Final concise.",
            "tools": null
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 10875,
        "total_tokens": 11067,
        "completion_tokens": 192,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 109
        },
        "output_tokens_details": {
          "reasoning_tokens": 109
        }
      }
    }

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

Input[](https://developers.cloudflare.com/ai/models/fireworks/ember-1/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/fireworks/ember-1/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/fireworks/ember-1/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/fireworks/ember-1/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
