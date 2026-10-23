---
url: https://developers.cloudflare.com/realtime/realtimekit/platform/network-allowlist/
title: Network allowlist \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:40:06.409127+00:00
---

# Network allowlist · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/platform/network-allowlist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Platform](https://developers.cloudflare.com/realtime/realtimekit/platform/)
  5. /Allowlist



# Network allowlist

Last updated Oct 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/platform/network-allowlist/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAllow service domainsAllow media trafficUse a wildcard domainVerify connectivity

If your network restricts outbound traffic, allow the following RealtimeKit domains and ports.

## Allow service domains

Allow these domains for RealtimeKit SDKs:

Domain | Purpose  
---|---  
`api.realtime.cloudflare.com` | Handles requests from RealtimeKit SDKs  
`api-silos.realtime.cloudflare.com` | Collects SDK logs  
`da-collector.realtime.cloudflare.com` | Collects call statistics  
`location.realtime.cloudflare.com` | Determines the location in call statistics reports  
`r2.cloudflarestorage.com` | Stores and retrieves chat messages  
`socket-edge.realtime.cloudflare.com` | Establishes signaling connections between clients and RealtimeKit  
  
If your application uses RealtimeKit Web UI Kit, also allow these domains:

Domain | Purpose  
---|---  
`rtk-assets.realtime.cloudflare.com` | Serves Web UI Kit assets, including speaker-test audio  
`rtk-uploads.realtime.cloudflare.com` | Serves notification sounds and other Web UI Kit assets  
  
Applications that use only RealtimeKit Core do not require the Web UI Kit asset domains.

If your application uses the [Whiteboard plugin](https://developers.cloudflare.com/realtime/realtimekit/custom-plugins/whiteboard/), also allow `whiteboard-v2.plugins.realtime.cloudflare.com`, which serves the whiteboard and syncs its boards.

## Allow media traffic

RealtimeKit uses the [Cloudflare Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) for media connections. Allow the following Session Traversal Utilities for NAT (STUN) and Traversal Using Relays around NAT (TURN) traffic:

Protocol | Domain | Primary port | Alternate port  
---|---|---|---  
STUN over UDP | `stun.cloudflare.com` | `3478/udp` | `53/udp`  
TURN over UDP | `turn.cloudflare.com` | `3478/udp` | `53/udp`  
TURN over TCP | `turn.cloudflare.com` | `3478/tcp` | `80/tcp`  
TURN over TLS | `turn.cloudflare.com` | `5349/tcp` | `443/tcp`  
  
Allow the primary and alternate ports where possible. Do not rely only on `53/udp`, because Internet service providers and browsers can block this port.

For protocol details, refer to [Service address and ports](https://developers.cloudflare.com/realtime/turn/#service-address-and-ports).

## Use a wildcard domain

If your network policy supports wildcard domains, you can use `*.realtime.cloudflare.com` instead of the listed `realtime.cloudflare.com` domains.

Individual domain rules are recommended because they restrict access to only the required services. If you use the wildcard domain, you must still allow `r2.cloudflarestorage.com`, `stun.cloudflare.com`, and `turn.cloudflare.com` separately, because the wildcard does not cover them.

## Verify connectivity

Run the [RealtimeKit pre-call test ↗︎](https://test.realtime.cloudflare.com/) to verify your device can reach the required services.

[PreviousData retention](https://developers.cloudflare.com/realtime/realtimekit/platform/data-retention/)[NextLegal](https://developers.cloudflare.com/realtime/realtimekit/platform/legal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/platform/network-allowlist.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
