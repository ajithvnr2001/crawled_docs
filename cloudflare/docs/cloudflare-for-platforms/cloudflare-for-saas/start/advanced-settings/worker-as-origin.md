---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/
title: Workers as your fallback origin \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-11-09T09:25:00.445713+00:00
---

# Workers as your fallback origin · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)Get started

  4. /Advanced Settings
  5. /Workers as your fallback origin



# Workers as your fallback origin

Last updated Nov 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow custom hostname traffic reaches your Worker When customers also use CloudflareSet up a Worker as your fallback originInteraction with custom origin serverRelated resources

If you are building your application on [Cloudflare Workers](https://developers.cloudflare.com/workers/), you can use a Worker as the origin for your SaaS zone (also known as your fallback origin).

## How custom hostname traffic reaches your Worker

When customers point their domains to your SaaS zone (for example, `mystore.customer.com` CNAMEs to `service.saasprovider.com`), their traffic enters your Cloudflare zone. Any Worker routes configured on your zone will match this incoming traffic.

For example, if you have:

  * Your SaaS zone: `saasprovider.com`
  * Your fallback origin: `service.saasprovider.com`
  * Customer's custom hostname: `mystore.customer.com` (pointed to your zone via CNAME)
  * Worker route: `*/*`



When a visitor requests `mystore.customer.com`, Cloudflare routes that request through your zone. The `*/*` route pattern matches all traffic entering your zone, including traffic from custom hostnames like `mystore.customer.com`.

Note

You do not need a separate Worker route for each custom hostname. The `*/*` route matches all traffic entering your zone, but a more specific route can override it.

### When customers also use Cloudflare

When a customer enables Cloudflare proxying on a CNAME record pointing to your SaaS hostname, Worker routes can match that target hostname.

For example, suppose `mystore.customer.com` points to `service.saasprovider.com`, with proxying enabled. Your SaaS zone has these routes:

Route | Worker  
---|---  
`*/*` | SaaS Worker  
`*.saasprovider.com/*` | None  
  
The more specific `*.saasprovider.com/*` route matches the target hostname, so these requests bypass your Worker. If your fallback origin has no origin server, requests can fail with a `522` error.

To send these requests to your Worker, add the route `service.saasprovider.com/*` and assign your SaaS Worker to it. Other hostnames covered by the exclusion will continue to bypass the Worker.

For more information, refer to [how customer DNS proxy settings affect Worker routing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/#o2o-behavior).

## Set up a Worker as your fallback origin

  1. In your SaaS zone, [create and set a fallback origin](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin). Ensure the fallback origin only has an [originless DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#originless-setups):

     * **Example** : `service.example.com AAAA 100::`
  2. In that same zone, navigate to **Workers Routes**.

  3. Click **Add route**.

  4. Configure a route to send traffic to your Worker. Choose one of the following options based on your needs:

     * **Route all traffic to the Worker** (recommended for most SaaS applications):

       * **Route** : `*/*`
       * **Worker** : Select the Worker used for your SaaS application.

This pattern routes all traffic entering your zone to the Worker, including requests from custom hostnames (for example, `mystore.customer.com`) and requests to your own subdomains (for example, `app.saasprovider.com`).

     * **Route all but specific routes to worker** :

       * **Route** : `*/*`
       * **Worker** : Select the Worker used for your SaaS application.
       * Add a second route for your zone's own hostnames with **Worker** set to **None** to exclude them.

For example, if your zone is `saasprovider.com` and you want `api.saasprovider.com` to bypass the Worker, create an additional route `api.saasprovider.com/*` with no Worker assigned. More specific routes take precedence over wildcard routes.

     * **Route only custom hostname traffic to the Worker** :

     * **Route** : `vanity.customer.com`

     * **Worker** : Select the Worker used for your SaaS application.

  5. Click **Save**.




* * *

Zone name restriction

Do not configure a custom hostname which matches the zone name. For example, if your SaaS zone is `example.com`, do not create a custom hostname named `example.com`.

## Interaction with custom origin server

Caution

When a Worker route matches incoming traffic, the request is handled by the Worker. The [`custom_origin_server`](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/) setting on individual custom hostnames is bypassed because the Worker processes the request before origin resolution occurs.

If you need per-hostname origin routing, implement it within your Worker using `request.headers.get("host")` or `request.cf.hostMetadata` (via [custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/)).

## Related resources

  * [Hostname routing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/) \- Route traffic with dispatch Workers and handle customers who also use Cloudflare.
  * [Workers routes](https://developers.cloudflare.com/workers/configuration/routing/routes/) \- Learn more about route pattern matching and validity rules.



[PreviousCustom origin server](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/)[NextCommon API Calls](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
