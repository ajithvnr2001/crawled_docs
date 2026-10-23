---
url: https://ai.google.dev/gemini-api/docs/imagen/
title: Generate images using Imagen
method: httpx+scrapegraph (scrapling: scrapling thin content (761 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:44:14.736144+00:00
---

# Generate images using Imagen

> Source: https://ai.google.dev/gemini-api/docs/imagen/

Imagen is Google's legacy image generation model. It is now shut down and no longer available in the Gemini API.

## Migrate to Nano Banana

Migrate to Nano Banana for image generation:

  * **Model name** : Use `gemini-2.5-flash-image` (or Nano Banana 2 models such as `gemini-3.1-flash-image`) instead of Imagen model names.
  * **Method** : Use `client.models.generate_content` instead of `client.models.generate_images`.
  * **Response handling** : Nano Banana returns content parts containing image data instead of a specific image response object.



See the [Image generation guide](https://ai.google.dev/gemini-api/docs/image-generation) for details and examples.
