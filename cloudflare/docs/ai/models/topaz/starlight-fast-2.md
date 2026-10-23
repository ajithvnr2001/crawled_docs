---
url: https://developers.cloudflare.com/ai/models/topaz/starlight-fast-2/
title: Starlight Fast 2 (topaz) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:58.957322+00:00
---

# Starlight Fast 2 (topaz) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/topaz/starlight-fast-2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



t

# Starlight Fast 2

video-to-video • topaz

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`topaz/starlight-fast-2`

  * Third-party



Topaz Labs Starlight Fast 2 (slf-2) enhances and upscales source video to 1080p or 4K with faster processing than Starlight Precise. It is designed for video restoration workflows where turnaround time is important.

Model Info|   
---|---  
More information| [link ↗](https://developer.topazlabs.com/)  
Pricing| 

  * Per provider unit$0.12

  
  
## Usage
    
    
    const response = await env.AI.run(
      'topaz/starlight-fast-2',
      {
        end_index: 120,
        frame_count: 150,
        frame_rate: 29.97,
        source_container: 'mp4',
        source_height: 360,
        source_width: 640,
        start_index: 0,
        target_resolution: '1920x1080',
        upscaling_factor: 2,
        video_uri:
          'https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "topaz/starlight-fast-2",
      "input": {
        "end_index": 120,
        "frame_count": 150,
        "frame_rate": 29.97,
        "source_container": "mp4",
        "source_height": 360,
        "source_width": 640,
        "start_index": 0,
        "target_resolution": "1920x1080",
        "upscaling_factor": 2,
        "video_uri": "https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/topaz/starlight-fast-2/fast-video-enhancement.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
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

upscaling_factor

`number`requireddefault: 1minimum: 1maximum: 8Output resolution multiplier relative to the source video

start_index

`integer`requireddefault: 0minimum: 0maximum: 9007199254740991First source frame to process

end_index

`integer`requireddefault: 1000000minimum: 0maximum: 9007199254740991Last source frame to process

video

`string`format: uriURL to the enhanced video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/topaz/starlight-fast-2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/starlight-fast-2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/topaz/starlight-fast-2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/starlight-fast-2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
