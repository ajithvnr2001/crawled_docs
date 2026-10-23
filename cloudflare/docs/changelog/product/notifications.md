---
url: https://developers.cloudflare.com/changelog/product/notifications/
title: Notifications Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:49.219476+00:00
---

# Notifications Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/notifications/

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

Oct 2, 2026

## [Webhooks on all plans and coding agent destinations](https://developers.cloudflare.com/changelog/post/2026-10-02-destination-enhancements/)

[Notifications](https://developers.cloudflare.com/notifications/)

Webhook destinations are now available on every Cloudflare plan, including Free. Previously, webhooks required a Pro plan or higher. Accounts without a paid zone can configure up to 100 webhook destinations.

Coding agents are also now supported as alert destinations. You can deliver alerts directly to supported coding agents alongside email, webhooks, and PagerDuty.

To configure destinations, go to **Observability** > **Alerts** > **Destinations** in the Cloudflare dashboard. For setup details, refer to [Configure webhooks](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/).

Oct 2, 2026

## [Monitors (Beta)](https://developers.cloudflare.com/changelog/post/2026-10-02-monitors/)

[Notifications](https://developers.cloudflare.com/notifications/)

The Alerts section now includes **Monitors** (Beta), a dedicated space for creating alerts based on your own [SQL API](https://developers.cloudflare.com/analytics/sql-api/) queries. Monitors are available under **Observability** > **Alerts** > **Monitors** in the Cloudflare dashboard.

![Monitors empty state showing the Create Monitor button and a diagram of the query-to-monitor-to-destinations flow.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2326,height=1014,format=webp/_astro/monitors-empty-state.BDD8ZbSb.png)

Each monitor evaluates a query against a supported SQL API dataset on a schedule and sends a notification when the result meets your detection criteria. Three detection methods are available:

  * **Threshold** : triggers when a query result crosses a fixed value.
  * **Anomaly detection** : triggers when a query result deviates from its historical baseline by more than a configured sensitivity.
  * **SLO** : triggers when the ratio of successful events to total events drops below a target percentage.



The monitor builder includes a visual query builder, custom SQL support, and a query preview that charts the signal over a configurable time range of up to 7 days.

![Monitor query builder showing dataset selection, metric, filters, and a query preview chart with anomaly bounds.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2542,height=1306,format=webp/_astro/monitors-query-builder.Bn253N-Y.png)

Pre-defined notifications for DDoS, SSL/TLS, Health Checks, and other Cloudflare products are now listed separately under **Platform Notifications**.

For configuration details, refer to [Monitors](https://developers.cloudflare.com/notifications/monitors/).
