---
url: https://developers.cloudflare.com/email-service/platform/pricing/
title: Pricing \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:49.197179+00:00
---

# Pricing · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPlan pricing

Cloudflare Email Service pricing is based on your Cloudflare plan and email usage.

## Plan pricing

Email Sending and Email Routing are available on both the Workers Free and Workers Paid plans. On the Workers Free plan, Email Sending sends only to [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/destination-addresses/) in your account. Sending to any other recipient requires the Workers Paid plan.

| Outbound emails (Email Sending) | Inbound emails (Email Routing)  
---|---|---  
**Workers Free** | Free, to verified destination addresses only | Unlimited  
**Workers Paid** | 3,000 included per month, then $0.35 per 1,000 emails | Unlimited  
  
The 3,000 included emails apply per account, per month, aligned with your Cloudflare subscription billing cycle. Emails that hard-bounce or are otherwise accepted by Email Service count toward the quota. Emails rejected at the API boundary, including sends blocked by the [suppression list](https://developers.cloudflare.com/email-service/concepts/suppressions/), do not count toward the quota.

Sends to verified destination addresses are free on every plan, including when only Email Routing is configured. They do not count toward the included quota.

Email Routing Workers is billed according to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

[PreviousLimits](https://developers.cloudflare.com/email-service/platform/limits/)[NextChangelog](https://developers.cloudflare.com/email-service/platform/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
