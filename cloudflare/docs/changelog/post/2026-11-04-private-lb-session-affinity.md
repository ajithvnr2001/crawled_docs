---
url: https://developers.cloudflare.com/changelog/post/2026-11-04-private-lb-session-affinity/
title: Steer Cloudflare One users and private networks to the same endpoint with session affinity and hash steering in private load balancers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:07.751703+00:00
---

# Steer Cloudflare One users and private networks to the same endpoint with session affinity and hash steering in private load balancers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-04-private-lb-session-affinity/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 4, 2026

## Steer Cloudflare One users and private networks to the same endpoint with session affinity and hash steering in private load balancers

[Load Balancing](https://developers.cloudflare.com/load-balancing/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Private load balancers](https://developers.cloudflare.com/load-balancing/private-network/) can now keep each user on the same endpoint. This helps with applications that keep session state on a single server.

Cloudflare One Client or Cloudflare WAN site

Connects to `100.112.0.0`

[Private load balancer](https://developers.cloudflare.com/load-balancing/private-network/)

Picks a healthy endpoint based on your steering policy

[Health monitors](https://developers.cloudflare.com/load-balancing/monitors/)[Steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)[Session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/#private-load-balancers)

  * Pool 1

[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

    * `10.0.0.1`vnet-a
  * Pool 2

[Cloudflare Mesh node](https://developers.cloudflare.com/mesh/)

    * `10.1.0.1`default
  * Pool 3

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

    * `10.2.0.1`default



Endpoint = IP address + virtual network

Two options are available:

  * **Hash endpoint steering.** In the dashboard, set a pool's **Endpoint steering** to [**Hash**](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering/#private-load-balancers). Each user is mapped to an endpoint within the pool.
  * **Session affinity.** With the API, set `session_affinity` to `ip_cookie` on the load balancer. Each user stays on the same endpoint while it remains healthy and your pools do not change. Refer to [Session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/#private-load-balancers).



For traffic from the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), Cloudflare identifies the user by their device, so a user stays on the same endpoint even if their IP address changes. For other traffic, such as from a [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) site, Cloudflare uses the source IP address.

This works for endpoints reached through Cloudflare Tunnel, Cloudflare Mesh, and Cloudflare WAN. Affinity pins the endpoint, not the `cloudflared` or Mesh replica that carries the traffic.

To learn how private load balancing fits with your connectors, refer to [Load balance private network traffic](https://developers.cloudflare.com/cloudflare-one/networks/load-balancing/).
