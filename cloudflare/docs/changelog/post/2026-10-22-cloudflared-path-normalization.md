---
url: https://developers.cloudflare.com/changelog/post/2026-10-22-cloudflared-path-normalization/
title: Cloudflare Tunnel supports URL normalization \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.504581+00:00
---

# Cloudflare Tunnel supports URL normalization · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-22-cloudflared-path-normalization/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 22, 2026

## Cloudflare Tunnel supports URL normalization

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-22-cloudflared-path-normalization/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting from version `2026.10.0`, [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) can normalize URLs before matching ingress rules. This improves security for tunnels with rules that require Cloudflare Access validation. The URL path sent to your origin stays the same.

In three months, starting 2027-01-25, new `cloudflared` releases will turn on URL normalization by default. Test your path-based routing before that date, as this change may affect which ingress rule matches a request. Configurations without rules requiring Access validation are unaffected.

This setting is currently off by default. To turn it on, run:
    
    
    cloudflared tunnel --disable-path-normalization=false run <TUNNEL_NAME_OR_UUID>

Alternatively, set `TUNNEL_DISABLE_PATH_NORMALIZATION=false` on each `cloudflared` replica and restart it.

For more information, refer to [ingress matching](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/#how-traffic-is-matched) and [Access validation at the origin](https://developers.cloudflare.com/tunnel/reference/origin-parameters/#access).
