---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/
title: Integrate Workers \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:37:09.239704+00:00
---

# Integrate Workers · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)
  4. /Integrate Workers



# Integrate Workers

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Public beta

The Gateway Forward action is available in public beta on all Zero Trust plans. Workers usage is subject to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

Use Cloudflare Workers to add your own logic to HTTP traffic that passes through Gateway. A Gateway HTTP policy with the **Forward** action sends matching, permitted traffic to a Worker in your account. The Worker can modify a request, transform a response, return its own response, or start background work such as a notification or an R2 write. You can write your own Worker for your use case or adapt a [Worker template](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/).

Gateway handles the proxy connection, TLS decryption, and upstream routing. Your Worker receives standard `Request` and `Response` objects and [Gateway context](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/) about the connection, policy, and user.

Gateway evaluates HTTP request policies before Forward policies. Body policies and inspection run after Worker invocation and can interrupt the Worker if they block the request.

A Forward policy does not override a Block policy or replace Gateway inspection. Refer to [How Forward works](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#how-it-works) for the request and response inspection order.

WebSocket traffic connects directly to the original upstream service and bypasses the Worker. Refer to [Known limitations](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#known-limitations) for protocol restrictions and other constraints.

  * [Forward traffic](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/): Deploy a Worker and select it in a Gateway HTTP policy.
  * [Available context](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/): Read connection metadata, user identity, and device posture.
  * [Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/): Start with a small script for notifications, capture, or content transformation.



The [gateway-workers skill ↗︎](https://github.com/cloudflare/skills/blob/main/skills/gateway-workers/SKILL.md) provides guidance for coding agents building or reviewing Workers used in Forward policies.

[PreviousHost selectors](https://developers.cloudflare.com/cloudflare-one/traffic-controls/egress-policies/host-selectors/)[NextForward traffic](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/integrate-workers/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
