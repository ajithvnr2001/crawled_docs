---
url: https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-mesh/
title: Set up a private origin via Cloudflare Mesh \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:44.382430+00:00
---

# Set up a private origin via Cloudflare Mesh · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-mesh/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Private origins](https://developers.cloudflare.com/dns/private-origins/)
  4. /Set up a private origin via Cloudflare Mesh



# Set up a private origin via Cloudflare Mesh

Last updated Nov 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin1\. Create a DNS record with private network routing2\. Verify end-to-end connectivity Check node health Send a request from an external client Confirm traffic on the originCommon pitfallsNext steps

This guide walks you through proxying public hostnames to origins on a private network. The private network is reachable through [Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/). The CDN, WAF, Cache, and other proxied features apply to this traffic the same way they apply to traffic destined for public origins.

## Before you begin

Confirm the following before you start:

  * **Private Origins available on your account** : contact your account team to enable it.
  * **Unified Routing enabled** : your account must be on [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) to use a private Cloudflare source range. Contact your account team to enable it. This applies to new and existing accounts.
  * **A Mesh node in the origin's network** : run a Mesh node on a host that can reach the origin, with a route covering the origin IP in your **default virtual network**. A single Mesh node can serve multiple origins. Refer to [Mesh routes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/) and [Get started with Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/get-started/).
  * **Return routes for the Cloudflare source IP ranges** : in the origin's network, add routes that send `100.64.0.0/12` (or your configured private `/12`) and `2606:4700:cf1:5000::/64` back to the Mesh node, and allow both ranges in the origin's firewall.



## 1\. Create a DNS record with private network routing

Create an `A` or `AAAA` record that points to the private IP address of your origin, with proxy status enabled and **Use private network routing** turned on. This tells Cloudflare to send traffic for the hostname through your Mesh network instead of over the public Internet.

For the dashboard and API steps, refer to [Private network routing](https://developers.cloudflare.com/dns/private-origins/private-network-routing/).

## 2\. Verify end-to-end connectivity

After the DNS record is in place, validate the path from the Cloudflare network through your Mesh network to the origin.

### Check node health

In the Cloudflare dashboard, confirm that the Mesh node in the origin's network is connected and healthy.

### Send a request from an external client

From a machine outside your private network, send an HTTPS request to the proxied hostname:
    
    
    curl -v https://<YOUR_DOMAIN>/

A successful response confirms that Cloudflare accepted the request, applied your proxied features, and reached the origin through the Mesh network.

### Confirm traffic on the origin

On the origin VM, verify that requests are arriving from the Cloudflare source IP ranges. To watch for incoming traffic on port `443`:
    
    
    sudo tcpdump -n -i any 'src net 100.64.0.0/12 and dst port 443'

For IPv6:
    
    
    sudo tcpdump -n -i any 'src net 2606:4700:cf1:5000::/64 and dst port 443'

Replace `100.64.0.0/12` with the source range configured for your account, and adjust the port to match the listener on your origin.

## Common pitfalls

Symptom | Cause and fix  
---|---  
Requests time out, nothing comes back | No return route for the Cloudflare source IP ranges. Add routes that send them back to the Mesh node.  
Traffic never reaches the Mesh node | The route to the origin is in a non-default virtual network. Move it to the default virtual network.  
Traffic tries to route over the public Internet | The **Use private network routing** toggle is not turned on for the DNS record. Edit the record and turn the toggle on.  
  
## Next steps

  * Review the [Private network routing](https://developers.cloudflare.com/dns/private-origins/private-network-routing/) reference for dashboard and API details.
  * If traffic is not reaching your origin, refer to [Troubleshooting](https://developers.cloudflare.com/dns/private-origins/troubleshooting/).



[PreviousSet up a private origin via Cloudflare Tunnel](https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-tunnel/)[NextPrivate network routing](https://developers.cloudflare.com/dns/private-origins/private-network-routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/private-origins/set-up-via-cloudflare-mesh.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
