---
url: https://docs.comfy.org/tutorials/image/nvidia/pid-latent-upscale/
title: PiD Latent Upscale ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:22.868517+00:00
---

# PiD Latent Upscale ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/nvidia/pid-latent-upscale/

## On this page

  * How PiD works
    * Available PiD checkpoints
    * Subgraph settings
    * Steps to run
  * Model downloads
    * Model storage location
    * Sample output



PixelDiT

# PiD Latent Upscale ComfyUI Workflow Example

Copy pageCopy page

PiD (Pixel Diffusion Decoder) turns a diffusion latent into a 4x super-resolved image in 4 distilled pixel-space steps. No separate VAE decode needed.

Copy pageCopy page

**PiD (Pixel Diffusion Decoder)** turns a diffusion **latent** into a **4x super-resolved image** in 4 distilled pixel-space steps. No separate VAE decode needed. This workflow demonstrates using PiD to upscale a Z-Image-Turbo latent from **1024px to 4096px**. **Related Links** :

  * [Comfy-Org/PixelDiT on Hugging Face](https://huggingface.co/Comfy-Org/PixelDiT)
  * [nvidia/PixelDiT-1300M-1024px (official release)](https://huggingface.co/nvidia/PixelDiT-1300M-1024px)

![PiD Latent Upscale workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_pid_latent_upscale_dit-1.webp)

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

Download JSON or search “Image Upscale: PiD Latent Decode” in Template Library

## 

​

How PiD works

PiD matches checkpoints by the **VAE / latent space** of the upstream model (the encoder side), not the diffusion model name alone. You need to select the PiD checkpoint that corresponds to the latent space of the model used for initial generation. This workflow uses **Z-Image-Turbo** (1024px latent to 4096px output) which shares Flux.1’s 16-ch VAE.

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Available PiD checkpoints

All checkpoints are downloaded from [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT) to `models/diffusion_models/`.

Checkpoint| Input to Output| Compatible latent (VAE backbone)  
---|---|---  
[`pid_flux1_512_to_2048_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux1_512_to_2048_4step_bf16.safetensors)| 512 to 2048| Flux1-dev 16-ch VAE (Flux.1, Z-Image)  
[`pid_flux1_1024_to_4096_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux1_1024_to_4096_4step_bf16.safetensors)| 1024 to 4096| Flux1-dev 16-ch VAE (Flux.1, Z-Image) **(this workflow)**  
[`pid_flux2_512_to_2048_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux2_512_to_2048_4step_bf16.safetensors)| 512 to 2048| Flux2-dev 128-ch VAE (Flux.2)  
[`pid_flux2_1024_to_4096_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux2_1024_to_4096_4step_bf16.safetensors)| 1024 to 4096| Flux2-dev 128-ch VAE (Flux.2)  
[`pid_sd3_512_to_2048_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_sd3_512_to_2048_4step_bf16.safetensors)| 512 to 2048| SD3 medium 16-ch VAE  
[`pid_sd3_1024_to_4096_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_sd3_1024_to_4096_4step_bf16.safetensors)| 1024 to 4096| SD3 medium 16-ch VAE  
  
### 

​

Subgraph settings

Configure these on the **Latent Upscale Decode (PiD)** subgraph:

Setting| Value| Description  
---|---|---  
`latent_format`| `flux`| `flux` for Flux.1/Flux.2/Z-Image, `sd3` for SD3 (Flux.2 is auto-detected by 128 channels)  
`degrade_sigma`| `0.0`| How “finished” the input latent is. `0.0` for fully denoised (default), `0.1–0.8` for partially denoised, `1.0` for pure noise  
  
### 

​

Steps to run

  1. **Generate a latent**. Use a T2I workflow (e.g., Z-Image-Turbo) to produce a latent image.
  2. **Connect to PiD**. Feed the latent into the **Latent Upscale Decode (PiD)** subgraph node.
  3. **Select checkpoint**. Choose the PiD checkpoint matching your upstream model’s VAE latent space.
  4. **Set output size**. Set PiD output size to **4x** the input latent resolution.
  5. **Run**. The subgraph decodes and upscales in a single 4-step pass.



## 

​

Model downloads

PiD is part of the PixelDiT model family. This workflow also requires the Z-Image-Turbo model for initial generation.

## PiD Flux.1 1024 to 4096

pid_flux1_1024_to_4096_4step_bf16.safetensors: PiD checkpoint for Flux.1 / Z-Image latent space

## Z-Image-Turbo diffusion

z_image_turbo_bf16.safetensors: used for initial generation before PiD upscale

## Text Encoder (Z-Image)

qwen_3_4b.safetensors: text encoder for Z-Image-Turbo

## VAE (Z-Image)

ae.safetensors: VAE for Z-Image-Turbo

## Text Encoder (PiD)

gemma_2_2b_it_elm_fp8_scaled.safetensors: text encoder for PiD subgraph CLIPLoader (type: pixeldit)

> PiD uses a built-in **pixel_space** VAE. No separate VAE file is needed for PiD itself.

### 

​

Model storage location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      ├── qwen_3_4b.safetensors
    │   │      └── gemma_2_2b_it_elm_fp8_scaled.safetensors
    │   ├── 📂 diffusion_models/
    │   │      ├── pid_flux1_1024_to_4096_4step_bf16.safetensors
    │   │      └── z_image_turbo_bf16.safetensors
    │   └── 📂 vae/
    │          └── ae.safetensors
    

### 

​

Sample output

![PiD sample output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_pid_latent_upscale_dit-2.webp)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/nvidia/pid-latent-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/nvidia/pid-latent-upscale)

[PixelDiT ComfyUI Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/pixeldit/pixeldit)[Krea-2 ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/image/krea/krea-2)

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
