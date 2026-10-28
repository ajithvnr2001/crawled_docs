---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/
title: Getting started \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:54:31.610666+00:00
---

# Getting started  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [ Overview ](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/#overview)
  * [ Download and install ](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/#download-and-install)
  * [ Next steps ](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/#next-steps)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Send feedback 
#  Getting started Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [ Overview ](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/#overview)
  * [ Download and install ](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/#download-and-install)
  * [ Next steps ](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started/#next-steps)


_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
This topic explains how to download and install Apigee Adapter for Envoy. 
##  Overview 
In the following steps, you will download and set up two applications on your system: the **Apigee Remote Service CLI** and the **Apigee Remote Service for Envoy**. 
##  Download and install 
  1. Create a base directory on your system in which to install the Remote Service CLI and the Remote Service. For example: 
```
mkdir ~/envoy-adapter
cd ~/envoy-adapter
export ENVOY_HOME=$PWD
```

  2. For the remaining steps, be sure you are in the `$ENVOY_HOME` directory: 
```
cd $ENVOY_HOME
```

  3. Download the [ latest release](https://github.com/apigee/apigee-remote-service-cli/releases) of the **Apigee Remote Service CLI** into `$ENVOY_HOME`. Be sure to grab the correct package for your operating system. 
  4. Download the [ latest release](https://github.com/apigee/apigee-remote-service-envoy/releases) of the **Apigee Remote Service for Envoy** into `$ENVOY_HOME`. 
  5. Create directories to hold the extracted package contents inside `$ENVOY_HOME`: 
```
mkdir apigee-remote-service-cli
mkdir apigee-remote-service-envoy
```

  6. Extract the tar file contents into the new directories: 
```
tar -xf apigee-remote-service-cli_version_platform.tar.gz -C apigee-remote-service-cli
tar -xf apigee-remote-service-envoy_version_platform.tar.gz -C apigee-remote-service-envoy
```

  7. Delete the tar files.
  8. When you complete these steps, `$ENVOY_HOME` contains two directories: 
```
ls -1 .
  apigee-remote-service-cli
  apigee-remote-service-envoy
```

  9. Create the following environment variables for the `apigee-remote-service-cli` and `apigee-remote-service-envoy` directories. You will use these environment variables throughout the documentation: 
```
export CLI_HOME=$PWD/apigee-remote-service-cli
export REMOTE_SERVICE_HOME=$PWD/apigee-remote-service-envoy
```



##  Next steps 
You are now ready to set up and use the Apigee Adapter for Envoy to proxy API calls with Apigee API management. The following examples show you how to use the adapter with Apigee hybrid and Apigee for Public Cloud:   
| Example  | Description  |  
| --- | --- |  
| [Istio sidecar with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/example-hybrid)  | Deploy the Remote Service into an Istio service mesh. The remote service provides the endpoints to the Istio sidecar proxies that are installed on your target services. This steup lets you use the Apigee Adapter for Envoy with an Apigee hybrid installation.  |  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
