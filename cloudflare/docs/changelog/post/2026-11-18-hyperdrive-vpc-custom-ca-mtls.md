---
url: https://developers.cloudflare.com/changelog/post/2026-11-18-hyperdrive-vpc-custom-ca-mtls/
title: Custom CA and mTLS certificates for Hyperdrive over Workers VPC \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:30.301561+00:00
---

# Custom CA and mTLS certificates for Hyperdrive over Workers VPC · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-18-hyperdrive-vpc-custom-ca-mtls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 18, 2026

## Custom CA and mTLS certificates for Hyperdrive over Workers VPC

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive can now connect to private databases over [Workers VPC](https://developers.cloudflare.com/workers-vpc/) with a custom certificate authority (CA) and client certificate authentication (mutual TLS, or mTLS). This covers PostgreSQL databases and Amazon RDS instances that present certificates signed by a private CA or the RDS CA bundle, and client certificates with RSA or EC P-256 keys.

Previously, a database that required a custom CA or a client certificate meant routing database traffic over WebSockets through [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) and [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/). That approach added an Access application, a service token, and WebSocket handling to maintain.

Hyperdrive now connects directly to the database over Workers VPC, without Access.

Attach the certificates to the VPC Service, then create a Hyperdrive configuration from that service:
    
    
    # Upload the private CA and the client certificate
    npx wrangler cert upload certificate-authority --ca-cert ./db-ca.pem --name db-ca
    npx wrangler cert upload mtls-certificate --cert ./client.pem --key ./client-key.pem --name db-client
    
    # Attach the certificates to the VPC Service for your database
    npx wrangler vpc service create my-postgres-db \
      --type tcp \
      --tcp-port 5432 \
      --app-protocol postgresql \
      --hostname <YOUR_DATABASE_HOSTNAME> \
      --tunnel-id <YOUR_TUNNEL_ID> \
      --certificate-authority <CA_CERTIFICATE_ID> \
      --client-certificate <CLIENT_CERTIFICATE_ID> \
      --cert-verification-mode verify_full
    
    # Create the Hyperdrive configuration from the VPC Service
    npx wrangler hyperdrive create <YOUR_CONFIG_NAME> \
      --service-id <YOUR_VPC_SERVICE_ID> \
      --database <DATABASE_NAME> \
      --user <DATABASE_USER> \
      --password <DATABASE_PASSWORD> \
      --scheme postgresql

You can use a custom CA, a client certificate, or both. Configure VPC Services with Wrangler 4.164.0 or later, the [API](https://developers.cloudflare.com/api/resources/connectivity/subresources/directory/subresources/services/), or Terraform provider 5.29.0 or later. Dashboard support for these settings is not yet available.

For setup details and certificate rotation, refer to [Connect Hyperdrive to a private database using Workers VPC](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/) and [Custom CA and client certificates](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/#custom-ca-and-client-certificates).
