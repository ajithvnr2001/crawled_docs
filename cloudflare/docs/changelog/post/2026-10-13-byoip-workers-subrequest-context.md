---
url: https://developers.cloudflare.com/changelog/post/2026-10-13-byoip-workers-subrequest-context/
title: Workers subrequests now preserve context for BYOIP destinations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:57:11.158485+00:00
---

# Workers subrequests now preserve context for BYOIP destinations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-13-byoip-workers-subrequest-context/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 13, 2026

## Workers subrequests now preserve context for BYOIP destinations

[Workers](https://developers.cloudflare.com/workers/)[BYOIP](https://developers.cloudflare.com/byoip/)[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now preserves Workers context when a subrequest targets a Cloudflare-proxied hostname using [Bring Your Own IP (BYOIP)](https://developers.cloudflare.com/byoip/). These requests are identified as Cloudflare-to-Cloudflare traffic instead of external Internet traffic.

Previously, some BYOIP subrequests could lose Workers context and original client signals. This could cause security rules to behave unexpectedly, Bot Management to evaluate an internal Cloudflare connection instead of the original client, or affected requests to return false `403` responses.

Workers subrequests to BYOIP destinations now preserve the [`CF-Worker`](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-worker) header and [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field. This supports consistent security rule evaluation across same-zone and cross-zone subrequests.

[Bot Management fields](https://developers.cloudflare.com/bots/reference/bot-management-variables/#o2o-and-subrequests) on the destination zone now represent the original end-user connection for affected BYOIP subrequests. Bot scores, verified bot status, and JA3/JA4 fingerprints no longer represent the internal connection between Cloudflare services.

Customers benefit from consistent security rule evaluation, accurate Bot Management results, and fewer unexpected failures when Workers access BYOIP-backed hostnames. The improvement is automatic and requires no configuration changes.

For more information, refer to [Cloudflare BYOIP](https://developers.cloudflare.com/byoip/) and [Workers subrequests](https://developers.cloudflare.com/workers/platform/limits/#subrequests).
