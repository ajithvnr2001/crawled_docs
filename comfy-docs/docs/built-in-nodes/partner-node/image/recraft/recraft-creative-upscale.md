---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-creative-upscale/
title: Recraft Creative Upscale - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:28.744535+00:00
---

# Recraft Creative Upscale - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-creative-upscale/

## On this page

  * Parameters
    * Basic Parameters
    * Output
  * Source Code



Recraft

# Recraft Creative Upscale - ComfyUI Native Node Documentation

Copy pageCopy page

A Recraft Partner node that uses AI to creatively enhance image details and resolution

Copy pageCopy page

![ComfyUI Native Recraft Creative Upscale Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7478834eaacd7370aad308c51518c743) The Recraft Creative Upscale node uses Recraft’s API to increase image resolution while creatively enhancing and enriching image details.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| -| Input image to be creatively upscaled  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| image| High-resolution image after creative upscaling  
  
## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftCreativeUpscaleNode(RecraftCrispUpscaleNode):
        """
        Upscale image synchronously.
        Enhances a given raster image using ‘creative upscale’ tool, boosting resolution with a focus on refining small details and faces.
        """
    
        RETURN_TYPES = (IO.IMAGE,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/image/Recraft"
    
        RECRAFT_PATH = "/proxy/recraft/images/creativeUpscale"
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-creative-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-creative-upscale)

[Recraft Controls - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-controls)[Recraft Crisp Upscale - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-crisp-upscale)

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
