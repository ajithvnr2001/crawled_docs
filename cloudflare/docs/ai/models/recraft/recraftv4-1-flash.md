---
url: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-flash/
title: Recraft V4.1 Flash (Recraft) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:59.574071+00:00
---

# Recraft V4.1 Flash (Recraft) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-flash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Flash

Text-to-Image • Recraft

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-flash`

  * Third-party



Recraft V4.1 Flash is Recraft's fastest and lowest-cost image model, generating a 1K raster image in about 1.3 seconds with quality close to Recraft V4.1. Built for high-volume generation and rapid iteration, with strong results for photography, portraits, atmospheric scenes, mixed media, and logo concepts. It outputs raster images only and does not support styles.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.recraft.ai/terms)  
More information| [link ↗](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1-flash)  
Pricing| 

  * Per image$0.007

  
  
## Usage
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-flash',
      { prompt: 'A minimalist logo of a mountain range with a sun rising behind it' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-flash",
      "input": {
        "prompt": "A minimalist logo of a mountain range with a sun rising behind it"
      }
    }'

![Simple Generation](https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/simple-generation.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/simple-generation.png"
      }
    }

## Examples

**Portrait Photo** — Generate a portrait photo with an aspect ratio
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-flash',
      { prompt: 'Portrait of an old fisherman, golden hour, film photo', size: '4:5' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-flash",
      "input": {
        "prompt": "Portrait of an old fisherman, golden hour, film photo",
        "size": "4:5"
      }
    }'

![Portrait Photo](https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/portrait-photo.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/portrait-photo.png"
      }
    }

**Custom Size** — Specify exact output dimensions
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-flash',
      {
        prompt: 'A flat illustration of a workspace with a laptop, coffee cup, and potted plant',
        size: '1344x768',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-flash",
      "input": {
        "prompt": "A flat illustration of a workspace with a laptop, coffee cup, and potted plant",
        "size": "1344x768"
      }
    }'

![Custom Size](https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/custom-size.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/custom-size.png"
      }
    }

**With Color Controls** — Guide generation with specific brand colors
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-flash',
      {
        prompt: 'An abstract geometric pattern suitable for a tech company brand identity',
        controls: { colors: [{ rgb: [255, 107, 53] }, { rgb: [0, 43, 91] }] },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-flash",
      "input": {
        "prompt": "An abstract geometric pattern suitable for a tech company brand identity",
        "controls": {
          "colors": [
            {
              "rgb": [
                255,
                107,
                53
              ]
            },
            {
              "rgb": [
                0,
                43,
                91
              ]
            }
          ]
        }
      }
    }'

![With Color Controls](https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/with-color-controls.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/with-color-controls.png"
      }
    }

**Background Color** — Set a specific background color
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-flash',
      {
        prompt: 'A clean icon of a lightning bolt',
        controls: { background_color: { rgb: [245, 245, 245] } },
        size: '1:1',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-flash",
      "input": {
        "prompt": "A clean icon of a lightning bolt",
        "controls": {
          "background_color": {
            "rgb": [
              245,
              245,
              245
            ]
          }
        },
        "size": "1:1"
      }
    }'

![Background Color](https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/background-color.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-1-flash/background-color.png"
      }
    }

## Parameters

prompt

`string`required

size

`string`

▶controls{}

`object`

image

`string`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-flash/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-flash/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-flash/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-flash/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
