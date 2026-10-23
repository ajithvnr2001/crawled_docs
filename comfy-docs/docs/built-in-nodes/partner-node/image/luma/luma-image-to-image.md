---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-image-to-image/
title: Luma Image to Image - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:35.498104+00:00
---

# Luma Image to Image - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-image-to-image/

## On this page

  * Node Function
  * Parameters
    * Basic Parameters
    * Optional Parameters
    * Output
  * Usage Examples
  * How It Works
  * Source Code



Luma

# Luma Image to Image - ComfyUI Built-in Node Documentation

Copy pageCopy page

Node for modifying images using Luma AI

Copy pageCopy page

![ComfyUI Built-in Luma Image to Image Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c59f5ee7cefc230c298f9e3d8a24e507) The Luma Image to Image node allows you to modify existing images using Luma AI technology based on text prompts, while preserving certain features and structure of the original image.

## 

​

Node Function

This node connects to Luma AI’s text-to-image API, enabling users to generate images through detailed text prompts. Luma AI is known for its excellent realism and detail, particularly excelling at generating photorealistic content and artistic style images.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| string| ""| Text prompt describing the content to generate  
model| select| -| Select which generation model to use  
aspect_ratio| select| 16:9| Set the aspect ratio of the output image  
seed| integer| 0| Seed value to determine if node should rerun, but actual results don’t depend on seed  
style_image_weight| float| 1.0| Weight of the style image, range 0.02-1.0, only effective when style_image is provided  
  
### 

​

Optional Parameters

Without the following parameter inputs, the node functions in text-to-image mode

Parameter| Type| Description  
---|---|---  
image_luma_ref| LUMA_REF| Luma reference node connection, influences generation results through input images, can consider up to 4 images  
style_image| image| Style reference image, uses only 1 image, influences the style of generated images, adjusted through `style_image_weight`  
character_image| image| Adds character features to the generated results, can be a batch of multiple images, up to 4 images  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| image| The generated image  
  
## 

​

Usage Examples

## 

​

How It Works

The Luma Image to Image node analyzes the input image and combines it with text prompts to guide the modification process. It uses Luma AI’s generation models to make creative changes to images based on prompts. Node process:

  1. First uploads the input image to ComfyAPI
  2. Then sends the image URL with the prompt to Luma API
  3. Waits for Luma AI to complete processing
  4. Downloads and returns the generated image

The image_weight parameter controls the degree of influence from the original image - values closer to 0 will preserve more of the original image features, while values closer to 1 allow for more substantial modifications.

## 

​

Source Code

[Node Source Code (Updated on 2025-05-05)]
    
    
    class LumaImageModifyNode(ComfyNodeABC):
        """
        Modifies images synchronously based on prompt and aspect ratio.
        """
    
        RETURN_TYPES = (IO.IMAGE,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/image/Luma"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "image": (IO.IMAGE,),
                    "prompt": (
                        IO.STRING,
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Prompt for the image generation",
                        },
                    ),
                    "image_weight": (
                        IO.FLOAT,
                        {
                            "default": 1.0,
                            "min": 0.02,
                            "max": 1.0,
                            "step": 0.01,
                            "tooltip": "Weight of the image; the closer to 0.0, the less the image will be modified.",
                        },
                    ),
                    "model": ([model.value for model in LumaImageModel],),
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
                "optional": {},
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        def api_call(
            self,
            prompt: str,
            model: str,
            image: torch.Tensor,
            image_weight: float,
            seed,
            auth_token=None,
            **kwargs,
        ):
            # first, upload image
            download_urls = upload_images_to_comfyapi(
                image, max_images=1, auth_token=auth_token
            )
            image_url = download_urls[0]
            # next, make Luma call with download url provided
            operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/luma/generations/image",
                    method=HttpMethod.POST,
                    request_model=LumaImageGenerationRequest,
                    response_model=LumaGeneration,
                ),
                request=LumaImageGenerationRequest(
                    prompt=prompt,
                    model=model,
                    modify_image_ref=LumaModifyImageRef(
                        url=image_url, weight=round(image_weight, 2)
                    ),
                ),
                auth_token=auth_token,
            )
            response_api: LumaGeneration = operation.execute()
    
            operation = PollingOperation(
                poll_endpoint=ApiEndpoint(
                    path=f"/proxy/luma/generations/{response_api.id}",
                    method=HttpMethod.GET,
                    request_model=EmptyRequest,
                    response_model=LumaGeneration,
                ),
                completed_statuses=[LumaState.completed],
                failed_statuses=[LumaState.failed],
                status_extractor=lambda x: x.state,
                auth_token=auth_token,
            )
            response_poll = operation.execute()
    
            img_response = requests.get(response_poll.assets.image)
            img = process_image_response(img_response)
            return (img,)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/luma/luma-image-to-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/luma/luma-image-to-image)

[Ideogram V2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v2)[Luma Reference - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-reference)

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
