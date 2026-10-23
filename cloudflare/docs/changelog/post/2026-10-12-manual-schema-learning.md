---
url: https://developers.cloudflare.com/changelog/post/2026-10-12-manual-schema-learning/
title: Run schema learning on demand \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:33.274037+00:00
---

# Run schema learning on demand · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-12-manual-schema-learning/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 12, 2026

## Run schema learning on demand

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manually request an API Shield schema learning run without waiting for the weekly schedule. Use this during testing after sending representative traffic to your API.

In **Web Assets** > **Operations** , open the **More options** menu for the operations table and select **Ad-hoc learn schema**. In the **Schema learning** dialog, select **Run learning**. The run covers the entire zone and uses observed traffic. Existing learning thresholds still apply.

The dialog shows the learning status and last completed run for the zone. The **Learned schema** view shows the learning result and last learning run for each operation. You can review individual results while the zone-wide run continues.

For instructions and traffic requirements, refer to [Run schema learning manually](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/#run-schema-learning-manually).
