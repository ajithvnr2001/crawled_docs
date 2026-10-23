---
url: https://ai.google.dev/gemini-api/docs/model-tuning/
title: Fine-tuning with the Gemini API
method: httpx+scrapegraph (scrapling: scrapling thin content (614 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
Error: BrowserContext.add_cookies: Protocol error (Storage.setCookies): Invalid cookie fields

Code context:
 627           )
 628           self._api_zone.set(parsed_st)
 629           try:
 630               return await cb()
 631           except Exception as error:
 632 →             raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
 633           finally:
 634               self._api_zone.set(None)
 635   
 636       def wrap_api_call_sync(
 637           self, cb: Callable[[], Any], is_internal: bool = False, title: str = None)
fetched_at: 2026-10-23T11:44:26.218685+00:00
---

# Fine-tuning with the Gemini API

> Source: https://ai.google.dev/gemini-api/docs/model-tuning/

With the deprecation of Gemini 1.5 Flash-001 in May 2025, we no longer have a model available which supports fine-tuning in the Gemini API or AI Studio, but it is supported in [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning).

We don't have immediate plans to bring fine-tuning support but would love to [hear from you on our developer forum](https://discuss.ai.google.dev/c/gemini-api/4) if fine-tuning is important to your use case.
