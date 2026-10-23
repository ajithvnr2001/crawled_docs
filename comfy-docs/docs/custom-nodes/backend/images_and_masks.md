---
url: https://docs.comfy.org/custom-nodes/backend/images_and_masks/
title: Images, Latents, and Masks - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:35.937023+00:00
---

# Images, Latents, and Masks - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/images_and_masks/

## On this page

  * Images
    * Working with PIL.Image
  * Masks
    * Masks from the Load Image Node
    * Understanding Mask Shapes
  * Latents



Python (Backend)

# Images, Latents, and Masks

Copy pageCopy page

Master backend data handling for Comfy custom nodes images and masks. Learn PyTorch tensor shapes, PIL conversions, and latents. Read the developer docs today.

Copy pageCopy page

When working with these datatypes, you will need to know about the `torch.Tensor` class. Complete documentation is [here](https://pytorch.org/docs/stable/tensors.html), or an introduction to the key concepts required for Comfy [here](https://docs.comfy.org/custom-nodes/backend/images_and_masks/tensors).

If your node has a single output which is a tensor, remember to return `(image,)` not `(image)`

Most of the concepts below are illustrated in the [example code snippets](https://docs.comfy.org/custom-nodes/backend/images_and_masks/snippets).

## 

​

Images

An IMAGE is a `torch.Tensor` with shape `[B,H,W,C]`, `C=3`. If you are going to save or load images, you will need to convert to and from `PIL.Image` format - see the code snippets below! Note that some `pytorch` operations offer (or expect) `[B,C,H,W]`, known as ‘channel first’, for reasons of computational efficiency. Just be careful.

### 

​

Working with PIL.Image

If you want to load and save images, you’ll want to use PIL:
    
    
    from PIL import Image, ImageOps
    

## 

​

Masks

A MASK is a `torch.Tensor` with shape `[B,H,W]`. In many contexts, masks have binary values (0 or 1), which are used to indicate which pixels should undergo specific operations. In some cases values between 0 and 1 are used indicate an extent of masking, (for instance, to alter transparency, adjust filters, or composite layers).

### 

​

Masks from the Load Image Node

The `LoadImage` node uses an image’s alpha channel (the “A” in “RGBA”) to create MASKs. The values from the alpha channel are normalized to the range [0,1] (torch.float32) and then inverted. The `LoadImage` node always produces a MASK output when loading an image. Many images (like JPEGs) don’t have an alpha channel. In these cases, `LoadImage` creates a default mask with the shape `[1, 64, 64]`.

### 

​

Understanding Mask Shapes

In libraries like `numpy`, `PIL`, and many others, single-channel images (like masks) are typically represented as 2D arrays, shape `[H,W]`. This means the `C` (channel) dimension is implicit, and thus unlike IMAGE types, batches of MASKs have only three dimensions: `[B, H, W]`. It is not uncommon to encounter a mask which has had the `B` dimension implicitly squeezed, giving a tensor `[H,W]`. To use a MASK, you will often have to match shapes by unsqueezing to produce a shape `[B,H,W,C]` with `C=1` To unsqueezing the `C` dimension, so you should `unsqueeze(-1)`, to unsqueeze `B`, you `unsqueeze(0)`. If your node receives a MASK as input, you would be wise to always check `len(mask.shape)`.

## 

​

Latents

A LATENT is a `dict`; the latent sample is referenced by the key `samples` and has shape `[B,C,H,W]`, with `C=4`.

LATENT is channel first, IMAGE is channel last

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/images_and_masks.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/images_and_masks)

[ComfyUI Custom Node DatatypesPrevious](https://docs.comfy.org/custom-nodes/backend/datatypes)[Hidden and Flexible inputsNext](https://docs.comfy.org/custom-nodes/backend/more_on_inputs)

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
