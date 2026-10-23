---
url: https://docs.comfy.org/tutorials/image/mage-flow/mage-flow/
title: Mage-Flow: ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:22.516967+00:00
---

# Mage-Flow: ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/mage-flow/mage-flow/

## On this page

  * Mage-Flow text-to-image workflow
    * Single-click generation
    * Using the workflow
  * Mage-Flow Turbo text-to-image workflow
  * Mage-Flow-Edit image edit workflow
    * Using image edit
  * Mage-Flow-Edit Turbo image edit workflow
    * Model downloads



Mage-Flow

# Mage-Flow: ComfyUI Workflow Example

Copy pageCopy page

Mage-Flow is Microsoft’s compact 4B model for text-to-image generation and instruction-based image editing in ComfyUI, with native resolutions up to 2K.

Copy pageCopy page

**Mage-Flow** is a compact 4B-scale generative stack from Microsoft Research for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: [Mage-VAE](https://huggingface.co/microsoft/Mage-VAE), a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer (NR-MMDiT) trained with rectified flow matching. Together with native-resolution packing, this shared stack powers two model instantiations: Mage-Flow for text-to-image generation and Mage-Flow-Edit for instruction-based image editing. Each ships in Base, RL-aligned, and 4-step Turbo variants. Mage-Flow supports native resolutions from 512 to 2048 pixels per side at any aspect ratio, including extreme dimensions like 4:1. **License** : [MIT](https://github.com/microsoft/Mage/blob/main/LICENSE) **Related Links** :

  * [Hugging Face: microsoft/Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)
  * [Hugging Face: Comfy-Org/Mage-Flow (ComfyUI models)](https://huggingface.co/Comfy-Org/Mage-Flow)
  * [Official GitHub repository](https://github.com/microsoft/Mage)
  * [Technical report (arXiv)](https://arxiv.org/abs/2607.19064)



## 

​

Mage-Flow text-to-image workflow

![Mage-Flow text-to-image workflow output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Mage_flow.png)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Mage-Flow” in Template Library

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

The workflow is organized into a few parts:

  1. **Text to Image (Mage-Flow) subgraph** : the core generation pipeline, containing model loading, prompt handling, native-resolution latent generation, sampling, and VAE decode
  2. **SaveImageAdvanced** : saves the generated image



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Single-click generation

At its simplest, just enter a text prompt in the subgraph, set your desired resolution, and click **Queue Prompt**. The defaults produce a high-quality image with minimal configuration.

### 

​

Using the workflow

  1. **Enter a prompt** — type a text description in the subgraph’s prompt input
  2. **Set resolution** — adjust width and height for your desired output size. Mage-Flow supports native resolutions from 512 to 2048 pixels per side.
  3. **Adjust settings** — configure the seed and negative prompt as needed
  4. **Click Queue** — press `Ctrl+Enter` to generate



## 

​

Mage-Flow Turbo text-to-image workflow

![Mage-Flow Turbo text-to-image workflow output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Mage_flow_turbo.png)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Mage-Flow Turbo” in Template Library

The Turbo variant uses a distilled 4-step checkpoint for faster generation while maintaining high quality. The workflow structure and controls are identical to the base text-to-image workflow, but uses the Turbo diffusion model for lower-latency inference.

## 

​

Mage-Flow-Edit image edit workflow

![Mage-Flow-Edit image edit workflow output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Mage_flow_edit.png)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Mage-Flow-Edit” in Template Library

## Download Sample Image

Get the example input image for this workflow

The image edit workflow uses Mage-Flow-Edit, an instruction-based model that edits images using natural language descriptions. Upload one or more reference images and describe the desired edit. The workflow is organized into a few parts:

  1. **LoadImage** : upload your reference images (up to 3)
  2. **Image Edit (Mage-Flow-Edit) subgraph** : the core editing pipeline containing model loading, reference image conditioning, prompt handling, and sampling
  3. **ImageCompare** : a side-by-side comparison of the original and edited image
  4. **SaveImage** : saves the edited output



### 

​

Using image edit

  1. **Upload reference images** — use the **LoadImage** node to load the image you want to edit (up to 3 images)
  2. **Enter your edit instruction** — type a text description of the edit you want to apply (e.g., “replace the background with a beach scene” or “turn this into a watercolor painting”)
  3. **Adjust settings** — configure resolution, seed, and other parameters
  4. **Click Queue** — press `Ctrl+Enter` to generate



## 

​

Mage-Flow-Edit Turbo image edit workflow

![Mage-Flow-Edit Turbo image edit workflow output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Mage_flow_edit_turbo.png)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Mage-Flow-Edit Turbo” in Template Library

## Download Sample Image

Get the example input image for this workflow

The Turbo variant of the edit workflow uses a distilled 4-step checkpoint for faster editing. The structure and controls match the base edit workflow but with reduced sampling steps.

### 

​

Model downloads

For local use, download the ComfyUI-optimized model files from [Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow).

## Text Encoder

qwen3vl_4b_bf16.safetensors: Qwen3VL-4B text encoder

## VAE

mage_flow_vae_bf16.safetensors

## Diffusion Model (Base Int8)

mage_flow_int8_convrot.safetensors: Base model used in the T2I workflow

## Diffusion Model (Turbo Int8)

mage_flow_turbo_int8_convrot.safetensors: Turbo model used in the Turbo T2I workflow

## Diffusion Model (Edit Int8)

mage_flow_edit_int8_convrot.safetensors: Edit model used in the Edit workflow

## Diffusion Model (Edit Turbo Int8)

mage_flow_edit_turbo_int8_convrot.safetensors: Edit Turbo model used in the Edit Turbo workflow

Other model variants (BF16, FP8) are also available for users with different hardware configurations. Place the files in the following directories:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── mage_flow_int8_convrot.safetensors
    │   │   ├── mage_flow_turbo_int8_convrot.safetensors
    │   │   ├── mage_flow_edit_int8_convrot.safetensors
    │   │   └── mage_flow_edit_turbo_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_4b_bf16.safetensors
    │   └── 📂 vae/
    │       └── mage_flow_vae_bf16.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/mage-flow/mage-flow.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/mage-flow/mage-flow)

[ComfyUI Ideogram 4.0 Open-Source Model TutorialPrevious](https://docs.comfy.org/tutorials/image/ideogram/ideogram-v4)[Ming Image 0.1 Design: RGBA Text to Image in ComfyUINext](https://docs.comfy.org/tutorials/image/ming-image/ming-image-0-1-design)

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
