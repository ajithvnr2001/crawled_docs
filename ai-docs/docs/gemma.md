---
url: https://ai.google.dev/gemma/
title: Gemma
method: httpx+scrapegraph (scrapling: scrapling thin content (581 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:46:18.098615+00:00
---

# Gemma

> Source: https://ai.google.dev/gemma/

![The text "EmbeddingGemma 2" in white and blue lettering, set against a dark background with layered blue geometric panels.](https://lh3.googleusercontent.com/UoMsDYSnnnPPBbZwTdU8PcQ3f2w0rq40xnh_uoln_sH3d1UDXD_uOxTphNqFbXFNOrHVLlQQWQECzQofXAjc5ln4NPZNN6La-1hmLF1tN9z2U7esLcHKdUsTaSCLT6I=w1440-h810-n-nu)

October 2026

### EmbeddingGemma 2

Expanding beyond text to unify code, images, video, and audio in a shared embedding space

[ Read blog ](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)
