---
url: https://developers.cloudflare.com/changelog/post/2026-10-19-precursor-monitor-mode/
title: Precursor adds Monitor mode \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:09:47.668243+00:00
---

# Precursor adds Monitor mode · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-19-precursor-monitor-mode/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 19, 2026

## Precursor adds Monitor mode

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We released Monitor mode at customers' request so they can test Precursor and the Precursor Interstitial without updating bot score.

In **Security** > **Settings** , the Precursor **Status** dropdown now offers _Off_ , _Monitor_ , and _Arm_. Selecting _Arm_ means Precursor detections can affect bot score and Challenge clearance. Selecting _Monitor_ means Precursor detections do not affect bot score or Challenge clearance.

![Precursor Status dropdown with Off, Monitor, and Arm options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=739,height=235,format=webp/_astro/precursor-monitor-mode-status.CRb5Sudr.png)

We also separated the Precursor Interstitial from the mode. Set the sitewide default with **Show Interstitial** , then add **Interstitial Rules** to customize it for specific requests. For example, leave **Show Interstitial** off across most of your site, but require an interstitial Challenge on `/checkout` to enforce a valid session before purchase.

![Precursor settings with Show Interstitial off and an Open interstitial rules button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=600,height=441,format=webp/_astro/precursor-interstitial-settings.Bpb_aV0o.png)

For more information, refer to the [**Precursor**](https://developers.cloudflare.com/cloudflare-challenges/precursor/) documentation.
