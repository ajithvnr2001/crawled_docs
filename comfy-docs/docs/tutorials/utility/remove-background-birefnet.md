---
url: https://docs.comfy.org/tutorials/utility/remove-background-birefnet/
title: BiRefNet: Remove Image Background in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:41.551056+00:00
---

# BiRefNet: Remove Image Background in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/remove-background-birefnet/

## On this page

  * Key strengths
  * BiRefNet Background Removal Workflow
    * 1\. Download Workflow
    * BiRefNet: Remove Background
    * 2\. Download Models
    * 3\. Using the Workflow
  * Additional Notes



Segmentation & Background

# BiRefNet: Remove Image Background in ComfyUI

Copy pageCopy page

Learn how to remove image backgrounds using the BiRefNet model, natively supported in ComfyUI

Copy pageCopy page

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

BiRefNet (Bilateral Reference Network) is a high-quality image background removal model. It produces clean, detailed masks for a wide range of subjects, including people, products, animals, and complex objects with fine details like hair or fur. BiRefNet is natively supported in ComfyUI (PR [#12747](https://github.com/Comfy-Org/ComfyUI/pull/12747)). The model weights are available under the [MIT License](https://github.com/ZhengPeng7/BiRefNet/blob/main/LICENSE). [BiRefNet on Hugging Face](https://huggingface.co/ZhengPeng7/BiRefNet) | [Comfy-Org Model Repository](https://huggingface.co/Comfy-Org/BiRefNet) | [Paper (arXiv)](https://arxiv.org/abs/2401.00807)

### 

​

Key strengths

  * **High-quality masks** : accurate edge detection for hair, fur, and fine details
  * **Versatile subject detection** : works well on people, products, animals, and complex scenes
  * **Simple one-click workflow** : just load an image and the model handles the rest
  * **RGBA output** : produces an image with transparent background ready for compositing



> **Limitations:** Extremely cluttered backgrounds or subjects that blend into the background may produce less accurate masks. The model processes a single image at a time.

## 

​

BiRefNet Background Removal Workflow

### 

​

1\. Download Workflow

Update your ComfyUI to the latest version, then go to `Workflow` -> `Browse Templates` and find “BiRefNet: Remove Background” under the Utility category.

### 

​

BiRefNet: Remove Background

Upload an image with any background. Generate a version with the background removed and a precision segmentation mask. ![BiRefNet remove background workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_birefnet_remove_background-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “BiRefNet: Remove Background” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## the_lily_veil.png

`LoadImage` node 17 · `the_lily_veil.png`

### 

​

2\. Download Models

The BiRefNet model is hosted on the [Comfy-Org BiRefNet model repository](https://huggingface.co/Comfy-Org/BiRefNet).

  * [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/blob/main/background_removal/birefnet.safetensors)

Place it in the following directory structure:
    
    
    📂 ComfyUI/
    └── 📂 models/
        └── 📂 background_removal/
            └── birefnet.safetensors
    

### 

​

3\. Using the Workflow

  * **Image** : Load an image via the `Load Image` node (place it in the ComfyUI `input/` folder)
  * The `Remove Background (BiRefNet)` subgraph processes the image and outputs: 
    * **IMAGE** : the result with a transparent background (RGBA)
    * **mask** : the extracted foreground mask

Outputs can be previewed and used as inputs to other nodes for compositing, further editing, or saving.

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

## 

​

Additional Notes

  * **Model directory** : the model must be placed in `ComfyUI/models/background_removal/`, not the `checkpoints` folder
  * **Update required** : BiRefNet support is available in recent ComfyUI versions. Make sure your ComfyUI is up to date.
  * **RGBA output** : the transparent background result can be directly composited onto new backgrounds or used in downstream workflows



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/remove-background-birefnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/remove-background-birefnet)

[SAM 3.1: Segment Anything in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/video-segment-sam3)[SDPose: Pose Detection in ComfyUINext](https://docs.comfy.org/tutorials/utility/pose-detection-sdpose)

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
