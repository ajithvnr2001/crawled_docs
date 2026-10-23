---
url: https://developers.cloudflare.com/ai/models/%40cf/cloudflare/clairic/
title: clairic (Cloudflare) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:38.862742+00:00
---

# clairic (Cloudflare) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/cloudflare/clairic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Cloudflare logo](https://developers.cloudflare.com/_astro/cloudflare.DP8rkHys.svg)

# clairic

Text Generation • Cloudflare

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/cloudflare/clairic`

  * Cloudflare-hosted
  * Vision



Clairic is a System One-style model that can extract, compute, estimate, and forecast values from inputs. It is strongly typed and outputs confidence scores and probabilities against its outputs. This model is in preview from the Cloudflare Workers AI team.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 65,536 tokens  
Terms and License| link  
Vision| Yes  
Unit Pricing| $0.10 per M input tokens  
  
## Usage
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const response = await env.AI.run("@cf/cloudflare/clairic", {
    			model: "clairic",
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
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/cloudflare/clairic",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
            "model": "clairic",
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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/cloudflare/clairic \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{
        "model": "clairic",
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
    
    
    {
      "model": "clairic",
      "answers": {
        "invoice_number": {"type": "text", "p_null": 3.8e-10, "span": [8, 16], "guess": "INV-2291", "confidence": 1, "value": "INV-2291"},
        "due_date": {"type": "date", "p_null": 1.9e-08, "guess": "2026-10-02", "confidence": 0.9999, "value": "2026-10-02"},
        "total": {"type": "number", "p_null": 2.3e-08, "guess": 1080, "confidence": 0.9999, "value": 1080},
        "contacts": {"type": "list", "value": ["Dana Ruiz", "Priya Shah"], "spans": [[120, 129], [131, 141]], "confidence": 0.9999},
        "po_number": {"type": "text", "p_null": 1, "span": [8, 16], "guess": "INV-2291", "confidence": 0.9995, "value": null},
        "days_to_pay": {"type": "estimate", "value": 30, "mean": 29.535, "median": 30, "p10": 21, "p90": 38, "p_below": 5.9e-06, "p_above": 1.2e-05}
      },
      "truncated": false,
      "usage": {"state_tokens": 61, "image_tokens": 0, "schema_tokens": 472, "input_tokens": 655, "output_tokens": 0, "passes": 3}
    }

## Parameters

model

`string`requireddefault: clairicpattern: ^(clairic|@cf/cloudflare/clairic)$Required. The model selector: "clairic".

state

`string`default: The text to read and predict from. Must be non-empty unless images are sent. Text answers are spans of this string.

▶fields{}

`object`requiredminProperties: 1Required. Map of field name to a typed field spec. At least one field; no upper limit. Fields that do not fit next to the state in one 8,192-token pass are split across parallel passes.

▶images[]

`array`maxItems: 4Optional embedded PNG, JPEG or WebP images placed before the state (max 4; 4 MiB each, 8 MiB total decoded; request body max 16 MiB). Remote URLs are not accepted.

reference_date

`string`ISO date that anchors dates written without a year.

▶options{}

`object`

model

`string`

▶answers{}

`object`One answer per field, keyed by field name. value is null when the input does not determine it.

truncated

`boolean`

state_text

`string`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clairic/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clairic/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clairic/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clairic/schema-output.json "Download")

## Terms

You may access or use this model at your sole discretion. Cloudflare does not make any representations, warranties, or guarantees regarding the model, including, but not limited to, as to its continued availability and integrity. If Cloudflare makes the model available to you, it is on an “AS IS” and “AS AVAILABLE” basis, and Cloudflare has no obligation to indemnify you for any claims arising from your use of the model. Cloudflare may cease providing it without entitling you to any refund, credit, or other compensation. Cloudflare will not be directly or indirectly responsible or liable to you in any manner, for any harms, damages, loss, lost profits, special or consequential damages, or claims, arising out of or in connection with the use of, or reliance on the performance of the model.

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
