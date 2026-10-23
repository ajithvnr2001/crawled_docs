---
url: https://ai.google.dev/gemini-api/docs/learnlm/
title: LearnLM
method: httpx+scrapegraph (scrapling: scrapling thin content (396 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:44:14.562536+00:00
---

# LearnLM

> Source: https://ai.google.dev/gemini-api/docs/learnlm/

LearnLM is no longer a separate listing in AI Studio. Instead, LearnLM capabilities have been integrated into Gemini starting with the [2.5 model series](https://ai.google.dev/gemini-api/docs/models).

To learn more about LearnLM's current status, visit the [LearnLM](https://cloud.google.com/solutions/learnlm) documentation.
