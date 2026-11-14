---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-template/
title: PixVerse Template - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:37.276459+00:00
---

# PixVerse Template - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-template/

## On this page

Back to top

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

## Parameters

### Required Parameters

Parameter| Type| Description  
---|---|---  
template| Select| Choose a template from available video presets  
  
### Output

Output| Type| Description  
---|---|---  
pixverse_template| PixverseIO.TEMPLATE| Configuration object containing the selected template ID  
  
## Source Code

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

[PixVerse Image to Video](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-image-to-video)[PixVerse Text to Video](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-text-to-video)
