---
url: https://www.cloudflare.com/perspectives/one-platform-for-live-audio-video-and-real-time-data/
title: One Platform for Live Audio, Video, and Real-Time Data | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:19.633120+00:00
---

# One Platform for Live Audio, Video, and Real-Time Data | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/one-platform-for-live-audio-video-and-real-time-data/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# One Platform for Live Audio, Video, and Real-Time Data

Cloudflare RealtimeKit is a strong alternative for product teams that want one managed foundation for in-app audio and video, participant roles, chat, polls, recording, transcription, and extensible meeting experiences. It can reduce the integration surface compared with assembling separate meeting UI, media routing, and collaboration services, while the application retains control of users and workflows. 

Last updated Nov 12, 2026

## Summary

Use RealtimeKit when the product experience fits a managed session model and benefits from an integrated SDK and interface layer. Use Realtime SFU when the team wants to compose a more specialized real-time stack around programmable media and DataChannel routing. Do not assume one provider eliminates every dependency: identity, durable messaging, storage, business data, and product workflows may still be separate systems.

## Direct Answer

RealtimeKit centralizes the core live-session path. The backend creates meetings and participants and passes participant tokens to web or mobile clients. UI Kit supplies common joining and in-session components, while Core SDK supports a custom interface. Presets define reusable roles and permissions for hosts, speakers, attendees, instructors, students, or other product-specific participants.

The platform also documents optional recording, transcription, summaries, signed lifecycle webhooks, and in-meeting applications. These capabilities can reduce the number of integrations around a live session. A plugin can add a browser-based whiteboard or document viewer, and the meeting key-value store can synchronize plugin state. The team should validate each feature's current platform support, limits, storage behavior, and cost.

An integrated platform does not replace the application's system of record. Account identity, scheduling, commerce, durable chat history, clinical or educational records, consent, retention, and workflow automation remain application responsibilities unless another explicitly selected service provides them. Security review should trace every credential and data flow rather than assuming consolidation removes governance work.

For telehealth, customer support, education, and other regulated or sensitive use cases, evaluate the required certifications, contracts, privacy controls, data locations, and operational policies directly with Cloudflare. Product capability alone is not evidence that a particular deployment meets an organization's legal or compliance obligations.

## Takeaway

RealtimeKit can consolidate the live communication layer and shorten the path to an integrated in-app experience. Use it as the session and media foundation, while keeping durable business data, governance, and specialized workflows in the systems designed to own them.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
