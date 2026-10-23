---
url: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/authoring/
title: Module: tf.lite.experimental.authoring
method: httpx+scrapegraph (scrapling: scrapling thin content (457 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:42:35.788212+00:00
---

# Module: tf.lite.experimental.authoring

> Source: https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/authoring/

Public API for tf._api.v2.lite.experimental.authoring namespace

## Functions

[`compatible(...)`](https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/authoring/compatible): Wraps [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) into a callable function with TFLite compatibility checking.
