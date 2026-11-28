---
url: https://developers.cloudflare.com/pages/configuration/git-integration/troubleshooting/
title: Troubleshooting builds \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:31.894781+00:00
---

# Troubleshooting builds · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/git-integration/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

Configuration

  4. /[Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/)
  5. /Troubleshooting builds



# Troubleshooting builds

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProject creation This repository is being used for a Cloudflare Pages project on a different Cloudflare account. Organization repository selection does not advance on GitHubDeployments This project is disconnected from your Git account, this may cause deployments to fail. Cloudflare Pages is not properly installed on your Git account, this may cause deployments to fail. The Cloudflare Pages installation has been suspended, this may cause deployments to fail. The project is linked to a repository that no longer exists, this may cause deployments to fail. The repository cannot be accessed, this may cause deployments to fail. There is an internal issue with your Cloudflare Pages Git installation. GitHub/GitLab is having an incident and push events to Cloudflare are operating in a degraded state. Check their status page for more details.

If your Git integration is experiencing issues, you may find the following banners on the **Deployments** page of your Pages project.

## Project creation

### `This repository is being used for a Cloudflare Pages project on a different Cloudflare account.`

Using the same GitHub or GitLab repository across separate Cloudflare accounts is disallowed. To use the repository for a Pages project in that Cloudflare account, delete any Pages projects using the repository in other Cloudflare accounts.

### Organization repository selection does not advance on GitHub

If your GitHub organization already has the **Cloudflare Workers and Pages** app installed but the repository selection step does not load or advance:

  1. In GitHub, open your organization settings and go to **Third-party Access** > **GitHub Apps**.
  2. Find **Cloudflare Workers and Pages** and select **Configure**.
  3. Update the **Repository access** list (for example, add or confirm the target repository) and select **Save** to refresh repository permissions.
  4. Return to Cloudflare and reconnect the repository.



## Deployments

If you run into issues related to deployments failing, check your project dashboard for source control management (SCM) installation warnings.

![Git installation warning banner on the Deployments page of a Cloudflare Pages project](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1504,height=168,format=webp/_astro/git.dashboard-error.z5oiIEkZ.png)

To resolve errors displayed in the Cloudflare Pages dashboard, follow the steps for the matching message.

### `This project is disconnected from your Git account, this may cause deployments to fail.`

To resolve this issue, reinstall the Git integration for [GitHub](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/#reinstall-the-cloudflare-github-app) or [GitLab](https://developers.cloudflare.com/pages/configuration/git-integration/gitlab-integration/#reinstall-the-cloudflare-gitlab-app). If the issue persists after uninstalling and reinstalling, [contact support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

### `Cloudflare Pages is not properly installed on your Git account, this may cause deployments to fail.`

To resolve this issue, reinstall the Git integration for [GitHub](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/#reinstall-the-cloudflare-github-app) or [GitLab](https://developers.cloudflare.com/pages/configuration/git-integration/gitlab-integration/#reinstall-the-cloudflare-gitlab-app). If the issue persists after uninstalling and reinstalling, [contact support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

### `The Cloudflare Pages installation has been suspended, this may cause deployments to fail.`

Go to your GitHub installation settings:

  * [Individual accounts ↗︎](https://github.com/settings/installations)
  * Organization accounts: `https://github.com/organizations/<YOUR_ORGANIZATION_NAME>/settings/installations`



Select **Configure** on the **Cloudflare Workers and Pages** application. Scroll to the bottom of the page and select **Unsuspend** to allow Cloudflare Pages to make future deployments.

### `The project is linked to a repository that no longer exists, this may cause deployments to fail.`

You may have deleted or transferred the repository associated with this Cloudflare Pages project. For a deleted repository, create a new Cloudflare Pages project with a repository that has not been deleted. For a transferred repository, either transfer the repository back to the original Git account or create a new Cloudflare Pages project with the transferred repository.

### `The repository cannot be accessed, this may cause deployments to fail.`

You may have excluded this repository from your installation's repository access settings. Go to your GitHub installation settings:

  * [Individual accounts ↗︎](https://github.com/settings/installations)
  * Organization accounts: `https://github.com/organizations/<YOUR_ORGANIZATION_NAME>/settings/installations`



Select **Configure** on the **Cloudflare Workers and Pages** application. Under **Repository access** , ensure that the repository associated with your Cloudflare Pages project is included in the list.

### `There is an internal issue with your Cloudflare Pages Git installation.`

This is an internal error in the Cloudflare Pages SCM system. Reinstall the Git integration for [GitHub](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/#reinstall-the-cloudflare-github-app) or [GitLab](https://developers.cloudflare.com/pages/configuration/git-integration/gitlab-integration/#reinstall-the-cloudflare-gitlab-app). If the issue persists, [contact support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

### `GitHub/GitLab is having an incident and push events to Cloudflare are operating in a degraded state. Check their status page for more details.`

This indicates that GitHub or GitLab may be experiencing an incident affecting push events to Cloudflare. Monitor their status pages ([GitHub ↗︎](https://www.githubstatus.com/), [GitLab ↗︎](https://status.gitlab.com/)) for updates and try deploying again later.

[PreviousGitLab integration](https://developers.cloudflare.com/pages/configuration/git-integration/gitlab-integration/)[NextHeaders](https://developers.cloudflare.com/pages/configuration/headers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/git-integration/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
