---
url: https://ai.google.dev/gemma/gemmaverse/
title: Explore Gemma models crafted by the community
method: httpx+scrapegraph (scrapling: scrapling thin content (621 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:46:17.713103+00:00
---

# Explore Gemma models crafted by the community

> Source: https://ai.google.dev/gemma/gemmaverse/

![](https://ai.google.dev/static/images/fallback/video_poster_fallback_light.57b61d57842a.jpg)![](https://ai.google.dev/static/images/fallback/video_poster_fallback_dark.4d55bc99efa6.jpg)

Your browser does not support the video tag.

### Understanding the language of single-cell biology

Based on Gemma and developed in collaboration with Yale University, [Cell2Sentence-Scale 27B](https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/) helped discover a potential new pathway for cancer therapy.
