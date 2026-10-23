---
url: https://developers.cloudflare.com/changelog/post/2026-10-15-gateway-workers-public-beta/
title: Gateway and Workers integration is now in public beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.542696+00:00
---

# Gateway and Workers integration is now in public beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-15-gateway-workers-public-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 15, 2026

## Gateway and Workers integration is now in public beta

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Workers](https://developers.cloudflare.com/workers/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Gateway now integrates with Cloudflare Workers in public beta on all Zero Trust plans. You can use the **Forward** action in [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-controls/http-policies/) to run your own code on matching, permitted traffic without managing a separate proxy.

The **Forward** action lets you transform HTTP requests and responses, return a coaching page, or run background tasks such as Slack notifications and R2 captures. Your Worker receives the request and [Gateway context](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/), including connection metadata, user identity, and device posture when available.

![A matching Gateway Forward policy sends HTTP traffic to a Worker, which processes requests and responses for Internet or private-network upstream services.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2048,height=1053,format=webp/_astro/gateway-workers-forward.CFUFJAE0.png)

Gateway handles the proxy connection, TLS decryption, and upstream routing. It evaluates HTTP request policies before Forward policies and inspects the final response before returning it to the user.

Gateway inspects the original request body before delivering it to your Worker. A body-inspection Block decision can interrupt the Worker.

To get started, [deploy a Worker and configure a Forward policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/), or adapt one of the [Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/).
