---
url: https://developers.cloudflare.com/pages/configuration/branch-build-controls/
title: Branch deployment controls \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:32.446317+00:00
---

# Branch deployment controls · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/branch-build-controls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Branch deployment controls



# Branch deployment controls

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProduction branch controlPreview branch control Custom preview branch control

When connected to your Git repository, Pages allows you to control which environments and branches automatically deploy. By default, Pages triggers a deployment whenever you commit to either your production or preview environment. With branch deployment controls, you can configure automatic deployments on a per-project basis.

For branch build controls on Cloudflare Workers, refer to [Workers Builds branch controls](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/).

## Production branch control

Direct Upload

If your project is a [Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/) project, you will not have the option to configure production branch controls. To update your production branch, you will need to manually call the [Update Project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/edit/) endpoint in the API.
    
    
    curl --request PATCH \
    "https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data "{\"production_branch\": \"main\"}"

To configure deployment options:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Go to **Settings** > **Build** > **Branch control**.




Pages defaults to setting your production environment to the branch you first push, but you can set your production branch to another branch.

You can also turn automatic deployment behavior on or off for the production branch using **Enable automatic production branch deployments** , then save your settings for the changes to take effect.

## Preview branch control

When configuring automatic preview deployments, there are three options to choose from.

  * **All non-Production branches** : By default, Pages will automatically deploy any and every commit to a preview branch.
  * **None** : Turns off automatic builds for all preview branches.
  * **Custom branches** : Customize the automatic deployments of certain preview branches.



### Custom preview branch control

By selecting **Custom branches** , you can specify branches you wish to include and exclude from automatic deployments in the provided configuration fields. The configuration fields can be filled in two ways:

  * **Static branch names** : Enter the precise name of the branch you are looking to include or exclude (for example, staging or dev).
  * **Wildcard syntax** : Use wildcards to match multiple branches. You can specify wildcards at the start or end of your rule. The order of execution for the configuration is (1) Excludes, (2) Includes, (3) Skip. Pages will process the exclude configuration first, then go to the include configuration. If a branch does not match either then it will be skipped.



Wildcard syntax

A wildcard (`*`) is a character that is used within rules. It can be placed alone to match anything or placed at the start or end of a rule to allow for better control over branch configuration. A wildcard matches zero or more characters. For example, if you want to match all branches that start with `fix/`, create the rule `fix/*` to match strings like `fix/1`, `fix/bugs`, or `fix/`.

**Example 1:**

If you want to enforce branch prefixes such as `fix/`, `feat/`, or `chore/` with wildcard syntax, you can include and exclude certain branches with the following rules:

  * Include Preview branches: `fix/*`, `feat/*`, `chore/*`
  * Exclude Preview branches: _(leave empty)_



Here Pages includes any branches with the indicated prefixes and skips everything else.

**Example 2:**

If you want to prevent [Dependabot ↗︎](https://github.com/dependabot) from creating a deployment for each PR it creates, you can exclude those branches with the following rules:

  * Include Preview branches: `*`
  * Exclude Preview branches: `dependabot/*`



Here Pages includes all branches except any branch starting with `dependabot/`.

**Example 3:**

If you only want to deploy release-prefixed branches, leave **Exclude Preview branches** empty (excludes evaluate before includes, so setting `*` in excludes would skip every branch):

  * Include Preview branches: `release/*`
  * Exclude Preview branches: _(leave empty)_



This deploys only branches starting with `release/` and skips all other branches.

[PreviousMigrate to Workers ↗︎](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/)[NextBuild caching](https://developers.cloudflare.com/pages/configuration/build-caching/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/branch-build-controls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
