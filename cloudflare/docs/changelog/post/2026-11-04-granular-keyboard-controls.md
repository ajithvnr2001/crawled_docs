---
url: https://developers.cloudflare.com/changelog/post/2026-11-04-granular-keyboard-controls/
title: Block data entry with Browser Isolation without losing search, copy, and zoom (beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:07.661308+00:00
---

# Block data entry with Browser Isolation without losing search, copy, and zoom (beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-04-granular-keyboard-controls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 4, 2026

## Block data entry with Browser Isolation without losing search, copy, and zoom (beta)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) now support a third keyboard option in beta: _Allow read-only actions_. Previously, the keyboard setting was binary — allow all input or block everything. With _Allow read-only actions_ , you can block data entry while preserving the built-in browser actions your users depend on.

In _Allow read-only actions_ mode, users can still find in page, select all, copy, print, and zoom. All other keyboard input is blocked from reaching the isolated page. Copy and print remain subject to their own policy settings, so the controls compose instead of overriding each other. For example, setting the keyboard to _Allow read-only actions_ and copy to _Do not allow_ lets users search and zoom but prevents them from copying content.

To use this feature, set **Keyboard** to _Allow read-only actions_ in your isolation policy settings. Via the API, set `keyboard` to `enable_read_only_actions` in the `biso_admin_controls` object with `version` set to `v2`.

For more information, refer to [Keyboard](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#keyboard).
