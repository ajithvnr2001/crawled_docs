---
url: https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-v4/
title: Ideogram 4.0 in ComfyUI: Text-to-Image with JSON Prompts - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.697846+00:00
---

# Ideogram 4.0 in ComfyUI: Text-to-Image with JSON Prompts - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-v4/

## On this page

  * What Ideogram 4.0 is good at
  * Example outputs
  * Live Conversation with Ideogram & ComfyOrg
  * Use it
  * Ideogram 4.0 Partner Node Text-to-Image Workflow
    * Prompt Format
    * Workflow Steps
    * Using the JSON Prompt Builder (Optional)
  * Additional Notes



Ideogram

# Ideogram 4.0 in ComfyUI: Text-to-Image with JSON Prompts

Copy pageCopy page

Generate images with Ideogram 4.0 in ComfyUI from plain language or structured JSON prompts, with control over layout, color palettes, and rendered text.

Copy pageCopy page

Ideogram 4.0 is a text-to-image model from Ideogram, offering photorealistic quality, accurate text rendering, and precise style control. You can use either plain natural language or **structured JSON prompts** for fine-grained control over layout, colors, and in-image text. Ideogram 4.5 is the newer model in the family and has its own page: [Ideogram 4.5 in ComfyUI](https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-4-5).

## 

​

What Ideogram 4.0 is good at

  * **Photorealistic quality** : Superior photorealism across generated images
  * **Accurate text rendering** : Renders literal text in the image, well suited for poster-like compositions
  * **Precise style control** : Structured JSON prompts control style palette, element placement (`bbox`), and per-element color palettes
  * **Flexible prompting** : Accepts plain natural language for quick ideas or structured JSON for fine-grained control
  * **No negative prompts needed** : Uses asymmetric classifier-free guidance instead of a separate negative prompt string



## 

​

Example outputs

Text-to-image generation from a structured JSON prompt: ![Ideogram 4.0 Example Output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_ideogram_v4_t2i.png) _Example output from the Ideogram 4.0 API_

## 

​

Live Conversation with Ideogram & ComfyOrg

A special live conversation with Mohammad Norouzi (CEO, Ideogram) and Yoland Yan (CEO, ComfyOrg), hosted by Purz & Rob.

## 

​

Use it

## Call it from code

Call it over HTTP through Comfy Router, with copy-paste Python, TypeScript, Swift and cURL snippets

This runs on the same Comfy account and is billed in the same credits as running it in ComfyUI below. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for per-model rates and [Concurrency limits](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits) for how many requests you can have in flight.

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

Ideogram 4.0 Partner Node Text-to-Image Workflow

![Ideogram 4.0 Text-to-Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ideogram v4: Text to Image (API)” in Template Library

![Ideogram 4.0 Example Output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_ideogram_v4_t2i.png) _Example output from the Ideogram 4.0 API_

### 

​

Prompt Format

The Ideogram V4 node supports two prompt formats:

  1. **Natural Language** : Simple and intuitive, best for quick ideas.
  2. **Structured JSON** : Offers fine-grained control over style palette, element placement (`bbox`), and literal text rendering in the image. Recommended for poster-like compositions.

The default workflow example uses a structured JSON prompt that includes:

  * `high_level_description`: Overall scene description
  * `style_description`: Aesthetic, lighting, medium, color palette
  * `compositional_deconstruction`: Per-element bounding boxes, descriptions, and color palettes



### 

​

Workflow Steps

  1. Download and drag the workflow file into ComfyUI
  2. The `Ideogram V4` node already contains a default structured JSON prompt: you can modify it or write plain natural language
  3. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
  4. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory



### 

​

Using the JSON Prompt Builder (Optional)

The workflow includes a built-in **Gemini** node (Gemini 3.1 Pro) to help you build structured JSON prompts:

  1. Describe your idea in the Gemini node’s user prompt field
  2. The model will generate a schema-matching JSON prompt
  3. Connect the `STRING` output to the `Ideogram V4` node’s `prompt` input
  4. Run the workflow



## 

​

Additional Notes

  * **Negative prompts are not needed** : The Ideogram 4.0 model uses asymmetric classifier-free guidance, where the unconditional pass drops text tokens, rather than requiring a separate negative prompt string.
  * **Model-assisted prompt building** : Consider using the **Ideogram 4 Prompt Builder** (KJNodes) for visual control over prompt construction on ComfyUI.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/ideogram/ideogram-v4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/ideogram/ideogram-v4)

[Ideogram P-Image - fast text-to-imagePrevious](https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-p-image)[Krea 3 in ComfyUI: Text to Image and Image EditingNext](https://docs.comfy.org/tutorials/partner-nodes/krea/krea-3)

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
