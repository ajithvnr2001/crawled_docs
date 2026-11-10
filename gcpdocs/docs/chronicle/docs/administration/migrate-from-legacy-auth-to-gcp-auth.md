---
url: https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-auth-to-gcp-auth/
title: Migrate to Google Cloud authentication \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T19:08:46.969596+00:00
---

# Migrate to Google Cloud authentication  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-auth-to-gcp-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate to Google Cloud authentication

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** For a comprehensive, end-to-end demo on the Migration process, see the [Google SecOps SIEM Legacy Infra Migration video ](https://youtu.be/Bg8VZftcrlg?si=3mvcaSucWS-KfZkd).

This document explains how to migrate an existing Google SecOps instance from legacy SIEM authentication to Google Cloud authentication.

## Before you begin

Make sure you have the following prerequisites:

  * The [required permissions](https://docs.cloud.google.com/chronicle/docs/onboard#roles-configure-idp) in your Google Cloud instance to perform the steps in this document.
  * Your Google SecOps instance has been migrated to your Google Cloud project.



## Migrate your instance

Complete the following steps:

  1. In the Google Cloud console, go to **Security > Google SecOps**.
  2. Under **Configure single sign-on** , select one of the following options based on which identity provider you use to manage user and group access to Google SecOps: 
     * If you are using Cloud Identity or Google Workspace, select **Google Cloud Identity**.
     * If you are using a third-party identity provider, select **Workforce Identity Federation** , and then select the workforce provider you want to use. You set this up when [configuring workforce identity federation](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).
  3. If you select **Workforce Identity Federation** , right-click **Test SSO setup** , and then open it in a private or incognito window. 
     * If you see a login screen, then SSO setup is successful.
     * If you don't see a login screen, verify the following settings: 
       * In your third-party identity provider (IdP), confirm that the Assertion Consumer Service (ACS) URL, Entity ID, and attribute mappings match your workforce provider. For more information, see [Configure a third-party identity provider for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).
       * In your firewall or proxy allowlist, confirm that outbound HTTPS and WebSocket Secure (WSS) traffic on TCP port `443` can reach all required sign-in domains. These include your IdP endpoints and Google domains, such as `*.backstory.chronicle.security`, `iam.googleapis.com`, and `accounts.google.com`. For more information, see [Network access and domain allowlist](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui#network-access-and-domain-allowlist).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
