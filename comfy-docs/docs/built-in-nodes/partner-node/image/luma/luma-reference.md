---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-reference/
title: Luma Reference - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:28.350885+00:00
---

# Luma Reference - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-reference/

## On this page

  * Node Function
  * Parameters
    * Basic Parameters
    * Output
  * Usage Example
  * How It Works
  * Source Code



Luma

# Luma Reference - ComfyUI Built-in Node Documentation

Copy pageCopy page

Helper node providing reference images for Luma image generation

Copy pageCopy page

![ComfyUI Built-in Luma Reference Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-reference.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=95659c8c2dd4e09b26feef3901678c83) The Luma Reference node allows you to set reference images and weights to guide the creation process of Luma image generation nodes, making the generated images closer to specific features of the reference images.

## 

​

Node Function

This node works as a helper tool for Luma generation nodes, allowing users to provide reference images to influence generation results. It enables users to set the weight of reference images to control how much they affect the final result. Multiple Luma Reference nodes can be chained together, with a maximum of 4 working simultaneously according to API requirements.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| Image| -| Input image used as reference  
weight| Float| 1.0| Controls the strength of the reference image’s influence (0-1)  
  
### 

​

Output

Output| Type| Description  
---|---|---  
luma_ref| LUMA_REF| Reference object containing image and weight  
  
## 

​

Usage Example

## Luma Text to Image Workflow Example

Luma Text to Image Workflow Example

## 

​

How It Works

The Luma Reference node receives image input and allows setting a weight value. The node doesn’t directly generate or modify images but creates a reference object containing image data and weight information, which is then passed to Luma generation nodes. During the generation process, Luma AI analyzes the features of the reference image and incorporates these features into the generation results based on the set weight. Higher weight values mean the generated image will be closer to the reference image’s features, while lower weight values indicate the reference image will only slightly influence the final result.

## 

​

Source Code

[Node Source Code (Updated on 2025-05-03)]
    
    
    class LumaReferenceNode(ComfyNodeABC):
        """
        Holds an image and weight for use with Luma Generate Image node.
        """
    
        RETURN_TYPES = (LumaIO.LUMA_REF,)
        RETURN_NAMES = ("luma_ref",)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "create_luma_reference"
        CATEGORY = "api node/image/Luma"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "image": (
                        IO.IMAGE,
                        {
                            "tooltip": "Image to use as reference.",
                        },
                    ),
                    "weight": (
                        IO.FLOAT,
                        {
                            "default": 1.0,
                            "min": 0.0,
                            "max": 1.0,
                            "step": 0.01,
                            "tooltip": "Weight of image reference.",
                        },
                    ),
                },
                "optional": {"luma_ref": (LumaIO.LUMA_REF,)},
            }
    
        def create_luma_reference(
            self, image: torch.Tensor, weight: float, luma_ref: LumaReferenceChain = None
        ):
            if luma_ref is not None:
                luma_ref = luma_ref.clone()
            else:
                luma_ref = LumaReferenceChain()
            luma_ref.add(LumaReference(image=image, weight=round(weight, 2)))
            return (luma_ref,)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/luma/luma-reference.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/luma/luma-reference)

[Luma Image to Image - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-image-to-image)[Luma Text to Image - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-text-to-image)

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
