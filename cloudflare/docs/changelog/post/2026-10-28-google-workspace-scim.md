---
url: https://developers.cloudflare.com/changelog/post/2026-10-28-google-workspace-scim/
title: Google Workspace SCIM user provisioning through generic SAML \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:16.762464+00:00
---

# Google Workspace SCIM user provisioning through generic SAML · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-28-google-workspace-scim/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2026

## Google Workspace SCIM user provisioning through generic SAML

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

System for Cross-domain Identity Management (SCIM) is an open standard that synchronizes user identities between an identity provider and a service. For more information, refer to [SCIM provisioning](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/). Google Workspace is rolling out custom SCIM profiles in beta. Organizations with access to the feature can use Google's built-in provisioning service to send user updates and deprovisioning events to Cloudflare One.

**You must use a generic SAML identity provider in Cloudflare One.** The dedicated Google Workspace integration does not support SCIM. Configure a SAML app in Google, then enter the Cloudflare SCIM endpoint and secret in the app's autoprovisioning settings. Turn on **Enable user deprovisioning** in Cloudflare One to revoke active Access sessions when Google deprovisions a user. Google's configured deprovisioning delay still applies. Support for the existing Google Workspace OIDC client will be added once Google adds support for OIDC + SCIM.

Group membership is configured separately. Have the Google SAML app send a `groups` attribute to include the user's selected Google groups during authentication. Selecting groups as a SCIM provisioning scope does not synchronize group membership, Google is still adding support for this in their SCIM provider.

Cloudflare One users must first authenticate to Access or register a device with the Cloudflare One Client before SCIM updates can apply. Availability of custom SCIM profiles depends on Google's beta rollout.

For setup instructions, refer to [Google Workspace (SAML/SCIM)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google-workspace-saml/).
