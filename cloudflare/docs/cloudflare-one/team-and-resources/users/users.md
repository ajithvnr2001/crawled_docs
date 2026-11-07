---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/
title: User logs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:31:57.732921+00:00
---

# User logs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources

  4. /[Users](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/)
  5. /User logs



# User logs

Last updated Nov 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView user logs Available logs Registered passkeys

User logs show a list of all users who have authenticated to Cloudflare One. For each user who has logged in, you can view their enrolled devices, login history, seat usage, and identity used for policy enforcement.

## View user logs

In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Team & Resources** > **Users**.

This page lists all users who have registered the Cloudflare One Client or authenticated to a Cloudflare Access application. You can select a user's name to view detailed logs, [revoke their session](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions), or [remove their seat](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/).

### Available logs

  * **User Registry identity** : Select the user's name to view their last seen identity. This identity is used to evaluate Gateway policies and Cloudflare One Client [device profiles](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/). A refresh occurs when the user re-authenticates the device client, logs into an Access application, or has their IdP group membership updated via [SCIM provisioning](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/). To track how the user's identity has changed over time, go to the **Audit logs** tab.
  * **Session identities** : The user's active sessions, the identity used to authenticate each session, and when each session will [expire](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).
  * **Devices** : Devices registered to the user via the Cloudflare One Client.
  * **Recent activities** : The user's five most recent Access login attempts. For more details, refer to your [authentication audit logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#authentication-logs).



### Registered passkeys

In a user's **User identity** tab, the **Passkeys** section lists their registered passkeys, creation dates, and last-used dates. Administrators can [remove a user's passkey](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/passkeys/#remove-a-users-passkey) from this section.

[PreviousView SCIM users and groups](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim-population-viewer/)[NextRisk score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/users/users.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
