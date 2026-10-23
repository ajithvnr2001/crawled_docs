---
url: https://docs.comfy.org/tutorials/flux/flux-1-uso/
title: ByteDance USO ComfyUI Native Workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:20.245754+00:00
---

# ByteDance USO ComfyUI Native Workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux-1-uso/

## On this page

  * ByteDance USO ComfyUI Native Workflow
    * FLUX.1 Dev USO Reference Image Generation
    * 1\. Workflow and input
    * 2\. Model links
    * 3\. Workflow instructions
    * 4\. Additional Notes



FLUX

# ByteDance USO ComfyUI Native Workflow example

Copy pageCopy page

Unified Style and Subject-Driven Generation with ByteDance’s USO model

Copy pageCopy page

**USO (Unified Style-Subject Optimized)** is a model developed by ByteDance’s UXO Team that unifies style-driven and subject-driven generation tasks. Built on FLUX.1-dev architecture, the model achieves both style similarity and subject consistency through disentangled learning and style reward learning (SRL). USO supports three main approaches:

  * **Subject-Driven** : Place subjects into new scenes while maintaining identity consistency
  * **Style-Driven** : Apply artistic styles to new content based on reference images
  * **Combined** : Use both subject and style references simultaneously

**Related Links**

  * [Project Page](https://bytedance.github.io/USO/)
  * [GitHub](https://github.com/bytedance/USO)
  * [Model Weights](https://huggingface.co/bytedance-research/USO)



## 

​

ByteDance USO ComfyUI Native Workflow

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

### 

​

FLUX.1 Dev USO Reference Image Generation

Use reference images to control both style and subject. Keep your character’s face while changing artistic style, or apply artistic styles to new scenes. ![FLUX.1 Dev USO reference image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_dev_uso_reference_image_gen-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## Download Workflow

Download the workflow JSON and drag it into ComfyUI

**Input materials** Upload this file to the matching `LoadImage` node:

## flux1_dev_uso_reference_image_gen_input_image.png

`LoadImage` node 47 · `flux1_dev_uso_reference_image_gen_input_image.png`

![flux1_dev_uso_reference_image_gen_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux1_dev_uso_reference_image_gen_input_image.png)

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux1_dev_uso_reference_image_gen_input_image.png)![FLUX.1 Dev USO example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux1_dev_uso_reference_image_gen.png)

### 

​

1\. Workflow and input

### 

​

2\. Model links

**checkpoints**

  * [flux1-dev-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/blob/main/flux1-dev-fp8.safetensors)

**loras**

  * [uso-flux1-dit-lora-v1.safetensors](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/blob/main/split_files/loras/uso-flux1-dit-lora-v1.safetensors)

**model_patches**

  * [uso-flux1-projector-v1.safetensors](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/blob/main/split_files/model_patches/uso-flux1-projector-v1.safetensors)

**clip_visions**

  * [sigclip_vision_patch14_384.safetensors](https://huggingface.co/Comfy-Org/sigclip_vision_384/blob/main/sigclip_vision_patch14_384.safetensors)

Please download all models and place them in the following directories:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── flux1-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   └── uso-flux1-dit-lora-v1.safetensors
    │   ├── 📂 model_patches/
    │   │   └── uso-flux1-projector-v1.safetensors
    │   ├── 📂 clip_visions/
    │   │   └── sigclip_vision_patch14_384.safetensors
    

### 

​

3\. Workflow instructions

![Workflow instructions](https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=60e1dc7cccd4b732ff2a6e24767d7630)

  1. Load models: 
     * 1.1 Ensure the `Load Checkpoint` node has `flux1-dev-fp8.safetensors` loaded
     * 1.2 Ensure the `LoraLoaderModelOnly` node has `dit_lora.safetensors` loaded
     * 1.3 Ensure the `ModelPatchLoader` node has `projector.safetensors` loaded
     * 1.4 Ensure the `Load CLIP Vision` node has `sigclip_vision_patch14_384.safetensors` loaded
  2. Content Reference: 
     * 2.1 Click `Upload` to upload the input image we provided
     * 2.2 The `ImageScaleToMaxDimension` node will scale your input image for content reference, 512px will keep more character features, but if you only use the character’s head as input, the final output image often has issues like the character taking up too much space. Setting it to 1024px gives much better results.
  3. In the example, we only use the `content reference` image input. If you want to use the `style reference` image input, you can use `Ctrl-B` to bypass the marked node group.
  4. Write your prompt or keep default
  5. Set the image size if you need
  6. The EasyCache node is for inference acceleration, but it will also sacrifice some quality and details. You can bypass it (Ctrl+B) if you don’t need to use it.
  7. Click the `Run` button, or use the shortcut `Ctrl(Cmd) + Enter` to run the workflow



### 

​

4\. Additional Notes

  1. Style reference only:

We also provide a workflow that only uses style reference in the same workflow we provided ![Workflow](https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=d5f16dbe97ac74b1bf01587aaabe12b8) The only different is we replaced the `content reference` node and only use an `Empty Latent Image` node.

  2. You can also bypass whole `Style Reference` group and use the workflow as a text to image workflow, which means this workflow has 4 variations


  * Only use content (subject) reference
  * Only use style reference
  * Mixed content and style reference
  * As a text to image workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux-1-uso.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux-1-uso)

[ComfyUI Flux.1 Text-to-Image Workflow ExamplePrevious](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image)[ComfyUI Flux.1 fill dev ExampleNext](https://docs.comfy.org/tutorials/flux/flux-1-fill-dev)

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
