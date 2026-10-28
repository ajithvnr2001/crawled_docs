---
url: https://docs.cloud.google.com/functions/docs/securing/function-identity/
title: Function Identity \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:14:28.884821+00:00
---

# Function Identity  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/securing/function-identity/

[ Skip to main content ](https://docs.cloud.google.com/functions/docs/securing/function-identity/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/functions/docs/securing/function-identity/)
  * [Deutsch](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=de)
  * [Español](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=es-419)
  * [Français](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=id)
  * [Italiano](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=it)
  * [Português](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=ja)
  * [한국어](https://docs.cloud.google.com/functions/docs/securing/function-identity/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/run-color.svg) ](https://docs.cloud.google.com/functions/docs)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Add a user-managed service account at deployment](https://docs.cloud.google.com/functions/docs/securing/function-identity/#add-user-managed-sa)
  * [Update the service account of an existing function](https://docs.cloud.google.com/functions/docs/securing/function-identity/#update-sa)


If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)


Send feedback 
  * On this page
  * [Add a user-managed service account at deployment](https://docs.cloud.google.com/functions/docs/securing/function-identity/#add-user-managed-sa)
  * [Update the service account of an existing function](https://docs.cloud.google.com/functions/docs/securing/function-identity/#update-sa)


# Function Identity Stay organized with collections  Save and categorize content based on your preferences.
This page provides supplemental information for configuring function identity for functions created using the [`gcloud functions`](https://docs.cloud.google.com/sdk/gcloud/reference/functions) commands or the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest).
If you've created or deployed functions using Cloud Run, see [Introduction to service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) and [Configure service identity for services](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) for a detailed description of configuring service identity. Cloud Run refers to the function identity as the _service identity_. 
For an introduction to the function identity concept, see the Cloud Run [Introduction to service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) guide.
## Add a user-managed service account at deployment
When deploying a function using `gcloud functions deploy`, add the `--service-account` flag. For example:

```
gcloud functions deploy FUNCTION_NAME --service-account SERVICE_ACCOUNT_EMAIL
```

Replace `FUNCTION_NAME` with your function name, and `SERVICE_ACCOUNT_EMAIL` with the service account email.
## Update the service account of an existing function
You can update the runtime service account of an existing function.
When deploying a function using `gcloud functions deploy`, add the `--service-account` flag:

```
gcloud functions deploy FUNCTION_NAME --service-account SERVICE_ACCOUNT_EMAIL
```

Replace `FUNCTION_NAME` with your function name, and `SERVICE_ACCOUNT_EMAIL` with the service account.
The redeployed function now uses the new runtime service account.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
