---
url: https://docs.cloud.google.com/chronicle/docs/log-in-to-ui/
title: Log in to Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T19:06:15.572039+00:00
---

# Log in to Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/log-in-to-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Log in to Google SecOps

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google Security Operations supports the Google Chrome and Mozilla Firefox browsers. Upgrade your browser to the most current version for optimal performance and security. The latest Chrome version is available for download at <https://www.google.com/chrome/>. Mobile operating systems (iOS/Android) and mobile browsers are not supported.

**Note:** You can access multiple Google SecOps instances within the same browser profile as long as you log in using the same user identity (the same Cloud Identity account or the same workforce identity pool). However, your active session is invalidated if you switch user accounts or access an instance configured with different workforce pool or different Google Cloud organization. To maintain concurrent sessions across different identities or authentication setups, use a separate browser profile or an incognito/private window for each session.

## Authentication and access

Google SecOps integrates with SSO solutions. Access to the Google SecOps platform requires valid enterprise credentials.

  1. Launch Chrome or Firefox.

  2. Verify you have active access to the corporate account.

  3. Go to the following URL and replace customer_subdomain with the customer-specific identifier to access the Google SecOps application:

`https://customer_subdomain.backstory.chronicle.security`


**Note:** Google SecOps doesn't provide an option to restrict user sessions.

## Network access and domain allowlist

Browser access to Google SecOps and Google Security Operations SOAR requires outbound HTTPS over Transport Layer Security (TLS) and WebSocket Secure (WSS) connections on TCP port `443`. If your organization uses egress firewalls, corporate proxies, or web filtering, add the required domains to your allowlist. The following sections list the required fully qualified domain names (FQDNs) and wildcard patterns. Configure domain-based allowlist rules instead of static IP addresses because Google IP addresses change dynamically.

### Mandatory SecOps and SOAR core domains

These domains support basic UI functionality, core API calls, and workspace navigation.

Domain pattern | Purpose  
---|---  
`*.backstory.chronicle.security` | Google SecOps frontend main domain, regional UI subdomains, authentication callback (`auth.backstory.chronicle.security`), and static application assets. If your firewall uses broader domain wildcards, you can add `*.chronicle.security` instead.  
`backstory.chronicle.security` | Bare apex domain serving core static application icons and images. Required if your proxy wildcard rule doesn't match the bare domain.  
`*-chronicle.googleapis.com` | Google SecOps core REST APIs (for example, `asia-southeast1-chronicle.googleapis.com`).  
`*-malachitefrontend-pa.googleapis.com` | Google SecOps regional frontend session initialization API (for example, `asia-southeast1-malachitefrontend-pa.googleapis.com`). This domain is covered if you allow `*.googleapis.com`.  
`*.siemplify-soar.com` | Google SecOps SOAR instance navigation and backend API endpoints.  
  
If your firewall policy doesn't allow wildcard domain entries, replace `*.backstory.chronicle.security`, `*-chronicle.googleapis.com`, and `*.siemplify-soar.com` with your tenant's specific URLs. Use the SOAR URL, Publisher hostname, and locational API endpoint provided when your tenant is provisioned.

If you deploy a Google SecOps SOAR Remote Agent using Podman or Docker, allow outbound HTTPS traffic on TCP port `443` to your container registries. Required registries include `*.pkg.dev`, `us-docker.pkg.dev`, and `gcr.io` for Artifact Registry, or `docker.io`. For more information, see [Network and firewall requirements](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/requirements-and-prerequisites#network-and-firewall-requirements).

### Mandatory authentication and Workforce Identity Federation domains

These domains support single sign-on (SSO), SAML and OpenID Connect (OIDC) authentication redirects, and identity provider (IdP) handshakes.

Domain pattern | Purpose  
---|---  
`iam.googleapis.com` | [Workforce Identity Federation](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication) authentication and token exchange API.  
`accounts.google.com` | Cloud Identity, Google Workspace, and Google OAuth 2.0 authorization and session token broker.  
`accounts.google.ccTLD` | Regional Google Account country-code TLD (ccTLD) check triggered based on the proxy's egress IP country, such as `accounts.google.com.sg`, `accounts.google.co.jp`, and `accounts.google.de`.  
`reauth.cloud.google.com` | Multi-factor authentication (MFA) session conformance.  
External IdP domains | Your organization's third-party IdP login and MFA asset domains, such as Okta or Microsoft Entra ID endpoints (`login.microsoftonline.com`, `*.msauth.net`, and `*.msftauth.net`).  
  
### Mandatory Google infrastructure and Cloud API domains

These endpoints support Google Cloud identity, resource permissions, static asset loading, and background platform services.

Domain pattern | Purpose  
---|---  
`*.googleapis.com` | Google API services. Allowing this wildcard simplifies proxy configuration across regional and supporting subdomains, such as `*-chronicle.googleapis.com`, `*-malachitefrontend-pa.googleapis.com`, `iam.googleapis.com`, `sts.googleapis.com`, `cloudresourcemanager.googleapis.com`, `firebase.googleapis.com`, and `fonts.googleapis.com`.  
`apis.google.com` | Google API Client Libraries (`gapi.loaded_0`) required by the Google SecOps web application.  
`console.cloud.google.com` | Google Cloud console integration and project context.  
`cloudconsole-pa.clients6.google.com` | Google Cloud console UI integration components.  
`cloudresourcemanager.googleapis.com` | Resource management and user permission validation.  
`firebase.googleapis.com` | Real-time notification and event streaming services.  
`*.gstatic.com` | Static platform resources, such as `ssl.gstatic.com` and `www.gstatic.com`.  
`fonts.gstatic.com` | Google Fonts static file host.  
`fonts.googleapis.com` | Google Fonts API interface.  
`*.googleusercontent.com` | Google Account profile images and user-affiliated static content, such as `lh3.googleusercontent.com`.  
`play.google.com` | Client-side application telemetry and logging.  
**Note:** If you administer Google SecOps in the Google Cloud console (`console.cloud.google.com`), also add the domains in [Allow access to Google Cloud console domains](https://docs.cloud.google.com/docs/get-started/required-domains) to your allowlist. For programmatic API, collector, or integration network rules, see [Verify firewall configuration for the Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/verify-firewall-configuration).

### Optional and non-blocking domains

Blocking these domains won't prevent core login or security investigation workflows, but it may affect usage telemetry, security policy reporting, or in-app survey prompts.

Domain pattern | Purpose  
---|---  
`www.google-analytics.com` | Usage metrics and session analytics.  
`www.googletagmanager.com` | Tag management for analytics deployment.  
`csp.withgoogle.com` | Content Security Policy (CSP) violation reporting.  
`*.siteintercept.qualtrics.com` | In-product user feedback and survey popups.  
  
## Initiate a search

Initiate a search by entering the domain, email, username, hostname, IP address, file hash, or URL into the search bar.

### Set the search window

Use the integrated **date** and **time** selector to focus your search on a specific window. Select the required dates and times using the calendar and clock settings dialog. 

**Note:** Google SecOps converts all recorded event timestamps to UTC to maintain consistency across all security data. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
