---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-vectorize-image/
title: Recraft Vectorize Image - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:30.211033+00:00
---

# Recraft Vectorize Image - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-vectorize-image/

## On this page

  * Parameters
    * Basic Parameters
    * Output
  * Usage Example
  * Source Code



Recraft

# Recraft Vectorize Image - ComfyUI Built-in Node Documentation

Copy pageCopy page

A Recraft Partner node that converts raster images to vector SVG format

Copy pageCopy page

![ComfyUI Built-in Recraft Vectorize Image Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=5d51a1b8e3e0147a608b40a2b63fd03b) The Recraft Vectorize Image node uses Recraft’s API to convert raster images (like photos, PNGs or JPEGs) into vector SVG format.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| Image| -| Input image to be converted to vector  
  
### 

​

Output

Output| Type| Description  
---|---|---  
SVG| Vector| Converted SVG vector graphic, needs to be connected to SaveSVG node to save  
  
## 

​

Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## 

​

Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class RecraftVectorizeImageNode:
        """
        Generates SVG synchronously from an input image.
        """
    
        RETURN_TYPES = (RecraftIO.SVG,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/image/Recraft"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "image": (IO.IMAGE, ),
                },
                "optional": {
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        def api_call(
            self,
            image: torch.Tensor,
            auth_token=None,
            **kwargs,
        ):
            svgs = []
            total = image.shape[0]
            pbar = ProgressBar(total)
            for i in range(total):
                sub_bytes = handle_recraft_file_request(
                    image=image[i],
                    path="/proxy/recraft/images/vectorize",
                    auth_token=auth_token,
                )
                svgs.append(SVG(sub_bytes))
                pbar.update(1)
    
            return (SVG.combine_all(svgs), )
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-vectorize-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-vectorize-image)

[Recraft Text to Vector - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-text-to-vector)[Save SVG - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/save-svg)

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
