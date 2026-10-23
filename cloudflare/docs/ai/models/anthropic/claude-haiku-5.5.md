---
url: https://developers.cloudflare.com/ai/models/anthropic/claude-haiku-5.5/
title: Claude Haiku 5.5 (Anthropic) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:06.865668+00:00
---

# Claude Haiku 5.5 (Anthropic) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/anthropic/claude-haiku-5.5/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Anthropic logo](https://developers.cloudflare.com/_astro/anthropic.DbRqBIjP.svg)

# Claude Haiku 5.5

Text Generation • Anthropic

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`anthropic/claude-haiku-5.5`

  * Third-party



Claude Haiku 5.5 is a fast, cost-efficient model for high-volume, latency-sensitive tasks such as classification, extraction, routing, and subagent work.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,000,000 tokens  
Terms and License| [link ↗](https://www.anthropic.com/legal/commercial-terms)  
More information| [link ↗](https://platform.claude.com/docs/en/models/haiku-5-5/overview)  
Request formats| Anthropic Messages  
Pricing| 

  * Short-context input (per 1M)$0.10
  * Short-context cached input (per 1M)$0.01
  * Short-context cache write (per 1M)$0.125
  * Short-context output (per 1M)$0.50
  * Long-context input (per 1M)$0.50
  * Long-context cached input (per 1M)$0.05
  * Long-context cache write (per 1M)$0.625
  * Long-context output (per 1M)$2.50

  
  
## Usage
    
    
    const response = await env.AI.run(
      'anthropic/claude-haiku-5.5',
      {
        max_tokens: 256,
        messages: [{ content: 'Classify this support ticket as billing, technical, or account: My invoice shows an unexpected charge.', role: 'user' }],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "anthropic/claude-haiku-5.5",
      "max_tokens": 256,
      "messages": [
        {
          "content": "Classify this support ticket as billing, technical, or account: My invoice shows an unexpected charge.",
          "role": "user"
        }
      ]
    }'
    
    
    **Billing**
    
    The ticket is about an invoice showing an unexpected charge, which falls under billing.
    
    
    {
      "id": "msg_011CfoNwxiMXWCayWiWZRotX",
      "type": "message",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "**Billing**\n\nThe ticket is about an invoice showing an unexpected charge, which falls under billing."
        }
      ],
      "model": "claude-haiku-5-5",
      "stop_reason": "end_turn",
      "usage": {
        "input_tokens": 40,
        "output_tokens": 35
      },
      "container": null,
      "stop_sequence": null,
      "stop_details": null,
      "diagnostics": null
    }

## Examples

**Structured Extraction** — Use adaptive thinking for structured extraction.
    
    
    const response = await env.AI.run(
      'anthropic/claude-haiku-5.5',
      {
        max_tokens: 1024,
        messages: [{ content: 'Extract the order ID and requested action from: Please cancel order #A-1042 before it ships.', role: 'user' }],
        output_config: { effort: 'medium' },
        thinking: { type: 'adaptive' },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "anthropic/claude-haiku-5.5",
      "max_tokens": 1024,
      "messages": [
        {
          "content": "Extract the order ID and requested action from: Please cancel order #A-1042 before it ships.",
          "role": "user"
        }
      ],
      "output_config": {"effort": "medium"},
      "thinking": {"type": "adaptive"}
    }'
    
    
    **Order ID:** A-1042
    **Requested action:** Cancel the order before it ships
    
    
    {
      "id": "msg_011CfoNx2fFMc8rnUuBBgE3A",
      "type": "message",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "**Order ID:** A-1042\n**Requested action:** Cancel the order before it ships"
        }
      ],
      "model": "claude-haiku-5-5",
      "stop_reason": "end_turn",
      "usage": {
        "input_tokens": 38,
        "output_tokens": 31
      },
      "container": null,
      "stop_sequence": null,
      "stop_details": null,
      "diagnostics": null
    }

**Streaming Response** — Stream a low-latency response incrementally.
    
    
    const response = await env.AI.run(
      'anthropic/claude-haiku-5.5',
      {
        max_tokens: 512,
        messages: [{ content: 'Return a concise three-step deployment checklist.', role: 'user' }],
        stream: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "anthropic/claude-haiku-5.5",
      "max_tokens": 512,
      "messages": [{"content": "Return a concise three-step deployment checklist.", "role": "user"}],
      "stream": true
    }'
    
    
    **Three-Step Deployment Checklist**
    
    1. **Pre-deployment**
       - Confirm all tests pass and code is reviewed and approved.
       - Verify configuration, environment variables, and secrets are set for the target environment.
       - Back up the current production state and prepare a rollback plan.
    
    2. **Deploy**
       - Release to production using the approved pipeline or process, avoiding manual changes where possible.
       - Run database migrations or other required schema changes, if any.
       - Monitor the rollout in stages if supported (e.g., canary or gradual release).
    
    3. **Post-deployment**
       - Run smoke tests on critical paths.
       - Check logs, error rates, and performance metrics against baseline.
       - Notify stakeholders of completion and keep the rollback plan ready for a defined monitoring window.
    
    
    [
      {
        "type": "message_start",
        "message": {
          "model": "claude-haiku-5-5",
          "id": "msg_011CfoNx62eTigAN2u1rkUKg",
          "type": "message",
          "role": "assistant",
          "content": [],
          "container": null,
          "stop_reason": null,
          "stop_sequence": null,
          "stop_details": null,
          "usage": {
            "input_tokens": 23,
            "cache_creation_input_tokens": 0,
            "cache_read_input_tokens": 0,
            "cache_creation": {
              "ephemeral_5m_input_tokens": 0,
              "ephemeral_1h_input_tokens": 0
            },
            "output_tokens": 4,
            "service_tier": "standard",
            "inference_geo": "global"
          },
          "diagnostics": null
        }
      },
      {
        "type": "content_block_start",
        "index": 0,
        "content_block": {
          "type": "thinking",
          "thinking": "",
          "signature": ""
        }
      },
      "... 75 more chunks omitted ...",
      {
        "type": "message_stop"
      }
    ]

## Parameters

▶messages[]

`array`required

max_tokens

`number`requiredexclusiveMinimum: 0

system

`string`

stream

`boolean`

▶metadata{}

`object`

id

`string`

type

`string`const: message

role

`string`const: assistant

▶content[]

`array`

model

`string`

stop_reason

`string`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/anthropic/claude-haiku-5.5/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/anthropic/claude-haiku-5.5/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/anthropic/claude-haiku-5.5/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/anthropic/claude-haiku-5.5/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
