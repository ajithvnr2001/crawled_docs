---
url: https://docs.comfy.org/development/cloud/overview/
title: v1 Cloud API Overview - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:43.717403+00:00
---

# v1 Cloud API Overview - ComfyUI

> Source: https://docs.comfy.org/development/cloud/overview/

## On this page

  * Base URL
  * Authentication
  * What the SDKs Don’t Cover Yet
  * Available Endpoints
  * Error Handling
  * Next Steps



v1 Cloud API (deprecated)

# v1 Cloud API Overview

Copy pageCopy page

The deprecated v1 Cloud API surface: authentication and the Cloud-specific endpoints Comfy API v2 does not expose

Copy pageCopy page

**Deprecated:** The v1 Cloud API is deprecated in favor of [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview). It remains available for existing integrations and for Cloud capabilities v2 does not expose yet, but endpoints and behavior may change without notice.

The v1 Cloud API provides programmatic access to [Comfy Cloud](https://docs.comfy.org/development/deploy/cloud), Comfy’s managed service for running workflows on cloud infrastructure. Comfy Cloud is a stateful application. Your account carries state that persists across jobs: credits and subscription tier, uploaded assets and generated outputs, the job queue, and the set of installed models and nodes. The v1 API is the surface for that whole application, so it contains functionality not supported in the portable [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview), such as queue management, model browsing, node definitions, and account endpoints. Use v2 (or the SDKs that wrap it) to submit workflows and retrieve results in a way that also works against Comfy API deployments and self-hosted ComfyUI. Use v1 for the Cloud-specific capabilities around it. To run workflows, start with the [Comfy Cloud Quickstart](https://docs.comfy.org/development/deploy/cloud) and the [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks). Credits and concurrency limits are covered in [Usage and Limits](https://docs.comfy.org/development/deploy/cloud-usage); runnable v1 examples are in the [Cloud API Reference](https://docs.comfy.org/development/cloud/api-reference). This page covers the v1-specific surface: authentication and the endpoints v2 does not expose.

**Subscription required:** API access requires a paid Comfy Cloud subscription; the Free tier does not include it. See the [pricing plans](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api).

## 

​

Base URL
    
    
    https://cloud.comfy.org
    

## 

​

Authentication

All v1 requests require an API key passed in the `X-API-Key` header:
    
    
    curl -X GET "https://cloud.comfy.org/api/user" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY"
    

See [Getting an API Key](https://docs.comfy.org/development/api-development/getting-an-api-key) for instructions on creating and managing keys. An invalid or missing key returns `401`. A key on an inactive subscription returns `429`. The same key is used for [Partner Nodes](https://docs.comfy.org/tutorials/partner-nodes/overview). Over HTTP you pass it again in `extra_data.api_key_comfy_org`; see [Using Partner Nodes](https://docs.comfy.org/development/cloud/api-reference#using-partner-nodes) for examples.

## 

​

What the SDKs Don’t Cover Yet

The SDKs cover running a workflow, getting the results back, and canceling a job. The rest of the Cloud surface is reachable over HTTP only, so call these endpoints directly even if you use an SDK for execution.

Capability| Endpoint| Reference  
---|---|---  
Queue status, running and pending jobs| `GET /api/queue`| [Queue Management](https://docs.comfy.org/development/cloud/api-reference#queue-management)  
Interrupt the current execution| `POST /api/interrupt`| [Queue Management](https://docs.comfy.org/development/cloud/api-reference#queue-management)  
Node definitions and input specs| `GET /api/object_info`| [Object Info](https://docs.comfy.org/development/cloud/api-reference#object-info)  
Browse available models| Model endpoints| [OpenAPI Specification](https://docs.comfy.org/development/cloud/openapi)  
Account and user information| `GET /api/user`| [OpenAPI Specification](https://docs.comfy.org/development/cloud/openapi)  
Mask uploads that reference an existing image| `POST /api/upload/mask`| [Uploading Inputs](https://docs.comfy.org/development/cloud/api-reference#uploading-inputs)  
  
Canceling a job is covered by both: the SDKs cancel a job you hold a handle to, and `POST /api/queue` cancels by ID.

## 

​

Available Endpoints

Category| Description  
---|---  
[Workflows](https://docs.comfy.org/development/cloud/api-reference#running-workflows)| Submit workflows, check status  
[Jobs](https://docs.comfy.org/development/cloud/api-reference#checking-job-status)| Monitor job status and queue  
[Inputs](https://docs.comfy.org/development/cloud/api-reference#uploading-inputs)| Upload images, masks, and other inputs  
[Outputs](https://docs.comfy.org/development/cloud/api-reference#downloading-outputs)| Download generated content  
[WebSocket](https://docs.comfy.org/development/cloud/api-reference#websocket-for-real-time-progress)| Real-time progress updates  
[Object Info](https://docs.comfy.org/development/cloud/api-reference#object-info)| Available nodes and their definitions  
  
## 

​

Error Handling

REST endpoints return standard HTTP status codes:

Status| Description  
---|---  
`400`| Invalid request (bad workflow, missing fields)  
`401`| Unauthorized (invalid or missing API key)  
`402`| Insufficient credits  
`429`| Subscription inactive  
`500`| Internal server error  
  
The SDKs raise these as typed exceptions instead, including `Unauthorized`, `InvalidWorkflow`, `InsufficientCredits`, `QueueFull`, and `JobFailed`, all extending `ComfyError`. Execution failures are separate from HTTP errors. See [Error Handling](https://docs.comfy.org/development/cloud/api-reference#error-handling) for the `exception_type` values delivered during execution.

## 

​

Next Steps

## Comfy Cloud Quickstart

Run a workflow from Python or TypeScript.

## Usage and Limits

Review Cloud credits, concurrency, and existing v1 integrations.

## Cloud API Reference

Complete endpoint documentation with curl, Python, and TypeScript examples.

## Comfy API v2 Reference

The versioned HTTP API underneath both SDKs. Use it from any language.

## OpenAPI Specification

Machine-readable API spec for code generation.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/cloud/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/cloud/overview)

[Request cancellationPrevious](https://docs.comfy.org/api-reference/v2/jobs/request-cancellation)[Cloud API ReferenceNext](https://docs.comfy.org/development/cloud/api-reference)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
