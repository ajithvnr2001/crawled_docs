---
url: https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro/
title: Seedance 1.0 Pro (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.027640+00:00
---

# Seedance 1.0 Pro (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedance 1.0 Pro

Text-to-Video • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`bytedance/seedance-1-pro`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



ByteDance's first-generation cinematic video model. Generates 1080p video from text or images with strong prompt adherence, stable motion, and native multi-shot narrative coherence. Supports first/last-frame image-to-video and image references.

Model Info|   
---|---  
More information| [link ↗](https://docs.byteplus.com/en/docs/ModelArk/video-generation-tutorial)  
Pricing| 

  * Default (per second)$0.05148
  * @480p (per second)$0.0243
  * @720p (per second)$0.05148
  * @1080p (per second)$0.1224

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1-pro',
      {
        prompt:
          'A handcrafted mechanical watch rests on black volcanic stone as a narrow beam of morning light moves across its polished steel case, macro cinematography, slow orbiting camera, crisp reflections',
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
      "model": "bytedance/seedance-1-pro",
      "input": {
        "prompt": "A handcrafted mechanical watch rests on black volcanic stone as a narrow beam of morning light moves across its polished steel case, macro cinematography, slow orbiting camera, crisp reflections",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1-pro/product-film.mp4"
      }
    }

## Examples

**Aerial Landscape** — Cinematic 1080p nature sequence with an aerial camera move
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1-pro',
      {
        prompt:
          'An aerial camera glides over a winding river through an autumn forest at dawn, low clouds drifting between amber trees, cinematic color grading, smooth forward movement',
        aspect_ratio: '16:9',
        duration: 5,
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1-pro",
      "input": {
        "prompt": "An aerial camera glides over a winding river through an autumn forest at dawn, low clouds drifting between amber trees, cinematic color grading, smooth forward movement",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "1080p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1-pro/aerial-landscape.mp4"
      }
    }

**First Frame Animation** — Animate a still image as the first frame of the video
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1-pro',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        prompt:
          'Steam rises gently from the cup while the camera slowly pushes in, soft afternoon window light, calm and natural movement',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1-pro",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "prompt": "Steam rises gently from the cup while the camera slowly pushes in, soft afternoon window light, calm and natural movement",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1-pro/first-frame-animation.mp4"
      }
    }

**Vertical Fashion Editorial** — Vertical fashion editorial for social video formats
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1-pro',
      {
        prompt:
          'A fashion editor walks through a sunlit greenhouse in a flowing emerald dress, leaves sway in a soft breeze, editorial photography, subtle handheld camera motion',
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
      "model": "bytedance/seedance-1-pro",
      "input": {
        "prompt": "A fashion editor walks through a sunlit greenhouse in a flowing emerald dress, leaves sway in a soft breeze, editorial photography, subtle handheld camera motion",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1-pro/vertical-fashion-editorial.mp4"
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

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
