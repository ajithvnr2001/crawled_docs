---
url: https://aistudio.google.com/apps/
title: Sign in
method: httpx+scrapegraph (scrapling: scrapling thin content (429 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../usr/local/lib/python3.10/dist-packages/playwright/_impl/_connection.py):
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
fetched_at: 2026-10-23T11:46:28.376861+00:00
---

# Sign in

> Source: https://aistudio.google.com/apps/

![](https://www.gstatic.com/images/branding/googleg_gradient/svg/googleg_gradient_standard_48px.svg)

# Sign in

Use your Google Account

Email or phone

Forgot email?

Type the text you hear or see

Not your computer? Use Guest mode to sign in privately. [Learn more about using Guest mode](https://support.google.com/chrome/answer/6130773?hl=en-US)

Next

Create account
