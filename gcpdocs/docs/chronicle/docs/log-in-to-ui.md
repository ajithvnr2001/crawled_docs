---
url: https://docs.cloud.google.com/chronicle/docs/log-in-to-ui/
title: Log in to Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T09:54:41.783057+00:00
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

If your organization uses egress firewalls, corporate proxies, or strict web filtering, you must add the following Fully Qualified Domain Names (FQDNs) to your network allowlist to ensure uninterrupted access to Google SecOps and Google SecOps SOAR.

### Mandatory SecOps and SOAR core domains

These domains support basic UI functionality, core API calls, and workspace navigation.

Domain pattern | Purpose  
---|---  
`*.backstory.chronicle.security` | Google SecOps frontend main domain, regional UI subdomains, and authentication callback (`auth.backstory.chronicle.security`).  
`backstory.chronicle.security` | Bare apex domain serving core static application icons and images (required if your proxy wildcard rule doesn't match the bare domain).  
`*-chronicle.googleapis.com` | Google SecOps core REST APIs (for example, `asia-southeast1-chronicle.googleapis.com`).  
`*-malachitefrontend-pa.googleapis.com` | Google SecOps regional frontend session initialization API (for example, `asia-southeast1-malachitefrontend-pa.googleapis.com`). This domain is covered if you allow `*.googleapis.com`.  
`*.siemplify-soar.com` | Google SecOps SOAR instance navigation and backend API endpoints.  
  
If your firewall policy doesn't allow wildcard domain entries, you can replace `*.backstory.chronicle.security`, `*-chronicle.googleapis.com`, and `*.siemplify-soar.com` with the specific SOAR URL, Publisher hostname, and locational API endpoint provided when your tenant is provisioned.

If you deploy a Google SecOps SOAR Remote Agent using a container engine (Podman or Docker), allow outbound HTTPS traffic on TCP port `443` to the container registries used to pull the agent container image, such as `*.pkg.dev` (including `us-docker.pkg.dev`) and `gcr.io` for Artifact Registry, or `docker.io`. For more information, see [Network and firewall requirements](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/requirements-and-prerequisites#network-and-firewall-requirements).

### Mandatory authentication and Workforce Identity Federation domains

These domains support single sign-on (SSO), SAML and OpenID Connect (OIDC) authentication redirects, and identity provider (IdP) handshakes.

Domain pattern | Purpose  
---|---  
`*.cloud.google` (specifically `auth.cloud.google` and `clientlog.cloud.google`) | Google Cloud Workforce Identity Federation (bring your own identity, or BYOID) sign-in portal, SAML and OIDC callback handler, and authentication telemetry.  
Note: This domain uses the `.google` top-level domain (TLD), not `.google.com`.  
`accounts.google.com` | Google OAuth 2.0 authorization and session token broker.  
`accounts.google.ccTLD` (for example, `accounts.google.com.sg`, `accounts.google.co.jp`, `accounts.google.de`) | Regional Google Account country-code TLD (ccTLD) check triggered based on the proxy's egress IP country.  
`reauth.cloud.google.com` | Multi-factor authentication (MFA) session conformance.  
External IdP domains (for example, Microsoft Entra ID: `login.microsoftonline.com`, `*.msauth.net`, `*.msftauth.net`) | Your organization's third-party IdP login and MFA asset domains. Because required endpoints vary by provider (such as Microsoft Entra ID, Okta, or AD FS), consult your IdP's documentation or inspect a browser network log (HAR file) during sign-in to verify all required domains.  
  
### Mandatory Google infrastructure and Cloud API domains

These endpoints support Google Cloud identity, resource permissions, static asset loading, and background platform services.

Domain pattern | Purpose  
---|---  
`*.googleapis.com` | Google API services. We recommend allowing this wildcard to simplify proxy configuration and prevent connection blocks across regional and supporting Google API subdomains (such as `*-chronicle.googleapis.com`, `*-malachitefrontend-pa.googleapis.com`, `sts.googleapis.com`, `cloudresourcemanager.googleapis.com`, `firebase.googleapis.com`, and `fonts.googleapis.com`).  
`apis.google.com` | Google API Client Libraries (`gapi.loaded_0`) required by the Google SecOps web application.  
`console.cloud.google.com` | Google Cloud console integration and project context.  
`cloudconsole-pa.clients6.google.com` | Google Cloud console UI integration components.  
`cloudresourcemanager.googleapis.com` | Resource management and user permission validation.  
`firebase.googleapis.com` | Real-time notification and event streaming services.  
`*.gstatic.com` | Static platform resources.  
`fonts.gstatic.com` | Google Fonts static file host.  
`fonts.googleapis.com` | Google Fonts API interface.  
`*.googleusercontent.com` (specifically `lh3.googleusercontent.com`) | Google Account profile images and user-affiliated static content.  
`play.google.com` | Client-side application telemetry and logging.  
  
### Optional and non-blocking domains

Blocking these domains won't prevent core login or security investigation workflows, but it may affect usage telemetry, security policy reporting, or in-app survey prompts.

Domain | Purpose  
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

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
