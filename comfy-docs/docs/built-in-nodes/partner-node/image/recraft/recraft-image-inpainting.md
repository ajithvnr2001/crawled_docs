---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-image-inpainting/
title: Recraft Image Inpainting - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:39.198344+00:00
---

# Recraft Image Inpainting - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-image-inpainting/

## On this page

Back to top

  * Parameters
    * Basic Parameters
    * Optional Parameters
    * Output
  * Source Code



Recraft

# Recraft Image Inpainting - ComfyUI Native Node Documentation

Copy pageCopy page

Selectively modify image regions using Recraft API

Copy pageCopy page

![ComfyUI Native Recraft Image Inpainting Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ce37045a2a53e129f5bec3e425f0002b) The Recraft Image Inpainting node lets you modify specific areas of an image while keeping the rest unchanged. By providing an image, mask and text prompt, you can generate new content to fill the selected areas.

## Parameters

### Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| -| Input image to modify  
mask| mask| -| Black and white mask defining areas to change  
prompt| string| ""| Text describing what to generate in masked area  
n| integer| 1| Number of results to generate (1-6)  
seed| integer| 0| Random seed value  
  
### Optional Parameters

Parameter| Type| Description  
---|---|---  
recraft_style| Recraft Style| Style settings for generated content  
negative_prompt| string| Elements to avoid in generated content  
recraft_controls| Recraft Controls| Additional controls like colors  
  
### Output

Output| Type| Description  
---|---|---  
IMAGE| image| Modified image result  
  
## Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftImageInpaintingNode:
        """
        Modify image based on prompt and mask.
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
                    "mask": (IO.MASK, ),
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
            mask: torch.Tensor,
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
                random_seed=seed,
            )
    
            # prepare mask tensor
            _, H, W, _ = image.shape
            mask = mask.unsqueeze(-1)
            mask = mask.movedim(-1,1)
            mask = common_upscale(mask, width=W, height=H, upscale_method="nearest-exact", crop="disabled")
            mask = mask.movedim(1,-1)
            mask = (mask > 0.5).float()
    
            images = []
            total = image.shape[0]
            pbar = ProgressBar(total)
            for i in range(total):
                sub_bytes = handle_recraft_file_request(
                    image=image[i],
                    mask=mask[i:i+1],
                    path="/proxy/recraft/images/inpaint",
                    request=request,
                    auth_token=auth_token,
                )
                images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
                pbar.update(1)
    
            images_tensor = torch.cat(images, dim=0)
            return (images_tensor, )
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-image-inpainting.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-image-inpainting)

[Recraft Crisp Upscale](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-crisp-upscale)[Recraft Image to Image](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-image-to-image)
