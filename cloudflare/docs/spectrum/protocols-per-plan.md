---
url: https://developers.cloudflare.com/spectrum/protocols-per-plan/
title: Protocols per plan \u00b7 Cloudflare Spectrum docs
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:39.437179+00:00
---

# Protocols per plan · Cloudflare Spectrum docs

> Source: https://developers.cloudflare.com/spectrum/protocols-per-plan/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Spectrum](https://developers.cloudflare.com/spectrum/)
  3. /Protocols per plan



# Protocols per plan

Last updated Nov 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

On this table, you have information about which protocols are available per plan.

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | Paid add-on | Paid add-on | Yes  
TCP (IP or DNS origin) | No | No | No | Paid add-on  
TCP (Worker origin, beta) | No | One app per zone | One app per zone | Paid add-on  
UDP | No | No | No | Paid add-on  
HTTP | No | No | No | Paid add-on  
HTTPS | No | No | No | Paid add-on  
Minecraft (one app allowed) | No | Yes | Yes | Yes  
SSH (one app allowed) | No | Yes | Yes | Yes  
RDP (one app allowed) | No | No | Yes | Yes  
  
For [Worker origins](https://developers.cloudflare.com/spectrum/how-to/route-tcp-traffic-to-a-worker/), each application uses a single TCP port. Pro and Business zones without Spectrum Enterprise can create one Worker-origin application in addition to their existing plan-supported applications. Port ranges are not supported.

The Enterprise column requires Spectrum Enterprise access, which is separate from a zone's Enterprise plan. [TLS termination](https://developers.cloudflare.com/spectrum/reference/settings-by-plan/) requires Spectrum Enterprise. Applications on Pro and Business subscriptions without Spectrum Enterprise pass TCP traffic through without terminating TLS.

[PreviousOverview](https://developers.cloudflare.com/spectrum/)[NextBYOIP](https://developers.cloudflare.com/spectrum/about/byoip/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/spectrum/protocols-per-plan.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
