---
url: https://docs.comfy.org/tutorials/controlnet/controlnet/
title: ControlNet in ComfyUI: Preprocessors, Models, and Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:18.477051+00:00
---

# ControlNet in ComfyUI: Preprocessors, Models, and Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/controlnet/controlnet/

## On this page

  * ControlNet Image Preprocessing Information
  * ComfyUI ControlNet Workflow Example Explanation
    * 1\. ControlNet Workflow Assets
    * 2\. Manual Model Installation
    * 3\. Step-by-Step Workflow Execution
  * Related Node Explanations
    * Load ControlNet Node Explanation
    * Apply ControlNet Node Explanation
  * Start Your Exploration



ControlNet

# ControlNet in ComfyUI: Preprocessors, Models, and Workflows

Copy pageCopy page

ControlNet in ComfyUI: control image generation with condition images instead of trial-and-error prompting, plus a step-by-step workflow example.

Copy pageCopy page

Achieving precise control over image creation in AI image generation cannot be done with just one click. It typically requires numerous generation attempts to produce a satisfactory image. However, the emergence of **ControlNet** has effectively addressed this challenge. ControlNet is a conditional control generation model based on diffusion models (such as Stable Diffusion), first proposed by [Lvmin Zhang](https://github.com/lllyasviel) and Maneesh Agrawala et al. in 2023 in the paper [Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543). ControlNet models significantly enhance the controllability of image generation and the ability to reproduce details by introducing multimodal input conditions, such as edge detection maps, depth maps, and pose keypoints. These conditioning constraints make image generation more controllable, allowing multiple ControlNet models to be used simultaneously during the drawing process for better results. Before ControlNet, we could only rely on the model to generate images repeatedly until we were satisfied with the results, which involved a lot of randomness. ![Images generated with random seeds in ComfyUI](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=81acd50958fd1df511237b3ba90b1b06) With the advent of ControlNet, we can control image generation by introducing additional conditions. For example, we can use a simple sketch to guide the image generation process, producing images that closely align with our sketch. ![Sketch-controlled image generation in ComfyUI](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=36c37d9cadfaabb3690404f8828143a7) In this example, we will guide you through installing and using ControlNet models in [ComfyUI](https://github.com/Comfy-Org/ComfyUI), and complete a sketch-controlled image generation example. ![ComfyUI ControlNet Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_controlnet.png)

The workflows for other types of ControlNet V1.1 models are similar to this example. You only need to select the appropriate model and upload the corresponding reference image based on your needs.

## 

​

ControlNet Image Preprocessing Information

Different types of ControlNet models typically require different types of reference images: ![Reference Images](https://github.com/Fannovel16/comfyui_controlnet_aux/blob/main/examples/CNAuxBanner.jpg?raw=true)

> Image source: [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

Since the current **Comfy Core** nodes do not include all types of **preprocessors** , in the actual examples in this documentation, we will provide pre-processed images. However, in practical use, you may need to use custom nodes to preprocess images to meet the requirements of different ControlNet models. Below are some relevant custom nodes:

  * [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
  * [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)



## 

​

ComfyUI ControlNet Workflow Example Explanation

### 

​

1\. ControlNet Workflow Assets

Please download the workflow image below and drag it into ComfyUI to load the workflow: ![ComfyUI Workflow - ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_controlnet.png)

Images with workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`. This image already includes download links for the corresponding models, and dragging it into ComfyUI will automatically prompt for downloads.

Please download the image below, which we will use as input: ![ComfyUI Sketch Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_input.png)

### 

​

2\. Manual Model Installation

If your network cannot successfully complete the automatic download of the corresponding models, please try manually downloading the models below and placing them in the specified directories:

  * [dreamCreationVirtual3DECommerce_v10.safetensors](https://civitai.com/api/download/models/731340?type=Model&format=SafeTensor&size=full&fp=fp16)
  * [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.safetensors?download=true)
  * [control_v11p_sd15_scribble_fp16.safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_scribble_fp16.safetensors?download=true)


    
    
    ComfyUI/
    ├── models/
    │   ├── checkpoints/
    │   │   └── dreamCreationVirtual3DECommerce_v10.safetensors
    │   ├── vae/
    │   │   └── vae-ft-mse-840000-ema-pruned.safetensors
    │   └── controlnet/
    │       └── control_v11p_sd15_scribble_fp16.safetensors
    

In this example, you could also use the VAE model embedded in dreamCreationVirtual3DECommerce_v10.safetensors, but we’re following the model author’s recommendation to use a separate VAE model.

### 

​

3\. Step-by-Step Workflow Execution

![ComfyUI Workflow - ControlNet Flow Diagram](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d26abbfd1993f28b88efcf6231246945)

  1. Ensure that `Load Checkpoint` can load **dreamCreationVirtual3DECommerce_v10.safetensors**
  2. Ensure that `Load VAE` can load **vae-ft-mse-840000-ema-pruned.safetensors**
  3. Click `Upload` in the `Load Image` node to upload the input image provided earlier
  4. Ensure that `Load ControlNet` can load **control_v11p_sd15_scribble_fp16.safetensors**
  5. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation



## 

​

Related Node Explanations

### 

​

Load ControlNet Node Explanation

![load controlnet](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c3a99d9bd08baaedb7a4d426cc930880) Models located in `ComfyUI\models\controlnet` will be detected by ComfyUI and can be loaded through this node.

### 

​

Apply ControlNet Node Explanation

![apply controlnet](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=de9e90df2dcfe5cc7020a8c9cdb40a65) This node accepts the ControlNet model loaded by `load controlnet` and generates corresponding control conditions based on the input image. **Input Types**

Parameter Name| Function  
---|---  
`positive`| Positive conditioning  
`negative`| Negative conditioning  
`control_net`| The ControlNet model to be applied  
`image`| Preprocessed image used as reference for ControlNet application  
`vae`| VAE model input  
`strength`| Strength of ControlNet application; higher values increase ControlNet’s influence on the generated image  
`start_percent`| Determines when to start applying ControlNet as a percentage; e.g., 0.2 means ControlNet guidance begins when 20% of diffusion is complete  
`end_percent`| Determines when to stop applying ControlNet as a percentage; e.g., 0.8 means ControlNet guidance stops when 80% of diffusion is complete  
  
**Output Types**

Parameter Name| Function  
---|---  
`positive`| Positive conditioning data processed by ControlNet  
`negative`| Negative conditioning data processed by ControlNet  
  
You can use chain connections to apply multiple ControlNet models, as shown in the image below. You can also refer to the [Mixing ControlNet Models](https://docs.comfy.org/tutorials/controlnet/mixing-controlnets) guide to learn more about combining multiple ControlNet models. ![apply controlnet chain link](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6fc3e75414f05e6c62062b4b746dc855)

You might see the `Apply ControlNet(Old)` node in some early workflows, which is an early version of the ControlNet node. It is currently deprecated and not visible by default in search and node lists.![apply controlnet old](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=eaf2f8df7456df845f7408495d19b9e8)To enable it, go to **Settings** —> **comfy** —> **Node** and enable the `Show deprecated nodes in search` option. However, it’s recommended to use the new node.

## 

​

Start Your Exploration

  1. Try creating similar sketches, or even draw your own, and use ControlNet models to generate images to experience the benefits of ControlNet.
  2. Adjust the `Control Strength` parameter in the Apply ControlNet node to control the influence of the ControlNet model on the generated image.
  3. Visit the [ControlNet-v1-1_fp16_safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/tree/main) repository to download other types of ControlNet models and try using them to generate images.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/controlnet/controlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/controlnet/controlnet)

[ComfyUI Multiple LoRAs: Chain Loaders for Blended StylesPrevious](https://docs.comfy.org/tutorials/basic/multiple-loras)[ComfyUI Pose ControlNet Usage ExampleNext](https://docs.comfy.org/tutorials/controlnet/pose-controlnet-2-pass)

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
