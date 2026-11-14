---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-controls/
title: Recraft Controls - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:39.679591+00:00
---

# Recraft Controls - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-controls/

## On this page

Back to top

  * Parameters
    * Optional Parameters
    * Output
  * Usage Example
  * How It Works
  * Source Code



Recraft

# Recraft Controls - ComfyUI Native Node Documentation

Copy pageCopy page

Node providing advanced control parameters for Recraft image generation

Copy pageCopy page

![ComfyUI Native Recraft Controls Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6c5b9b0c3f9e255975e9bca7d12a9d2b) The Recraft Controls node lets you define control parameters (like colors and background colors) to guide Recraft’s image generation process. This node combines multiple control inputs into a unified control object.

## Parameters

### Optional Parameters

Parameter| Type| Description  
---|---|---  
colors| Recraft Color| Color controls for image generation  
background_color| Recraft Color| Background color control  
  
### Output

Output| Type| Description  
---|---|---  
recraft_controls| Recraft Controls| Control config object for Recraft generation nodes  
  
## Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## How It Works

Node process:

  1. Collects input control parameters (colors and background_color)
  2. Combines these parameters into a structured control object
  3. Outputs this control object for connecting to Recraft generation nodes

When connected to Recraft generation nodes, these control parameters influence the AI generation process. The AI considers multiple factors beyond just the text prompt’s semantic content. If color inputs are configured, the AI will try to use these colors appropriately in the generated image.

## Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftControlsNode:
        """
        Create Recraft Controls for customizing Recraft generation.
        """
    
        RETURN_TYPES = (RecraftIO.CONTROLS,)
        RETURN_NAMES = ("recraft_controls",)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "create_controls"
        CATEGORY = "api node/image/Recraft"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                },
                "optional": {
                    "colors": (RecraftIO.COLOR,),
                    "background_color": (RecraftIO.COLOR,),
                }
            }
    
        def create_controls(self, colors: RecraftColorChain=None, background_color: RecraftColorChain=None):
            return (RecraftControls(colors=colors, background_color=background_color), )
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-controls.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-controls)

[Recraft Color RGB](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-color-rgb)[Recraft Creative Upscale](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-creative-upscale)
