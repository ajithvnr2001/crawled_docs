---
url: https://developers.cloudflare.com/changelog/post/2026-11-02-module-registry-default/
title: Workers will use the new module registry by default on November 17 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.567583+00:00
---

# Workers will use the new module registry by default on November 17 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-02-module-registry-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 2, 2026

## Workers will use the new module registry by default on November 17

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting November 17, 2026, JavaScript Workers with a [compatibility date](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) of `2026-11-17` or later will use the new module registry by default. You will no longer need the `new_module_registry` flag for these dates. Python Workers keep using the legacy registry.

The module registry finds and loads JavaScript modules in your Worker. We [announced the new registry in September 2026 ↗︎](https://blog.cloudflare.com/workers-module-registry-nodejs/). It improves compatibility with JavaScript standards and Node.js. In Workers using [Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/), you can use `require()` to load ES modules. The module and its dependencies must not use top-level `await`.

You can also use `import.meta` to get information about the current module and find the URL of another module without loading it:

src/index.jsjs
    
    
    export default {
    	fetch() {
    		return Response.json({
    			moduleUrl: import.meta.url,
    			isEntrypoint: import.meta.main,
    			helperUrl: import.meta.resolve("./helper.js"),
    		});
    	},
    };

src/index.tsts
    
    
    export default {
    	fetch(): Response {
    		return Response.json({
    			moduleUrl: import.meta.url,
    			isEntrypoint: import.meta.main,
    			helperUrl: import.meta.resolve("./helper.js"),
    		});
    	},
    } satisfies ExportedHandler;

When deployed with `src/index.ts` as the unbundled entrypoint, `isEntrypoint` is `true`. `helperUrl` is a URL within your Worker bundle. Resolving the URL does not check whether the module exists or load it over the network. Build tools may transform `import.meta`. To try this example directly, refer to [unbundled deployments](https://developers.cloudflare.com/workers/wrangler/configuration/#bundling).

Existing Workers keep their current behavior until you change their compatibility date or flags. To try the new registry before November 17, keep your current date and add `new_module_registry` to your [compatibility flags](https://developers.cloudflare.com/workers/configuration/compatibility-flags/).

Before updating, check your dependencies for invalid import attributes and changes to `require()` behavior. The new registry rejects invalid import attributes. Calls to `require()` also fail if the module or any of its dependencies use top-level `await`. To keep the legacy registry with a compatibility date of `2026-11-17` or later, add `legacy_module_registry`.

For migration details, refer to the [new module registry compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#new-module-registry), [bundling documentation](https://developers.cloudflare.com/workers/wrangler/bundling/#runtime-module-loading), and [Node.js compatibility documentation](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).
