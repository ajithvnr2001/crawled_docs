---
url: https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/tanstack-start/
title: Migrate TanStack Start from Vercel to Cloudflare Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:45.286868+00:00
---

# Migrate TanStack Start from Vercel to Cloudflare Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/tanstack-start/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Static Assets](https://developers.cloudflare.com/workers/static-assets/)Migration Guides

  4. /[Migrate from Vercel to Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/)
  5. /TanStack Start



# Migrate TanStack Start from Vercel to Cloudflare Workers

Last updated Nov 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginMigrate with a coding agentMigrate manuallyKnown issuesRelated resources

This guide moves a [TanStack Start ↗︎](https://tanstack.com/start) application from Vercel to Cloudflare Workers. On Vercel, TanStack Start runs through the Nitro Vite plugin. On Workers, the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) replaces it.

Server functions, server routes, and client-only routes work without code changes.

## Before you begin

  * Your project must use `@tanstack/react-start` 1.132.0 or later. Earlier versions do not export `@tanstack/react-start/server-entry`. Upgrade all `@tanstack/*` packages to the same version.
  * Your project must build with Vite. Projects built with Rsbuild are not supported.
  * Review the steps in [Before you begin](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/#before-you-begin) that apply to every framework.



## Migrate with a coding agent

Copy this prompt into your coding agent. The agent stops before it deploys.
    
    
    Migrate this TanStack Start app from Vercel to Cloudflare Workers (Workers with Static Assets, not Pages).
    
    0. Work on a new git branch. Install dependencies exactly as locked with the repository's package manager (<pm>).
       - If <pm> rejects the lockfile format (for example, pnpm 10 or later with lockfileVersion '6.0'), convert the lockfile with an older major version, such as `npx pnpm@9 install --lockfile-only`. Do not re-resolve dependencies. Commit the conversion separately.
       - With pnpm 10 or later, add `allowBuilds: { esbuild: true, workerd: true }` to pnpm-workspace.yaml. Never run the interactive `pnpm approve-builds`.
    1. Confirm that vite.config.ts uses tanstackStart() from @tanstack/react-start/plugin/vite. If the project uses Rsbuild, stop and tell me. Confirm that @tanstack/react-start is 1.132.0 or later. If it is older, stop and propose upgrading all @tanstack/* packages together.
    2. Remove Vercel configuration:
       - Port redirects and headers from vercel.json, then delete vercel.json and .vercel/.
       - Uninstall the `nitro` package. Remove the nitro() plugin and its import from vite.config.ts.
       - List runtime @vercel/* usage (kv, blob, postgres, og, edge-config, analytics). Propose Cloudflare equivalents, but do not rewrite them without asking me.
    3. Install @cloudflare/vite-plugin and wrangler as dev dependencies.
    4. In vite.config.ts, add cloudflare({ viteEnvironment: { name: "ssr" } }) as the first plugin. Keep tanstackStart() before the React plugin. Keep all other plugins in their existing order.
    5. Create wrangler.jsonc with "$schema": "node_modules/wrangler/config-schema.json", "name": "<repository name, lowercase, hyphens>", "main": "@tanstack/react-start/server-entry", "compatibility_date": "<today>", and "observability": { "enabled": true }. Do not set "assets". Do not add nodejs_compat. A compatibility date of 2026-08-04 or later already enables it. If package.json "name" differs from the repository name, use the repository name and tell me.
    6. Keep the existing dev and build scripts and their flags. Add preview="vite preview", deploy="<pm> run build && wrangler deploy", and cf-typegen="wrangler types". Remove scripts that start a Node.js server, such as `node .output/server/index.mjs`. Add .wrangler/ and .dev.vars* to .gitignore.
    7. Create public/_headers so hashed assets keep a one-year cache:
       /assets/*
         Cache-Control: public, max-age=31536000, immutable
    8. Read bindings and secrets in server functions and routes with `import { env } from "cloudflare:workers"`. Run cf-typegen and make sure tsconfig.json includes worker-configuration.d.ts. If vercel.json had crons, create src/server.ts that exports { fetch: handler.fetch, scheduled }, with handler imported from "@tanstack/react-start/server-entry". Point "main" at src/server.ts and add triggers.crons.
    9. If tanstackStart({ prerender }) is turned on, build and confirm that prerendering still works.
    10. Search server code for Node.js-only APIs: file system writes, child_process, and native modules such as sharp, canvas, or bcrypt. These fail on Workers and in `vite dev`. List them and propose KV, D1, or R2. Do not rewrite data layers without asking me.
    11. Run `<pm> run build`, then `<pm> run preview --port <free port> --strictPort`. Request every route, API route, and one server function with curl. Compare the results with the live Vercel site. If vitest uses vite.config.ts, tell me that it now loads the Cloudflare plugin.
    
    Rules: use only non-interactive commands; store local secrets in a gitignored .dev.vars file with placeholder values; never print secret values; do not deploy, log in, or change DNS.
    When you finish, list the files you changed, the Vercel features without an equivalent, the secrets I must set with `npx wrangler secret put <NAME>`, and the deploy command.

## Migrate manually

  1. Remove the Nitro package and install the Cloudflare Vite plugin and Wrangler:

npmyarnpnpmbun
         
         npm uninstall nitro
         
         yarn remove nitro
         
         pnpm remove nitro
         
         bun remove nitro

npmyarnpnpmbun
         
         npm i -D @cloudflare/vite-plugin wrangler
         
         yarn add -D @cloudflare/vite-plugin wrangler
         
         pnpm add -D @cloudflare/vite-plugin wrangler
         
         bun add -d @cloudflare/vite-plugin wrangler

  2. In `vite.config.ts`, remove `nitro()` and its import. Add the Cloudflare plugin as the first plugin:

vite.config.tsts
         
         import { defineConfig } from "vite";
         import { cloudflare } from "@cloudflare/vite-plugin";
         import { tanstackStart } from "@tanstack/react-start/plugin/vite";
         import viteReact from "@vitejs/plugin-react";
         
         export default defineConfig({
         	plugins: [
         		cloudflare({ viteEnvironment: { name: "ssr" } }),
         		tanstackStart(),
         		viteReact(),
         	],
         });

  3. Create a Wrangler configuration file. Do not set `assets`, because the Cloudflare Vite plugin generates it.
         
         {
         	"$schema": "node_modules/wrangler/config-schema.json",
         	"name": "<YOUR_PROJECT_NAME>",
         	"main": "@tanstack/react-start/server-entry",
         	// Set this to today's date
         	"compatibility_date": "2026-11-06",
         	"observability": {
         		"enabled": true,
         	},
         }
         
         "$schema" = "node_modules/wrangler/config-schema.json"
         name = "<YOUR_PROJECT_NAME>"
         main = "@tanstack/react-start/server-entry"
         # Set this to today's date
         compatibility_date = "2026-11-06"
         
         [observability]
         enabled = true

  4. Add a `public/_headers` file so hashed assets keep a one-year cache:

public/_headerstxt
         
         /assets/*
           Cache-Control: public, max-age=31536000, immutable

  5. Add these scripts to `package.json`:

package.jsonjson
         
         {
         	"scripts": {
         		"preview": "vite preview",
         		"deploy": "npm run build && wrangler deploy",
         		"cf-typegen": "wrangler types"
         	}
         }

Remove any script that starts a Node.js server, such as `node .output/server/index.mjs`.

  6. Generate types for your bindings:

npmyarnpnpm
         
         npm run cf-typegen
         
         yarn run cf-typegen
         
         pnpm run cf-typegen

Read bindings in server functions and routes with `import { env } from "cloudflare:workers"`.

  7. Build and preview your application locally. The preview runs in the Workers runtime.

npmyarnpnpm
         
         npm run build
         
         yarn run build
         
         pnpm run build

npmyarnpnpm
         
         npm run preview
         
         yarn run preview
         
         pnpm run preview

  8. Delete `vercel.json` and deploy your application:

npmyarnpnpm
         
         npm run deploy
         
         yarn run deploy
         
         pnpm run deploy




To add [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/), [Queues](https://developers.cloudflare.com/queues/), or [Durable Objects](https://developers.cloudflare.com/durable-objects/), create a custom server entrypoint. For more information, refer to [Custom entrypoints](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/#custom-entrypoints).

## Known issues

  * **Assets are not cached.** Without `public/_headers`, Workers serves files in `/assets/` with `max-age=0, must-revalidate`.
  * **The server function format changes after a lockfile re-resolve.** Re-resolving dependencies can upgrade `seroval`, which changes the server function wire format. Convert old lockfiles instead.
  * **File system writes fail.** Runtime writes to the file system fail on Workers. They also fail in `vite dev`, which now runs in the Workers runtime. Use [KV](https://developers.cloudflare.com/kv/), [D1](https://developers.cloudflare.com/d1/), or [R2](https://developers.cloudflare.com/r2/) instead.
  * **Automatic configuration leaves the`nitro` package installed.** `wrangler setup` removes the `nitro()` plugin call but not the package.
  * **Vitest fails with`module is not defined`.** Vitest loads `vite.config.ts`, which now includes the Cloudflare plugin. Give Vitest its own configuration file.



## Related resources

  * [TanStack Start framework guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/)
  * [Migrate from Vercel to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/)
  * [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/)



[PreviousSvelteKit](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/sveltekit/)[NextStatic site or SPA](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/static-site/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/migration-guides/vercel-to-workers/tanstack-start.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
