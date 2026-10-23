---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v1/
title: Ideogram V1 - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:27.900459+00:00
---

# Ideogram V1 - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v1/

## On this page

  * Parameter Description
    * Required Parameters
    * Output
  * Source Code



Ideogram

# Ideogram V1 - ComfyUI Native Node Documentation

Copy pageCopy page

Node for creating precise text rendering images using Ideogram API

Copy pageCopy page

![ComfyUI Native Ideogram V1 Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=10b0ea0f9a0ddb9c1184540f977e2cef) The Ideogram V1 node allows you to generate images with high-quality text rendering capabilities using Ideogram’s text-to-image API.

## 

​

Parameter Description

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| string| ""| Text prompt describing the content to generate  
turbo| boolean| False| Whether to use turbo mode (faster but possibly lower quality)  
aspect_ratio| select| ”1:1”| Image aspect ratio  
magic_prompt_option| select| ”AUTO”| Determines whether to use MagicPrompt in generation, options: AUTO, ON, OFF  
seed| integer| 0| Random seed value (0-2147483647)  
negative_prompt| string| ""| Specifies elements you don’t want in the image  
num_images| integer| 1| Number of images to generate (1-8)  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| image| Generated image result  
  
## 

​

Source Code

[Node Source Code (Updated on 2025-05-03)]
    
    
    class IdeogramV1(ComfyNodeABC):
        """
        Generates images synchronously using the Ideogram V1 model.
    
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
                            "tooltip": "The aspect ratio for image generation.",
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
                },
                "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
            }
    
        RETURN_TYPES = (IO.IMAGE,)
        FUNCTION = "api_call"
        CATEGORY = "api node/image/ideogram/v1"
        DESCRIPTION = cleandoc(__doc__ or "")
        API_NODE = True
    
        def api_call(
            self,
            prompt,
            turbo=False,
            aspect_ratio="1:1",
            magic_prompt_option="AUTO",
            seed=0,
            negative_prompt="",
            num_images=1,
            auth_token=None,
        ):
            # Determine the model based on turbo setting
            aspect_ratio = V1_V2_RATIO_MAP.get(aspect_ratio, None)
            model = "V_1_TURBO" if turbo else "V_1"
    
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
                        aspect_ratio=aspect_ratio if aspect_ratio != "ASPECT_1_1" else None,
                        magic_prompt_option=(
                            magic_prompt_option if magic_prompt_option != "AUTO" else None
                        ),
                        negative_prompt=negative_prompt if negative_prompt else None,
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/ideogram/ideogram-v1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/ideogram/ideogram-v1)

[ByteDanceImageEditNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceImageEditNode)[Ideogram V2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v2)

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
