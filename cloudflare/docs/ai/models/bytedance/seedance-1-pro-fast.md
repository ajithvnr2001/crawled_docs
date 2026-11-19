---
url: https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro-fast/
title: Seedance 1.0 Pro Fast (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.075241+00:00
---

# Seedance 1.0 Pro Fast (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro-fast/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedance 1.0 Pro Fast

Text-to-Video • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`bytedance/seedance-1-pro-fast`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



A speed- and cost-optimized variant of Seedance 1.0 Pro, delivering roughly 30-60% faster inference at about 60% lower cost while keeping the same capability surface. Suited to rapid iteration, storyboarding, and platform-scale video workloads.

Model Info|   
---|---  
More information| [link ↗](https://docs.byteplus.com/en/docs/ModelArk/video-generation-tutorial)  
Pricing| 

  * Default (per second)$0.020592
  * @480p (per second)$0.00972
  * @720p (per second)$0.020592
  * @1080p (per second)$0.04896

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1-pro-fast',
      {
        prompt:
          'A bright red electric scooter races through a clean white studio while colorful geometric shapes unfold behind it, energetic commercial lighting, smooth tracking shot',
        aspect_ratio: '16:9',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1-pro-fast",
      "input": {
        "prompt": "A bright red electric scooter races through a clean white studio while colorful geometric shapes unfold behind it, energetic commercial lighting, smooth tracking shot",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1-pro-fast/launch-teaser.mp4"
      }
    }

## Examples

**Vertical Food Clip** — Vertical creator-style food clip
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1-pro-fast',
      {
        prompt:
          'Close-up of a chef slicing a ripe strawberry tart, glossy glaze catching the light, crumbs falling in slow motion, warm bakery background, satisfying social-media food video',
        aspect_ratio: '9:16',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1-pro-fast",
      "input": {
        "prompt": "Close-up of a chef slicing a ripe strawberry tart, glossy glaze catching the light, crumbs falling in slow motion, warm bakery background, satisfying social-media food video",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1-pro-fast/vertical-food-clip.mp4"
      }
    }

**Animated Product Still** — Animate a still image for a rapid social concept
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1-pro-fast',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        prompt:
          'The tea cup rotates slightly as steam curls upward, the camera makes a quick elegant push-in, cozy cafe atmosphere',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1-pro-fast",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "prompt": "The tea cup rotates slightly as steam curls upward, the camera makes a quick elegant push-in, cozy cafe atmosphere",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1-pro-fast/animated-product-still.mp4"
      }
    }

## Parameters

prompt

`string`requiredmaxLength: 10000Text prompt describing the video to generate

image

`string`Reference image (HTTP(S) URL or base64 data URI) for image-to-video

last_frame_image

`string`Reference image (HTTP(S) URL or base64 data URI) for last-frame guidance. Only works if an image start frame is also given.

duration

`integer`requireddefault: 5minimum: 4maximum: 12Video duration in seconds

resolution

`string`requireddefault: 720penum: 480p, 720p, 1080pVideo resolution

aspect_ratio

`string`requireddefault: 16:9enum: 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, 9:21Video aspect ratio. Ignored if an image is used.

fps

`number`requireddefault: 24const: 24Frame rate (frames per second)

camera_fixed

`boolean`requireddefault: falseWhether to fix camera position

watermark

`boolean`requireddefault: falseWhether to add a watermark to the output video

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation

use_virtual_avatar

`boolean`requireddefault: falseRoute image reference inputs (image, reference_images, last_frame_image) through ByteDance's trusted virtual avatar asset library before generation. Intended for AI-generated/virtual character avatars that would otherwise be blocked by face or deepfake detection

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro-fast/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro-fast/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro-fast/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro-fast/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
