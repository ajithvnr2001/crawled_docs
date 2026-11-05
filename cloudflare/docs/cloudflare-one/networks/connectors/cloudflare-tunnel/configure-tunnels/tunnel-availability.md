---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/
title: Tunnel availability and failover \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:10.926169+00:00
---

# Tunnel availability and failover · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Configure a tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/)
  5. /Tunnel availability and failover



# Tunnel availability and failover

Last updated Nov 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewcloudflared replicas When to use cloudflared replicasCloudflare Load Balancers When to use load balancers Types of load balancers

Our lightweight and open-source connector, [`cloudflared` ↗︎](https://github.com/cloudflare/cloudflared), was built to be highly available without any additional configuration requirements. When you run a tunnel, `cloudflared` establishes four outbound-only connections between the origin server and the Cloudflare network. These four connections are made to four different servers spread across at least two distinct data centers. This model ensures high availability and mitigates the risk of individual connection failures. This means in event a single connection, server, or data center goes offline, your resources will remain available.

## `cloudflared` replicas

You can deploy additional instances of `cloudflared` for availability and failover. These instances are called replicas. Each replica establishes four new connections to Cloudflare, providing additional points of ingress to your origin. All replicas point to the same tunnel, so if a single host running `cloudflared` goes down, the remaining replicas continue to serve traffic.

Cloudflare network

Forwards each request to the geographically closest replica

4 outbound connections per replica

Your network

  * cloudflared

Replica 1 on `host-a`

tunnel-01
  * cloudflared

Replica 2 on `host-b`

tunnel-01



Application

Replicas do not support traffic steering (such as round-robin or hash-based routing). When a request arrives at Cloudflare, it is forwarded to the geographically closest replica. If that connection fails, Cloudflare retries with other replicas, but there is no guarantee about which one is chosen. If you need intelligent traffic distribution, use Cloudflare Load Balancers instead.

### When to use `cloudflared` replicas

  * To provide additional points of availability for a single tunnel.
  * To allocate failover nodes within your network.
  * To update the configuration of a tunnel [without downtime](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/#update-with-multiple-cloudflared-instances).



For setup instructions, refer to [Deploy cloudflared replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/).

## Cloudflare Load Balancers

[Cloudflare Load Balancing](https://developers.cloudflare.com/load-balancing/) proactively steers traffic away from unhealthy origins and intelligently distributes the traffic load based on your choice of [steering algorithms](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/). Unlike `cloudflared` replicas which all use the same tunnel, a typical load balancer setup requires creating multiple tunnels. Most customers will create one tunnel per data center and one load balancer pool per tunnel.

  * Internet

  * Cloudflare One Client

  * Cloudflare WAN




[Cloudflare Load Balancer](https://developers.cloudflare.com/load-balancing/)

Steers traffic to healthy tunnels, with one pool per tunnel

  * Data center 1

Tunnel 1

`cloudflared` forwards traffic to your app servers

    * App server
    * App server
  * Data center 2

Tunnel 2

`cloudflared` forwards traffic to your app servers

    * App server
    * App server



### When to use load balancers

  * To intelligently steer traffic based on latency, geolocation, or other signals.
  * To implement failover logic if a tunnel reaches an inactive state.
  * To get a [health alert](https://developers.cloudflare.com/notifications/notification-available/#load-balancing) when a tunnel reaches an inactive state.
  * To distribute traffic more evenly across your Cloudflare Tunnel-accessible origins or endpoints.



For setup instructions, refer to [Public load balancers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/) or [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/) depending on your use case.

### Types of load balancers

There are two types of load balancers that you can use with Cloudflare Tunnel endpoints:

  * [Public load balancers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/) steer traffic from the Internet to applications published on a Cloudflare domain. Use this method if your service is served by Cloudflare Tunnel via a [published application route](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-publish-an-application).
  * [Private load balancers](https://developers.cloudflare.com/load-balancing/private-network/) steer traffic from Cloudflare One Clients, Cloudflare WAN, and other on-ramps to an internal IP on your private network. Use this method if your service is connected to Cloudflare Tunnel via a [CIDR route](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/). To keep each user on the same endpoint, use [hash steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering/#private-load-balancers) or [session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/#private-load-balancers).



Note

[Private hostname routes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) are not currently compatible with Load Balancing. If your service is connected via a hostname route, use `cloudflared` replicas for high availability.

[PreviousTunnel with firewall](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/)[NextDeploy cloudflared replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
