---
url: https://developers.cloudflare.com/changelog/post/2026-10-22-granular-read-and-monitor-ga/
title: Granular Tunnel Read And Monitor role is generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.591643+00:00
---

# Granular Tunnel Read And Monitor role is generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-22-granular-read-and-monitor-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 22, 2026

## Granular Tunnel Read And Monitor role is generally available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-22-granular-read-and-monitor-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The **Cloudflare Tunnel - Granular Connector cloudflared Read And Monitor** role is now generally available. You can grant a member read access and log streaming for specific [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances without granting write access or access to every Tunnel in your account.

This role includes the same access as **Cloudflare Tunnel - Granular Connector cloudflared Read** : viewing selected Tunnels, their IP and hostname routes, and connector host details. It also grants [remote log streaming](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming), so support operators can troubleshoot a Tunnel without changing its configuration. The existing **Read** role does not grant log streaming access.

To assign the role, follow [Grant a granular permission](https://developers.cloudflare.com/tunnel/guides/granular-permissions/#grant-a-granular-permission). For the available roles, refer to the [resource-scoped roles reference](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles).
