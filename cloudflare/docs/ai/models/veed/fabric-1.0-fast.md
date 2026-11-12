---
url: https://developers.cloudflare.com/ai/models/veed/fabric-1.0-fast/
title: VEED Fabric 1.0 Fast (veed) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.334072+00:00
---

# VEED Fabric 1.0 Fast (veed) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/veed/fabric-1.0-fast/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



v

# VEED Fabric 1.0 Fast

Image-to-Video • veed

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`veed/fabric-1.0-fast`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



A faster variant of VEED Fabric 1.0 optimized for lower-latency lipsync video generation.

Model Info|   
---|---  
More information| [link ↗](https://fal.ai/models/veed/fabric-1.0/fast)  
Pricing| 

  * @480p (per second)$0.10
  * @720p (per second)$0.20
  * Default (per second)$0.20

  
  
## Usage
    
    
    const response = await env.AI.run(
      'veed/fabric-1.0-fast',
      {
        image_url: 'https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png',
        audio_url: 'https://v3.fal.media/files/elephant/Oz_g4AwQvXtXpUHL3Pa7u_Hope.mp3',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "veed/fabric-1.0-fast",
      "input": {
        "image_url": "https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png",
        "audio_url": "https://v3.fal.media/files/elephant/Oz_g4AwQvXtXpUHL3Pa7u_Hope.mp3",
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "video": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/veed__fabric-1.0-fast/quick-lipsync.mp4"
      },
      "state": "Completed"
    }

## Examples

**Preview at 480p** — Faster, cheaper preview at 480p.
    
    
    const response = await env.AI.run(
      'veed/fabric-1.0-fast',
      {
        image_url: 'https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png',
        audio_url: 'https://v3.fal.media/files/elephant/Oz_g4AwQvXtXpUHL3Pa7u_Hope.mp3',
        resolution: '480p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "veed/fabric-1.0-fast",
      "input": {
        "image_url": "https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png",
        "audio_url": "https://v3.fal.media/files/elephant/Oz_g4AwQvXtXpUHL3Pa7u_Hope.mp3",
        "resolution": "480p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "video": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/veed__fabric-1.0-fast/preview-at-480p.mp4"
      },
      "state": "Completed"
    }

## Parameters

image_url

`string`requiredURL of the source image. Accepts a publicly reachable HTTP(S) URL or a base64 data URI (data:image/...;base64,...).

audio_url

`string`requiredURL of the driving audio. Accepts a publicly reachable HTTP(S) URL or a base64 data URI (data:audio/...;base64,...).

resolution

`string`requireddefault: 720penum: 480p, 720pResolution of the generated video.

video

`string`format: uriPresigned URL for the generated lipsync video.

duration

`number`Duration of the generated video in seconds, when reported by the provider.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/veed/fabric-1.0-fast/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/veed/fabric-1.0-fast/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/veed/fabric-1.0-fast/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/veed/fabric-1.0-fast/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
