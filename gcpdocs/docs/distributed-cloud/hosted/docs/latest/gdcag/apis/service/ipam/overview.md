---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/
title: IP Address Management API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:06:43.087326+00:00
---

# IP Address Management API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdistributed-cloud%2Fhosted%2Fdocs%2Flatest%2Fgdcag%2Fapis%2Fservice%2Fipam%2Foverview%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Service endpoint and discovery document](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/#service-endpoint-discovery-document)
  * [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/#example-resource)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)


Was this helpful?
Send feedback 
#  IP Address Management API overview Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Service endpoint and discovery document](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/#service-endpoint-discovery-document)
  * [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview/#example-resource)


The IP Address Management (IPAM) API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM). It manages IP address allocation across a Google Distributed Cloud (GDC) air-gapped deployment.
To use the IPAM API, we recommend that you use the gdcloud CLI, or call the API directly using the `kubectl` CLI. If your application needs to use your own libraries to call this API, use the following examples and the full API definitions to build your requests:
  * [ipam.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/ipam-v1)
  * [ipam.global.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/global-ipam-v1)


## Service endpoint and discovery document
The IPAM APIs are provided in two packages depending on zonal deployment or global deployment.
The API endpoints for the zonal and global IPAM APIs are the following, respectively:
  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/ipam.gdc.goog/v1`
  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/ipam.global.gdc.goog/v1`


The `MANAGEMENT_API_SERVER_ENDPOINT` variable is the endpoint of the Management API server.
Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the IPAM API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. After that command is running, you can access the document at the following URLs:
  * `http://127.0.0.1:8001/apis/ipam.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/ipam.global.gdc.goog/v1`


## Example custom resources
The following is an example of a zonal `Subnet` object:

```
apiVersion: ipam.gdc.goog/v1
kind: Subnet
metadata:
  labels:
    ipam.gdc.goog/overlay-network-type: External
    ipam.gdc.goog/category-type: ExternalOverlayNetwork
  name: test-subnet
  namespace: root
spec:
  type: Root
  ipv4Request:
    cidr: 10.0.0.0/16
  networkSpec:
    staticVLANID: 100
    enableVLANID: true
    enableGateway: true

```

The following is an example of a global `Subnet` object for a default VPC root CIDR:

```
apiVersion: ipam.global.gdc.goog/v1
kind: Subnet
metadata:
  labels:
    ipam.gdc.goog/vpc: default-vpc
    ipam.gdc.goog/usage: network-root-range
  name: default-vpc-root-cidr
  namespace: platform
spec:
  ipv4Request:
    cidr: 10.200.0.0/23
  type: Root

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
