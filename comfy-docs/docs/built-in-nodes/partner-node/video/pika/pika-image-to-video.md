---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-image-to-video/
title: Pika 2.2 Image to Video - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:32.113347+00:00
---

# Pika 2.2 Image to Video - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-image-to-video/

## On this page

  * Parameters
    * Required Parameters
    * Output
  * How It Works
  * Source Code



Pika

# Pika 2.2 Image to Video - ComfyUI Native Node Documentation

Copy pageCopy page

A node that converts static images to dynamic videos using Pika AI

Copy pageCopy page

![ComfyUI Native Pika 2.2 Image to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4d84ed0f286826f853aeb820bf01c473) The Pika 2.2 Image to Video node connects to Pika’s latest 2.2 API to transform static images into dynamic videos. It preserves the visual features of the original image while adding natural motion based on text prompts.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| Image| -| Input image to convert to video  
prompt_text| String| ""| Text prompt describing video motion and content  
negative_prompt| String| ""| Elements to avoid in the video  
seed| Integer| 0| Random seed for generation  
resolution| Select| ”1080p”| Output video resolution  
duration| Select| ”5s”| Length of generated video  
  
### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
  
## 

​

How It Works

The node sends the input image and parameters (prompts, resolution, duration, etc.) to Pika’s API server as multipart form data. The API processes this and returns the generated video. Users can control the output by adjusting the prompts, negative prompts, random seed and other parameters.

## 

​

Source Code

[Node Source Code (Updated 2025-05-05)]
    
    
    class PikaImageToVideoV2_2(PikaNodeBase):
        """Pika 2.2 Image to Video Node."""
    
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": {
                    "image": (
                        IO.IMAGE,
                        {"tooltip": "The image to convert to video"},
                    ),
                    **cls.get_base_inputs_types(PikaBodyGenerate22I2vGenerate22I2vPost),
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        DESCRIPTION = "Sends an image and prompt to the Pika API v2.2 to generate a video."
        RETURN_TYPES = ("VIDEO",)
    
        def api_call(
            self,
            image: torch.Tensor,
            prompt_text: str,
            negative_prompt: str,
            seed: int,
            resolution: str,
            duration: int,
            auth_token: Optional[str] = None,
        ) -> tuple[VideoFromFile]:
            """API call for Pika 2.2 Image to Video."""
            # Convert image to BytesIO
            image_bytes_io = tensor_to_bytesio(image)
            image_bytes_io.seek(0)  # Reset stream position
    
            # Prepare file data for multipart upload
            pika_files = {"image": ("image.png", image_bytes_io, "image/png")}
    
            # Prepare non-file data using the Pydantic model
            pika_request_data = PikaBodyGenerate22I2vGenerate22I2vPost(
                promptText=prompt_text,
                negativePrompt=negative_prompt,
                seed=seed,
                resolution=resolution,
                duration=duration,
            )
    
            initial_operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path=PATH_IMAGE_TO_VIDEO,
                    method=HttpMethod.POST,
                    request_model=PikaBodyGenerate22I2vGenerate22I2vPost,
                    response_model=PikaGenerateResponse,
                ),
                request=pika_request_data,
                files=pika_files,
                content_type="multipart/form-data",
                auth_token=auth_token,
            )
    
            return self.execute_task(initial_operation, auth_token)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/pika/pika-image-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/pika/pika-image-to-video)

[MiniMax Text to Video - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-text-to-video)[Pika 2.2 Scenes - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-scenes)

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
