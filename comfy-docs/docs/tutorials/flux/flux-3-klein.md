---
url: https://docs.comfy.org/tutorials/flux/flux-3-klein/
title: FLUX 3 Image Klein in ComfyUI: Text-to-Image and Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:20.387863+00:00
---

# FLUX 3 Image Klein in ComfyUI: Text-to-Image and Edit - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux-3-klein/

## On this page

  * About FLUX.3 [klein]
  * FLUX 3 Image Klein Workflows
    * FLUX 3 Image Klein: Text to Image
    * FLUX 3 Image Klein Distilled: Text to Image
    * FLUX 3 Image Klein: Image Edit
    * FLUX 3 Image Klein Distilled: Image Edit
  * FLUX 3 Image Klein Model Downloads
  * Prompting and reference tips



FLUX

# FLUX 3 Image Klein in ComfyUI: Text-to-Image and Edit

Copy pageCopy page

Run FLUX.3 [klein] locally in ComfyUI: open-weights text-to-image and instruction-driven image editing, with a distilled checkpoint for fast 4–16 step runs.

Copy pageCopy page

## 

​

About FLUX.3 [klein]

FLUX.3 [klein] is Black Forest Labs’ open-weights FLUX.3 image model for local ComfyUI: text-to-image and instruction-driven image editing in one family, with a full checkpoint and a step-distilled variant for faster 4–16 step runs. Weights ship on Hugging Face under the FLUX Kommunity License — download once, run on your own GPU, no API key and no per-image credits. Need the hosted path instead? FLUX.3 also runs as a Partner Node through [FLUX 3 Image](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-image) (billed per image). Use local klein weights on your GPU; use the Partner Node when you want the hosted model with no download. **Model highlights:**

  * Text-to-image and image editing from the same weights; edits take an instruction prompt plus reference images
  * Two checkpoints: full FLUX 3 Image Klein, and Distilled for guidance-free sampling in 4–16 steps
  * Multi-reference prompting via `<ref_image_0>`, `<ref_image_1>`, and so on
  * Optional Qwen3.5 9B prompt upsampler that expands short requests into full captions before generation
  * Single-file checkpoints in bf16, int8 (convrot), and nvfp4, with a Qwen3-VL-4B text encoder and the FLUX.2 VAE

**License** : [FLUX Kommunity License](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/blob/main/LICENSE.md) **Version requirement** : FLUX 3 Klein templates need ComfyUI 0.41.0 or later (shipped in the 0.41.1 backport, ComfyUI#17070).

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

FLUX 3 Image Klein Workflows

### 

​

FLUX 3 Image Klein: Text to Image

Generate an image from a prompt alone, with no input files. The workflow is a subgraph: open it to reach the loaders, the sampler, and the canvas size. ![FLUX 3 Image Klein text to image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Image Klein: Text to Image” in Template Library

  1. Enter your prompt in the subgraph’s positive prompt widget
  2. Set `width` and `height`, or pick a frame from `ResolutionSelector` (1:1 square by default)
  3. Adjust `steps` (50 by default) and `cfg` (3.5 by default)
  4. The prompt upsampler is on by default, so a short prompt is expanded by the Qwen3.5 9B upsampler before sampling. Turn `enable_prompt_upsampler` off to generate from your own words instead
  5. Click **Queue**. The image is saved by the `SaveImage` node to `ComfyUI/output/`



### 

​

FLUX 3 Image Klein Distilled: Text to Image

Generate an image from a prompt with the step-distilled checkpoint, which runs in 16 steps with no guidance. Prompt upsampling is on by default, so a short prompt is expanded into a full caption before sampling. ![FLUX 3 Image Klein Distilled text to image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Image Klein Distilled: Text to Image” in Template Library

  1. Enter your prompt. The template upsamples it first, so a short description is enough
  2. Set `steps` between 4 and 16 (16 by default). The distilled checkpoint runs with `cfg` 1, so raising `cfg` does not help
  3. Pick a frame from `ResolutionSelector`
  4. Click **Queue** to generate

**Example output** ![FLUX 3 Image Klein Distilled text to image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux3_klein_distilled_t2i.png)

### 

​

FLUX 3 Image Klein: Image Edit

Edit a photo from an instruction prompt, with the original image connected as a reference. The instruction replaces the reference content: here the prompt changes the dress color to red while everything else stays in place. ![FLUX 3 Image Klein image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Image Klein: Image Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## fashion_portrait_blue_silk_gown_vis.png

`LoadImage` node 54 · `fashion_portrait_blue_silk_gown_vis.png`

![fashion_portrait_blue_silk_gown_vis.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/fashion_portrait_blue_silk_gown_vis.png)

  1. Load your source image in the `LoadImage` node
  2. Connect it to `Set Reference Multi Latent`. The first reference is `<ref_image_0>` in the prompt, the next is `<ref_image_1>`, and so on
  3. Write the edit as a full description of the result. In the shipped example the prompt is `In <ref_image_0>, change the dress color <obj_1> to red`
  4. Adjust the canvas with `Empty Flux 2 Latent` (1024 x 1024 in the template) if you want a different output size
  5. Click **Queue**. `ImageCompare` shows the input and the result side by side

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/fashion_portrait_blue_silk_gown_vis.png)![FLUX 3 Image Klein image edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux3_klein_image_edit.png)

### 

​

FLUX 3 Image Klein Distilled: Image Edit

Edit an image with the step-distilled checkpoint: one reference image, one instruction prompt, 16 steps, and no guidance. ![FLUX 3 Image Klein Distilled image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX 3 Image Klein Distilled: Image Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## woman_gold_earring_teal_top_portrait.png

`LoadImage` node 11 · `woman_gold_earring_teal_top_portrait.png`

![woman_gold_earring_teal_top_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/woman_gold_earring_teal_top_portrait.png)

  1. Load the image you want to edit and connect it to `Set Reference Multi Latent`
  2. Write the edit prompt. The shipped example replaces an earring and describes the new one in detail, including what must not appear
  3. Keep `steps` in the 4 to 16 range and leave `cfg` at 1
  4. Click **Queue** and compare the input with the result in `ImageCompare`



## 

​

FLUX 3 Image Klein Model Downloads

The FLUX 3 Klein weights live in the gated repository [black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy). Open it, accept the license agreement, and then download the files. The templates use the int8 (convrot) single-file checkpoints; bf16 and nvfp4 versions of the same checkpoints are in the same repository.

## flux3_image_klein_base_int8_convrot.safetensors

Diffusion model, full FLUX 3 Image Klein checkpoint. The text to image and image edit templates load this file.

## flux3_image_klein_sd_int8_convrot.safetensors

Diffusion model, step-distilled checkpoint for 4 to 16 steps.

## qwen3vl_4b_int8_convrot.safetensors

Text encoder for both checkpoints. Load it with `CLIPLoader` type `flux3`.

## qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors

Prompt upsampler used by the text to image templates.

## flux2-vae.safetensors

VAE for FLUX 3 Klein. The FLUX.2 VAE.

**Model storage location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      ├── flux3_image_klein_base_int8_convrot.safetensors
    │   │      └── flux3_image_klein_sd_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │      ├── qwen3vl_4b_int8_convrot.safetensors
    │   │      └── qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

## 

​

Prompting and reference tips

  * **Write the result, not the change.** The image editing templates expect a full caption of the finished image with the edit folded in, which is why the examples describe the new object in detail instead of saying “change this”.
  * **References are added to both conditionings.** Connect extra images to `Set Reference Multi Latent` in order, address them as `<ref_image_0>`, `<ref_image_1>`, and so on, and add each one to both the positive and the negative prompt, the way the reference pipeline does.
  * **Reference size is a cost dial.** The templates resize each reference to roughly 1 megapixel and the output latent takes that size. Keeping references at their native size, which Black Forest Labs’ own pipeline does up to about 16 megapixels, keeps more detail in the edit at a higher cost.
  * **Step count depends on the checkpoint.** The full checkpoint runs at 50 steps in the templates, with guidance 3.5 on text to image and 1 on image edit. The step-distilled checkpoint runs at 16 steps with guidance fixed at 1, and it is the one to use when you want a fast pass.
  * **The templates ship a`Create Bounding Boxes` node.** It draws boxes over the source image for planning regional edits, and its list of boxes is shown in the `Preview Any` node so you can fold the regions into the prompt.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux-3-klein.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux-3-klein)

[ComfyUI FLUX.2 Klein 4B GuidePrevious](https://docs.comfy.org/tutorials/flux/flux-2-klein)[FLUX.1 Krea Dev ComfyUI Workflow TutorialNext](https://docs.comfy.org/tutorials/flux/flux1-krea-dev)

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
