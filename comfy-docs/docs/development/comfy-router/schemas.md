---
url: https://docs.comfy.org/development/comfy-router/schemas/
title: Comfy Router model schemas and results - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:53.476990+00:00
---

# Comfy Router model schemas and results - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/schemas/

## On this page

  * Read input and output schemas
    * Cache a schema
  * Validation and fallback schemas
  * Read the result
  * Next



Router API

# Comfy Router model schemas and results

Copy pageCopy page

Fetch a Router model’s OpenAPI input and output schema, cache it with ETags, and read the model’s native result shape.

Copy pageCopy page

Each Router model accepts its own native request body and returns its own native result. Read the model’s schema to learn both.

## 

​

Read input and output schemas

Each model exposes a standalone OpenAPI document:
    
    
    curl --dump-header schema-headers.txt \
      -H "X-API-Key: $COMFY_API_KEY" \
      https://api.comfy.org/v2/models/bfl/flux-2-pro/openapi.json
    

Within the model operation, `requestBody` describes the input, and the `200` response describes the output when an output schema has been authored. Input validation and output documentation are different: Router validates against its input schema but does not validate the returned provider result against its output schema. Inspect the output media type as well as its fields. An unauthored output can use `*/*`, and some models return binary data rather than JSON.

### 

​

Cache a schema

Save the schema and its `ETag`. On a later schema fetch, pass that ETag in `If-None-Match`. A `304` has no body; keep the cached document. A `200` supplies a replacement document and ETag.
    
    
    curl -H "X-API-Key: $COMFY_API_KEY" \
      -H 'If-None-Match: "previous-etag-value"' \
      https://api.comfy.org/v2/models/bfl/flux-2-pro/openapi.json
    

The schema route uses `Cache-Control: private, must-revalidate`. Keep authenticated responses out of shared caches. This ETag/304 behavior applies only to the schema endpoint.

## 

​

Validation and fallback schemas

An authored input schema rejects invalid fields before the provider call with `422` and a `detail[]` array. Read the field paths in `loc`; see [validation errors](https://docs.comfy.org/development/comfy-router/errors#validation-errors). Some schemas accept any JSON object and set `x-comfy-input-schema-authored: false`. Router forwards those requests without model-specific validation, so the provider can still reject them.

## 

​

Read the result

Router returns each model’s terminal result shape. There is no common image, video, or text envelope: BFL image output uses `result.sample`, while other models can return URL lists or inline bytes. Some asset URLs are rehosted by Comfy; others remain provider URLs or inline bytes. Check [result assets](https://docs.comfy.org/development/comfy-router/reference#result-assets) and download expiring assets promptly. Replays do not renew URLs.

## 

​

Next

  * [Queued requests](https://docs.comfy.org/development/comfy-router/queue): submit a run and collect the result later.
  * [Errors and retries](https://docs.comfy.org/development/comfy-router/errors): handle failures without paying twice.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/schemas.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/schemas)

[Discover Comfy Router modelsPrevious](https://docs.comfy.org/development/comfy-router/discover-models)[Queue Comfy Router requestsNext](https://docs.comfy.org/development/comfy-router/queue)

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
