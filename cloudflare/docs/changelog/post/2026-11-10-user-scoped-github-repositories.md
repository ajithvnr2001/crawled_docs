---
url: https://developers.cloudflare.com/changelog/post/2026-11-10-user-scoped-github-repositories/
title: Workers Builds and Pages now list GitHub repositories based on your GitHub account \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:00:58.620259+00:00
---

# Workers Builds and Pages now list GitHub repositories based on your GitHub account · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-10-user-scoped-github-repositories/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 10, 2026

## Workers Builds and Pages now list GitHub repositories based on your GitHub account

[Workers](https://developers.cloudflare.com/workers/)[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you connect a GitHub repository to [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) or [Pages](https://developers.cloudflare.com/pages/), the accounts and repositories you can pick from are now based on your own GitHub account, so the list reflects the repositories you work with on GitHub. Previously, the list was based on the Cloudflare Workers & Pages GitHub App installations linked to your Cloudflare account, so it could include repositories that you cannot access on GitHub.

![Three developers on the same Cloudflare account have all authorized the app, and the app is installed on acme-corp and dev-1. Each sees a different repository picker. dev-1 can pick acme-corp or dev-1, with payments-api and website listed for acme-corp. dev-2 can only pick acme-corp, with only website listed. dev-3 has no accounts or repositories, only the option to add a GitHub account.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=704,format=webp/_astro/github-repository-access.D8iduHF9.png)

The list now shows:

  * Your own GitHub account, if the app is installed on it.
  * GitHub organizations that have the app installed, where you can access at least one repository.
  * The repositories you can access in each of them.



GitHub accounts that belong to other users are no longer listed, even if they have given you access to one of their repositories.

**What this means for you:**

Authorizing the app and installing it are two separate steps on GitHub. For more details, refer to Install and authorize the app for [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/#install-and-authorize-the-app) and [Pages](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/#install-and-authorize-the-app).

![Authorize: tells Cloudflare who you are, once per person, listed under Authorized GitHub Apps. Install: decides which repositories Cloudflare can access, listed under Installed GitHub Apps.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=392,format=webp/_astro/github-authorize-vs-install.DsQ5aSYE.png)

  * **If you have already authorized the app with your GitHub user:** Nothing changes. You can check on the [Authorized GitHub Apps page ↗︎](https://github.com/settings/apps/authorizations) on GitHub.
  * **If you have not:** The next time you connect a repository, Cloudflare sends you to GitHub to authorize the app. You only need to do this once, even if someone else on your Cloudflare account already connected GitHub.
  * **If the app is not installed on any GitHub account you can access:** After you authorize, install the app on your own GitHub account or an organization, the same as before.
  * **If an account or organization is missing from the list:** Select **Add GitHub account** and install the app on it.



Projects that are already connected to a repository are not affected and keep building.

For more information, refer to Repository access for [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/#repository-access) and [Pages](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/#repository-access).
