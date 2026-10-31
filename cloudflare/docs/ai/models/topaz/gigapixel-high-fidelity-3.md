---
url: https://developers.cloudflare.com/ai/models/topaz/gigapixel-high-fidelity-3/
title: Gigapixel High Fidelity 3 (topaz) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:16.613960+00:00
---

# Gigapixel High Fidelity 3 (topaz) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/topaz/gigapixel-high-fidelity-3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



t

# Gigapixel High Fidelity 3

Image-to-Image • topaz

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`topaz/gigapixel-high-fidelity-3`

  * Third-party



Topaz Labs Gigapixel High Fidelity 3 is a precision image upscaler tuned for high-resolution sources and professional photography, preserving fine texture and detail with minimal alteration. It adds recovery-strength and opacity controls over High Fidelity 2.

Model Info|   
---|---  
More information| [link ↗](https://developer.topazlabs.com/image-models/gigapixel/high-fidelity-3)  
Pricing| 

  * Per provider unit$0.12

  
  
## Usage
    
    
    const response = await env.AI.run(
      'topaz/gigapixel-high-fidelity-3',
      {
        image:
          'https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e000842/GSFC_20171208_Archive_e000842~medium.jpg',
        output_format: 'jpeg',
        output_width: 2560,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "topaz/gigapixel-high-fidelity-3",
      "input": {
        "image": "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e000842/GSFC_20171208_Archive_e000842~medium.jpg",
        "output_format": "jpeg",
        "output_width": 2560
      }
    }'

![Star Field Upscale](https://examples.aig.cloudflare.com/topaz/gigapixel-high-fidelity-3/star-field-upscale.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/topaz/gigapixel-high-fidelity-3/star-field-upscale.jpeg"
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

recovery_strength

`number`minimum: 0maximum: 1Strength of detail recovery (Topaz default 1.0)

opacity

`number`minimum: 0maximum: 1Blend of the enhanced result over the source (Topaz default 1.0)

image

`string`format: uriTime-limited presigned URL to the upscaled image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-high-fidelity-3/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-high-fidelity-3/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-high-fidelity-3/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/topaz/gigapixel-high-fidelity-3/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
