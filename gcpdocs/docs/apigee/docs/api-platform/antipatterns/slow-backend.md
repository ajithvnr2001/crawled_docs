---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/
title: Antipattern: Allow a slow backend \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:02:57.028086+00:00
---

# Antipattern: Allow a slow backend  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Antipattern](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#antipattern)
    * [Inadequately sized backend](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#inad)
    * [Slow backend](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#slow)
  * [Impact](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#impact)
  * [Best practice](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#best-practice)
  * [Further reading](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#further-reading)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)


Send feedback 
#  Antipattern: Allow a slow backend Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Antipattern](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#antipattern)
    * [Inadequately sized backend](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#inad)
    * [Slow backend](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#slow)
  * [Impact](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#impact)
  * [Best practice](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#best-practice)
  * [Further reading](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#further-reading)


_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/slow-backend) documentation._
Backend systems run the services that API proxies access. In other words, they are the fundamental reason for the very existence of APIs and the API Management Proxy layer.
Any API request that is routed via the Apigee platform traverses a typical path before it hits the backend: 
  * The request originates from a client which could be anything from a browser to an app.
  * The request is then received by the Apigee gateway.
  * It is processed within the gateway. As a part of this processing, the request passes onto a number of distributed components.
  * The gateway then routes the request to the backend that responds to the request.
  * The response from the backend then traverses back the exact reverse path via the Apigee gateway back to the client.


![TBD](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/antipatterns/client-edge-backend.png)
In effect, the performance of API requests routed via Apigee is dependent on both Apigee and the backend systems. In this antipattern, we will focus on the impact on API requests due to badly performing backend systems.
## Antipattern
Let us consider the case of a problematic backend. These are the possibilities:
* [Inadequately sized backend](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#slow)
* [Slow backend](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend/#inad)
### Inadequately sized backend
The challenge in exposing the services on these backend systems via APIs is that they are accessible to a large number of end users. From a business perspective, this is a desirable challenge, but something that needs to be dealt with.
Many times backend systems are not prepared for this extra demand on their services and are consequently under sized or are not tuned for efficient response.
The problem with an "inadequately sized" backend is that if there is a spike in API requests, then it will stress the resources like CPU, Load and Memory on the backend systems. This would eventually cause API requests to fail.
### Slow backend
The problem with an improperly tuned backend is that it would be very slow to respond to any requests coming to it, thereby leading to increased latencies, premature timeouts and a compromised customer experience.
The Apigee platform offers a few tunable options to circumvent and manage the slow backend. But these options have limitations.
## Impact
  * In the case of an inadequately sized backend, increase in traffic could lead to failed requests.
  * In the case of a slow backend, the latency of requests will increase.


## Best practice
  * Use caching to store the responses to improve the API response times and reduce the load on the backend server.
  * Resolve the underlying problem in the slow backend servers.


## Further reading
  * [Apigee caching internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
