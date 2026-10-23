---
url: https://docs.comfy.org/tutorials/partner-nodes/bria/fibo/
title: Bria FIBO in ComfyUI: JSON-Prompt Image Editing and Outpainting - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:26.557104+00:00
---

# Bria FIBO in ComfyUI: JSON-Prompt Image Editing and Outpainting - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bria/fibo/

## On this page

  * What Bria FIBO Edit is good at
  * Example outputs
    * Bria: Image Edit
    * Bria: Image Outpainting



Bria

# Bria FIBO in ComfyUI: JSON-Prompt Image Editing and Outpainting

Copy pageCopy page

Edit and extend images in ComfyUI with Bria FIBO partner workflows: structured JSON prompts for targeted edits, plus seamless outpainting.

Copy pageCopy page

FIBO Edit is Bria AI’s JSON-native image editing model, now available in ComfyUI through Partner Nodes. It lets you combine images with structured JSON prompts to make precise, targeted edits: no prompt guessing, no unwanted changes to the rest of your image.

## 

​

What Bria FIBO Edit is good at

  * **Surgical edits** : Change specific attributes (lighting, color, texture, materials) without breaking the rest of the scene
  * **Background swaps and object modifications** : Precise control over targeted areas
  * **Reproducible, auditable edits** : Structured JSON inputs for consistent results
  * **100% licensed data** : Full governance and legal clarity for commercial use
  * **Strong prompt adherence** : Validated on PRISM-style evaluations

FIBO Edit excels at various editing tasks:

  * **Time of day changes** : Relight your scene or change the time of day
  * **Material and texture swaps** : Try different colors, materials, fabrics, and clothing
  * **Object material replacement** : Swap out the material on specific objects
  * **Masked area editing** : Mask out a specific area to edit with precision
  * **Text adjustment** : Adjust the text in an image
  * **Art style transformation** : Re-imagine your image in a different art style



## 

​

Example outputs

Precision image editing with structured JSON control over lighting, composition, and camera settings: ![Bria: Image Edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bria_image_edit.png)

To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

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

Bria: Image Edit

FIBO enables precise, predictable image editing through structured JSON control over lighting, composition, and camera settings. ![Bria: Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Image Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## sunlit_rooftop_capture.png

`LoadImage` node 5 · `sunlit_rooftop_capture.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/sunlit_rooftop_capture.png)![Bria: Image Edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bria_image_edit.png)

### 

​

Bria: Image Outpainting

A professional Bria-powered outpainting template designed for seamless image extension and edge-aware scene expansion. ![Bria: Image Outpainting workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_outpainting-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Image Outpainting” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## baby_otter.png

`LoadImage` node 11 · `baby_otter.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/baby_otter.png)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bria/fibo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bria/fibo)

[Bria Background Removal in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/bria/background-removal)[Bria Eraser, Expand Image, and GenFill in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/bria/image-editing)

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
