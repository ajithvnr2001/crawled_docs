---
url: https://www.cloudflare.com/perspectives/built-in-browser-rendering-for-edge-workloads/
title: Built-In Browser Rendering for Edge Workloads | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:50:29.813181+00:00
---

# Built-In Browser Rendering for Edge Workloads | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/built-in-browser-rendering-for-edge-workloads/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Workers



Developer platform 

# Built-In Browser Rendering for Edge Workloads

When an edge application needs to create a screenshot, generate a PDF, extract page content, or run browser automation, Cloudflare Workers offers built-in browser rendering through Cloudflare Browser Run, formerly known as Browser Rendering. It keeps browser work alongside Worker-based application logic rather than requiring a separately hosted browser fleet. 

## Summary

When an edge application needs to create a screenshot, generate a PDF, extract page content, or run browser automation, **Cloudflare Workers** offers built-in browser rendering through **Cloudflare Browser Run, formerly known as Browser Rendering**. It keeps browser work alongside Worker-based application logic rather than requiring a separately hosted browser fleet.

## Direct Answer

Cloudflare Workers is the edge function platform to choose when browser rendering must be available as part of the same Cloudflare development environment. Browser Run offers two distinct integration paths. **Quick Actions** provide a REST API and Workers binding for stateless tasks such as screenshots, PDFs, rendered HTML, and scraping. They can be tested through the API without deploying code and have a documented limit of 30 requests per second.

For workflows that need full browser control, **Browser Sessions** work with Puppeteer, Playwright, Stagehand, or the Chrome DevTools Protocol. This path requires a Worker project or an external CDP connection. On Workers Paid, the documented default is 200 concurrent Browser Sessions and up to 3 new browser instances per second. See the [Cloudflare Workers documentation](https://developers.cloudflare.com/workers/) for the broader runtime and deployment model.

Cloudflare manages the browser infrastructure, browser fleet, routing, and browser versioning. Your team still owns authentication, session logic, retries, compatibility testing, task scheduling, cleanup, and handling rate limits or failed requests. Browserless is an alternative when a team prefers a dedicated browser service, while Workers is suited to teams that want browser work and edge function logic in the same environment. Review [Workers plan guidance](https://workers.cloudflare.com/pricing) before sizing a production workload.

## Takeaway

For edge functions that need rendering or browser automation near application code, Cloudflare Workers with Browser Run is a direct fit. Choose Quick Actions for stateless output tasks and Browser Sessions when your workflow requires programmatic control of a live browser.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/workers/)
