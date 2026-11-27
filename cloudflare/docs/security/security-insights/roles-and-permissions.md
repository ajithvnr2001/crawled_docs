---
url: https://developers.cloudflare.com/security/security-insights/roles-and-permissions/
title: Roles and permissions \u00b7 Security dashboard docs
method: scrapling+scrapegraph
fetched_at: 2026-11-27T10:39:59.612716+00:00
---

# Roles and permissions · Security dashboard docs

> Source: https://developers.cloudflare.com/security/security-insights/roles-and-permissions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security dashboard](https://developers.cloudflare.com/security/)
  3. /[Security Insights](https://developers.cloudflare.com/security/security-insights/)
  4. /Roles and permissions



# Roles and permissions

Last updated Nov 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDashboard rolesAPI token permissions Account and zone scope

Security Insights separates access to findings, on-demand scans, and automatic scan settings. Permissions also depend on the account, domain, and product associated with an insight.

## Dashboard roles

Assign [member roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/) for the accounts or domains a member needs. These account-scoped roles provide the following access:

Role | View insights | Archive or restore insights | Start on-demand scans | Turn automatic scans on or off  
---|---|---|---|---  
Security Center Admin | All products | All products | Yes | Yes  
Administrator | All products | All products | Yes | Yes  
Super Administrator - All Privileges | All products | All products | Yes | Yes  
Security Center Read | All products | No | No | No  
Administrator Read Only | All products | No | No | No  
DNS | DNS | DNS | Yes | No  
Firewall | WAF | WAF | Yes | No  
Page Shield | Client-side security | Client-side security | Yes | No  
Page Shield Read | Client-side security | No | No | No  
SSL/TLS, Caching, Performance, Page Rules, and Customization | SSL/TLS | SSL/TLS | Yes | No  
  
The **Domain Administrator** , **Domain Administrator Read Only** , and **Domain DNS** roles provide read-only access to DNS insights for their assigned domains. These roles do not grant insight archiving, on-demand scans, or account-wide automatic scan settings.

Access to Security Insights does not grant permission to change the underlying product configuration. For example, resolving an insight by changing a zone setting requires permission to edit that setting.

For least privilege, use **Security Center Read** to review findings. Use **Security Center Admin** to manage findings and scans without granting general account administration. Product-specific roles limit which findings a member can view and archive, but their on-demand scan permission is not limited to that product.

## API token permissions

Create an [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the permission for your endpoint:

Permission | Read | Edit (includes Read)  
---|---|---  
Account Security Center Insights | View findings, account scan history, and automatic scan settings. | Archive or restore findings, start account scans, and turn automatic scans on or off.  
Zone Security Center Insights | View findings and zone scan history. | Archive or restore findings and start zone scans.  
  
### Account and zone scope

Account permissions apply to selected accounts, not individual domains. Use them with `/accounts/{account_id}/security-center/insights` and `/accounts/{account_id}/security-center/state`. The account insights endpoint can also return zone-level findings for some products, but not all.

Zone permissions apply to selected zones and cover all supported zone products. To restrict access to specific domains, select only those zones and use `/zones/{zone_id}/security-center/insights`. You do not need separate product permissions to read these insights. Zone permissions do not grant access to automatic scan settings.

[PreviousReview Security Insights](https://developers.cloudflare.com/security/security-insights/review-insights/)[NextSecurity Analytics](https://developers.cloudflare.com/security/analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security/security-insights/roles-and-permissions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
