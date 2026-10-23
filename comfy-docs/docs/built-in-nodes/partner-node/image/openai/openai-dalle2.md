---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-dalle2/
title: OpenAI DALL\u00b7E 2 - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:28.246142+00:00
---

# OpenAI DALL·E 2 - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-dalle2/

## On this page

  * Parameters
    * Basic Parameters
    * Optional Parameters
    * Output
  * Features
  * Source Code



OpenAI

# OpenAI DALL·E 2 - ComfyUI Native Node Documentation

Copy pageCopy page

Node for generating images using OpenAI’s DALL·E 2 model

Copy pageCopy page

![ComfyUI Native Stability AI Stable Image Ultra Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=2a1ad9dab55bb9b02c4551dbf05078ff) The OpenAI DALL·E 2 node allows you to use OpenAI’s DALL·E 2 API to generate creative images from text descriptions.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| string| ""| Text prompt for DALL·E to generate images, supports multi-line input  
seed| integer| 0| The result is not actually related to the seed, this parameter only determines whether to re-execute  
size| select| ”1024x1024”| Output image size, options: 256x256, 512x512, 1024x1024  
n| integer| 1| Number of images to generate, range 1-8  
  
### 

​

Optional Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| None| Optional reference image for image editing  
mask| mask| None| Optional mask for inpainting (white areas will be replaced)  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| image| Generated image(s)  
  
## 

​

Features

  * Basic function: Generate images from text prompts
  * Image editing: When both image and mask parameters are provided, performs image editing (white masked areas will be replaced)



## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class OpenAIDalle2(ComfyNodeABC):
        """
        Generates images synchronously via OpenAI's DALL·E 2 endpoint.
    
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
                    "size": (
                        IO.COMBO,
                        {
                            "options": ["256x256", "512x512", "1024x1024"],
                            "default": "1024x1024",
                            "tooltip": "Image size",
                        },
                    ),
                    "n": (
                        IO.INT,
                        {
                            "default": 1,
                            "min": 1,
                            "max": 8,
                            "step": 1,
                            "display": "number",
                            "tooltip": "How many images to generate",
                        },
                    ),
                    "image": (
                        IO.IMAGE,
                        {
                            "default": None,
                            "tooltip": "Optional reference image for image editing.",
                        },
                    ),
                    "mask": (
                        IO.MASK,
                        {
                            "default": None,
                            "tooltip": "Optional mask for inpainting (white areas will be replaced)",
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
            image=None,
            mask=None,
            n=1,
            size="1024x1024",
            auth_token=None,
        ):
            model = "dall-e-2"
            path = "/proxy/openai/images/generations"
            content_type = "application/json"
            request_class = OpenAIImageGenerationRequest
            img_binary = None
    
            if image is not None and mask is not None:
                path = "/proxy/openai/images/edits"
                content_type = "multipart/form-data"
                request_class = OpenAIImageEditRequest
    
                input_tensor = image.squeeze().cpu()
                height, width, channels = input_tensor.shape
                rgba_tensor = torch.ones(height, width, 4, device="cpu")
                rgba_tensor[:, :, :channels] = input_tensor
    
                if mask.shape[1:] != image.shape[1:-1]:
                    raise Exception("Mask and Image must be the same size")
                rgba_tensor[:, :, 3] = 1 - mask.squeeze().cpu()
    
                rgba_tensor = downscale_image_tensor(rgba_tensor.unsqueeze(0)).squeeze()
    
                image_np = (rgba_tensor.numpy() * 255).astype(np.uint8)
                img = Image.fromarray(image_np)
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format="PNG")
                img_byte_arr.seek(0)
                img_binary = img_byte_arr  # .getvalue()
                img_binary.name = "image.png"
            elif image is not None or mask is not None:
                raise Exception("Dall-E 2 image editing requires an image AND a mask")
    
            # Build the operation
            operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path=path,
                    method=HttpMethod.POST,
                    request_model=request_class,
                    response_model=OpenAIImageGenerationResponse,
                ),
                request=request_class(
                    model=model,
                    prompt=prompt,
                    n=n,
                    size=size,
                    seed=seed,
                ),
                files=(
                    {
                        "image": img_binary,
                    }
                    if img_binary
                    else None
                ),
                content_type=content_type,
                auth_token=auth_token,
            )
    
            response = operation.execute()
    
            img_tensor = validate_and_cast_response(response)
            return (img_tensor,)
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/openai/openai-dalle2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/openai/openai-dalle2)

[Luma Text to Image - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-text-to-image)[OpenAI DALL·E 3 - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-dalle3)

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
