---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-image-to-video/
title: Kling Image to Video - ComfyUI Built-in Node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:38.217968+00:00
---

# Kling Image to Video - ComfyUI Built-in Node - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-image-to-video/

## On this page

Back to top

  * Parameters
    * Basic Parameters
    * Output
  * Source Code



Kling

# Kling Image to Video - ComfyUI Built-in Node

Copy pageCopy page

A node that converts static images to dynamic videos using Kling’s AI technology

Copy pageCopy page

![ComfyUI Built-in Kling Image to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d4c1f57cbb7824acee3d6c584252dbdd) The Kling Image to Video node converts static images into dynamic video content using Kling’s image-to-video API.

## Parameters

### Basic Parameters

All parameters below are required:

Parameter| Type| Default| Description  
---|---|---|---  
start_frame| Image| -| Input source image  
prompt| String| ""| Text prompt describing video action and content  
negative_prompt| String| ""| Elements to avoid in the video  
cfg_scale| Float| 7.0| Controls how closely to follow the prompt  
model_name| Select| ”kling-v1-5”| Model type to use  
aspect_ratio| Select| ”16:9”| Output video aspect ratio  
duration| Select| ”5s”| Generated video duration  
mode| Select| ”pro”| Video generation mode  
  
### Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
video_id| String| Unique video identifier  
duration| String| Actual video duration  
  
## Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class KlingImage2VideoNode(KlingNodeBase):
        """Kling Image to Video Node"""
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "start_frame": model_field_to_node_input(
                        IO.IMAGE, KlingImage2VideoRequest, "image"
                    ),
                    "prompt": model_field_to_node_input(
                        IO.STRING, KlingImage2VideoRequest, "prompt", multiline=True
                    ),
                    "negative_prompt": model_field_to_node_input(
                        IO.STRING,
                        KlingImage2VideoRequest,
                        "negative_prompt",
                        multiline=True,
                    ),
                    "model_name": model_field_to_node_input(
                        IO.COMBO,
                        KlingImage2VideoRequest,
                        "model_name",
                        enum_type=KlingVideoGenModelName,
                    ),
                    "cfg_scale": model_field_to_node_input(
                        IO.FLOAT, KlingImage2VideoRequest, "cfg_scale"
                    ),
                    "mode": model_field_to_node_input(
                        IO.COMBO,
                        KlingImage2VideoRequest,
                        "mode",
                        enum_type=KlingVideoGenMode,
                    ),
                    "aspect_ratio": model_field_to_node_input(
                        IO.COMBO,
                        KlingImage2VideoRequest,
                        "aspect_ratio",
                        enum_type=KlingVideoGenAspectRatio,
                    ),
                    "duration": model_field_to_node_input(
                        IO.COMBO,
                        KlingImage2VideoRequest,
                        "duration",
                        enum_type=KlingVideoGenDuration,
                    ),
                },
                "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
            }
    
        RETURN_TYPES = ("VIDEO", "STRING", "STRING")
        RETURN_NAMES = ("VIDEO", "video_id", "duration")
        DESCRIPTION = "Kling Image to Video Node"
    
        def get_response(self, task_id: str, auth_token: str) -> KlingImage2VideoResponse:
            return poll_until_finished(
                auth_token,
                ApiEndpoint(
                    path=f"{PATH_IMAGE_TO_VIDEO}/{task_id}",
                    method=HttpMethod.GET,
                    request_model=KlingImage2VideoRequest,
                    response_model=KlingImage2VideoResponse,
                ),
            )
    
        def api_call(
            self,
            start_frame: torch.Tensor,
            prompt: str,
            negative_prompt: str,
            model_name: str,
            cfg_scale: float,
            mode: str,
            aspect_ratio: str,
            duration: str,
            camera_control: Optional[KlingCameraControl] = None,
            end_frame: Optional[torch.Tensor] = None,
            auth_token: Optional[str] = None,
        ) -> tuple[VideoFromFile]:
            validate_prompts(prompt, negative_prompt, MAX_PROMPT_LENGTH_I2V)
            initial_operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path=PATH_IMAGE_TO_VIDEO,
                    method=HttpMethod.POST,
                    request_model=KlingImage2VideoRequest,
                    response_model=KlingImage2VideoResponse,
                ),
                request=KlingImage2VideoRequest(
                    model_name=KlingVideoGenModelName(model_name),
                    image=tensor_to_base64_string(start_frame),
                    image_tail=(
                        tensor_to_base64_string(end_frame)
                        if end_frame is not None
                        else None
                    ),
                    prompt=prompt,
                    negative_prompt=negative_prompt if negative_prompt else None,
                    cfg_scale=cfg_scale,
                    mode=KlingVideoGenMode(mode),
                    aspect_ratio=KlingVideoGenAspectRatio(aspect_ratio),
                    duration=KlingVideoGenDuration(duration),
                    camera_control=camera_control,
                ),
                auth_token=auth_token,
            )
    
            task_creation_response = initial_operation.execute()
            validate_task_creation_response(task_creation_response)
            task_id = task_creation_response.data.task_id
    
            final_response = self.get_response(task_id, auth_token)
            validate_video_result_response(final_response)
    
            video = get_video_from_response(final_response)
            return video_result_to_node_output(video)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/kwai_vgi/kling-image-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/kwai_vgi/kling-image-to-video)

[Kling Camera Controls](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-controls)[Kling Start-End Frame to Video](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-start-end-frame-to-video)
