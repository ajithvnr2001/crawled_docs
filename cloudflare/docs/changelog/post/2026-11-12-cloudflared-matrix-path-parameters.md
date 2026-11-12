---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-cloudflared-matrix-path-parameters/
title: Cloudflare Tunnel extends URL normalization \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.765283+00:00
---

# Cloudflare Tunnel extends URL normalization · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-cloudflared-matrix-path-parameters/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Cloudflare Tunnel extends URL normalization

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting from version `2026.11.0`, [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) extends the [URL normalization introduced in `2026.10.0`](https://developers.cloudflare.com/changelog/post/2026-10-22-cloudflared-path-normalization/). Normalization now handles semicolon-delimited path parameters before matching ingress rules. This improves security for tunnels with rules that require Cloudflare Access validation. The URL path sent to your origin stays the same.

Starting 2027-02-08, new `cloudflared` releases will turn on URL normalization by default. This replaces the previously announced date of 2027-01-25, giving you time to test the updated behavior. Upgrade to version `2026.11.0` or later and test your path-based routing before that date, including rules that match paths containing semicolons. Configurations without rules requiring Access validation are unaffected.

This setting is currently off by default. To turn it on, run:
    
    
    cloudflared tunnel --disable-path-normalization=false run <TUNNEL_NAME_OR_UUID>

Alternatively, set `TUNNEL_DISABLE_PATH_NORMALIZATION=false` on each `cloudflared` replica and restart it.

For more information, refer to [ingress matching](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/#how-traffic-is-matched) and [Access validation at the origin](https://developers.cloudflare.com/tunnel/reference/origin-parameters/#access).
