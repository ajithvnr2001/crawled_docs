---
url: https://developers.cloudflare.com/ai/models/recraft/vectorize/
title: Recraft Vectorize (Recraft) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.523787+00:00
---

# Recraft Vectorize (Recraft) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/recraft/vectorize/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft Vectorize

Image-to-Image • Recraft

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`recraft/vectorize`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Recraft Vectorize converts a raster image (PNG, JPG or WEBP) into a clean, editable SVG made of shapes. Use it to make logos, icons and illustrations scalable. V1 Pro produces higher-quality vectors.

Model Info|   
---|---  
More information| [link ↗](https://www.recraft.ai/docs/api-reference/tools/vectorize)  
Pricing| 

  * Per provider unit$0.001

  
  
## Usage
    
    
    const response = await env.AI.run(
      'recraft/vectorize',
      {
        image: 'https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/ocr-test3.png',
        version: 'v1_pro',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/vectorize",
      "input": {
        "image": "https://arkdocs-en.tos-ap-southeast-1.volces.com/images/image-generation/ocr-test3.png",
        "version": "v1_pro"
      }
    }'

![Sticker Art to SVG \(V1 Pro\)](https://examples.aig.cloudflare.com/recraft/vectorize/sticker-art-to-svg-v1-pro.svg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/vectorize/sticker-art-to-svg-v1-pro.svg"
      }
    }

## Examples

**Vectorize an Illustration** — Turn a raster illustration into an editable SVG.
    
    
    const response = await env.AI.run(
      'recraft/vectorize',
      {
        image:
          'https://cdn.prod.website-files.com/655727fe69827d9a402de12c/679b82f54ef9617939df9d8e_motorcycle--going-fast.png',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/vectorize",
      "input": {
        "image": "https://cdn.prod.website-files.com/655727fe69827d9a402de12c/679b82f54ef9617939df9d8e_motorcycle--going-fast.png"
      }
    }'

![Vectorize an Illustration](https://examples.aig.cloudflare.com/recraft/vectorize/vectorize-an-illustration.svg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/vectorize/vectorize-an-illustration.svg"
      }
    }

**Cut-Out Shapes** — Shapes that don't overlap, for vinyl cutters and screen printing.
    
    
    const response = await env.AI.run(
      'recraft/vectorize',
      {
        image:
          'https://cdn.prod.website-files.com/655727fe69827d9a402de12c/679b82f54ef9617939df9d8e_motorcycle--going-fast.png',
        shape_stacking: 'cut_out',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/vectorize",
      "input": {
        "image": "https://cdn.prod.website-files.com/655727fe69827d9a402de12c/679b82f54ef9617939df9d8e_motorcycle--going-fast.png",
        "shape_stacking": "cut_out"
      }
    }'

![Cut-Out Shapes](https://examples.aig.cloudflare.com/recraft/vectorize/cut-out-shapes.svg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/vectorize/cut-out-shapes.svg"
      }
    }

## Parameters

image

`string`requiredminLength: 1URL or data URL of the input image: PNG, JPG or WEBP, under 20 MB, up to 16 MP, sides 256 to 4096 px.

version

`string`enum: v1, v1_pro"v1" ($0.01) or "v1_pro" (higher-quality vectors, $0.04). Defaults to "v1".

shape_stacking

`string`enum: hierarchical, cut_out"hierarchical" layers shapes; "cut_out" makes shapes that do not overlap (for cutters and printing). Defaults to "hierarchical".

image

`string`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/recraft/vectorize/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/vectorize/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/recraft/vectorize/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/vectorize/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
