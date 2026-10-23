---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/remainder/
title: mp.tasks.vision.drawing_utils.math.remainder
method: httpx+scrapegraph (scrapling: scrapling thin content (720 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:42:30.618988+00:00
---

# mp.tasks.vision.drawing_utils.math.remainder

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/remainder/

Difference between x and the closest integer multiple of y.

#### View aliases

**Main aliases**

[`mp.tasks.vision.drawing_styles.drawing_utils.math.remainder`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/remainder)
    
    
    mp.tasks.vision.drawing_utils.math.remainder(
        x, y, /
    )
    

Return x - n _y where n_ y is the closest integer multiple of y. In the case where x is exactly halfway between two multiples of y, the nearest even value of n is used. The result is always exact.
