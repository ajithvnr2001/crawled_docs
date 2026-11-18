---
url: https://developers.cloudflare.com/ai/models/lightricks/ltx-2-3-fast/
title: LTX-2.3 Fast (lightricks) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.482414+00:00
---

# LTX-2.3 Fast (lightricks) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/lightricks/ltx-2-3-fast/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



l

# LTX-2.3 Fast

Text-to-Video • lightricks

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`lightricks/ltx-2-3-fast`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Lightricks LTX-2.3 Fast is a low-cost video generation model for text-to-video and image-to-video, with synchronized audio, first-to-last frame control, portrait and landscape output up to 4K, and clips up to 20 seconds.

Model Info|   
---|---  
More information| [link ↗](https://docs.ltx.io/models/ltx-2-3)  
Pricing| 

  * @720p (per second)$0.03
  * @1080p (per second)$0.06
  * @2k (per second)$0.12
  * @4k (per second)$0.24
  * Default (per second)$0.03

  
  
## Usage
    
    
    const response = await env.AI.run(
      'lightricks/ltx-2-3-fast',
      {
        prompt: 'A paper boat drifting across a calm pond at sunrise',
        duration: 6,
        resolution: '1920x1080',
        fps: 24,
        generate_audio: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "lightricks/ltx-2-3-fast",
      "input": {
        "prompt": "A paper boat drifting across a calm pond at sunrise",
        "duration": 6,
        "resolution": "1920x1080",
        "fps": 24,
        "generate_audio": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/lightricks/ltx-2-3-fast/text-to-video.mp4"
      }
    }

## Examples

**Image-to-Video** — Animate a still image into a short video
    
    
    const response = await env.AI.run(
      'lightricks/ltx-2-3-fast',
      {
        prompt: 'The camera slowly pushes in while clouds drift past the tower',
        image_uri: 'https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg',
        duration: 6,
        resolution: '1920x1080',
        fps: 24,
        generate_audio: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "lightricks/ltx-2-3-fast",
      "input": {
        "prompt": "The camera slowly pushes in while clouds drift past the tower",
        "image_uri": "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg",
        "duration": 6,
        "resolution": "1920x1080",
        "fps": 24,
        "generate_audio": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/lightricks/ltx-2-3-fast/image-to-video.mp4"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 10000Text prompt describing the video

image_uri

`string`format: uriHTTPS URI for the first frame

last_frame_uri

`string`format: uriHTTPS URI for the last frame

▶duration

`one of`required

resolution

`string`requireddefault: 1920x1080enum: 1280x720, 720x1280, 1920x1080, 1080x1920, 2560x1440, 1440x2560, 3840x2160, 2160x3840

▶fps

`one of`required

generate_audio

`boolean`requireddefault: true

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-3-fast/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-3-fast/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-3-fast/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-3-fast/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
