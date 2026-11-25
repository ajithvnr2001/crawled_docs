---
url: https://developers.cloudflare.com/ai/models/pruna/z-image-turbo/
title: Z-Image Turbo (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.345952+00:00
---

# Z-Image Turbo (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/z-image-turbo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# Z-Image Turbo

Text-to-Image • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`pruna/z-image-turbo`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Z-Image Turbo is Tongyi-MAI's 6B-parameter distilled text-to-image model, served by Pruna. It generates photorealistic images in about 8 steps, renders English and Chinese text well, and supports custom sizes up to 2048×2048.

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/models/z-image-turbo)  
Pricing| 

  * Per image$0.005

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/z-image-turbo',
      { prompt: 'A red fox curled up asleep in fresh snow, soft morning light, photorealistic' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/z-image-turbo",
      "input": {
        "prompt": "A red fox curled up asleep in fresh snow, soft morning light, photorealistic"
      }
    }'

![Fox in the Snow](https://examples.aig.cloudflare.com/pruna/z-image-turbo/fox-in-the-snow.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/z-image-turbo/fox-in-the-snow.jpg"
      }
    }

## Examples

**Bilingual Neon Sign** — Renders Chinese and English text in the same image, wide format, PNG.
    
    
    const response = await env.AI.run(
      'pruna/z-image-turbo',
      {
        prompt:
          'A rainy night street in Shanghai, a glowing neon sign that reads "营业中 OPEN LATE" in red Chinese characters and blue English letters, reflections on wet pavement, cinematic',
        width: 1440,
        height: 768,
        output_format: 'png',
        seed: 42,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/z-image-turbo",
      "input": {
        "prompt": "A rainy night street in Shanghai, a glowing neon sign that reads \"营业中 OPEN LATE\" in red Chinese characters and blue English letters, reflections on wet pavement, cinematic",
        "width": 1440,
        "height": 768,
        "output_format": "png",
        "seed": 42
      }
    }'

![Bilingual Neon Sign](https://examples.aig.cloudflare.com/pruna/z-image-turbo/bilingual-neon-sign.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/z-image-turbo/bilingual-neon-sign.png"
      }
    }

**Fast Product Shot** — Studio product photo with go_fast for the lowest latency.
    
    
    const response = await env.AI.run(
      'pruna/z-image-turbo',
      {
        prompt:
          'Studio product photo of a matte black wireless earbud case on a white marble pedestal, soft rim light, shallow depth of field',
        go_fast: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/z-image-turbo",
      "input": {
        "prompt": "Studio product photo of a matte black wireless earbud case on a white marble pedestal, soft rim light, shallow depth of field",
        "go_fast": true
      }
    }'

![Fast Product Shot](https://examples.aig.cloudflare.com/pruna/z-image-turbo/fast-product-shot.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/z-image-turbo/fast-product-shot.jpg"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1Text description of the image to generate.

width

`integer`minimum: 64maximum: 2048Width of the generated image in pixels (64-2048). Defaults to 1024.

height

`integer`minimum: 64maximum: 2048Height of the generated image in pixels (64-2048). Defaults to 1024.

num_inference_steps

`integer`minimum: 1maximum: 50Number of inference steps (1-50). Defaults to 8.

guidance_scale

`number`minimum: 0maximum: 20Guidance scale (0-20). Should be 0 for Turbo models, which is the default.

go_fast

`boolean`Apply additional optimizations for faster generation. Defaults to false.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

output_format

`string`enum: jpg, png, webpFormat of the output image. Defaults to jpg.

output_quality

`integer`minimum: 0maximum: 100Quality when saving jpg or webp output, from 0 to 100. Defaults to 80.

enable_safety_filter

`boolean`Check the prompt against the content policy. Defaults to false; the always-on categories are still blocked.

image

`string`format: uriPresigned URL for the generated image.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/z-image-turbo/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/z-image-turbo/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/z-image-turbo/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/z-image-turbo/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
