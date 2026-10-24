---
url: https://docs.cloud.google.com/service-extensions/docs/configure-media-cdn-edge-extensions/
title: Configure a Media CDN edge extension \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T05:41:22.067949+00:00
---

# Configure a Media CDN edge extension  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/configure-media-cdn-edge-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Configure a Media CDN edge extension Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure Media CDN edge extensions (`CdnEdgeExtension`) to attach WebAssembly (Wasm) plugins to [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview) Edge Cache Services (`EdgeCacheService`).

A `CdnEdgeExtension` resource attaches directly to an `EdgeCacheService` deployment and runs one or more ordered extension chains (`extensionChains`). Each extension chain is matched by using Common Expression Language (CEL) expressions and can contain a maximum of two chained `WasmPlugin` resources.

For more information, see [Media CDN extensions overview](https://docs.cloud.google.com/service-extensions/docs/media-cdn-extensions-overview).

## Before you begin

  1. [Create a Media CDN origin](https://docs.cloud.google.com/media-cdn/docs/quickstart#create-origin)
  2. [Create a Media CDN service](https://docs.cloud.google.com/media-cdn/docs/quickstart#create-service)
  3. [Create a plugin by using Service Extensions](https://docs.cloud.google.com/service-extensions/docs/create-plugin)

  4. When configuring a `CdnEdgeExtension` resource, consider that Media CDN edge extensions run _before_ most Media CDN features, including route matching and cache lookup. This lets a plugin rewrite headers or URLs to influence HTTP routing. However, plugin code can't inspect custom headers that Media CDN route rules add or built-in features. To access client and connection properties, such as client region, IP address, or TLS parameters, configure [forward attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).




## Set up the Media CDN edge extension

To configure a `CdnEdgeExtension` resource and attach plugins to an `EdgeCacheService` deployment, do the following:

  1. Define the `CdnEdgeExtension` resource in a YAML file.

The following example invokes `WASM_PLUGIN` to process both request and response headers when you send a request to `media.example.com`.

**Note** : The `failOpen: false` setting returns an HTTP `500` error code if the plugin fails or times out.
         
         cat >cdn-edge-extension.yaml <<EOF
         edgeCacheServices:
         - projects/PROJECT_ID/locations/global/edgeCacheServices/SERVICE_NAME
         extensionChains:
         - name: "edge-plugin-chain"
           matchCondition:
             celExpression: 'request.host == "media.example.com"'
           extensions:
           - name: "auth-and-header-plugin"
             service: projects/PROJECT_ID/locations/global/wasmPlugins/WASM_PLUGIN
             failOpen: false
             supportedEvents:
             - REQUEST_HEADERS
             - RESPONSE_HEADERS
             forwardAttributes:
             - request.method
             - request.host
             - request.path
             - source.client_region
         EOF
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `SERVICE_NAME`: name of the target `Media CDN` service (`EdgeCacheService`)
     * `WASM_PLUGIN`: name of your plugin, such as `my-wasm-plugin-resource`

For more information about the fields in the YAML file, see [ExtensionChain](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/ExtensionChain) in the API documentation.

  2. Use the `gcloud beta service-extensions cdn-edge-extensions import` command to import the `CdnEdgeExtension` resource:
         
         gcloud beta service-extensions cdn-edge-extensions import cdn-edge-ext \
            --source=cdn-edge-extension.yaml \
            --location=global
         

**Note** : It might take some time for the new plugin configuration to be distributed across all locations.




## Limitations

  * You can attach only one edge extension to an `EdgeCacheService` deployment.
  * An edge extension chain can contain a maximum of two plugins.
  * Media CDN edge extensions support `REQUEST_HEADERS` and `RESPONSE_HEADERS` events. These extensions don't support HTTP body or trailer processing.
  * Media CDN edge extensions let you use only one regular expression for each CEL expression.
  * Names of extension chains and extensions must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034). Under this specification, names can contain up to 63 lowercase alphanumeric characters or hyphens, must start with a letter, and must end with a letter or number.



For more information about resource limits, see [Quotas and limits](https://docs.cloud.google.com/service-extensions/docs/quotas).

## What's next

  * [View plugin log messages](https://docs.cloud.google.com/service-extensions/docs/monitor-media-cdn-plugins#logging)
  * [Monitor plugin performance](https://docs.cloud.google.com/service-extensions/docs/monitor-media-cdn-plugins#monitoring)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
