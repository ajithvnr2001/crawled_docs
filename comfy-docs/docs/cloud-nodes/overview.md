---
url: https://docs.comfy.org/cloud-nodes/overview/
title: Comfy Cloud nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:34.277413+00:00
---

# Comfy Cloud nodes - ComfyUI

> Source: https://docs.comfy.org/cloud-nodes/overview/

## On this page

  * What it is
  * Getting started
  * Available nodes
  * Billing
  * Limitations
  * Related



Comfy Cloud Nodes

# Comfy Cloud nodes

Copy pageCopy page

Run curated workflows on Comfy Cloud’s GPUs from a local ComfyUI install, no subscription required

Copy pageCopy page

A Comfy Cloud node is a regular ComfyUI node that sends its job to run on Comfy’s own GPUs instead of the local machine. Drop it into a graph like any other node. No subscription is required: an account and credits are enough, the same as any other partner node.

Comfy Cloud nodes run open source models on the cloud. Not to be confused with Partner Nodes.

## 

​

What it is

Each Comfy Cloud node runs one fixed workflow on a pinned model version, so a saved graph keeps producing the same result over time. Your graph, prompts, and inputs stay on your machine apart from what the node sends to run the job.

## 

​

Getting started

Comfy Cloud nodes ship with ComfyUI **v0.34.5 or later**. They are part of ComfyUI core, so there is nothing to install separately.

1

Update ComfyUI

Update to v0.34.5 or later. See [How to update ComfyUI](https://docs.comfy.org/installation/update_comfyui) for the portable, desktop, and manual install paths.

2

Restart ComfyUI

The nodes only register at startup, so they will not appear until you restart.

3

Find a node

Search the node library for **Comfy Cloud** , then wire one into your graph like any other node. Every node carries a `[BETA]` suffix in its display name.

## 

​

Available nodes

Eight nodes at launch, across image, video, and audio:

Node| Modality  
---|---  
Comfy Cloud Flux 2 Text to Image| Image  
Comfy Cloud Mage Flow Text to Image| Image  
Comfy Cloud Mage Flow Turbo Text to Image| Image  
Comfy Cloud Z-Image Turbo Text to Image| Image  
Comfy Cloud MiniMax H3 Text to Video| Video  
Comfy Cloud MiniMax H3 Image to Video| Video  
Comfy Cloud MiniMax H3 First-Last Frame to Video| Video  
Comfy Cloud MiniMax Music 3 Text to Audio| Audio  
  
## 

​

Billing

Comfy Cloud nodes are billed per GPU-second in credits, shown on the node before you run it. There is no subscription and no monthly floor.

## 

​

Limitations

  * No bring-your-own LoRA or checkpoint yet. Each node exposes a fixed set of hosted weights. Direct upload is a planned next step, not available in this release.



## 

​

Related

  * [Comfy Cloud pricing](https://comfy.org/pricing)
  * [Partner Nodes overview](https://docs.comfy.org/tutorials/partner-nodes/overview) (the separate third-party API node catalog)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/cloud-nodes/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/cloud-nodes/overview)

[VOID: Video Inpainting in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/void-video-inpainting)[Partner NodesNext](https://docs.comfy.org/tutorials/partner-nodes/overview)

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
