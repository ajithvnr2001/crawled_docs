---
url: https://docs.comfy.org/development/comfy-router/headers/
title: Comfy Router headers - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:45.395678+00:00
---

# Comfy Router headers - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/headers/

## On this page

  * Request headers
  * Response headers
  * Status codes that carry two meanings
  * Next



Reference

# Comfy Router headers

Copy pageCopy page

The request headers you can send to Comfy Router and the response headers it returns, for every model: authentication, idempotency, request IDs, error buckets, retry pacing and spend limits.

Copy pageCopy page

Every Router model uses `POST /v2/models/{provider}/{model}` with its own JSON body. This page covers the headers shared across models; the [API reference](https://docs.comfy.org/development/comfy-router/reference) lists the generated contract. The Comfy SDKs (`comfy-sdk` for Python, `@comfyorg/sdk` for TypeScript) handle authentication and generate idempotency keys. They expose selected response metadata as described below. Raw HTTP clients must send and read the headers themselves.

## 

​

Request headers

​

X-API-Key

string

A Comfy API key, `comfyui-...`, created in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router). It uses your workspace’s model access and credit balance. You can also send it as `Authorization: Bearer comfyui-...`; if both headers are present, `X-API-Key` wins.

​

Authorization

string

`Bearer <token>`. A `comfyui-` value is an API key. Any other value is treated as a Comfy Cloud JWT.

​

Idempotency-Key

string

Identifies one logical generation. Generate and store a UUID before the call, then reuse it for retries of the unchanged request. The key can replay a result or collect accepted work for up to 24 hours. The SDKs generate keys and let you supply your own (`idempotency_key=` in Python, `idempotencyKey` in TypeScript). See [retry outcomes](https://docs.comfy.org/development/comfy-router/errors#retry-outcomes) for conflicts, expiry, and non-replayable results.

​

Content-Type

string

`application/json`. Send the model’s native JSON input. Fields and validation requirements vary by model; see [Using the Router API](https://docs.comfy.org/development/comfy-router/api).

​

If-None-Match

string

On `GET /v2/models/{provider}/{model}/openapi.json` only. Send the `ETag` you hold from an earlier `200`; when it still matches, the answer is a bodyless `304` with the same `ETag`. Cache a model’s schema for the life of your process and revalidate it this way rather than re-reading it before every call.

## 

​

Response headers

​

X-Comfy-Request-Id

string

required

Identifies this HTTP request. Include it when contacting support. TypeScript exposes it as `requestId`; Python exposes `request_id` on errors.

​

X-Comfy-Error-Type

string

The machine-readable error category. On a `422`, use this header because the validation body has `detail[]` and no `error_type`. Combine it with the HTTP status to decide what to do. Treat an unknown value as `internal_error` for control flow and preserve it for diagnostics.

​

Idempotent-Replayed

boolean

Present and `true` when Router serves a stored result instead of running the model again. It is absent on a fresh run. On the queued submit route, a replayed `201` returns the original request handle rather than queueing a second run.

​

Retry-After

integer

Seconds to wait before retrying. On `409` / `concurrency_limit_exceeded` or `504` / `deadline_exceeded`, retry the same request and key after the wait. On `429` / `rate_limited`, it tells you when the rate limit resets. On a queued request’s status read and its `202` result read, it is Router’s hint for when polling again is worth the round trip.

​

X-Committed-Spend-Limit

integer

The ceiling on partner spend committed to calls still running, in USD cents. An enforcing spend gate can return it on admitted responses and on its `429` refusals. It is absent when the gate is not enforcing or a different control refused the request.

​

X-Committed-Spend-Current

integer

USD cents currently committed to calls in flight. An admitted response includes its own call; a `429` excludes the refused call. Sent alongside `X-Committed-Spend-Limit`.

​

X-Committed-Spend-Remaining

integer

USD cents left below the committed-spend ceiling. It can be positive on a refusal when the requested call costs more than the remaining amount.

​

ETag

string

On `GET /v2/models/{provider}/{model}/openapi.json`. Store it and send it back as `If-None-Match` to revalidate a cached schema.

​

Cache-Control

string

On the schema route: `private, must-revalidate`. Keep the response in a private cache and revalidate stale copies with the `ETag`.

## 

​

Status codes that carry two meanings

Three statuses are shared by two buckets, and the header is what tells them apart:

Status| `X-Comfy-Error-Type`| What to do  
---|---|---  
`409`| `concurrency_limit_exceeded`| The original call for this key is still running. Wait `Retry-After`, re-send the same key.  
`409`| `invalid_input`| Inspect the conflict. Restore the original request if you changed it. A consumed, non-replayable key cannot recover the result; use a new key only if you intend a new, potentially billable generation.  
`429`| `concurrency_limit_exceeded`| Too many calls in flight, or the committed-spend ceiling (see the `X-Committed-Spend-*` headers). Clears when one of your own calls finishes.  
`429`| `rate_limited`| Wait for `Retry-After` before retrying.  
`504`| `deadline_exceeded`| Router’s own 10-minute bound. With `Retry-After`, re-send the same key to collect the running generation.  
`504`| `provider_timeout`| The partner timed out. Follow the [retry and billing guidance](https://docs.comfy.org/development/comfy-router/errors#retry-outcomes); do not treat this as a guarantee of no charge.  
  
## 

​

Next

  * [Quickstart](https://docs.comfy.org/development/comfy-router/quickstart): send a request and read the result.
  * [Using the Comfy Router API](https://docs.comfy.org/development/comfy-router/api): model discovery, schemas, errors, retries, and billing.
  * [API reference](https://docs.comfy.org/development/comfy-router/reference): the generated contract these headers are defined in.
  * [Limitations](https://docs.comfy.org/development/comfy-router/limitations): what Router does not do today, and what to use instead.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/headers.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/headers)

[Comfy Router API referencePrevious](https://docs.comfy.org/development/comfy-router/reference)[Comfy Router capabilities and limitsNext](https://docs.comfy.org/development/comfy-router/limitations)

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
