---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ai_gateway_events/
title: AI Gateway Events \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.577363+00:00
---

# AI Gateway Events · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ai_gateway_events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /AI Gateway Events



# AI Gateway Events

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCachedEndpointGatewayMetadataMetricsModelProviderRateLimitedRequestBodyRequestedModelResponseBodyRoutingDecisionIDRoutingReasonStatusCodeTimestampUserAgent

The descriptions below detail the fields available for `ai_gateway_events`.

## Cached

Type: `bool`

Request cached.

## Endpoint

Type: `string`

Requested endpoint.

## Gateway

Type: `string`

The AI Gateway that generated the log message.

## Metadata

Type: `object`

User defined metadata attached to the request.

## Metrics

Type: `object`

Provider-independent cost and usage metrics for the request, for example {"cost":0.0042,"durationMs":1234}.

## Model

Type: `string`

Model that served the request. For the model the caller asked for, refer to RequestedModel.

## Provider

Type: `string`

Requested provider name.

## RateLimited

Type: `bool`

Request rate limited.

## RequestBody

Type: `object`

Encrypted Request body in the format {"type":"encrypted","data":"base64"}.

## RequestedModel

Type: `string`

Model name the caller requested, for example `cloudflare/auto`. This can differ from Model when AI Gateway routes the request to another model.

## ResponseBody

Type: `object`

Encrypted Response body in the format {"type":"encrypted","data":"base64"}.

## RoutingDecisionID

Type: `string`

Smart routing decision ID, matching the `cf-aig-routing-decision-id` response header. Empty when no routing decision was made.

## RoutingReason

Type: `string`

Reason smart routing selected the model, matching the `cf-aig-routing-reason` response header. Empty when no routing decision was made.

## StatusCode

Type: `int`

Response status code.

## Timestamp

Type: `int or string`

Time the log event was recorded, after the request completed.

## UserAgent

Type: `string`

User-Agent header sent by the client, truncated to 512 characters.

[PreviousAccount Abuse Protection Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/account_abuse_protection_events/)[NextAudit Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/ai_gateway_events.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
