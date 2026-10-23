---
url: https://docs.comfy.org/tutorials/partner-nodes/krea/krea-2-t2i/
title: Krea 2 in ComfyUI: Text-to-Image with Style References - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:32.663399+00:00
---

# Krea 2 in ComfyUI: Text-to-Image with Style References - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/krea/krea-2-t2i/

## On this page

  * What Krea 2 Text to Image is good at
  * Krea 2 Image Node Documentation
  * Krea 2 Text to Image Workflow
  * Krea 2 Style Reference Workflow
  * Additional Notes



Krea

# Krea 2 in ComfyUI: Text-to-Image with Style References

Copy pageCopy page

Generate images with the Krea 2 Image node in ComfyUI using Krea 2 Medium or Large, up to 10 style references, moodboards, and adjustable creativity.

Copy pageCopy page

The [Krea 2 Image Node](https://docs.comfy.org/built-in-nodes/Krea2ImageNode) allows you to generate high-quality images from text prompts using Krea AI’s next-generation model. It supports two model variants, **Krea 2 Medium** for expressive illustrations and **Krea 2 Large** for expressive photorealism, with optional moodboard and style reference inputs.

## 

​

What Krea 2 Text to Image is good at

  * **Two model variants** : Krea 2 Medium for expressive illustrations, Krea 2 Large for expressive photorealism
  * **Style references** : Apply the aesthetic style, mood, and visual direction of up to 10 reference images to your generation
  * **Moodboard support** : Use the `moodboard_id` parameter with a moodboard from [Krea’s website](https://www.krea.ai)
  * **Adjustable generation settings** : Control aspect ratio, resolution, creativity level, and seed



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

Krea 2 Image Node Documentation

Check the following documentation for detailed node parameter settings:

  * [Krea 2 Image Node](https://docs.comfy.org/built-in-nodes/Krea2ImageNode)
  * [Krea 2 Style Reference Node](https://docs.comfy.org/built-in-nodes/Krea2StyleReferenceNode)



## 

​

Krea 2 Text to Image Workflow

![Krea 2 Text to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Krea2” in Template Library

  1. **Enter your prompt** : type a text description in the **Krea2ImageNode**
  2. **Select a model variant** : choose between **Krea 2 Medium** (illustrations) or **Krea 2 Large** (photorealism)
  3. **Adjust parameters** : set aspect ratio, resolution, creativity level, and seed
  4. **Click Queue** : press `Ctrl+Enter` or click the Queue button to generate
  5. **View result** : the generated image appears in the **SaveImage** node, saved to `ComfyUI/output/`



## 

​

Krea 2 Style Reference Workflow

![Krea 2 Style Reference Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_style_reference-1.webp) The Style Reference workflow adds an extra step: upload one or more reference images that define the aesthetic style, mood, and visual direction. The generated image will match your prompt while applying the style from your reference images.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Krea 2: Style Reference” in Template Library

  1. **Upload reference images** : use the **LoadImage** nodes to load style reference images (supports up to 10)
  2. **Enter your prompt** : describe the scene you want in the **Krea2ImageNode**
  3. **Select a model variant** : choose between Medium and Large
  4. **Adjust style strength** : modify the style reference strength in the **Krea2StyleReferenceNode** nodes
  5. **Click Queue** : press `Ctrl+Enter` to generate
  6. **View result** : the generated image appears in the **SaveImage** node



## 

​

Additional Notes

  * The Krea 2 Image node supports up to **10 style reference images** simultaneously
  * The `moodboard_id` parameter requires a valid UUID from a Krea moodboard on [Krea’s website](https://www.krea.ai)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/krea/krea-2-t2i.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/krea/krea-2-t2i)

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
