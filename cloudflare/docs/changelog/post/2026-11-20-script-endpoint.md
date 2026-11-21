---
url: https://developers.cloudflare.com/changelog/post/2026-11-20-script-endpoint/
title: Run custom scripts in Browser Run with /script \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:30.565336+00:00
---

# Run custom scripts in Browser Run with /script · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-20-script-endpoint/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 20, 2026

## Run custom scripts in Browser Run with /script

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) now runs custom browser automation written with Playwright, Puppeteer, or the raw Chrome DevTools Protocol (CDP) in a single API request, with the new [`/script` endpoints](https://developers.cloudflare.com/browser-run/script/). Submit a JavaScript function, and Browser Run executes it in an isolated Worker connected to a browser session, so you do not need to deploy a Worker.
    
    
    curl -i -X POST "https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-run/script" \
      -H "Authorization: Bearer <apiToken>" \
      -H "Content-Type: application/json" \
      -d '{
        "code": "async ({ page }) => { await page.goto(\"https://example.com\"); return { title: await page.title() }; }",
        "library": "playwright"
      }'
    
    
    HTTP/2 200
    content-type: application/json
    cf-browser-session-id: 8f7c2e3a-1b4d-4c6e-9a0f-2d5b7e9c1a3f
    cf-browser-target-id: A1B2C3D4E5F60718293A4B5C6D7E8F90
    
    {
      "success": true,
      "result": {
        "title": "Example Domain"
      }
    }

  * `POST /script` acquires a browser, runs your function, and returns its result as `{ "success": true, "result": ... }`. The session and page are returned in the `cf-browser-session-id` and `cf-browser-target-id` response headers (except Kitesurf runs).
  * `POST /script/<sessionId>` runs follow-up scripts in a session you already hold, from `/script` or from `POST /devtools/browser`. Pass `targetId` to attach to a specific page, or create extra pages to run scripts concurrently in one session.
  * Session launch options (`keep_alive`, `recording`, `lab`) go in the `/script` query string. Use `browser=kitesurf` to run a CDP script on [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/).
  * From a Worker, call the same endpoints through the [browser binding](https://developers.cloudflare.com/browser-run/script/#use-the-browser-binding) with `env.BROWSER.script()`, without an API token.
  * From the Cloudflare dashboard, write and run scripts against a live browser in [Script Studio](https://developers.cloudflare.com/browser-run/script/#try-scripts-in-the-dashboard), without an API token.
  * Neither endpoint closes the session after your script runs. Close it with `DELETE /devtools/browser/<sessionId>` or `browser.close()`. Otherwise, it ends at its idle timeout.



For more information, refer to [Custom scripts](https://developers.cloudflare.com/browser-run/script/).
