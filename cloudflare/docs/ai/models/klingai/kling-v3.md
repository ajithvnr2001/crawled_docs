---
url: https://developers.cloudflare.com/ai/models/klingai/kling-v3/
title: Kling v3 (Kling AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.213672+00:00
---

# Kling v3 (Kling AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/klingai/kling-v3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Kling AI logo](https://developers.cloudflare.com/_astro/kling.CbZKRtvH.svg)

# Kling v3

Text-to-Video • Kling AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`klingai/kling-v3`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Kling V3 is Kling AI's text-to-video model with audio generation support.

Model Info|   
---|---  
Terms and License| [link ↗](https://klingai.com/terms)  
More information| [link ↗](https://klingai.com/)  
Pricing| 

  * Default (per second)$0.112
  * default audio$0.168

  
  
## Usage
    
    
    const response = await env.AI.run(
      'klingai/kling-v3',
      {
        prompt:
          'A golden retriever running through a field of sunflowers on a sunny day',
        duration: 5,
        aspect_ratio: '16:9',
        sound: 'on',
      },
      {
        gateway: { id: 'default' },
      }
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "klingai/kling-v3",
      "input": {
        "aspect_ratio": "16:9",
        "duration": 5,
        "prompt": "A golden retriever running through a field of sunflowers on a sunny day",
        "sound": "on"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/klingai/kling-v3/simple-video.mp4"
      }
    }

## Parameters

prompt

`string`requiredText prompt describing the video to generate

negative_prompt

`string`Negative text prompt

image_input

`string`Base64-encoded reference image for i2v

duration

`integer`requireddefault: 5minimum: 3maximum: 15Video duration in seconds

aspect_ratio

`string`requireddefault: 16:9enum: 16:9, 9:16, 1:1Video aspect ratio

sound

`string`requireddefault: onenum: on, offWhether to generate sound with the video

video

`string`URL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/klingai/kling-v3/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v3/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/klingai/kling-v3/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/klingai/kling-v3/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
