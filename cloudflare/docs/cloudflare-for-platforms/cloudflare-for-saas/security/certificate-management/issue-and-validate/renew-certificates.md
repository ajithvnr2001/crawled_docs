---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/
title: Renew certificates \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:38:29.642375+00:00
---

# Renew certificates · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Security](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/)[Certificate management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/)

  4. /Issue and validate certificates
  5. /Renew



# Renew

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHTTP validationTXT validation

Custom hostname certificates have a 90-day validity period and are available for renewal 30 days before their expiration.

The validation method selected when you create a custom hostname applies to initial certificate issuance. During an Automated Certificate Management Environment (ACME) renewal, Cloudflare selects a method based on the hostname's current configuration and eligibility.

You can explicitly change the method through the API. DigiCert uses a separate renewal workflow.

## HTTP validation

Cloudflare can automatically renew a custom hostname certificate through [HTTP validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/) when all these conditions are true:

  * The custom hostname is not a wildcard.
  * The hostname is active.1
  * The hostname points to the SaaS provider.
  * The hostname traffic is proxied through Cloudflare.
  * The hostname does not use [Delegated DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/).



Cloudflare may use HTTP validation even if you selected TXT for initial issuance.

If automatic HTTP validation is unavailable, retrieve the custom hostname's current `ssl.method` and `ssl.validation_records`. Share the required HTTP or TXT records with the domain owner.

## TXT validation

Wildcard hostnames cannot use HTTP validation. They must use [TXT validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/).

Non-wildcard hostnames with properly configured [Delegated DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/) also remain TXT-based. Keep the delegation CNAME record in place for future renewals.

For manual TXT validation, use each certificate order's current `ssl.validation_records`. These records can change between certificate orders.

These tokens can be fetched through the API or the dashboard when the certificates are in a [pending validation](https://developers.cloudflare.com/ssl/reference/certificate-statuses/#new-certificates) state during custom hostname creation or during certificate renewals.

If your hostname is using another validation method, you will need to [update](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/) the `"method"` field in the SSL object to be `"txt"`.

After this step, follow the normal steps for [TXT validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/).

Note

To automate TXT placement for future certificate orders, consider [Delegated DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/).

## Footnotes

  1. Meaning Cloudflare could verify your customer's ownership of the hostname and the [hostname status](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/) is active. ↩




[PreviousTroubleshooting](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/)[NextTLS Management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
