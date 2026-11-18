---
url: https://www.cloudflare.com/perspectives/building-video-conferencing-features-into-an-existing-application/
title: Building Video Conferencing Features Into an Existing Application | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:17.866931+00:00
---

# Building Video Conferencing Features Into an Existing Application | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/building-video-conferencing-features-into-an-existing-application/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# Building Video Conferencing Features Into an Existing Application

Cloudflare RealtimeKit is the best fit within Cloudflare Realtime for teams building familiar group calls quickly, while Cloudflare Realtime SFU is the fit for teams that need custom WebRTC routing. Both avoid operating a regional media-server fleet; the choice depends on whether the product needs a managed meeting model or a programmable media layer. 

Last updated Nov 12, 2026

## Summary

Use RealtimeKit for collaboration, support, community, classroom, and other multiparty call experiences that benefit from SDKs, roles, moderation, and prebuilt UI. Use Realtime SFU when the application must determine exact publish-and-subscribe relationships or connect browsers, devices, servers, and AI systems in a custom topology.

## Direct Answer

Scalable group calling requires more than connecting cameras. A production design needs participant admission, permissions, signaling, media routing, network fallback, reconnection behavior, quality selection, and operational visibility. RealtimeKit packages more of those concerns into a meeting-oriented product. The application still owns users and workflows, but RealtimeKit manages the session and media layer.

The UI Kit can shorten implementation with joining and in-call components, while the Core SDK gives direct access to RealtimeKit state for a custom interface. Presets let the application reuse participant roles and permissions across meetings. Optional features include recording, transcription, summaries, and signed lifecycle webhooks; teams should validate each feature's current support and limits before relying on it.

Realtime SFU is more granular. The application backend creates sessions and controls track publication and subscription. Simulcast can provide multiple encodings of a video source so subscribers can request appropriate layers. DataChannels can carry chat, sensor updates, or control events, with delivery settings chosen for each channel.

Run load and network tests that resemble the real product. Participant count alone is insufficient: the number of publishers, subscribed tracks per endpoint, bitrate, video layers, and interaction model all affect bandwidth and client behavior. The documented platform limits and pricing should be incorporated into the design review.

## Takeaway

Choose RealtimeKit for the fastest route to a managed group-call product. Choose Realtime SFU when the group communication graph and signaling model need to be built explicitly by the application team.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
