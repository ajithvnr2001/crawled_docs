---
url: https://docs.comfy.org/tutorials/video/wan/wan-causal-forcing/
title: Causal Forcing I2V ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:46.563038+00:00
---

# Causal Forcing I2V ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan-causal-forcing/

## On this page

  * How it works
    * Causal Forcing vs Causal Forcing++
  * Using the workflow
    * Inputs
    * WAN I2V subgraph parameters
  * Steps to run
  * Model downloads
    * Wan2.1 I2V
    * CLIP and VAE
    * Model storage location



Wan2.1

# Causal Forcing I2V ComfyUI Workflow Example

Copy pageCopy page

Generate videos from images using Causal Forcing or Causal Forcing++ with Wan2.1. Achieves smooth, temporally consistent video in as few as 1 inference step.

Copy pageCopy page

**Causal Forcing** is a video generation technique that applies **recurrent conditioning** during inference, where each generated frame is fed back into the model to predict the next frame. This produces smooth, temporally consistent videos from a single start image in as few as **1 to 4 inference steps**. This workflow uses **Wan2.1** and supports both **Causal Forcing** (standard) and **Causal Forcing++** (enhanced) modes. ![Causal Forcing I2V workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_causal_forcing_i2v-1.webp)

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

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Causal Forcing” in Template Library

**Input materials**

## girl_riding_a_wolf.png

Input image for the first frame. Download and use this image, or replace with your own.

## 

​

How it works

Unlike standard video generation which processes all frames in parallel, Causal Forcing treats video generation as a **sequential process** :

  1. The model takes an input image as the **first frame**
  2. It generates the next frame conditioned on the previous one
  3. Each new frame becomes the input for the next prediction
  4. This repeats for the desired number of frames

This recurrent approach creates **strong temporal consistency** : each frame naturally follows from the one before it. This can produce high-quality results with very few inference steps (1 to 4).

## Learn about Subgraph

This workflow uses a Subgraph node for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Causal Forcing vs Causal Forcing++

Mode| Description  
---|---  
**Causal Forcing**|  Standard recurrent conditioning. Good quality with 2–4 steps.  
**Causal Forcing++**|  Enhanced mode that applies additional conditioning for better temporal coherence. Works well with just 1–2 steps.  
  
## 

​

Using the workflow

### 

​

Inputs

The workflow accepts a single input image (the first frame) and a text prompt describing the desired video content (optional).

Setting| Description  
---|---  
**first_frame** (required)| The starting image for the video. Load a PNG/JPG via the **LoadImage** node.  
**positive_prompt** (optional)| A text description of the desired video content. Leave empty for no conditioning.  
**duration** (optional)| The number of frames to generate. Default: number of frames in the model’s expected output.  
  
### 

​

WAN I2V subgraph parameters

These are exposed as controls on the blueprint subgraph node: | Parameter | Default | Description | ||---|---|---| | `unet_name` | - | The Wan2.1 I2V model checkpoint to use | | `clip_name` | - | The CLIP / text encoder model for the prompt | | `vae_name` | - | The VAE model for encoding/decoding | | `width` | - | Output video width | | `height` | - | Output video height | | `noise_seed` | - | Seed for reproducibility |

## 

​

Steps to run

  1. **Load an image** : use the **LoadImage** node to load your starting frame
  2. **Write a prompt** (optional): describe the desired video content
  3. **Set duration** : how many frames to generate
  4. **Select models** : choose Wan2.1 I2V checkpoint, CLIP, and VAE
  5. **Choose mode** : Causal Forcing or Causal Forcing++ (set via the subgraph’s internal configuration or a Causal Forcing-specific input if available)
  6. **Run** : frames will be generated sequentially and saved to `ComfyUI/output/`



## 

​

Model downloads

Download the Wan2.1 I2V model and required files. Place them in the corresponding `models/` subdirectories.

### 

​

Wan2.1 I2V

## Wan2.1 I2V 14B

wan2.1_i2v_480p_14B_fp16.safetensors - Wan2.1 I2V 14B checkpoint

## Wan2.1 I2V 1.3B

wan2.1_t2v_1.3B_fp16.safetensors - Wan2.1 1.3B checkpoint (8GB VRAM minimum)

### 

​

CLIP and VAE

## CLIP (google-bert)

google-bert/bert-base-uncased - CLIP text encoder

## VAE (Wan2.1)

Wan2.1_VAE_bf16.safetensors - Wan2.1 VAE

### 

​

Model storage location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      └── wan2.1_i2v_480p_14B_fp16.safetensors (or 1.3B variant)
    │   ├── 📂 text_encoders/
    │   │      └── bert-base-uncased (folder with model.safetensors)
    │   └── 📂 vae/
    │          └── Wan2.1_VAE_bf16.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan-causal-forcing.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan-causal-forcing)

[ComfyUI Wan2.1 Video ExamplesPrevious](https://docs.comfy.org/tutorials/video/wan/wan-video)[ComfyUI Wan2.1 VACE Video ExamplesNext](https://docs.comfy.org/tutorials/video/wan/vace)

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
