---
url: https://docs.comfy.org/tutorials/image/ideogram/ideogram-v4/
title: ComfyUI Ideogram 4.0 Open-Source Model Tutorial - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:21.821430+00:00
---

# ComfyUI Ideogram 4.0 Open-Source Model Tutorial - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/ideogram/ideogram-v4/

## On this page

  * Ideogram 4.0 Text-to-Image Workflow
    * Ideogram v4: Text to Image
    * Prompt Format
    * Ideogram 4.0 model downloads
    * Workflow Steps
    * Note on Safety Filter
  * Live Conversation with Ideogram & ComfyOrg



Ideogram

# ComfyUI Ideogram 4.0 Open-Source Model Tutorial

Copy pageCopy page

Ideogram 4.0 in ComfyUI: run Ideogram’s open-source text-to-image model locally, with accurate text rendering and JSON or natural-language style prompts.

Copy pageCopy page

Ideogram 4.0 is the latest text-to-image model from Ideogram, released as an open-source model that runs entirely on your own hardware. It delivers superior photorealistic quality, accurate text rendering, and precise style control. You can use either plain natural language or **structured JSON prompts** for fine-grained control over layout, colors, and in-image text.

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

Ideogram 4.0 Text-to-Image Workflow

### 

​

Ideogram v4: Text to Image

Input a text prompt or structured JSON description. Generate an image with precise layout, color, and style control using Ideogram 4.0. ![Ideogram 4.0 text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ideogram4_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ideogram v4: Text to Image” in Template Library

**Example output** ![Ideogram 4.0 example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_ideogram4_t2i.png)

### 

​

Prompt Format

The open-source workflow supports two prompt modes:

  1. **Natural language** : Quick and easy, best for simple ideas
  2. **Structured JSON** : For precise control over layout, colors, and style

The workflow includes a prompt construction template that you can use with any LLM to generate matching JSON prompts. A note inside the workflow explains:

> The model is trained on structured JSON captions (scene summary, style block, background, and optional per-object descriptions with bounding boxes and hex color palettes). Official inference validates prompts against that schema.

### 

​

Ideogram 4.0 model downloads

You can find all repackaged model files at [Comfy-Org/Ideogram-4](https://huggingface.co/Comfy-Org/Ideogram-4) on Hugging Face.

## ideogram4_fp8_scaled.safetensors

Diffusion model for Ideogram 4.0 (~13.8 GB). Place in `models/diffusion_models/`

## ideogram4_unconditional_fp8_scaled.safetensors

Unconditional diffusion model for Ideogram 4.0 (~13.8 GB). Place in `models/diffusion_models/`

## qwen3vl_8b_fp8_scaled.safetensors

Text encoder for Ideogram 4.0 (~8 GB). Place in `models/text_encoders/`

## gemma4_e4b_it_fp8_scaled.safetensors

Text encoder for Ideogram 4.0 (~2 GB). Place in `models/text_encoders/`

## flux2-vae.safetensors

VAE for Ideogram 4.0 (~335 MB). Place in `models/vae/`

**Model storage location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── ideogram4_fp8_scaled.safetensors
    │   │   └── ideogram4_unconditional_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen3vl_8b_fp8_scaled.safetensors
    │   │   └── gemma4_e4b_it_fp8_scaled.safetensors
    │   └── 📂 vae/
    │       └── flux2-vae.safetensors
    

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check the Subgraph documentation to learn how to customize and extend.

### 

​

Workflow Steps

  1. Download and place the models in the correct directories (see table above)
  2. Download and drag the workflow file into ComfyUI
  3. Enter your prompt (natural language or structured JSON) in the Ideogram4 subgraph node
  4. (Optional) Adjust resolution using the `ResolutionSelector` node
  5. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
  6. View the result in the `Save Image` node. Output files are saved to `ComfyUI/output/`



### 

​

Note on Safety Filter

If you see “Image blocked by safety filter”, this is Ideogram 4.0’s built-in safety filter. Non-JSON (plain-text) prompts have a higher false-positive rate. Using structured JSON prompts reduces the chance of your prompt being blocked. For more details, see [Ideogram 4’s official prompting guide](https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md#safety-filter).

## 

​

Live Conversation with Ideogram & ComfyOrg

A special live conversation with Mohammad Norouzi (CEO, Ideogram) and Yoland Yan (CEO, ComfyOrg), hosted by Purz & Rob.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/ideogram/ideogram-v4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/ideogram/ideogram-v4)

[Krea-2 ComfyUI Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/krea/krea-2)[Mage-Flow: ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/image/mage-flow/mage-flow)

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
