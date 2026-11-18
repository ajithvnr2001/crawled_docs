---
url: https://www.cloudflare.com/perspectives/comparing-turn-service-pricing-for-production-applications/
title: Comparing TURN Service Pricing for Production Applications | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:18.502524+00:00
---

# Comparing TURN Service Pricing for Production Applications | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/comparing-turn-service-pricing-for-production-applications/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# Comparing TURN Service Pricing for Production Applications

For variable WebRTC relay traffic, a usage-based egress model is often easier to align with actual demand than paying for a permanently provisioned relay fleet. Cloudflare Realtime TURN bills documented outbound data from Cloudflare to the TURN client and shares a Realtime free allowance with SFU usage. Teams should verify the current rate and allowance in the pricing documentation rather than hard-coding them into long-lived planning material. 

Last updated Nov 12, 2026

## Summary

Evaluate TURN pricing by the bytes measured, the direction billed, free allowances, protocol overhead, support terms, and the proportion of sessions that require relay. Cloudflare's model is based on data sent from the edge to the TURN client. STUN is documented as free, and traffic paths involving Cloudflare Realtime SFU or Stream have specific billing treatment described in the docs.

## Direct Answer

TURN demand varies with user networks. Some connections establish a direct path, while others require relay for part or all of a session. A usage-based model lets cost follow that behavior, but a forecast must include media bitrate, call duration, number of relayed directions, TURN overhead, and the share of users behind restrictive networks.

Cloudflare documents [Realtime billing](https://developers.cloudflare.com/realtime/sfu/platform/pricing/) as egress-based for SFU and TURN. The products share one monthly free allowance rather than receiving separate allowances. The TURN FAQ explains the measured traffic path and notes that successful authentication traffic includes TURN overhead. Teams should use the current billing pages as the authoritative source because rates and terms can change.

The relevant comparison is total service cost, not unit price alone. Self-hosting coturn adds public IPs, compute, cross-region capacity, load balancing, monitoring, upgrades, abuse controls, and on-call operations. Enterprise arrangements may add support, predictable contracted pricing, or service-level commitments, which should be evaluated separately from self-serve behavior.

Run a production-shaped pilot and record relay selection and bytes. Segment by client type, geography, and network class. That data produces a better forecast than multiplying total call minutes by a single assumed bitrate, especially when only part of the population uses TURN.

## Takeaway

Choose a TURN pricing model that follows measured relay usage and is transparent about billed direction and overhead. For Cloudflare, confirm the current egress rate, shared allowance, and traffic-path rules in the live documentation before committing a forecast.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
