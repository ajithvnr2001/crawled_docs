---
url: https://developers.cloudflare.com/ai/models/klingai/kling-v4-image/
title: Kling Image 4.0 (Kling AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.207368+00:00
---

# Kling Image 4.0 (Kling AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/klingai/kling-v4-image/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Kling AI logo](https://developers.cloudflare.com/_astro/kling.CbZKRtvH.svg)

# Kling Image 4.0

Text-to-Image • Kling AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`klingai/kling-v4-image`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Kling Image 4.0 is Kling AI's latest image model, generating 2K images from a text prompt and up to 10 reference images, in nine aspect ratios including auto.

Model Info|   
---|---  
Terms and License| [link ↗](https://klingai.com/terms)  
More information| [link ↗](https://kling.ai/document-api)  
Pricing| 

  * Per image$0.063
  * Per input image$0.003

  
  
## Usage
    
    
    const response = await env.AI.run(
      'klingai/kling-v4-image',
      {
        prompt:
          'A photorealistic portrait of a fox in an autumn forest, golden hour lighting',
        resolution: '2k',
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
      "model": "klingai/kling-v4-image",
      "input": {
        "aspect_ratio": "16:9",
        "prompt": "A photorealistic portrait of a fox in an autumn forest, golden hour lighting",
        "resolution": "2k"
      }
    }'

![Simple Generation](https://examples.aig.cloudflare.com/klingai/kling-v4-image/simple-generation.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/klingai/kling-v4-image/simple-generation.png",
        "images": [
          "https://examples.aig.cloudflare.com/klingai/kling-v4-image/simple-generation.png"
        ]
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 50000Text prompt describing the image, up to 50,000 English characters. Refer to reference images as @image_1, @image_2, and so on.

▶images[]

`array`maxItems: 10Reference images for image-to-image: https URLs, data URIs or raw base64 (JPG or PNG, up to 30 MB, at least 300 px per side, aspect ratio between 2:5 and 5:2)

n

`integer`requireddefault: 1minimum: 1maximum: 9Number of images to generate

resolution

`string`requireddefault: 2kenum: 2kOutput resolution

aspect_ratio

`string`requireddefault: autoenum: auto, 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9Aspect ratio of the generated image; auto picks one from the input

image

`string`URL to the first generated image

▶images[]

`array`URLs to all generated images

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-image/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-image/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-image/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-image/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
