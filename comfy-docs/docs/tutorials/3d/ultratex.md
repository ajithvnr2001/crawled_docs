---
url: https://docs.comfy.org/tutorials/3d/ultratex/
title: UltraTex in ComfyUI: Texture a 3D Model From One Image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:30.169825+00:00
---

# UltraTex in ComfyUI: Texture a 3D Model From One Image - ComfyUI

> Source: https://docs.comfy.org/tutorials/3d/ultratex/

## On this page

Back to top

  * Texture a 3D model
  * What to change
  * Before you run
  * Model downloads



3D

# UltraTex in ComfyUI: Texture a 3D Model From One Image

Copy pageCopy page

Texture an untextured 3D mesh in ComfyUI with UltraTex on FLUX.2 Klein 9B: render six normal views, paint albedo and metallic/roughness, and bake a PBR GLB.

Copy pageCopy page

**UltraTex** textures a 3D mesh from a single reference image. It is a 2K multi-view texturing framework from SIGGRAPH Asia 2026, and in ComfyUI it runs on the FLUX.2 Klein base 9B backbone: the UltraTex LoRAs repaint that model into a texture generator, and the UltraTex VAE keeps the rendered views clean. Point it at an untextured mesh plus one picture of how the object should look. The workflow renders the mesh from six world-normal views, paints albedo in one pass and metallic/roughness in another, bakes both onto the mesh UVs, and saves a PBR GLB with the PNG maps. It needs ComfyUI **0.46.0+** and template pack **0.11.115+**.

## Texture a 3D model

Load your mesh in **Load 3D (Advanced)** and the reference image in **Load Image** , then run the workflow. The template ships with a frog statuette mesh and its painted version, so it runs as downloaded. ![UltraTex texturing a frog statuette mesh from one reference image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_ultratex_texture_3d_model-1.webp)

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

## Download Workflow

Download JSON or search “UltraTex: Texture a 3D Model” in Template Library

**Input materials**

## sir_frog.obj

The mesh to texture, opened in Load 3D (Advanced)

## sir_frog.png

The reference: how the object should look

## What to change

  * **Load 3D (Advanced)** : your mesh and the camera the front view is taken from. The bake reuses that same camera rig.
  * **Load Image** : the reference seen from the front camera’s side, because it lands on the front view. Keep one object in one orientation.
  * **Rendered Mesh Resolution** (1024) sizes the renders and the latent. **Texture Resolution** (4096) sizes the baked maps.
  * **Albedo pass** runs 4 steps at seed 1. **Metallic/roughness pass** runs 8 steps at seed 4.
  * **Camera orbit** is pinned to four side views plus top and bottom, six views in total. UltraTex Conditioning accepts only that six-view set or the four side views alone, so a reduced orbit needs a matching latent batch size of 4.



## Before you run

  * The mesh must already have UVs. The bake and the apply step reuse them, and there is no unwrap step.
  * Seeds change surface detail only. The silhouette always comes from the mesh.
  * `fill_unseen` grows colour into texels no view saw. Turn it off to keep the mesh’s own texture in those areas.



## Model downloads

Seven files go under `ComfyUI/models`. The shipped graph needs 13.16 GB; swapping the checkpoint to the full-precision build brings it to 21.87 GB.

## Diffusion model: flux-2-klein-base-9b_int8_convrot.safetensors

FLUX.2 Klein base 9B, INT8, 9.44 GB. Place in `ComfyUI/models/diffusion_models/`

## Distillation LoRA: flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors

Loaded at strength 0.5, 1.96 GB. Place in `ComfyUI/models/loras/`

## Albedo LoRA: ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors

Albedo pass, 478 MB. Place in `ComfyUI/models/loras/`

## Metallic/roughness LoRA: ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors

Metallic/roughness pass, 478 MB. Place in `ComfyUI/models/loras/`

## Embedding: flux-2-klein-9b_empty_prompt.safetensors

Pre-encoded empty prompt, 25 MB. Place in `ComfyUI/models/embeddings/`

## VAE: ultratex_flux2_vae_fp32.safetensors

UltraTex VAE, FP32, 336 MB. Place in `ComfyUI/models/vae/`

## Background removal: birefnet.safetensors

Masks the reference image, 444 MB. Place in `ComfyUI/models/background_removal/`

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── flux-2-klein-base-9b_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   ├── flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors
    │   │   ├── ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors
    │   │   └── ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors
    │   ├── 📂 embeddings/
    │   │   └── flux-2-klein-9b_empty_prompt.safetensors
    │   ├── 📂 vae/
    │   │   └── ultratex_flux2_vae_fp32.safetensors
    │   └── 📂 background_removal/
    │       └── birefnet.safetensors
    

The graph loads no text encoder: `Load Conditioning` reads the pre-encoded empty prompt instead. Model weights carry the [FLUX Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B/blob/main/LICENSE.md). Paper and code: [UltraTex on arXiv](https://arxiv.org/abs/2609.23169), [yiboz2001/UltraTex](https://github.com/yiboz2001/UltraTex).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/3d/ultratex.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/3d/ultratex)

[OmniGen2](https://docs.comfy.org/tutorials/image/omnigen/omnigen2)[Pixal3D](https://docs.comfy.org/tutorials/3d/pixal3d)
