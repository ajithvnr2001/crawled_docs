---
url: https://developers.cloudflare.com/ai/models/bria/rmbg-3.0/
title: RMBG 3.0 (bria) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.232894+00:00
---

# RMBG 3.0 (bria) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bria/rmbg-3.0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



b

# RMBG 3.0

Image-to-Image • bria

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`bria/rmbg-3.0`Copy

Use with the [Workers AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), the AI Gateway [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), or the [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/).

Calling the provider directly? Use the provider's model name instead, including with [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) or the provider's own SDK. For example, Anthropic's name for `anthropic/claude-opus-4.8` is `claude-opus-4-8`.

  * Third-party



Bria's RMBG 3.0 removes the background from an image and returns a PNG cutout with a transparent background, with cleaner edges than RMBG 2.0 on hair, fur, glass, smoke and other fine or see-through detail. In Bria's blind test on 234 hard images it gave the best or tied-best cutout on 185, more than Photoroom, remove.bg, Ideogram, BiRefNet or RMBG 2.0. It is trained only on licensed data and takes a few seconds per image; for speed and high volume use bria/remove-background (RMBG 2.0).

Model Info|   
---|---  
Terms and License| [link ↗](https://bria.ai/terms-of-use)  
More information| [link ↗](https://docs.bria.ai/whats-new/rmbg-3)  
Pricing| 

  * Per image$0.018

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bria/rmbg-3.0',
      {
        image:
          'https://docs.bria.ai/assets/hair-in.ecdf8abae813b036bf5f0db7f48f2e8128a2c2c7f24504803c798d87a63750e4.3d71a9a0.webp',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bria/rmbg-3.0",
      "input": {
        "image": "https://docs.bria.ai/assets/hair-in.ecdf8abae813b036bf5f0db7f48f2e8128a2c2c7f24504803c798d87a63750e4.3d71a9a0.webp"
      }
    }'

![Loose Curly Hair](https://examples.aig.cloudflare.com/bria/rmbg-3.0/loose-curly-hair.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/bria/rmbg-3.0/loose-curly-hair.png"
      }
    }

## Examples

**See-Through Glassware** — Remove the background behind wine glasses and a glass carafe while the glass stays see-through. Input from Bria's RMBG 3.0 launch page.
    
    
    const response = await env.AI.run(
      'bria/rmbg-3.0',
      {
        image:
          'https://docs.bria.ai/assets/glass-in.93980e97cdade22040b0254f2a98edd7735e0fa32d800bebe8da60c4d2635ca8.3d71a9a0.webp',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bria/rmbg-3.0",
      "input": {
        "image": "https://docs.bria.ai/assets/glass-in.93980e97cdade22040b0254f2a98edd7735e0fa32d800bebe8da60c4d2635ca8.3d71a9a0.webp"
      }
    }'

![See-Through Glassware](https://examples.aig.cloudflare.com/bria/rmbg-3.0/see-through-glassware.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/bria/rmbg-3.0/see-through-glassware.png"
      }
    }

**Wisps of Smoke** — Isolate incense smoke from a patterned textile, keeping the semi-transparent wisps. Input from Bria's RMBG 3.0 launch page.
    
    
    const response = await env.AI.run(
      'bria/rmbg-3.0',
      {
        image:
          'https://docs.bria.ai/assets/smoke-in.5cd10f54a22f918882c091233932184895c120b58d382728d97b83c692216773.3d71a9a0.webp',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bria/rmbg-3.0",
      "input": {
        "image": "https://docs.bria.ai/assets/smoke-in.5cd10f54a22f918882c091233932184895c120b58d382728d97b83c692216773.3d71a9a0.webp"
      }
    }'

![Wisps of Smoke](https://examples.aig.cloudflare.com/bria/rmbg-3.0/wisps-of-smoke.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/bria/rmbg-3.0/wisps-of-smoke.png"
      }
    }

## Parameters

image

`string`requiredminLength: 1JPEG, PNG, or WEBP image, a public URL or base64-encoded image data (a `data:` URI prefix is accepted).

preserve_alpha

`boolean`Keep partial transparency from the input alpha channel. When false, every foreground pixel is fully opaque. Default true.

visual_input_content_moderation

`boolean`Reject the request if the input image fails content moderation. Default false.

visual_output_content_moderation

`boolean`Fail the request if the result fails content moderation. Default false.

image

`string`format: uriURL of the PNG cutout with a transparent background. Bria hosts it for a limited time (3 days by default); download it to keep it.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bria/rmbg-3.0/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bria/rmbg-3.0/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bria/rmbg-3.0/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bria/rmbg-3.0/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
