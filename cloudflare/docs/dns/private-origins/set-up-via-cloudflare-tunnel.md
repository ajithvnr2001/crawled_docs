---
url: https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-tunnel/
title: Set up a private origin via Cloudflare Tunnel \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:44.319729+00:00
---

# Set up a private origin via Cloudflare Tunnel · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-tunnel/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Private origins](https://developers.cloudflare.com/dns/private-origins/)
  4. /Set up a private origin via Cloudflare Tunnel



# Set up a private origin via Cloudflare Tunnel

Last updated Nov 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin1\. Create a DNS record with private network routing2\. Verify end-to-end connectivity Check tunnel health Send a request from an external client Confirm traffic on the originCommon pitfallsNext steps

This guide walks you through proxying public hostnames to origins on a private network. The private network is reachable through a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) running `cloudflared`. The CDN, WAF, Cache, and other proxied features apply to this traffic the same way they apply to traffic destined for public origins.

## Before you begin

Confirm the following before you start:

  * **Private Origins available on your account** : contact your account team to enable it.
  * **A healthy`cloudflared` tunnel**: the connector must run on a host that can reach the origin. Refer to [Get started with Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/).
  * **A private network route covering the origin IP** : add a route (CIDR) for the origin's network to the tunnel, in your **default virtual network**. Refer to [Connect a private network CIDR](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/).



Private network routing over Cloudflare Tunnel does not require Unified Routing or return routes for Cloudflare source IP ranges. Your origin sees the host running `cloudflared` as the source of incoming traffic.

## 1\. Create a DNS record with private network routing

Create an `A` or `AAAA` record that points to the private IP address of your origin, with proxy status enabled and **Use private network routing** turned on. This tells Cloudflare to send traffic for the hostname through your tunnel instead of over the public Internet.

For the dashboard and API steps, refer to [Private network routing](https://developers.cloudflare.com/dns/private-origins/private-network-routing/).

## 2\. Verify end-to-end connectivity

After the DNS record is in place, validate the path from the Cloudflare network through your tunnel to the origin.

### Check tunnel health

In the Cloudflare dashboard, confirm that the tunnel carrying the route to your origin shows as healthy. If the tunnel is down, refer to [Tunnel troubleshooting](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/).

### Send a request from an external client

From a machine outside your private network, send an HTTPS request to the proxied hostname:
    
    
    curl -v https://<YOUR_DOMAIN>/

A successful response confirms that Cloudflare accepted the request, applied your proxied features, and reached the origin through the tunnel.

### Confirm traffic on the origin

On the origin VM, verify that requests are arriving from the host running `cloudflared`. To watch for incoming traffic from that host on port `443`, replace `<CLOUDFLARED_HOST_IP>` with its IP address:
    
    
    sudo tcpdump -n -i any 'src host <CLOUDFLARED_HOST_IP> and dst port 443'

Adjust the port to match the listener on your origin.

## Common pitfalls

Symptom | Cause and fix  
---|---  
Traffic never reaches the tunnel | The route to the origin is in a non-default virtual network. Move it to the default virtual network.  
Origin rejects connections | The origin firewall does not allow the host running `cloudflared`. Allow it.  
Traffic tries to route over the public Internet | The **Use private network routing** toggle is not turned on for the DNS record. Edit the record and turn the toggle on.  
  
## Next steps

  * Review the [Private network routing](https://developers.cloudflare.com/dns/private-origins/private-network-routing/) reference for dashboard and API details.
  * If traffic is not reaching your origin, refer to [Troubleshooting](https://developers.cloudflare.com/dns/private-origins/troubleshooting/).



[PreviousSet up a private origin via Cloudflare WAN](https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/)[NextSet up a private origin via Cloudflare Mesh](https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-mesh/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/private-origins/set-up-via-cloudflare-tunnel.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
