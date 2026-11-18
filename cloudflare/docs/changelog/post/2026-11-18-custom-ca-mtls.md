---
url: https://developers.cloudflare.com/changelog/post/2026-11-18-custom-ca-mtls/
title: Custom CA and client certificates (mTLS) for Workers VPC \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.971706+00:00
---

# Custom CA and client certificates (mTLS) for Workers VPC · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-18-custom-ca-mtls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 18, 2026

## Custom CA and client certificates (mTLS) for Workers VPC

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

VPC Services can now verify private services that use certificates from your own certificate authority (CA), and authenticate to services that require mutual TLS (mTLS). Previously, Workers VPC only trusted publicly trusted CAs and [Cloudflare Origin CA](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/), so connecting to a private CA meant weakening verification with `verify_ca` or `disabled`, and origins that required client certificates were unreachable.

Upload your CA certificate and client certificate, then reference them from the TLS settings of a VPC Service:
    
    
    npx wrangler cert upload certificate-authority --ca-cert ./ca.pem --name private-ca
    npx wrangler cert upload mtls-certificate --cert ./client.pem --key ./client-key.pem --name private-client
    
    npx wrangler vpc service create private-db \
      --type tcp \
      --tcp-port 5432 \
      --app-protocol postgresql \
      --hostname db.internal.example \
      --tunnel-id <TUNNEL_ID> \
      --certificate-authority <CA_CERTIFICATE_ID> \
      --client-certificate <CLIENT_CERTIFICATE_ID> \
      --cert-verification-mode verify_full

You can use a custom CA, a client certificate, or both. The settings apply to HTTPS connections from `http` services and to TLS connections from `tcp` services, including PostgreSQL databases used with [Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/), such as Amazon RDS instances that use the RDS CA bundle.

You can configure custom CA and client certificates with Wrangler 4.164.0 or later, the [API](https://developers.cloudflare.com/api/resources/connectivity/subresources/directory/subresources/services/), or Terraform provider 5.29.0 or later.

For details, refer to [Custom CA and client certificates](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/#custom-ca-and-client-certificates).
