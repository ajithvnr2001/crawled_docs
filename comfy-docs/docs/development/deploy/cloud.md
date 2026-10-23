---
url: https://docs.comfy.org/development/deploy/cloud/
title: Comfy Cloud Quickstart - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:55.355734+00:00
---

# Comfy Cloud Quickstart - ComfyUI

> Source: https://docs.comfy.org/development/deploy/cloud/

## On this page

  * Quickstart
  * Next steps



Comfy Cloud

# Comfy Cloud Quickstart

Copy pageCopy page

Run an API-format workflow on Comfy Cloud with a paid subscription, API key, and the Comfy SDK.

Copy pageCopy page

Comfy Cloud is a fully managed, always-available ComfyUI environment. Build workflows in the browser or run them through the SDK. There is no Build or deployment to create.

New to Comfy Cloud? Start with the [Comfy Cloud introduction](https://docs.comfy.org/get_started/cloud). This quickstart shows how to run workflows from an app.

## 

​

Quickstart

Requires a paid subscription, an [API key](https://docs.comfy.org/development/api-development/getting-an-api-key), and an API-format workflow. The [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks) target Cloud by default.

1

Create an API key

Create an API key at [platform.comfy.org](https://platform.comfy.org). See [Getting an API Key](https://docs.comfy.org/development/api-development/getting-an-api-key) for details.

2

Install the SDK

Python

TypeScript
    
    
    pip install comfy-sdk
    
    
    
    npm i @comfyorg/sdk
    

3

Export a workflow in API format

In the Cloud editor, save your tested workflow as `workflow_api.json` with `File → Export Workflow (API)`. See [Workflow API Format](https://docs.comfy.org/development/api-development/workflow-api-format).

4

Run it

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    client = Comfy(api_key="comfyui-...")  # Comfy Cloud is the default target
    
    wf = client.workflows.from_file("workflow_api.json")
    
    job = client.run(wf)
    for output in job.get_outputs("9"):
        output.to_file(output.name)
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    const client = new Comfy({ apiKey: "comfyui-..." }); // Comfy Cloud is the default target
    
    const wf = await client.workflows.fromFile("workflow_api.json");
    
    const job = await client.run(wf);
    await job.getOutputs("9")[0].toFile("out.png");
    

`"9"` is the output node ID. See the [SDK guide](https://docs.comfy.org/development/api-development/sdks) for inputs, progress, and error handling.

The same SDK code can target [Comfy API deployments](https://docs.comfy.org/development/serverless/quickstart) and [self-hosted ComfyUI](https://docs.comfy.org/development/deploy/self-hosting). See [Running Workflows](https://docs.comfy.org/development/run-workflows/overview).

## 

​

Next steps

## Usage and Limits

Check how Cloud credits and concurrent jobs work.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/deploy/cloud.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/deploy/cloud)

[Comfy API Deployment GuidePrevious](https://docs.comfy.org/development/serverless/overview)[Usage and LimitsNext](https://docs.comfy.org/development/deploy/cloud-usage)

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
