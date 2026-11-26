---
url: https://developers.cloudflare.com/ai/models/topaz/proteus-4/
title: Proteus 4 (topaz) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.603606+00:00
---

# Proteus 4 (topaz) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/topaz/proteus-4/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



t

# Proteus 4

video-to-video • topaz

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`topaz/proteus-4`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Topaz Labs Proteus 4 (prob-4) is a general-purpose precision video enhancer that upscales, denoises and sharpens low to medium quality footage to 1080p or 4K without generating new detail. It is Topaz's recommended default model and costs far less than the generative Starlight models.

Model Info|   
---|---  
More information| [link ↗](https://developer.topazlabs.com/video-models/upscaling-and-enhancement/precision/proteus)  
Pricing| 

  * Per provider unit$0.12

  
  
## Usage
    
    
    const response = await env.AI.run(
      'topaz/proteus-4',
      {
        frame_count: 150,
        frame_rate: 29.97,
        source_container: 'mp4',
        source_height: 360,
        source_width: 640,
        video_uri:
          'https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4',
        target_resolution: '1920x1080',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "topaz/proteus-4",
      "input": {
        "frame_count": 150,
        "frame_rate": 29.97,
        "source_container": "mp4",
        "source_height": 360,
        "source_width": 640,
        "video_uri": "https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4",
        "target_resolution": "1920x1080"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/topaz/proteus-4/upscale-to-1080p.mp4"
      }
    }

## Examples

**4K with Manual Clean-Up** — Upscale to 4K and set the noise, compression-artifact and detail values yourself.
    
    
    const response = await env.AI.run(
      'topaz/proteus-4',
      {
        frame_count: 150,
        frame_rate: 29.97,
        source_container: 'mp4',
        source_height: 360,
        source_width: 640,
        video_uri:
          'https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4',
        target_resolution: '3840x2160',
        parameter_mode: 'Manual',
        noise: 0.3,
        compression: 0.4,
        details: 0.2,
        blur: 0.1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "topaz/proteus-4",
      "input": {
        "frame_count": 150,
        "frame_rate": 29.97,
        "source_container": "mp4",
        "source_height": 360,
        "source_width": 640,
        "video_uri": "https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4",
        "target_resolution": "3840x2160",
        "parameter_mode": "Manual",
        "noise": 0.3,
        "compression": 0.4,
        "details": 0.2,
        "blur": 0.1
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/topaz/proteus-4/4k-with-manual-clean-up.mp4"
      }
    }

## Parameters

video_uri

`string`requiredformat: uriHTTPS URI of the source video to enhance

source_container

`string`requiredenum: 3gp, avi, dv, flv, m1v, m2t, m2ts, m2v, m4v, mkv, mov, mp4, mpeg, mpg, mts, mxf, ser, ts, vob, webm, wmvContainer format of the source video

source_width

`integer`requiredexclusiveMinimum: 0maximum: 9007199254740991Width of the source video in pixels

source_height

`integer`requiredexclusiveMinimum: 0maximum: 9007199254740991Height of the source video in pixels

frame_count

`integer`requiredexclusiveMinimum: 0maximum: 9007199254740991Total frame count of the source video (used by Topaz for credit estimation)

frame_rate

`number`requiredexclusiveMinimum: 0Frame rate of the source video in frames per second (e.g. 29.97)

target_resolution

`string`requireddefault: 1920x1080enum: 1920x1080, 3840x2160Target output resolution

parameter_mode

`string`enum: Auto, Manual, Relative"Auto" estimates every value, "Relative" nudges the estimates by the amounts you send, "Manual" uses your values as they are.

compression

`number`minimum: -1maximum: 1Strength of compression artifact recovery, from -1 to 1. Estimated if omitted.

details

`number`minimum: -1maximum: 1Amount of detail reconstruction, from -1 to 1. Estimated if omitted.

noise

`number`minimum: -1maximum: 1Amount of noise reduction, from -1 to 1. Estimated if omitted.

halo

`number`minimum: -1maximum: 1Amount of halo reduction, from -1 to 1. Estimated if omitted.

preblur

`number`minimum: -1maximum: 1Anti-aliasing and deblurring strength, from -1 to 1. Estimated if omitted.

blur

`number`minimum: -1maximum: 1Amount of sharpening, from -1 to 1. Estimated if omitted.

video

`string`format: uriURL to the enhanced video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/topaz/proteus-4/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/proteus-4/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/topaz/proteus-4/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/proteus-4/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
