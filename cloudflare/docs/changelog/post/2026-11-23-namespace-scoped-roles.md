---
url: https://developers.cloudflare.com/changelog/post/2026-11-23-namespace-scoped-roles/
title: Grant access to Workers in specific dispatch namespaces \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.249377+00:00
---

# Grant access to Workers in specific dispatch namespaces · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-23-namespace-scoped-roles/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 23, 2026

## Grant access to Workers in specific dispatch namespaces

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now grant members, User Groups, and API tokens access to the Workers in specific [dispatch namespaces](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace). Previously, managing Workers in a namespace required account-wide Workers access. Now you can create a token that deploys Workers to one namespace without giving it access to Workers in other namespaces or elsewhere in your account.

Choose from four roles to control the level of access:

  * **Workers Namespace Metadata Read-Only** : View Workers, settings, and bindings in the namespace. Excludes script code and secrets.
  * **Workers Namespace Content Read-Only** : Everything in Metadata Read-Only, plus script code and secret names.
  * **Workers Namespace Editor** : Create, update, deploy, and delete Workers in the namespace, including their code, settings, and secrets. Cannot view, update, or delete the namespace itself.
  * **Workers Namespace Admin** : Everything in Editor, plus the ability to view, update, and delete the namespace itself.

![Permission policy form showing four Workers Namespace roles scoped to an individual namespace](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=1130,format=webp/_astro/individual-namespace-member-role-ui.CmiePFgX.png)

A namespace role applies to every current and future Worker in the selected namespaces, and only to those Workers. Unlike the Workers Editor role, Workers Namespace Editor can create and delete Workers, so use it for teammates who deploy Workers and for CI/CD tokens. For example, scope your staging pipeline's token to the `staging` namespace so it cannot deploy to `production`.

Namespace roles are available today for all Workers for Platforms customers. You can configure them in the Cloudflare dashboard or through the API.

#### Grant access to members and User Groups

In the Cloudflare dashboard, go to the **Members** page and select a [member](https://developers.cloudflare.com/fundamentals/manage-members/manage/). Add a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), set the scope to **Individual Namespaces** , then select the namespaces and a Workers Namespace role.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)

To give several people the same access, assign the policy to a [User Group](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) instead of each member individually.

#### Create a scoped API token

Go to the **Account API Tokens** page and create an [account-owned API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/). Set the scope to **Specified Namespaces**.

[ Go to **Account API tokens** ↗ ](https://dash.cloudflare.com/?to=/:account/api-tokens) ![Account API token scope picker with Specified Namespaces selected](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2012,height=1812,format=webp/_astro/specified-namespaces-scope-picker.BaS300Ew.png)

Then select the namespaces the token can access and choose a Workers Namespace role.

![Account API token policy with Workers Namespace Metadata Read-Only access scoped to a specific namespace](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2014,height=940,format=webp/_astro/specified-namespaces-permission-policy-ui.LSohEJcG.png)

For more information, refer to [Workers for Platforms roles and permissions](https://developers.cloudflare.com/workers/authorization/workers-for-platforms/).
