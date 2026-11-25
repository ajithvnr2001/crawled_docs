---
url: https://developers.cloudflare.com/kv/concepts/kv-namespaces/
title: KV namespaces \u00b7 Cloudflare Workers KV docs
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:50.378565+00:00
---

# KV namespaces · Cloudflare Workers KV docs

> Source: https://developers.cloudflare.com/kv/concepts/kv-namespaces/

  1. [Home](https://developers.cloudflare.com/)
  2. /[KV](https://developers.cloudflare.com/kv/)
  3. /Key concepts
  4. /KV namespaces



# KV namespaces

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewJurisdictionsBind your KV namespace in configurationBind your KV namespace via the dashboard

A KV namespace is a key-value database replicated to Cloudflare’s global network.

Bind your KV namespaces in your Worker configuration file or via the Cloudflare dashboard.

Note

KV namespace IDs are public and bound to your account.

## Jurisdictions

Namespaces can optionally be restricted to a jurisdiction to durably store data only within a specific region. Refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/) for more information.

## Bind your KV namespace in configuration

The following content appears twice: first for the Cloudflare CLI (`cf`), then for Wrangler. Use `cf` for new projects. In an existing project, use the CLI that the project already uses.

Cloudflare CLI

To bind KV namespaces to your Worker in [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), add a property to `worker.env` using `bindings.kv()`. The property key is the binding name used to refer to the KV namespace in your Worker:

  * `id` `string` required

    * The ID of the KV namespace.
  * `dev` `object` optional

    * Local development options. Set `dev: { remote: true }` to connect to the remote KV namespace during `cf dev`.



`cloudflare.config.ts` does not have a `preview_id` field. During `cf dev`, bindings use local storage by default unless you set `dev: { remote: true }`. To use a different namespace `id` for [Worker Previews](https://developers.cloudflare.com/cf/projects/#deploy-a-preview) or modes, pass a function to `defineConfig(({ mode, isPreview }) => ...)`.

Example:

cloudflare.config.tsts
    
    
    import { bindings, defineConfig } from "cf/config";
    import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };
    
    export default defineConfig({
    	worker: {
    		name: "my-worker",
    		entrypoint,
    		compatibilityDate: "<COMPATIBILITY_DATE>",
    		env: {
    			TEST_NAMESPACE: bindings.kv({ id: "<TEST_ID>" }),
    		},
    	},
    });

Wrangler

To bind KV namespaces to your Worker in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/), assign an array of objects with the following properties to the `kv_namespaces` key:

  * `binding` `string` required

    * The binding name used to refer to the KV namespace.
  * `id` `string` required

    * The ID of the KV namespace.
  * `preview_id` `string` optional

    * The ID of the KV namespace used during `wrangler dev`.



Example:
    
    
    {
    	"kv_namespaces": [
    		{
    			"binding": "<TEST_NAMESPACE>",
    			"id": "<TEST_ID>"
    		}
    	]
    }
    
    
    [[kv_namespaces]]
    binding = "<TEST_NAMESPACE>"
    id = "<TEST_ID>"

## Bind your KV namespace via the dashboard

To bind the namespace to your Worker in the Cloudflare dashboard:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your **Worker**.

  3. Select **Settings** > **Bindings**.

  4. Select **Add**.

  5. Select **KV Namespace**.

  6. Enter your desired variable name (the name of the binding).

  7. Select the KV namespace you wish to bind the Worker to.

  8. Select **Deploy**.




[PreviousKV bindings](https://developers.cloudflare.com/kv/concepts/kv-bindings/)[NextRead key-value pairs](https://developers.cloudflare.com/kv/api/read-key-value-pairs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/kv/concepts/kv-namespaces.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
