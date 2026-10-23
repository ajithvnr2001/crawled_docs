---
url: https://docs.comfy.org/tutorials/partner-nodes/meta/muse-image/
title: Meta Muse Image in ComfyUI: Text to Image and Image Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:34.808674+00:00
---

# Meta Muse Image in ComfyUI: Text to Image and Image Edit - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/meta/muse-image/

## On this page

  * What Meta Muse Image is good at
  * Example outputs
  * Meta Muse Image Text to Image workflow
  * Meta Muse Image Edit workflow
    * Input files
  * Get started
    * Prompting tips
  * Pricing



Meta

# Meta Muse Image in ComfyUI: Text to Image and Image Edit

Copy pageCopy page

Run Meta’s agentic Muse Image 1.0 in ComfyUI: text-to-image with built-in web search, plus instruction-based editing across up to 10 reference images.

Copy pageCopy page

Meta Muse Image 1.0 is the first image generation model from Meta Superintelligence Labs, announced on July 7, 2026. It generates images at roughly 2.5 megapixels and stands out for its agentic approach: before rendering, the model can search the web for facts, search for reference images, and even run code to get quantities, layouts, charts, and diagrams precise. ComfyUI exposes Muse Image through two Partner Nodes: Meta Muse Image Text to Image for generation, and Meta Muse Image Edit for instruction-based editing and combining.

## 

​

What Meta Muse Image is good at

  * **Agentic rendering** : The model plans before it draws, using built-in web search, image search, and code execution (all three toggles are on by default in the node’s advanced options)
  * **Precise quantities and layouts** : Text-heavy posters, charts, diagrams, and layouts benefit from the code-execution path; turning it off falls back to approximation
  * **Multi-reference editing** : The Edit node accepts 1 to 10 reference images. Refer to them in the prompt as `@Image1`, `@Image2`, and so on, numbered in input order
  * **Flexible framing** : 14 aspect ratios from 1:1 up to 21:9 and 9:21, plus `auto`, which lets the model choose from the prompt (generation) or keeps the input’s ratio (edit)
  * **Reasoning control** : Choose `high` or `low` reasoning strength depending on how much planning the image needs



## 

​

Example outputs

Text-to-image generation from a single prompt: ![Muse Image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/muse_image_1.0.png)

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

Meta Muse Image Text to Image workflow

Generate an image from a text description using Meta’s Muse Image 1.0 model. One text prompt is accepted and one image is output. ![Meta Muse Image Text-to-Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Muse Image” in Template Library

![Muse Image Text-to-Image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/muse_image_1.0.png)

## 

​

Meta Muse Image Edit workflow

Edit or combine up to 10 reference images guided by a text prompt. Reference images are connected to the `image_1` to `image_10` inputs, and the prompt addresses each one as `@Image1`, `@Image2`, and so on, numbered in input order. A batched input counts once per image. ![Meta Muse Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Muse Image” in Template Library

### 

​

Input files

## Whale figure

deep_blue_whale_swim_scene.png

## Modern house

desert_red_modern_house.png

The example workflow combines the two inputs with the prompt: “Use the whale figure from @image1 and make it roam across the sky above the picture in @image2”. ![Muse Image Edit output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_meta_muse_image_image_edit.png)

## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Muse Image`



### 

​

Prompting tips

  * Be explicit about what must stay accurate: Muse Image follows instructions closely, so state counts, positions, and labels directly in the prompt
  * For posters and diagrams, keep the code execution toggle on (advanced options) so quantities and alignment are computed rather than approximated
  * In the Edit workflow, name every reference you connect. An `@Image` tag with no connected input fails the run
  * Use `auto` aspect ratio when you want the model to decide the framing from the prompt; use a fixed ratio for consistent series output



## 

​

Pricing

Node| Credits  
---|---  
Meta Muse Image Text to Image| 3.017 / image  
Meta Muse Image Edit| 3.017 / image  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/meta/muse-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/meta/muse-image)

[Luma Image to Image in ComfyUI: Prompt-Driven Image EditingPrevious](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-image-to-image)[OpenAI GPT Image 2.5 Node: Flare and Sunburst WorkflowsNext](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2-5)

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
