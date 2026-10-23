---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-text-to-image/
title: Luma Text to Image - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:28.074714+00:00
---

# Luma Text to Image - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-text-to-image/

## On this page

  * Node Function
  * Parameters
    * Basic Parameters
    * Optional Parameters
    * Output
  * Usage Example
  * How It Works
  * Source Code



Luma

# Luma Text to Image - ComfyUI Native Node Documentation

Copy pageCopy page

A node that converts text descriptions into high-quality images using Luma AI

Copy pageCopy page

![ComfyUI Native Luma Text to Image Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=19025e6d9d71bde0458f444404afe2b6) The Luma Text to Image node allows you to create highly realistic and artistic images from text descriptions using Luma AI’s advanced image generation capabilities.

## 

​

Node Function

This node connects to Luma AI’s text-to-image API, enabling users to generate images through detailed text prompts. Luma AI is known for its excellent realism and detail representation, particularly excelling at producing photorealistic content and artistic style images.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| String| ""| Text prompt describing the content to generate  
model| Select| -| Choose which generation model to use  
aspect_ratio| Select| 16:9| Set the output image’s aspect ratio  
seed| Integer| 0| Seed value to determine if the node should re-run, but actual results are independent of the seed  
style_image_weight| Float| 1.0| Style image weight, range 0.0-1.0, only applies when style_image is provided, higher means stronger style reference  
  
### 

​

Optional Parameters

Parameter| Type| Description  
---|---|---  
image_luma_ref| LUMA_REF| Luma reference node connection to influence generation with input images; up to 4 images  
style_image| Image| Style reference image; only 1 image will be used  
character_image| Image| Character reference images; can be a batch of multiple, up to 4 images  
  
### 

​

Output

Output| Type| Description  
---|---|---  
IMAGE| Image| Generated image result  
  
## 

​

Usage Example

## Luma Text to Image Usage Example

Detailed guide for Luma Text to Image workflow

## 

​

How It Works

The Luma Text to Image node analyzes the text prompt provided by the user and creates corresponding images through Luma AI’s generation models. This process uses deep learning technology to understand text descriptions and convert them into visual representations. Users can fine-tune the generation process by adjusting various parameters, including resolution, guidance scale, and negative prompts. Additionally, the node supports using reference images and concept guidance to further influence the generation results, allowing creators to more precisely achieve their creative vision.

## 

​

Source Code

[Node Source Code (Updated on 2025-05-03)]
    
    
    class LumaImageGenerationNode(ComfyNodeABC):
        """
        Generates images synchronously based on prompt and aspect ratio.
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
                    "prompt": (
                        IO.STRING,
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Prompt for the image generation",
                        },
                    ),
                    "model": ([model.value for model in LumaImageModel],),
                    "aspect_ratio": (
                        [ratio.value for ratio in LumaAspectRatio],
                        {
                            "default": LumaAspectRatio.ratio_16_9,
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
                    "style_image_weight": (
                        IO.FLOAT,
                        {
                            "default": 1.0,
                            "min": 0.0,
                            "max": 1.0,
                            "step": 0.01,
                            "tooltip": "Weight of style image. Ignored if no style_image provided.",
                        },
                    ),
                },
                "optional": {
                    "image_luma_ref": (
                        LumaIO.LUMA_REF,
                        {
                            "tooltip": "Luma Reference node connection to influence generation with input images; up to 4 images can be considered."
                        },
                    ),
                    "style_image": (
                        IO.IMAGE,
                        {"tooltip": "Style reference image; only 1 image will be used."},
                    ),
                    "character_image": (
                        IO.IMAGE,
                        {
                            "tooltip": "Character reference images; can be a batch of multiple, up to 4 images can be considered."
                        },
                    ),
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        def api_call(
            self,
            prompt: str,
            model: str,
            aspect_ratio: str,
            seed,
            style_image_weight: float,
            image_luma_ref: LumaReferenceChain = None,
            style_image: torch.Tensor = None,
            character_image: torch.Tensor = None,
            auth_token=None,
            **kwargs,
        ):
            # handle image_luma_ref
            api_image_ref = None
            if image_luma_ref is not None:
                api_image_ref = self._convert_luma_refs(
                    image_luma_ref, max_refs=4, auth_token=auth_token
                )
            # handle style_luma_ref
            api_style_ref = None
            if style_image is not None:
                api_style_ref = self._convert_style_image(
                    style_image, weight=style_image_weight, auth_token=auth_token
                )
            # handle character_ref images
            character_ref = None
            if character_image is not None:
                download_urls = upload_images_to_comfyapi(
                    character_image, max_images=4, auth_token=auth_token
                )
                character_ref = LumaCharacterRef(
                    identity0=LumaImageIdentity(images=download_urls)
                )
    
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
                    aspect_ratio=aspect_ratio,
                    image_ref=api_image_ref,
                    style_ref=api_style_ref,
                    character_ref=character_ref,
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
    
        def _convert_luma_refs(
            self, luma_ref: LumaReferenceChain, max_refs: int, auth_token=None
        ):
            luma_urls = []
            ref_count = 0
            for ref in luma_ref.refs:
                download_urls = upload_images_to_comfyapi(
                    ref.image, max_images=1, auth_token=auth_token
                )
                luma_urls.append(download_urls[0])
                ref_count += 1
                if ref_count >= max_refs:
                    break
            return luma_ref.create_api_model(download_urls=luma_urls, max_refs=max_refs)
    
        def _convert_style_image(
            self, style_image: torch.Tensor, weight: float, auth_token=None
        ):
            chain = LumaReferenceChain(
                first_ref=LumaReference(image=style_image, weight=weight)
            )
            return self._convert_luma_refs(chain, max_refs=1, auth_token=auth_token)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/luma/luma-text-to-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/luma/luma-text-to-image)

[Luma Reference - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/luma/luma-reference)[OpenAI DALL·E 2 - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/openai/openai-dalle2)

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
