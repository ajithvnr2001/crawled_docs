---
url: https://docs.comfy.org/tutorials/utility/void-video-inpainting/
title: VOID: Video Inpainting in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:42.106238+00:00
---

# VOID: Video Inpainting in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/void-video-inpainting/

## On this page

  * Key strengths
  * VOID Video Inpainting Workflow
    * 1\. Download Workflow
    * VOID: Video Inpainting
    * 2\. Download Models
    * 3\. Using the Workflow
  * Additional Notes



Video

# VOID: Video Inpainting in ComfyUI

Copy pageCopy page

Learn how to remove objects from videos using the VOID video inpainting model by Netflix, natively supported in ComfyUI

Copy pageCopy page

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

VOID (Video Object Inpainting and Deletion) is a powerful video inpainting model open-sourced by Netflix. It uses a two-pass diffusion pipeline built on [CogVideoX](https://github.com/THUDM/CogVideo) to remove objects from videos and fill the resulting holes with temporally coherent content. VOID removes objects along with **all interactions they induce on the scene** , not just secondary effects like shadows and reflections, but physical interactions like objects falling when a person is removed. For example, if a person holding a guitar is removed, VOID also removes the person’s effect on the guitar, causing it to fall naturally. VOID is natively supported in ComfyUI (PR [#13403](https://github.com/Comfy-Org/ComfyUI/pull/13403)), and its complete model weights are available under the [Apache 2.0 License](https://github.com/Netflix/void-model?tab=Apache-2.0-1-ov-file). [VOID Model - GitHub](https://github.com/Netflix/void-model) | [Paper (arXiv)](https://arxiv.org/abs/2604.02296) | [🤗 Diffusers Pipeline](https://huggingface.co/netflix/void-model)

**Before** (left): the original footage with the snowboarder. **After** (right): the processed result after removing the snowboarder from the scene. VOID removes unwanted objects while maintaining natural motion, lighting, and scene coherence across frames.

### 

​

Key strengths

  * **Interaction-aware removal** : removes not just the object, but all physical interactions it caused on the scene (shadows, reflections, falling objects)
  * **Object removal** , not single-frame patching: produces coherent motion and lighting across the entire clip
  * **Two-pass refinement** : Pass 2 provides superior temporal stability (fewer jitters and flashes) compared to Pass 1 alone, especially on longer cuts or textured backgrounds



> **Limitations:** Unclear masks, chaotic motion, or targets that dominate the frame may still produce suboptimal results. Prompting cannot fix fundamentally wrong segmentation.

## 

​

VOID Video Inpainting Workflow

### 

​

1\. Download Workflow

Update your ComfyUI to the latest version, then go to `Workflow` -> `Browse Templates` and find “VOID: Video Inpainting” under the Utility category.

### 

​

VOID: Video Inpainting

Upload a video and mask the object you want to remove. Generate a clean video with the object and its physical interactions deleted. ![VOID video inpainting workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_void_video_inpainting-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “VOID: Video Inpainting” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## snowboarder.mp4

`LoadVideo` node 4 · `snowboarder.mp4`

### 

​

2\. Download Models

All models are hosted on the [Comfy-Org VOID model repository](https://huggingface.co/Comfy-Org/void-model). **Diffusion Models** : the core two-pass inpainting model:

  * [void_pass2.safetensors](https://huggingface.co/Comfy-Org/void-model/blob/main/diffusion_models/void_pass2.safetensors): Refinement pass, better temporal stability
  * [void_pass1.safetensors](https://huggingface.co/Comfy-Org/void-model/blob/main/diffusion_models/void_pass1.safetensors): Primary pass

**VAE:**

  * [cogvideox_vae.safetensors](https://huggingface.co/Comfy-Org/void-model/blob/main/vae/cogvideox_vae.safetensors)

**Optical Flow:**

  * [raft_large_C_T_SKHT_V2-ff5fadd5.safetensors](https://huggingface.co/Comfy-Org/void-model/blob/main/optical_flow/raft_large_C_T_SKHT_V2-ff5fadd5.safetensors)

**SAM3 Checkpoint** : for segmentation:

  * [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/blob/main/checkpoints/sam3.1_multiplex_fp16.safetensors)

**Text Encoder:**

  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors)


    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── sam3.1_multiplex_fp16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── t5xxl_fp16.safetensors
    │   ├── 📂 vae/
    │   │   └── cogvideox_vae.safetensors
    │   ├── 📂 optical_flow/
    │   │   └── raft_large_C_T_SKHT_V2-ff5fadd5.safetensors
    │   └── 📂 diffusion_models/
    │       ├── void_pass2.safetensors
    │       └── void_pass1.safetensors
    

### 

​

3\. Using the Workflow

**Inputs:**

  * **Source video** : Load a video via the `Load Video` node (place it in the ComfyUI `input/` folder)
  * **Positive prompt (inpaint fill)** : Describe the scene **after** removal. Focus on what remains and how it looks, not on what was removed 
    * Example: `empty kitchen counter, daylight, tiles visible`
  * **Negative prompt** : Optional anti-artifact list; can be left empty
  * **SAM3 object prompt** : A short label for **what** to mask out. SAM3 uses semantic understanding to create a segmentation mask for the target object. 
    * Example: `person in blue jacket`, `red cup on table`
    * Max tokens for SAM3 prompts is **32**. To prompt multiple subjects separately, separate with commas and use `:N` to specify the max objects detected per prompt: `eye:2, window panels:4`

**Modes:**

Prompt| Role  
---|---  
SAM3 object| **What** is removed (SAM3 creates the mask via semantic segmentation)  
Positive (inpaint)| **How** the hole is filled across time  
  
Use **Pass 2** (refinement pass) for longer clips or textured backgrounds where temporal stability matters. **Pass 1** alone is faster but may show more jitter.

## Learn about Subgraph

This workflow uses Subgraph nodes for modular video processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

## 

​

Additional Notes

  * **Mask quality matters** : a clean, tight mask around the target object produces the best results
  * **Prompt writing tip** : describe the scene as it should appear _naturally_ after removal, not the removal itself
  * **Use negative prompt** only when you see repeating defects (watermarks, blur, extra limbs)
  * **Two-pass workflow** : the template runs Pass 1 then Pass 2 automatically; you can also run just Pass 1 for faster iterations during testing



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/void-video-inpainting.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/void-video-inpainting)

[ComfyUI frame interpolation workflowPrevious](https://docs.comfy.org/tutorials/utility/frame-interpolation)[Comfy Cloud nodesNext](https://docs.comfy.org/cloud-nodes/overview)

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
