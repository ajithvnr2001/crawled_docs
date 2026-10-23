---
url: https://docs.comfy.org/development/deploy/cloud-usage/
title: Usage and Limits - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.336393+00:00
---

# Usage and Limits - ComfyUI

> Source: https://docs.comfy.org/development/deploy/cloud-usage/

## On this page

  * Credits and usage
  * Concurrent jobs
  * Runtime and queue limits
  * Existing v1 integrations
  * Next steps



Comfy Cloud

# Usage and Limits

Copy pageCopy page

Understand Comfy Cloud credits, concurrent jobs, and the limits that apply when running workflows through the SDK.

Copy pageCopy page

Workflows submitted through the Comfy Cloud API use the same credits and concurrency limits as other Cloud workflows.

## 

​

Credits and usage

API requests draw from the same monthly credit allocation as the Comfy Cloud web UI. There is no separate API credit pool. Each tier’s included credits, top-up options, and per-workflow runtime caps apply to API jobs in the same way as UI jobs. See the [pricing page](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) for monthly credit amounts and top-up options. You can purchase top-ups from your account dashboard.

## 

​

Concurrent jobs

You can submit multiple workflows without waiting for previous jobs to complete. Jobs run in parallel up to your subscription tier’s limit:

Plan| Concurrent workflows  
---|---  
Standard| 1  
Creator| 3  
Pro| 5  
  
Team plans run more concurrent workflows per member than Pro. Check [platform.comfy.org](https://platform.comfy.org) for the concurrency on your account. Additional jobs queue and run as slots become available. If the queue is full, the SDKs retry within a bounded budget before raising `QueueFull`.

Parallel execution is available through the API. See the [pricing plans](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) for subscription details.

## 

​

Runtime and queue limits

Every Cloud workflow has a maximum runtime. A job that runs past the limit is cancelled automatically:

Plan| Maximum runtime  
---|---  
Standard| 30 minutes  
Creator| 30 minutes  
Pro| 1 hour  
  
You can have up to 100 workflows queued at once. To raise a Team concurrency limit, [contact support](https://support.comfy.org/).

## 

​

Existing v1 integrations

The deprecated [v1 Cloud API](https://docs.comfy.org/development/cloud/overview) also runs against Comfy Cloud. Use it for existing integrations or Cloud capabilities not yet available in [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview). Runnable examples are in the deprecated [Cloud API Reference](https://docs.comfy.org/development/cloud/api-reference).

## 

​

Next steps

## Comfy Cloud Quickstart

Set up the SDK and run your first Cloud workflow.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/deploy/cloud-usage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/deploy/cloud-usage)

[Comfy Cloud QuickstartPrevious](https://docs.comfy.org/development/deploy/cloud)[Self-Hosting OptionsNext](https://docs.comfy.org/development/deploy/self-hosting)

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
