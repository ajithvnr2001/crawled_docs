---
url: https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p2/
title: Tripo P2: Quad Topology 3D Model Generation in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:39.790779+00:00
---

# Tripo P2: Quad Topology 3D Model Generation in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p2/

## On this page

  * What Tripo P2 is good at
  * Tripo P2: Text to Model
    * Steps to Run
    * Quad output note
  * Tripo P2: Image to Model
    * Steps to Run
    * Input tips
  * Tripo P2: Multiview to Model
    * Steps to Run
  * Node options reference



Tripo

# Tripo P2: Quad Topology 3D Model Generation in ComfyUI

Copy pageCopy page

Generate production-ready 3D models with Tripo P2 partner nodes in ComfyUI: native quad topology, face budgets up to 50,000, and texture levels from 2K to 8K.

Copy pageCopy page

Tripo P2 is Tripo’s P-series 3D generation model that outputs native quad-topology meshes. Where traditional text-to-3D and image-to-3D models return triangle meshes, Tripo P2 builds geometry from four-sided faces with clean edge loops around joints and even density on flat surfaces. Quads deform predictably under a rig, subdivide cleanly, and are the standard input for retopology-heavy pipelines in games, film, and product visualization. Tripo P2 supports three input modes: text to model, single image to model, and multiview to model (front, left, back, and right references). Mesh budgets reach 50,000 triangles, or 25,000 quads in quad mode. Texture output is tiered: standard at 2K, detailed at 4K, extreme at 8K, with PBR maps (metallic, roughness, normal) available alongside the base color. In ComfyUI, the P2 nodes work like the rest of the Tripo partner nodes: add the node, provide your input, and the workflow handles texturing, rigging, conversion, and export automatically. No local GPU or model download is required.

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

What Tripo P2 is good at

  * **Native quad topology** : quad meshes with clean edge flow, ready for rigging and animation without manual retopology
  * **Large mesh budgets** : 48 to 50,000 triangles, or 48 to 25,000 quads in quad mode
  * **Tiered texturing** : standard (2K), detailed (4K), or extreme (8K) base color textures, with optional PBR maps
  * **Three input modes** : text prompts, a single reference image, or up to four multiview images (front, left, back, right)

Pricing depends on the selected texture level. See [Pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for details.

## 

​

Tripo P2: Text to Model

Generate a 3D model from a text description. Tripo P2 first draws a concept image from the prompt (controlled by `image_seed`), then models the geometry from it. ![Tripo P2 Text to Model Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_text_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Tripo P2: Text to Model” in Template Library

### 

​

Steps to Run

  1. **Enter your prompt** : describe the 3D model in the **Tripo P2: Text to Model** node (up to 1024 characters). A negative prompt is available in advanced options
  2. **Choose the texture level** : `standard` (2K), `detailed` (4K), `extreme` (8K), or `none` for an untextured mesh
  3. **Toggle quad output** : with `quad` enabled the mesh returns as FBX; disabled it returns as GLB
  4. **Set the face limit** : target face count between 48 and 50,000 (48 to 25,000 with quad), or leave at -1 to let Tripo choose
  5. **Click Queue** : press `Ctrl+Enter` to generate

After generation, the node requests the texture level you selected, so the mesh is textured as part of generation, and the workflow saves that result directly (the GLB output, or FBX when `quad` is on). The template also contains **TripoTextureNodeV2** , **TripoRigNode** , **TripoRetargetNode** , and **TripoConversionNode** nodes, but they are bypassed and disconnected by default: connect and enable them (`Ctrl+B` toggles bypass) when you want that extra post-processing.

### 

​

Quad output note

When `quad` is enabled, connect **Save 3D** to the FBX output slot. When `quad` is disabled, use the GLB output slot.

## 

​

Tripo P2: Image to Model

Generate a 3D model from a single reference image. ![Tripo P2 Image to Model Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_image_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Tripo P2: Image to Model” in Template Library

### 

​

Steps to Run

  1. **Upload a reference image** : load a front-view image of your subject with the **LoadImage** node
  2. **Choose the texture level** : `standard`, `detailed`, `extreme`, or `none`
  3. **Toggle quad output** : FBX when enabled, GLB when disabled
  4. **Set texture alignment** : `original_image` matches the input image’s colors, `geometry` fits the textures to the generated shape (advanced options)
  5. **Click Queue** : press `Ctrl+Enter` to generate



### 

​

Input tips

  * Low-resolution or low-quality images can be enhanced before modeling with the `enable_image_autofix` advanced option
  * `align_image` orientation rotates the model to the viewpoint of the input image (advanced options)



## 

​

Tripo P2: Multiview to Model

Generate a 3D model from reference views. The multiview node takes a required front view plus up to three of the left, back, and right views, and at least one of those extra views must be connected: with the front view alone the node returns an error. It reconstructs the geometry with the same native quad topology as the other P2 nodes. ![Tripo P2 Multiview to Model Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_multiview_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Tripo P2: Multiview to Model” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## worker_doll_front.png

`LoadImage` node 16 · front view

## worker_doll_back.png

`LoadImage` node 19 · back view

### 

​

Steps to Run

  1. **Load the reference views** : the template ships with a front view (`LoadImage` node 16) and a back view (`LoadImage` node 19). The node also exposes `image_left` and `image_right` inputs for a four-view reconstruction
  2. **Choose the texture level** : `standard` (2K), `detailed` (4K), `extreme` (8K), or `none` for an untextured mesh
  3. **Toggle quad output** : with `quad` enabled the mesh returns as FBX; disabled it returns as GLB
  4. **Set the face limit** : target face count between 48 and 50,000 (48 to 25,000 with quad), or leave at -1 to let Tripo choose
  5. **Click Queue** : press `Ctrl+Enter` to generate

The workflow saves the generated mesh directly. The texture, rig, retarget, and conversion nodes the template also contains are bypassed and disconnected by default.

## 

​

Node options reference

Options shared by all three P2 nodes:

Option| Values| Default| Notes  
---|---|---|---  
`quad`| on / off| off| Quad mesh as FBX when on, triangle mesh as GLB when off  
`face_limit`| 48 to 50,000 (25,000 with quad)| -1| Target face count; the result can exceed it  
`texture`| standard / detailed / extreme / none| standard| 2K / 4K / 8K base color; none returns an untextured mesh  
`pbr`| on / off| on| Metallic, roughness, and normal maps; ignored when texture is none  
`model_seed`| 0 to 2147483647| 42| Seed for the geometry  
  
Advanced options include `texture_seed`, `auto_size` (real-world scale in meters), `export_uv`, and `compress_geometry` (Meshopt compression; compressed meshes are much smaller but cannot be previewed in ComfyUI’s 3D viewport).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/tripo/tripo-p2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/tripo/tripo-p2)

[Hyper3D Rodin in ComfyUI: Single and Multi-View 3D GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/rodin/model-generation)[Tripo P1 in ComfyUI: Text, Image, and Multiview 3D GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p1)

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
