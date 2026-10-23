---
url: https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-6/
title: Meshy 6 in ComfyUI: Text, Image, and Multi-View to 3D - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:34.011840+00:00
---

# Meshy 6 in ComfyUI: Text, Image, and Multi-View to 3D - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-6/

## On this page

  * About Meshy 6
  * What Meshy 6 is good at
  * Text-to-Model Workflow
  * Image-to-Model Workflow
  * Multi-view to Model Workflow



Meshy

# Meshy 6 in ComfyUI: Text, Image, and Multi-View to 3D

Copy pageCopy page

Generate 3D models in ComfyUI with the Meshy 6 partner node: text-to-3D, image-to-3D, and multi-view workflows with PBR textures.

Copy pageCopy page

Meshy is a leading AI-powered 3D generation platform that enables users to create high-quality 3D models from text prompts, images, or multi-view inputs. ComfyUI has now natively integrated the Meshy API, allowing you to conveniently use the related nodes for 3D model generation.

## 

​

About Meshy 6

Meshy 6 is a generation of Meshy’s 3D model generation technology, featuring significant improvements in geometry quality, texture fidelity, and workflow efficiency.

## 

​

What Meshy 6 is good at

  * **Smarter geometry** : Improved mesh topology with cleaner edges and more coherent structures
  * **Higher texture fidelity** : Enhanced texture generation with better detail preservation and color accuracy
  * **Faster workflows** : Optimized generation pipeline for quicker turnaround times
  * **Multiple input modes** : Supports text-to-3D, image-to-3D, and multi-view to 3D generation
  * **PBR support** : Generate physically-based rendering maps including metallic, roughness, and normal maps



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

## 

​

Text-to-Model Workflow

Generate 3D models directly from text descriptions using Meshy 6.

## Run on Comfy Cloud

Run the text-to-model workflow instantly on Comfy Cloud.

## Download Workflow

Download the workflow JSON file for local use.

![Meshy 6 Text-to-Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_text_to_model-1.webp)

## 

​

Image-to-Model Workflow

Convert 2D images into detailed 3D models with Meshy 6’s image-to-3D capabilities.

## Run on Comfy Cloud

Run the image-to-model workflow instantly on Comfy Cloud.

## Download Workflow

Download the workflow JSON file for local use.

![Meshy 6 Image-to-Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_image_to_model-1.webp)

## Download Sample Input Image

Get the example input image for this workflow.

## 

​

Multi-view to Model Workflow

Generate 3D models from multiple view images for more accurate geometry and texture reconstruction.

## Run on Comfy Cloud

Run the multi-view workflow instantly on Comfy Cloud.

## Download Workflow

Download the workflow JSON file for local use.

![Meshy 6 Multi-view to Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_multi_image_to_model-1.webp)

## Download Front View

Get the example front view image.

## Download Back View

Get the example back view image.

## Download Side View

Get the example side view image.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/meshy/meshy-6.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/meshy/meshy-6)

[Meshy 7 in ComfyUI: Text to 3D and Image to 3D WorkflowsPrevious](https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-7)[Hyper3D Rodin in ComfyUI: Single and Multi-View 3D GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/rodin/model-generation)

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
