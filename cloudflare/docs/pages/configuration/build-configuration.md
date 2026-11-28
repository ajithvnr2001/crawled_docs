---
url: https://developers.cloudflare.com/pages/configuration/build-configuration/
title: Build configuration \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:32.524976+00:00
---

# Build configuration · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/build-configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Build configuration



# Build configuration

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBuild commands and directoriesFramework presetsEnvironment variables

You can configure how Cloudflare Pages builds your site and where its output files are located. For build configuration on Cloudflare Workers, refer to [Workers Builds configuration](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/).

## Build commands and directories

Provide a build command to tell Cloudflare Pages how to build your application. For projects not listed in the presets table, refer to your framework's documentation.

The build output directory indicates where your project's build command outputs the built version of your Cloudflare Pages site. Often, this defaults to `dist` or `public`, but you can customize it.

Understanding your build configuration

The build command is provided by your framework. For example, a Vite project uses `npm run build` as its build command. When you are working without a framework and do not need a build step, leave the **Build command** field blank. Pages determines whether a build has succeeded or failed by reading the exit code returned from the user-supplied build command. Any non-zero return code causes a build to fail. An exit code of `0` marks the Pages build as successful and uploads assets regardless of whether logs are written to standard error.

The build output directory is generated from the build command. Each framework has its own naming convention. For example, the build output directory is `dist` or `public` for many frameworks.

The root directory is where your site's content lives. If not specified, Cloudflare assumes that your linked Git repository is the root directory. Specify the root directory for cases like monorepos, where multiple projects live in one repository.

## Framework presets

Cloudflare maintains a list of build configurations for popular frameworks and tools. These are accessible during project creation. The following table lists the standard build commands and output directories for each preset.

If you are not using a preset and do not need a build step, leave the **Build command** field blank (or use `exit 0` if your workflow requires a non-empty command).

Framework/tool| Build command| Build directory  
---|---|---  
React (Vite)| `npm run build`| `dist`  
Gatsby| `npx gatsby build`| `public`  
Next.js (Static HTML Export)| `npx next build`| `out`  
Nuxt.js| `npm run build`| `dist`  
Qwik| `npm run build`| `dist`  
Remix| `npm run build`| `build/client`  
Svelte| `npm run build`| `public`  
SvelteKit| `npm run build`| `.svelte-kit/cloudflare`  
Vue| `npm run build`| `dist`  
Analog| `npm run build`| `dist/analog/public`  
Astro| `npm run build`| `dist`  
Angular| `npm run build`| `dist/cloudflare`  
Brunch| `npx brunch build --production`| `public`  
Docusaurus| `npm run build`| `build`  
Elder.js| `npm run build`| `public`  
Eleventy| `npx @11ty/eleventy`| `_site`  
Ember.js| `npx ember-cli build`| `dist`  
GitBook| `npx gitbook-cli build`| `_book`  
Gridsome| `npx gridsome build`| `dist`  
Hugo| `hugo`| `public`  
Jekyll| `jekyll build`| `_site`  
MkDocs| `mkdocs build`| `site`  
Pelican| `pelican content`| `output`  
React Static| `react-static build`| `dist`  
Slate| `./deploy.sh`| `build`  
Umi| `npx umi build`| `dist`  
VitePress| `npx vitepress build`| `.vitepress/dist`  
Zola| `zola build`| `public`  
  
## Environment variables

If your project uses environment variables during builds, you can configure them in the Cloudflare dashboard:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Select **Settings** > **Variables and Secrets**.




Note

Environment variables configured under **Settings** > **Variables and Secrets** are available at build time and at runtime for Pages Functions. Changes take effect on the next deployment.

The following system environment variables are injected by default (but can be overridden):

Environment Variable | Injected value | Example use-case  
---|---|---  
`CI` | `true` | Changing build behaviour when run on CI versus locally  
`CF_PAGES` | `1` | Changing build behaviour when run on Pages versus locally  
`CF_PAGES_COMMIT_SHA` | `<sha1-hash-of-current-commit>` | Passing current commit ID to error reporting, for example, Sentry  
`CF_PAGES_BRANCH` | `<branch-name-of-current-deployment>` | Customizing build based on branch, for example, disabling debug logging on `production`  
`CF_PAGES_URL` | `<url-of-current-deployment>` | Allowing build tools to know the URL the page will be deployed at  
  
[PreviousBuild caching](https://developers.cloudflare.com/pages/configuration/build-caching/)[NextBuild image](https://developers.cloudflare.com/pages/configuration/build-image/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/build-configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
