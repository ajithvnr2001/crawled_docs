---
url: https://docs.comfy.org/tutorials/image/cosmos/cosmos-predict2-t2i/
title: Cosmos Predict2 in ComfyUI: Text-to-Image Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:20.953967+00:00
---

# Cosmos Predict2 in ComfyUI: Text-to-Image Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/cosmos/cosmos-predict2-t2i/

Image

# Cosmos Predict2 in ComfyUI: Text-to-Image Generation

Copy pageCopy page

Run NVIDIA Cosmos-Predict2 text-to-image generation in ComfyUI: install the models and complete the workflow from a text prompt.

Copy pageCopy page

Cosmos-Predict2 is NVIDIA’s next-generation physical world foundation model, specifically designed for high-quality visual generation and prediction tasks in physical AI scenarios. The model features exceptional physical accuracy, environmental interactivity, and detail reproduction capabilities, enabling realistic simulation of complex physical phenomena and dynamic scenes. Cosmos-Predict2 supports various generation methods including Text-to-Image (Text2Image) and Video-to-World (Video2World), and is widely used in industrial simulation, autonomous driving, urban planning, scientific research, and other fields. GitHub:[Cosmos-predict2](https://github.com/nvidia-cosmos/cosmos-predict2) huggingface: [Cosmos-Predict2](https://huggingface.co/collections/nvidia/cosmos-predict2-68028efc052239369a0f2959) This guide will walk you through completing **text-to-image** workflow in ComfyUI. For the video generation section, please refer to the following part:

## Cosmos Predict2 Video Generation

Using Cosmos-Predict2 for video generation

  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/cosmos/cosmos-predict2-t2i.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/cosmos/cosmos-predict2-t2i)

[Ming Image 0.1 Design: RGBA Text to Image in ComfyUIPrevious](https://docs.comfy.org/tutorials/image/ming-image/ming-image-0-1-design)[ComfyUI OmniGen2 Native Workflow ExamplesNext](https://docs.comfy.org/tutorials/image/omnigen/omnigen2)

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
