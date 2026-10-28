---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/authentik-oidc/
title: authentik (OIDC) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:53.347864+00:00
---

# authentik (OIDC) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/authentik-oidc/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /authentik (OIDC)



# authentik (OIDC)

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create an application in authentik2\. Add authentik to Cloudflare Access3\. Test the integration

Connect authentik to Cloudflare Access with OpenID Connect (OIDC). OIDC is the recommended protocol when your identity provider supports both OIDC and SAML.

## Prerequisites

  * An authentik account with administrator access
  * A Cloudflare account with Zero Trust access
  * A publicly accessible authentik deployment with a trusted TLS certificate



## 1\. Create an application in authentik

Your Cloudflare Access team name is part of the redirect URI. Locate your team name before you configure authentik.

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  1. Log in to authentik as an administrator and open the Admin interface.
  2. Go to **Applications** > **Applications** and select **New Application**.
  3. Enter the application details and select **Next**.
  4. For the provider type, select **OAuth2/OpenID Connect**.
  5. Configure the provider: 
     1. Enter a provider name.

     2. Select an authorization flow.

     3. Add a redirect URI with the _Strict_ matching mode and _Authorization_ type:
            
            https://<YOUR_TEAM_NAME>.cloudflareaccess.com/cdn-cgi/access/callback

     4. Select a signing key. The signing key allows Access to verify tokens through the authentik JSON Web Key Set (JWKS) endpoint.

     5. Ensure that the provider includes the `openid`, `email`, and `profile` scope mappings.

  6. Record the **Client ID** , **Client Secret** , and application slug.
  7. Select **Submit**.



For more information about authentik provider settings, refer to [OAuth 2.0 provider ↗︎](https://docs.goauthentik.io/add-secure-apps/providers/oauth2/).

## 2\. Add authentik to Cloudflare Access

  1. In Cloudflare Zero Trust, go to **Integrations** > **Identity providers**.

[ Go to **Identity providers** ↗ ](https://one.dash.cloudflare.com/?to=/:account/one/integrations/identity-providers)
  2. Select **Add new identity provider** > **OpenID Connect**.

  3. Enter the following values. Replace `<AUTHENTIK_DOMAIN>` with your authentik hostname and `<APPLICATION_SLUG>` with the application slug from authentik.

Field | Value  
---|---  
Name | `authentik`  
App ID | The authentik **Client ID**  
Client secret | The authentik **Client Secret**  
Auth URL | `https://<AUTHENTIK_DOMAIN>/application/o/authorize/`  
Token URL | `https://<AUTHENTIK_DOMAIN>/application/o/token/`  
Certificate URL | `https://<AUTHENTIK_DOMAIN>/application/o/<APPLICATION_SLUG>/jwks/`  
  
  4. Select **Save**.




The token and certificate endpoints must allow requests from Cloudflare. Interactive challenges or firewall rules on these endpoints can prevent Access from completing authentication.

## 3\. Test the integration

  1. In Cloudflare Zero Trust, go to **Integrations** > **Identity providers**.

[ Go to **Identity providers** ↗ ](https://one.dash.cloudflare.com/?to=/:account/one/integrations/identity-providers)
  2. Find the authentik identity provider and select **Test**.

  3. Complete the authentik login flow.

  4. Verify that Cloudflare displays a successful test result and the expected email address.




[PreviousAmazon Cognito](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/)[Nextauthentik (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/authentik-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/authentik-oidc.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
