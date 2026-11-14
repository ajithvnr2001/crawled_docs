---
url: https://developers.cloudflare.com/changelog/post/2026-11-13-spend-management/
title: Set spending limits for Workers and Durable Objects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:52.212317+00:00
---

# Set spending limits for Workers and Durable Objects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-13-spend-management/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 13, 2026

## Set spending limits for Workers and Durable Objects

[Billing](https://developers.cloudflare.com/billing/)[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set spending limits for Workers and Durable Objects to help control unexpected usage costs, or receive email alerts while your applications keep running. Support for more products is coming soon.

Use these controls alongside [AI Gateway spend limits](https://developers.cloudflare.com/ai-gateway/features/spend-limits/) to manage compute and AI inference costs across your application. AI Gateway supports per-user and per-model budgets for Workers AI and other AI providers, applied to requests routed through your gateway.

Workers and Durable Objects limits apply across your account for the current subscription billing period. Each product has its own spending controls.

#### Set your limits and alerts

In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select your account and go to **Billing** > **Spend limits**. Choose a spending limit, notification email, and alert thresholds for Workers or Durable Objects.

For example, configure a $10 Workers spending limit with email alerts at $5 and $9. To receive alerts while your applications keep running, turn off **Block usage**.

![Workers controls with usage blocking at $10, a notification email, and alert thresholds at $5 and $9.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=600,height=653,format=webp/_astro/workers-spending-controls.BHHAwbV8.png)

#### See when a limit takes effect

The overview shows each product's recorded spend, alert thresholds, and pause status. Email alerts notify you without stopping usage. When a spending limit takes effect, Cloudflare blocks the product's supported operations.

![Spend limits overview with Workers marked Services paused and separate spend and threshold indicators for Durable Objects.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2006,height=249,format=webp/_astro/spend-management-overview.qnHUshUO.png)

To resume usage, raise the limit above current spend, turn it off, or remove it. Usage also resumes when the next billing period starts.

Usage reporting and blocking take time, so recorded spend can exceed a limit. Read about [what counts toward a limit](https://developers.cloudflare.com/billing/manage/spend-management/#what-counts-toward-a-limit).

#### Choose alerts, limits, or both

For example, set a $50 spending limit for Workers and a $20 email alert for Durable Objects:
    
    
    flowchart LR
        A["Durable Objects reaches $20"] --> B["Email alert sent"]
        B --> C["Usage continues"]
        D["Workers reaches $50"] --> E["Spending limit takes effect"]
        E --> F["New Worker invocations blocked"]
    

#### Set a spending limit with the cf CLI

[Install the cf CLI and select your account](https://developers.cloudflare.com/cf/get-started/), then run this command to set a $50 spending limit for Workers usage in the current billing period:
    
    
    cf billing spend-policies create \
      --name 'Workers $50 spending limit' \
      --product-id workers \
      --enabled true \
      --threshold-cents 5000 \
      --action usage_block

The amount is in US cents: `5000` means $50. To set a spending limit for Durable Objects, use `--product-id durable_objects` and update the name. Limits count usage already recorded in the current billing period.

You can also give this prompt to your coding agent. It will ask which product you want to manage and what spending limit to set, then use the CLI to configure it.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

#### Use spending limits alongside budget alerts

The [budget alerts introduced earlier this year](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) notify you about account-wide usage costs without stopping usage. You can keep using them alongside the new product-specific spending limits and email alerts for Workers and Durable Objects.

To configure account-wide alerts, go to **Billing** > **Billable Usage** or follow the [budget alerts guide](https://developers.cloudflare.com/billing/manage/budget-alerts/).

Read the [spending limits and alerts guide](https://developers.cloudflare.com/billing/manage/spend-management/) to learn how spending limits work and manage limits and alerts through the dashboard or cf CLI.
