---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.webhookSubscriptions/create/
title: Method: projects.locations.brands.webhookSubscriptions.create \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:58.679375+00:00
---

# Method: projects.locations.brands.webhookSubscriptions.create  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.webhookSubscriptions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Method: projects.locations.brands.webhookSubscriptions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a webhook subscription.

### HTTP request

`POST https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*}/webhookSubscriptions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of webhook subscriptions. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`webhookSubscriptionId` |  `string` Optional. The ID to use for the webhook subscription, which will become the final component of the webhook subscription's resource name.This value should be 4-63 characters, and valid characters are [a-z0-9-], with the first character a letter and the last a letter or a number (RFC-1034).  
  
### Request body

The request body contains an instance of `[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.webhookSubscriptions#WebhookSubscription)`.

### Response body

If successful, the response body contains a newly created instance of `[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.webhookSubscriptions#WebhookSubscription)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
