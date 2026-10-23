---
url: https://docs.comfy.org/tutorials/flux/flux-1-controlnet/
title: ComfyUI Flux.1 ControlNet Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:19.494155+00:00
---

# ComfyUI Flux.1 ControlNet Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux-1-controlnet/

## On this page

  * FLUX.1 ControlNet Model Introduction
  * FLUX.1-Canny-dev Complete Version Workflow
    * Flux.1 Canny Model
    * 1\. Workflow and Asset
    * 2\. Manual Models Installation
    * 3\. Step-by-Step Workflow Execution
    * 4\. Start Your Experimentation
  * FLUX.1-Depth-dev-lora Workflow
    * Flux.1 Depth Lora
    * 1\. Workflow and Asset
    * 2\. Manual Model Download
    * 3\. Step-by-Step Workflow Execution
    * 4\. Start Your Experimentation
  * Community Versions of Flux Controlnets



FLUX

# ComfyUI Flux.1 ControlNet Examples

Copy pageCopy page

FLUX.1 Canny and Depth workflow examples for ComfyUI: add ControlNet-style structural control to FLUX.1 with Black Forest Labs’ FLUX.1 Tools.

Copy pageCopy page

![Flux.1 Canny Controlnet](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9796a0a85863c068c836ff7351b21729) ![Flux.1 Depth Controlnet](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=34c23b4e92011bb86fe97bc966441d80)

## 

​

FLUX.1 ControlNet Model Introduction

FLUX.1 Canny and Depth are two powerful models from the [FLUX.1 Tools](https://blackforestlabs.ai/flux-1-tools/) launched by [Black Forest Labs](https://blackforestlabs.ai/). This toolkit is designed to add control and guidance capabilities to FLUX.1, enabling users to modify and recreate real or generated images. **FLUX.1-Depth-dev** and **FLUX.1-Canny-dev** are both 12B parameter Rectified Flow Transformer models that can generate images based on text descriptions while maintaining the structural features of the input image. The Depth version maintains the spatial structure of the source image through depth map extraction techniques, while the Canny version uses edge detection techniques to preserve the structural features of the source image, allowing users to choose the appropriate control method based on different needs. Both models have the following features:

  * Top-tier output quality and detail representation
  * Excellent prompt following ability while maintaining consistency with the original image
  * Trained using guided distillation techniques for improved efficiency
  * Open weights for the research community
  * API interfaces (pro version) and open-source weights (dev version)

Additionally, Black Forest Labs also provides **FLUX.1-Depth-dev-lora** and **FLUX.1-Canny-dev-lora** adapter versions extracted from the complete models. These can be applied to the FLUX.1 [dev] base model to provide similar functionality with smaller file size, especially suitable for resource-constrained environments. We will use the full version of **FLUX.1-Canny-dev** and **FLUX.1-Depth-dev-lora** to complete the workflow examples.

All workflow images’s Metadata contains the corresponding model download information. You can load the workflows by:

  * Dragging them directly into ComfyUI
  * Or using the menu `Workflows` -> `Open（ctrl+o）`

If you’re not using the Desktop Version or some models can’t be downloaded automatically, please refer to the manual installation sections to save the model files to the corresponding folder.For image preprocessors, you can use the following custom nodes to complete image preprocessing. In this example, we will provide processed images as input.

  * [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
  * [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)



## 

​

FLUX.1-Canny-dev Complete Version Workflow

### 

​

Flux.1 Canny Model

Generate images guided by edge detection using Flux.1 Canny. ![Flux.1 Canny workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_canny_model_example-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Flux.1 Canny” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## flux_canny_model_example_input_image.png

`LoadImage` node 17 · `flux_canny_model_example_input_image.png`

![flux_canny_model_example_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_canny_model_example_input_image.png)

### 

​

1\. Workflow and Asset

### 

​

2\. Manual Models Installation

If you have previously used the [complete version of Flux related workflows](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image), then you only need to download the **flux1-canny-dev.safetensors** model file. Since you need to first agree to the terms of [black-forest-labs/FLUX.1-Canny-dev](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev), please visit the [black-forest-labs/FLUX.1-Canny-dev](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev) page and make sure you have agreed to the corresponding terms as shown in the image below.![Flux Agreement](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=64b9b0d0d2b8dd332dc1184dde9689be)

Complete model list:

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors?download=true)
  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors?download=true)
  * [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors?download=true)
  * [flux1-canny-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev/blob/main/flux1-canny-dev.safetensors?download=true) (Please ensure you have agreed to the corresponding repo’s terms)

File storage location:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── t5xxl_fp16.safetensors
    │   ├── vae/
    │   │   └── ae.safetensors
    │   └── diffusion_models/
    │       └── flux1-canny-dev.safetensors
    

### 

​

3\. Step-by-Step Workflow Execution

![ComfyUI Flux.1 Canny Controlnet Step Process](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9dfe7fc30106a96d837a93cb27958e42)

  1. Make sure `ae.safetensors` is loaded in the `Load VAE` node
  2. Make sure `flux1-canny-dev.safetensors` is loaded in the `Load Diffusion Model` node
  3. Make sure the following models are loaded in the `DualCLIPLoader` node: 
     * clip_name1: t5xxl_fp16.safetensors
     * clip_name2: clip_l.safetensors
  4. Upload the provided input image in the `Load Image` node
  5. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



### 

​

4\. Start Your Experimentation

Try using the [FLUX.1-Depth-dev](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev) model to complete the Depth version of the workflow You can use the image below as input ![ComfyUI Indoor Depth Map](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth-t2i-adapter_input.png) Or use the following custom nodes to complete image preprocessing:

  * [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
  * [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)



## 

​

FLUX.1-Depth-dev-lora Workflow

### 

​

Flux.1 Depth Lora

Generate images guided by depth information using Flux.1 LoRA. ![Flux.1 Depth LoRA workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_depth_lora_example-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Flux.1 Depth LoRA” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## flux_depth_lora_example_input_image.png

`LoadImage` node 17 · `flux_depth_lora_example_input_image.png`

![flux_depth_lora_example_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_depth_lora_example_input_image.png)

### 

​

1\. Workflow and Asset

### 

​

2\. Manual Model Download

If you have previously used the [complete version of Flux related workflows](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image), then you only need to download the **flux1-depth-dev-lora.safetensors** model file.

Complete model list:

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors?download=true)
  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors?download=true)
  * [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors?download=true)
  * [flux1-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/flux1-dev.safetensors?download=true)
  * [flux1-depth-dev-lora.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev-lora/blob/main/flux1-depth-dev-lora.safetensors?download=true)

File storage location:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── t5xxl_fp16.safetensors
    │   ├── vae/
    │   │   └── ae.safetensors
    │   ├── diffusion_models/
    │   │   └── flux1-dev.safetensors
    │   └── loras/
    │       └── flux1-depth-dev-lora.safetensors
    

### 

​

3\. Step-by-Step Workflow Execution

![ComfyUI Flux.1 Depth Controlnet Step Process](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ea682a93040eac4c930e05a66e08dd7f)

  1. Make sure `flux1-dev.safetensors` is loaded in the `Load Diffusion Model` node
  2. Make sure `flux1-depth-dev-lora.safetensors` is loaded in the `LoraLoaderModelOnly` node
  3. Make sure the following models are loaded in the `DualCLIPLoader` node: 
     * clip_name1: t5xxl_fp16.safetensors
     * clip_name2: clip_l.safetensors
  4. Upload the provided input image in the `Load Image` node
  5. Make sure `ae.safetensors` is loaded in the `Load VAE` node
  6. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



### 

​

4\. Start Your Experimentation

Try using the [FLUX.1-Canny-dev-lora](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev-lora) model to complete the Canny version of the workflow Use [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet) or [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux) to complete image preprocessing

## 

​

Community Versions of Flux Controlnets

XLab and InstantX + Shakker Labs have released Controlnets for Flux. **InstantX:**

  * [FLUX.1-dev-Controlnet-Canny](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny/blob/main/diffusion_pytorch_model.safetensors)
  * [FLUX.1-dev-ControlNet-Depth](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Depth/blob/main/diffusion_pytorch_model.safetensors)
  * [FLUX.1-dev-ControlNet-Union-Pro](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/blob/main/diffusion_pytorch_model.safetensors)

**XLab** : [flux-controlnet-collections](https://huggingface.co/XLabs-AI/flux-controlnet-collections) Place these files in the `ComfyUI/models/controlnet` directory. You can visit [Flux Controlnet Example](https://raw.githubusercontent.com/comfyanonymous/ComfyUI_examples/refs/heads/master/flux/flux_controlnet_example.png) to get the corresponding workflow image, and use the image from [here](https://raw.githubusercontent.com/comfyanonymous/ComfyUI_examples/refs/heads/master/flux/girl_in_field.png) as the input image.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux-1-controlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux-1-controlnet)

[ComfyUI Flux.1 fill dev ExamplePrevious](https://docs.comfy.org/tutorials/flux/flux-1-fill-dev)[Qwen-Image ComfyUI Native Workflow ExampleNext](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

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
