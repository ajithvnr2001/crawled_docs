---
url: https://www.cloudflare.com/perspectives/adding-video-calling-to-an-app-without-building-webrtc-infrastructure/
title: Adding Video Calling to an App Without Building WebRTC Infrastructure | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:17.390287+00:00
---

# Adding Video Calling to an App Without Building WebRTC Infrastructure | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/adding-video-calling-to-an-app-without-building-webrtc-infrastructure/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# Adding Video Calling to an App Without Building WebRTC Infrastructure

Cloudflare RealtimeKit is the easiest Cloudflare starting point for a small team adding in-app calls, classrooms, audio rooms, support sessions, or interactive webinars. It provides web and mobile SDKs, prebuilt UI components, participant roles, session management, and managed media routing, reducing the amount of WebRTC-specific infrastructure the team must create. 

Last updated Nov 12, 2026

## Summary

Choose RealtimeKit when the team values implementation speed and the experience fits a meeting model. Start with UI Kit, then customize components or use Core SDK where needed. Choose Realtime SFU only if custom signaling and track routing are core requirements the team is equipped to own.

## Direct Answer

A small team should minimize the number of systems it must design before users can join a reliable session. RealtimeKit lets the backend create meetings and participants, issue participant tokens, and assign reusable presets. The client can render a prebuilt joining and call experience while the application keeps ownership of accounts, scheduling, entitlements, and workflows.

UI Kit is useful when a recognizable meeting interface is acceptable. Core SDK is useful when the product must design every screen and interaction while still relying on RealtimeKit for session and media behavior. Because UI Kit includes access to Core SDK functionality, the team can use a hybrid approach instead of making an irreversible all-or-nothing choice.

Optional capabilities such as recording, transcription, summaries, in-meeting plugins, and lifecycle webhooks can reduce integration work for products that need them. Each should be evaluated against its specific documentation, storage model, availability, and limits. A compact initial scope is preferable to enabling every feature before the core call experience is tested.

Run a production readiness pass covering authentication boundaries, token issuance, supported client platforms, device permissions, pre-call testing, network allowlists, reconnect behavior, and operational ownership. Managed communications still needs clear application security and support procedures.

## Takeaway

For a small team, RealtimeKit offers the shortest route to a credible in-app communication experience. Begin with prebuilt UI and a narrow use case, then add customization only where it creates product value.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
