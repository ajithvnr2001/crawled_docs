---
url: https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/
title: Troubleshoot Helm chart issues \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:42:38.912924+00:00
---

# Troubleshoot Helm chart issues  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/

. [ Skip to main content ](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/)
  * [Deutsch](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=de)
  * [Español](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=es-419)
  * [Français](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=id)
  * [Italiano](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=it)
  * [Português](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=ja)
  * [한국어](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Helm commands no longer work in Helm 3.7](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/#helm37)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)


Was this helpful?
Send feedback 
#  Troubleshoot Helm chart issues Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Helm commands no longer work in Helm 3.7](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot/#helm37)


Learn about troubleshooting steps that you might find helpful if you run into problems managing Helm charts in Artifact Registry.
### Helm commands no longer work in Helm 3.7
[Helm 3.7.0](https://github.com/helm/helm/releases/tag/v3.7.0) introduced changes to OCI support that are not backwards-compatible, including changed and removed commands for working with registries.
Run `helm version` to check your Helm version.
[Install Helm 3.8.0 or later](https://helm.sh/docs/intro/install/) to use Helm charts with Artifact Registry. In previous versions of Helm, OCI support is experimental.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
