---
url: https://developers.cloudflare.com/ai/models/openai/gpt-image-2.6-sunburst/
title: GPT Image 2.6 Sunburst (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.772839+00:00
---

# GPT Image 2.6 Sunburst (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-image-2.6-sunburst/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT Image 2.6 Sunburst

Text-to-Image • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`openai/gpt-image-2.6-sunburst`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



OpenAI's most capable image generation and editing model. It accepts text and image inputs and produces images with low, medium, high, xhigh, max, and auto quality settings.

Model Info|   
---|---  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://developers.openai.com/api/docs/models/gpt-image-2.6-sunburst)  
Pricing| 

  * Input (per 1M tokens)$5.00
  * Cached input (per 1M tokens)$1.25
  * Input image (per 1M tokens)$8.00
  * Cached input image (per 1M tokens)$2.00
  * Output image (per 1M tokens)$30.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.6-sunburst',
      {
        prompt:
          'A cutaway editorial illustration of a floating ocean research station during a storm, showing laboratories, hydroponic gardens, autonomous submersibles, and illuminated underwater cables, precise technical details, dramatic but realistic lighting',
        quality: 'max',
        size: '1536x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.6-sunburst",
      "input": {
        "prompt": "A cutaway editorial illustration of a floating ocean research station during a storm, showing laboratories, hydroponic gardens, autonomous submersibles, and illuminated underwater cables, precise technical details, dramatic but realistic lighting",
        "quality": "max",
        "size": "1536x1024"
      }
    }'

![Technical Editorial Illustration](https://examples.aig.cloudflare.com/openai/gpt-image-2.6-sunburst/technical-editorial-illustration.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.6-sunburst/technical-editorial-illustration.png"
      }
    }

## Examples

**Portrait WebP** — Generate a portrait composition in WebP format
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.6-sunburst',
      {
        prompt:
          'A fashion portrait of an astronaut botanist in a glass greenhouse on Mars, crimson dust visible through the windows, translucent fabric, delicate blue flowers in the foreground, soft rim light, sophisticated magazine photography',
        quality: 'xhigh',
        size: '1024x1536',
        output_format: 'webp',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.6-sunburst",
      "input": {
        "prompt": "A fashion portrait of an astronaut botanist in a glass greenhouse on Mars, crimson dust visible through the windows, translucent fabric, delicate blue flowers in the foreground, soft rim light, sophisticated magazine photography",
        "quality": "xhigh",
        "size": "1024x1536",
        "output_format": "webp"
      }
    }'

![Portrait WebP](https://examples.aig.cloudflare.com/openai/gpt-image-2.6-sunburst/portrait-webp.webp)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.6-sunburst/portrait-webp.webp"
      }
    }

**Cinematic Reference Edit** — Edit a reference image into a cinematic scene while preserving its main subject
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.6-sunburst',
      {
        prompt:
          "Turn the reference drawing into a polished cinematic stop-motion scene. Preserve the character's face and red scarf, add a miniature train platform at night, warm station lights, shallow depth of field, handcrafted felt and paper textures",
        images: [
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=',
        ],
        quality: 'high',
        background: 'opaque',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.6-sunburst",
      "input": {
        "prompt": "Turn the reference drawing into a polished cinematic stop-motion scene. Preserve the character'\''s face and red scarf, add a miniature train platform at night, warm station lights, shallow depth of field, handcrafted felt and paper textures",
        "images": [
          "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII="
        ],
        "quality": "high",
        "background": "opaque"
      }
    }'

![Cinematic Reference Edit](https://examples.aig.cloudflare.com/openai/gpt-image-2.6-sunburst/cinematic-reference-edit.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.6-sunburst/cinematic-reference-edit.png"
      }
    }

## Parameters

prompt

`string`requiredText prompt describing the image to generate or edit

▶images[]

`array`maxItems: 16Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).

quality

`string`enum: low, medium, high, xhigh, max, autoQuality of the generated image

size

`string`enum: 1024x1024, 1024x1536, 1536x1024, autoSize of the generated image. For gif output, the size of each frame.

background

`string`enum: transparent, opaque, autoBackground transparency setting. Use transparent for images with no background, opaque for a solid background, or auto to let the model decide.

output_format

`string`enum: png, webp, jpeg, gifOutput format for the generated image. Use gif for an animated GIF.

moderation

`string`enum: auto, lowContent moderation level. Use low for less restrictive filtering, or auto for the default.

output_compression

`integer`minimum: 0maximum: 100Compression level from 0 to 100 for webp and jpeg output

complexity

`string`enum: low, medium, highHow much the model plans the image before it renders it, separately from quality

frame_count

`integer`minimum: 2maximum: 16Number of frames, from 2 to 16, for gif output

frame_duration_ms

`integer`minimum: 20maximum: 9007199254740991Delay per frame in milliseconds, at least 20, for gif output

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.6-sunburst/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.6-sunburst/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.6-sunburst/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.6-sunburst/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
