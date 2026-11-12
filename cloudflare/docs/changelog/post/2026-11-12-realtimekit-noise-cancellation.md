---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-realtimekit-noise-cancellation/
title: Add noise cancellation to web apps built on RealtimeKit \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.793795+00:00
---

# Add noise cancellation to web apps built on RealtimeKit · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-realtimekit-noise-cancellation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Add noise cancellation to web apps built on RealtimeKit

[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now add [noise cancellation](https://developers.cloudflare.com/realtime/realtimekit/humans/core/noise-cancellation/) to [RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) web apps with the new `@cloudflare/realtimekit-noise-cancellation` package. RealtimeKit is a high-level SDK for adding real-time audio and video components, such as video meetings, to your web or mobile app.

Install the package:

npmyarnpnpmbun
    
    
    npm i @cloudflare/realtimekit-noise-cancellation
    
    
    yarn add @cloudflare/realtimekit-noise-cancellation
    
    
    pnpm add @cloudflare/realtimekit-noise-cancellation
    
    
    bun add @cloudflare/realtimekit-noise-cancellation

After you [initialize the meeting](https://developers.cloudflare.com/realtime/realtimekit/humans/core/), pass it to `init()`:
    
    
    import { RealtimeKitNoiseCancellation } from "@cloudflare/realtimekit-noise-cancellation";
    
    // Enables automatically when the mic is available, without delaying join.
    void RealtimeKitNoiseCancellation.init({ meeting }).catch(console.warn);

#### How it works

  * Filters background noise in the participant's browser, before their audio is sent to the meeting.
  * Turns on automatically after `init()`, as soon as the participant's microphone is on.
  * Keeps running through mute, unmute, and reconnects, and cleans up when the participant leaves.
  * Never unmutes the microphone.



Noise cancellation works in React, Angular, and JavaScript apps on Chrome, Edge, Firefox, and Safari, including mobile browsers. The RealtimeKit iOS and Android SDKs do not yet support it.

#### Learn more

  * [Noise Cancellation](https://developers.cloudflare.com/realtime/realtimekit/humans/core/noise-cancellation/): setup for React, Angular, and JavaScript, plus the full API
  * [Noise cancellation example ↗︎](https://github.com/cloudflare/realtimekit-web-examples/tree/main/react-examples/examples/with-noise-cancellation): RealtimeKit's default meeting UI with noise cancellation turned on, also available in Angular and HTML in the same repository
  * [RealtimeKit release notes](https://developers.cloudflare.com/realtime/realtimekit/release-notes/)
  * [RealtimeKit quickstart](https://developers.cloudflare.com/realtime/realtimekit/quickstart/)


