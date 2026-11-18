---
url: https://www.cloudflare.com/perspectives/choosing-a-real-time-sdk-for-fast-application-development/
title: Choosing a Real-Time SDK for Fast Application Development | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:18.292036+00:00
---

# Choosing a Real-Time SDK for Fast Application Development | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/choosing-a-real-time-sdk-for-fast-application-development/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# Choosing a Real-Time SDK for Fast Application Development

Use RealtimeKit UI Kit when the team wants to launch with prebuilt joining and in-call components. Use RealtimeKit Core SDK when the product needs to control every screen, interaction, and visual state. Teams can also combine them because UI Kit includes the Core SDK APIs. 

Last updated Nov 12, 2026

## Summary

UI Kit prioritizes implementation speed and a complete default experience. Core SDK prioritizes design freedom while preserving RealtimeKit's managed sessions and media routing. A hybrid approach is often practical: use proven prebuilt controls for commodity call behavior and custom components for differentiated workflows.

## Direct Answer

The [RealtimeKit SDK selection guide](https://developers.cloudflare.com/realtime/realtimekit/humans/sdk-selection/) explains the UI Kit and Core SDK options. UI Kit includes the setup screen, participant grid, media controls, chat, and polls. A team can use the default layout, customize branding, and replace or configure individual components. This is a good fit for a minimum viable product, an internal tool, or a product whose communication interface follows familiar meeting conventions.

Core SDK exposes session, participant, and media state so the application can build its own interface. It is the better choice for specialized layouts, workflow-specific controls, device experiences, or products where the communication interaction is a central part of the brand. The tradeoff is more frontend state management, accessibility work, testing, and design responsibility.

The choice does not change the backend trust boundary. The application backend should use its Cloudflare API credentials to create RealtimeKit resources and pass participant authentication tokens to clients. Cloudflare API tokens should never be embedded in the frontend.

A useful rollout begins with UI Kit to validate meeting creation, participant admission, device permissions, and media behavior. The team can then replace components that need differentiation, using Core SDK where the prebuilt interface no longer fits. This reduces early implementation risk without locking the product into an unchangeable layout.

## Takeaway

Start with UI Kit unless the product has a clear reason to own every interaction. Use Core SDK for differentiated experiences, and combine both when only part of the interface requires custom behavior.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
