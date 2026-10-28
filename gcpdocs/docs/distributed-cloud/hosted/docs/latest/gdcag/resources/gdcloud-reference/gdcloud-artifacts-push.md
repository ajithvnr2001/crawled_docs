---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/
title: gdcloud artifacts push \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:29:59.542781+00:00
---

# gdcloud artifacts push  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-push/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdistributed-cloud%2Fhosted%2Fdocs%2Flatest%2Fgdcag%2Fresources%2Fgdcloud-reference%2Fgdcloud-artifacts-push%2F&prompt=select_account)
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
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)


Was this helpful?
Send feedback 
#  gdcloud artifacts push Stay organized with collections  Save and categorize content based on your preferences.
## NAME
gdcloud artifacts push - Push OCI packages to a registry.
## SYNOPSIS

```
gdcloud artifacts push SOURCE DESTINATION [flags]

```

### EXAMPLES

```
To push a OCI packages to a registry, run:

            gdcloud artifacts push SOURCE DESTINATION

        To push a single manifest of the repository to the registry, run:

            gdcloud artifacts push SOURCE DESTINATION --single-manifest-repo

        To push OCI packages to a registry without adhering to TLS protocols, run:

            gdcloud artifacts push SOURCE DESTINATION --insecure

        The SOURCE path must point to a directory containing the OCI bundle.
        The DESTINATION is a reference of a remote OCI image. For example, gcr.io/cloud-marketplace/google/nginx:1.25.
        This command writes the extracted image to the output path specified in SOURCE. This output path must point to an empty directory.

```

### OPTIONAL FLAGS

```
      --ca-cert-path string    Absolute file path to the user-provided CA certificate file that is used to push a manifest over a HTTPS connection.
      --insecure               Allow pushing to the registry, and establish a connection to the server, even for server connections otherwise considered insecure.
      --single-manifest-repo   Tag and push the single manifest of the repository, as opposed to the image index, to the registry.

```

### GDCLOUD WIDE FLAGS
These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.
For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
