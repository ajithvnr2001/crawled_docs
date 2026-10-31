---
url: https://developers.cloudflare.com/ai/models/topaz/gigapixel-standard-2/
title: Gigapixel Standard 2 (topaz) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.065707+00:00
---

# Gigapixel Standard 2 (topaz) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/topaz/gigapixel-standard-2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



t

# Gigapixel Standard 2

Image-to-Image • topaz

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`topaz/gigapixel-standard-2`

  * Third-party



Topaz Labs Gigapixel Standard 2 is a general-purpose precision image upscaler that balances detail, sharpness, and noise reduction while staying true to the source. It is the recommended default for photos, graphics, and print, with optional face recovery.

Model Info|   
---|---  
More information| [link ↗](https://developer.topazlabs.com/image-models/gigapixel/standard-2)  
Pricing| 

  * Per provider unit$0.12

  
  
## Usage
    
    
    const response = await env.AI.run(
      'topaz/gigapixel-standard-2',
      {
        image: 'https://tile.loc.gov/storage-services/service/pnp/ppmsca/13300/13397r.jpg',
        output_format: 'jpeg',
        output_width: 1900,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "topaz/gigapixel-standard-2",
      "input": {
        "image": "https://tile.loc.gov/storage-services/service/pnp/ppmsca/13300/13397r.jpg",
        "output_format": "jpeg",
        "output_width": 1900
      }
    }'

![Poster Upscale](https://examples.aig.cloudflare.com/topaz/gigapixel-standard-2/poster-upscale.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/topaz/gigapixel-standard-2/poster-upscale.jpeg"
      }
    }

## Examples

**Small Photo Upscale** — Upscale a 640-pixel photo 4x to 2560 pixels wide. Standard 2 picks its own enhancement settings, so none are needed. Photo: NASA.
    
    
    const response = await env.AI.run(
      'topaz/gigapixel-standard-2',
      {
        image:
          'https://images-assets.nasa.gov/image/KSC-20260313-PH-JBS01_0157/KSC-20260313-PH-JBS01_0157~small.jpg',
        output_format: 'jpeg',
        output_width: 2560,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "topaz/gigapixel-standard-2",
      "input": {
        "image": "https://images-assets.nasa.gov/image/KSC-20260313-PH-JBS01_0157/KSC-20260313-PH-JBS01_0157~small.jpg",
        "output_format": "jpeg",
        "output_width": 2560
      }
    }'

![Small Photo Upscale](https://examples.aig.cloudflare.com/topaz/gigapixel-standard-2/small-photo-upscale.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/topaz/gigapixel-standard-2/small-photo-upscale.jpeg"
      }
    }

**Thumbnail Portrait** — Upscale a 127-pixel thumbnail of an 1863 portrait 6x to 762 pixels wide. Face recovery rebuilds a sharp face where a plain upscale smears it. Photo: Alexander Gardner, via the Library of Congress (no known restrictions).
    
    
    const response = await env.AI.run(
      'topaz/gigapixel-standard-2',
      {
        face_enhancement: true,
        face_enhancement_creativity: 0.2,
        face_enhancement_strength: 0.8,
        image: 'https://tile.loc.gov/storage-services/service/pnp/ppmsca/19300/19301_150px.jpg',
        output_format: 'jpeg',
        output_width: 762,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "topaz/gigapixel-standard-2",
      "input": {
        "face_enhancement": true,
        "face_enhancement_creativity": 0.2,
        "face_enhancement_strength": 0.8,
        "image": "https://tile.loc.gov/storage-services/service/pnp/ppmsca/19300/19301_150px.jpg",
        "output_format": "jpeg",
        "output_width": 762
      }
    }'

![Thumbnail Portrait](https://examples.aig.cloudflare.com/topaz/gigapixel-standard-2/thumbnail-portrait.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/topaz/gigapixel-standard-2/thumbnail-portrait.jpeg"
      }
    }

## Parameters

image

`string`requiredSource image as a public HTTPS URL or a base64 data URI (JPEG, PNG, or TIFF)

output_width

`integer`minimum: 1maximum: 32000Desired output width in pixels. If only one dimension is set, the other scales proportionally. If neither is set, the source resolution is kept (enhancement without upscaling)

output_height

`integer`minimum: 1maximum: 32000Desired output height in pixels. If only one dimension is set, the other scales proportionally. If neither is set, the source resolution is kept (enhancement without upscaling)

output_format

`string`requireddefault: jpegenum: jpeg, png, tiffFormat of the upscaled image

crop_to_fill

`boolean`Crop to fill the requested dimensions instead of letterboxing when the aspect ratio differs

face_enhancement

`boolean`Run face recovery on detected faces

face_enhancement_strength

`number`minimum: 0maximum: 1Strength of face recovery

face_enhancement_creativity

`number`minimum: 0maximum: 1Face recovery style, from realistic (0) to creative (1)

subject_detection

`string`enum: foreground, background, allWhere enhancements are applied

sharpen

`number`minimum: 0maximum: 1Amount of additional sharpening

denoise

`number`minimum: 0maximum: 1Amount of noise reduction

fix_compression

`number`minimum: 0maximum: 1Amount of compression-artifact reduction

image

`string`format: uriTime-limited presigned URL to the upscaled image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-standard-2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-standard-2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-standard-2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-standard-2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
