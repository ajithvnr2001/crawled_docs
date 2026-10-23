---
url: https://docs.comfy.org/tutorials/3d/pixal3d/
title: Pixal3D Image to 3D Model ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:16.438358+00:00
---

# Pixal3D Image to 3D Model ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/3d/pixal3d/

## On this page

  * Pixal3D: Image to 3D Model
  * Pixal3D: Multi Views to 3D
  * How it works
  * Steps to run
  * Model downloads
    * Model storage location



3D

# Pixal3D Image to 3D Model ComfyUI Workflow Example

Copy pageCopy page

Generate high-fidelity 3D models with full PBR textures from a single image using Pixal3D, a pixel-aligned image-to-3D model from Tencent ARC.

Copy pageCopy page

**Pixal3D** is an open-source image-to-3D model from Tencent ARC, presented at SIGGRAPH 2026. It turns a single image into a high-fidelity 3D asset with full PBR materials. Most 3D-native generators synthesize shapes in a canonical space and inject image cues through attention, which leaves pixel-to-3D associations ambiguous. Pixal3D instead uses pixel-aligned generation: it establishes direct pixel-to-3D correspondence through back-projection, so the front of the generated model matches your input image 1:1, with no warped or misaligned textures.

### 

​

Pixal3D: Image to 3D Model

Upload a single image. Generate a high-fidelity 3D model with full PBR textures, aligned to your input view. This workflow also includes the TRELLIS.2 pipeline. The `Boolean (Switch to Trellis2)` node defaults to `false`, which runs the Pixal3D pipeline and loads the Pixal3D model automatically. ![Pixal3D workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_trellis2_image_to_model-1.webp)

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

## Run on Comfy Cloud

Run this workflow instantly on Comfy Cloud

## Download Workflow

Download JSON or search “Pixal3D & TRELLIS.2: Image to Model” in Template Library

**Input materials** Upload this file to the `LoadImage` node:

## viking_wolf_rune_axe.png

`LoadImage` node 122 · `viking_wolf_rune_axe.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/viking_wolf_rune_axe.png)

### 

​

Pixal3D: Multi Views to 3D

Generate a 3D model from a character turnaround sheet (front, side, and back views on one image). The multiview model uses the extra viewpoints to reconstruct geometry the single-image pipeline cannot see, which gives more accurate side and back profiles. Use the `Character Turnaround Sheet Generator` template in the template library to produce the turnaround sheet with Nano Banana 2, or prepare your own multi-view image with the subject separated from the background. ![Pixal3D Multi Views workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_multi_views-1.webp)

## Run on Comfy Cloud

Run this workflow instantly on Comfy Cloud

## Download Workflow

Download JSON or search “Pixal3D: Multi Views to 3D” in Template Library

**Input materials** Upload this file to the `LoadImage` node:

## character_turnaround_4view_sheet.png

`LoadImage` node 364 · `character_turnaround_4view_sheet.png`

The workflow uses the models listed below. Download them and place them in the corresponding `models/` subdirectories:

## Pixal3D Multiview UNet

pixal3d_multiview_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## Shape VAE

trellis_2_shape_vae_bf16.safetensors → ComfyUI/models/vae/

## Texture VAE

trellis_2_texture_vae_bf16.safetensors → ComfyUI/models/vae/

## DINOv3 CLIP vision

dino_v3_L_naf_fp32.safetensors → ComfyUI/models/clip_vision/

## BiRefNet background removal

birefnet.safetensors → ComfyUI/models/background_removal/

## 

​

How it works

Pixal3D combines camera-aware, pixel-aligned generation with a complete mesh post-processing pipeline:

  1. **Background removal** : BiRefNet removes the background from the input image, and the workflow crops the subject to a centered canvas. A switch lets you skip background removal
  2. **Camera estimation** : MoGe estimates geometry and the camera field of view from the image. The FOV drives the pixel-aligned conditioning
  3. **Structure generation** : a sparse structure latent is sampled and decoded into voxels, then converted into a rough mesh
  4. **Shape refinement** : the shape stage and the upsampling stage refine the mesh up to the target resolution (1536)
  5. **Texture generation** : a texture diffusion stage produces PBR material voxels (base color, metallic, roughness)
  6. **Post-processing** : DC remesh, QEM decimation, UV unwrapping, and baking of base color, normal, and ambient occlusion maps into the final textured mesh



## 

​

Steps to run

  1. **Load an image** : use the `LoadImage` node to load a single image of the object
  2. **Queue the workflow** : press Ctrl (Cmd on macOS) + Enter
  3. **Wait for the pipeline** : the structure, shape, and texture stages run in sequence, followed by post-processing
  4. **View the result** : inspect the mesh in the `Preview3DAdvanced` node. The 3D model is saved to `ComfyUI/output/3d/ComfyUI/`



## 

​

Model downloads

Download the models used by this workflow. Both diffusion checkpoints are required: the switch selects which one runs. Place them in the corresponding `models/` subdirectories.

## Pixal3D UNet

pixal3d_int8_convrot.safetensors: Pixal3D diffusion model, loaded by default

## TRELLIS.2 UNet

trellis_2_int8_convrot.safetensors: TRELLIS.2 diffusion model, loaded when the switch is set to `true`

## Shape VAE

trellis_2_shape_vae_bf16.safetensors: VAE for structure and shape decoding

## Texture VAE

trellis_2_texture_vae_bf16.safetensors: VAE for texture decoding

## DINOv3 CLIP vision

dino_v3_L_naf_fp32.safetensors: CLIP vision encoder for image conditioning

## MoGe geometry

moge_2_vitl_normal_fp16.safetensors: depth and camera estimation for pixel-aligned conditioning

## BiRefNet background removal

birefnet.safetensors: background removal model for preprocessing

### 

​

Model storage location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      ├── pixal3d_int8_convrot.safetensors
    │   │      └── trellis_2_int8_convrot.safetensors
    │   ├── 📂 vae/
    │   │      ├── trellis_2_shape_vae_bf16.safetensors
    │   │      └── trellis_2_texture_vae_bf16.safetensors
    │   ├── 📂 clip_vision/
    │   │      └── dino_v3_L_naf_fp32.safetensors
    │   ├── 📂 geometry_estimation/
    │   │      └── moge_2_vitl_normal_fp16.safetensors
    │   └── 📂 background_removal/
    │          └── birefnet.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/3d/pixal3d.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/3d/pixal3d)

[ComfyUI Hunyuan3D-2 ExamplesPrevious](https://docs.comfy.org/tutorials/3d/hunyuan3D-2)[TRELLIS.2 Image to 3D Model ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/3d/trellis2)

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
