---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/
title: KRM API aiplatform.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:06:20.854118+00:00
---

# KRM API aiplatform.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdistributed-cloud%2Fhosted%2Fdocs%2Flatest%2Fappliance%2Fapis%2Fservice%2Fvertex-ai%2Fvertex-ai-pretrained-api%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#overview)
  * [aiplatform.gdc.goog/v1](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#aiplatformgdcgoogv1)
    * [Application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#application)
    * [ApplicationStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#applicationstatus)
    * [Package](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#package)
    * [PackageList](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagelist)
    * [PackageSpec](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagespec)
    * [PackageStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagestatus)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)


Was this helpful?
Send feedback 
#  KRM API aiplatform.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#overview)
  * [aiplatform.gdc.goog/v1](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#aiplatformgdcgoogv1)
    * [Application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#application)
    * [ApplicationStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#applicationstatus)
    * [Package](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#package)
    * [PackageList](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagelist)
    * [PackageSpec](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagespec)
    * [PackageStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagestatus)


## Overview
The pre-trained APIs are a collection of AI services that include Optical Character Recognition (OCR), Speech-to-Text, and Translation. The services are enabled and disabled using the Kubernetes Resource Model (KRM) API. The KRM API is a management API that is optionally used by the AI Platform Admin.
## aiplatform.gdc.goog/v1
Package v1 contains API Schema definitions for the aiplatform.gdc.goog v1 API group
### Application
Application defines the type of AI Application
_Appears in:_ - [ApplicationStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#applicationstatus) - [PackageSpec](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagespec)  
| Field  | Description  |  
| --- | --- |  
|  `name` _ApplicationName_  |   |  
|  `path` _string_  | path of Application helm in harbor  |  
### ApplicationStatus
ApplicationStatus keeps track of each application thats is deployed
_Appears in:_ - [PackageStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagestatus)  
| Field  | Description  |  
| --- | --- |  
|  `application` _[Application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#application)_  |   |  
|  `deployed` _boolean_  | Indicates if application is deployed successfully  |  
|  `messages` _string array_  | Hold the messages if any  |  
### Package
Package is the Schema for the packages API
_Appears in:_ - [PackageList](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagelist)  
| Field  | Description  |  
| --- | --- |  
|  `apiVersion` _string_  | `aiplatform.gdc.goog/v1`  |  
|  `kind` _string_  | `Package`  |  
|  `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_  | Refer to Kubernetes API documentation for fields of `metadata`.  |  
|  `spec` _[PackageSpec](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagespec)_  |   |  
|  `status` _[PackageStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#packagestatus)_  |   |  
### PackageList
PackageList contains a list of Packages  
| Field  | Description  |  
| --- | --- |  
|  `apiVersion` _string_  | `aiplatform.gdc.goog/v1`  |  
|  `kind` _string_  | `PackageList`  |  
|  `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_  | Refer to Kubernetes API documentation for fields of `metadata`.  |  
|  `items` _[Package](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#package) array_  |   |  
### PackageSpec
PackageSpec defines the desired state of Package
_Appears in:_ - [Package](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#package)  
| Field  | Description  |  
| --- | --- |  
|  `applications` _[Application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#application) array_  | applications list ex. ocr  |  
### PackageStatus
PackageStatus defines the observed state of Package
_Appears in:_ - [Package](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#package)  
| Field  | Description  |  
| --- | --- |  
|  `observedGeneration` _integer_  | The generation observed by the application controller.  |  
|  `applicationStatuses` _object (keys:ApplicationName, values:[ApplicationStatus](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/vertex-ai-pretrained-api/#applicationstatus))_  | The status of deployed applications  |  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
