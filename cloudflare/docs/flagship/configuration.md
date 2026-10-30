---
url: https://developers.cloudflare.com/flagship/configuration/
title: Configuration \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:31.630131+00:00
---

# Configuration · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /Configuration



# Configuration

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd the bindingBind to multiple appsGenerate typesUse the bindingLocal development Copy flags from your remote app Manage the local store Use the remote app instead Use the cf CLI

To use Flagship in a Cloudflare Worker, add a Flagship binding to your Wrangler configuration file. The binding gives your Worker access to `env.FLAGS`, which provides methods to evaluate feature flags.

## Add the binding

Add the `flagship` block to your Wrangler configuration file with a binding name and your app ID.
    
    
    {
    	"flagship": [
    		{
    			"binding": "FLAGS",
    			"app_id": "<APP_ID>",
    		},
    	],
    }
    
    
    [[flagship]]
    binding = "FLAGS"
    app_id = "<APP_ID>"

Replace `<APP_ID>` with the app ID from your Flagship app. If you have not created an app yet, refer to the [Get started guide](https://developers.cloudflare.com/flagship/get-started/#create-an-app-and-a-flag). The `binding` field sets the name you use to access Flagship in your Worker code (for example, `env.FLAGS`).

## Bind to multiple apps

A single Worker can bind to multiple Flagship apps. Use the array form to define more than one binding:
    
    
    {
    	"flagship": [
    		{
    			"binding": "FLAGS",
    			"app_id": "<APP_ID_1>",
    		},
    		{
    			"binding": "EXPERIMENT_FLAGS",
    			"app_id": "<APP_ID_2>",
    		},
    	],
    }
    
    
    [[flagship]]
    binding = "FLAGS"
    app_id = "<APP_ID_1>"
    
    [[flagship]]
    binding = "EXPERIMENT_FLAGS"
    app_id = "<APP_ID_2>"

Each binding is available as a separate property on the `env` object (for example, `env.FLAGS` and `env.EXPERIMENT_FLAGS`).

## Generate types

After adding the binding, run `npx wrangler types` to generate TypeScript types. This creates the `Env` interface with each binding typed as `Flagship`.
    
    
    interface Env {
    	FLAGS: Flagship;
    	EXPERIMENT_FLAGS: Flagship;
    }

## Use the binding

Call evaluation methods on `env.FLAGS` to resolve flag values at runtime. Each method accepts a flag key, a default value, and an optional evaluation context.
    
    
    export default {
    	async fetch(request, env) {
    		const isEnabled = await env.FLAGS.getBooleanValue("my-feature", false, {
    			userId: "user-42",
    		});
    
    		return new Response(isEnabled ? "Feature is on" : "Feature is off");
    	},
    };
    
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const isEnabled = await env.FLAGS.getBooleanValue("my-feature", false, {
    			userId: "user-42",
    		});
    
    		return new Response(isEnabled ? "Feature is on" : "Feature is off");
    	},
    };

Refer to the [binding API reference](https://developers.cloudflare.com/flagship/binding/) for the full list of methods.

## Local development

During local development, Flagship bindings use a local flag store by default. This applies to [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev), the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), the [Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/), and [`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development). The store starts empty, so evaluations return the default value you pass at the call site until you add flags.

This is the default behavior in Wrangler v4.135.0 and later, and in `@cloudflare/vite-plugin` v1.56.0 and later.

### Copy flags from your remote app

To copy flags from your remote app into the local store:
    
    
    npx wrangler flagship flags pull <APP_ID>

`pull` also seeds the account tag used for [percentage rollout](https://developers.cloudflare.com/flagship/targeting/percentage-rollouts/) bucketing, so local buckets match the remote app. Flags that exist only in the local store are left untouched.

Flags are not pulled automatically, so `wrangler dev` works offline and never overwrites flags you changed locally.

`pull` writes to the default local store in `.wrangler/state`. If your dev server keeps its data in a different directory, pass `--persist-to <DIRECTORY>` so that `pull` writes to the same place. For example, the Cloudflare Vite plugin 2.0 beta keeps its data in `.cloudflare/state`:
    
    
    npx wrangler flagship flags pull <APP_ID> --persist-to .cloudflare/state

### Manage the local store

To create or change flags without affecting the remote app, pass `--local` to the flag commands:
    
    
    npx wrangler flagship flags create <APP_ID> new-checkout --local
    npx wrangler flagship flags list <APP_ID> --local

Flag commands still default to the remote app. You cannot pass `--local` and `--remote` together.

You can also inspect and edit the local store in [Local Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/). Flagship apps appear in Local Explorer in Wrangler v4.148.0 and later, and in `@cloudflare/vite-plugin` v1.63.0 and later.

### Use the remote app instead

To evaluate against the remote app during local development, set `remote` to `true` on the binding:
    
    
    {
    	"flagship": [
    		{
    			"binding": "FLAGS",
    			"app_id": "<APP_ID>",
    			"remote": true,
    		},
    	],
    }
    
    
    [[flagship]]
    binding = "FLAGS"
    app_id = "<APP_ID>"
    remote = true

### Use the cf CLI

[`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development) uses the local flag store, the same as `wrangler dev`.

To manage local flags with `cf`, add `--local` to a supported `cf flagship` command. No dev server needs to be running, and the app does not need to be bound to a Worker.
    
    
    cf flagship apps flags list --app-id <APP_ID> --local
    cf flagship apps flags get <FLAG_KEY> --app-id <APP_ID> --local

These commands support `--local`:

  * `cf flagship apps list`
  * `cf flagship apps flags list`, `get`, `create`, `update`, `patch`, `delete`, and `evaluate`
  * `cf flagship apps evaluate get`



Other `cf flagship` commands, such as `cf flagship apps get`, `cf flagship apps definitions get`, and `cf flagship apps flags changelog`, fail with `This command has no local equivalent.` Run them without `--local` to use the remote app.

By default, `cf` keeps [local data in its own directory](https://developers.cloudflare.com/cf/projects/#local-resource-data), which `wrangler dev` and the Cloudflare Vite plugin do not read. To work on the same flags as your dev server, pass its data directory. This is `.wrangler/state` for `wrangler dev` and the Cloudflare Vite plugin 1.x, and `.cloudflare/state` for the Vite plugin 2.0 beta:
    
    
    cf flagship apps flags list --app-id <APP_ID> --local --persist-to .wrangler/state

`cf` cannot copy flags from your remote app. Use `npx wrangler flagship flags pull <APP_ID>` instead, with the same `--persist-to` value if you set one.

[PreviousAPI tokens](https://developers.cloudflare.com/flagship/api-tokens/)[NextBest practices](https://developers.cloudflare.com/flagship/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
