---
url: https://developers.cloudflare.com/pages/configuration/build-caching/
title: Build caching \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:32.485230+00:00
---

# Build caching · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/build-caching/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Build caching



# Build caching

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAbout build cache Requirements Package managers Frameworks LimitsEnable build cacheClear build cache

Improve Pages build times by caching dependencies and build output between builds with a project-wide shared cache. For build caching on Cloudflare Workers, refer to [Workers Builds build caching](https://developers.cloudflare.com/workers/ci-cd/builds/build-caching/).

The first build to occur after enabling build caching on your Pages project will save to cache. Every subsequent build will restore from cache unless configured otherwise.

## About build cache

When enabled, the build cache will automatically detect and cache data from each build. Refer to [Frameworks](https://developers.cloudflare.com/pages/configuration/build-caching/#frameworks) to review what directories are automatically saved and restored from the build cache.

### Requirements

Build caching requires the V2 or [V3 build system](https://developers.cloudflare.com/pages/configuration/build-image/#v3-build-system). To upgrade from V2 to V3, refer to the [v2 to v3 migration instructions](https://developers.cloudflare.com/pages/configuration/build-image/#v2-to-v3-migration).

### Package managers

Pages will cache the global cache directories of the following package managers:

Package Manager | Directories cached  
---|---  
[npm ↗︎](https://www.npmjs.com/) | `.npm`  
[yarn ↗︎](https://yarnpkg.com/) | `.cache/yarn`  
[pnpm ↗︎](https://pnpm.io/) | `.pnpm-store`, `.local/share/pnpm/store`  
[bun ↗︎](https://bun.sh/) | `.bun/install/cache`  
  
### Frameworks

Some frameworks provide a cache directory that is typically populated by the framework with intermediate build outputs or dependencies during build time. Pages will automatically detect the framework you are using and cache this directory for reuse in subsequent builds.

The following frameworks support build output caching:

Framework | Directories cached  
---|---  
Astro | `node_modules/.astro`  
Docusaurus | `node_modules/.cache`, `.docusaurus`, `build`  
Eleventy | `.cache`  
Gatsby | `.cache`, `public`  
Hugo | `.cache`  
Next.js | `.next/cache`  
Nuxt | `node_modules/.cache/nuxt`  
SvelteKit | `node_modules/.cache/imagetools`  
  
Hugo build caching

Hugo does not use `.cache` by default. To use build caching with Hugo, set `--cacheDir=$PWD/.cache` in your build command. For example:
    
    
    hugo --minify --cacheDir=$PWD/.cache

Pages detects Hugo projects via the presence of a `hugo.toml`, `hugo.yaml`, `hugo.yml`, or `hugo.json` config file.

### Limits

The following limits are imposed for build caching:

  * **Retention** : Cache is purged seven days after its last read date. Unread cache artifacts are purged seven days after creation.
  * **Storage** : Every project is allocated 10 GB. If the project cache exceeds this limit, the project will automatically start deleting artifacts that were read least recently.



## Enable build cache

To enable build caching:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Go to **Settings** > **Build** > **Build cache**.

  4. Select **Enable** to turn on build caching.




## Clear build cache

The build cache can be cleared for a project if needed, such as when debugging build issues. To clear the build cache:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Go to **Settings** > **Build** > **Build cache**.

  4. Select **Clear Cache** to clear the build cache.




[PreviousBranch deployment controls](https://developers.cloudflare.com/pages/configuration/branch-build-controls/)[NextBuild configuration](https://developers.cloudflare.com/pages/configuration/build-configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/build-caching.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
