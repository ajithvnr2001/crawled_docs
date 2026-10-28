---
url: https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/
title: Enabling an API in your Google Cloud project \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:49:46.696069+00:00
---

# Enabling an API in your Google Cloud project  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/

[ Skip to main content ](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/)
  * [Deutsch](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=de)
  * [Español](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=es-419)
  * [Français](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=id)
  * [Italiano](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=it)
  * [Português](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=ja)
  * [한국어](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/#before_you_begin)
  * [Enabling an API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/#enabling_an_api)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)


Send feedback 
#  Enabling an API in your Google Cloud project Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/#before_you_begin)
  * [Enabling an API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/#enabling_an_api)


OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/enable-api)
When an API requires an API key and the API is associated with a Google Cloud project that you don't have access to, you have the following options to obtain an API key:
  * **Option 1** : Ask a security admin to create an API key for you.
  * **Option 2** : Ask a security admin to [grant you access to the project](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access) so that you can create an API key in the same project that the API is associated with.
  * **Option 3** : Ask a security admin to [grant you access to enable the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-callers) in your own Google Cloud project so that you can create an API key.


## Before you begin
[Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
## Enabling an API
If you used option 3 and asked someone to grant you access to enable the API, follow the steps below to enable the API in your own Google Cloud project.
To enable an API:
[Console](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/#console)[gcloud](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api/#gcloud) More
  1. In the Google Cloud console, go to APIs & services for your project. 
[Go to APIs & Services](https://console.cloud.google.com/apis)
  2. On the **Library** page, click **Private APIs**. If you don't see the API listed, that means you haven't been granted access to enable the API.
  3. Click the API you want to enable. If you need help finding the API, use the search field.
  4. In the page that displays information about the API, click **Enable**.


  1. Enter the following to display the project IDs for your Google Cloud projects:

```
gcloud projects list

```

  2. Using the applicable project ID from the previous step, set the default project to the one in which you want to enable the API:

```
gcloud config set project YOUR_PROJECT_ID

```

  3. Get a list of services that you can enable in your project:

```
gcloud services list --available

```

If you don't see the API listed, that means you haven't been granted access to enable the API.
  4. Using the applicable service name from the previous step, enable the service:

```
gcloud services enable SERVICE_NAME

```



For more information on the preceding commands, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference).
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
