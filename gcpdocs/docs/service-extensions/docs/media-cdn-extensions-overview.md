---
url: https://docs.cloud.google.com/service-extensions/docs/media-cdn-extensions-overview/
title: Media CDN extensions overview \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:25:11.999398+00:00
---

# Media CDN extensions overview  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/media-cdn-extensions-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Media CDN extensions overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Service Extensions lets you use extensions to insert custom code in the [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview) processing path. This page provides an overview about Media CDN extensions.

Media CDN provides many built-in core capabilities to address the most common use cases for content delivery networks (CDNs). You might have requirements beyond these capabilities. For example, you might need to normalize headers to improve caching, use a custom URL signing algorithm, or port legacy behavior from an existing CDN to Media CDN.

You can use edge extensions (`CdnEdgeExtension`) to run WebAssembly (Wasm) [plugins](https://docs.cloud.google.com/service-extensions/docs/plugins-overview) directly at the Google edge network in front of the cache in the Media CDN processing path.

A `CdnEdgeExtension` resource attaches directly to an `EdgeCacheService` deployment and runs one or more ordered extension chains (`extensionChains`). Each extension chain defines Common Expression Language (CEL) match conditions (`matchCondition.celExpression`) to selectively evaluate requests based on hostnames, URL paths, query parameters, or HTTP request headers.

Plugins can access and manipulate both HTTP request headers and response headers, influence cache key generation, validate custom authorization tokens or URL signatures, and serve synthetic responses. For more information, see Figure 1.

[ ![Media CDN edge extensions use plugins to add custom
     code to the processing path.](https://docs.cloud.google.com/static/service-extensions/images/plugins-processing-path.svg)](https://docs.cloud.google.com/static/service-extensions/images/plugins-processing-path.svg) **Figure 1.** Media CDN edge extensions use plugins to add custom code to the processing path (click to enlarge). **Important:** To request access to Media CDN, contact your Google Cloud sales representative or your account team.

## How Media CDN edge extensions work

When a client request reaches an `EdgeCacheService` that's extended by an edge extension, the extension runs in the following sequence:

  1. **Match condition evaluation** : Media CDN extracts request attributes and evaluates the ordered `extensionChains` defined in the `CdnEdgeExtension`. The first chain whose CEL expression evaluates to `true` runs, and all subsequent chains are skipped.

  2. **Plugin request header processing (`REQUEST_HEADERS`)**: your configured plugins run sequentially. You can chain a maximum of two plugins within a single extension chain. Plugins can inspect forwarded HTTP headers and Envoy attributes, add or rewrite request headers, or return a direct synthetic response to the client.

  3. **Route matching and origin selection** : Media CDN evaluates route rules and then selects the target origin based on the request, including any request headers or URL paths that the plugins modified.

  4. **Cache lookup and origin fetch** : Media CDN evaluates cache keys (which can incorporate request headers or URL paths that the plugins modified), checks edge cache storage, and serves content when a cache hit occurs or fetches content from the selected origin when a cache miss occurs.

  5. **Plugin response header processing (`RESPONSE_HEADERS`)**: after content is retrieved from either the cache or the origin, your configured plugins run sequentially. Then, the modified response headers are delivered to the downstream client.

  6. **Delivery to client** : the final response headers and body are delivered to the client.


**Note:** Media CDN edge extensions support both `REQUEST_HEADERS` and `RESPONSE_HEADERS` processing events. Media CDN doesn't support callouts (gRPC `ext_proc`), HTTP body callbacks, or HTTP trailer processing.

## What's next

  * [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin)
  * [Configure a Media CDN edge extension](https://docs.cloud.google.com/service-extensions/docs/configure-media-cdn-edge-extensions)
  * [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
