---
url: https://ai.google.dev/api/webhooks/
title: Gemini Webhooks API
method: scrapling+scrapegraph
fetched_at: 2026-10-30T10:43:21.618837+00:00
---

# Gemini Webhooks API

> Source: https://ai.google.dev/api/webhooks/

Webhooks allow the Gemini API to push real-time notifications to your server when asynchronous or Long-Running Operations (LROs) complete. This replaces the need to poll the API for status updates, reducing latency and overhead.

[View as markdown](https://ai.google.dev/static/api/webhooks.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)

## CreateWebhook

post  https://generativelanguage.googleapis.com/v1beta/webhooks 

Creates a new Webhook.

  * Path / Query parameters
  * Request body
  * Response



### Path / Query Parameters

webhook_id string (optional)

The webhook_id to use for the webhook. If not specified, the server will generate a unique ID.

### Request body

The request body contains data with the following structure:

webhook Webhook (required)

Required. The webhook to create.

### Response

If successful, the response body contains data with the following structure:

uri string (required)

Required. The URI to which webhook events will be sent.

subscribed_events array (string) (required)

Required. The events that the webhook is subscribed to. Available events: \- batch.succeeded \- batch.expired \- batch.failed \- interaction.requires_action \- interaction.completed \- interaction.failed \- video.generated

name string (optional)

Optional. The user-provided name of the webhook.

create_time string (optional)

Output only. The timestamp when the webhook was created.

update_time string (optional)

Output only. The timestamp when the webhook was last updated.

signing_secrets array (SigningSecret) (optional)

Output only. The signing secrets associated with this webhook.

Represents a signing secret used to verify webhook payloads.

#### Fields

truncated_secret string (optional)

Output only. The truncated version of the signing secret.

expire_time string (optional)

Output only. The expiration date of the signing secret.

state enum (string) (optional)

Output only. The state of the webhook.

Possible values:

  * `enabled`

The webhook is enabled.

  * `disabled`

The webhook is disabled by the user.

  * `disabled_due_to_failed_deliveries`

The webhook is disabled due to failed deliveries.




new_signing_secret string (optional)

Output only. The new signing secret for the webhook. Only populated on create.

id string (optional)

Output only. The ID of the webhook.

### Example

####  Example Response
    
    
    {
      "uri": "string",
      "subscribed_events": [
        "string"
      ],
      "name": "string",
      "create_time": "string",
      "update_time": "string",
      "signing_secrets": [
        {
          "truncated_secret": "string",
          "expire_time": "string"
        }
      ],
      "state": "enabled",
      "new_signing_secret": "string",
      "id": "string"
    }

## PingWebhook

post  https://generativelanguage.googleapis.com/v1beta/webhooks/{id}:ping 

Sends a ping event to a Webhook.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. The ID of the webhook to ping.

### Response

If successful, the response is empty.

### Example

## RotateSigningSecret

post  https://generativelanguage.googleapis.com/v1beta/webhooks/{id}:rotateSigningSecret 

Generates a new signing secret for a Webhook.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. The ID of the webhook for which to generate a signing secret.

### Response

If successful, the response body contains data with the following structure:

secret string (optional)

Output only. The newly generated signing secret.

### Example

####  Example Response
    
    
    {
      "secret": "string"
    }

## ListWebhooks

get  https://generativelanguage.googleapis.com/v1beta/webhooks 

Lists all Webhooks.

  * Path / Query parameters
  * Response



### Path / Query Parameters

page_size integer (optional)

Optional. The maximum number of webhooks to return. The service may return fewer than this value. If unspecified, at most 50 webhooks will be returned. The maximum value is 1000.

page_token string (optional)

Optional. A page token, received from a previous `ListWebhooks` call. Provide this to retrieve the subsequent page.

### Response

If successful, the response body contains data with the following structure:

webhooks array (Webhook) (optional)

The webhooks.

next_page_token string (optional)

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

### Example

####  Example Response
    
    
    {
      "webhooks": [
        {
          "uri": "string",
          "subscribed_events": [
            "string"
          ],
          "name": "string",
          "create_time": "string",
          "update_time": "string",
          "signing_secrets": [
            {
              "truncated_secret": "string",
              "expire_time": "string"
            }
          ],
          "state": "enabled",
          "new_signing_secret": "string",
          "id": "string"
        }
      ],
      "next_page_token": "string"
    }

## GetWebhook

get  https://generativelanguage.googleapis.com/v1beta/webhooks/{id} 

Gets a specific Webhook.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. The ID of the webhook to retrieve.

### Response

If successful, the response body contains data with the following structure:

uri string (required)

Required. The URI to which webhook events will be sent.

subscribed_events array (string) (required)

Required. The events that the webhook is subscribed to. Available events: \- batch.succeeded \- batch.expired \- batch.failed \- interaction.requires_action \- interaction.completed \- interaction.failed \- video.generated

name string (optional)

Optional. The user-provided name of the webhook.

create_time string (optional)

Output only. The timestamp when the webhook was created.

update_time string (optional)

Output only. The timestamp when the webhook was last updated.

signing_secrets array (SigningSecret) (optional)

Output only. The signing secrets associated with this webhook.

Represents a signing secret used to verify webhook payloads.

#### Fields

truncated_secret string (optional)

Output only. The truncated version of the signing secret.

expire_time string (optional)

Output only. The expiration date of the signing secret.

state enum (string) (optional)

Output only. The state of the webhook.

Possible values:

  * `enabled`

The webhook is enabled.

  * `disabled`

The webhook is disabled by the user.

  * `disabled_due_to_failed_deliveries`

The webhook is disabled due to failed deliveries.




new_signing_secret string (optional)

Output only. The new signing secret for the webhook. Only populated on create.

id string (optional)

Output only. The ID of the webhook.

### Example

####  Example Response
    
    
    {
      "uri": "string",
      "subscribed_events": [
        "string"
      ],
      "name": "string",
      "create_time": "string",
      "update_time": "string",
      "signing_secrets": [
        {
          "truncated_secret": "string",
          "expire_time": "string"
        }
      ],
      "state": "enabled",
      "new_signing_secret": "string",
      "id": "string"
    }

## UpdateWebhook

patch  https://generativelanguage.googleapis.com/v1beta/webhooks/{id} 

Updates an existing Webhook.

  * Path / Query parameters
  * Request body
  * Response



### Path / Query Parameters

id string (required)

Required. The ID of the webhook to update.

### Request body

The request body contains data with the following structure:

webhook WebhookUpdate (required)

Required. The webhook to update.

#### Fields

name string (optional)

Optional. The user-provided name of the webhook.

uri string (optional)

Optional. The URI to which webhook events will be sent.

subscribed_events array (string) (optional)

Optional. The events that the webhook is subscribed to. Available events: \- batch.succeeded \- batch.expired \- batch.failed \- interaction.requires_action \- interaction.completed \- interaction.failed \- video.generated

state enum (string) (optional)

Optional. The state of the webhook.

Possible values:

  * `enabled`

The webhook is enabled.

  * `disabled`

The webhook is disabled by the user.

  * `disabled_due_to_failed_deliveries`

The webhook is disabled due to failed deliveries.




id string (required)

Required. The ID of the webhook to update.

update_mask string (optional)

Optional. The list of fields to update.

### Response

If successful, the response body contains data with the following structure:

uri string (required)

Required. The URI to which webhook events will be sent.

subscribed_events array (string) (required)

Required. The events that the webhook is subscribed to. Available events: \- batch.succeeded \- batch.expired \- batch.failed \- interaction.requires_action \- interaction.completed \- interaction.failed \- video.generated

name string (optional)

Optional. The user-provided name of the webhook.

create_time string (optional)

Output only. The timestamp when the webhook was created.

update_time string (optional)

Output only. The timestamp when the webhook was last updated.

signing_secrets array (SigningSecret) (optional)

Output only. The signing secrets associated with this webhook.

Represents a signing secret used to verify webhook payloads.

#### Fields

truncated_secret string (optional)

Output only. The truncated version of the signing secret.

expire_time string (optional)

Output only. The expiration date of the signing secret.

state enum (string) (optional)

Output only. The state of the webhook.

Possible values:

  * `enabled`

The webhook is enabled.

  * `disabled`

The webhook is disabled by the user.

  * `disabled_due_to_failed_deliveries`

The webhook is disabled due to failed deliveries.




new_signing_secret string (optional)

Output only. The new signing secret for the webhook. Only populated on create.

id string (optional)

Output only. The ID of the webhook.

### Example

####  Example Response
    
    
    {
      "uri": "string",
      "subscribed_events": [
        "string"
      ],
      "name": "string",
      "create_time": "string",
      "update_time": "string",
      "signing_secrets": [
        {
          "truncated_secret": "string",
          "expire_time": "string"
        }
      ],
      "state": "enabled",
      "new_signing_secret": "string",
      "id": "string"
    }

## DeleteWebhook

delete  https://generativelanguage.googleapis.com/v1beta/webhooks/{id} 

Deletes a Webhook.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. The ID of the webhook to delete.

### Response

If successful, the response is empty.

### Example

## Resources

### Webhook

A Webhook resource.

#### Fields

uri string (required)

Required. The URI to which webhook events will be sent.

subscribed_events array (string) (required)

Required. The events that the webhook is subscribed to. Available events: \- batch.succeeded \- batch.expired \- batch.failed \- interaction.requires_action \- interaction.completed \- interaction.failed \- video.generated

name string (optional)

Optional. The user-provided name of the webhook.

create_time string (optional)

Output only. The timestamp when the webhook was created.

update_time string (optional)

Output only. The timestamp when the webhook was last updated.

signing_secrets array (SigningSecret) (optional)

Output only. The signing secrets associated with this webhook.

Represents a signing secret used to verify webhook payloads.

#### Fields

truncated_secret string (optional)

Output only. The truncated version of the signing secret.

expire_time string (optional)

Output only. The expiration date of the signing secret.

state enum (string) (optional)

Output only. The state of the webhook.

Possible values:

  * `enabled`

The webhook is enabled.

  * `disabled`

The webhook is disabled by the user.

  * `disabled_due_to_failed_deliveries`

The webhook is disabled due to failed deliveries.




new_signing_secret string (optional)

Output only. The new signing secret for the webhook. Only populated on create.

id string (optional)

Output only. The ID of the webhook.
