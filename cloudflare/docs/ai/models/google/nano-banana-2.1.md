---
url: https://developers.cloudflare.com/ai/models/google/nano-banana-2.1/
title: Nano Banana 2.1 (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:04.080297+00:00
---

# Nano Banana 2.1 (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/nano-banana-2.1/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Nano Banana 2.1

Text-to-Image • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/nano-banana-2.1`

  * Third-party



Google's Nano Banana 2.1 image generation and editing model, optimized for a balance of quality and performance.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 131,072 tokens  
Terms and License| [link ↗](https://ai.google.dev/gemini-api/terms)  
More information| [link ↗](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/nano-banana-2-1)  
Pricing| 

  * Input text (per 1M tokens)$1.50
  * Input image (per 1M tokens)$1.50
  * Output text (per 1M tokens)$7.50
  * Reasoning (per 1M tokens)$7.50
  * Output image (per 1M tokens)$30.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/nano-banana-2.1',
      {
        prompt:
          'A cinematic landscape of a misty mountain valley at sunrise, with warm golden light and dramatic clouds',
        aspect_ratio: '16:9',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2.1",
      "input": {
        "prompt": "A cinematic landscape of a misty mountain valley at sunrise, with warm golden light and dramatic clouds",
        "aspect_ratio": "16:9"
      }
    }'

![Cinematic Landscape](https://examples.aig.cloudflare.com/google/nano-banana-2.1/cinematic-landscape.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2.1/cinematic-landscape.png"
      }
    }

## Examples

**Watercolor Edit** — Edit an image with a text prompt
    
    
    const response = await env.AI.run(
      'google/nano-banana-2.1',
      {
        prompt: 'Turn the scene into a watercolor illustration with soft pastel colors',
        image_input: ['https://storage.googleapis.com/cloud-samples-data/generative-ai/image/scones.jpg'],
        aspect_ratio: 'match_input_image',
        output_format: 'png',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2.1",
      "input": {
        "prompt": "Turn the scene into a watercolor illustration with soft pastel colors",
        "image_input": [
          "https://storage.googleapis.com/cloud-samples-data/generative-ai/image/scones.jpg"
        ],
        "aspect_ratio": "match_input_image",
        "output_format": "png"
      }
    }'

![Watercolor Edit](https://examples.aig.cloudflare.com/google/nano-banana-2.1/watercolor-edit.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2.1/watercolor-edit.png"
      }
    }

**Grounded Travel Poster** — Create a search-grounded travel poster
    
    
    const response = await env.AI.run(
      'google/nano-banana-2.1',
      {
        prompt:
          'A stylish vintage travel poster celebrating the latest landmarks and cultural highlights of Tokyo, with bold Japanese-inspired typography, Mount Fuji in the distance, and a warm limited-color print palette',
        aspect_ratio: '2:3',
        google_search: true,
        output_format: 'jpg',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2.1",
      "input": {
        "prompt": "A stylish vintage travel poster celebrating the latest landmarks and cultural highlights of Tokyo, with bold Japanese-inspired typography, Mount Fuji in the distance, and a warm limited-color print palette",
        "aspect_ratio": "2:3",
        "google_search": true,
        "output_format": "jpg"
      }
    }'

![Grounded Travel Poster](https://examples.aig.cloudflare.com/google/nano-banana-2.1/grounded-travel-poster.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2.1/grounded-travel-poster.jpg"
      }
    }

**Editorial Product Campaign** — Create a polished product campaign image from a reference
    
    
    const response = await env.AI.run(
      'google/nano-banana-2.1',
      {
        prompt:
          'Transform this product photo into a premium editorial campaign image on a sculptural stone pedestal, with soft studio lighting, deep emerald accents, realistic shadows, and a clean luxury magazine aesthetic',
        image_input: [
          'https://storage.googleapis.com/cloud-samples-data/generative-ai/image/320px-Felis_catus-cat_on_snow.jpg',
        ],
        aspect_ratio: '4:5',
        output_format: 'jpg',
        resolution: '2K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2.1",
      "input": {
        "prompt": "Transform this product photo into a premium editorial campaign image on a sculptural stone pedestal, with soft studio lighting, deep emerald accents, realistic shadows, and a clean luxury magazine aesthetic",
        "image_input": [
          "https://storage.googleapis.com/cloud-samples-data/generative-ai/image/320px-Felis_catus-cat_on_snow.jpg"
        ],
        "aspect_ratio": "4:5",
        "output_format": "jpg",
        "resolution": "2K"
      }
    }'

![Editorial Product Campaign](https://examples.aig.cloudflare.com/google/nano-banana-2.1/editorial-product-campaign.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2.1/editorial-product-campaign.jpg"
      }
    }

## Parameters

prompt

`string`required

▶image_input[]

`array`maxItems: 3

aspect_ratio

`string`enum: match_input_image, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

output_format

`string`enum: jpg, png

resolution

`string`enum: 1K, 2K, 4K

google_search

`boolean`

image_search

`boolean`

image

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/nano-banana-2.1/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-2.1/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/nano-banana-2.1/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-2.1/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
