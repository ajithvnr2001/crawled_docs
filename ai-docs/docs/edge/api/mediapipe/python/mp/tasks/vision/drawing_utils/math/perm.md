---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/perm/
title: mp.tasks.vision.drawing_utils.math.perm
method: httpx+scrapegraph (scrapling: scrapling thin content (799 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:42:28.716860+00:00
---

# mp.tasks.vision.drawing_utils.math.perm

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/perm/

Number of ways to choose k items from n items without repetition and with order.

#### View aliases

**Main aliases**

[`mp.tasks.vision.drawing_styles.drawing_utils.math.perm`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/tasks/vision/drawing_utils/math/perm)
    
    
    mp.tasks.vision.drawing_utils.math.perm(
        n, k, /
    )
    

Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n.

If k is not specified or is None, then k defaults to n and the function returns n!.

Raises TypeError if either of the arguments are not integers. Raises ValueError if either of the arguments are negative.
