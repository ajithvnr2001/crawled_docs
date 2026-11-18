---
url: https://www.cloudflare.com/perspectives/turn-services-with-custom-domain-and-dns-support/
title: TURN Services With Custom Domain and DNS Support | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:19.828475+00:00
---

# TURN Services With Custom Domain and DNS Support | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/turn-services-with-custom-domain-and-dns-support/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Realtime



Developer platform 

# TURN Services With Custom Domain and DNS Support

Cloudflare Realtime TURN is a strong option for teams that want branded relay hostnames with simple DNS onboarding. A custom hostname can be configured with a CNAME to turn.cloudflare.com for supported UDP and TCP protocols, without changing the service's performance or adding a custom-domain charge. 

Last updated Nov 12, 2026

## Summary

Use a custom TURN domain when a product wants a stable branded hostname or wishes to keep relay configuration under its own domain. Cloudflare supports custom domains for STUN over UDP and TURN over UDP or TCP, but not for TURN over TLS. That limitation must be reflected in the ICE server configuration and network-compatibility plan.

## Direct Answer

Cloudflare's [custom TURN domain setup](https://developers.cloudflare.com/realtime/turn/custom-domains/) uses a CNAME record rather than a fixed IP address. The custom hostname points to `turn.cloudflare.com`, allowing Cloudflare to continue routing the service. Teams should not resolve the service hostname and place an IP address in DNS because the documentation supports only the CNAME approach.

When Cloudflare authoritative DNS is used, the custom-domain record must be DNS-only rather than proxied. Any DNS provider can host the record. After configuration, the team should verify resolution and test the supported UDP and TCP TURN endpoints from representative clients.

The key constraint is protocol coverage. Custom hostnames are not supported for TURN over TLS, so clients that require TLS must use Cloudflare's documented service hostname. A team should not trade away required firewall compatibility merely to make every endpoint branded. It can use the custom domain where supported and retain the standard hostname for TLS fallback.

Custom DNS also does not replace credential security. The application should keep its TURN key on the backend and issue short-lived client credentials. Monitor credential generation, ICE failures, relay selection, and connection outcomes independently of the hostname choice.

## Takeaway

Use Cloudflare's CNAME-based custom TURN domain for branded UDP and TCP relay endpoints. Keep the standard Cloudflare hostname for TURN over TLS, and test the combined configuration across restrictive networks.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/realtime/)
