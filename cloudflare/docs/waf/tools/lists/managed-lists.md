---
url: https://developers.cloudflare.com/waf/tools/lists/managed-lists/
title: Managed Lists \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:48.409903+00:00
---

# Managed Lists · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/lists/managed-lists/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

Additional tools

  4. /[Lists](https://developers.cloudflare.com/waf/tools/lists/)
  5. /Managed Lists



# Managed Lists

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/lists/managed-lists/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManaged IP Lists

Cloudflare provides Managed Lists you can use in rule expressions. These lists are regularly updated.

Note

This feature requires an Enterprise plan.

## Managed IP Lists

Use Managed IP Lists to access Cloudflare's IP threat intelligence.

Cloudflare provides the following Managed IP Lists:

Display name | Name in expressions | Description  
---|---|---  
Cloudflare Open Proxies | `cf.open_proxies` | IP addresses of known open HTTP and SOCKS proxy endpoints, which are frequently used to launch attacks and hide attackers identity.  
Cloudflare Anonymizers | `cf.anonymizer` | IP addresses of known anonymizers (Open SOCKS Proxies, VPNs, and TOR nodes).  
Cloudflare VPNs | `cf.vpn` | IP addresses of known VPN servers.  
Cloudflare Malware | `cf.malware` | IP addresses of known sources of malware.  
Cloudflare Botnets, Command and Control Servers | `cf.botnetcc` | IP addresses of known botnet command-and-control servers.  
  
  


[PreviousBulk Redirect Lists ↗︎](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-lists)[NextCreate in the dashboard](https://developers.cloudflare.com/waf/tools/lists/create-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/lists/managed-lists.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
