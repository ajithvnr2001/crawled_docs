---
url: https://developers.cloudflare.com/email-service/
title: Cloudflare Email Service \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:38:31.422691+00:00
---

# Cloudflare Email Service · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/

  1. [Home](https://developers.cloudflare.com/)
  2. /Email Service



# Cloudflare Email Service

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesRelated productsMore resources

Send transactional email and route incoming email with Cloudflare Email Service. Arbitrary-recipient sending requires Workers Paid, while routing supports Workers Free and Paid.

Cloudflare Email Service sends transactional email and handles incoming email.

  * **Email Sending** Beta sends outbound transactional emails. 

Available on Workers Paid plan

  * **Email Routing** processes incoming emails with Workers or forwards them to destination addresses. 

Available on Free and Paid plans




Note

Sending to [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#destination-addresses) in your account is free on Workers Free and Paid plans, even when only Email Routing is configured.

Use Email Sending for account emails, order confirmations, and alerts. Use Email Routing to process or forward incoming messages.

Send email through the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/), [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/), or [authenticated SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/).

[Get started](https://developers.cloudflare.com/email-service/get-started/)

* * *

## Features

[Email Sending](https://developers.cloudflare.com/email-service/get-started/send-emails/)

Send transactional emails from Workers or other applications.

Use Email Sending

[Email Routing](https://developers.cloudflare.com/email-service/get-started/route-emails/)

Route incoming emails to custom addresses, Workers, or external destinations.

Use Email Routing

[Deliverability](https://developers.cloudflare.com/email-service/concepts/deliverability/)

Review email authentication and sender reputation factors.

Use Deliverability

[Analytics & Observability](https://developers.cloudflare.com/email-service/observability/)

Review sending and routing activity, metrics, and analytics.

Use Analytics & Observability

[API](https://developers.cloudflare.com/email-service/api/)

Send and route emails using the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/), [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/), or [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/).

Use API

* * *

## Related products

[Workers](https://developers.cloudflare.com/workers/)

Send and process email from Workers.

[Queues](https://developers.cloudflare.com/queues/)

Send Email Sending events to a queue.

[Analytics Engine](https://developers.cloudflare.com/analytics/)

Store custom metrics from email Workers.

* * *

## More resources

### [Platform limits](https://developers.cloudflare.com/email-service/platform/limits/)

Review Email Service limits and quotas.

### [Pricing](https://developers.cloudflare.com/email-service/platform/pricing/)

Review Email Service pricing and plans.

### [Examples](https://developers.cloudflare.com/email-service/examples/)

View Email Service code examples.

### [Discord](https://discord.cloudflare.com)

Ask questions and discuss Email Service with other developers.

### [Twitter](https://x.com/cloudflaredev)

Follow product announcements and developer updates.

[NextSend emails](https://developers.cloudflare.com/email-service/get-started/send-emails/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
