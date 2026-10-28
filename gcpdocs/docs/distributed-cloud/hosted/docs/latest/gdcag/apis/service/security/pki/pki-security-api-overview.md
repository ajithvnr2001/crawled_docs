---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/
title: PKI Security API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:07:55.255754+00:00
---

# PKI Security API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdistributed-cloud%2Fhosted%2Fdocs%2Flatest%2Fgdcag%2Fapis%2Fservice%2Fsecurity%2Fpki%2Fpki-security-api-overview%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Service endpoint and discovery document](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/#service-endpoint-discover-doc)
  * [Example PKI BYO certificate issuer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/#example-byo-cert)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)


Was this helpful?
Send feedback 
#  PKI Security API overview Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Service endpoint and discovery document](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/#service-endpoint-discover-doc)
  * [Example PKI BYO certificate issuer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/pki-security-api-overview/#example-byo-cert)


The PKI Security API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM). It is used to manage and configure web certificates to secure web endpoints in your Google Distributed Cloud (GDC) air-gapped environment.
## Service endpoint and discovery document
The API endpoint for the PKI Security API is `https://GDC_API_SERVER_ENDPOINT/apis/pki.security.gdc.goog/v1` where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.
Using the `kubectl proxy` command, you can access the API endpoint URLs in your browser or with a tool such as `curl` to get the discovery document for the PKI Security API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. After that command is running, you can access the document at the following URL: `http://127.0.0.1:8001/apis/pki.security.gdc.goog/v1`.
## Example PKI BYO certificate issuer
The following is an example of a PKI Security bring-your-own (BYO) certificate issuer:

```
apiVersion: pki.security.gdc.goog/v1
kind: CertificateIssuer
metadata:
  name: byo-cert-issuer
  namespace: pki-system
  labels:
    pki.security.gdc.goog/is-default-issuer: "true"
spec:
  byoCertConfig:
    fallbackCertificateAuthority:
      name: default-web-tls-ca
      namespace: pki-system

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
