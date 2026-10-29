---
url: https://developers.cloudflare.com/ai/models/klingai/kling-v3-image/
title: Kling v3 Image (Kling AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.185985+00:00
---

# Kling v3 Image (Kling AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/klingai/kling-v3-image/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Kling AI logo](https://developers.cloudflare.com/_astro/kling.CbZKRtvH.svg)

# Kling v3 Image

Text-to-Image • Kling AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`klingai/kling-v3-image`

  * Third-party



Kling V3 Image is Kling AI's text-to-image model for photorealistic image generation.

Model Info|   
---|---  
Terms and License| [link ↗](https://klingai.com/terms)  
More information| [link ↗](https://klingai.com/)  
Pricing| 

  * Per image$0.027

  
  
## Usage
    
    
    const response = await env.AI.run(
      'klingai/kling-v3-image',
      {
        prompt:
          'A photorealistic portrait of a fox in an autumn forest, golden hour lighting',
        resolution: '1k',
        aspect_ratio: '16:9',
      },
      {
        gateway: { id: 'default' },
      }
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "klingai/kling-v3-image",
      "input": {
        "aspect_ratio": "16:9",
        "prompt": "A photorealistic portrait of a fox in an autumn forest, golden hour lighting",
        "resolution": "1k"
      }
    }'

![Simple Generation](https://examples.aig.cloudflare.com/klingai/kling-v3-image/simple-generation.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/klingai/kling-v3-image/simple-generation.png"
      }
    }

## Parameters

prompt

`string`requiredText prompt describing the image to generate

negative_prompt

`string`Negative text prompt

image

`string`Reference image (Base64 encoding or URL) for image-to-image

resolution

`string`requireddefault: 1kenum: 1k, 2kImage generation resolution (1k: standard, 2k: high-res)

aspect_ratio

`string`requireddefault: 16:9enum: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9Aspect ratio of generated images

image

`string`URL to the generated image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-image/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-image/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-image/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-image/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
