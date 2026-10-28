---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/
title: Cassandra logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:03:58.648714+00:00
---

# Cassandra logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [ Use the logs command ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/#use-the-logs-command)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Send feedback 
#  Cassandra logs Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [ Use the logs command ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs/#use-the-logs-command)


Version 1.17 (latest)keyboard_arrow_down
Supported versions:
  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-logs.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-logs.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-logs.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-logs.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)
Unsupported versions:
  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-logs.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-logs.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-logs.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-logs.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-logs.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-logs.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cassandra-logs.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cassandra-logs.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cassandra-logs.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-logs.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cassandra-logs.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cassandra-logs.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cassandra-logs.html)


Use the Cassandra logs to help diagnose problems with the `cassandra` pods.
Logs are a good way to troubleshoot problems with your installation. See also [Logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging). 
##  Use the logs command 
You can view Cassandra logs using the kubectl logs command. For example: 

```
kubectl logs apigee-cassandra-default-0 -n APIGEE_NAMESPACE
```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
