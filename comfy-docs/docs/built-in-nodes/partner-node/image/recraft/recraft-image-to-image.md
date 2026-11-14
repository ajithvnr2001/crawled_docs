---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-image-to-image/
title: Recraft Image to Image - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:39.292010+00:00
---

# Recraft Image to Image - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-image-to-image/

## On this page

Back to top

  * Parameters
    * Basic Parameters
    * Optional Parameters
    * Output
  * Source Code



Recraft

# Recraft Image to Image - ComfyUI Native Node Documentation

Copy pageCopy page

A Recraft Partner node that generates new images based on text prompts and reference images

Copy pageCopy page

![ComfyUI Native Recraft Image to Image Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=80e1a35d96e8943dee2cd18151db2db4) The Recraft Image to Image node uses Recraft’s API to generate new images based on a reference image and text prompts.

## Parameters

### Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| -| Reference image input  
prompt| string| ""| Text description for the generated image  
n| integer| 1| Number of images to generate (1-6)  
seed| integer| 0| Random seed value  
  
### Optional Parameters

Parameter| Type| Description  
---|---|---  
recraft_style| Recraft Style| Style settings for generated images  
negative_prompt| string| Elements to avoid in generated images  
recraft_controls| Recraft Controls| Additional controls like colors  
  
### Output

Output| Type| Description  
---|---|---  
IMAGE| image| Generated image result  
  
## Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftImageToImageNode:
        """
        Modify image based on prompt and strength.
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
                    "strength": (
                        IO.FLOAT,
                        {
                            "default": 0.5,
                            "min": 0.0,
                            "max": 1.0,
                            "step": 0.01,
                            "tooltip": "Defines the difference with the original image, should lie in [0, 1], where 0 means almost identical, and 1 means miserable similarity."
                        }
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
                    "recraft_controls": (
                        RecraftIO.CONTROLS,
                        {
                            "tooltip": "Optional additional controls over the generation via the Recraft Controls node."
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
            strength: float,
            seed,
            auth_token=None,
            recraft_style: RecraftStyle = None,
            negative_prompt: str = None,
            recraft_controls: RecraftControls = None,
            **kwargs,
        ):
            default_style = RecraftStyle(RecraftStyleV3.realistic_image)
            if recraft_style is None:
                recraft_style = default_style
    
            controls_api = None
            if recraft_controls:
                controls_api = recraft_controls.create_api_model()
    
            if not negative_prompt:
                negative_prompt = None
    
            request = RecraftImageGenerationRequest(
                prompt=prompt,
                negative_prompt=negative_prompt,
                model=RecraftModel.recraftv3,
                n=n,
                strength=round(strength, 2),
                style=recraft_style.style,
                substyle=recraft_style.substyle,
                style_id=recraft_style.style_id,
                controls=controls_api,
                random_seed=seed,
            )
    
            images = []
            total = image.shape[0]
            pbar = ProgressBar(total)
            for i in range(total):
                sub_bytes = handle_recraft_file_request(
                    image=image[i],
                    path="/proxy/recraft/images/imageToImage",
                    request=request,
                    auth_token=auth_token,
                )
                images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
                pbar.update(1)
    
            images_tensor = torch.cat(images, dim=0)
            return (images_tensor, )
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-image-to-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-image-to-image)

[Recraft Image Inpainting](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-image-inpainting)[Recraft Remove Background](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-remove-background)
