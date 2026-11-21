---
url: https://developers.cloudflare.com/ai/models/bytedance/seedream-5.5/
title: Seedream 5.5 (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:30.198121+00:00
---

# Seedream 5.5 (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedream-5.5/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedream 5.5

Text-to-Image • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`bytedance/seedream-5.5`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party
  * Zero data retention



Seedream 5.5 is ByteDance's image generation and editing model with text prompts, up to 10 reference images, 1K, 1.5K, 2K, or custom pixel-size output, PNG or JPEG output, and native transparent backgrounds.

Model Info|   
---|---  
More information| [link ↗](https://docs.byteplus.com/en/docs/modelark/seedream-5-5)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.035
  * output size 1k$0.02
  * output size 2k$0.035
  * Per input image$0.008

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedream-5.5',
      {
        prompt:
          'A transparent acrylic standee with a Christmas theme and a thin white edge. Scrapbook collage style: a red-and-green vinyl record with a golden rim at the center, surrounded by a wreath of pine branches, red berries, golden stars and snowflake stickers. A minimalist white music-player UI below with a progress bar (01:24 / 04:32). Transparent background.',
        background: 'transparent',
        output_format: 'png',
        size: '2K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-5.5",
      "input": {
        "prompt": "A transparent acrylic standee with a Christmas theme and a thin white edge. Scrapbook collage style: a red-and-green vinyl record with a golden rim at the center, surrounded by a wreath of pine branches, red berries, golden stars and snowflake stickers. A minimalist white music-player UI below with a progress bar (01:24 / 04:32). Transparent background.",
        "background": "transparent",
        "output_format": "png",
        "size": "2K"
      }
    }'

![Transparent Acrylic Standee](https://examples.aig.cloudflare.com/bytedance/seedream-5.5/transparent-acrylic-standee-0.png)
    
    
    {
      "state": "Completed",
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/bytedance/seedream-5.5/transparent-acrylic-standee-0.png"
        ]
      }
    }

## Examples

**Extract Stickers from Two Images** — Multi-reference input with transparent output: pull the stickers out of two images into one PNG.
    
    
    const response = await env.AI.run(
      'bytedance/seedream-5.5',
      {
        prompt:
          "Extract the sticker elements from Image 1 and Image 2, then place all of them in one transparent-background image. Keep each sticker's text, colors and shapes, remove everything else, and arrange them without overlap with sharp edges.",
        image: [
          'https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/ocr-test3.png',
          'https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/ocr-test4.png',
        ],
        background: 'transparent',
        output_format: 'png',
        size: '2K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-5.5",
      "input": {
        "prompt": "Extract the sticker elements from Image 1 and Image 2, then place all of them in one transparent-background image. Keep each sticker'\''s text, colors and shapes, remove everything else, and arrange them without overlap with sharp edges.",
        "image": [
          "https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/ocr-test3.png",
          "https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/ocr-test4.png"
        ],
        "background": "transparent",
        "output_format": "png",
        "size": "2K"
      }
    }'

![Extract Stickers from Two Images](https://examples.aig.cloudflare.com/bytedance/seedream-5.5/extract-stickers-from-two-images-0.png)
    
    
    {
      "state": "Completed",
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/bytedance/seedream-5.5/extract-stickers-from-two-images-0.png"
        ]
      }
    }

**Consistent Portrait Edit** — Edit a portrait while keeping the person's identity, pose and style.
    
    
    const response = await env.AI.run(
      'bytedance/seedream-5.5',
      {
        prompt:
          'Have the person blow a round, semi-transparent pink bubblegum bubble. Keep the identity, facial features, gaze, hairstyle, pearl earrings, clothing, pose, blue background and composition unchanged.',
        image:
          'https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/seedream-5-5-multi-round-editing-input.png',
        background: 'opaque',
        output_format: 'png',
        size: '2K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-5.5",
      "input": {
        "prompt": "Have the person blow a round, semi-transparent pink bubblegum bubble. Keep the identity, facial features, gaze, hairstyle, pearl earrings, clothing, pose, blue background and composition unchanged.",
        "image": "https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/seedream-5-5-multi-round-editing-input.png",
        "background": "opaque",
        "output_format": "png",
        "size": "2K"
      }
    }'

![Consistent Portrait Edit](https://examples.aig.cloudflare.com/bytedance/seedream-5.5/consistent-portrait-edit-0.png)
    
    
    {
      "state": "Completed",
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/bytedance/seedream-5.5/consistent-portrait-edit-0.png"
        ]
      }
    }

**Widescreen JPEG** — Custom pixel size with JPEG output.
    
    
    const response = await env.AI.run(
      'bytedance/seedream-5.5',
      {
        prompt:
          'A dramatic mountain lake at sunrise, mist over the water, cinematic landscape photography',
        size: '1664x936',
        output_format: 'jpeg',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-5.5",
      "input": {
        "prompt": "A dramatic mountain lake at sunrise, mist over the water, cinematic landscape photography",
        "size": "1664x936",
        "output_format": "jpeg"
      }
    }'

![Widescreen JPEG](https://examples.aig.cloudflare.com/bytedance/seedream-5.5/widescreen-jpeg-0.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/bytedance/seedream-5.5/widescreen-jpeg-0.jpeg"
        ]
      }
    }

## Parameters

prompt

`string`requiredText prompt describing the image to generate or the edit to make

▶image

`one of`

size

`string`Output size: 1K, 1.5K, 2K, or WIDTHxHEIGHT (921,600-4,624,220 total pixels)

output_format

`string`enum: png, jpegOutput image format. Provider default is png.

background

`string`enum: auto, transparent, opaqueBackground handling. "transparent" returns an RGBA PNG and requires png output.

watermark

`boolean`requireddefault: falseWhether to add an AI-generated watermark to the output image

▶images[]

`array`minItems: 1format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5.5/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5.5/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5.5/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5.5/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
