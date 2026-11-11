---
url: https://developers.cloudflare.com/ai/models/klingai/kling-v4-flash/
title: Kling 4.0 Flash (Kling AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:00:58.542371+00:00
---

# Kling 4.0 Flash (Kling AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/klingai/kling-v4-flash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Kling AI logo](https://developers.cloudflare.com/_astro/kling.CbZKRtvH.svg)

# Kling 4.0 Flash

Text-to-Video • Kling AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`klingai/kling-v4-flash`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Kling 4.0 Flash is Kling AI's fast text-to-video model, producing 3 to 20 seconds of 720p video from prompts of up to 26,000 characters.

Model Info|   
---|---  
Terms and License| [link ↗](https://klingai.com/terms)  
More information| [link ↗](https://klingai.com/)  
Pricing| 

  * @720p (per second)$0.094
  * Default (per second)$0.094

  
  
## Usage
    
    
    const response = await env.AI.run(
      'klingai/kling-v4-flash',
      {
        aspect_ratio: '16:9',
        duration: 5,
        prompt:
          'A paper boat drifts down a narrow, rain-soaked Tokyo alley at night. Neon signs in pink and teal reflect in the puddles and ripple as raindrops fall. The camera tracks low alongside the boat, close to the water. Cinematic, photorealistic, shallow depth of field.',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "klingai/kling-v4-flash",
      "input": {
        "aspect_ratio": "16:9",
        "duration": 5,
        "prompt": "A paper boat drifts down a narrow, rain-soaked Tokyo alley at night. Neon signs in pink and teal reflect in the puddles and ripple as raindrops fall. The camera tracks low alongside the boat, close to the water. Cinematic, photorealistic, shallow depth of field."
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/klingai/kling-v4-flash/neon-alley-paper-boat.mp4"
      }
    }

## Examples

**Latte Art Close-Up** — Vertical 9:16 video for mobile and social feeds
    
    
    const response = await env.AI.run(
      'klingai/kling-v4-flash',
      {
        aspect_ratio: '9:16',
        duration: 5,
        prompt:
          'A barista pours steamed milk into a latte in slow motion, forming a heart. Warm morning light streams through a café window behind her. The camera starts on the cup and slowly tilts up to her smile. Cozy, realistic, soft focus background.',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "klingai/kling-v4-flash",
      "input": {
        "aspect_ratio": "9:16",
        "duration": 5,
        "prompt": "A barista pours steamed milk into a latte in slow motion, forming a heart. Warm morning light streams through a café window behind her. The camera starts on the cup and slowly tilts up to her smile. Cozy, realistic, soft focus background."
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/klingai/kling-v4-flash/latte-art-close-up.mp4"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 26000Text prompt describing the video: scene, actions, camera movement, and style. Up to 26,000 English characters, or 11,000 non-English characters.

duration

`integer`requireddefault: 5minimum: 3maximum: 20Video duration in seconds

aspect_ratio

`string`requireddefault: 16:9enum: 21:9, 16:9, 9:16, 1:1Video aspect ratio

resolution

`string`requireddefault: 720penum: 720pOutput resolution

video

`string`URL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-flash/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-flash/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-flash/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v4-flash/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
