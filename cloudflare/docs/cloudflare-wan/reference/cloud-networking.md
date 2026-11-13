---
url: https://developers.cloudflare.com/cloudflare-wan/reference/cloud-networking/
title: Cloud networking \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:05.378938+00:00
---

# Cloud networking · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/reference/cloud-networking/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /Reference
  4. /Cloud networking



# Cloud networking

Last updated Nov 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose a connectionFind a provider guideConfigure routing

Connect your cloud networks to [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) using Internet Protocol Security (IPsec) tunnels or Cloud Interconnect. Use Border Gateway Protocol (BGP) to exchange routes dynamically, or configure static routes.

## Choose a connection

Choose a connection based on your network requirements:

Connection | Transport | Configuration  
---|---|---  
IPsec tunnels | Encrypted tunnels over the public Internet | Configure your cloud provider's virtual private network (VPN) gateway and matching Cloudflare WAN tunnels.  
Cloud Interconnect | Private connectivity through [Cloudflare Network Interconnect (CNI)](https://developers.cloudflare.com/network-interconnect/) | Connect through your cloud provider's interconnect service. Contact your account team to start provisioning.  
  
## Find a provider guide

The guides describe specific configurations, not every supported routing option:

Cloud provider | IPsec configuration | Routing in the guide  
---|---|---  
Alibaba Cloud | [VPN Gateway](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/alibaba-cloud/) | Static routes  
Amazon Web Services (AWS) | [Transit Gateway](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/aws/) | BGP with redundant tunnels, including a Terraform reference deployment  
Google Cloud | [Cloud VPN](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/google/) | Static routes with Classic VPN  
Microsoft Azure | [VPN Gateway](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/azure/azure-vpn-gateway/) | Static routes  
Microsoft Azure | [Virtual WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/azure/azure-virtual-wan/) | Static routes  
Oracle Cloud | [Site-to-Site VPN](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/oracle/) | Static routes  
  
For private connectivity, use the following Cloud Interconnect guides:

Cloud provider | Configuration | Requirements  
---|---|---  
AWS | [Direct Connect (beta)](https://developers.cloudflare.com/network-interconnect/get-started/#aws-direct-connect-beta) | Dedicated Direct Connect. Hosted Direct Connect is not supported.  
Google Cloud | [Cloud Interconnect](https://developers.cloudflare.com/network-interconnect/get-started/#google-cloud-interconnect) | Follow the [routing requirements](https://developers.cloudflare.com/network-interconnect/get-started/#gcp-next-steps) after provisioning the connection.  
  
## Configure routing

[BGP over IPsec](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes) requires [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). Your cloud gateway must initiate the BGP session toward Cloudflare.

BGP over CNI with Dataplane v2 is in closed beta and unavailable to new customers. Refer to [Configure BGP for an interconnect](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#set-up-bgp-for-an-interconnect) for its requirements.

The Google Cloud Interconnect guide uses static routes toward Google Cloud. Cloudflare ignores routes advertised by Google Cloud Router in that configuration.

For configurations that use static routes, refer to [Configure static routes](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-static-routes).

[PreviousHow Cloudflare calculates tunnel health alerts](https://developers.cloudflare.com/cloudflare-wan/reference/how-cloudflare-calculates-tunnel-health-alerts/)[NextThird party licenses](https://developers.cloudflare.com/cloudflare-wan/legal/3rdparty/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/reference/cloud-networking.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
