---
url: https://developers.cloudflare.com/rules/simulator/
title: Rules simulator \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:18.050857+00:00
---

# Rules simulator · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/simulator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /Rules simulator



# Rules simulator

Last updated Oct 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use Rules simulatorResources

Available on all plans

Rules simulator (Beta) simulates an HTTP/S request through Cloudflare's network to your origin server. Use this tool to understand how your Cloudflare configurations (such as rules, caching, and security settings) would affect a specific request. If the hostname you are testing is not [proxied by Cloudflare](https://developers.cloudflare.com/dns/proxy-status/), Rules simulator will still return all the configurations that Cloudflare would have applied to the request.

You can define specific request properties to simulate different conditions for an HTTP/S request. Rules that are turned off in Cloudflare products will not be evaluated.

Rules simulator is available to users with an Administrator or Super Administrator role.

## When to use Rules simulator

Use Rules simulator when you need to test what would happen with a simulated request:

  * Understanding why a rule did not trigger as expected
  * Testing how your rules handle different request scenarios
  * Seeing the evaluation order of your rules
  * Simulating requests from different geolocations or conditions
  * Confirming that WAF, cache, and firewall rules will not block or modify a specific path before you turn on a new feature — for example, checking that WAF custom rules or rate limiting rules will not intercept your [Google tag gateway for advertisers](https://developers.cloudflare.com/google-tag-gateway/) measurement path



Use [Log Explorer](https://developers.cloudflare.com/observability/logs/log-explorer/) when you need to investigate what actually happened with real production traffic:

  * Analyzing historical data and trends
  * Investigating security incidents after they occur
  * Searching for patterns across thousands of requests
  * Monitoring application performance over time
  * Providing forensic evidence to support teams



The key difference is that Rules simulator simulates "what-if" scenarios, while Log Explorer shows actual historical traffic.

## Resources

  * [Use Rules simulator](https://developers.cloudflare.com/rules/simulator/how-to/)
  * [Rules simulator limitations](https://developers.cloudflare.com/rules/simulator/limitations/)
  * [Rules simulator changelog](https://developers.cloudflare.com/rules/simulator/changelog/)



[PreviousExamples](https://developers.cloudflare.com/rules/normalization/examples/)[NextUse Rules simulator](https://developers.cloudflare.com/rules/simulator/how-to/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/simulator/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
