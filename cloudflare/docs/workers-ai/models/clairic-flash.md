---
url: https://developers.cloudflare.com/workers-ai/models/clairic-flash/
title: clairic-flash (Cloudflare) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:05.271046+00:00
---

# clairic-flash (Cloudflare) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/clairic-flash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![Cloudflare logo](https://developers.cloudflare.com/_astro/cloudflare.DP8rkHys.svg)

# clairic-flash

Text Generation • Cloudflare

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`@cf/cloudflare/clairic-flash`Copy

  * Cloudflare-hosted
  * Vision
  * Zero data retention



Clairic is a System One-style model that can extract, compute, estimate, and forecast values from inputs. It is strongly typed and outputs confidence scores and probabilities against its outputs. This model is in early research preview from the Cloudflare Workers AI team.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 65,536 tokens  
Terms and License| link  
Vision| Yes  
Zero data retention| Yes  
Unit Pricing| $0.10 per M input tokens  
  
How media inputs are billed

Clairic converts media inputs to input tokens and bills them at the input token rate for the model. Clairic does not charge for output tokens. For per-model rates, refer to [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Clairic answers each `text` field in its own pass. Other fields share a pass, and Clairic splits fields that do not fit beside the `state` and images in one pass across more passes. Every pass includes the full `state` and all images, so Clairic bills their tokens once per pass. `usage.passes` reports the number of passes.

Clairic tokenizes images as follows:

  1. **Resize** : Clairic keeps the image aspect ratio, but: 
     * Rounds each side to a multiple of 32 pixels.
     * Scales up images with an area under about 65,000 pixels (256x256) to reach that area.
     * Does not scale down larger images.
  2. **Count patches** : Each 32x32-pixel block is one token: `tokens = (width / 32) x (height / 32)`.
  3. **Add markers** : Clairic adds two tokens to mark where the image starts and ends.



Each request accepts up to four images (4 MiB each, 8 MiB combined).

Media tokens count toward the context window of the model on every pass, together with the fields. If giving each `text` field its own pass would exceed the context window, Clairic combines fields into fewer passes. If the request still does not fit, it fails. Otherwise, Clairic truncates the text `state` to fit the remaining space.

## Usage
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const response = await env.AI.run("@cf/cloudflare/clairic-flash", {
    			model: "clairic-flash",
    			state: "Invoice INV-2291 from Northwind Supply, issued 2026-09-02, net 30. 4 pallets at $250.00 each, shipping $80.00. Contact: Dana Ruiz, Priya Shah.",
    			fields: {
    				invoice_number: { type: "text" },
    				due_date: {
    					type: "date",
    					instructions: "Issue date plus the net payment days",
    				},
    				total: {
    					type: "number",
    					decimals: 2,
    					unit: "USD",
    					instructions: "Amount due including shipping",
    				},
    				contacts: { type: "list", items: "text" },
    				po_number: { type: "text", instructions: "Purchase order number" },
    				days_to_pay: {
    					type: "estimate",
    					min: 0,
    					max: 120,
    					step: 1,
    					instructions: "Days after issue until this invoice is paid",
    				},
    			},
    		});
    
    		// response.answers.invoice_number -> exact span of the state, with character offsets
    		// response.answers.due_date       -> date worked out from the issue date and terms
    		// response.answers.po_number      -> null: the invoice has no PO number
    		// response.answers.days_to_pay    -> median and 80% interval (p10 to p90)
    		return Response.json(response);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/cloudflare/clairic-flash",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
            "model": "clairic-flash",
            "state": "Invoice INV-2291 from Northwind Supply, issued 2026-09-02, net 30. 4 pallets at $250.00 each, shipping $80.00. Contact: Dana Ruiz, Priya Shah.",
            "fields": {
                "invoice_number": {"type": "text"},
                "due_date": {
                    "type": "date",
                    "instructions": "Issue date plus the net payment days",
                },
                "total": {
                    "type": "number",
                    "decimals": 2,
                    "unit": "USD",
                    "instructions": "Amount due including shipping",
                },
                "contacts": {"type": "list", "items": "text"},
                "po_number": {"type": "text", "instructions": "Purchase order number"},
                "days_to_pay": {
                    "type": "estimate",
                    "min": 0,
                    "max": 120,
                    "step": 1,
                    "instructions": "Days after issue until this invoice is paid",
                },
            },
        },
    )
    print(response.json())
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/cloudflare/clairic-flash \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{
        "model": "clairic-flash",
        "state": "Invoice INV-2291 from Northwind Supply, issued 2026-09-02, net 30. 4 pallets at $250.00 each, shipping $80.00. Contact: Dana Ruiz, Priya Shah.",
        "fields": {
          "invoice_number": { "type": "text" },
          "due_date": { "type": "date", "instructions": "Issue date plus the net payment days" },
          "total": { "type": "number", "decimals": 2, "unit": "USD", "instructions": "Amount due including shipping" },
          "contacts": { "type": "list", "items": "text" },
          "po_number": { "type": "text", "instructions": "Purchase order number" },
          "days_to_pay": {
            "type": "estimate",
            "min": 0,
            "max": 120,
            "step": 1,
            "instructions": "Days after issue until this invoice is paid"
          }
        }
      }'

## Parameters

model

`string`requireddefault: clairic-flashpattern: ^(clairic-flash|@cf/cloudflare/clairic-flash)$Required. The model selector: "clairic-flash".

state

`string`default: The text to read and predict from. Must be non-empty unless images or documents are sent. Text answers are spans of this string.

▶fields{}

`object`requiredminProperties: 1Required. Map of field name to a typed field spec. At least one field; no upper limit. Each prompt (state plus fields) must fit in 65,273 input tokens; input is never truncated and oversized requests are rejected. Unknown keys for a field's type are rejected.

▶images[]

`array`maxItems: 4Optional embedded PNG, JPEG or WebP images placed before the state (max 4; 4 MiB each, 8 MiB total decoded across images and documents; request body max 16 MiB). Remote URLs are not accepted.

▶documents[]

`array`maxItems: 4Optional embedded PDFs (4 MiB each). Rendered pages plus images must total at most 4. Encrypted PDFs are rejected.

reference_date

`string`ISO date that anchors dates written without a year.

▶options{}

`object`

model

`string`Always "clairic-flash", whichever selector was sent.

▶answers{}

`object`One answer per field, keyed by field name. value is null when the input does not determine it. Generated answers (text, number, boolean, enum, object, source_only fields, lists) carry valid/complete/decoder metadata; typed answers (date, time, datetime, duration, compute) carry guess instead.

truncated

`boolean`True when any generated answer or list is invalid or incomplete. Input is never truncated.

state_text

`string`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/clairic-flash/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/clairic-flash/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/clairic-flash/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/clairic-flash/schema-output.json "Download")

## Terms

You may access or use this model at your sole discretion. Cloudflare does not make any representations, warranties, or guarantees regarding the model, including, but not limited to, as to its continued availability and integrity. If Cloudflare makes the model available to you, it is on an “AS IS” and “AS AVAILABLE” basis, and Cloudflare has no obligation to indemnify you for any claims arising from your use of the model. Cloudflare may cease providing it without entitling you to any refund, credit, or other compensation. Cloudflare will not be directly or indirectly responsible or liable to you in any manner, for any harms, damages, loss, lost profits, special or consequential damages, or claims, arising out of or in connection with the use of, or reliance on the performance of the model.

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
