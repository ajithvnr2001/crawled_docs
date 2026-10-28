---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/authentik-saml/
title: authentik (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:53.220791+00:00
---

# authentik (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/authentik-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /authentik (SAML)



# authentik (SAML)

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create an application in authentik2\. Get the authentik provider details3\. Add authentik to Cloudflare Access4\. Test the integration

Connect authentik to Cloudflare Access with Security Assertion Markup Language (SAML) 2.0.

## Prerequisites

  * An authentik account with administrator access
  * A Cloudflare account with Zero Trust access
  * A publicly accessible authentik deployment with a trusted TLS certificate



## 1\. Create an application in authentik

Your Cloudflare Access team name is part of the Assertion Consumer Service (ACS) URL. Locate your team name before you configure authentik.

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  1. Log in to authentik as an administrator and open the Admin interface.
  2. Go to **Applications** > **Applications** and select **New Application**.
  3. Enter the application details and select **Next**.
  4. For the provider type, select **SAML Provider**.
  5. Configure the provider: 
     1. Enter a provider name and select an authorization flow.

     2. For **ACS URL** , enter:
            
            https://<YOUR_TEAM_NAME>.cloudflareaccess.com/cdn-cgi/access/callback

     3. For **Audience** , enter the same Cloudflare Access callback URL.

     4. Select a **Signing Certificate** and keep **Sign assertions** turned on.

     5. For **Service Provider Binding** , select _Post_.

     6. For **Default NameID Policy** , select _Email address_.

  6. Select **Create Application**.



For more information about authentik provider settings, refer to [Create a SAML provider ↗︎](https://docs.goauthentik.io/add-secure-apps/providers/saml/create-saml-provider/).

## 2\. Get the authentik provider details

  1. In the authentik Admin interface, go to **Applications** > **Providers**.

  2. Select the SAML provider that you created for Cloudflare Access.

  3. Record the following values. Replace `<AUTHENTIK_DOMAIN>` with your authentik hostname and `<APPLICATION_SLUG>` with the associated application slug.

Cloudflare field | authentik value  
---|---  
Single Sign-On URL | `https://<AUTHENTIK_DOMAIN>/application/saml/<APPLICATION_SLUG>/`  
IdP Entity ID or Issuer URL | `https://<AUTHENTIK_DOMAIN>/application/saml/<APPLICATION_SLUG>/metadata/`  
  
  4. Under **Download signing certificate** , select **Download**. Save the certificate for the Cloudflare configuration.




The metadata tab also contains the SAML endpoint, entity ID, and signing certificate. For more information, refer to [SAML Provider ↗︎](https://docs.goauthentik.io/add-secure-apps/providers/saml/).

## 3\. Add authentik to Cloudflare Access

  1. In Cloudflare Zero Trust, go to **Integrations** > **Identity providers**.

[ Go to **Identity providers** ↗ ](https://one.dash.cloudflare.com/?to=/:account/one/integrations/identity-providers)
  2. Select **Add new identity provider** > **SAML**.

  3. Enter a name for the identity provider.

  4. Enter the **Single Sign-On URL** and **IdP Entity ID or Issuer URL** from authentik.

  5. For **Signing certificate** , paste the certificate downloaded from authentik.

  6. Select **Save**.




Caution

Access cannot verify SAML responses after the authentik signing certificate expires or changes. Update the certificate in Cloudflare Access before you rotate it in authentik.

## 4\. Test the integration

  1. In Cloudflare Zero Trust, go to **Integrations** > **Identity providers**.

[ Go to **Identity providers** ↗ ](https://one.dash.cloudflare.com/?to=/:account/one/integrations/identity-providers)
  2. Find the authentik identity provider and select **Test**.

  3. Complete the authentik login flow.

  4. Verify that Cloudflare displays a successful test result and the expected email address.




[Previousauthentik (OIDC)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/authentik-oidc/)[NextAWS IAM (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/authentik-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
