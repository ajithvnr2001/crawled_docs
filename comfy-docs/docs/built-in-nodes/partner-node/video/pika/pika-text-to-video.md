---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-text-to-video/
title: Pika 2.2 Text to Video - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:32.250465+00:00
---

# Pika 2.2 Text to Video - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-text-to-video/

## On this page

  * Parameters
    * Required Parameters
    * Output
  * Source Code



Pika

# Pika 2.2 Text to Video - ComfyUI Native Node Documentation

Copy pageCopy page

A node that converts text descriptions into videos using Pika AI

Copy pageCopy page

![ComfyUI Native Pika 2.2 Text to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3eea0be5229f14d73d79d17a1b9872ea) The Pika 2.2 Text to Video node uses Pika’s 2.2 API to create videos from text descriptions. It connects to Pika’s text-to-video API, allowing users to generate videos using text prompts with various control parameters.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt_text| String| ""| Text prompt describing the video content  
negative_prompt| String| ""| Elements to exclude from the video  
seed| Integer| 0| Random seed for generation  
resolution| Select| ”1080p”| Output video resolution  
duration| Select| ”5s”| Length of generated video  
aspect_ratio| Float| 1.7777777777777777| Video aspect ratio, range 0.4-2.5, step 0.001  
  
### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
  
## 

​

Source Code

[Node Source Code (Updated 2025-05-05)]
    
    
    class PikaTextToVideoNodeV2_2(PikaNodeBase):
        """Pika 2.2 Text to Video Node."""
    
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": {
                    **cls.get_base_inputs_types(PikaBodyGenerate22T2vGenerate22T2vPost),
                    "aspect_ratio": model_field_to_node_input(
                        IO.FLOAT,
                        PikaBodyGenerate22T2vGenerate22T2vPost,
                        "aspectRatio",
                        step=0.001,
                        min=0.4,
                        max=2.5,
                        default=1.7777777777777777,
                    ),
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        RETURN_TYPES = ("VIDEO",)
        DESCRIPTION = "Sends a text prompt to the Pika API v2.2 to generate a video."
    
        def api_call(
            self,
            prompt_text: str,
            negative_prompt: str,
            seed: int,
            resolution: str,
            duration: int,
            aspect_ratio: float,
            auth_token: Optional[str] = None,
        ) -> tuple[VideoFromFile]:
            """API call for Pika 2.2 Text to Video."""
            initial_operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path=PATH_TEXT_TO_VIDEO,
                    method=HttpMethod.POST,
                    request_model=PikaBodyGenerate22T2vGenerate22T2vPost,
                    response_model=PikaGenerateResponse,
                ),
                request=PikaBodyGenerate22T2vGenerate22T2vPost(
                    promptText=prompt_text,
                    negativePrompt=negative_prompt,
                    seed=seed,
                    resolution=resolution,
                    duration=duration,
                    aspectRatio=aspect_ratio,
                ),
                auth_token=auth_token,
                content_type="application/x-www-form-urlencoded",
            )
    
            return self.execute_task(initial_operation, auth_token)
    
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/pika/pika-text-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/pika/pika-text-to-video)

[Pika 2.2 Scenes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-scenes)[Pikadditions - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Pikadditions)

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
