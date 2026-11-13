---
url: https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/
title: Billing and Limitations \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:13.904924+00:00
---

# Billing and Limitations · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Static Assets](https://developers.cloudflare.com/workers/static-assets/)
  4. /Billing and Limitations



# Billing and Limitations

Last updated Nov 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBillingLimitations Range requestsTroubleshooting

## Billing

Requests to a project with static assets can either return static assets or invoke the Worker script, depending on if the request [matches a static asset or not](https://developers.cloudflare.com/workers/static-assets/routing/).

  * Requests to static assets are free and unlimited. Requests to the Worker script (for example, in the case of SSR content) are billed according to Workers pricing. Refer to [pricing](https://developers.cloudflare.com/workers/platform/pricing/#example-2) for an example.
  * There is no additional cost for storing Assets.
  * **Important note for free tier users** : When using [`run_worker_first`](https://developers.cloudflare.com/workers/static-assets/binding/#run_worker_first), requests matching the specified patterns will always invoke your Worker script. If you exceed your free tier request limits, these requests will receive a 429 (Too Many Requests) response instead of falling back to static asset serving. Negative patterns (patterns beginning with `!/`) will continue to serve assets correctly, as requests are directed to assets, without invoking your Worker script.



## Limitations

See the [Platform Limits](https://developers.cloudflare.com/workers/platform/limits/#static-assets)

### Range requests

When a request for a static asset includes a `Range` header, Workers returns `200 OK` with the full file instead of `206 Partial Content`, and the response has no `Content-Range` or `Accept-Ranges` header. Some clients need range support, for example Safari when it plays video.

To serve byte ranges, route the affected paths to your Worker with [`run_worker_first`](https://developers.cloudflare.com/workers/static-assets/binding/#run_worker_first). In your Worker, fetch the file with `env.ASSETS.fetch()`, then return a `206 Partial Content` response that contains the requested bytes and a `Content-Range` header.

## Troubleshooting

  * `assets.bucket is a required field` — if you see this error, you need to update Wrangler to at least `3.78.10` or later. `bucket` is not a required field.
  * Asset requests fail after a deployment — HTML and asset requests may use different versions. An older page may also request a file missing from the version handling that request. Refer to [Version skew and static assets](https://developers.cloudflare.com/workers/versions-and-deployments/version-skew/).



[PreviousDirect Uploads](https://developers.cloudflare.com/workers/static-assets/direct-upload/)[NextOverview](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/billing-and-limitations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
