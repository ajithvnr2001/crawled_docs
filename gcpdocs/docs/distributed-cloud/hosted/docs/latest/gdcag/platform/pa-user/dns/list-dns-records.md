---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/
title: List DNS records \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:18:15.879729+00:00
---

# List DNS records  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/#before-you-begin)
  * [List DNS records](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/#list-dns-records)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


Was this helpful?
Send feedback 
#  List DNS records Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/#before-you-begin)
  * [List DNS records](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/#list-dns-records)


This document guides you on how to list DNS records in a DNS zone in Google Distributed Cloud (GDC) air-gapped.
## Before you begin
To list DNS records in GDC, you must have the following:
  * The necessary identity and access roles. To list DNS records for your project, ask your **IAM Project Admin** to grant you the **Managed DNS Project Viewer** (`managed-dns-project-viewer`) role.
  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * If you are using `kubectl`, a kubeconfig file for the global API server. If you have not yet generated this file, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).


## List DNS records
You can list DNS records using the gdcloud CLI or the Kubernetes API.
[ gdcloud ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/#gdcloud)[ API ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records/#api) More
To list all DNS records in a project, use the [`gdcloud dns record-sets list`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-record-sets-list) command:

```
gdcloud dns record-sets list \
    --dns-zone=DNS_ZONE_NAME \
    [--project=PROJECT_NAMESPACE]

```

To fetch a single DNS record by name, use the [`gdcloud dns record-sets describe`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-record-sets-describe) command:

```
gdcloud dns record-sets describe RESOURCE_RECORD_NAME \
    [--dns-zone=DNS_ZONE_NAME] \
    [--project=PROJECT_NAMESPACE]

```

Replace the following:
  * `RESOURCE_RECORD_NAME`: the name of the DNS record to fetch.
  * `DNS_ZONE_NAME`: the name of the DNS zone containing the records (optional).
  * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.


Use the Kubernetes API in GDC to list DNS records.
To list a single record, run the following command:

```
kubectl --kubeconfig GLOBAL_API_SERVER get resourcerecordset.networking.global.gdc.goog RESOURCE_RECORD_NAME -n PROJECT_NAMESPACE

```

To list all DNS Records under a project, run the following command:

```
kubectl --kubeconfig GLOBAL_API_SERVER get resourcerecordset.networking.global.gdc.goog -n PROJECT_NAMESPACE

```

Replace the following:
  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) for details.
  * `RESOURCE_RECORD_NAME`: the DNS record to be listed such as `cname.system.example.com`.
  * `PROJECT_NAMESPACE`: the namespace of your project.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
