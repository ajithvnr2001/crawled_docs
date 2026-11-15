---
url: https://docs.comfy.org/tutorials/partner-nodes/tripo/model-generation/
title: Tripo in ComfyUI: Text, Image, and Multi-view 3D Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:55.738523+00:00
---

# Tripo in ComfyUI: Text, Image, and Multi-view 3D Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/tripo/model-generation/

## On this page

Back to top

  * What Tripo Model Generation is good at
  * Text-to-Model Workflow
    * 2\. Complete the Workflow Execution Step by Step
  * Image-to-Model Workflow
    * 2\. Complete the Workflow Execution Step by Step
  * Multi-view Model Generation Workflow
    * 2\. Complete the Workflow Execution Step by Step
  * Subsequent Task Processing for the Same Task



Tripo

# Tripo in ComfyUI: Text, Image, and Multi-view 3D Generation

Copy pageCopy page

Generate 3D models in ComfyUI from a text prompt, images, or multiple views with the Tripo partner nodes, then run follow-up tasks on the same task ID.

Copy pageCopy page

Tripo AI is a company focused on generative AI 3D modeling. It provides user-friendly platforms and API services that can quickly convert text prompts or 2D images (single or multiple) into high-quality 3D models. ComfyUI has now natively integrated the corresponding Tripo API, allowing you to conveniently use the related nodes in ComfyUI for model generation.

## What Tripo Model Generation is good at

Currently, ComfyUI’s Partner nodes support the following Tripo model generation capabilities:

  * Text-to-model
  * Image-to-model
  * Multi-view model generation
  * Rig model
  * Retarget rigged model



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

## Text-to-Model Workflow

Generate a 3D model from a text prompt with Tripo’s text-to-model capabilities. ![Tripo Text-to-Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_text_to_model-1.webp)

## Run Text-to-Model on Cloud

Try the Text-to-Model workflow instantly on Comfy Cloud.

## Download Text-to-Model Workflow

Download JSON to run locally in ComfyUI.

### 2\. Complete the Workflow Execution Step by Step

![ComfyUI Tripo Text to Model Step Guide](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b25199fbdd5c00f3fd8a1b587586bbed) You can refer to the numbers in the image to complete the basic text-to-model workflow execution:

  1. In the `Tripo: Text to Model` node, input your prompt in the `prompt` field 
     * model: You can select different models
     * style: You can set different styles
     * texture_quality: You can set different texture qualities
  2. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/` directory
  3. In the `Preview 3D` node, click to expand the menu
  4. Select `Export` to directly export the corresponding model



## Image-to-Model Workflow

Generate a 3D model from a single image input. ![Tripo Image-to-Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_image_to_model-1.webp)

## Run Image-to-Model on Cloud

Try the Image-to-Model workflow instantly on Comfy Cloud.

## Download Image-to-Model Workflow

Download JSON to run locally in ComfyUI.

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/image_to_model/panda.jpg)

### 2\. Complete the Workflow Execution Step by Step

![ComfyUI Tripo Text to Model Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=302a46095bbb73ea478f441fa489b763) You can refer to the numbers in the image to complete the basic image-to-model workflow execution:

  1. In the `Load Image` node, load the provided input image
  2. In the `Tripo: Image to Model` node, modify the corresponding parameter settings 
     * model: You can select different models
     * style: You can set different styles
     * texture_quality: You can set different texture qualities
  3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/` directory
  4. For model download, please refer to the instructions in the text-to-model section



## Multi-view Model Generation Workflow

Generate a 3D model from multiple view images for enhanced accuracy. ![Tripo Multi-view Model Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_multiview_to_model-1.webp)

## Run Multiview-to-Model on Cloud

Try the Multiview-to-Model workflow instantly on Comfy Cloud.

## Download Multiview-to-Model Workflow

Download JSON to run locally in ComfyUI.

![Front View](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/front.jpg) ![Back View](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/back.jpg)

### 2\. Complete the Workflow Execution Step by Step

![ComfyUI Tripo Text to Model Step Guide](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5c4abf93f36e2ea96202c7cdb92d9917) You can refer to the numbers in the image to complete the basic multi-view to model workflow execution:

  1. In the `Load Image` nodes, load the provided input images respectively
  2. In the `Tripo: Image to Model` node, modify the corresponding parameter settings 
     * model: You can select different models
     * style: You can set different styles
     * texture_quality: You can set different texture qualities
  3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/` directory
  4. For other view inputs, you can refer to the step diagram and set the corresponding node mode to `Always` to enable it
  5. For model download, please refer to the instructions in the text-to-model section



## Subsequent Task Processing for the Same Task

Tripo’s corresponding nodes provide subsequent processing for the same task, you only need to input the corresponding `model_task_id` in the relevant nodes, and we have also provided the corresponding nodes in the relevant templates, you can also modify the corresponding node mode as needed to enable it ![Tripo Task Processing](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ad7966d458e1d327c98d2b21eccdd7a4)

Generated models are downloaded to your output directory as soon as the task finishes, so the model file survives independently of Tripo. The task IDs do not. Tripo keeps a task record for 7 days after the task completes (effective December 1, 2026), so rerunning a saved workflow more than 7 days later with an older `model_task_id` fails at the follow-up node. To keep going, connect `Tripo: Import Model` to the model file in your output directory and use its new `model_task_id`.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/tripo/model-generation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/tripo/model-generation)

[Tripo 3.1](https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-3-1)[Overview](https://docs.comfy.org/tutorials/partner-nodes/audio/overview)
