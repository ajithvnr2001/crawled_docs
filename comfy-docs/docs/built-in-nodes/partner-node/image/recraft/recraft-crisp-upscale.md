---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-crisp-upscale/
title: Recraft Crisp Upscale - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:28.942355+00:00
---

# Recraft Crisp Upscale - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-crisp-upscale/

## On this page

  * Parameters
    * Basic Parameters
    * Output
  * Source Code



Recraft

# Recraft Crisp Upscale - ComfyUI Native Node Documentation

Copy pageCopy page

A Recraft Partner node that enhances image clarity and resolution using AI

Copy pageCopy page

![ComfyUI Native Recraft Crisp Upscale Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=69f9f1c716832688e95c562c1f9be1c2) The Recraft Crisp Upscale node uses Recraft’s API to improve image resolution and clarity.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| -| Input image to be upscaled  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| image| Upscaled and enhanced output image  
  
## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftCrispUpscaleNode:
        """
        Upscale image synchronously.
        Enhances a given raster image using ‘crisp upscale’ tool, increasing image resolution, making the image sharper and cleaner.
        """
    
        RETURN_TYPES = (IO.IMAGE,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/image/Recraft"
    
        RECRAFT_PATH = "/proxy/recraft/images/crispUpscale"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "image": (IO.IMAGE, ),
                },
                "optional": {
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        def api_call(
            self,
            image: torch.Tensor,
            auth_token=None,
            **kwargs,
        ):
            images = []
            total = image.shape[0]
            pbar = ProgressBar(total)
            for i in range(total):
                sub_bytes = handle_recraft_file_request(
                    image=image[i],
                    path=self.RECRAFT_PATH,
                    auth_token=auth_token,
                )
                images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
                pbar.update(1)
    
            images_tensor = torch.cat(images, dim=0)
            return (images_tensor,)
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-crisp-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-crisp-upscale)

[Recraft Creative Upscale - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-creative-upscale)[Recraft Image Inpainting - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-image-inpainting)

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
