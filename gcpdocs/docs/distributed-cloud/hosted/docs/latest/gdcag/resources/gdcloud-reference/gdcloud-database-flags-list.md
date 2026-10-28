---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/
title: gdcloud database flags list \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:17:43.770612+00:00
---

# gdcloud database flags list  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-flags-list/?hl=ko)


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


Send feedback 
#  gdcloud database flags list Stay organized with collections  Save and categorize content based on your preferences.
## NAME
gdcloud database flags list - List all database flags for the specified database version.
## SYNOPSIS

```
gdcloud database flags list [flags]

```

### EXAMPLES

```
To list all available database flags for a database version, run:

  gdcloud database flags list --database-version=POSTGRESQL_14


```

### REQUIRED FLAGS

```
      --database-version string   Database version of the database for which to list the flags.

```

### OPTIONAL FLAGS

```
      --zone string   Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.

```

### GDCLOUD WIDE FLAGS
These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.
For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
