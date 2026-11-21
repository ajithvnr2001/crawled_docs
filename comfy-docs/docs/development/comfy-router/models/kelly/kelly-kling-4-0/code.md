---
url: https://docs.comfy.org/development/comfy-router/models/kelly/kelly-kling-4-0/code/
title: Use Kelly Kling 4.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:28.874682+00:00
---

# Use Kelly Kling 4.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kelly/kelly-kling-4-0/code/

## On this page

Back to top

  * Request setup
  * Schema
    * Input
    * Output
  * Before you ship



Kelly

# Use Kelly Kling 4.0 with Comfy Router

Copy pageCopy page

Call kelly/kelly-kling-4.0 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kelly/kelly-kling-4.0`, served by Comfy Router from Kelly. **Input:** Text · **Output:** Video

## Request setup

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. For Python, run `pip install comfy-sdk`. For TypeScript, run `npm install @comfyorg/sdk`. cURL uses raw HTTP. **Model ID:** `kelly/kelly-kling-4.0` **Endpoint:** `POST https://api.comfy.org/v2/models/kelly/kelly-kling-4.0`

Router has not published an authored input schema for this model, so there is no request example to generate a snippet from. Router forwards the body to Kelly unchanged: build it from Kelly’s own API documentation, then send it with the [Router quickstart](https://docs.comfy.org/development/comfy-router/quickstart).

## Schema

### Input

Router has not published an authored input schema for this model yet: `GET /v2/models/kelly/kelly-kling-4.0/openapi.json` returns an open object with `x-comfy-input-schema-authored: false`. Router forwards the body to Kelly unchanged, so Kelly’s own API documentation is authoritative for the request fields, and Router does not perform model-specific input validation. Provider validation still applies.

### Output

_This schema does not declare named properties._

## Before you ship

The SDKs create an `Idempotency-Key` and reuse it for automatic retries. For manual retries, reuse the original key. Router can hold the connection for up to 10 minutes. When a request fails, Router sends an `X-Comfy-Error-Type` response header explaining why. A `422` means Router rejected the input before calling the provider, and a `413` means the request body was larger than Router accepts. Download generated assets promptly because [result URLs can expire](https://docs.comfy.org/development/comfy-router/reference#result-assets). Any size limit named in a field description above is the provider’s own bound on that field, quoted from the provider’s specification. Router applies a separate cap to the whole request body, which base64-encoded media counts against: see [request body size](https://docs.comfy.org/development/comfy-router/limitations#request-bodies-are-capped). This page documents one partner model called through Comfy Router. The same `comfy-sdk` / `@comfyorg/sdk` package also ships a second client, for running a whole ComfyUI workflow graph on Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, with `client.workflows`, `client.assets` and `client.jobs`. See [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

## Headers

Authentication, idempotency, request IDs, error buckets, retry pacing, spend limits.

## Using the Router API

Model discovery, validation errors, retries, and billing.

## Limitations

What Router does not do today, and what to use instead.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kelly/kelly-kling-4-0/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kelly/kelly-kling-4-0/code)

[P Image Ideogram](https://docs.comfy.org/development/comfy-router/models/ideogram/p-image-ideogram/code)[Kelly Seedance 2.0 Fast](https://docs.comfy.org/development/comfy-router/models/kelly/kelly-seedance-2-0-fast/code)
