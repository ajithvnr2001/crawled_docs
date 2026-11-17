---
url: https://developers.cloudflare.com/waf/payload-logging/view/
title: View the payload content in the dashboard \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-11-17T10:23:32.947155+00:00
---

# View the payload content in the dashboard · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/payload-logging/view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Payload logging](https://developers.cloudflare.com/waf/payload-logging/)
  4. /View the payload content in the dashboard



# View the payload content in the dashboard

Last updated Nov 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

View the content of the matched rule payload in the dashboard by entering your private key.

  1. Open [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/):

     1. In the Cloudflare dashboard, go to the **Analytics** page.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)
     2. Select the **Events** tab.

  2. Under **Sampled logs** , expand the details of an event triggered by a supported rule with payload logging enabled.

  3. Under **Matched service** , select **Decrypt payload match**.

![Example of a security event with available payload match data \(still encrypted\)](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1084,height=335,format=webp/_astro/payload-logging-example.CMWUOj2Y.png)
  4. Enter your private key in the pop-up window and select **Decrypt**.

Note

The private key is not sent to a Cloudflare server. The decryption occurs entirely in the browser.




If the private key you entered decrypts the encrypted payload successfully, the dashboard will show the name of the fields that matched and the matched string in clear text, along with some text appearing before and after the match.

![Viewing the decrypted payload match data after entering your private key in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=460,height=165,format=webp/_astro/payload-decrypted.DoVOmjx4.png)

[PreviousManaged Rules in the dashboard](https://developers.cloudflare.com/waf/payload-logging/configure/)[NextConfigure via API](https://developers.cloudflare.com/waf/payload-logging/configure-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/payload-logging/view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
