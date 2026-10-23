---
url: https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/
title: Jev 1.14 (typesafe) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:58.707847+00:00
---

# Jev 1.14 (typesafe) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



t

# Jev 1.14

Text Generation • typesafe

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`typesafe/jev-1.14.0`

  * Third-party



Jev 1.14 is TypeSafe's structured evaluation model. It evaluates one state against typed Noul, Choice, Score, and Box questions and returns calibrated answers with probabilities and confidence. Image inputs and Box questions are beta and dreamer-ready, not recommended for production.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 32,000 tokens  
Terms and License| [link ↗](https://docs.typesafe.ai/legal.md)  
More information| [link ↗](https://docs.typesafe.ai/models.md)  
Pricing| 

  * Input (per 1M tokens)$0.042
  * Cached input (per 1M tokens)$0.00
  * Output (per 1M tokens)$0.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'typesafe/jev-1.14.0',
      {
        state: { photo: 'black-rectangle' },
        assets: {
          'black-rectangle': {
            type: 'image',
            format: 'png',
            data_base64:
              'iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC',
          },
        },
        questions: { visible: { type: 'noul', instructions: 'Is there a black rectangle in `photo`?' } },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "typesafe/jev-1.14.0",
      "input": {
        "state": {
          "photo": "black-rectangle"
        },
        "assets": {
          "black-rectangle": {
            "type": "image",
            "format": "png",
            "data_base64": "iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC"
          }
        },
        "questions": {
          "visible": {
            "type": "noul",
            "instructions": "Is there a black rectangle in `photo`?"
          }
        }
      }
    }'
    
    
    {
      "model": "jev-1.14.0",
      "answers": {
        "visible": {
          "type": "noul",
          "noul": 0.95
        }
      },
      "usage": {
        "input_tokens": 489,
        "output_tokens": 20
      }
    }

## Examples

**Beta image instructions** — Beta image input: compare a referenced image in instructions
    
    
    const response = await env.AI.run(
      'typesafe/jev-1.14.0',
      {
        state: 'A black rectangle image is attached as black-rectangle.',
        assets: {
          'black-rectangle': {
            type: 'image',
            format: 'png',
            data_base64:
              'iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC',
          },
        },
        questions: {
          visible: { type: 'noul', instructions: 'Does black-rectangle contain a black rectangle?' },
        },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "typesafe/jev-1.14.0",
      "input": {
        "state": "A black rectangle image is attached as black-rectangle.",
        "assets": {
          "black-rectangle": {
            "type": "image",
            "format": "png",
            "data_base64": "iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC"
          }
        },
        "questions": {
          "visible": {
            "type": "noul",
            "instructions": "Does black-rectangle contain a black rectangle?"
          }
        }
      }
    }'
    
    
    {
      "model": "jev-1.14.0",
      "answers": {
        "visible": {
          "type": "noul",
          "noul": 0.98
        }
      },
      "usage": {
        "input_tokens": 694,
        "output_tokens": 20
      }
    }

**Beta Box detection** — Beta Box question: locate the black rectangle
    
    
    const response = await env.AI.run(
      'typesafe/jev-1.14.0',
      {
        state: { photo: 'black-rectangle' },
        assets: {
          'black-rectangle': {
            type: 'image',
            format: 'png',
            data_base64:
              'iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC',
          },
        },
        questions: { rectangle: { type: 'box', instructions: 'Find the black rectangle in `photo`' } },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "typesafe/jev-1.14.0",
      "input": {
        "state": {
          "photo": "black-rectangle"
        },
        "assets": {
          "black-rectangle": {
            "type": "image",
            "format": "png",
            "data_base64": "iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC"
          }
        },
        "questions": {
          "rectangle": {
            "type": "box",
            "instructions": "Find the black rectangle in `photo`"
          }
        }
      }
    }'
    
    
    {
      "model": "jev-1.14.0",
      "answers": {
        "rectangle": {
          "type": "box",
          "box": {
            "top": 0.23,
            "bottom": 0.83,
            "left": 0.14,
            "right": 0.76
          },
          "confidence": 0.74
        }
      },
      "usage": {
        "input_tokens": 487,
        "output_tokens": 20
      }
    }

**Beta Box with visibility check** — Beta Box question: pair location with a visibility check
    
    
    const response = await env.AI.run(
      'typesafe/jev-1.14.0',
      {
        state: { photo: 'black-rectangle' },
        assets: {
          'black-rectangle': {
            type: 'image',
            format: 'png',
            data_base64:
              'iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC',
          },
        },
        questions: {
          visible: { type: 'noul', instructions: 'Is there a black rectangle in `photo`?' },
          rectangle: { type: 'box', instructions: 'Find the black rectangle in `photo`' },
        },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "typesafe/jev-1.14.0",
      "input": {
        "state": {
          "photo": "black-rectangle"
        },
        "assets": {
          "black-rectangle": {
            "type": "image",
            "format": "png",
            "data_base64": "iVBORw0KGgoAAAANSUhEUgAAARgAAAEYAQAAAACv9dQhAAAATklEQVR42u3ZoQ3AMAADwU8X6f47RkpJigqKI52pD5l6rH5zxTAMwzAMwzBMVWtnfpr7rWzIMAzDMAzDMAzDMMzpZvgQGYZhGIZhGKaqB4heFTaRz7VhAAAAAElFTkSuQmCC"
          }
        },
        "questions": {
          "visible": {
            "type": "noul",
            "instructions": "Is there a black rectangle in `photo`?"
          },
          "rectangle": {
            "type": "box",
            "instructions": "Find the black rectangle in `photo`"
          }
        }
      }
    }'
    
    
    {
      "model": "jev-1.14.0",
      "answers": {
        "visible": {
          "type": "noul",
          "noul": 0.95
        },
        "rectangle": {
          "type": "box",
          "box": {
            "top": 0.24,
            "bottom": 0.81,
            "left": 0.15,
            "right": 0.74
          },
          "confidence": 0.74
        }
      },
      "usage": {
        "input_tokens": 504,
        "output_tokens": 36
      }
    }

## Parameters

▶state

`one of`required

▶assets{}

`object`

▶questions{}

`object`required

model

`string`minLength: 1

▶answers{}

`object`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
