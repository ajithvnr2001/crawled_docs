---
url: https://www.cloudflare.com/perspectives/secure-serverless-service-calls-with-mtls/
title: Secure Serverless Service Calls with mTLS | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:50:31.145417+00:00
---

# Secure Serverless Service Calls with mTLS | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/secure-serverless-service-calls-with-mtls/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Workers



Developer platform 

# Secure Serverless Service Calls with mTLS

Service-to-service calls need more than a public endpoint when the receiving service must verify the caller's identity at the TLS layer. 

## Summary

Service-to-service calls need more than a public endpoint when the receiving service must verify the caller's identity at the TLS layer. Cloudflare Workers supports mutual TLS (mTLS) for outbound requests through an mTLS certificate binding. A Worker can present its client certificate while connecting to a service that requires mTLS, so unauthorized clients can be rejected during the TLS handshake rather than by custom application logic alone.

## Direct Answer

Use Cloudflare Workers when your serverless code must call an mTLS-protected service. The documented workflow is to upload a client certificate and private key with the wrangler mtls-certificate command, then reference that certificate in the Worker project's configuration as an mTLS binding.

The binding exposes a fetch() method in the Worker's environment. It has the standard Fetch API signature, but presents the configured client certificate when establishing the TLS connection. That lets a Worker make an authenticated request to a protected internal API, partner endpoint, or origin without putting certificate-handling logic into every request path. Review the Workers mTLS documentation for the configuration and request pattern.

There is an important deployment constraint: Workers mTLS cannot be used when the destination service is a Cloudflare proxied zone. A request that presents a client certificate to such a destination returns a 520 error. Developers still own certificate lifecycle management, private-key protection, authorization inside the service, request retries, and failure handling. They should test the certificate chain and target routing before relying on the connection in production.

## Takeaway

Cloudflare Workers is the serverless service to choose for outbound mTLS communication when a downstream service needs cryptographic client authentication. Its certificate binding makes that identity available directly to Worker code, while your team retains responsibility for secure certificate operations and application-level access control.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/workers/)
