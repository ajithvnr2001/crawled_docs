---
url: https://docs.comfy.org/development/comfy-router/discover-models/
title: Discover Comfy Router models - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:44.362670+00:00
---

# Discover Comfy Router models - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/discover-models/

## On this page

  * Discover the catalog
    * Pagination
  * Read one model
  * Next



Router API

# Discover Comfy Router models

Copy pageCopy page

List the Comfy Router catalog with GET /v2/models, page through it with cursors, and fetch one model’s entry by its ID.

Copy pageCopy page

Every Router model is addressed by an ID of the form `{provider}/{model}`. Use the catalog to find that ID, then call `POST /v2/models/{provider}/{model}`.

## 

​

Discover the catalog

List models with the same API key used for generation:
    
    
    curl -H "X-API-Key: $COMFY_API_KEY" \
      "https://api.comfy.org/v2/models?limit=50"
    

An abbreviated catalog response:
    
    
    {
      "data": [
        {
          "id": "bfl/flux-2-pro",
          "provider": "bfl",
          "model": "flux-2-pro",
          "billing": { "charges_on_policy_rejection": "no" }
        }
      ],
      "has_more": true,
      "next_cursor": "example-cursor",
      "limit": 50
    }
    

Use `id` in the invocation path. The `billing` object contains billing facts, not a price. Read [policy-refusal billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts) before relying on it.

### 

​

Pagination

  * When `has_more` is `true`, pass the returned `next_cursor` as `cursor`. Stop when `has_more` is `false`, even if an earlier page was shorter than requested.
  * Treat cursors as opaque. URL-encode the value, for example with cURL `--get --data-urlencode "cursor=$NEXT_CURSOR"`; do not calculate offsets or modify the cursor.
  * `limit` defaults to 20 and is capped at 100. Values above the cap are clamped; zero and negative values select the default. The response reports the limit actually used.
  * An invalid cursor returns `400` / `invalid_input`. It does not silently restart the list.
  * A cursor can remain valid across catalog updates, but traversal is not a snapshot: a model added before your current position may not appear in that walk.

`503` / `service_unavailable` is temporary. Retry with backoff; do not treat it as an empty catalog. SDK run methods call the selected model directly.

## 

​

Read one model

Fetch a catalog entry directly when you know the model ID:
    
    
    curl -H "X-API-Key: $COMFY_API_KEY" \
      https://api.comfy.org/v2/models/bfl/flux-2-pro
    

The model detail endpoint avoids walking the entire catalog. Use the [API reference](https://docs.comfy.org/development/comfy-router/reference) for the complete entry fields.

## 

​

Next

  * [Schemas and results](https://docs.comfy.org/development/comfy-router/schemas): read a model’s input and output schema before calling it.
  * [All models](https://docs.comfy.org/development/comfy-router/models): browse the catalog with a working request for each model.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/discover-models.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/discover-models)

[Comfy Router API overviewPrevious](https://docs.comfy.org/development/comfy-router/api)[Comfy Router model schemas and resultsNext](https://docs.comfy.org/development/comfy-router/schemas)

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
