---
url: https://docs.comfy.org/development/comfyui-server/api-proxy/
title: API Proxy for Self-Hosted ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:54.728502+00:00
---

# API Proxy for Self-Hosted ComfyUI - ComfyUI

> Source: https://docs.comfy.org/development/comfyui-server/api-proxy/

## On this page

  * Install and run
  * Point the SDK at it
  * Authentication
  * Next steps



Run Workflows

# API Proxy for Self-Hosted ComfyUI

Copy pageCopy page

Serve the Comfy API v2 in front of your own ComfyUI so the official SDKs can run workflows against it

Copy pageCopy page

The [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks) speak [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview). A self-hosted ComfyUI serves v2 through [comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy), a small open-source service that runs alongside your instance.

## 

​

Install and run
    
    
    pip install comfy-api-proxy
    comfy-api-proxy
    

By default it proxies the ComfyUI on `127.0.0.1:8188` and serves the v2 API on `127.0.0.1:8189`. Use `--comfyui` and `--port` to change either. Run it with `--comfyui-base-dir /path/to/ComfyUI` if you also want to upload model files into your install.

## 

​

Point the SDK at it

Set the base URL and construct the client as usual:
    
    
    export COMFY_BASE_URL="http://127.0.0.1:8189"
    

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    client = Comfy()
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    const client = new Comfy();
    

Everything in the [SDK guide](https://docs.comfy.org/development/api-development/sdks) works the same way against the proxy as against Comfy Cloud.

## 

​

Authentication

Authentication is not required by default. If the proxy is configured with a static bearer token, pass that token as the SDK API key: `Comfy(api_key="...")`.

The proxy binds to loopback only by default. If you expose it beyond loopback, for example in front of a ComfyUI on a rented GPU, configure a bearer token or put an authenticating reverse proxy in front of it.

## 

​

Next steps

  * [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks): the client guide
  * [Comfy API v2 Reference](https://docs.comfy.org/api-reference/v2/overview): the HTTP contract the proxy serves
  * [Self-Hosting Options](https://docs.comfy.org/development/deploy/self-hosting): where to run the ComfyUI behind it
  * [Design Notes](https://docs.comfy.org/development/api-development/sdks-design#the-local-proxy): why the proxy exists



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfyui-server/api-proxy.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfyui-server/api-proxy)

[Comfy SDKs: Python and TypeScript Clients for ComfyUIPrevious](https://docs.comfy.org/development/api-development/sdks)[Workflow API FormatNext](https://docs.comfy.org/development/api-development/workflow-api-format)

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
