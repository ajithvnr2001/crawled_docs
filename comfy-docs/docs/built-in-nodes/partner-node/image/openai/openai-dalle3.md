---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-dalle3/
title: OpenAI DALL\u00b7E 3 - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:28.578827+00:00
---

# OpenAI DALL·E 3 - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-dalle3/

## On this page

  * Parameters
    * Input Parameters
    * Output Parameters
  * Source Code



OpenAI

# OpenAI DALL·E 3 - ComfyUI Native Node Documentation

Copy pageCopy page

Node for generating high-quality images using OpenAI’s DALL·E 3 model

Copy pageCopy page

![ComfyUI Native OpenAI DALL·E 3 Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1d4da35db8baddcd1321ef98365e26d0) This node connects to OpenAI’s DALL·E 3 API, allowing users to generate high-quality images through detailed text prompts. DALL·E 3 is OpenAI’s image generation model that offers significantly improved image quality, more accurate prompt understanding, and better detail rendering compared to previous versions.

## 

​

Parameters

### 

​

Input Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| string| ""| Detailed text prompt describing what to generate  
seed| integer| 0| Final result is not related to seed, this parameter only determines whether to re-execute  
quality| selection| ”standard”| Image quality, options: “standard” or “hd”  
style| selection| ”natural”| Visual style, options: “natural” or “vivid”. “Vivid” makes the model tend to create more surreal and dramatic images, while “natural” generates more realistic, less surreal images  
size| selection| ”1024x1024”| Output image size, options: “1024x1024”, “1024x1792”, or “1792x1024”  
  
### 

​

Output Parameters

Output| Type| Description  
---|---|---  
IMAGE| image| The generated image result  
  
## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class OpenAIDalle3(ComfyNodeABC):
        """
        Generates images synchronously via OpenAI's DALL·E 3 endpoint.
    
        Uses the proxy at /proxy/openai/images/generations. Returned URLs are short‑lived,
        so download or cache results if you need to keep them.
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
                            "tooltip": "Text prompt for DALL·E",
                        },
                    ),
                },
                "optional": {
                    "seed": (
                        IO.INT,
                        {
                            "default": 0,
                            "min": 0,
                            "max": 2**31 - 1,
                            "step": 1,
                            "display": "number",
                            "control_after_generate": True,
                            "tooltip": "not implemented yet in backend",
                        },
                    ),
                    "quality": (
                        IO.COMBO,
                        {
                            "options": ["standard", "hd"],
                            "default": "standard",
                            "tooltip": "Image quality",
                        },
                    ),
                    "style": (
                        IO.COMBO,
                        {
                            "options": ["natural", "vivid"],
                            "default": "natural",
                            "tooltip": "Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images.",
                        },
                    ),
                    "size": (
                        IO.COMBO,
                        {
                            "options": ["1024x1024", "1024x1792", "1792x1024"],
                            "default": "1024x1024",
                            "tooltip": "Image size",
                        },
                    ),
                },
                "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
            }
    
        RETURN_TYPES = (IO.IMAGE,)
        FUNCTION = "api_call"
        CATEGORY = "api node/image/openai"
        DESCRIPTION = cleandoc(__doc__ or "")
        API_NODE = True
    
        def api_call(
            self,
            prompt,
            seed=0,
            style="natural",
            quality="standard",
            size="1024x1024",
            auth_token=None,
        ):
            model = "dall-e-3"
    
            # build the operation
            operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/openai/images/generations",
                    method=HttpMethod.POST,
                    request_model=OpenAIImageGenerationRequest,
                    response_model=OpenAIImageGenerationResponse,
                ),
                request=OpenAIImageGenerationRequest(
                    model=model,
                    prompt=prompt,
                    quality=quality,
                    size=size,
                    style=style,
                    seed=seed,
                ),
                auth_token=auth_token,
            )
    
            response = operation.execute()
    
            img_tensor = validate_and_cast_response(response)
            return (img_tensor,)
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/openai/openai-dalle3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/openai/openai-dalle3)

[OpenAI DALL·E 2 - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-dalle2)[OpenAI GPT Image 1 - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-gpt-image1)

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
