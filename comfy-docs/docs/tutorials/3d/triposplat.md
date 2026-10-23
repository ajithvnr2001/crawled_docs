---
url: https://docs.comfy.org/tutorials/3d/triposplat/
title: TripoSplat Image to Gaussian Splat ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:16.568817+00:00
---

# TripoSplat Image to Gaussian Splat ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/3d/triposplat/

## On this page

  * TripoSplat: Image to Gaussian Splat
  * How it works
  * Workflow node guide
    * LoadImage
    * TripoSplat (subgraph)
    * CreateCameraInfo
    * RenderSplat
    * SplatToMesh
    * SaveGLB
    * SaveVideo
    * SplatToFile3D
    * CreateVideo
  * Steps to run
  * Output options
  * Model downloads
    * Model storage location



3D

# TripoSplat Image to Gaussian Splat ComfyUI Workflow Example

Copy pageCopy page

Generate high-quality 3D Gaussian splat representations from a single 2D image using TripoSplat, with controllable density and budget for rendering.

Copy pageCopy page

**TripoSplat** is an open-source model that generates **3D Gaussian splat** representations directly from a single 2D image. It was developed by VAST-AI and released under an open-source license. Unlike traditional 3D reconstruction methods that require multiple views or generate meshes as the primary output, TripoSplat creates **Gaussian splat** representations: a rendering technique where thousands of colored 3D Gaussians are placed in space to represent a scene. This approach enables fast, high-quality rendering with controllable density and budget.

### 

​

TripoSplat: Image to Gaussian Splat

Upload a single 2D image. Generate a high-quality 3D Gaussian splat representation with controllable density and budget for rendering. ![TripoSplat workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_triposplat_image_to_gaussian_splat-1.webp)

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

Download JSON or search “TripoSplat: Image to Gaussian Splat” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## white-hotel-on-rocky-island.png

`LoadImage` node 99 · `white-hotel-on-rocky-island.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/white-hotel-on-rocky-island.png)

## 

​

How it works

TripoSplat uses a **feed-forward architecture** that takes a single RGB image and directly predicts a set of 3D Gaussian primitives. The pipeline involves:

  1. **Image encoding** : the input image is processed by a vision encoder (DINOv2)
  2. **Triplane generation** : features are decoded into a triplane representation
  3. **Gaussian prediction** : the triplane is sampled to produce Gaussian parameters (position, scale, rotation, opacity, color)
  4. **Rendering** : Gaussians are rendered from arbitrary viewpoints using differentiable splatting



## Learn about Subgraph

This workflow uses a Subgraph node for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

## 

​

Workflow node guide

### 

​

LoadImage

  * Loads your input image (PNG/JPG)
  * Sample image: `white-hotel-on-rocky-island.png` (available in Template Library)



### 

​

TripoSplat (subgraph)

The main subgraph node processes the image and generates the 3D Gaussian splat. Exposed parameters:

Parameter| Default| Description  
---|---|---  
`switch`| —| Enable/disable the subgraph  
`num_gaussians`| —| Number of Gaussian primitives to generate (controls quality/performance)  
`seed`| —| Random seed for reproducibility  
`unet_name`| —| TripoSplat diffusion model checkpoint  
`clip_name`| —| CLIP vision encoder model  
`vae_name`| —| VAE for encoding/decoding (2 entries: one for the main VAE, one for the encoder)  
`bg_removal_name`| —| Background removal model  
  
### 

​

CreateCameraInfo

  * Defines the camera orbit for rendering the result
  * Parameters: orbit type, angle, distance, field of view, etc.
  * Default: orbit at 35° elevation, 30 distance, 2.5 zoom



### 

​

RenderSplat

  * Renders the Gaussian splat into a 2D image from the defined camera angle
  * Parameters: output resolution (default 1024×1024), image quality settings



### 

​

SplatToMesh

  * Converts the Gaussian splat to a mesh (optional)
  * Parameters: mesh density, smoothing, simplification



### 

​

SaveGLB

  * Saves the result as a GLB 3D file



### 

​

SaveVideo

  * Saves a video of the rendered 3D scene



### 

​

SplatToFile3D

  * Exports the Gaussian splat in SPZ format



### 

​

CreateVideo

  * Creates a video from rendered frames



## 

​

Steps to run

  1. **Load an image** : use the **LoadImage** node to load a single 2D image
  2. **Run the TripoSplat subgraph** : the model will generate a Gaussian splat representation
  3. **Choose output format** : export as GLB, SPZ, video, or render to mesh
  4. **View results** : use the created 3D file or rendered preview



## 

​

Output options

Node| Format| Use case  
---|---|---  
**SaveGLB**| `.glb`| Standard 3D file format, importable into 3D software  
**SplatToFile3D**| `.spz`| Compressed Gaussian splat format for efficient storage  
**RenderSplat**|  2D image| Quick preview of the result from any angle  
**SplatToMesh**|  Mesh| Convert to traditional mesh for further editing  
  
## 

​

Model downloads

Download the TripoSplat model and required files. Place them in the corresponding `models/` subdirectories.

## TripoSplat diffusion

triposplat_fp16.safetensors: TripoSplat diffusion model checkpoint

## TripoSplat VAE decoder

triposplat_vae_decoder_fp16.safetensors: VAE decoder

## Flux2 VAE

flux2-vae.safetensors: FLUX.2 VAE for latent encoding

## DINOv2 CLIP

dino_v3_vit_h.safetensors: CLIP vision encoder (DINOv2)

## BiRefNet bg removal

birefnet.safetensors: Background removal model for preprocessing

### 

​

Model storage location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      └── triposplat_fp16.safetensors
    │   ├── 📂 vae/
    │   │      ├── triposplat_vae_decoder_fp16.safetensors
    │   │      └── flux2-vae.safetensors
    │   ├── 📂 clip_vision/
    │   │      └── dino_v3_vit_h.safetensors
    │   └── 📂 background_removal/
    │          └── birefnet.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/3d/triposplat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/3d/triposplat)

[ComfyUI OmniGen2 Native Workflow ExamplesPrevious](https://docs.comfy.org/tutorials/image/omnigen/omnigen2)[ComfyUI Hunyuan3D-2 ExamplesNext](https://docs.comfy.org/tutorials/3d/hunyuan3D-2)

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
