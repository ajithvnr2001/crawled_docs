---
url: https://developers.cloudflare.com/changelog/post/2026-08-19-event-spec-compliance/
title: Event and EventTarget spec compliance improvements \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:47.877185+00:00
---

# Event and EventTarget spec compliance improvements · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-19-event-spec-compliance/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2026

## Event and EventTarget spec compliance improvements

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-event-spec-compliance/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Several improvements bring the Workers runtime's `Event`, `EventTarget`, and related APIs closer to their web platform specifications.

#### `isTrusted` is now correct for user-constructed events

User-constructed event subclasses (`new MessageEvent(...)`, `new CustomEvent(...)`, `new ErrorEvent(...)`, `new CloseEvent(...)`) now correctly report `isTrusted` as `false`. Previously, these incorrectly reported `isTrusted` as `true`.

#### `on<type>` handlers fire in registration order

Event handler attributes such as `onmessage` and `onabort` now fire in their registration order relative to `addEventListener()` calls, matching browser behavior. Previously, `on<type>` handlers always fired before any `addEventListener()` listeners regardless of when they were assigned.

#### `MessageEvent` constructor improvements

`new MessageEvent(type)` now works without providing an init object — `data` defaults to `null` per spec. The `MessageEventInit` dictionary also now supports the full spec surface: `origin`, `lastEventId`, `source`, and `ports`, in addition to `data`.

#### `CloseEvent` and `ErrorEvent` constructor improvements

The `CloseEventInit` and `ErrorEventInit` dictionaries now accept the standard `EventInit` members `bubbles`, `cancelable`, and `composed`.

#### `MessagePort` starts on any `message` listener

Adding a `message` event listener to a `MessagePort` via `addEventListener("message", ...)` now starts the port, matching browser behavior. Previously, only assigning `onmessage` would start the port.
