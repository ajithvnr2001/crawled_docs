---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/
title: Software support and deprecation policy \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:29:56.616953+00:00
---

# Software support and deprecation policy  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/support-deprecation/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


Was this helpful?
Send feedback 
#  Software support and deprecation policy Stay organized with collections  Save and categorize content based on your preferences.
This document describes the Google Distributed Cloud (GDC) air-gapped software support and deprecation policy. 
  1. GDC will provide a minimum of one year's notice of any breaking change. This notice might be issued anytime after a service or feature becomes generally available (GA), but the change itself won't take effect until the one-year notice period has concluded. If a deprecation notice is issued immediately after a service becomes generally available, there will be a one-year period before the service is decommissioned.
  2. GDC will provide support for one year for each minor version release of any feature or service that is generally available(GA). The support period starts from when the component's feature or a minor version is officially released as part of a GDC release and published and not when it is deployed by the user. Certain features might be available for an additional service-specific grace period after the end of the official support period and before the feature version is decommissioned. During this grace period, out-of-support versions of software components won't be patched or supported. However, software and documentation will continue to be available to allow users to upgrade to a supported version.
  3. GDC reserves the right to ask users to migrate to a newer feature or a minor version to mitigate the risk of critical security vulnerabilities that cannot be patched in older feature or minor versions. This is a rare occurrence, but sometimes, it is not feasible to apply security patches to old feature or minor versions of components, and it is important to take steps to protect user data and workloads.
  4. Security patches will be provided in accordance with the applicable service level objectives (SLOs) for both preview and general availability (GA) features. However, GDCservice level agreement (SLA) commitments are not applicable to preview features. SLAs only apply for GA features.
  5. Features that exists only in preview may be deprecated or removed without notice. Backward compatibility might not be maintained when features graduate from one preview release to another or different versions of the preview API. Preview feature releases will be shut down after their capabilities reach the stable channel.
  6. GDC releases (feature, minor, and patch versions) must be applied by Infrastructure Operators (IOs) to the deployment and associated organizations as soon as possible. The GDC release version is an internal version and is only visible to IOs.
    1. A new GDC feature or a minor version must be applied within 60 days of the release publication and, at the latest, by 120 days (grace period) unless otherwise directed by the GDC team. 
    2. A new GDC patch version must be applied as soon as possible, especially if the release version contains critical fixes necessary for security and compliance. GDC patch versions can be skipped to catch up with the latest version. However, the feature or minor versions cannot be skipped and every version must be applied. 
  7. Platform Administrators (PAs) are responsible for providing adequate maintenance windows (MW) for the organization or the platform, so that the operator and automation can apply upgrades and patches promptly.
  8. Infrastructure Operators (IOs) must upgrade to the latest patch version available for each feature or a minor version unless explicitly advised otherwise by GDC to avoid missing security and bug fixes.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
