---
url: https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/
title: Defining runtime settings \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:42:59.522848+00:00
---

# Defining runtime settings  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/

[ Skip to main content ](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/)
  * [Deutsch](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=de)
  * [Español](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=es-419)
  * [Français](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=id)
  * [Italiano](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=it)
  * [Português](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=ja)
  * [한국어](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fappengine%2Fdocs%2Fstandard%2Fgo%2Fconfiguring-your-app-with-app-yaml%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/serverless-color.svg) ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [About app.yaml files](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/#intro)
  * [All configuration elements](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/#all_configuration_elements)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)


Was this helpful?
Send feedback 
#  Defining runtime settings Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [About app.yaml files](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/#intro)
  * [All configuration elements](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml/#all_configuration_elements)


An App Engine app is configured using an `app.yaml` file, that contains the runtime, handlers, scaling, and other general settings including environment variables. 
## About `app.yaml` files
You can specify the runtime configuration for your Go 1.12+ app, including versions and URLs, in the `app.yaml` file. This file acts as a deployment descriptor of a specific [service](https://docs.cloud.google.com/appengine/docs/standard/an-overview-of-app-engine) version. 
You must first create the `app.yaml` file for the `default` service of your app before you can create and deploy `app.yaml` files for additional services. 
Generally, your `app.yaml` file requires only the `runtime` element for a simple Go 1.12+ app in the standard environment, for example: 

```
runtime: go127

```

App Engine provides default values for all other settings, including the [F1 instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes), which determines the memory and CPU resources that are available to your app, and [automatic scaling](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#scaling_types), which controls how and when new instances of your app are created.
If you need to override the default settings, create an `app.yaml` file and specify the settings you need. For more information, see [`app.yaml` file reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml). 
You can specify a unique name for your `app.yaml` files, but then you must specify the file name with the [deployment command](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app) as well. For example, if you name your `app.yaml` file `service-name-app.yaml` or `app.standard.yaml`, then you must deploy your app using either:

```
gcloud app deploy service-name-app.yaml
gcloud app deploy app.standard.yaml

```
To learn more about structuring multiple services and `app.yaml` files in your app, see [Structuring web services](https://docs.cloud.google.com/appengine/docs/standard/configuration-files). 
## All configuration elements
For a complete list of all the supported elements in this configuration file, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
