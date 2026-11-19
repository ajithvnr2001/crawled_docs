---
url: https://developers.cloudflare.com/ai/models/kwaivgi/kling-v2.6/
title: Kling v2.6 (kwaivgi) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.213961+00:00
---

# Kling v2.6 (kwaivgi) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/kwaivgi/kling-v2.6/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



k

# Kling v2.6

Text-to-Video • kwaivgi

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`kwaivgi/kling-v2.6`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Kling v2.6 generates cinematic 5- or 10-second videos with synchronized audio from text prompts or a base64-encoded starting image. It supports 16:9, 9:16, and 1:1 aspect ratios, with optional negative prompts and standard or pro quality modes.

Model Info|   
---|---  
Terms and License| [link ↗](https://klingai.com/terms)  
More information| [link ↗](https://klingai.com/)  
Pricing| 

  * Default (per second)$0.07
  * default audio$0.14

  
  
## Usage
    
    
    const response = await env.AI.run(
      'kwaivgi/kling-v2.6',
      {
        prompt:
          'A cinematic wide shot of a red hot-air balloon drifting above a mountain valley at sunrise, the camera slowly tracking forward as golden light breaks through the clouds.',
        aspect_ratio: '16:9',
        duration: '5',
        mode: 'pro',
        sound: 'on',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "kwaivgi/kling-v2.6",
      "input": {
        "prompt": "A cinematic wide shot of a red hot-air balloon drifting above a mountain valley at sunrise, the camera slowly tracking forward as golden light breaks through the clouds.",
        "aspect_ratio": "16:9",
        "duration": "5",
        "mode": "pro",
        "sound": "on"
      }
    }'
    
    
    {
      "code": 0,
      "message": "SUCCEED",
      "request_id": "088b1870-9e01-49b4-9b8c-485313e0259c",
      "data": {
        "task_id": "949523490075068623",
        "task_status": "succeed",
        "task_info": {},
        "task_result": {
          "videos": [
            {
              "id": "949520558369162413",
              "url": "https://examples.aig.cloudflare.com/kwaivgi/kling-v2.6/generate-a-cinematic-mountain-sunrise.mp4",
              "duration": "5.041"
            }
          ]
        },
        "task_status_msg": "",
        "created_at": 1794413587278,
        "updated_at": 1794413715176,
        "final_unit_deduction": "0",
        "final_balance_deduction": {
          "quota": "0.42",
          "list_price": "0.7"
        }
      }
    }

## Parameters

prompt

`string`requiredText prompt for video generation

negative_prompt

`string`Things to exclude from the video

aspect_ratio

`string`requireddefault: 16:9enum: 16:9, 9:16, 1:1Output aspect ratio

duration

`string`requireddefault: 5enum: 5, 10Video duration in seconds

mode

`string`requireddefault: proenum: std, proGeneration quality mode

sound

`string`requireddefault: onenum: on, offGenerate synchronized audio

video

`string`format: uriGenerated video URL

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/kwaivgi/kling-v2.6/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/kwaivgi/kling-v2.6/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/kwaivgi/kling-v2.6/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/kwaivgi/kling-v2.6/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
