---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/
title: Wipe out KMS keys \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:17:53.318966+00:00
---

# Wipe out KMS keys  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#before-you-begin)
    * [Request IAM roles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#request-iam-roles)
    * [Prepare your environment](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#prepare-environment)
  * [Delete all keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#delete-keys)
    * [Delete all zonal keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#delete-zonal-keys)
    * [Delete all multi-zone keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#delete-multi-zone-keys)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


Send feedback 
#  Wipe out KMS keys Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#before-you-begin)
    * [Request IAM roles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#request-iam-roles)
    * [Prepare your environment](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#prepare-environment)
  * [Delete all keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#delete-keys)
    * [Delete all zonal keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#delete-zonal-keys)
    * [Delete all multi-zone keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/key-systems/#delete-multi-zone-keys)


The Platform Administrator (PA) can delete Key Management System (KMS) keys in the Management API server.
The PA can delete the AEAD and Signing keys in the project namespace. See [Supported keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/kms) for the full list of KMS keys.
## Before you begin
Before deleting KMS keys, you must request the necessary permissions and prepare your environment.
### Request IAM roles
Contact your IAM Org Admin to request the following roles:
  * **KMS Admin** (`kms-admin`): create, update, delete, and use KMS keys in your project namespace.
  * **Global MZAEADKey Deleter** (`global-mzaeadkey-deleter`): delete multi-zone `AEAD` keys in your project namespace.


### Prepare your environment
  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.
  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).
  * Generate the necessary kubeconfig files. You need the path to the relevant kubeconfig file to use with the `kubectl` commands.
    * To delete zonal keys, [generate the kubeconfig file for the management API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).
    * To delete multi-zone keys, [generate the kubeconfig file for the global API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).


## Delete all keys
You can delete zonal keys from the management API server or multi-zone keys from the global API server.
### Delete all zonal keys
To delete all zonal keys in a project namespace, use the following command:

```
kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
  delete KEY_PRIMITIVE --namespace=PROJECT --all

```

Replace the following:
  * MANAGEMENT_API_SERVER_KUBECONFIG: the kubeconfig file of the management API server.
  * KEY_PRIMITIVE: the key you want to delete. For example: `aeadkey` for the `AEAD` key.
  * PROJECT: the name of the project. For example: `kms-test1`.


### Delete all multi-zone keys
To delete all multi-zone keys in a project namespace, use the following command:

```
kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG \
  delete mzaeadkey --namespace=PROJECT --all

```

Replace the following:
  * GLOBAL_API_SERVER_KUBECONFIG: the kubeconfig file of the global API server.
  * PROJECT: the name of the project. For example: `kms-test1`.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
