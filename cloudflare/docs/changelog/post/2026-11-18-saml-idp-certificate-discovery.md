---
url: https://developers.cloudflare.com/changelog/post/2026-11-18-saml-idp-certificate-discovery/
title: Automatically retrieve SAML IdP signing certificates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.619621+00:00
---

# Automatically retrieve SAML IdP signing certificates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-18-saml-idp-certificate-discovery/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 18, 2026

## Automatically retrieve SAML IdP signing certificates

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access can retrieve signing certificates from a SAML identity provider's metadata endpoint. Your IdP can publish replacement certificates without requiring you to upload each one to Access.

In your generic SAML identity provider configuration, set **Signing certificate source** to **Fetch certificates from IdP metadata** and enter the **IdP metadata URL**. The endpoint must return SAML metadata XML over public HTTPS, without authentication or redirects. It must not return a JSON Web Key Set (JWKS).

For API configurations, use `metadata_url` instead of manual certificate fields:
    
    
    {
    	"type": "saml",
    	"config": {
    		"issuer_url": "https://idp.example.com",
    		"sso_target_url": "https://idp.example.com/sso",
    		"metadata_url": "https://idp.example.com/metadata.xml"
    	}
    }

Access caches the certificates and does not poll the endpoint.

Removing a compromised certificate from metadata does not immediately revoke the cached certificate or existing Access sessions. For setup, planned rotation, and emergency replacement guidance, refer to [Discover IdP signing certificates](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#discover-idp-signing-certificates).
