---
url: https://developers.cloudflare.com/fundamentals/manage-members/policies/
title: Policies \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:01:03.439252+00:00
---

# Policies · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/manage-members/policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /[Members and permissions](https://developers.cloudflare.com/fundamentals/manage-members/)
  4. /Policies



# Policies

Last updated Nov 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManage policiesViewing Effective Permissions

Policies define what access a given user has to your account or domains, and are constructed out of three parts:

  1. An actor (your user).
  2. A `ResourceGroup` (a scope).
  3. A `PermissionGroup` (roles).



An account member can have one or several of these policies to represent the most appropriate access. A member’s effective permissions are the union of all policies assigned to them—whether directly, or through group membership.

To increase the usability and flexibility of Cloudflare's role system, changes to the API have been made to expose these underlying data principles and allow users to interact with them.

For example, you may want to assign multiple policies and use scopes to control access to an account where you have a single account with both Production and Staging domains, and a user that should be able see the whole account, purge the production domains, but have the ability to configure the staging domains.

## Manage policies

A set of standard API endpoints is present on every account that allow access to your members, which has recently been enhanced by a list of `resourceGroups` and `PermissionGroups`.

  * A `resourceGroup` is a unique identifier for the scope for which a policy applies.
  * A `permissionGroup` is a unique identifier for the set of roles that are assigned to a given policy.



Refer to the [API documentation](https://developers.cloudflare.com/api/) for more information.

## Viewing Effective Permissions

Cloudflare supports assigning permissions to members both directly and through [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/). A member’s effective permissions are additive; they represent the union of all permissions granted directly to a member and those inherited through a member's group membership.

Note

To understand a member's full access, open that member's details from the **Members** page.

The member details view shows all permission policies associated with the member, including policies inherited through [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/).

Use the **Groups** tab when you need to review or change the policies assigned to a group itself.

[PreviousManage](https://developers.cloudflare.com/fundamentals/manage-members/manage/)[NextRoles](https://developers.cloudflare.com/fundamentals/manage-members/roles/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/manage-members/policies.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
