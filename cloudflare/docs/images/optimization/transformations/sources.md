---
url: https://developers.cloudflare.com/images/optimization/transformations/sources/
title: Define source origins \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:16.659574+00:00
---

# Define source origins · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/transformations/sources/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Remote images (transformations)
  5. /Define source origins



# Define source origins

Last updated Nov 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure allowed origins Zone WorkerHow the allowlist worksMatch hostnames and subdomainsMatch pathsFollow redirectsAllow any origin Zone Worker

Transformation URLs fetch source images before applying optimizations.

By default, Images accepts sources images only from the same zone where it serves the transformation. Use an allowlist to control the origins where `/cdn-cgi/image/` transformation URLs can fetch source images.

Note

The allowlist applies only to `/cdn-cgi/image/` transformation URLs. It does not apply to the [Images binding](https://developers.cloudflare.com/images/optimization/binding/) or when a Worker uses `cf.image` on a `fetch()` subrequest.

## Configure allowed origins

Before you can specify an allowlist, you must [enable transformation URLs](https://developers.cloudflare.com/images/optimization/transformations/url/) for the zone or Worker that serves them.

Configure allowed origins at the same scope as the URL interface.

### Zone

Interface | Setting  
---|---  
Wrangler | Not available  
Cloudflare CLI | [`cf zones transformations-allowed-origins edit`](https://developers.cloudflare.com/images/optimization/transformations/url/#zone-cli)  
Dashboard | [**Images** > **Transformations** > **Sources**](https://developers.cloudflare.com/images/optimization/transformations/url/#zone-dashboard)  
REST API | [`transformations_allowed_origins`](https://developers.cloudflare.com/images/optimization/transformations/url/#zone-rest-api)  
  
### Worker

Interface | Setting  
---|---  
Wrangler | [`images.url_transformations.allowed_origins`](https://developers.cloudflare.com/images/optimization/transformations/url/#worker-wrangler-cli)  
Cloudflare CLI | [`worker.images.urlTransformations.allowedOrigins`](https://developers.cloudflare.com/images/optimization/transformations/url/#worker-wrangler-cli)  
Dashboard | Not available  
REST API | [`allowed_origins`](https://developers.cloudflare.com/images/optimization/transformations/url/#worker-rest-api)  
  
## How the allowlist works

Cloudflare rejects a transformation request when the source does not match the active allowlist.

The same hostname, wildcard, path, and redirect behaviors apply to both zone-scoped and Worker-scoped allowlists in production.

For zone-scoped transformations without an allowlist, Images accepts sources from any hostname in the same zone, including subdomains.

For custom domains routed to a Worker, the Worker's `allowed_origins` list replaces the zone-scoped allowlist handled by that Worker.

Worker allowlists

When configuring an allowlist for a Worker, explicitly include every hostname used for relative or same-host sources, including its `workers.dev` hostname and connected custom domains.

For example, consider a Worker that serves transformations from both:

  * `image-app.<YOUR_SUBDOMAIN>.workers.dev`
  * `images.example.com`



You must add both hostnames to the allowlist to use `/image.png` as a relative source from either hostname in production.

When developing locally, Images always accepts relative sources.

## Match hostnames and subdomains

Each hostname in an allowlist matches only that exact hostname unless you use a wildcard.

Allowed origin | Accepted source hostnames | Rejected source hostnames  
---|---|---  
`b.com` | `b.com` | `media.b.com`, `cdn.b.com`  
`media.b.com` | `media.b.com` | `b.com`, `cdn.b.com`  
`*.b.com` | `b.com`, `media.b.com`, `cdn.b.com` | `example.com`  
  
Add `*.` before a domain to match the domain and all of its subdomains.

## Match paths

You can restrict an allowed origin to a path. If you omit the path, then Images accepts source images from every path on that hostname.

Cloudflare matches the configured path against the beginning of the source path.

Allowed origin | Source URL | Result  
---|---|---  
`b.com/themes` | `https://b.com/themes/image.png` | Accepted  
`b.com/themes` | `https://b.com/themes/icons/image.png` | Accepted  
`b.com/themes` | `https://b.com/media/themes/image.png` | Rejected  
  
## Follow redirects

Cloudflare checks the initial source URL against the allowed origins. After accepting the initial URL, Images follows redirects and processes the resulting image even when they lead to an origin that is not allowed.

Only allow hostnames whose redirects you trust.

## Allow any origin

Caution

Allowing any origin lets third parties request transformations through the URL interface, which may cause unintended usage. Use this setting only when you expect arbitrary source hostnames.

To accept publicly available source images from any origin:

### Zone

  * **Cloudflare CLI:** Set the value to `"*"`:


    
    
    cf zones transformations-allowed-origins edit \
       --zone example.com \
       --value "*"

  * REST API: Send "value": "*" to the [`transformations_allowed_origins`](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_allowed_origins/) endpoint.
  * **Dashboard:** Select **Any origin** under **Sources**.



Changing a zone to accept any origin clears its allowlist.

### Worker

  * **Wrangler** : Set `allowed_origins = ["*"]`.
  * **Cloudflare CLI** : Set `allowedOrigins: ["*"]` in `cloudflare.config.ts`.
  * **REST API** : Set `allowed_origins` to `["*"]` in the Worker transformation settings request.



For Worker configuration, `"*"` must be the only entry in the list.

[PreviousTransform via URL](https://developers.cloudflare.com/images/optimization/transformations/url/)[NextCreate transformation flows](https://developers.cloudflare.com/images/optimization/transformations/flows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/transformations/sources.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
