---
url: https://developers.cloudflare.com/changelog/product/byoip/
title: BYOIP Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:57:11.548160+00:00
---

# BYOIP Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/byoip/

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

BYOIP

Cache / CDN

CASB

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

Oct 13, 2026

## [Workers subrequests now preserve context for BYOIP destinations](https://developers.cloudflare.com/changelog/post/2026-10-13-byoip-workers-subrequest-context/)

[Workers](https://developers.cloudflare.com/workers/)[BYOIP](https://developers.cloudflare.com/byoip/)[Bots](https://developers.cloudflare.com/bots/)

Cloudflare now preserves Workers context when a subrequest targets a Cloudflare-proxied hostname using [Bring Your Own IP (BYOIP)](https://developers.cloudflare.com/byoip/). These requests are identified as Cloudflare-to-Cloudflare traffic instead of external Internet traffic.

Previously, some BYOIP subrequests could lose Workers context and original client signals. This could cause security rules to behave unexpectedly, Bot Management to evaluate an internal Cloudflare connection instead of the original client, or affected requests to return false `403` responses.

Workers subrequests to BYOIP destinations now preserve the [`CF-Worker`](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-worker) header and [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field. This supports consistent security rule evaluation across same-zone and cross-zone subrequests.

[Bot Management fields](https://developers.cloudflare.com/bots/reference/bot-management-variables/#o2o-and-subrequests) on the destination zone now represent the original end-user connection for affected BYOIP subrequests. Bot scores, verified bot status, and JA3/JA4 fingerprints no longer represent the internal connection between Cloudflare services.

Customers benefit from consistent security rule evaluation, accurate Bot Management results, and fewer unexpected failures when Workers access BYOIP-backed hostnames. The improvement is automatic and requires no configuration changes.

For more information, refer to [Cloudflare BYOIP](https://developers.cloudflare.com/byoip/) and [Workers subrequests](https://developers.cloudflare.com/workers/platform/limits/#subrequests).
