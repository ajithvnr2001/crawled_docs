---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-text-to-video/
title: Kling Text to Video - ComfyUI Built-in Node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:31.493739+00:00
---

# Kling Text to Video - ComfyUI Built-in Node - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-text-to-video/

## On this page

  * Parameters
    * Required Parameters
    * Output
  * How It Works
  * Source Code



Kling

# Kling Text to Video - ComfyUI Built-in Node

Copy pageCopy page

A node that converts text descriptions into videos using Kling’s AI technology

Copy pageCopy page

![ComfyUI Built-in Kling Text to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-text-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7ddc3d180854e9a1e836154b3f36a58d) The Kling Text to Video node connects to Kling’s API service to generate videos from text descriptions. Users simply provide descriptive text to create corresponding video content.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| String| ""| Text prompt describing desired video content  
negative_prompt| String| ""| Elements to avoid in the video  
cfg_scale| Float| 7.0| Controls how closely to follow the prompt  
model_name| Select| ”kling-v2-master”| Video generation model to use  
aspect_ratio| Select| AspectRatio enum| Output video aspect ratio  
duration| Select| Duration enum| Length of generated video  
mode| Select| Mode enum| Video generation mode  
  
### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
Kling ID| String| Task identifier  
Duration (sec)| String| Video length in seconds  
  
## 

​

How It Works

The node sends text prompts to Kling’s API server, which processes and returns the generated video. The process includes initial request and status polling. When complete, the node downloads and outputs the video. Users can control the generation by adjusting parameters like negative prompts, configuration scale, and video properties. The system validates prompt length to ensure API compliance.

## 

​

Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class KlingTextToVideoNode(KlingNodeBase):
        """Kling Text to Video Node"""
    
        @staticmethod
        def poll_for_task_status(task_id: str, auth_token: str) -> KlingText2VideoResponse:
            """Polls the Kling API endpoint until the task reaches a terminal state."""
            polling_operation = PollingOperation(
                poll_endpoint=ApiEndpoint(
                    path=f"{PATH_TEXT_TO_VIDEO}/{task_id}",
                    method=HttpMethod.GET,
                    request_model=EmptyRequest,
                    response_model=KlingText2VideoResponse,
                ),
                completed_statuses=[
                    TaskStatus.succeed.value,
                ],
                failed_statuses=[TaskStatus.failed.value],
                status_extractor=lambda response: (
                    response.data.task_status.value
                    if response.data and response.data.task_status
                    else None
                ),
                auth_token=auth_token,
            )
            return polling_operation.execute()
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "prompt": model_field_to_node_input(
                        IO.STRING, KlingText2VideoRequest, "prompt", multiline=True
                    ),
                    "negative_prompt": model_field_to_node_input(
                        IO.STRING, KlingText2VideoRequest, "negative_prompt", multiline=True
                    ),
                    "model_name": model_field_to_node_input(
                        IO.COMBO,
                        KlingText2VideoRequest,
                        "model_name",
                        enum_type=ModelName,
                        default="kling-v2-master",
                    ),
                    "cfg_scale": model_field_to_node_input(
                        IO.FLOAT, KlingText2VideoRequest, "cfg_scale"
                    ),
                    "mode": model_field_to_node_input(
                        IO.COMBO, KlingText2VideoRequest, "mode", enum_type=Mode
                    ),
                    "duration": model_field_to_node_input(
                        IO.COMBO, KlingText2VideoRequest, "duration", enum_type=Duration
                    ),
                    "aspect_ratio": model_field_to_node_input(
                        IO.COMBO,
                        KlingText2VideoRequest,
                        "aspect_ratio",
                        enum_type=AspectRatio,
                    ),
                },
                "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
            }
    
        RETURN_TYPES = ("VIDEO", "STRING", "STRING")
        RETURN_NAMES = ("VIDEO", "Kling ID", "Duration (sec)")
        DESCRIPTION = "Kling Text to Video Node"
    
        def api_call(
            self,
            prompt: str,
            negative_prompt: str,
            model_name: str,
            cfg_scale: float,
            mode: str,
            duration: int,
            aspect_ratio: str,
            camera_control: Optional[CameraControl] = None,
            auth_token: Optional[str] = None,
        ) -> tuple[VideoFromFile, str, str]:
            validate_prompts(prompt, negative_prompt, MAX_PROMPT_LENGTH_T2V)
            initial_operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path=PATH_TEXT_TO_VIDEO,
                    method=HttpMethod.POST,
                    request_model=KlingText2VideoRequest,
                    response_model=KlingText2VideoResponse,
                ),
                request=KlingText2VideoRequest(
                    prompt=prompt if prompt else None,
                    negative_prompt=negative_prompt if negative_prompt else None,
                    duration=Duration(duration),
                    mode=Mode(mode),
                    model_name=ModelName(model_name),
                    cfg_scale=cfg_scale,
                    aspect_ratio=AspectRatio(aspect_ratio),
                    camera_control=camera_control,
                ),
                auth_token=auth_token,
            )
    
            initial_response = initial_operation.execute()
            if not is_valid_initial_response(initial_response):
                error_msg = f"Kling initial request failed. Code: {initial_response.code}, Message: {initial_response.message}, Data: {initial_response.data}"
                logging.error(error_msg)
                raise KlingApiError(error_msg)
    
            task_id = initial_response.data.task_id
            final_response = self.poll_for_task_status(task_id, auth_token)
            if not is_valid_video_response(final_response):
                error_msg = (
                    f"Kling task {task_id} succeeded but no video data found in response."
                )
                logging.error(error_msg)
                raise KlingApiError(error_msg)
    
            video = final_response.data.task_result.videos[0]
            logging.debug("Kling task %s succeeded. Video URL: %s", task_id, video.url)
            return (
                download_url_to_video_output(video.url),
                str(video.id),
                str(video.duration),
            )
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/kwai_vgi/kling-text-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/kwai_vgi/kling-text-to-video)

[Kling Start-End Frame to Video - ComfyUI Built-in NodePrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-start-end-frame-to-video)[MiniMax Image to Video - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-image-to-video)

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
