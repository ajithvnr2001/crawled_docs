---
url: https://docs.comfy.org/interface/features/autogrow-inputs/
title: Dynamic Inputs - Autogrow Node Slots in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:00.594872+00:00
---

# Dynamic Inputs - Autogrow Node Slots in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/interface/features/autogrow-inputs/

## On this page

  * How autogrow inputs work
  * Nodes that use autogrow inputs



Feature components

# Dynamic Inputs - Autogrow Node Slots in ComfyUI

Copy pageCopy page

Autogrow inputs add a new slot to a node when you fill the last one, so a single node can take as many images, masks or latents as you need.

Copy pageCopy page

![Batch Images node with one image connected and one free input below it](https://mintcdn.com/dripart/U2iZLdB9XBorZSfA/images/interface/features/autogrow/autogrow-1.png?fit=max&auto=format&n=U2iZLdB9XBorZSfA&q=85&s=b702db2e40661333c41b9783a2090f38) Some nodes in ComfyUI have **autogrow inputs** , also called **dynamic inputs**. These nodes do not show a fixed list of slots. They add another input as soon as you connect the last free one, so a single node can batch two images or twenty without any extra setup.

## 

​

How autogrow inputs work

  1. **Connect the last free input.** In the example on this page, an image source is linked to `image0` on the **Batch Images** node, while `image1` is still free.
  2. **Watch the node grow.** As soon as you fill the last free input, the node appends a new empty input below it. In the picture below, the new `image2` input appears after `image1` is connected.
  3. **Repeat as needed.** Every time you fill the last input, the node grows again, until it reaches the maximum number of inputs that node allows.

![Batch Images node with two connected inputs and a newly added free input highlighted](https://mintcdn.com/dripart/U2iZLdB9XBorZSfA/images/interface/features/autogrow/autogrow-2.png?fit=max&auto=format&n=U2iZLdB9XBorZSfA&q=85&s=cafe6c1aa5420a7c2445ff30fb499548) Two more details worth knowing:

  * **Order matters.** The inputs are passed to the node in the order they appear, so `image0` comes before `image1` and so on. Keep that in mind when the result depends on the sequence, for example when you batch images that run through a video model.
  * **The free input is a placeholder.** It is only part of the node’s data once you connect something to it. A node that allows zero inputs still runs when every slot is empty.



## 

​

Nodes that use autogrow inputs

Node| Input that grows| Maximum inputs  
---|---|---  
**Batch Images**| `image`| 50  
**Batch Masks**| `mask`| 50  
**Batch Latents**| `latent`| 50  
**And** / **Or**| `value`| 10  
**Nano Banana 2** and other partner nodes that take reference images| `image_1`, `image_2`, and so on| up to 14 images  
  
Each node decides its own limits. Hover the input in ComfyUI to read its tooltip when you are not sure how many values it accepts.

Autogrow is part of the ComfyUI V3 node schema. If you write custom nodes, see [Dynamic Inputs](https://docs.comfy.org/custom-nodes/v3_migration#dynamic-inputs) for the `Autogrow` template API.

## Batch Images node

Combine several images into one batch, with as many inputs as you need.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/features/autogrow-inputs.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/features/autogrow-inputs)

[Node docs - View documentation for any nodePrevious](https://docs.comfy.org/interface/features/node-docs)[Mask Editor - Create and Edit Masks in ComfyUINext](https://docs.comfy.org/interface/maskeditor)

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
