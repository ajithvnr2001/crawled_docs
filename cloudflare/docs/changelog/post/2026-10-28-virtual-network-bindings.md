---
url: https://developers.cloudflare.com/changelog/post/2026-10-28-virtual-network-bindings/
title: Select a virtual network for VPC Network bindings \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:18.998221+00:00
---

# Select a virtual network for VPC Network bindings · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-28-virtual-network-bindings/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2026

## Select a virtual network for VPC Network bindings

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

VPC Network bindings can select a specific virtual network by setting `network_id` to `cf1:vnet:<UUID>`, where the UUID is the ID of the virtual network. Continue to use `cf1:network` to select your account's default virtual network.

Multiple bindings can select different virtual networks. This lets one Worker reach separate backends that use the same private IP address:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "vpc_networks": [
        {
          "binding": "PRODUCTION",
          "network_id": "cf1:vnet:<PRODUCTION_VNET_UUID>",
          "remote": true
        },
        {
          "binding": "STAGING",
          "network_id": "cf1:vnet:<STAGING_VNET_UUID>",
          "remote": true
        }
      ]
    }
    
    
    [[vpc_networks]]
    binding = "PRODUCTION"
    network_id = "cf1:vnet:<PRODUCTION_VNET_UUID>"
    remote = true
    
    [[vpc_networks]]
    binding = "STAGING"
    network_id = "cf1:vnet:<STAGING_VNET_UUID>"
    remote = true

For details, refer to [VPC Networks configuration](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/).
