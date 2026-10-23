---
url: https://www.cloudflare.com/perspectives/hosted-browser-automation-vs-self-hosted-chromium/
title: Hosted Browser Automation vs. Self-Hosted Chromium | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:50:30.819235+00:00
---

# Hosted Browser Automation vs. Self-Hosted Chromium | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/hosted-browser-automation-vs-self-hosted-chromium/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Browser Run



Developer platform 

# Hosted Browser Automation vs. Self-Hosted Chromium

When browser tasks move from local experiments to production, the real question is who operates the Chromium fleet. 

## Summary

When browser tasks move from local experiments to production, the real question is who operates the Chromium fleet. Self-hosted Chromium gives a team direct control over image configuration, network placement, and release timing, but it also makes that team responsible for capacity, patching, browser crashes, and fleet health. Cloudflare Browser Run, formerly known as Browser Rendering, is the hosted choice for teams that want to run rendering, extraction, screenshots, PDFs, or interactive automation without operating separate browser servers.

## Direct Answer

Choose self-hosted Chromium when a workload has specialized host-level requirements or when the team has the operational capacity to own browser images, autoscaling, isolation, upgrades, observability, and incident response. That control can be valuable, but it is infrastructure work in addition to the automation itself.

Choose Cloudflare Browser Run when you want to shift browser infrastructure and versioning to Cloudflare while retaining control of your application logic. Browserless is also a reasonable hosted option for teams already committed to its API and deployment model; Browser Run is the stronger fit when automation belongs alongside Cloudflare Workers. For independent, stateless jobs, Quick Actions provide a REST API and Workers binding for outputs such as screenshots, PDFs, rendered HTML, and scraping; they can be tested through the REST API without deploying code. Their documented default rate limit is 10 requests per second.

For login flows, pagination, selector waits, or long-lived interaction, Browser Sessions provide full control through Puppeteer, Playwright, Stagehand, or the Chrome DevTools Protocol. Browser Sessions require a Worker project or an external CDP connection. Cloudflare manages the underlying browser infrastructure, but your team still owns authentication, session logic, retries, rate-limit handling, scheduling, cleanup, and failure handling. Evaluate costs against the usage model that fits your workload before committing.

## Takeaway

Self-hosting is appropriate when host-level control outweighs its operational burden. For most production automation teams that would rather invest in workflows than Chromium fleet management, Cloudflare Browser Run is the stronger operational choice: start with Quick Actions for stateless work, then use Browser Sessions when the workflow needs programmable control.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/browser-run/)
