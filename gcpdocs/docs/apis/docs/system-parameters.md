---
url: https://docs.cloud.google.com/apis/docs/system-parameters/
title: System parameters \u00a0|\u00a0 Cloud APIs \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:48:19.812717+00:00
---

# System parameters  |  Cloud APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/system-parameters/

[ Skip to main content ](https://docs.cloud.google.com/apis/docs/system-parameters/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apis/docs/system-parameters/)
  * [Deutsch](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=de)
  * [Español](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=it)
  * [Português](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apis/docs/system-parameters/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/developer-tools-color.svg) ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [HTTP mapping](https://docs.cloud.google.com/apis/docs/system-parameters/#http_mapping)
  * [gRPC mapping](https://docs.cloud.google.com/apis/docs/system-parameters/#grpc_mapping)
  * [Definitions](https://docs.cloud.google.com/apis/docs/system-parameters/#definitions)
  * [Changelog](https://docs.cloud.google.com/apis/docs/system-parameters/#changelog)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)


Send feedback 
#  System parameters Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP mapping](https://docs.cloud.google.com/apis/docs/system-parameters/#http_mapping)
  * [gRPC mapping](https://docs.cloud.google.com/apis/docs/system-parameters/#grpc_mapping)
  * [Definitions](https://docs.cloud.google.com/apis/docs/system-parameters/#definitions)
  * [Changelog](https://docs.cloud.google.com/apis/docs/system-parameters/#changelog)


Google's API platform defines _system parameters_ to control common functionality across REST and gRPC APIs, such as API keys, response field masks, quota attribution, and JSON formatting. Depending on the protocol, you pass system parameters to a service as URL query parameters or HTTP headers. You can specify these parameters directly when writing custom code, though tools such as the Google-provided [client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained) handle many of them automatically.
## HTTP mapping
For HTTP requests, system parameters are sent as URL query parameters or HTTP request headers. For example, if you have a system parameter `$foo`, it's sent as `?$foo=xxx` in the URL, or `?%24foo=xxx` if URL-encoded. See the table below for details.
## gRPC mapping
For [gRPC](https://grpc.io/) requests, system parameters are sent as HTTP request headers with keys in lowercase. See the table below for details.
## Definitions
The following table lists all system parameters and their definitions.  
| URL Query Parameter  | HTTP/gRPC Header  | Description  |  
| --- | --- | --- |  
|   | `Authorization`  | Authentication credentials. See [Authentication overview](https://docs.cloud.google.com/docs/authentication) for details.  |  
|  `$alt`,  
`alt`  |   | Alternative response format. Supported values are `json` (default), `media`, `proto`, `sse` (JSON streams).  |  
| `$apiVersion`  | `X-Goog-Api-Version`  | The API version to use. Not all APIs support this parameter: check the API documentation before using it.  |  
| `$.xgafv`  |   | JSON error format. Supported values are `1`, `2` (default). The error format `1` should only be used by [Google API Client Libraries](https://developers.google.com/api-client-library).  |  
|  `$callback`,  
`callback`  |   | JSONP callback parameter.  |  
| `$ct`  | `Content-Type`  | HTTP Content-Type request header override.  |  
|  `$fields`,  
`fields`  | `X-Goog-FieldMask`  |  [`FieldMask`](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/field_mask.proto) used for response filtering. If empty, all fields should be returned unless documented otherwise.  |  
|   | `X-HTTP-Method-Override`  | The intended HTTP method for the request. Some network proxies don't accept all HTTP methods.  |  
|  `$key`,  
`key`  | `X-Goog-Api-Key`  | Google API key. See https://cloud.google.com/docs/authentication/api-keys for details.  |  
|  `passwd`,  
`password`  |   | Reserved to prevent putting passwords in URLs.  |  
|  `$prettyPrint`,  
`prettyPrint`  |   | Pretty-print JSON response. Supported values are `true` (default), `false`.  |  
| `quotaUser`  | `X-Goog-Quota-User`  | A pseudo user identifier for charging per-user quotas. If not specified, the authenticated principal is used. If there is no authenticated principal, the client IP address will be used. When specified, a valid API key with service restrictions must be used to identify the quota project. Otherwise, this parameter is ignored.  |  
| `$outputDefaults`  |   | Force to output proto default values for JSON responses.  |  
| `$unique`  |   | Unique query parameter to disable request caching.  |  
|   | `X-Goog-Api-Client`  | API client identification. The value is a space-separated list of `NAME "/" SEMVER` strings, where the `NAME` should only contain lowercase letters, digits, and "-", and the `SEMVER` should be a semantic version string. For example: X-Goog-Api-Client: python/3.5.0 grpc-google-pubsub-v1/0.1.0-beta2 linux/2.7.0.  |  
|   | `X-Goog-Request-Reason`  | Contains a reason for making the request, which is intended to be recorded in audit logging. An example reason would be a support-case ticket number. For audit logs, the characters in the reason determine whether the reason is base64 encoded before being attached to the log entry. Reasons that include only letters, digits, and spaces are retained in plain text. Reasons that include other characters are base64 encoded.  |  
| `$userProject`  | `X-Goog-User-Project`  | A caller-specified project for quota and billing purposes. The caller must have `serviceusage.services.use` permission on the project.  |  
|   | `X-Server-Timeout`  | Timeout (in seconds, float value) for the server to finish processing the request. This system param only applies to REST APIs for which client-side timeout is not applicable.  |  
|   | `x-goog-request-params`  | Passing additional parameters for gRPC requests. The value must be URL query string encoded (e.g., `key1=value1&key2=value2`).  
  
The specific keys and values supported within this header are dependent on the individual Google API service and method being called. There is no single, universal set of parameters for this header. Always consult the documentation for the specific API you are interacting with to determine which parameters are supported or required.  
  
Common uses include:
  * **Routing Information:** For regionalized services, this header often carries parameters to help GFEs route the request to the correct regional backend. This frequently involves keys matching resource name parts (e.g., `name=projects/my-proj/locations/us-central1`, `parent=projects/my-proj/locations/us-central1`) or explicit location parameters (e.g., `grpc-location=locations/us-central1`).
  * **API-Specific Functionality:** For example, the BigQuery Storage Write API uses the `write_stream` parameter within this header for non-US multi-region gRPC calls (e.g., `x-goog-request-params: write_stream=projects/myproject/datasets/myds/tables/mytable/streams/mystream`).

Example:  
`x-goog-request-params: name=projects/my-project/locations/us-central1&foo=bar`  |  
## Changelog
  * 2026-10 Published documentation for `X-Goog-Api-Version`.
  * 2026-06 Updated documentation for `x-goog-request-params`.
  * 2021-11 Published documentation for `x-goog-request-params`.
  * 2021-02 Published documentation for `quotaUser`.
  * 2020-07 Deprecated OAuth 2.0 query parameters.
  * 2019-10 Introduced `X-Server-Timeout` system parameter.
  * 2017-10 Introduced `X-Goog-User-Project` system parameter.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
