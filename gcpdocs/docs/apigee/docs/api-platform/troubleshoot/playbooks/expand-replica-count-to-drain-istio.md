---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/
title: Expand Istio property replica counts to avoid problems when draining Istio nodes \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:02:29.903431+00:00
---

# Expand Istio property replica counts to avoid problems when draining Istio nodes  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)


Send feedback 
#  Expand Istio property replica counts to avoid problems when draining Istio nodes Stay organized with collections  Save and categorize content based on your preferences.
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
When draining Istio pods some nodes may not drain because they have a replica count of `1`, while `3` or more replicas are required. In order to avoid this, you should set the minimum replica count for each property to at least `3`. 
When backing up and draining Istio nodes you may see errors like: 

```
kubectl drain` failed to evict and reschedule pods to another node due to PodDisruptionBudget definitions:
===
NAMESPACE NAME MIN AVAILABLE MAX UNAVAILABLE ALLOWED DISRUPTIONS AGE
istio-system istio-ingressgateway 1 N/A 2 5d11h
istio-system istio-pilot 1 N/A 2 5d11h
===
```

For `istio-ingressgateway` and `istio-pilot` you can set the `istio.ingressgateway.replicaCountMin` and `istio.pilot.replicaCountMin` properties to **`3`**or higher. See the[ Configuration properties reference, `istio`](https://docs.cloud.google.com/apigee/docs/hybrid/latest/config-prop-ref#istio). 
For other `istio` components (that don't have a `replicaCountMin` property), see [ Manually upgrading a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) in the GKE documentation or [ IstioOperator Options](https://istio.io/latest/docs/reference/config/istio.operator.v1alpha1/) in the Istio documentation. 
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
