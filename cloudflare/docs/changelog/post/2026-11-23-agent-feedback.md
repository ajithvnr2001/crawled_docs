---
url: https://developers.cloudflare.com/changelog/post/2026-11-23-agent-feedback/
title: Send feedback from the Cloudflare CLI and MCP \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:00.094519+00:00
---

# Send feedback from the Cloudflare CLI and MCP · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-23-agent-feedback/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 23, 2026

## Send feedback from the Cloudflare CLI and MCP

[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Send bug reports, feature requests, and feedback about where you got stuck directly to Cloudflare.

Sign in with `cf auth login` or set `CLOUDFLARE_API_TOKEN`, then use `cf feedback` with a short note.
    
    
    cf feedback "The deploy output did not identify the selected environment"

Coding agents connected to the Cloudflare API Model Context Protocol (MCP) server can use the `submit_feedback` tool. The tool requires a `message`, `type`, and `impact`. It accepts optional details such as the task and the expected and actual results. Both options return a submission ID you can share.

For examples and the diagnostic details included in CLI reports, refer to [Agent feedback](https://developers.cloudflare.com/cf/agent-feedback/).
