---
url: https://developers.cloudflare.com/pages/configuration/build-watch-paths/
title: Build watch paths \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:32.285274+00:00
---

# Build watch paths · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/build-watch-paths/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Build watch paths



# Build watch paths

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure pathsExamples Trigger builds for specific directories (monorepo) Exclude a directory from triggering builds Trigger builds for a specific filetype Trigger builds for a directory but exclude a subdirectory

When you connect a Git repository to Pages, by default a change to any file in the repository triggers a Pages build. You can configure Pages to include or exclude specific paths to skip builds for unrelated changes. This is useful in a monorepo project structure to limit unnecessary builds. For build watch paths on Cloudflare Workers, refer to [Workers Builds build watch paths](https://developers.cloudflare.com/workers/ci-cd/builds/build-watch-paths/).

## Configure paths

To configure which paths are included and excluded:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Go to **Settings** > **Build** > **Build watch paths**. Pages defaults to including all paths (`[*]`) and excluding none (`[]`).




The configuration fields can be filled in two ways:

  * **Static filepaths** : Enter the precise name of the file you are looking to include or exclude (for example, `docs/README.md`).
  * **Wildcard syntax:** Use wildcards to match multiple paths. You can specify wildcards at the start or end of your rule.



Wildcard syntax

A wildcard (`*`) matches zero or more characters, **including path separators (`/`)**. This means a single `*` at the end of a path pattern will match files in nested subdirectories as well. For example:

  * `docs/*` matches `docs/README.md`, `docs/guides/setup.md`, and `docs/guides/advanced/config.md`.
  * `*.md` matches `README.md`, `docs/README.md`, and `src/content/guide.md`.
  * `*` alone matches all files in the repository.



For each path in a push event, build watch paths will be evaluated as follows:

  * Paths satisfying excludes conditions are ignored first
  * Any remaining paths are checked against includes conditions
  * If any matching path is found, a build is triggered. Otherwise the build is skipped



Pages will bypass the path matching for a push event and default to building the project if:

  * A push event contains 0 file changes, in case a user pushes an empty push event to trigger a build
  * A push event contains 3000+ file changes or 20+ commits



## Examples

### Trigger builds for specific directories (monorepo)

To trigger a build only when files change within specific directories, such as `project-a/` and `packages/`, use the following rules. Because `*` matches across path separators, this includes changes in nested subdirectories like `project-a/src/index.js` or `packages/utils/lib/helpers.ts`:

  * Include paths: `project-a/*`, `packages/*`
  * Exclude paths: _(leave empty)_



### Exclude a directory from triggering builds

To trigger a build for any changes except those in a specific directory, such as `docs/` (including nested paths like `docs/guides/setup.md`), use the following rules:

  * Include paths: `*`
  * Exclude paths: `docs/*`



### Trigger builds for a specific filetype

To trigger a build only when a specific file or filetype changes, such as any `.md` file in the repository, use the following rules:

  * Include paths: `*.md`
  * Exclude paths: _(leave empty)_



### Trigger builds for a directory but exclude a subdirectory

To trigger a build for changes in `src/` while ignoring changes in `src/tests/`, use the following rules:

  * Include paths: `src/*`
  * Exclude paths: `src/tests/*`



[PreviousBuild image](https://developers.cloudflare.com/pages/configuration/build-image/)[NextCustom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/build-watch-paths.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
