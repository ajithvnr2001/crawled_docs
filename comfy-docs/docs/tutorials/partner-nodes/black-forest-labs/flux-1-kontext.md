---
url: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-kontext/
title: FLUX.1 Kontext in ComfyUI: Pro and Max Image Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:25.897907+00:00
---

# FLUX.1 Kontext in ComfyUI: Pro and Max Image Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-kontext/

## On this page

  * What FLUX.1 Kontext is good at
  * Example outputs
  * Use it
  * FLUX.1 Kontext Multiple Image Input Workflow
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Step by Step
  * FLUX.1 Kontext Pro Image Partner Nodes Workflow
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Step by Step
  * FLUX.1 Kontext Max Image Partner Nodes Workflow
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Step by Step
  * FLUX Kontext Prompt Techniques
    * 1\. Basic Modifications
    * 2\. Style Transfer
    * 3\. Character Consistency
    * 4\. Text Editing
  * Common Problem Solutions
    * Character Changes Too Much
    * Composition Position Changes
    * Style Application Inaccuracy
  * Core Principles
  * Best Practice Templates



Black Forest Labs

# FLUX.1 Kontext in ComfyUI: Pro and Max Image Editing

Copy pageCopy page

Edit images in ComfyUI with the FLUX.1 Kontext Pro and Max partner nodes: object and style changes, background swap, character consistency, and text editing.

Copy pageCopy page

FLUX.1 Kontext is a professional image-to-image editing model developed by Black Forest Labs, focusing on intelligent understanding of image context and precise editing. It can perform various editing tasks without complex descriptions, including object modification, style transfer, background replacement, character consistency editing, and text editing. The core advantage of Kontext lies in its excellent context understanding ability and character consistency maintenance, ensuring that key elements such as character features and composition layout remain stable even after multiple iterations of editing. Currently, ComfyUI has supported two models of FLUX.1 Kontext:

  * **Kontext Pro** is ideal for editing, composing, and remixing.
  * **Kontext Max** pushes the limits on typography, prompt precision, and speed.



## 

​

What FLUX.1 Kontext is good at

  * **Versatile editing without complex descriptions** : Object modification, style transfer, background replacement, character consistency editing, and text editing
  * **Context understanding** : Intelligent understanding of image context enables precise, targeted edits
  * **Character consistency** : Character features and composition layout remain stable even after multiple iterations of editing
  * **Multiple image input** : The `Image Stitch` node stitches multiple images into a single image for editing with FLUX.1 Kontext
  * **Two model tiers** : Kontext Pro for editing, composing, and remixing; Kontext Max for typography, prompt precision, and speed



## 

​

Example outputs

Editing a stitched multi-image input (a girl, a dog, and a sofa combined into one scene): ![FLUX.1 Kontext multiple image input example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/multiple_image_input.png) Image editing with Kontext Pro, ideal for editing, composing, and remixing: ![FLUX.1 Kontext Pro image editing example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image.png) Image editing with Kontext Max, which pushes the limits on typography, prompt precision, and speed: ![FLUX.1 Kontext Max image editing example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image.png)

## 

​

Use it

## Call it from code

Call Kontext Pro or Max over HTTP through Comfy Router, with copy-paste Python, TypeScript, Swift and cURL snippets

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

FLUX.1 Kontext Multiple Image Input Workflow

We have recently updated to support multiple image input workflows. Using the new `Image Stitch` node, you can stitch multiple images into a single image and edit it using FLUX.1 Kontext.

### 

​

1\. Workflow File Download

The `metadata` of the images below contains the workflow information. Please download and drag them into ComfyUI to load the corresponding workflow. ![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/multiple_image_input.png) Download the following images for input or use your own images: ![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/girl.jpg) ![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/dog.jpg) ![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/sofa.jpg)

### 

​

2\. Complete the Workflow Step by Step

![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bf6e2ac1877f37556b354699f1960129) You can follow the numbered steps in the image to complete the workflow:

  1. Upload the provided images in the `Load image` node
  2. Modify the necessary parameters in `Flux.1 Kontext Pro Image`: 
     * `prompt` Enter the prompt for the image you want to edit
     * `aspect_ratio` Set the aspect ratio of the original image, which must be between 1:4 and 4:1
     * `prompt_upsampling` Set whether to use prompt upsampling. If enabled, it will automatically modify the prompt to get richer results, but the results are not reproducible
  3. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image editing
  4. After waiting for the API to return results, you can view the edited image in the `Save Image` node, and the corresponding image will also be saved to the `ComfyUI/output/` directory



The subsequent two workflows only differ in the Partner nodes used. In fact, you only need to modify based on the multiple image input workflow, with no significant differences

## 

​

FLUX.1 Kontext Pro Image Partner Nodes Workflow

### 

​

1\. Workflow File Download

The `metadata` of the image below contains the workflow information. Please download and drag it into ComfyUI to load the corresponding workflow. ![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image.png) Download the image below for input or use your own image: ![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image_input.png)

### 

​

2\. Complete the Workflow Step by Step

![ComfyUI FLUX.1 Kontext Pro Image Partner Nodes Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ff2c42a34894ae54e32a24058ad12755) You can follow the numbered steps in the image to complete the workflow:

  1. Load the image you want to edit in the `Load Image` node
  2. (Optional) Modify the necessary parameters in `Flux.1 Kontext Pro Image`
  3. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image editing
  4. After waiting for the API to return results, you can view the edited image in the `Save Image` node, and the corresponding image will also be saved to the `ComfyUI/output/` directory



## 

​

FLUX.1 Kontext Max Image Partner Nodes Workflow

### 

​

1\. Workflow File Download

The `metadata` of the image below contains the workflow information. Please download and drag it into ComfyUI to load the corresponding workflow. ![ComfyUI FLUX.1 Kontext Max Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image.png) Download the image below for input or use your own image for demonstration: ![ComfyUI FLUX.1 Kontext Max Image Partner Nodes Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image_input.png)

### 

​

2\. Complete the Workflow Step by Step

![ComfyUI FLUX.1 Kontext Max Image Partner Nodes Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3f91d4f54822bef88bca4e7024170950) You can follow the numbered steps in the image to complete the workflow:

  1. Load the image you want to edit in the `Load Image` node
  2. (Optional) Modify the necessary parameters in `Flux.1 Kontext Max Image`
  3. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image editing
  4. After waiting for the API to return results, you can view the edited image in the `Save Image` node, and the corresponding image will also be saved to the `ComfyUI/output/` directory



## 

​

FLUX Kontext Prompt Techniques

### 

​

1\. Basic Modifications

  * Simple and direct: `"Change the car color to red"`
  * Maintain style: `"Change to daytime while maintaining the same style of the painting"`



### 

​

2\. Style Transfer

**Principles:**

  * Clearly name style: `"Transform to Bauhaus art style"`
  * Describe characteristics: `"Transform to oil painting with visible brushstrokes, thick paint texture"`
  * Preserve composition: `"Change to Bauhaus style while maintaining the original composition"`



### 

​

3\. Character Consistency

**Framework:**

  * Specific description: `"The woman with short black hair"` instead of “she”
  * Preserve features: `"while maintaining the same facial features, hairstyle, and expression"`
  * Step-by-step modifications: Change background first, then actions



### 

​

4\. Text Editing

  * Use quotes: `"Replace 'joy' with 'BFL'"`
  * Maintain format: `"Replace text while maintaining the same font style"`



## 

​

Common Problem Solutions

### 

​

Character Changes Too Much

❌ Wrong: `"Transform the person into a Viking"` ✅ Correct: `"Change the clothes to be a viking warrior while preserving facial features"`

### 

​

Composition Position Changes

❌ Wrong: `"Put him on a beach"` ✅ Correct: `"Change the background to a beach while keeping the person in the exact same position, scale, and pose"`

### 

​

Style Application Inaccuracy

❌ Wrong: `"Make it a sketch"` ✅ Correct: `"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"`

## 

​

Core Principles

  1. **Be Specific and Clear** \- Use precise descriptions, avoid vague terms
  2. **Step-by-step Editing** \- Break complex modifications into multiple simple steps
  3. **Explicit Preservation** \- State what should remain unchanged
  4. **Verb Selection** \- Use “change”, “replace” rather than “transform”



## 

​

Best Practice Templates

**Object Modification:** `"Change [object] to [new state], keep [content to preserve] unchanged"` **Style Transfer:** `"Transform to [specific style], while maintaining [composition/character/other] unchanged"` **Background Replacement:** `"Change the background to [new background], keep the subject in the exact same position and pose"` **Text Editing:** `"Replace '[original text]' with '[new text]', maintain the same font style"`

> **Remember:** The more specific, the better. Kontext excels at understanding detailed instructions and maintaining consistency.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/black-forest-labs/flux-1-kontext.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/black-forest-labs/flux-1-kontext)

[FLUX 1.1 Pro Ultra in ComfyUI: 4 MP Text-to-Image and Image RemixPrevious](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)[FLUX 3 Image in ComfyUI: Text to Image and Image EditNext](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-image)

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
