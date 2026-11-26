---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-activate-pay-as-you-go-cli-mcp/
title: Activate Cloudflare subscriptions from the CLI and MCP \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.641179+00:00
---

# Activate Cloudflare subscriptions from the CLI and MCP · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-activate-pay-as-you-go-cli-mcp/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## Activate Cloudflare subscriptions from the CLI and MCP

[Billing](https://developers.cloudflare.com/billing/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You and your agents can now activate Cloudflare subscriptions from the [Cloudflare CLI](https://developers.cloudflare.com/cf/) (`cf`) or [Cloudflare Model Context Protocol (MCP) servers](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/), without switching to the dashboard.

Previously, OAuth sessions used by `cf` and MCP could not create subscriptions, so activating a product meant leaving your terminal or agent session to complete checkout in the dashboard. You can now activate subscriptions in place for common workflows:

  * **[Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/)** : Move beyond [Free plan limits](https://developers.cloudflare.com/workers/platform/limits/#account-plan-limits) such as 100,000 requests per day and 10 ms of CPU time, with 10 million requests and 30 million CPU milliseconds included each month for $5 per month plus usage.
  * **[R2](https://developers.cloudflare.com/r2/pricing/)** : Activate an R2 subscription to start creating buckets, with 10 GB of free monthly storage plus usage-based billing beyond the free tier.
  * **[Zero Trust](https://developers.cloudflare.com/cloudflare-one/setup/)** : Sign up for Zero Trust (with up to 50 users included on the Free plan) to put a Worker behind [Cloudflare Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/).



To use this from the CLI, update to `cf` `1.0.0-rc.5` or later and reauthenticate with `cf auth login` so your session receives the updated OAuth scopes. Your account must also have a verified email address and an existing [billing profile with a payment method on file](https://developers.cloudflare.com/billing/get-started/create-billing-profile/).

In MCP clients that support the MCP `2026-07-28` specification and [MCP elicitation ↗︎](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation), Cloudflare displays the plan price and asks for your permission before activating a subscription on your account. Clients that do not support elicitation are directed to the dashboard.

For more information, refer to [Usage-based billing](https://developers.cloudflare.com/billing/understand/usage-based-billing/) and [Use cf with coding agents](https://developers.cloudflare.com/cf/agents/).
