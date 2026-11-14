---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image/
title: Recraft Style - Realistic Image - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:38.787882+00:00
---

# Recraft Style - Realistic Image - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image/

## On this page

Back to top

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

## Node Function

This node creates a style configuration object that guides Recraft’s image generation process towards realistic photo effects.

## Parameters

### Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
substyle| select| None| Specific substyle of realistic photo (Required)  
  
### Output

Output| Type| Description  
---|---|---  
recraft_style| Recraft Style| Style config object to connect to Recraft generation nodes  
  
## Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## Source Code

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

[Recraft Style - Logo Raster](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-logo-raster)[Recraft Text to Image](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-text-to-image)
