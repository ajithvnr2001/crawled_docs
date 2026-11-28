---
url: https://developers.cloudflare.com/pages/configuration/monorepos/
title: Monorepos \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:31.928363+00:00
---

# Monorepos · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/monorepos/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Monorepos



# Monorepos

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet upBuildsGit integration GitHub check runs and GitLab commit statusesMonorepo management toolsLimitations

While some apps are built from a single repository, Pages also supports apps with more complex setups. A monorepo is a repository that has multiple subdirectories each containing its own application. For monorepos on Cloudflare Workers, refer to [Workers Builds monorepos](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#monorepos).

## Set up

You can create multiple projects using the same repository, [in the same way that you would create any other Pages project](https://developers.cloudflare.com/pages/get-started/git-integration/). You have the option to vary the build command and/or root directory of your project to tell Pages where you would like your build command to run. All project names must be unique even if connected to the same repository.

## Builds

When you connect a Git repository to Pages, by default a change to any file in the repository triggers a Pages build.

![Monorepo example diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3600,height=828,format=webp/_astro/pages-path.D3Q_3sei.png)

Take for example `my-monorepo` with two associated Pages projects (`marketing-app` and `ecommerce-app`) and their listed dependencies. By default, if you change a file in the project directory for `marketing-app`, then a build for the `ecommerce-app` project is also triggered, even though `ecommerce-app` and its dependencies have not changed. To avoid duplicate builds, include and exclude both [build watch paths](https://developers.cloudflare.com/pages/configuration/build-watch-paths/) and [branches](https://developers.cloudflare.com/pages/configuration/branch-build-controls/) to specify when Pages should skip a build for a given project.

## Git integration

Once you have created a separate Pages project for each of the projects within your Git repository, each Git push will issue a new build and deployment for all connected projects unless specified in your build configuration.

GitHub will display separate comments for each project with the updated project and deployment URL if there is a Pull Request associated with the branch.

### GitHub check runs and GitLab commit statuses

If you have multiple projects associated with your repository, your [GitHub check run ↗︎](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks#checks) or [GitLab commit status ↗︎](https://docs.gitlab.com/user/project/merge_requests/status_checks/) will appear like the following on your repository:

![GitHub check run](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1020,height=316,format=webp/_astro/ghcheckrun.Cv3SMhfT.png)![GitLab commit status](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=584,height=176,format=webp/_astro/glcommitstatus.BXV17OMM.png)

If a build skips for any reason (for example, CI Skip, build watch paths, or branch deployment controls), the check run or commit status does not appear.

## Monorepo management tools

While Pages does not provide specialized tooling for dependency management in monorepos, you can bring additional tooling to help manage your repository. For simple subpackage management, use tools like [npm ↗︎](https://docs.npmjs.com/cli/using-npm/workspaces), [pnpm ↗︎](https://pnpm.io/workspaces), and [Yarn ↗︎](https://yarnpkg.com/features/workspaces) workspaces. You can also use tools such as [Turborepo ↗︎](https://turborepo.com/docs), [Nx ↗︎](https://nx.dev/getting-started/intro), or [Lerna ↗︎](https://lerna.js.org/docs/getting-started) to manage dependencies and task execution.

## Limitations

  * Monorepo support requires the V2 or [V3 build system](https://developers.cloudflare.com/pages/configuration/build-image/#v3-build-system).
  * You can configure a maximum of 5 Pages projects per repository. If you need this limit raised, contact your Cloudflare account team or use the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5).



[PreviousHeaders](https://developers.cloudflare.com/pages/configuration/headers/)[NextPreview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/monorepos.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
