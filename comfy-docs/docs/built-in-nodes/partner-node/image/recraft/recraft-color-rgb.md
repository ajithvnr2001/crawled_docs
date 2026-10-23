---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-color-rgb/
title: Recraft Color RGB - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:28.455662+00:00
---

# Recraft Color RGB - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-color-rgb/

## On this page

  * Node Function
  * Parameters
    * Basic Parameters
    * Output
  * Usage Example
  * Source Code



Recraft

# Recraft Color RGB - ComfyUI Native Node Documentation

Copy pageCopy page

Helper node for defining color controls in Recraft image generation

Copy pageCopy page

![ComfyUI Native Recraft Color RGB Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=406b336f43d8d8872ab620d8d5777f5f) The Recraft Color RGB node lets you define precise RGB color values to control colors in Recraft image generation.

## 

​

Node Function

This node creates a color configuration object that connects to the Recraft Controls node to specify colors used in generated images.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
r| integer| 0| Red channel (0-255)  
g| integer| 0| Green channel (0-255)  
b| integer| 0| Blue channel (0-255)  
  
### 

​

Output

Output| Type| Description  
---|---|---  
recraft_color| Recraft Color| Color config object to connect to Recraft Controls  
  
## 

​

Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftColorRGBNode:
        """
        Create Recraft Color by choosing specific RGB values.
        """
    
        RETURN_TYPES = (RecraftIO.COLOR,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        RETURN_NAMES = ("recraft_color",)
        FUNCTION = "create_color"
        CATEGORY = "api node/image/Recraft"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "r": (IO.INT, {
                        "default": 0,
                        "min": 0,
                        "max": 255,
                        "tooltip": "Red value of color."
                    }),
                    "g": (IO.INT, {
                        "default": 0,
                        "min": 0,
                        "max": 255,
                        "tooltip": "Green value of color."
                    }),
                    "b": (IO.INT, {
                        "default": 0,
                        "min": 0,
                        "max": 255,
                        "tooltip": "Blue value of color."
                    }),
                },
                "optional": {
                    "recraft_color": (RecraftIO.COLOR,),
                }
            }
    
        def create_color(self, r: int, g: int, b: int, recraft_color: RecraftColorChain=None):
            recraft_color = recraft_color.clone() if recraft_color else RecraftColorChain()
            recraft_color.add(RecraftColor(r, g, b))
            return (recraft_color, )
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-color-rgb.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-color-rgb)

[OpenAI GPT Image 1 - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-gpt-image1)[Recraft Controls - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-controls)

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
