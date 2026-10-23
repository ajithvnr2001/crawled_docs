---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image/
title: Recraft Style - Realistic Image - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:30.519605+00:00
---

# Recraft Style - Realistic Image - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image/

## On this page

  * Node Function
  * Parameters
    * Basic Parameters
    * Output
  * Usage Example
  * Source Code



Recraft

# Recraft Style - Realistic Image - ComfyUI Native Node Documentation

Copy pageCopy page

A helper node for setting realistic photo style in Recraft image generation

Copy pageCopy page

![ComfyUI Native Recraft Style - Realistic Image Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d841ce2d09abd4dd25d467f459f3734f) The Recraft Style - Realistic Image node helps set up realistic photo styles for Recraft image generation, with various substyle options to control the visual characteristics of generated images.

## 

​

Node Function

This node creates a style configuration object that guides Recraft’s image generation process towards realistic photo effects.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
substyle| select| None| Specific substyle of realistic photo (Required)  
  
### 

​

Output

Output| Type| Description  
---|---|---  
recraft_style| Recraft Style| Style config object to connect to Recraft generation nodes  
  
## 

​

Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftStyleV3RealisticImageNode:
        """
        Select realistic_image style and optional substyle.
        """
    
        RETURN_TYPES = (RecraftIO.STYLEV3,)
        RETURN_NAMES = ("recraft_style",)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "create_style"
        CATEGORY = "api node/image/Recraft"
    
        RECRAFT_STYLE = RecraftStyleV3.realistic_image
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "substyle": (get_v3_substyles(s.RECRAFT_STYLE),),
                }
            }
    
        def create_style(self, substyle: str):
            if substyle == "None":
                substyle = None
            return (RecraftStyle(self.RECRAFT_STYLE, substyle),)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image)

[Recraft Style - Logo Raster - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-logo-raster)[Recraft Text to Image - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-text-to-image)

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
