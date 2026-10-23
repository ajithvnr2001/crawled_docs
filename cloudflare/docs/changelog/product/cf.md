---
url: https://developers.cloudflare.com/changelog/product/cf/
title: Cloudflare CLI Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:21.119781+00:00
---

# Cloudflare CLI Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/cf/

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

Oct 17, 2026

## [Test Cron Triggers with Local Explorer](https://developers.cloudflare.com/changelog/post/2026-10-17-local-explorer-cron-triggers/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Local Explorer can now send one-off Cron Trigger invocations to a Worker's `scheduled()` handler during local development. This removes the need to construct request URLs when testing handler behavior.

Start your local development server with [`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development), [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev), or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Open `/cdn-cgi/local/explorer` on the server URL and select **Cron Triggers**.

The browser interface supports the following tasks:

  * Invoke configured cron expressions
  * Build ad hoc expressions
  * Set reusable scheduled times
  * Inspect outcomes and `noRetry()` status



Ad hoc triggers and scheduled time presets stay in your browser. They do not change `cloudflare.config.ts`, your Wrangler configuration, or deployed Cron Triggers. Local development does not run cron schedules automatically.

Full logs and traces are available in the development session that owns the Worker when that session has **Observability** turned on.

The following example uses port `8787`. Replace it with your development server port, such as `5173` for Vite.

The Local Explorer API exposes the same operation for tools and AI agents. The request targets an exact Worker name and accepts a cron expression and optional scheduled time:
    
    
    curl -X POST \
      "http://localhost:8787/cdn-cgi/local/explorer/api/local/scheduled?worker=my-worker" \
      -H "Content-Type: application/json" \
      --data '{"cron":"0 * * * *","scheduled_time":1745856238000}'

For more details, refer to [Test Cron Triggers with Local Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/#test-cron-triggers).

Oct 16, 2026

## [Search Cloudflare documentation with the Cloudflare CLI](https://developers.cloudflare.com/changelog/post/2026-10-16-docs-search/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Cloudflare CLI `1.0.0-beta.16` includes `cf docs search`, so you and your coding agent can find Cloudflare documentation without leaving the terminal. Search for guides, tutorials, and examples across Cloudflare products.

To install or update to the latest release:

npmyarnpnpmbun
    
    
    npm install --global cf@latest
    
    
    yarn global add cf@latest
    
    
    pnpm add --global cf@latest
    
    
    bun add --global cf@latest

Describe what you want to do, or ask a question:
    
    
    cf docs search "proxy a DNS record"
    cf docs search "rate limit requests with WAF"
    cf docs search "schedule a worker"

The command searches live Cloudflare documentation and returns up to five ranked JSON results. Each result includes a title, description, and documentation URL. An Internet connection is required.

![Terminal demo of Cloudflare CLI beta-16 searching DNS and WAF documentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=720,format=webp/_astro/docs-search-demo.cWBK3YBx.gif)

Agents can parse the results and fetch a complete page as Markdown. For example, use `jq` to select the first result, then request its URL with the `Accept: text/markdown` header:
    
    
    url=$(cf docs search "proxy a DNS record" | jq -r '.[0].url')
    curl -H "Accept: text/markdown" "$url"

This release also standardizes generated command names to kebab-case. For example, `cf accounts billing getCredits` becomes `cf accounts billing get-credits`. For the full list of breaking command and flag changes, refer to the [Cloudflare CLI release notes ↗︎](https://github.com/cloudflare/cf/blob/main/packages/cli/CHANGELOG.md).

For more information, refer to [Find Cloudflare documentation with a coding agent](https://developers.cloudflare.com/cf/agents/#find-cloudflare-documentation).

Sep 28, 2026

## [Cloudflare CLI is now in beta](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is now in beta. `cf` is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers, without switching between tools.

Install `cf` globally, then sign in:

npmyarnpnpmbun
    
    
    npm install --global cf
    
    
    yarn global add cf
    
    
    pnpm add --global cf
    
    
    bun add --global cf
    
    
    cf auth login

With `cf`, you can:

  * **Manage resources across Cloudflare.** More than 2,900 commands cover the public Cloudflare API, and most print their results as JSON.
  * **Create and deploy Workers.** `cf init` creates a project that uses [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), a typed configuration file. `cf dev`, `cf build`, and `cf deploy` develop, build, and deploy it.
  * **Move from Wrangler.** `cf migrate` converts a Wrangler configuration file to `cloudflare.config.ts`. You can also run `cf` resource commands in an existing Wrangler project without migrating it.
  * **Work with coding agents.** `cf cli search` finds the command for a task from a plain-language description, so an agent can find and run commands without prior knowledge of `cf`.



`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

To get started, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/). To move an existing project, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).
