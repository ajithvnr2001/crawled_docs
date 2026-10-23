---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/bfl/flux-1-1-pro-ultra-image/
title: Flux 1.1 [pro] Ultra Image - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:27.493743+00:00
---

# Flux 1.1 [pro] Ultra Image - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/bfl/flux-1-1-pro-ultra-image/

## On this page

  * Parameter Description
    * Basic Parameters
    * Optional Parameters
    * Output
  * Usage Examples
  * How It Works
  * Source Code



BFL

# Flux 1.1 [pro] Ultra Image - ComfyUI Native Node Documentation

Copy pageCopy page

Create images using Black Forest Labs’ high-resolution image generation API

Copy pageCopy page

![ComfyUI Native Flux 1.1 \[pro\] Ultra Image node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=51f4ad7b93c0df61bcc855eac5324802) The Flux 1.1 [pro] Ultra Image node allows you to generate ultra-high-resolution images through text prompts, directly connecting to Black Forest Labs’ latest image generation API. This node supports two main usage modes:

  1. **Text-to-Image** : Generate high-quality images from text prompts (when no image input is used)
  2. **Image-to-Image** : Combine existing images with prompts to create new images that blend features from both (Remix mode)

This node supports Ultra mode through API calls, capable of generating images at 4 times the resolution of standard Flux 1.1 [pro] (up to 4MP), without sacrificing prompt adherence, and maintaining super-fast generation times of just 10 seconds. Compared to other high-resolution models, it’s more than 2.5 times faster.

## 

​

Parameter Description

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| String| ""| Text description for generating the image  
prompt_upsampling| Boolean| False| Whether to use prompt upsampling technique to enhance details. When enabled, automatically modifies prompts for more creative generation, but results become non-deterministic (same seed won’t produce exactly the same result)  
seed| Integer| 0| Random seed value, controls generation randomness  
aspect_ratio| String| ”16:9”| Width-to-height ratio of the image, must be between 1:4 and 4:1  
raw| Boolean| False| When set to True, generates less processed, more natural-looking images  
  
### 

​

Optional Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image_prompt| Image| None| Optional input, used for Image-to-Image (Remix) mode  
image_prompt_strength| Float| 0.1| Active when `image_prompt` is input, adjusts the blend between prompt and image prompt. Higher values make output closer to input image, range is 0.0-1.0  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| Image| Generated high-resolution image result  
  
## 

​

Usage Examples

Please visit the tutorial below to see corresponding usage examples

  * [Flux 1.1 Pro Ultra Image Partner Nodes ComfyUI Official Example Workflow](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)



## 

​

How It Works

Flux 1.1 [pro] Ultra mode uses optimized deep learning architecture and efficient GPU acceleration technology to achieve high-resolution image generation without sacrificing speed. When a request is sent to the API, the system parses the prompt, applies appropriate parameters, then computes the image in parallel, finally generating and returning the high-resolution result. Compared to regular models, Ultra mode particularly focuses on detail preservation and consistency at large scales, ensuring impressive quality even at 4MP high resolution.

## 

​

Source Code

[Node Source Code (Updated on 2025-05-03)]
    
    
    class FluxProUltraImageNode(ComfyNodeABC):
        """
        Generates images synchronously based on prompt and resolution.
        """
    
        MINIMUM_RATIO = 1 / 4
        MAXIMUM_RATIO = 4 / 1
        MINIMUM_RATIO_STR = "1:4"
        MAXIMUM_RATIO_STR = "4:1"
    
        @classmethod
        def INPUT_TYPES(s):
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
                    "prompt_upsampling": (
                        IO.BOOLEAN,
                        {
                            "default": False,
                            "tooltip": "Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation, but results are nondeterministic (same seed will not produce exactly the same result).",
                        },
                    ),
                    "seed": (
                        IO.INT,
                        {
                            "default": 0,
                            "min": 0,
                            "max": 0xFFFFFFFFFFFFFFFF,
                            "control_after_generate": True,
                            "tooltip": "The random seed used for creating the noise.",
                        },
                    ),
                    "aspect_ratio": (
                        IO.STRING,
                        {
                            "default": "16:9",
                            "tooltip": "Aspect ratio of image; must be between 1:4 and 4:1.",
                        },
                    ),
                    "raw": (
                        IO.BOOLEAN,
                        {
                            "default": False,
                            "tooltip": "When True, generate less processed, more natural-looking images.",
                        },
                    ),
                },
                "optional": {
                    "image_prompt": (IO.IMAGE,),
                    "image_prompt_strength": (
                        IO.FLOAT,
                        {
                            "default": 0.1,
                            "min": 0.0,
                            "max": 1.0,
                            "step": 0.01,
                            "tooltip": "Blend between the prompt and the image prompt.",
                        },
                    ),
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        @classmethod
        def VALIDATE_INPUTS(cls, aspect_ratio: str):
            try:
                validate_aspect_ratio(
                    aspect_ratio,
                    minimum_ratio=cls.MINIMUM_RATIO,
                    maximum_ratio=cls.MAXIMUM_RATIO,
                    minimum_ratio_str=cls.MINIMUM_RATIO_STR,
                    maximum_ratio_str=cls.MAXIMUM_RATIO_STR,
                )
            except Exception as e:
                return str(e)
            return True
    
        RETURN_TYPES = (IO.IMAGE,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/image/bfl"
    
        def api_call(
            self,
            prompt: str,
            aspect_ratio: str,
            prompt_upsampling=False,
            raw=False,
            seed=0,
            image_prompt=None,
            image_prompt_strength=0.1,
            auth_token=None,
            **kwargs,
        ):
            operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/bfl/flux-pro-1.1-ultra/generate",
                    method=HttpMethod.POST,
                    request_model=BFLFluxProUltraGenerateRequest,
                    response_model=BFLFluxProGenerateResponse,
                ),
                request=BFLFluxProUltraGenerateRequest(
                    prompt=prompt,
                    prompt_upsampling=prompt_upsampling,
                    seed=seed,
                    aspect_ratio=validate_aspect_ratio(
                        aspect_ratio,
                        minimum_ratio=self.MINIMUM_RATIO,
                        maximum_ratio=self.MAXIMUM_RATIO,
                        minimum_ratio_str=self.MINIMUM_RATIO_STR,
                        maximum_ratio_str=self.MAXIMUM_RATIO_STR,
                    ),
                    raw=raw,
                    image_prompt=(
                        image_prompt
                        if image_prompt is None
                        else convert_image_to_base64(image_prompt)
                    ),
                    image_prompt_strength=(
                        None if image_prompt is None else round(image_prompt_strength, 2)
                    ),
                ),
                auth_token=auth_token,
            )
            output_image = handle_bfl_synchronous_operation(operation)
            return (output_image,)
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/bfl/flux-1-1-pro-ultra-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/bfl/flux-1-1-pro-ultra-image)

[FluxProImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxProImageNode)[ByteDanceImageEditNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceImageEditNode)

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
