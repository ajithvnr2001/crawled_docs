---
url: https://docs.comfy.org/tutorials/basic/lora/
title: LoRA Models in ComfyUI: Install, Load, and Apply Styles - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:05.257759+00:00
---

# LoRA Models in ComfyUI: Install, Load, and Apply Styles - ComfyUI

> Source: https://docs.comfy.org/tutorials/basic/lora/

## On this page

  * Required Model Installation
  * LoRA Workflow File
  * Complete the Workflow Step by Step
  * Load LoRA Node Introduction
    * Input Types
    * Output Types
  * Try It Yourself



Basic Examples

# LoRA Models in ComfyUI: Install, Load, and Apply Styles

Copy pageCopy page

Install a LoRA file, load it with the Load LoRA node, and run a workflow that blends its style on top of a base checkpoint.

Copy pageCopy page

**LoRA (Low-Rank Adaptation)** is an efficient technique for fine-tuning large generative models like Stable Diffusion. It introduces trainable low-rank matrices to the pre-trained model, adjusting only a portion of parameters rather than retraining the entire model, thus achieving optimization for specific tasks at a lower computational cost. Compared to base models like SD1.5, LoRA models are smaller and easier to train. ![LoRA Model vs Base Model Comparison](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=742213e2c13c5be487ea3e9827630e5a) The image above compares generation with the same parameters using [dreamshaper_8](https://civitai.com/models/4384?modelVersionId=128713) directly versus using the [blindbox_V1Mix](https://civitai.com/models/25995/blindbox) LoRA model. As you can see, by using a LoRA model, we can generate images in different styles without adjusting the base model. We will demonstrate how to use a LoRA model. All LoRA variants: Lycoris, loha, lokr, locon, etc… are used in the same way. In this example, we will learn how to load and use a LoRA model in [ComfyUI](https://github.com/Comfy-Org/ComfyUI), covering the following topics:

  1. Installing a LoRA model
  2. Generating images using a LoRA model
  3. A simple introduction to the `Load LoRA` node



## 

​

Required Model Installation

Download the [dreamshaper_8.safetensors](https://civitai.com/api/download/models/128713?type=Model&format=SafeTensor&size=pruned&fp=fp16) file and put it in your `ComfyUI/models/checkpoints` folder. Download the [blindbox_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model&format=SafeTensor&size=full&fp=fp16) file and put it in your `ComfyUI/models/loras` folder.

## 

​

LoRA Workflow File

Download the image below and **drag it into ComfyUI** to load the workflow. ![ComfyUI Workflow - LoRA](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5f67dbeed58fd00da65100432c06edc7)

Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.

## 

​

Complete the Workflow Step by Step

Follow the steps in the diagram below to ensure the workflow runs correctly. ![ComfyUI Workflow - LoRA Flow Diagram](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/lora.png)

  1. Ensure `Load Checkpoint` loads `dreamshaper_8.safetensors`
  2. Ensure `Load LoRA` loads `blindbox_V1Mix.safetensors`
  3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to generate the image



## 

​

Load LoRA Node Introduction

![Load LoRA Node](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=86dd2ba28327b5c6c182a9fb4f4404bb) Models in the `ComfyUI\models\loras` folder will be detected by ComfyUI and can be loaded using this node.

### 

​

Input Types

Parameter Name| Function  
---|---  
`model`| Connect to the base model  
`clip`| Connect to the CLIP model  
`lora_name`| Select the LoRA model to load and use  
`strength_model`| Affects how strongly the LoRA influences the model weights; higher values make the LoRA style stronger  
`strength_clip`| Affects how strongly the LoRA influences the CLIP text embeddings  
  
### 

​

Output Types

Parameter Name| Function  
---|---  
`model`| Outputs the model with LoRA adjustments applied  
`clip`| Outputs the CLIP model with LoRA adjustments applied  
  
This node supports chain connections, allowing multiple `Load LoRA` nodes to be linked in series to apply multiple LoRA models. For more details, please refer to [ComfyUI Multiple LoRAs Example](https://docs.comfy.org/tutorials/basic/multiple-loras) ![LoRA Node Chain Connection](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf)

## 

​

Try It Yourself

  1. Try modifying the prompt or adjusting different parameters of the `Load LoRA` node, such as `strength_model`, to observe changes in the generated images and become familiar with the `Load LoRA` node.
  2. Visit [CivitAI](https://civitai.com/models) to download other kinds of LoRA models and try using them.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/basic/lora.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/basic/lora)

[ComfyUI Image Upscale WorkflowPrevious](https://docs.comfy.org/tutorials/basic/upscale)[ComfyUI Multiple LoRAs: Chain Loaders for Blended StylesNext](https://docs.comfy.org/tutorials/basic/multiple-loras)

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
