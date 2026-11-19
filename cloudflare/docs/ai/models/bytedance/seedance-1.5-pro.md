---
url: https://developers.cloudflare.com/ai/models/bytedance/seedance-1.5-pro/
title: Seedance 1.5 Pro (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:03.877445+00:00
---

# Seedance 1.5 Pro (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedance-1.5-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedance 1.5 Pro

Text-to-Video • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`bytedance/seedance-1.5-pro`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



ByteDance's joint audio-video model. A dual-branch diffusion transformer generates synchronized native audio and video in a single pass, giving millisecond-precision lip-sync across English, Mandarin, Japanese, Korean, Spanish, Portuguese, Indonesian, and Chinese dialects, plus cinematic camera control and character consistency at up to 1080p.

Model Info|   
---|---  
More information| [link ↗](https://seed.bytedance.com/en/seedance1_5_pro)  
Pricing| 

  * Default (per second)$0.0247104
  * @480p (per second)$0.011664
  * @720p (per second)$0.0247104
  * @1080p (per second)$0.058752
  * @480p w/ audio (per second)$0.023328
  * @720p w/ audio (per second)$0.0494208
  * @1080p w/ audio (per second)$0.117504

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1.5-pro',
      {
        prompt:
          'A small sailboat crosses a glassy lake beneath the northern lights, its reflection rippling softly in the dark water, wide cinematic shot, tranquil atmosphere',
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
      "model": "bytedance/seedance-1.5-pro",
      "input": {
        "prompt": "A small sailboat crosses a glassy lake beneath the northern lights, its reflection rippling softly in the dark water, wide cinematic shot, tranquil atmosphere",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1.5-pro/aurora-on-the-lake.mp4"
      }
    }

## Examples

**Spoken Workshop Scene** — Joint audio-video generation with an expressive spoken performance
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1.5-pro',
      {
        prompt:
          "A young scientist in a bright workshop looks at the camera and says, 'Every small experiment brings us closer to a better future,' then smiles as a tiny robot rolls across the desk, natural conversational delivery, warm room tone",
        aspect_ratio: '16:9',
        duration: 5,
        generate_audio: true,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1.5-pro",
      "input": {
        "prompt": "A young scientist in a bright workshop looks at the camera and says, '\''Every small experiment brings us closer to a better future,'\'' then smiles as a tiny robot rolls across the desk, natural conversational delivery, warm room tone",
        "aspect_ratio": "16:9",
        "duration": 5,
        "generate_audio": true,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1.5-pro/spoken-workshop-scene.mp4"
      }
    }

**Jazz Performance** — High-resolution music-performance scene with synchronized native audio
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1.5-pro',
      {
        prompt:
          'A jazz pianist plays an intimate melody in a dimly lit club, fingers moving across the keys as the camera slowly circles the grand piano, warm amber spotlights, natural piano music and room ambience',
        aspect_ratio: '16:9',
        duration: 5,
        generate_audio: true,
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1.5-pro",
      "input": {
        "prompt": "A jazz pianist plays an intimate melody in a dimly lit club, fingers moving across the keys as the camera slowly circles the grand piano, warm amber spotlights, natural piano music and room ambience",
        "aspect_ratio": "16:9",
        "duration": 5,
        "generate_audio": true,
        "resolution": "1080p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1.5-pro/jazz-performance.mp4"
      }
    }

**Rainy Cafe Animation** — Animate a first-frame image with synchronized ambient sound
    
    
    const response = await env.AI.run(
      'bytedance/seedance-1.5-pro',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        prompt:
          'The camera slowly moves closer as steam rises from the cup and gentle rain can be heard against a nearby window, quiet cafe ambience',
        duration: 5,
        generate_audio: true,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-1.5-pro",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "prompt": "The camera slowly moves closer as steam rises from the cup and gentle rain can be heard against a nearby window, quiet cafe ambience",
        "duration": 5,
        "generate_audio": true,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-1.5-pro/rainy-cafe-animation.mp4"
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

generate_audio

`boolean`requireddefault: falseWhether to generate synchronized native audio with the video. Audio output is billed at a higher rate than silent output.

watermark

`boolean`requireddefault: falseWhether to add a watermark to the output video

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation

use_virtual_avatar

`boolean`requireddefault: falseRoute image reference inputs (image, reference_images, last_frame_image) through ByteDance's trusted virtual avatar asset library before generation. Intended for AI-generated/virtual character avatars that would otherwise be blocked by face or deepfake detection

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1.5-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1.5-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1.5-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-1.5-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
