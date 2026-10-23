---
url: https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-7/
title: Meshy 7 in ComfyUI: Text to 3D and Image to 3D Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:34.122940+00:00
---

# Meshy 7 in ComfyUI: Text to 3D and Image to 3D Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-7/

## On this page

  * What Meshy 7 is good at
  * Meshy 7 text-to-model workflow
  * Meshy 7 image-to-model workflow



Meshy

# Meshy 7 in ComfyUI: Text to 3D and Image to 3D Workflows

Copy pageCopy page

Generate production-ready 3D models with Meshy 7 in ComfyUI: text-to-3D and image-to-3D workflows with ultra mode, PBR textures, rigging, and animation

Copy pageCopy page

Meshy 7 is Meshy’s 3D generation foundation model, built around image-to-3D alignment. It reads input images at multiple scales and accepts higher-resolution input, so fine shape information survives into generation instead of being averaged out. The result is 3D geometry, color, material, and pattern that stay aligned with the source image. In ComfyUI, Meshy 7 is available through the Meshy Partner Nodes. You can generate a draft model from a text prompt or a single image, then refine it into a fully textured asset with PBR maps, rig it, and animate it, all inside one workflow. Every Meshy node exposes Meshy 7.1, Meshy 7, Meshy 6, and `latest` in its **model** option. The text-to-model template starts on Meshy 7 and the image-to-model template starts on Meshy 7.1.

## 

​

What Meshy 7 is good at

  * **Text-to-3D and image-to-3D** : Generate a model from a text prompt or a single input image
  * **Ultra Mode** : An extra refinement pass for higher-fidelity geometry with finer surface detail, available on Meshy 7.1, Meshy 7, and `latest` models. Text to Model and Image to Model also select the pass resolution with `ultra_resolution`: `2k` (2048³) by default, or `4k` (4096³) on Meshy 7.1 and `latest`
  * **PBR texturing** : Generate metallic, roughness, and normal maps with 2K to 8K base color textures
  * **Full asset pipeline** : Refine, rig, and animate the generated model in the same workflow



To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

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

## 

​

Meshy 7 text-to-model workflow

Generate a 3D model directly from a text description. The workflow creates the draft mesh with the Meshy 7 Text to Model node, then textures, rigs, and animates it automatically.

## Run on Comfy Cloud

Run the text-to-model workflow instantly on Comfy Cloud.

## Download Workflow

Download the workflow JSON file for local use.

![Meshy 7 Text-to-Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_text_to_model-1.webp)

## 

​

Meshy 7 image-to-model workflow

Convert a single 2D image into a detailed 3D model. Meshy 7’s multi-scale image encoder preserves fine shape information from the source image, and the workflow textures, rigs, and animates the result in one pass.

## Run on Comfy Cloud

Run the image-to-model workflow instantly on Comfy Cloud.

## Download Workflow

Download the workflow JSON file for local use.

![Meshy 7 Image-to-Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_image_to_model-1.webp)

## Download Sample Input Image

Get the example input image for this workflow.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/meshy/meshy-7.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/meshy/meshy-7)

[Hunyuan 3D 3.0 in ComfyUI: Text, Image, and Multi-View to 3DPrevious](https://docs.comfy.org/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0)[Meshy 6 in ComfyUI: Text, Image, and Multi-View to 3DNext](https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-6)

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
