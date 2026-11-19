---
url: https://developers.cloudflare.com/ai/models/google/gemini-decision-1/
title: Gemini Decision 1 (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:03.984543+00:00
---

# Gemini Decision 1 (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/gemini-decision-1/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Gemini Decision 1

Text Generation • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`google/gemini-decision-1`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party
  * Zero data retention



Gemini Decision 1 evaluates typed questions over shared text, images, audio, video, and PDFs. It returns calibrated yes/no probabilities, choices, and rubric scores for classification, routing, and ranking, with zero output tokens.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 262,144 tokens  
Terms and License| [link ↗](https://aistudio.google.com/docs/terms)  
More information| [link ↗](https://aistudio.google.com/docs/models/gemini-decision-1)  
Zero data retention| Yes  
Pricing| 

  * Input (per 1M tokens)$0.10
  * Output (per 1M tokens)$0.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/gemini-decision-1',
      {
        input: 'The blue mug I ordered on Monday arrived cracked on Wednesday.',
        questions: { is_damaged: { type: 'noul', instructions: 'Did the item arrive damaged?' } },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-decision-1",
      "input": {
        "input": "The blue mug I ordered on Monday arrived cracked on Wednesday.",
        "questions": {
          "is_damaged": {
            "type": "noul",
            "instructions": "Did the item arrive damaged?"
          }
        }
      }
    }'
    
    
    {
      "answers": {
        "is_damaged": {
          "confidence": 0.99,
          "noul": 0.99,
          "type": "noul"
        }
      },
      "usage": {
        "total_tokens": 100,
        "total_input_tokens": 100,
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 100
          }
        ],
        "total_output_tokens": 0
      }
    }

## Examples

**Route and score a support ticket** — Ask independent yes/no, choice, and score questions over the same input.
    
    
    const response = await env.AI.run(
      'google/gemini-decision-1',
      {
        input: [
          { type: 'text', text: 'Customer tier: Gold. Order: headphones, $240.\n' },
          {
            type: 'text',
            text: 'Audio cuts out on the left earcup. Fix it today or I cancel my membership.',
          },
        ],
        questions: {
          is_defect: {
            type: 'noul',
            instructions: 'Is the customer reporting a hardware defect?',
            criteria: {
              true_description: 'The product itself is broken or faulty.',
              false_description: 'A preference, sizing, shipping, or pricing complaint.',
            },
          },
          department: {
            type: 'choice',
            instructions: 'Which department should handle this request?',
            criteria: {
              billing: 'Payments, invoices, and refunds.',
              technical: 'Problems using the product or hardware faults.',
              shipping: 'Delivery and tracking.',
              other: 'Anything outside these categories.',
            },
          },
          churn_risk: {
            type: 'score',
            instructions: 'How likely is the customer to churn if this issue is not resolved?',
            criteria: [
              'No churn signal',
              'Mild frustration',
              'Mentions alternatives',
              'Threatens to cancel',
            ],
          },
        },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-decision-1",
      "input": {
        "input": [
          {
            "type": "text",
            "text": "Customer tier: Gold. Order: headphones, $240.\n"
          },
          {
            "type": "text",
            "text": "Audio cuts out on the left earcup. Fix it today or I cancel my membership."
          }
        ],
        "questions": {
          "is_defect": {
            "type": "noul",
            "instructions": "Is the customer reporting a hardware defect?",
            "criteria": {
              "true_description": "The product itself is broken or faulty.",
              "false_description": "A preference, sizing, shipping, or pricing complaint."
            }
          },
          "department": {
            "type": "choice",
            "instructions": "Which department should handle this request?",
            "criteria": {
              "billing": "Payments, invoices, and refunds.",
              "technical": "Problems using the product or hardware faults.",
              "shipping": "Delivery and tracking.",
              "other": "Anything outside these categories."
            }
          },
          "churn_risk": {
            "type": "score",
            "instructions": "How likely is the customer to churn if this issue is not resolved?",
            "criteria": [
              "No churn signal",
              "Mild frustration",
              "Mentions alternatives",
              "Threatens to cancel"
            ]
          }
        }
      }
    }'
    
    
    {
      "answers": {
        "churn_risk": {
          "confidence": 0.9871029342727191,
          "score": 2.9847557447368054,
          "probabilities": {
            "0": 0.00024958590912331545,
            "1": 0.001848017717667642,
            "2": 0.01079946210049003,
            "3": 0.9871029342727191
          },
          "legend": {
            "0": "No churn signal",
            "1": "Mild frustration",
            "2": "Mentions alternatives",
            "3": "Threatens to cancel"
          },
          "type": "score"
        },
        "is_defect": {
          "confidence": 0.9740036578099637,
          "noul": 0.9740036578099637,
          "type": "noul"
        },
        "department": {
          "confidence": 0.9785049522314109,
          "choice": "technical",
          "probabilities": {
            "technical": 0.9785049522314109,
            "billing": 0.006229438550145094,
            "other": 0.013127015151353486,
            "shipping": 0.0021385940670906965
          },
          "type": "choice"
        }
      },
      "usage": {
        "total_tokens": 315,
        "total_input_tokens": 315,
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 315
          }
        ],
        "total_output_tokens": 0
      }
    }

**Evaluate an audio recording** — Evaluate spoken content and delivery directly from an audio URL.
    
    
    const response = await env.AI.run(
      'google/gemini-decision-1',
      {
        input: {
          type: 'audio',
          uri: 'https://storage.googleapis.com/generativeai-downloads/audio/rehearsing.wav',
          mime_type: 'audio/wav',
        },
        questions: {
          mentions_launch: {
            type: 'noul',
            instructions: 'Is the speaker talking about a product campaign launch?',
          },
          delivery: {
            type: 'score',
            instructions: 'How fluent and prepared does the speaker sound?',
            criteria: [
              'Hesitant, searching for notes, or self-correcting.',
              'Mostly steady with minor pauses.',
              'Polished, fluent, and confident throughout.',
            ],
          },
        },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-decision-1",
      "input": {
        "input": {
          "type": "audio",
          "uri": "https://storage.googleapis.com/generativeai-downloads/audio/rehearsing.wav",
          "mime_type": "audio/wav"
        },
        "questions": {
          "mentions_launch": {
            "type": "noul",
            "instructions": "Is the speaker talking about a product campaign launch?"
          },
          "delivery": {
            "type": "score",
            "instructions": "How fluent and prepared does the speaker sound?",
            "criteria": [
              "Hesitant, searching for notes, or self-correcting.",
              "Mostly steady with minor pauses.",
              "Polished, fluent, and confident throughout."
            ]
          }
        }
      }
    }'
    
    
    {
      "answers": {
        "delivery": {
          "confidence": 0.8753272828029849,
          "score": 0.13564676347359578,
          "probabilities": {
            "0": 0.8753272828029849,
            "1": 0.11369867092043455,
            "2": 0.010974046276580619
          },
          "legend": {
            "0": "Hesitant, searching for notes, or self-correcting.",
            "1": "Mostly steady with minor pauses.",
            "2": "Polished, fluent, and confident throughout."
          },
          "type": "score"
        },
        "mentions_launch": {
          "confidence": 0.9023548793133858,
          "noul": 0.9023548793133858,
          "type": "noul"
        }
      },
      "usage": {
        "total_tokens": 2147,
        "total_input_tokens": 2147,
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 298
          },
          {
            "modality": "audio",
            "tokens": 1849
          }
        ],
        "total_output_tokens": 0
      }
    }

## Parameters

▶input

`one of`required

▶questions{}

`object`required

▶answers{}

`object`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/gemini-decision-1/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-decision-1/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/gemini-decision-1/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-decision-1/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
