---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-digital-illustration/
title: Recraft Style - Digital Illustration - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:38.985622+00:00
---

# Recraft Style - Digital Illustration - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-digital-illustration/

## On this page

Back to top

  * Parameters
    * Basic Parameters
    * Output
  * Usage Example
  * Source Code



Recraft

# Recraft Style - Digital Illustration - ComfyUI Native Node Documentation

Copy pageCopy page

A helper node for setting digital illustration style in Recraft image generation

Copy pageCopy page

![ComfyUI Native Recraft Style Digital Illustration Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=dce25f2de84056b2fe15b3264ffcf80e) This node creates a style configuration object that guides Recraft’s image generation process towards a digital illustration look.

## Parameters

### Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
substyle| select| None| Specific substyle of digital illustration  
  
### Output

Output| Type| Description  
---|---|---  
recraft_style| Recraft Style| Style config object to connect to Recraft generation nodes  
  
## Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftStyleV3DigitalIllustrationNode(RecraftStyleV3RealisticImageNode):
        """
        Select digital_illustration style and optional substyle.
        """
    
        RECRAFT_STYLE = RecraftStyleV3.digital_illustration
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-style-digital-illustration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-style-digital-illustration)

[Recraft Replace Background](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-replace-background)[Recraft Style - Logo Raster](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-logo-raster)
