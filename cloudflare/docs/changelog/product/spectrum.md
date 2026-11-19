---
url: https://developers.cloudflare.com/changelog/product/spectrum/
title: Spectrum Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.727944+00:00
---

# Spectrum Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/spectrum/

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

Spectrum

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

Nov 19, 2026

## [Redesigned Spectrum dashboard](https://developers.cloudflare.com/changelog/post/2026-11-19-redesigned-dashboard/)

[Spectrum](https://developers.cloudflare.com/spectrum/)

The Spectrum pages in the Cloudflare dashboard have been redesigned. Your existing applications and their settings do not change.

The **Spectrum Applications** page lists each application's type, edge port, origin, and edge IP type, with the last minute of connections, ingress, and egress. You can search the list and sort it by column.

Creating or editing an application now opens a full page instead of a modal, with settings grouped into **Application Configuration** , **Origin Configuration** , and **Advanced Options**. To edit an application, select its hostname, or select the three dots next to it > **Edit**.

You can now create and edit applications that use [static IPs](https://developers.cloudflare.com/spectrum/about/static-ip/) or [BYOIP](https://developers.cloudflare.com/spectrum/about/byoip/) addresses in the dashboard. Under **Edge IP Type** , select **Dedicated IPs**. Leave **Subdomain** blank to create an application on the zone apex.

New TCP and UDP applications created in the dashboard now have **IP Access Rules** turned off by default, which matches the API default. To enforce IP Access rules for an application, turn on **IP Access Rules** under **Advanced Options**. Existing applications keep their current setting.

To create your first application, refer to [Get started with Spectrum](https://developers.cloudflare.com/spectrum/get-started/).

To share feedback on the redesigned dashboard, complete [this form ↗︎](https://forms.gle/BW9RoXZpgx7B5HZC6).
