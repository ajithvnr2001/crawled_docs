---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v2/
title: Ideogram V2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:27.715521+00:00
---

# Ideogram V2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v2/

## On this page

  * Parameters
    * Required Parameters
    * Optional Parameters
    * Output
  * Source Code



Ideogram

# Ideogram V2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Node for creating high-quality images and text rendering using Ideogram V2 API

Copy pageCopy page

![ComfyUI Built-in Ideogram V2 Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b9df9b148b7fdd0552ee35417c59a769) The Ideogram V2 node allows you to generate more refined images using Ideogram’s second-generation AI model, with significant improvements in text rendering, image quality, and overall aesthetics.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| string| ""| Text prompt describing the content to generate  
turbo| boolean| False| Whether to use turbo mode (faster generation, possibly lower quality)  
  
### 

​

Optional Parameters

Parameter| Type| Default| Description  
---|---|---|---  
aspect_ratio| dropdown| ”1:1”| Image aspect ratio, effective when resolution is set to “Auto”  
resolution| dropdown| ”Auto”| Output image resolution, if not set to “Auto”, it will override the aspect_ratio setting  
magic_prompt_option| dropdown| ”AUTO”| Determines whether to use MagicPrompt feature during generation, options are [“AUTO”, “ON”, “OFF”]  
seed| integer| 0| Random seed value, range 0-2147483647  
style_type| dropdown| ”NONE”| Generation style type (V2 only), options are [“AUTO”, “GENERAL”, “REALISTIC”, “DESIGN”, “RENDER_3D”, “ANIME”]  
negative_prompt| string| ""| Specifies elements you don’t want to appear in the image  
num_images| integer| 1| Number of images to generate, range 1-8  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| image| Generated image(s)  
  
## 

​

Source Code

[Node Source Code (Updated on 2025-05-03)]
    
    
    class IdeogramV2(ComfyNodeABC):
        """
        Generates images synchronously using the Ideogram V2 model.
    
        Images links are available for a limited period of time; if you would like to keep the image, you must download it.
        """
    
        def __init__(self):
            pass
    
        @classmethod
        def INPUT_TYPES(cls) -> InputTypeDict:
            return {
                "required": {
                    "prompt": (
                        IO.STRING,
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Prompt for the image generation",
                        },
                    ),
                    "turbo": (
                        IO.BOOLEAN,
                        {
                            "default": False,
                            "tooltip": "Whether to use turbo mode (faster generation, potentially lower quality)",
                        }
                    ),
                },
                "optional": {
                    "aspect_ratio": (
                        IO.COMBO,
                        {
                            "options": list(V1_V2_RATIO_MAP.keys()),
                            "default": "1:1",
                            "tooltip": "The aspect ratio for image generation. Ignored if resolution is not set to AUTO.",
                        },
                    ),
                    "resolution": (
                        IO.COMBO,
                        {
                            "options": list(V1_V1_RES_MAP.keys()),
                            "default": "Auto",
                            "tooltip": "The resolution for image generation. If not set to AUTO, this overrides the aspect_ratio setting.",
                        },
                    ),
                    "magic_prompt_option": (
                        IO.COMBO,
                        {
                            "options": ["AUTO", "ON", "OFF"],
                            "default": "AUTO",
                            "tooltip": "Determine if MagicPrompt should be used in generation",
                        },
                    ),
                    "seed": (
                        IO.INT,
                        {
                            "default": 0,
                            "min": 0,
                            "max": 2147483647,
                            "step": 1,
                            "control_after_generate": True,
                            "display": "number",
                        },
                    ),
                    "style_type": (
                        IO.COMBO,
                        {
                            "options": ["AUTO", "GENERAL", "REALISTIC", "DESIGN", "RENDER_3D", "ANIME"],
                            "default": "NONE",
                            "tooltip": "Style type for generation (V2 only)",
                        },
                    ),
                    "negative_prompt": (
                        IO.STRING,
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Description of what to exclude from the image",
                        },
                    ),
                    "num_images": (
                        IO.INT,
                        {"default": 1, "min": 1, "max": 8, "step": 1, "display": "number"},
                    ),
                    #"color_palette": (
                    #    IO.STRING,
                    #    {
                    #        "multiline": False,
                    #        "default": "",
                    #        "tooltip": "Color palette preset name or hex colors with weights",
                    #    },
                    #),
                },
                "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
            }
    
        RETURN_TYPES = (IO.IMAGE,)
        FUNCTION = "api_call"
        CATEGORY = "api node/image/ideogram/v2"
        DESCRIPTION = cleandoc(__doc__ or "")
        API_NODE = True
    
        def api_call(
            self,
            prompt,
            turbo=False,
            aspect_ratio="1:1",
            resolution="Auto",
            magic_prompt_option="AUTO",
            seed=0,
            style_type="NONE",
            negative_prompt="",
            num_images=1,
            color_palette="",
            auth_token=None,
        ):
            aspect_ratio = V1_V2_RATIO_MAP.get(aspect_ratio, None)
            resolution = V1_V1_RES_MAP.get(resolution, None)
            # Determine the model based on turbo setting
            model = "V_2_TURBO" if turbo else "V_2"
    
            # Handle resolution vs aspect_ratio logic
            # If resolution is not AUTO, it overrides aspect_ratio
            final_resolution = None
            final_aspect_ratio = None
    
            if resolution != "AUTO":
                final_resolution = resolution
            else:
                final_aspect_ratio = aspect_ratio if aspect_ratio != "ASPECT_1_1" else None
    
            operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/ideogram/generate",
                    method=HttpMethod.POST,
                    request_model=IdeogramGenerateRequest,
                    response_model=IdeogramGenerateResponse,
                ),
                request=IdeogramGenerateRequest(
                    image_request=ImageRequest(
                        prompt=prompt,
                        model=model,
                        num_images=num_images,
                        seed=seed,
                        aspect_ratio=final_aspect_ratio,
                        resolution=final_resolution,
                        magic_prompt_option=(
                            magic_prompt_option if magic_prompt_option != "AUTO" else None
                        ),
                        style_type=style_type if style_type != "NONE" else None,
                        negative_prompt=negative_prompt if negative_prompt else None,
                        color_palette=color_palette if color_palette else None,
                    )
                ),
                auth_token=auth_token,
            )
    
            response = operation.execute()
    
            if not response.data or len(response.data) == 0:
                raise Exception("No images were generated in the response")
    
            image_urls = [image_data.url for image_data in response.data if image_data.url]
    
            if not image_urls:
                raise Exception("No image URLs were generated in the response")
    
            return (download_and_process_images(image_urls),)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/ideogram/ideogram-v2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/ideogram/ideogram-v2)

[Ideogram V1 - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v1)[Luma Image to Image - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-image-to-image)

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
