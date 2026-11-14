---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-logo-raster/
title: Recraft Style - Logo Raster - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:38.715151+00:00
---

# Recraft Style - Logo Raster - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-logo-raster/

## On this page

Back to top

  * Parameters
    * Basic Parameters
    * Output
  * Usage Example
  * Source Code



Recraft

# Recraft Style - Logo Raster - ComfyUI Built-in Node Documentation

Copy pageCopy page

Helper node for setting logo raster style in Recraft image generation

Copy pageCopy page

![ComfyUI Built-in Recraft Style - Logo Raster Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ec7753b1c7e871abc94ce5ea90472301) This node creates a style configuration object that guides Recraft’s image generation process toward professional logo design effects. By selecting different substyles, you can define the design style, complexity and use cases of the generated logo.

## Parameters

### Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
substyle| Selection| -| Specific substyle for logo raster (Required)  
  
### Output

Output| Type| Description  
---|---|---  
recraft_style| Recraft Style| Style configuration object, connects to Recraft generation node  
  
## Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class RecraftStyleV3LogoRasterNode(RecraftStyleV3RealisticImageNode):
        """
        Select vector_illustration style and optional substyle.
        """
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "substyle": (get_v3_substyles(s.RECRAFT_STYLE, include_none=False),),
                }
            }
    
        RECRAFT_STYLE = RecraftStyleV3.logo_raster
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-style-logo-raster.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-style-logo-raster)

[Recraft Style - Digital Illustration](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-digital-illustration)[Recraft Style - Realistic Image](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image)
