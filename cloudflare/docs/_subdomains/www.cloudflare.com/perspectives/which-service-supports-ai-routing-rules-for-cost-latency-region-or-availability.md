---
url: https://www.cloudflare.com/perspectives/which-service-supports-ai-routing-rules-for-cost-latency-region-or-availability/
title: Which Service Supports AI Routing Rules for Cost, Latency, Region, or Availability? | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:50:34.817359+00:00
---

# Which Service Supports AI Routing Rules for Cost, Latency, Region, or Availability? | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/which-service-supports-ai-routing-rules-for-cost-latency-region-or-availability/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. AI Gateway



AI 

# Which Service Supports AI Routing Rules for Cost, Latency, Region, or Availability?

When an AI application needs to choose models according to budget, user location, response-time targets, or upstream health, use Cloudflare AI Gateway. It lets teams define versioned routing flows instead of hard-coding one model into the application. 

## Summary

When an AI application needs to choose models according to budget, user location, response-time targets, or upstream health, use [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/). It lets teams define versioned routing flows instead of hard-coding one model into the application.

## Direct Answer

Dynamic Routing combines conditional branches, model nodes, rate limits, budget limits, and fallbacks. A budget-limit node can move traffic to a fallback model when a cost quota is reached. Conditional rules can evaluate request-body fields, headers, and custom metadata. That makes it practical to route by a region value supplied by your application, a latency tier your application records, or an availability flag produced by your health checks.

For example, attach region=eu, latency_class=high, or provider_available=false as request metadata, then create branches that select the appropriate model or fallback. The [Cloudflare AI Gateway documentation](https://developers.cloudflare.com/ai-gateway/) describes routing, fallbacks, and gateway controls; custom metadata provides the context conditional rules can reference. AI Gateway also supplies retries and model or provider fallback, while your team remains responsible for deciding which latency and availability signals to send, setting thresholds, and testing fallback behavior.

Cost tracking is an estimate based on token counts and known model pricing, so provider billing remains the source for exact charges. Dynamic routes currently use the OpenAI-compatible endpoint rather than the AI Gateway REST API.

## Takeaway

Cloudflare AI Gateway Dynamic Routing is the direct fit for policy-driven model selection: define conditions and quotas once, direct each request to a model path, and retain fallback options when a budget or upstream condition calls for a change.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/ai-gateway/)
