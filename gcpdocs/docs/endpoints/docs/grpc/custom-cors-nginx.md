---
url: https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/
title: Creating a Custom nginx.conf to Support CORS \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:01:10.041205+00:00
---

# Creating a Custom nginx.conf to Support CORS  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/

[ Skip to main content ](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/)
  * [Deutsch](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=de)
  * [Español](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=es-419)
  * [Français](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=id)
  * [Italiano](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=it)
  * [Português](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=ja)
  * [한국어](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Adding the CORS options to nginx.conf](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/#adding_the_cors_options_to_nginxconf)
  * [What's next](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)


Was this helpful?
Send feedback 
#  Creating a Custom nginx.conf to Support CORS Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Adding the CORS options to nginx.conf](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/#adding_the_cors_options_to_nginxconf)
  * [What's next](https://docs.cloud.google.com/endpoints/docs/grpc/custom-cors-nginx/#whats_next)


[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/custom-cors-nginx) | gRPC
As described in [Adding CORS support to ESP](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options#adding_cors_support_to_esp), you can configure the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) to support CORS. If the ESP options don't provide the CORS support that your application requires, you can add the CORS options to ESP's configuration file, `nginx.conf`.
## Adding the CORS options to `nginx.conf`
To add the CORS options:
  1. Start with a `nginx.conf` file that contains the configuration required by Cloud Endpoints. You can start with the [sample `nginx.conf`](https://github.com/GoogleCloudPlatform/endpoints-samples/blob/master/k8s/nginx.conf), or if you have already deployed ESP, you can SSH to the ESP container and copy the `nginx.conf` file from the `/etc/nginx/endpoints/` directory.
  2. Add the CORS options that your application requires to `nginx.conf`. You can use the [CORS on NGINX](https://enable-cors.org/server_nginx.html) example as a starting point.
  3. Start ESP with the `--nginx_config` option with the path to the custom `nginx.conf` file.


## What's next
  * Learn about [ESP's startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options).
  * Learn how to [SSH to ESP's container on GKE](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment#checking_configuration_files).
  * Learn about [using a custom nginx.conf on GKE ](https://docs.cloud.google.com/endpoints/docs/grpc/custom-nginx).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
