---
url: https://docs.comfy.org/development/comfy-router/billing/
title: Comfy Router billing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:43.972766+00:00
---

# Comfy Router billing - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/billing/

## On this page

  * Model billing facts
  * Reconcile charges
  * Next



Router API

# Comfy Router billing

Copy pageCopy page

How Comfy Router charges for model calls, what the catalog’s policy-refusal billing field means, and how to reconcile usage.

Copy pageCopy page

You are billed when the provider bills Comfy. The same rule applies to synchronous and [queued](https://docs.comfy.org/development/comfy-router/queue#idempotency-and-billing) calls, and a same-key [retry](https://docs.comfy.org/development/comfy-router/errors#retry-outcomes) that replays a result is not a second charge.

## 

​

Model billing facts

`GET /v2/models` and the model detail response include `billing.charges_on_policy_rejection`. This describes a policy refusal, not every failure or a price estimate.

Value| Meaning  
---|---  
`yes`| A policy refusal is charged.  
`no`| A policy refusal is not charged.  
`unknown`| Nobody has established the behavior yet. Treat it as maybe charged.  
  
Compare these strings explicitly: `"no"` is truthy in Python and JavaScript. Treat any unrecognized value as `unknown`. A request refused for lack of credits reports `insufficient_credits`.

## 

​

Reconcile charges

Provider payloads may include their own cost or usage numbers; those are not the Comfy charge. `X-Comfy-Credits-Used` is available only for some models and successful responses. When Router replays a result for the same `Idempotency-Key`, it repeats the original header with `Idempotent-Replayed: true`. The call is still charged once, so do not count a replayed header again. An absent header does not mean the call was free. Use [workspace usage and invoices](https://platform.comfy.org) for reconciliation, and preserve the request ID when investigating a charge.

## 

​

Next

  * [Limitations](https://docs.comfy.org/development/comfy-router/limitations#comfy-charges-and-usage): what Router does and does not report about charges.
  * [Errors and retries](https://docs.comfy.org/development/comfy-router/errors): retry without creating a second billable call.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/billing.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/billing)

[Comfy Router errors and retriesPrevious](https://docs.comfy.org/development/comfy-router/errors)[Comfy Router API referenceNext](https://docs.comfy.org/development/comfy-router/reference)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
