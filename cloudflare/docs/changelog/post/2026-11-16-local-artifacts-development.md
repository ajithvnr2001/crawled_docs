---
url: https://developers.cloudflare.com/changelog/post/2026-11-16-local-artifacts-development/
title: Artifacts now supports local development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-17T10:23:32.363505+00:00
---

# Artifacts now supports local development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-16-local-artifacts-development/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 16, 2026

## Artifacts now supports local development

[Artifacts](https://developers.cloudflare.com/artifacts/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now develop and test [Artifacts](https://developers.cloudflare.com/artifacts/) locally. Create repos, import Git repositories over HTTPS, issue repo tokens, and clone or push with Git on your machine before deploying to Cloudflare's global network. Local repos are separate from your deployed repos, so you can test changes without affecting production data.

Local repos also emit the same [Artifacts events](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/) as production when a repo is created, imported, forked, or deleted, or when a repo token is created or revoked. This lets you test the Workflows that react to them before you deploy.

To use local repos when you run your Worker locally, add an Artifacts binding to your Wrangler configuration file:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "artifacts-worker",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-11-17",
      "artifacts": [
        {
          "binding": "ARTIFACTS",
          "namespace": "default"
        }
      ]
    }
    
    
    name = "artifacts-worker"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-11-17"
    
    [[artifacts]]
    binding = "ARTIFACTS"
    namespace = "default"

Run `npx wrangler dev`, then use the binding the same way you would in production:
    
    
    const created = await env.ARTIFACTS.create("starter-repo");
    
    return Response.json({
    	remote: created.remote,
    	token: created.token,
    });
    
    
    const created = await env.ARTIFACTS.create("starter-repo");
    
    return Response.json({
    	remote: created.remote,
    	token: created.token,
    });

The returned `remote` points to your local dev session, so you can use it with a standard Git client to clone and push.

Local development requires the latest version of Wrangler and Git 2.32 or later on your `PATH`.

When you develop with `npx wrangler dev`, the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), or the [Workers Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/), Artifacts bindings use the local simulator by default. To use your deployed repos instead, set `remote = true` on the binding.

To learn more, refer to [Local development](https://developers.cloudflare.com/artifacts/guides/local-development/).
