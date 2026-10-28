---
url: https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/
title: Reading and writing temporary files \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:42:08.039888+00:00
---

# Reading and writing temporary files  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/

[ Skip to main content ](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?tab=python#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/)
  * [Deutsch](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=de)
  * [Español](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=es-419)
  * [Français](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=id)
  * [Italiano](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=it)
  * [Português](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=ja)
  * [한국어](https://docs.cloud.google.com/appengine/docs/standard/using-temp-files/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fappengine%2Fdocs%2Fstandard%2Fusing-temp-files%2F%3Ftab%3Dpython&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/serverless-color.svg) ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)


Was this helpful?
Send feedback 
#  Reading and writing temporary files Stay organized with collections  Save and categorize content based on your preferences.
Go Java Node.js PHP Python Ruby
While [Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage) is the recommended solution for reading and writing files in App Engine, if your app only needs to write temporary files, you can use language-specific methods to write files to a directory named `/tmp`.
All files in this directory are stored in the instance's RAM, therefore writing to `/tmp` takes up system memory. In addition, files in the `/tmp` directory are only available to the app instance that created the files. When the instance is deleted, the temporary files are deleted.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
