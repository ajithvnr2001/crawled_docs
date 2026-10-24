---
url: https://developers.cloudflare.com/changelog/post/2026-10-23-workers-builds-pin-npm-version/
title: Pin your npm version in Workers Builds with packageManager \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-24T07:00:53.594756+00:00
---

# Pin your npm version in Workers Builds with packageManager · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-23-workers-builds-pin-npm-version/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 23, 2026

## Pin your npm version in Workers Builds with packageManager

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now choose the npm version that [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) uses by setting the `packageManager` field in your `package.json`. Before the build installs dependencies, it installs the npm version you set, so a lockfile written by a newer npm version installs the same way in your build as it does locally.

package.jsonjson
    
    
    {
    	"packageManager": "npm@11.19.1"
    }

The `packageManager` field also sets the version of Yarn, pnpm, and Bun. Use an exact version, such as `npm@11.19.1`, not a range. Workers Builds does not use the `engines.npm` field to choose an npm version.

For more information, refer to [Package manager versions](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#package-manager-versions).
