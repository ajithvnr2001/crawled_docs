---
url: https://docs.comfy.org/tutorials/flux/flux-2-klein/
title: FLUX.2 Klein in ComfyUI: Fast Text-to-Image and Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-08T14:09:48.010412+00:00
---

# FLUX.2 Klein in ComfyUI: Fast Text-to-Image and Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux-2-klein/

## On this page

Back to top

  * About FLUX.2 [klein]
  * FLUX.2 Klein 4B Workflows
    * FLUX.2 [Klein] 4B: Text to Image
    * FLUX.2 [Klein] 4B: Image Edit
    * FLUX.2 [Klein] 4B Distilled: Image Edit
  * FLUX.2 Klein 4B Model Downloads
  * FLUX.2 Klein 9B Workflows
    * FLUX.2 [Klein] 9B: Text to Image
    * FLUX.2 [Klein] 9B: Image Edit
    * FLUX.2 [Klein] 9B Distilled: Image Edit
  * FLUX.2 Klein 9B Model Downloads



FLUX

# FLUX.2 Klein in ComfyUI: Fast Text-to-Image and Editing

Copy pageCopy page

Run FLUX.2 Klein 4B in ComfyUI for text-to-image and multi-reference image editing, with a distilled variant that finishes in about one second.

Copy pageCopy page

## 

​

About FLUX.2 [klein]

FLUX.2 [Klein] is the fastest model in the FLUX family, unifying text-to-image and image editing in one compact architecture. It’s designed for interactive workflows, immediate previews, and latency-critical applications, with distilled variants delivering end-to-end inference around one second while keeping strong quality for single- and multi-reference editing. **Model highlights:**

  * Two 4B types: Base (undistilled) for maximum flexibility and fine-tuning; Distilled (4-step) for speed-first deployments
  * Performance: distilled ~1.2s (5090) · 8.4GB VRAM; base ~17s (5090) · 9.2GB VRAM
  * Editing support: style transforms, semantic edits, object replacement/removal, multi-reference composition, iterative edits



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

FLUX.2 Klein 4B Workflows

### 

​

FLUX.2 [Klein] 4B: Text to Image

![FLUX.2 Klein 4B text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_text_to_image-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## 4B Text-to-Image Workflow

Download the text-to-image workflow for FLUX.2 Klein 4B.

**Example output** ![FLUX.2 Klein 4B text-to-image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_klein_text_to_image.png)

### 

​

FLUX.2 [Klein] 4B: Image Edit

![FLUX.2 Klein 4B image edit base workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_base-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## 4B Image Edit Base

Download the image editing workflow using the 4B base model.

**Input materials** Upload these files to the matching `LoadImage` nodes:

## robed_women.png

`LoadImage` node 76 · `robed_women.png`

## pink_tone_chair.png

`LoadImage` node 81 · `pink_tone_chair.png`

![robed_women.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/robed_women.png)![pink_tone_chair.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/pink_tone_chair.png)

**Example output** ![FLUX.2 Klein 4B image edit base example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/thumbnail/image_flux2_klein_image_edit_4b_base.png)

### 

​

FLUX.2 [Klein] 4B Distilled: Image Edit

![FLUX.2 Klein 4B image edit distilled workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_distilled-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## 4B Image Edit Distilled

Download the fast distilled 4B image editing workflow.

**Input materials** Upload these files to the matching `LoadImage` nodes:

## handbag_white.png

`LoadImage` node 76 · `handbag_white.png`

## comfy_logo_blue.png

`LoadImage` node 81 · `comfy_logo_blue.png`

![handbag_white.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/handbag_white.png)![comfy_logo_blue.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/comfy_logo_blue.png)

**Example output** ![FLUX.2 Klein 4B image edit distilled example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_klein_image_edit_4b_distilled.png)

## 

​

FLUX.2 Klein 4B Model Downloads

## qwen_3_4b.safetensors

Text encoder for 4B models.

## flux-2-klein-base-4b-fp8.safetensors

Diffusion model (4B base).

## flux-2-klein-4b-fp8.safetensors

Diffusion model (4B distilled).

## flux2-vae.safetensors

VAE for 4B models.

**4B Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_4b.safetensors
    │   ├── 📂 diffusion_models/
    │   │      ├── flux-2-klein-base-4b-fp8.safetensors
    │   │      └── flux-2-klein-4b-fp8.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

## 

​

FLUX.2 Klein 9B Workflows

### 

​

FLUX.2 [Klein] 9B: Text to Image

![FLUX.2 Klein 9B text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image_9b-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## 9B Text-to-Image Workflow

Download the text-to-image workflow for FLUX.2 Klein 9B.

**Example output** ![FLUX.2 Klein 9B text-to-image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_text_to_image_9b.png)

### 

​

FLUX.2 [Klein] 9B: Image Edit

![FLUX.2 Klein 9B image edit base workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## 9B Image Edit Base

Download the image editing workflow using the 9B base model.

**Input materials** Upload these files to the matching `LoadImage` nodes:

## car_interior_white.jpeg

`LoadImage` node 76 · `car_interior_white.jpeg`

## comfy_logo_blue.png

`LoadImage` node 81 · `comfy_logo_blue.png`

![car_interior_white.jpeg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/car_interior_white.jpeg)![comfy_logo_blue.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/comfy_logo_blue.png)

**Example output** ![FLUX.2 Klein 9B image edit base example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/thumbnail/image_flux2_klein_image_edit_9b_base.png)

### 

​

FLUX.2 [Klein] 9B Distilled: Image Edit

![FLUX.2 Klein 9B image edit distilled workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_distilled-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## 9B Image Edit Distilled

Download the fast distilled 9B image editing workflow.

**Input materials** Upload these files to the matching `LoadImage` nodes:

## bold_outfit_woman.jpeg

`LoadImage` node 76 · `bold_outfit_woman.jpeg`

## handbag_white.png

`LoadImage` node 121 · `handbag_white.png`

![bold_outfit_woman.jpeg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/bold_outfit_woman.jpeg)![handbag_white.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/handbag_white.png)

**Example output** ![FLUX.2 Klein 9B image edit distilled example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_klein_image_edit_9b_distilled.png)

## 

​

FLUX.2 Klein 9B Model Downloads

For diffusion models, please visit BFL’s repo, accept the agreement, and then download the models.

## flux-2-klein-base-9b-fp8.safetensors

Diffusion model (9B base).

## flux-2-klein-9b-fp8.safetensors

Diffusion model (9B distilled).

## qwen_3_8b_fp8mixed.safetensors

Text encoder for 9B models.

## flux2-vae.safetensors

VAE for 9B models.

**9B Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      ├── flux-2-klein-9b-fp8.safetensors
    │   │      └── flux-2-klein-base-9b-fp8.safetensors
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_8b_fp8mixed.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux-2-klein.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux-2-klein)

[FLUX.2 Dev](https://docs.comfy.org/tutorials/flux/flux-2-dev)[FLUX.1 Krea Dev](https://docs.comfy.org/tutorials/flux/flux1-krea-dev)
