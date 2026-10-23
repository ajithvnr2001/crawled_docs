---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-scenes/
title: Pika 2.2 Scenes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:34.500925+00:00
---

# Pika 2.2 Scenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-scenes/

## On this page

  * Parameters
    * Required Parameters
    * Optional Parameters
    * Output
  * How It Works
  * Source Code



Pika

# Pika 2.2 Scenes - ComfyUI Built-in Node Documentation

Copy pageCopy page

A node that creates coherent scene videos from multiple images using Pika AI

Copy pageCopy page

![ComfyUI Built-in Pika 2.2 Scenes Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-scenes.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=84326ffddf831516f76705979410d289) The Pika 2.2 Scenes node allows you to upload multiple images and generate a high-quality video incorporating these elements. It uses Pika’s 2.2 API to create smooth scene transitions between the images.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt_text| string| ""| Text prompt describing video content and scenes  
negative_prompt| string| ""| Elements to exclude from the video  
seed| integer| 0| Random seed for generation  
ingredients_mode| select| ”creative”| Image combination mode  
resolution| select| API default| Output video resolution  
duration| select| API default| Output video length  
aspect_ratio| float| 1.7777777777777777 (16:9)| Video aspect ratio, range 0.4-2.5  
  
### 

​

Optional Parameters

Parameter| Type| Description  
---|---|---  
image_ingredient_1| image| First scene image  
image_ingredient_2| image| Second scene image  
image_ingredient_3| image| Third scene image  
image_ingredient_4| image| Fourth scene image  
image_ingredient_5| image| Fifth scene image  
  
### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| video| Generated video  
  
## 

​

How It Works

The Pika 2.2 Scenes node analyzes all input images and creates a video containing these image elements. The node sends the images and parameters to Pika’s API server, which processes them and returns the generated video. Users can guide the video style and content through prompts, and exclude unwanted elements using negative prompts. The node supports up to 5 input images as ingredients and generates the final video based on the specified combination mode, resolution, duration, and aspect ratio.

## 

​

Source Code
    
    
    class PikaScenesV2_2(PikaNodeBase):
        """Pika 2.2 Scenes Node."""
    
        @classmethod
        def INPUT_TYPES(cls):
            image_ingredient_input = (
                IO.IMAGE,
                {"tooltip": "Image that will be used as ingredient to create a video."},
            )
            return {
                "required": {
                    **cls.get_base_inputs_types(
                        PikaBodyGenerate22C2vGenerate22PikascenesPost,
                    ),
                    "ingredients_mode": model_field_to_node_input(
                        IO.COMBO,
                        PikaBodyGenerate22C2vGenerate22PikascenesPost,
                        "ingredientsMode",
                        enum_type=IngredientsMode,
                        default="creative",
                    ),
                    "aspect_ratio": model_field_to_node_input(
                        IO.FLOAT,
                        PikaBodyGenerate22C2vGenerate22PikascenesPost,
                        "aspectRatio",
                        step=0.001,
                        min=0.4,
                        max=2.5,
                        default=1.7777777777777777,
                    ),
                },
                "optional": {
                    "image_ingredient_1": image_ingredient_input,
                    "image_ingredient_2": image_ingredient_input,
                    "image_ingredient_3": image_ingredient_input,
                    "image_ingredient_4": image_ingredient_input,
                    "image_ingredient_5": image_ingredient_input,
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        DESCRIPTION = "Combine your images to create a video with the objects in them. Upload multiple images as ingredients and generate a high-quality video that incorporates all of them."
        RETURN_TYPES = ("VIDEO",)
    
        def api_call(
            self,
            prompt_text: str,
            negative_prompt: str,
            seed: int,
            resolution: str,
            duration: int,
            ingredients_mode: str,
            aspect_ratio: float,
            image_ingredient_1: Optional[torch.Tensor] = None,
            image_ingredient_2: Optional[torch.Tensor] = None,
            image_ingredient_3: Optional[torch.Tensor] = None,
            image_ingredient_4: Optional[torch.Tensor] = None,
            image_ingredient_5: Optional[torch.Tensor] = None,
            auth_token: Optional[str] = None,
        ) -> tuple[VideoFromFile]:
            """API call for Pika Scenes 2.2."""
            all_image_bytes_io = []
            for image in [
                image_ingredient_1,
                image_ingredient_2,
                image_ingredient_3,
                image_ingredient_4,
                image_ingredient_5,
            ]:
                if image is not None:
                    image_bytes_io = tensor_to_bytesio(image)
                    image_bytes_io.seek(0)
                    all_image_bytes_io.append(image_bytes_io)
    
            # Prepare files data for multipart upload
            pika_files = [
                ("images", (f"image_{i}.png", image_bytes_io, "image/png"))
                for i, image_bytes_io in enumerate(all_image_bytes_io)
            ]
    
            # Prepare non-file data using the Pydantic model
            pika_request_data = PikaBodyGenerate22C2vGenerate22PikascenesPost(
                ingredientsMode=ingredients_mode,
                promptText=prompt_text,
                negativePrompt=negative_prompt,
                seed=seed,
                resolution=resolution,
                duration=duration,
                aspectRatio=aspect_ratio,
            )
    
            initial_operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path=PATH_PIKASCENES,
                    method=HttpMethod.POST,
                    request_model=PikaBodyGenerate22C2vGenerate22PikascenesPost,
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/pika/pika-scenes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/pika/pika-scenes)

[Pika 2.2 Image to Video - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-image-to-video)[Pika 2.2 Text to Video - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-text-to-video)

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
