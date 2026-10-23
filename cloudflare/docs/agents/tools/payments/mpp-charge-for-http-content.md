---
url: https://developers.cloudflare.com/agents/tools/payments/mpp-charge-for-http-content/
title: Charge for HTTP content \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:24.361109+00:00
---

# Charge for HTTP content · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/payments/mpp-charge-for-http-content/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

Tools

  4. /[Agentic Payments](https://developers.cloudflare.com/agents/tools/payments/)
  5. /Charge for HTTP content



# Charge for HTTP content

Last updated Aug 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/tools/payments/mpp-charge-for-http-content/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesConfigurationSelective gating with Bot ManagementDeployCustom Worker endpointsRelated

The [mpp-proxy ↗︎](https://github.com/cloudflare/mpp-proxy) template is a Cloudflare Worker that sits in front of any HTTP backend. When a request hits a protected route, the proxy returns a `402` response with an MPP payment challenge. After the client pays, the proxy verifies the payment, forwards the request to your origin, and issues a 1-hour session cookie.

Deploy the mpp-proxy template to your Cloudflare account:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/mpp-proxy)

## Prerequisites

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up)
  * An HTTP backend to gate
  * A wallet address to receive payments



## Configuration

Define protected routes in `wrangler.jsonc`:
    
    
    {
    	"vars": {
    		"PAY_TO": "0xYourWalletAddress",
    		"TEMPO_TESTNET": false,
    		"PAYMENT_CURRENCY": "0x20c000000000000000000000b9537d11c60e8b50",
    		"PROTECTED_PATTERNS": [
    			{
    				"pattern": "/premium/*",
    				"amount": "0.01",
    				"description": "Access to premium content for 1 hour"
    			}
    		]
    	}
    }

Note

Set `TEMPO_TESTNET` to `true` and `PAYMENT_CURRENCY` to `0x20c0000000000000000000000000000000000000` for testnet development.

## Selective gating with Bot Management

With [Bot Management](https://developers.cloudflare.com/bots/), the proxy can charge crawlers while keeping the site free for humans:
    
    
    {
    	"pattern": "/content/*",
    	"amount": "0.25",
    	"description": "Content access for 1 hour",
    	"bot_score_threshold": 30,
    	"except_detection_ids": [120623194, 117479730]
    }

Requests with a bot score at or below `bot_score_threshold` are directed to the paywall. Use `except_detection_ids` to allowlist specific crawlers by [detection ID](https://developers.cloudflare.com/ai-crawl-control/reference/bots/).

## Deploy

Clone the template, edit `wrangler.jsonc`, and deploy:
    
    
    git clone https://github.com/cloudflare/mpp-proxy
    cd mpp-proxy
    npm install
    npx wrangler secret put JWT_SECRET
    npx wrangler secret put MPP_SECRET_KEY
    npx wrangler deploy

For full configuration options, proxy modes, and Bot Management examples, refer to the [mpp-proxy README ↗︎](https://github.com/cloudflare/mpp-proxy).

## Custom Worker endpoints

To add MPP middleware directly to a Worker, refer to [Accept payments with MPP](https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/#charge-for-a-worker-route).

## Related

  * [mpp.dev ↗︎](https://mpp.dev) — Protocol specification
  * [Pay Per Crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/) — Cloudflare-native monetization without custom code



[PreviousOverview](https://developers.cloudflare.com/agents/tools/payments/)[NextOverview](https://developers.cloudflare.com/agents/tools/payments/x402/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/payments/mpp-charge-for-http-content.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
