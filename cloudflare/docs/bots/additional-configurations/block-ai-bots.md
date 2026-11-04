---
url: https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/
title: AI Crawler and Agent access policies \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:24.171040+00:00
---

# AI Crawler and Agent access policies · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Additional configurations
  4. /AI Crawler and Agent access policies



# AI Crawler and Agent access policies

Last updated Nov 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAI Crawler and Agent access policies Behaviors Policy actions Configure policies for existing domains Default policies for new domains Personal Agent policies

Note

This feature was previously called **Configure AI bot policies**.

## AI Crawler and Agent access policies

AI Crawler and Agent access policies let you control AI crawler and agent traffic by behavior. You can set actions for Search, Agent, and Training traffic, and customize access for the top Personal Agents.

### Behaviors

Cloudflare offers configuration for the most common AI behaviors:

  * **Search** : crawlers that collect or index your content to answer questions about it later.
  * **Agent** : automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents.
  * **Training** : crawlers taking your content to train or fine-tune a model, including mixed-purpose crawlers that are used both for Training and for Search.



Each policy applies to Verified bots with that behavior and matching unverified bots.

### Policy actions

Choose an action for each behavior. Available actions are:

Action | Effect  
---|---  
_Block_ | Block matching requests across the zone.  
_Block on pages with ads_ | Block matching requests on pages where Cloudflare detects ads.  
_Allow (do not block)_ | Do not block matching requests.  
_Disallow_ | For Training only, tell crawlers not to access your content through `robots.txt`.  
  
`robots.txt` directives are voluntary. Crawlers can ignore them. When Bot Preference Sync is enabled, **Disallow** also blocks AI training crawlers at Cloudflare's edge. Mixed-purpose crawlers used for both Search and Training are excluded from this edge block.

### Configure policies for existing domains

To configure these policies for an existing zone:

  1. In the Cloudflare dashboard, go to **Security** > **Settings**.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **Bot traffic** , then select **AI Crawler and Agent access policies**.

  3. Select an action for each behavior. For Agents, you can also granularly customize access for the top Personal Agents.

  4. Select **Save**.




### Default policies for new domains

For new domains, **Search** , **Agents** , and **Training** use **Allow (do not block)** by default. You can change these defaults after onboarding in **Security** > **Settings** > **AI Crawler and Agent access policies**.

Training actions also apply to mixed-purpose crawlers used for both Search and Training.

### Personal Agent policies

Personal Agents inherit the **Agents** policy by default. Changing the **Agents** policies updates each Personal Agent. You can then choose individual actions again. Cloudflare recommends **Allow (do not block)** for Personal Agents.

You can also configure Personal Agent policies during zone onboarding.

[PreviousAI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/)[NextCustom rules](https://developers.cloudflare.com/bots/additional-configurations/custom-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/additional-configurations/block-ai-bots.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
