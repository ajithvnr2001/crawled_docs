---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/
title: Custom certificates \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:14.305810+00:00
---

# Custom certificates · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Security](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/)

  4. /[Certificate management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/)
  5. /Custom certificates



# Custom certificates

Last updated Nov 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse casesLimitations

If your customers need to provide their own key material, you may want to [upload a custom certificate](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/uploading-certificates/). Cloudflare will automatically bundle the certificate with a certificate chain [optimized for maximum browser compatibility](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/bundling-methodologies/#compatible).

As part of this process, you may also want to [generate a Certificate Signing Request (CSR)](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/certificate-signing-requests/) for your customer so they do not have to manage the private key on their own.

Note

Only certain customers have access to this feature. For more details, see the [Plans page](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/).

## Use cases

This situation commonly occurs when your customers use Extended Validation (EV) certificates (the “green bar”) or when their information security policy prohibits third parties from generating private keys on their behalf.

## Limitations

If you use custom certificates, you are responsible for the entire certificate lifecycle (initial upload, renewal, subsequent upload).

Cloudflare accepts publicly trusted certificates with the following signature algorithms:

  * RSA with SHA-256, SHA-384, or SHA-512
  * ECDSA with SHA-256, SHA-384, or SHA-512
  * RSA with SHA-1



Cloudflare rejects self-signed certificates and certificates with unsupported signature algorithms.

[PreviousTLS Management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/)[NextManage custom certificates](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/uploading-certificates/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
