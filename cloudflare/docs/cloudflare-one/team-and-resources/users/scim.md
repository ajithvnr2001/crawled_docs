---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/
title: SCIM provisioning \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:21.501434+00:00
---

# SCIM provisioning · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources

  4. /[Users](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/)
  5. /SCIM provisioning



# SCIM provisioning

Last updated Oct 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported identity providersSync users and groups in Zero Trust policiesView provisioned users and groupsCommon provider-specific issues

System for Cross-domain Identity Management (SCIM) is an open standard protocol that allows identity providers to synchronize user identity information with cloud applications and services. After configuring SCIM, user identities that you create, edit, or delete in the identity provider are automatically updated across all supported applications. This makes it easier for IT admins to onboard new users, update their groups and permissions, and revoke access in the event of an employee termination or security breach.

Note

This section covers SCIM provisioning for Cloudflare Zero Trust only. To provision access to your Cloudflare account, you will need to set up a distinct [dashboard SSO SCIM integration](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/) in your IdP. You can assign users and groups to this new SCIM application to define who can access the Cloudflare dashboard.

Users provisioned via the Zero Trust SCIM integration will not have access to your Cloudflare dashboard unless you have manually added them to your [Cloudflare dashboard SSO application](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/).

## Supported identity providers

Cloudflare One supports SCIM provisioning for all SAML and OIDC identity providers that use SCIM version `2.0`.

For Google's built-in SCIM provisioning, you must use a [Google Workspace (SAML/SCIM) integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google-workspace-saml/), not the dedicated Google Workspace integration. Google's custom SCIM profiles are in beta and provision users; configure [SAML group membership mapping](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google-workspace-saml/#1-create-a-custom-saml-app-in-google-workspace) separately to send groups during authentication.

## Sync users and groups in Zero Trust policies

Cloudflare Access can automatically deprovision users from Zero Trust after they are deactivated in the identity provider and display synchronized group names in the Access and Gateway policy builders. Cloudflare does not provision new users in Zero Trust when they are added to the identity provider -- users must first register a device with the Cloudflare One Client or authenticate to an Access application.

SCIM affects Access and Gateway policy evaluation differently.

Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on **Enable user deprovisioning** , removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.

Gateway evaluates identity-based policies against the [User Registry identity](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/). SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.

To set up SCIM for Zero Trust, refer to our [SSO integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) guides.

## View provisioned users and groups

Use the [SCIM population viewer](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim-population-viewer/) to inspect users and groups provisioned through each identity provider. You can search for resources, inspect their attributes and group membership, and compare resource IDs with SCIM provisioning logs.

## Common provider-specific issues

SCIM behavior depends on the identity provider configuration as well as Cloudflare.

Common issues include:

  * **Okta** : User sync and group sync are separate. Make sure **Push Groups** is configured if you expect groups to appear in Zero Trust policies.
  * **Microsoft Entra ID** : Group sync only occurs for groups included in the provisioning scope. The `userName` attribute should match the user's email address in Cloudflare One.
  * **Google Workspace** : SCIM requires a generic SAML integration. Selecting Google groups as a provisioning scope limits which users are provisioned; it does not send group membership. Configure the SAML app to send a `groups` attribute for group-based policies.



If users appear but groups do not, verify the IdP-side SCIM app first before troubleshooting Cloudflare policy behavior.

[PreviousSeat management](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/)[NextView SCIM users and groups](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim-population-viewer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/users/scim.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
