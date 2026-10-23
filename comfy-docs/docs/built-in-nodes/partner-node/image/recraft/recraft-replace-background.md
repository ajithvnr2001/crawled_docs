---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-replace-background/
title: Recraft Replace Background - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:29.592109+00:00
---

# Recraft Replace Background - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-replace-background/

## On this page

  * Parameters
    * Basic Parameters
    * Optional Parameters
    * Output
  * Source Code



Recraft

# Recraft Replace Background - ComfyUI Native Node Documentation

Copy pageCopy page

A Recraft Partner node that automatically detects foreground subjects and replaces backgrounds

Copy pageCopy page

![ComfyUI Native Recraft Replace Background Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=798d76cef5bcc224546b066e8a9b2db2) The Recraft Replace Background node uses Recraft’s API to intelligently detect subjects in images and generate new backgrounds based on text prompts.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| -| Input image with subject to preserve  
prompt| string| ""| Text prompt for background generation  
n| integer| 1| Number of images to generate (1-6)  
seed| integer| 0| Random seed value for node re-runs  
  
### 

​

Optional Parameters

Parameter| Type| Description  
---|---|---  
recraft_style| Recraft Style| Style settings for background generation  
negative_prompt| string| Text describing elements to avoid  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| image| Final image with replaced background  
  
## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftReplaceBackgroundNode:
        """
        Replace background on image, based on provided prompt.
        """
    
        RETURN_TYPES = (IO.IMAGE,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/image/Recraft"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "image": (IO.IMAGE, ),
                    "prompt": (
                        IO.STRING,
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Prompt for the image generation.",
                        },
                    ),
                    "n": (
                        IO.INT,
                        {
                            "default": 1,
                            "min": 1,
                            "max": 6,
                            "tooltip": "The number of images to generate.",
                        },
                    ),
                    "seed": (
                        IO.INT,
                        {
                            "default": 0,
                            "min": 0,
                            "max": 0xFFFFFFFFFFFFFFFF,
                            "control_after_generate": True,
                            "tooltip": "Seed to determine if node should re-run; actual results are nondeterministic regardless of seed.",
                        },
                    ),
                },
                "optional": {
                    "recraft_style": (RecraftIO.STYLEV3,),
                    "negative_prompt": (
                        IO.STRING,
                        {
                            "default": "",
                            "forceInput": True,
                            "tooltip": "An optional text description of undesired elements on an image.",
                        },
                    ),
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        def api_call(
            self,
            image: torch.Tensor,
            prompt: str,
            n: int,
            seed,
            auth_token=None,
            recraft_style: RecraftStyle = None,
            negative_prompt: str = None,
            **kwargs,
        ):
            default_style = RecraftStyle(RecraftStyleV3.realistic_image)
            if recraft_style is None:
                recraft_style = default_style
    
            if not negative_prompt:
                negative_prompt = None
    
            request = RecraftImageGenerationRequest(
                prompt=prompt,
                negative_prompt=negative_prompt,
                model=RecraftModel.recraftv3,
                n=n,
                style=recraft_style.style,
                substyle=recraft_style.substyle,
                style_id=recraft_style.style_id,
            )
    
            images = []
            total = image.shape[0]
            pbar = ProgressBar(total)
            for i in range(total):
                sub_bytes = handle_recraft_file_request(
                    image=image[i],
                    path="/proxy/recraft/images/replaceBackground",
                    request=request,
                    auth_token=auth_token,
                )
                images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
                pbar.update(1)
    
            images_tensor = torch.cat(images, dim=0)
            return (images_tensor, )
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-replace-background.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-replace-background)

[Recraft Remove Background - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-remove-background)[Recraft Style - Digital Illustration - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-style-digital-illustration)

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
