---
url: https://developers.cloudflare.com/ai/models/openai/decisions/
title: Decisions (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:52.722314+00:00
---

# Decisions (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/decisions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# Decisions

Text Generation • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/decisions`

  * Third-party



Decisions uses GPT-6 Luna to evaluate shared text or image evidence against typed questions. It returns probabilities, fixed choices, or rubric scores for low-latency classification, routing, and prioritization workflows.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,050,000 tokens  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://developers.openai.com/api/docs/guides/decisions)  
Pricing| 

  * Input (per 1M tokens)$0.10
  * Output (per 1M tokens)$0.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/decisions',
      {
        input: 'The customer reports that their card was charged twice for one order.',
        questions: [
          {
            instructions: 'Is this report about a billing problem?',
            name: 'billing_issue',
            type: 'predicate',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/decisions",
      "input": {
        "input": "The customer reports that their card was charged twice for one order.",
        "questions": [
          {
            "instructions": "Is this report about a billing problem?",
            "name": "billing_issue",
            "type": "predicate"
          }
        ]
      }
    }'
    
    
    {
      "model": "gpt-6-luna",
      "answers": [
        {
          "type": "predicate",
          "name": "billing_issue",
          "probability": 1
        }
      ],
      "usage": {
        "input_tokens": 169,
        "input_tokens_details": {
          "cached_tokens": 0,
          "cache_write_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 169
      }
    }

## Examples

**Select a category** — Route a customer request to one of several departments
    
    
    const response = await env.AI.run(
      'openai/decisions',
      {
        input: 'My package was expected yesterday, but tracking has not updated.',
        questions: [
          {
            choices: [
              { description: 'Payments, invoices, and refunds.', value: 'billing' },
              { description: 'Problems using the product.', value: 'technical' },
              { description: 'Delivery and tracking.', value: 'shipping' },
              { description: 'Requests outside these categories.', value: 'other' },
            ],
            instructions: 'Which department should handle this request?',
            name: 'department',
            type: 'choice',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/decisions",
      "input": {
        "input": "My package was expected yesterday, but tracking has not updated.",
        "questions": [
          {
            "choices": [
              {
                "description": "Payments, invoices, and refunds.",
                "value": "billing"
              },
              {
                "description": "Problems using the product.",
                "value": "technical"
              },
              {
                "description": "Delivery and tracking.",
                "value": "shipping"
              },
              {
                "description": "Requests outside these categories.",
                "value": "other"
              }
            ],
            "instructions": "Which department should handle this request?",
            "name": "department",
            "type": "choice"
          }
        ]
      }
    }'
    
    
    {
      "model": "gpt-6-luna",
      "answers": [
        {
          "type": "choice",
          "name": "department",
          "choice": "shipping",
          "probabilities": [
            {
              "value": "billing",
              "probability": 0
            },
            {
              "value": "technical",
              "probability": 0.01
            },
            {
              "value": "shipping",
              "probability": 0.99
            },
            {
              "value": "other",
              "probability": 0
            }
          ],
          "confidence": 0.99
        }
      ],
      "usage": {
        "input_tokens": 149,
        "input_tokens_details": {
          "cached_tokens": 0,
          "cache_write_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 149
      }
    }

**Score against a rubric** — Score an issue against ordered severity levels
    
    
    const response = await env.AI.run(
      'openai/decisions',
      {
        input: 'Export fails in Safari but works in Chrome.',
        questions: [
          {
            instructions: 'How severe is this issue?',
            levels: [
              { description: 'Appearance only; no lost functionality.', label: 'Cosmetic' },
              { description: 'A task fails, but another way works.', label: 'Workaround available' },
              { description: 'A task fails with no workaround.', label: 'Fully blocked' },
            ],
            name: 'severity',
            type: 'score',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/decisions",
      "input": {
        "input": "Export fails in Safari but works in Chrome.",
        "questions": [
          {
            "instructions": "How severe is this issue?",
            "levels": [
              {
                "description": "Appearance only; no lost functionality.",
                "label": "Cosmetic"
              },
              {
                "description": "A task fails, but another way works.",
                "label": "Workaround available"
              },
              {
                "description": "A task fails with no workaround.",
                "label": "Fully blocked"
              }
            ],
            "name": "severity",
            "type": "score"
          }
        ]
      }
    }'
    
    
    {
      "model": "gpt-6-luna",
      "answers": [
        {
          "type": "score",
          "name": "severity",
          "score": 0.99,
          "probabilities": [
            {
              "value": 0,
              "label": "Cosmetic",
              "probability": 0.02
            },
            {
              "value": 1,
              "label": "Workaround available",
              "probability": 0.97
            },
            {
              "value": 2,
              "label": "Fully blocked",
              "probability": 0.01
            }
          ],
          "confidence": 0.96
        }
      ],
      "usage": {
        "input_tokens": 146,
        "input_tokens_details": {
          "cached_tokens": 0,
          "cache_write_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 146
      }
    }

## Parameters

▶input

`one of`required

▶questions[]

`array`requiredminItems: 1maxItems: 200

prompt_cache_key

`string`

prompt_cache_options

`object | null`

safety_identifier

`string`

▶answers[]

`array`

model

`string`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/decisions/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/decisions/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/decisions/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/decisions/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
