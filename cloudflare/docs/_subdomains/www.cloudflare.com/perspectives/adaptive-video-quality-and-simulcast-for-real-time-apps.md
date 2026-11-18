---
url: https://www.cloudflare.com/perspectives/adaptive-video-quality-and-simulcast-for-real-time-apps/
title: Adaptive Video Quality and Simulcast for Real-Time Apps | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:17.435611+00:00
---

# Adaptive Video Quality and Simulcast for Real-Time Apps | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/adaptive-video-quality-and-simulcast-for-real-time-apps/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# Adaptive Video Quality and Simulcast for Real-Time Apps

Cloudflare Realtime SFU is a strong choice when an application needs explicit simulcast control. A publisher can send multiple encodings of a video source, and each subscriber can request a preferred encoding with a defined priority and fallback policy. This helps the application match delivered quality to layout and network conditions. 

Last updated Nov 12, 2026

## Summary

Use [Realtime SFU simulcast](https://developers.cloudflare.com/realtime/sfu/features/simulcast/) when subscriber-aware layer selection is part of the product. The application configures encodings, communicates available layer identifiers, and updates a subscription's preferred layer. Simulcast is a tool for adaptation, not a substitute for client monitoring, sensible bitrate choices, or product-level quality logic.

## Direct Answer

Simulcast lets one video source be encoded at multiple qualities. The publisher advertises the encodings using RTP Stream Identifiers, and the SFU can forward a selected layer to each subscriber. A large tile may request a higher-quality encoding while a thumbnail or constrained connection receives a lower-quality one.

With Realtime SFU, the application backend specifies the preferred layer when it creates or updates a remote track subscription. It can also define what happens when bandwidth is insufficient or the requested layer is unavailable. The documented defaults do not automatically select an alternative layer, so the team must configure fallback behavior intentionally.

The product still needs a quality policy. It should decide when to change layers based on layout, endpoint statistics, network observations, and user priorities. It should also handle publishers that stop sending an encoding and subscribers that reconnect. Testing should include rapid layout changes, constrained uplinks, packet loss, and heterogeneous device capabilities.

RealtimeKit is more appropriate when a team wants a managed meeting experience rather than direct control of SFU track requests. The service manages the meeting and media behavior at a higher abstraction level. Direct Realtime SFU integration is for teams that need the layer-selection mechanism as part of their own application logic.

## Takeaway

Use Realtime SFU simulcast for explicit, subscriber-specific video-layer selection. Treat adaptation as an application policy supported by the SFU, and test that policy under real network and layout changes.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
