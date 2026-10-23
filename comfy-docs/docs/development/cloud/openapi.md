---
url: https://docs.comfy.org/development/cloud/openapi/
title: OpenAPI Specification - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:43.887544+00:00
---

# OpenAPI Specification - ComfyUI

> Source: https://docs.comfy.org/development/cloud/openapi/

## On this page

  * Comfy Cloud API Specification
  * Interactive API Reference
  * Using the Specification
  * Download
  * Authentication
    * Getting an API Key
    * Using the API Key
  * Base URL
  * WebSocket Connection



v1 Cloud API (deprecated)

# OpenAPI Specification

Copy pageCopy page

Machine-readable OpenAPI specification for Comfy Cloud API

Copy pageCopy page

**Deprecated:** The v1 Cloud API is deprecated in favor of [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview). Endpoints, request/response formats, and behavior may be modified without notice.

# 

​

Comfy Cloud API Specification

This page provides the complete OpenAPI 3.0 specification for the Comfy Cloud API.

**Subscription Required:** Running workflows via the API requires an active Comfy Cloud subscription. See [pricing plans](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) for details.

## 

​

Interactive API Reference

Explore the full API with interactive documentation:

## Cloud API Reference

Browse endpoints, view schemas, and try requests

## 

​

Using the Specification

The OpenAPI spec can be used to:

  * **Generate client libraries** in any language using tools like [OpenAPI Generator](https://openapi-generator.tech/)
  * **Import into API tools** like Postman, Insomnia, or Paw
  * **Generate documentation** using tools like Redoc or Swagger UI
  * **Validate requests** in your application



## 

​

Download

You can download the raw OpenAPI specification file:

## openapi-cloud.yaml

Download the OpenAPI 3.0 specification

## 

​

Authentication

All API requests require an API key passed in the `X-API-Key` header.

### 

​

Getting an API Key

See [Getting an API Key](https://docs.comfy.org/development/api-development/getting-an-api-key) for step-by-step instructions with screenshots.

### 

​

Using the API Key
    
    
    X-API-Key: your-api-key
    

## 

​

Base URL

Environment| URL  
---|---  
Production| `https://cloud.comfy.org`  
  
## 

​

WebSocket Connection

For real-time updates, connect to the WebSocket endpoint:
    
    
    wss://cloud.comfy.org/ws?clientId={uuid}&token={api_key}
    

See the [Cloud API Reference](https://docs.comfy.org/development/cloud/api-reference#websocket-for-real-time-progress) for message types and handling.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/cloud/openapi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/cloud/openapi)

[Cloud API ReferencePrevious](https://docs.comfy.org/development/cloud/api-reference)[Get information about current prompt executionsNext](https://docs.comfy.org/api-reference/cloud/workflow/get-information-about-current-prompt-executions)

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
