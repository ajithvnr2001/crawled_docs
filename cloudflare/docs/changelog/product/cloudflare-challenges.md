---
url: https://developers.cloudflare.com/changelog/product/cloudflare-challenges/
title: Bots Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.529409+00:00
---

# Bots Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/cloudflare-challenges/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Challenges

China Network

Cloud Workload Security

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Notifications

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 28, 2026

## [China-native Challenge Pages for the China Network](https://developers.cloudflare.com/changelog/post/2026-10-28-china-native-challenge-pages/)

[China Network](https://developers.cloudflare.com/china-network/)[Challenges](https://developers.cloudflare.com/cloudflare-challenges/)[Bots](https://developers.cloudflare.com/bots/)

Challenge Pages served through the Cloudflare China Network now use Turnstile widgets hosted in Mainland China. This means that visitors in Mainland China can complete challenges faster and more reliably because widgets no longer need to make cross-border requests.

**You do not need to take any action: this change applies automatically when a China Network zone presents a Challenge Page.** Visitors served by Cloudflare's global network will continue to receive the global Challenge Page experience.

For more information, refer to [Interstitial Challenge Pages](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/) and [Cloudflare China Network](https://developers.cloudflare.com/china-network/).

Oct 19, 2026

## [Precursor adds Monitor mode](https://developers.cloudflare.com/changelog/post/2026-10-19-precursor-monitor-mode/)

[Bots](https://developers.cloudflare.com/bots/)

We released Monitor mode at customers' request so they can test Precursor and the Precursor Interstitial without updating bot score.

In **Security** > **Settings** , the Precursor **Status** dropdown now offers _Off_ , _Monitor_ , and _Arm_. Selecting _Arm_ means Precursor detections can affect bot score and Challenge clearance. Selecting _Monitor_ means Precursor detections do not affect bot score or Challenge clearance.

![Precursor Status dropdown with Off, Monitor, and Arm options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=739,height=235,format=webp/_astro/precursor-monitor-mode-status.CRb5Sudr.png)

We also separated the Precursor Interstitial from the mode. Set the sitewide default with **Show Interstitial** , then add **Interstitial Rules** to customize it for specific requests. For example, leave **Show Interstitial** off across most of your site, but require an interstitial Challenge on `/checkout` to enforce a valid session before purchase.

![Precursor settings with Show Interstitial off and an Open interstitial rules button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=600,height=441,format=webp/_astro/precursor-interstitial-settings.Bpb_aV0o.png)

For more information, refer to the [**Precursor**](https://developers.cloudflare.com/cloudflare-challenges/precursor/) documentation.

Sep 16, 2026

## [Control JavaScript Detections API results](https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/)

[Bots](https://developers.cloudflare.com/bots/)

Enterprise Bot Management customers can control whether Cloudflare uses results created through the JavaScript Detections API for bot scoring and detections.

Turn **JavaScript Detections for API traffic** on or off in **Security** > **Settings**. You can also configure the zone through the Bot Management API by setting `jsd_api_results_enabled`:
    
    
    {
    	"jsd_api_results_enabled": true
    }

This setting is separate from zone-wide script injection. When it is off, the API script can still execute and return `success` to the callback, but Cloudflare does not consume the result.

For more information, refer to [JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/#api).

Aug 31, 2026

## [Bot Management's machine learning model now retrains more frequently instead of shipping fixed versions](https://developers.cloudflare.com/changelog/post/2026-08-31-adaptive-intelligence/)

[Bots](https://developers.cloudflare.com/bots/)

We have launched Adaptive Intelligence, a new bot detection engine built to close the gap between when an attack pattern first appears and when protection against it reaches every customer. You can [read the announcement blog ↗︎](https://blog.cloudflare.com/introducing-adaptive-intelligence/) for the full story behind why we built it.

Adaptive Intelligence, the machine learning model behind your bot score, now retrains more frequently instead of shipping as a fixed, numbered version. As new bypass tools and bot frameworks appear, the model learns from them and folds that knowledge in without waiting for a scheduled release.

Every update is validated before it affects you. New model versions run in shadow mode first, scored but not acted on, and are compared against the current model before rolling out gradually.

Enterprise customers with **Auto-update machine learning** switched on under Bot Management configurations get Adaptive Intelligence automatically, with no version to migrate and nothing else to configure.

To learn more, refer to [Adaptive Intelligence](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/#adaptive-intelligence-business-and-enterprise) and [Machine Learning models](https://developers.cloudflare.com/bots/reference/machine-learning-models/).

Jul 13, 2026

## [Precursor introduces session-based bot detection](https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/)

[Bots](https://developers.cloudflare.com/bots/)

Precursor is rolling out to all customers starting today. Precursor is client-side JavaScript that enables session-based bot detection.

You can [read the announcement blog ↗︎](https://blog.cloudflare.com/introducing-precursor) for background on why we built Precursor and how session-level behavioral detection works.

With Precursor enabled, Cloudflare can:

  * Continuously evaluate behavioral signals across a session
  * Re-validate challenge clearance as behavior changes
  * Update bot scores with session context
  * Provide client-side visibility where none previously existed



It integrates with existing protections, including Security Rules, and can be enabled directly from the Cloudflare dashboard with configurable modes to balance security and user experience.

![Animated walkthrough of enabling Precursor in the Cloudflare dashboard](https://developers.cloudflare.com/images/precursor/enabling_precursor.gif)

To learn more, refer to the [Precursor documentation](https://developers.cloudflare.com/cloudflare-challenges/precursor/).

Jul 1, 2026

## [New options to manage AI traffic](https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/)

[Bots](https://developers.cloudflare.com/bots/)

Not all AI traffic is the same. Now, all customers — including those on the Free plan — can manage AI crawlers based on what they actually do on your site. Cloudflare groups AI traffic into three behaviors you can control independently: [Search, Agent, and Training](https://developers.cloudflare.com/bots/concepts/bot/#ai-bots). This lets you keep the automated traffic that sends readers and revenue back to you, while blocking the traffic that only takes from your content.

Each behavior maps to a real use case. **Search** covers crawlers that index your content so they can answer questions about it later, where you should expect referral traffic or other equitable compensation in return. **Agent** covers automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents. **Training** covers crawlers that take your content to train or fine-tune a model. For each preset you can choose to block on all pages, block only on pages that display ads, or choose not to block.

![The Configure AI bot traffic policies screen, where Search, Agent, and Training can each be set to allow, block, or block only on pages with ads](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=4720,height=2966,format=webp/_astro/ai-bot-traffic-policies.BqXU7Gmv.png)

Starting **September 15, 2026** , new domains onboarding to Cloudflare receive updated defaults: Bots classified as Training or as Agent are blocked on pages that display ads, while **Search** remains allowed. On that date, multi-purpose crawlers that combine Search and Training will be affected by the new defaults to block Training. All customers can [opt out of the new defaults ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/settings) at any time before September 15.

Jul 1, 2026

## [More visibility into bot traffic with BotBase and Business Insights](https://developers.cloudflare.com/changelog/post/2026-07-01-botbase-attribution-business-insights/)

[Bots](https://developers.cloudflare.com/bots/)

With Content Independence Day 2026, [Enterprise Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/) customers get two new tools that make bot traffic far easier to see and reason about: [BotBase](https://developers.cloudflare.com/bots/botbase/), a searchable directory of every bot Cloudflare tracks, and [Business Insights](https://developers.cloudflare.com/bots/business-insights/), a dashboard that shows how much value each crawler sends back to your business.

BotBase is Cloudflare's directory of all known bots and agents, available directly in the dashboard. It shows how Cloudflare classifies each bot by behavior — Search, Agent, Training, and other categories such as Transact, Data Collection, SEO, and Ads Verification — so you can understand why a given crawler is visiting you. You can search and filter the full catalogue, filter your own traffic down to a single bot to investigate its activity on your zone, and copy any bot's detection ID to target it precisely in [Security rules](https://developers.cloudflare.com/security/rules/). Every tracked bot in BotBase is also published in [Cloudflare Radar's bots and agents directory ↗︎](https://radar.cloudflare.com/bots/directory).

Business Insights is built for content owners and business decision-makers who want to know which bots help or harm their business, without reading rule syntax. The dashboard reports crawl-to-referral ratios both site-wide and per bot operator — comparing how often a company crawls your content against how many visitors it actually refers back — over the last 24 hours, 7 days, or 30 days. Each operator is labeled with Cloudflare's [updated classification](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) and an action status of Allowed, Blocked, or Partially blocked, giving stakeholders a shared, at-a-glance view of the AI traffic reaching your site.

![The Business Insights dashboard, showing bot traffic, content page requests, crawl-to-referral ratio, and a per-operator bot activity table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=8192,height=5064,format=webp/_astro/attribution-business-insights.Cu-ZtxkX.png)
