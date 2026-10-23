---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-template/
title: PixVerse Template - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:34.042065+00:00
---

# PixVerse Template - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-template/

## On this page

  * Parameters
    * Required Parameters
    * Output
  * Source Code



PixVerse

# PixVerse Template - ComfyUI Native Node Documentation

Copy pageCopy page

A helper node that provides preset templates for PixVerse video generation

Copy pageCopy page

![ComfyUI Native PixVerse Template Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9995576d223575123de26cc31872a7f1) The PixVerse Template node lets you choose from predefined video generation templates to control the style and effects of PixVerse video generation nodes. This helper node connects to PixVerse video generation nodes, allowing users to quickly apply preset video styles without manually adjusting complex parameter combinations.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Description  
---|---|---  
template| Select| Choose a template from available video presets  
  
### 

​

Output

Output| Type| Description  
---|---|---  
pixverse_template| PixverseIO.TEMPLATE| Configuration object containing the selected template ID  
  
## 

​

Source Code

[Node Source Code (Updated 2025-05-05)]
    
    
    class PixverseTemplateNode:
        """
        Select template for Pixverse Video generation.
        """
    
        RETURN_TYPES = (PixverseIO.TEMPLATE,)
        RETURN_NAMES = ("pixverse_template",)
        FUNCTION = "create_template"
        CATEGORY = "api node/video/Pixverse"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "template": (list(pixverse_templates.keys()), ),
                }
            }
    
        def create_template(self, template: str):
            template_id = pixverse_templates.get(template, None)
            if template_id is None:
                raise Exception(f"Template '{template}' is not recognized.")
            # just return the integer
            return (template_id,)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/pixverse/pixverse-template.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/pixverse/pixverse-template)

[PixVerse Image to Video - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-image-to-video)[PixVerse Text to Video - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-text-to-video)

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
