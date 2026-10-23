---
url: https://developers.cloudflare.com/ai/models/bria/ad-delayer/
title: Ad Delayer (bria) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:05.834737+00:00
---

# Ad Delayer (bria) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bria/ad-delayer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



b

# Ad Delayer

Image-to-Document • bria

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bria/ad-delayer`

  * Third-party



Ad Delayer turns a finished, flat ad image into an editable JSON layer document: a background plate, product and logo cutouts, live text with typography, and vector shapes, with each image layer hosted as its own file. It is designed for flat ads; results for ordinary photographs are not guaranteed. Bria trains it exclusively on licensed data.

Model Info|   
---|---  
Terms and License| [link ↗](https://bria.ai/terms-of-use)  
More information| [link ↗](https://docs.bria.ai/ads/transformations/delayer-ad)  
Pricing| 

  * Per image$0.30

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bria/ad-delayer',
      { image: 'https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/simple-generation.jpg' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bria/ad-delayer",
      "input": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/simple-generation.jpg"
      }
    }'
    
    
    Constructed a layered ad.
    
    
    {
      "state": "Completed",
      "result": {
        "layer_document": "https://examples.aig.cloudflare.com/bria/ad-delayer/concert-poster.json",
        "text": "Constructed a layered ad."
      }
    }

## Parameters

▶image

`one of`required

layer_document

`string`format: uriURL of the JSON layer document: the canvas size, font stylesheets, and z-ordered image, vector, and text layers. Image layers link to their extracted assets through `asset_path`. Bria hosts the document and assets for 30 days.

text

`string`Short summary from Bria of the layers it built.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bria/ad-delayer/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bria/ad-delayer/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bria/ad-delayer/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bria/ad-delayer/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
