---
url: https://developers.cloudflare.com/agents/tools/payments/mpp/
title: MPP (Machine Payments Protocol) \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:24.566857+00:00
---

# MPP (Machine Payments Protocol) · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/payments/mpp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

Tools

  4. /[Agentic Payments](https://developers.cloudflare.com/agents/tools/payments/)
  5. /MPP (Machine Payments Protocol)



# MPP (Machine Payments Protocol)

Last updated Aug 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/tools/payments/mpp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksPayment intentsCompatibility with x402Build on CloudflareSDKsRelated

[Machine Payments Protocol (MPP) ↗︎](https://mpp.dev) is an open protocol for machine-to-machine payments. It standardizes the HTTP `402 Payment Required` status code with a formal authentication scheme proposed to the [IETF ↗︎](https://paymentauth.org). MPP gives agents, applications, and people one interface to pay for a service in the same HTTP request.

MPP is payment-method agnostic. It supports stablecoins, cards through Stripe, and custom payment methods. A service can offer more than one method.

## How it works

  1. An Agent or HTTP client requests a paid resource.
  2. The service returns `402 Payment Required` with a payment Challenge.
  3. The client fulfills the payment.
  4. The client retries with a payment Credential.
  5. The service returns the resource with a payment Receipt.



HTTP services exchange payment data in authentication headers. Model Context Protocol (MCP) tools use the same flow through JSON-RPC.

## Payment intents

MPP defines three payment intents:

  * **`charge`** — Collect a one-time payment.
  * **`session`** — Charge for measured usage.
  * **`subscription`** — Sell recurring access.



For more information, refer to [MPP payment intents ↗︎](https://mpp.dev/intents/).

## Compatibility with x402

MPP is backwards-compatible with [x402](https://developers.cloudflare.com/agents/tools/payments/x402/). MPP clients can consume existing x402 services without changes to those services.

## Build on Cloudflare

### [Accept payments](https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/)

Charge for a Worker route or an MCP tool

### [Pay from the Agents SDK](https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/)

Pay HTTP services and MCP tools from a Cloudflare Agent

## SDKs

MPP provides SDKs for TypeScript, Python, Rust, Go, and Ruby. The Cloudflare guides use the TypeScript [`mppx` SDK ↗︎](https://mpp.dev/sdk/typescript/).

For current packages and integrations, refer to the [MPP SDK documentation ↗︎](https://mpp.dev/sdk/).

## Related

  * [mpp.dev ↗︎](https://mpp.dev) — Protocol documentation and guides
  * [IETF specification ↗︎](https://paymentauth.org) — Payment HTTP Authentication Scheme
  * [Pay Per Crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/) — Cloudflare-native web content monetization



[PreviousPay from coding tools](https://developers.cloudflare.com/agents/tools/payments/x402/pay-with-tool-plugins/)[NextAccept payments with MPP](https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/payments/mpp/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
