---
url: https://developers.cloudflare.com/email-service/configuration/destination-addresses/
title: Destination addresses \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.394925+00:00
---

# Destination addresses · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/configuration/destination-addresses/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Configuration
  4. /Destination addresses



# Destination addresses

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSend to destination addressesAdd a destination addressManage destination addresses

A destination address is a verified email address in your account. Email Routing forwards messages to destination addresses, and Email Sending can send to them.

Destination addresses are shared at the account level and can be reused with any other domain in your account. Before you can create a [routing rule](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/), you must add and verify at least one destination address.

## Send to destination addresses

You can send to verified destination addresses directly through the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) or the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/), free of charge on any plan — including when only Email Routing is configured. From an onboarded [sending domain](https://developers.cloudflare.com/email-service/configuration/domains/), you can also send to them over [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/). Sends to verified destination addresses do not count toward your monthly quota or daily sending limits.

On the Workers Free plan, Email Sending sends only to verified destination addresses. Refer to [Limits](https://developers.cloudflare.com/email-service/platform/limits/#verified-destination-addresses) and [Pricing](https://developers.cloudflare.com/email-service/platform/pricing/) for details.

## Add a destination address

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account.

  2. Go to **Compute** > **Email Service** > **Email Routing** > **Destination Addresses**.

[ Go to **Email Routing** ↗ ](https://dash.cloudflare.com/?to=/:account/email-service/routing)
  3. Under **Destination addresses** , enter the email address you want to use as a destination in the inline form and submit it.

  4. Cloudflare sends a verification email to that address. Open the email and select **Verify email address** to activate it.




Until a destination address is verified, any routing rule that points to it stays disabled.

## Manage destination addresses

The **Destination Addresses** page lists every address on your account, including those pending verification. From this page you can resend a verification email or delete a destination address.

Note

Deleting a destination address automatically disables all routing rules that use that address as a destination.

[PreviousDomain configuration](https://developers.cloudflare.com/email-service/configuration/domains/)[NextEmail routing rules](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/configuration/destination-addresses.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
