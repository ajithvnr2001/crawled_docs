---
url: https://developers.cloudflare.com/ai/models/google/gemini-omni-1.2-flash/
title: Gemini Omni 1.2 Flash (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:51.996981+00:00
---

# Gemini Omni 1.2 Flash (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/gemini-omni-1.2-flash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Gemini Omni 1.2 Flash

Text-to-Video • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`google/gemini-omni-1.2-flash`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Gemini Omni 1.2 Flash is Google's video generation and editing model with native audio. It turns text, images or video into 3 to 15 second clips at up to 4K, and supports conversational editing, video extension and first and last frame interpolation.

Model Info|   
---|---  
Terms and License| [link ↗](https://ai.google.dev/gemini-api/terms)  
More information| [link ↗](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)  
Pricing| 

  * Input text (per 1M tokens)$1.50
  * Input image (per 1M tokens)$1.50
  * Input video (per 1M tokens)$1.50
  * Input audio (per 1M tokens)$1.50
  * Output text (per 1M tokens)$9.00
  * Reasoning (per 1M tokens)$9.00
  * Output video (per 1M tokens)$12.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/gemini-omni-1.2-flash',
      {
        text: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
        aspect_ratio: '16:9',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.2-flash",
      "input": {
        "text": "A marble rolling fast on a chain reaction style track, continuous smooth shot.",
        "aspect_ratio": "16:9",
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.2-flash/text-to-video.mp4"
      }
    }

## Examples

**Portrait city** — Generate a portrait-format cinematic city scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-1.2-flash',
      {
        text: 'A futuristic city with neon lights and flying cars, cinematic camera movement and atmospheric haze.',
        aspect_ratio: '9:16',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.2-flash",
      "input": {
        "text": "A futuristic city with neon lights and flying cars, cinematic camera movement and atmospheric haze.",
        "aspect_ratio": "9:16",
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.2-flash/portrait-city.mp4"
      }
    }

**Mountain sunrise** — Generate a high-resolution landscape nature scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-1.2-flash',
      {
        text: 'A drone shot flying over a mountain landscape at sunrise, golden light reflecting across a misty valley.',
        aspect_ratio: '16:9',
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.2-flash",
      "input": {
        "text": "A drone shot flying over a mountain landscape at sunrise, golden light reflecting across a misty valley.",
        "aspect_ratio": "16:9",
        "resolution": "1080p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.2-flash/mountain-sunrise.mp4"
      }
    }

**Chain reaction** — Generate a low-resolution landscape action scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-1.2-flash',
      {
        text: 'A marble rolling quickly along a wooden track, knocking through a playful chain reaction in one continuous shot.',
        aspect_ratio: '16:9',
        resolution: '360p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.2-flash",
      "input": {
        "text": "A marble rolling quickly along a wooden track, knocking through a playful chain reaction in one continuous shot.",
        "aspect_ratio": "16:9",
        "resolution": "360p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.2-flash/chain-reaction.mp4"
      }
    }

## Parameters

text

`string`Text prompt or editing instruction

image

`string`First-frame or primary reference image

last_frame

`string`Last-frame reference image

▶reference_images[]

`array`maxItems: 10

video

`string`Reference video for editing or extension

audio

`string`Reference audio input

previous_interaction_id

`string`

aspect_ratio

`string`enum: 16:9, 9:16

resolution

`string`enum: 360p, 720p, 1080p, 4k

▶video

`one of`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.2-flash/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.2-flash/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.2-flash/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.2-flash/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
