---
url: https://www.cloudflare.com/perspectives/sfu-vs-mcu-vs-peer-to-peer-for-real-time-video/
title: SFU vs. MCU vs. Peer-to-Peer for Real-Time Video | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:19.735292+00:00
---

# SFU vs. MCU vs. Peer-to-Peer for Real-Time Video | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/sfu-vs-mcu-vs-peer-to-peer-for-real-time-video/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# SFU vs. MCU vs. Peer-to-Peer for Real-Time Video

An SFU is generally the best starting point for multiparty WebRTC applications that need low latency and client-specific stream selection. Peer-to-peer works well for one-to-one communication and some very small groups, while an MCU can fit applications that specifically require a server-composed output. Cloudflare Realtime SFU provides managed selective forwarding without requiring the product team to operate the media-server fleet. 

Last updated Nov 12, 2026

## Summary

Choose peer-to-peer for simple one-to-one paths, an SFU for multiparty calls and subscriber-specific routing, and an MCU when centralized live mixing or composition is a core requirement. Recording a composed layout does not by itself require the live experience to use an MCU.

## Direct Answer

An SFU receives tracks from publishers and forwards chosen tracks to subscribers. This preserves the individual streams and lets the application decide which media each endpoint should receive. Cloudflare Realtime SFU exposes that control through sessions, publications, subscriptions, and track updates. Its simulcast support allows a publisher to send multiple encodings and a subscriber to select a preferred layer with a defined fallback policy.

Peer-to-peer avoids a media server in the direct path, which can be efficient for two endpoints. In a mesh group call, however, each participant sends media to every other participant, so connection count and uplink demand grow with the room. TURN can relay a blocked peer connection, but it does not turn a mesh into a scalable fanout architecture.

An MCU decodes incoming media, mixes or composites it, and encodes a new output. That can simplify some constrained clients or create a uniform composed feed, but it requires server-side media processing. The tradeoff can include additional compute, latency, and loss of per-track flexibility. The correct choice depends on whether composition is part of the live product requirement, not on a general assumption that one architecture is always superior.

For a meeting-style product that wants managed features, RealtimeKit may be the more relevant choice than directly selecting an SFU architecture. RealtimeKit can capture composite video or separate participant audio tracks for recording while providing a managed live experience. For a custom WebRTC system, Realtime SFU is the product that exposes track-level routing.

Teams should model endpoint capabilities, bandwidth, layouts, recording, downstream processing, and audience interaction. If most viewers are passive and a small presenter group broadcasts to a large audience, a CDN-oriented live streaming product such as Cloudflare Stream Live may fit better than either a multiparty SFU or MCU design.

## Takeaway

Start with an SFU for interactive, track-aware WebRTC applications. Introduce server-side composition only where a specific output or client constraint requires it, and evaluate Stream Live for large watch-only broadcasts.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
