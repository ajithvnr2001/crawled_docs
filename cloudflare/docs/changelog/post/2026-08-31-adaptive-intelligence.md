---
url: https://developers.cloudflare.com/changelog/post/2026-08-31-adaptive-intelligence/
title: Bot Management's machine learning model now retrains more frequently instead of shipping fixed versions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:34.793318+00:00
---

# Bot Management's machine learning model now retrains more frequently instead of shipping fixed versions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-31-adaptive-intelligence/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 31, 2026

## Bot Management's machine learning model now retrains more frequently instead of shipping fixed versions

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We have launched Adaptive Intelligence, a new bot detection engine built to close the gap between when an attack pattern first appears and when protection against it reaches every customer. You can [read the announcement blog ↗︎](https://blog.cloudflare.com/introducing-adaptive-intelligence/) for the full story behind why we built it.

Adaptive Intelligence, the machine learning model behind your bot score, now retrains more frequently instead of shipping as a fixed, numbered version. As new bypass tools and bot frameworks appear, the model learns from them and folds that knowledge in without waiting for a scheduled release.

Every update is validated before it affects you. New model versions run in shadow mode first, scored but not acted on, and are compared against the current model before rolling out gradually.

Enterprise customers with **Auto-update machine learning** switched on under Bot Management configurations get Adaptive Intelligence automatically, with no version to migrate and nothing else to configure.

To learn more, refer to [Adaptive Intelligence](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/#adaptive-intelligence-business-and-enterprise) and [Machine Learning models](https://developers.cloudflare.com/bots/reference/machine-learning-models/).
