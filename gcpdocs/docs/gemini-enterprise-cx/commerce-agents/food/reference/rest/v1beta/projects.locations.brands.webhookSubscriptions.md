---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions
title: REST Resource: projects.locations.brands.webhookSubscriptions \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:35.396526+00:00
---

# REST Resource: projects.locations.brands.webhookSubscriptions  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  REST Resource: projects.locations.brands.webhookSubscriptions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WebhookSubscription
    * JSON representation
  * State
  * WebhookAuthConfig
    * JSON representation
  * BasicAuth
    * JSON representation
  * SecretSource
    * JSON representation
  * ApiKeyAuth
    * JSON representation
  * BearerTokenAuth
    * JSON representation
  * Methods



## Resource: WebhookSubscription

A webhook subscription configured for a brand to receive real-time event notifications.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#State)),
      "eventTypes": [
        string
      ],
      "destinationUrl": string,
      "filter": string,
      "authConfig": {
        object ([WebhookAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#WebhookAuthConfig))
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the webhook subscription. Format: `projects/{project}/locations/{location}/brands/{brand}/webhookSubscriptions/{webhookSubscription}`  
`displayName` |  `string` Optional. Human-readable display name for this webhook subscription.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#State)`)` Optional. The current state of the webhook subscription. Users may transition a subscription between `ACTIVE` and `PAUSED`.  
`eventTypes[]` |  `string` Required. Event types that trigger this webhook subscription (e.g., `sessions/started`, `sessions/updated`, `sessions/closed`, `orders/updated`).  
`destinationUrl` |  `string` Required. The HTTPS endpoint URL where webhook events are delivered via HTTP POST.  
`filter` |  `string` Optional. Common Expression Language (CEL) filter expression evaluated against event attributes (e.g., `channel == 'CHANNEL_TYPE_DRIVE_THROUGH' && store.endsWith('/stores/store-123')`). If empty, all events matching `eventTypes` for the brand are delivered.  
`authConfig` |  `object (`[WebhookAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#WebhookAuthConfig)`)` Optional. Authentication configuration for outbound webhook deliveries.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this webhook subscription was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this webhook subscription was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

Lifecycle state of the webhook subscription.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | The subscription is active and receiving webhook event deliveries.  
`PAUSED` | The subscription has been paused by the user and will not receive events until re-activated.  
`SUSPENDED` | The subscription has been automatically suspended by the platform circuit breaker due to repeated delivery failures.  
  
## WebhookAuthConfig

Authentication configuration for outbound webhook deliveries.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "basicAuth": {
        object ([BasicAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#BasicAuth))
      },
      "apiKeyAuth": {
        object ([ApiKeyAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#ApiKeyAuth))
      },
      "bearerTokenAuth": {
        object ([BearerTokenAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#BearerTokenAuth))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The authentication method to use when dispatching webhook requests. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`basicAuth` |  `object (`[BasicAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#BasicAuth)`)` Optional. Configuration for HTTP Basic authentication.  
`apiKeyAuth` |  `object (`[ApiKeyAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#ApiKeyAuth)`)` Optional. Configuration for API key / custom header authentication.  
`bearerTokenAuth` |  `object (`[BearerTokenAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#BearerTokenAuth)`)` Optional. Configuration for Bearer token authentication.  
End of mutually exclusive fields.  
  
## BasicAuth

HTTP Basic Authentication (`Authorization: Basic <base64(user:pass)>`).

JSON representation  
---  
      
    
    {
      "credential": {
        object ([SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#SecretSource))
      }
    }  
  
Fields  
---  
`credential` |  `object (`[SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#SecretSource)`)` Required. Secret containing the colon-separated basic auth credential in `<username>:<password>` format.  
  
## SecretSource

Reference to a secret value used for webhook authentication.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "secretVersion": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The backing store for the secret value. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`secretVersion` |  `string` Optional. The name of the Secret Manager secret version resource storing the secret value. Format: `projects/{project}/secrets/{secret}/versions/{secretVersion}`Note: You must grant the `roles/secretmanager.secretAccessor` role to the Food Ordering AI Agent service agent `service-<PROJECT-NUMBER>@gcp-sa-foodorderingaiagent.iam.gserviceaccount.com`.  
End of mutually exclusive fields.  
  
## ApiKeyAuth

API Key / Custom Header Authentication (`<header>: <secret_value>`).

JSON representation  
---  
      
    
    {
      "header": string,
      "apiKey": {
        object ([SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#SecretSource))
      }
    }  
  
Fields  
---  
`header` |  `string` Required. The HTTP header to populate (e.g., "X-API-Key").  
`apiKey` |  `object (`[SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#SecretSource)`)` Required. Secret containing the API key or header value.  
  
## BearerTokenAuth

Bearer Token Authentication (`Authorization: Bearer <token>`).

JSON representation  
---  
      
    
    {
      "token": {
        object ([SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#SecretSource))
      }
    }  
  
Fields  
---  
`token` |  `object (`[SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions#SecretSource)`)` Required. Secret containing the bearer token.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions/create)`

|  Creates a webhook subscription.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions/delete)`

|  Deletes the specified webhook subscription.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions/get)`

|  Gets a webhook subscription.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions/list)`

|  Lists webhook subscriptions for a brand.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.webhookSubscriptions/patch)`

|  Updates the specified webhook subscription.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
