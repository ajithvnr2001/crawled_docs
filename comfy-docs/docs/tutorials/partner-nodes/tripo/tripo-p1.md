---
url: https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p1/
title: Tripo P1 in ComfyUI: Text, Image, and Multiview 3D Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:39.398769+00:00
---

# Tripo P1 in ComfyUI: Text, Image, and Multiview 3D Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p1/

## On this page

  * What Tripo P1 is good at
  * Tripo P1: Text to Model
    * Steps to Run
    * Key Processing Nodes
  * Tripo P1: Image to Model
    * Steps to Run
  * Tripo P1: Multiview to Model
    * Steps to Run
    * Input Tips



Tripo

# Tripo P1 in ComfyUI: Text, Image, and Multiview 3D Generation

Copy pageCopy page

Generate 3D models with Tripo P1 in ComfyUI from text, a single image, or multiview references: clean topology, texturing, rigging, and retargeting.

Copy pageCopy page

The [Tripo P1](https://docs.comfy.org/built-in-nodes/TripoP1ImageToModelNode) Partner Nodes enable fast, high-quality 3D model generation from text prompts, single images, or multi-view references. The generated models come with clean topology, optimized polygon budgets, and support for texturing, rigging, and retargeting — ready for use in game engines and 3D applications.

## 

​

What Tripo P1 is good at

  * **Flexible inputs** : Generate 3D models from text prompts, single images, or multi-view references
  * **Clean topology** : Models come with clean topology and optimized polygon budgets
  * **Texturing, rigging, and retargeting** : Generated models support texturing, rigging, and retargeting
  * **Game-ready output** : Assets are ready for use in game engines and 3D applications



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

Tripo P1: Text to Model

Generate a 3D model from a text description. ![Tripo P1 Text to Model Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_text_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Tripo P1: Text to Model” in Template Library

### 

​

Steps to Run

  1. **Enter your prompt** — describe the 3D model in the **TripoP1TextToModelNode**
  2. **Select texture mode** — choose between Textured, None, or PBR
  3. **Enable refinement** — toggle quad remeshing for cleaner topology
  4. **Set seed** — control reproducibility
  5. **Click Queue** — press `Ctrl+Enter` to generate
  6. **Preview and export** — use the **Preview3D** node to inspect, and **SaveGLB** to export



### 

​

Key Processing Nodes

After the initial generation, the workflow automatically processes the model through:

  * **TripoTextureNode** — applies materials and textures
  * **TripoConversionNode** — converts to GLTF format (or other export formats)
  * **TripoRigNode** — adds a skeleton for animation
  * **TripoRetargetNode** — applies a preset animation (default: idle)



## 

​

Tripo P1: Image to Model

Generate a 3D model from a single reference image. ![Tripo P1 Image to Model Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_image_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Tripo P1: Image to Model” in Template Library

### 

​

Steps to Run

  1. **Upload a reference image** — use the **LoadImage** node to load a front-view image of your subject
  2. **Select texture mode** — choose Textured, None, or PBR
  3. **Enable refinement** — toggle quad remeshing
  4. **Choose texture type** — options include `original_image` or `standard`
  5. **Click Queue** — press `Ctrl+Enter` to generate



## 

​

Tripo P1: Multiview to Model

Generate a 3D model from multiple viewpoint images for better accuracy. ![Tripo P1 Multiview to Model Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_mv_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Tripo P1: Multiview to Model” in Template Library

### 

​

Steps to Run

  1. **Upload multi-view images** — use multiple **LoadImage** nodes for front, left, back, and other angles
  2. **Select texture mode** — choose Textured, None, or PBR
  3. **Choose detail level** — options include `standard` and `detailed`
  4. **Set texture references** — choose which image drives the texture
  5. **Click Queue** — press `Ctrl+Enter` to generate



### 

​

Input Tips

  * Provide at least **front-facing and profile views** for best results
  * Ensure consistent lighting and pose across all reference images
  * Higher-quality input images produce better textured output



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/tripo/tripo-p1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/tripo/tripo-p1)

[Tripo P2: Quad Topology 3D Model Generation in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p2)[Tripo 3.1: High-Detail 3D Asset Generation ComfyUI Official GuideNext](https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-3-1)

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
