---
url: https://developers.cloudflare.com/ai/models/klingai/kling-v3-motion-control/
title: Kling v3 Motion Control (Kling AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.183971+00:00
---

# Kling v3 Motion Control (Kling AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/klingai/kling-v3-motion-control/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Kling AI logo](https://developers.cloudflare.com/_astro/kling.CbZKRtvH.svg)

# Kling v3 Motion Control

video-to-video • Kling AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`klingai/kling-v3-motion-control`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Kling AI Motion Control 3.0 transfers a reference video's motion to a character image, generating 3–30 seconds when matching the video orientation or up to 10 seconds when matching the image orientation, with optional prompt guidance and 720p or 1080p output.

Model Info|   
---|---  
Terms and License| [link ↗](https://klingai.com/terms)  
More information| [link ↗](https://kling.ai/document-api/api/video/motion-control)  
Pricing| 

  * Default (per second)$0.126
  * @720p (per second)$0.126
  * @1080p (per second)$0.168

  
  
## Usage
    
    
    const response = await env.AI.run(
      'klingai/kling-v3-motion-control',
      {
        audio: 'off',
        character_orientation: 'video',
        image_url:
          'https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/35d77e27300cf5e8995704cd858d759c.png',
        prompt:
          "Keep the character's gray T-shirt and denim shorts while matching the dancer's fluid movements.",
        resolution: '720p',
        video_url: 'https://v4-kling.kechuangai.com/kcdn/cdn-kcdn112452/kling-qa-test/dance_10s.mp4',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "klingai/kling-v3-motion-control",
      "input": {
        "audio": "off",
        "character_orientation": "video",
        "image_url": "https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-qa-test/35d77e27300cf5e8995704cd858d759c.png",
        "prompt": "Keep the character'\''s gray T-shirt and denim shorts while matching the dancer'\''s fluid movements.",
        "resolution": "720p",
        "video_url": "https://v4-kling.kechuangai.com/kcdn/cdn-kcdn112452/kling-qa-test/dance_10s.mp4"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/klingai/kling-v3-motion-control/animate-a-character-from-motion.mp4"
      }
    }

## Parameters

prompt

`string`maxLength: 2500Optional prompt for scene and background details

image_url

`string`requiredformat: uriPublic URL of the character image (JPG or PNG)

video_url

`string`requiredformat: uriPublic URL of the motion reference video (MP4 or MOV)

character_orientation

`string`requireddefault: videoenum: video, imageMatch character orientation to the reference video or image

audio

`string`requireddefault: originalenum: original, offKeep the reference video audio or omit audio

resolution

`string`requireddefault: 720penum: 720p, 1080pGenerated video resolution

video

`string`URL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-motion-control/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-motion-control/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-motion-control/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v3-motion-control/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
