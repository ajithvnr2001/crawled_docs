---
url: https://docs.comfy.org/tutorials/image/krea/krea-2/
title: Krea-2 ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:22.093535+00:00
---

# Krea-2 ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/krea/krea-2/

## On this page

  * Watch the Launch Event
  * Available Model Weights
  * Krea-2 Turbo text-to-image workflow
    * Krea-2: Text to Image
    * Single-click generation
    * Workflow controls
    * Style LoRAs
    * Model downloads
    * Model storage location
  * Krea-2 Turbo style reference workflow
    * Krea-2 Int8: Image Style Reference
    * Using style reference



Krea 2

# Krea-2 ComfyUI Workflow Example

Copy pageCopy page

Krea 2 is a text-to-image model designed for high aesthetic quality and stylistic diversity. It comes in two variants: RAW (base) and Turbo (distilled).

Copy pageCopy page

**Krea 2** is an image generation model from [Krea AI](https://www.krea.ai), trained from scratch and focused on creative and stylistic exploration. Krea 2 ships as two models designed to work together: **train LoRAs on RAW, run inference on Turbo** :

  * **Krea 2 RAW** : the base model with full-step sampling (52 steps). No distillation, diverse and highly malleable, ideal for fine-tuning and LoRA training.
  * **Krea 2 Turbo** : an 8-step distilled checkpoint for fast, high-quality generation. LoRAs trained on RAW apply seamlessly to Turbo.

**License** : [Krea AI Community License](https://www.krea.ai/krea-2-licensing)

## 

​

Watch the Launch Event

To learn more about Krea 2, the story behind its development, its capabilities, and what it means for the open-source ecosystem, watch the launch event recording above (featuring Victor Perez, Miguel Lara, and ComfyAnonymous).

## 

​

Available Model Weights

Krea 2 is available in two variants:

  * **Krea 2 RAW** : the base model with full-step sampling (52 steps). Designed for diversity and malleability, best for fine-tuning and LoRA training.
  * **Krea 2 Turbo** : an 8-step distilled checkpoint built for fast, high-quality generation. LoRAs trained on RAW apply seamlessly to Turbo.

**Related Links** :

  * [Krea 2 on Hugging Face (RAW)](https://huggingface.co/krea/Krea-2-Raw)
  * [Krea 2 on Hugging Face (Turbo)](https://huggingface.co/krea/Krea-2-Turbo)
  * [Comfy-Org/Krea-2 (ComfyUI models)](https://huggingface.co/Comfy-Org/Krea-2)
  * [Official GitHub repository](https://github.com/krea-ai/krea-2)
  * [Prompting guidelines](https://github.com/krea-ai/krea-2/blob/main/docs/prompting.md)
  * [Technical report](https://www.krea.ai/blog/krea-2-technical-report)



## 

​

Krea-2 Turbo text-to-image workflow

### 

​

Krea-2: Text to Image

Generate images from text prompts using Krea 2, a foundation model built for aesthetic quality and creative control. It focuses on rendering expressive, stylistically diverse images. ![Krea-2 Turbo text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Krea-2” in Template Library

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

  1. **Text to Image (Krea-2 Turbo) subgraph** : the core generation pipeline, containing model loading, prompt handling, sampling, and VAE decode
  2. **ResolutionSelector** : choose your desired output resolution. Krea 2 supports outputs from 1K to 2K. Set the megapixels value to 2.0 to get 2K resolution.
  3. **CustomCombo (LoRA selector)** : a pre-built trigger word selector for the available style LoRAs. If you download additional LoRAs, you can customize this selector and pair them with the corresponding LoRA files accordingly.
  4. **SaveImage** : saves the generated image



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Single-click generation

At its simplest, just enter a text prompt in the subgraph, select a resolution, and click **Queue Prompt**. The defaults (8 steps, prompt enhancement enabled, no LoRA) produce a high-quality image with minimal configuration.

### 

​

Workflow controls

The **Text to Image (Krea-2 Turbo)** subgraph exposes the following controls:

Control| Description  
---|---  
**Text String (User Prompt)**|  The text prompt describing the image you want to generate  
**prompt_enhance**|  Toggle LLM-powered prompt expansion on/off  
**LLM_max_token**|  Maximum token length for prompt enhancement  
**Width / Height**|  Output resolution (controlled by ResolutionSelector)  
**Seed**|  Random seed for reproducibility  
**enable_lora?**|  Enable or disable style LoRA  
**LoRA Strength**|  Strength of the applied style LoRA  
**LoRA Trigger Word**|  Auto-populated trigger word for the selected LoRA  
  
### 

​

Style LoRAs

Krea also released a collection of style LoRAs for Krea 2. Select one in the **CustomCombo** node and enable `enable_lora?` in the subgraph to apply the style:

LoRA| Trigger Word| Recommended Strength| Download  
---|---|---|---  
krea2_darkbrush| monochrome ink wash style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_darkbrush.safetensors)  
krea2_dotmatrix| monochrome stippling style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_dotmatrix.safetensors)  
krea2_kidsdrawing| naive expressive sketch style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_kidsdrawing.safetensors)  
krea2_neondrip| textured abstract style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_neondrip.safetensors)  
krea2_rainywindow| rainy window style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_rainywindow.safetensors)  
krea2_retroanime| purple retro anime style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_retroanime.safetensors)  
krea2_softwatercolor| art deco watercolor style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_softwatercolor.safetensors)  
krea2_sunsetblur| ethereal motion blur style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_sunsetblur.safetensors)  
krea2_vintagetarot| vintage tarot style| 1.0| [Download](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_vintagetarot.safetensors)  
  
Place the `.safetensors` files in `ComfyUI/models/loras/`.

### 

​

Model downloads

For local use, download the ComfyUI-optimized model files from [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2).

## Diffusion Model (FP8)

krea2_turbo_fp8_scaled.safetensors: Turbo FP8 (recommended for most users)

## Text Encoder (FP8)

qwen3vl_4b_fp8_scaled.safetensors: Qwen3VL-4B text encoder

## VAE

qwen_image_vae.safetensors

## Style LoRAs

View all style LoRAs on Hugging Face

Other model variants (BF16, NVFP4, MXFP8) are also available for users with higher-end hardware.

#### 

​

Model storage location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── krea2_turbo_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_4b_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── qwen_image_vae.safetensors
    │   └── 📂 loras/
    │       └── krea2_softwatercolor.safetensors (and other style LoRAs)
    

## 

​

Krea-2 Turbo style reference workflow

### 

​

Krea-2 Int8: Image Style Reference

Generate images with the Krea-2 Turbo model while referencing the style of 1–2 uploaded images, using the high-performance Int8 Convrot format for fast inference. ![Krea-2 Turbo style reference workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_int8_image_style_reference-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Krea-2 Style Reference” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## krea2_reference_image.png

`LoadImage` node 69 · `krea2_reference_image.png`

![krea2_reference_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/krea2_reference_image.png)

**Example output** ![Krea-2 style reference example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_krea2_turbo_int8_image_style_reference.png) The style reference workflow builds on the Krea-2 Turbo pipeline by adding reference image conditioning. Upload one or more reference images to influence the aesthetic style, mood, and visual direction of the generated output. The workflow is organized into a few parts:

  1. **Image Style Reference (Krea-2 Turbo) subgraph** : the core generation pipeline with style reference support, containing model loading, reference image conditioning, prompt handling, and sampling
  2. **LoadImage** : upload your style reference images
  3. **ResolutionSelector** : choose your desired output resolution. Krea 2 supports outputs from 1K to 2K.
  4. **SaveImage** : saves the generated image



### 

​

Using style reference

  1. **Upload reference images** : use the **LoadImage** node to load one or more style reference images
  2. **Enter your prompt** : type a text description in the subgraph’s user prompt input
  3. **Select a model variant** : choose the model checkpoint in the subgraph’s model selector
  4. **Adjust settings** : configure resolution, seed, and optionally enable prompt enhancement
  5. **Click Queue** : press `Ctrl+Enter` to generate

This style reference workflow uses a dedicated diffusion model and LoRA. The text encoder and VAE are shared with the text-to-image workflow.

## Diffusion Model (INT8)

krea2_turbo_int8_convrot.safetensors

## Text Encoder (FP8)

qwen3vl_4b_fp8_scaled.safetensors: Qwen3VL-4B text encoder

## VAE

qwen_image_vae.safetensors

## Style Reference LoRA

krea2_style_reference.safetensors

Place the files in the following directories:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── krea2_turbo_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_4b_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── qwen_image_vae.safetensors
    │   └── 📂 loras/
    │       └── krea2_style_reference.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/krea/krea-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/krea/krea-2)

[PixelDiT ComfyUI Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/pixeldit/pixeldit)[ComfyUI Ideogram 4.0 Open-Source Model TutorialNext](https://docs.comfy.org/tutorials/image/ideogram/ideogram-v4)

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
