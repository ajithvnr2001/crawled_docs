---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-color-rgb/
title: Recraft Color RGB - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:39.758278+00:00
---

# Recraft Color RGB - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-color-rgb/

## On this page

Back to top

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

## Node Function

This node creates a color configuration object that connects to the Recraft Controls node to specify colors used in generated images.

## Parameters

### Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
r| integer| 0| Red channel (0-255)  
g| integer| 0| Green channel (0-255)  
b| integer| 0| Blue channel (0-255)  
  
### Output

Output| Type| Description  
---|---|---  
recraft_color| Recraft Color| Color config object to connect to Recraft Controls  
  
## Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## Source Code

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

[OpenAI GPT Image 1](https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-gpt-image1)[Recraft Controls](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-controls)
