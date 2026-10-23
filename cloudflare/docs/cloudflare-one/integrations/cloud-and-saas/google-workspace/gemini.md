---
url: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/
title: Gemini for Google Workspace \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:59:23.793086+00:00
---

# Gemini for Google Workspace · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations[Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

  4. /[Google Workspace](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/)
  5. /Gemini for Google Workspace



# Gemini for Google Workspace

Last updated Oct 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntegration prerequisitesIntegration permissionsSecurity findings User account settings Inactive or suspended users Gemini licensing

The Gemini for Google Workspace integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.

## Integration prerequisites

  * A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan
  * A Google Workspace user with [Super Admin privileges ↗︎](https://support.google.com/a/answer/2405986) and [Owner permissions ↗︎](https://cloud.google.com/iam/docs/understanding-roles) in the Google Cloud Platform (GCP) project used



## Integration permissions

Refer to [Google Workspace integration permissions](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/#integration-permissions) for information on which API permissions to enable.

## Security findings

The Gemini for Google Workspace integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by [severity level](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels).

To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its [RSS feed](https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/gemini.mdx.atom).

### User account settings

Finding type | FindingTypeID | Severity | Description  
---|---|---|---  
Google Workspace: Admin user with Gemini license with two-factor authentication disabled | `4d179f48-ab14-4f20-a45c-2bcf8228d95d` | High | An administrator with a Gemini for Google Workspace license does not have two-factor authentication enabled.  
Google Workspace: User with Gemini license with two-factor authentication disabled | `1b33c200-c0cc-4c55-99fa-92c16a98976e` | Medium | A user with a Gemini for Google Workspace license does not have two-factor authentication enabled.  
  
### Inactive or suspended users

Finding type | FindingTypeID | Severity | Description  
---|---|---|---  
Google Workspace: Admin user suspended with AI Ultra license | `0d19a636-e4ca-4ab1-b590-7e0ff19c7fef` | Low | An administrator account with an AI Ultra (Gemini for Workspace) license is suspended.  
Google Workspace: User suspended with AI Ultra license | `e642db61-dc20-4742-89c4-b8041ed237cb` | Low | A user account with an AI Ultra (Gemini for Workspace) license is suspended.  
  
### Gemini licensing

Finding type | FindingTypeID | Severity | Description  
---|---|---|---  
Google Workspace: Admin user with AI Ultra license | `c7519b56-d42a-4eda-ba59-21a0b30ad94a` | Low | An administrator in Google Workspace is assigned an AI Ultra (Gemini for Workspace) license.  
Google Workspace: User with AI Ultra license | `8299627e-19cd-4ae1-95ba-35ab6ec78413` | Low | A user in Google Workspace is assigned an AI Ultra (Gemini for Workspace) license.  
  
[PreviousGoogle Drive (FedRAMP)](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive-fedramp/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
