---
url: https://docs.comfy.org/tutorials/partner-nodes/tencent/hy-4/
title: Tencent HY4 in ComfyUI: Image to Prompt and Image Analysis - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:55.158279+00:00
---

# Tencent HY4 in ComfyUI: Image to Prompt and Image Analysis - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/tencent/hy-4/

## On this page

Back to top

  * What the Tencent HY node is good at
  * Tencent HY4 image to prompt workflow
    * Steps to run the workflow
    * Prompting tips
  * Get started



Tencent

# Tencent HY4 in ComfyUI: Image to Prompt and Image Analysis

Copy pageCopy page

Run Tencent HY4 in ComfyUI to turn a reference image into an art prompt, a caption, or a chart breakdown, with reasoning, multi-image, and token controls.

Copy pageCopy page

**Tencent HY4** is Tencent’s large language model, available in ComfyUI through the `Tencent HY` partner node. The node takes a text prompt and up to 20 images and returns text: an art prompt written from a reference image, a caption, a chart breakdown, or any other answer you ask for. Hy4 was released on November 4, 2026. It is the first Hy generation with visual understanding, and Tencent reports improvements over Hy4 preview in instruction following, long-context comprehension, and long-horizon agentic tasks. The node calls the model through Comfy API, so no model downloads and no local GPU are required. The template covered here is the image to prompt example: it reads a photo and writes a comma-separated prompt that you can paste into an image model.

## 

​

What the Tencent HY node is good at

  * **Image to prompt** : writes a structured prompt covering subject, composition, camera, lighting, color, texture, and style
  * **Image understanding** : captions, chart and diagram breakdowns, and fine detail checks on photos, screenshots, and documents
  * **Multiple images per request** : up to 20 images in one call, where each image in a batch counts once
  * **Instruction control** : `system_prompt` holds a standing role, while `prompt` carries the task for this run
  * **Reasoning toggle** : `reasoning` makes the model think before answering, for tasks that need it
  * **Long answers** : `max_tokens` accepts up to 64000 tokens



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

Tencent HY4 image to prompt workflow

The template loads a reference photo, asks Tencent HY for a standard art prompt, and can optionally save the prompt and answer with the run. ![Tencent HY4 image to prompt workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy4-1.webp)

## Download Workflow

Download JSON or search “Tencent: Hy4” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## blue_poppies_field.png

`LoadImage` node · `blue_poppies_field.png`

### 

​

Steps to run the workflow

This workflow demonstrates how to generate a reply with Tencent HY and optionally save that conversation into ComfyUI. Load a reference image, run the graph, then read the answer in `Preview Any`. If you want a saved copy, keep `Save Text` so it writes the prompt and answer under `output/Hy4/`; skip or remove that node if you do not need to save.

### 

​

Prompting tips

  * State the output format. The template’s `Only output positive prompt, no extra explanations` line is what keeps the answer paste-ready
  * When you connect several images, refer to them in order (`the first image`, `the second image`) so details land on the right one
  * Put repeated instructions in `system_prompt` and leave `prompt` for the task, for example `You write photography prompts for a stock library`
  * `seed` only decides whether the node re-runs. Answers still vary between runs



## 

​

Get started

Update ComfyUI, search Template Library for `Tencent: Hy4`, and open the image to prompt workflow. Tencent HY4 bills from API token usage. See the [pricing table](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the Hy4 rates.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/tencent/hy-4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/tencent/hy-4)

[Image Generation](https://docs.comfy.org/tutorials/partner-nodes/runway/image-generation)[HY Image 3.5](https://docs.comfy.org/tutorials/partner-nodes/tencent/hy-image-3-5)
