---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-text-to-video/
title: MiniMax Text to Video - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:31.986739+00:00
---

# MiniMax Text to Video - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-text-to-video/

## On this page

  * Parameters
    * Required Parameters
    * Output
  * Source Code



MiniMax

# MiniMax Text to Video - ComfyUI Native Node Documentation

Copy pageCopy page

A node that converts text descriptions into videos using MiniMax AI

Copy pageCopy page

![ComfyUI Native MiniMax Text to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-text-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c141952741306e4733795f063cfe4f66) The MiniMax Text to Video node connects to MiniMax’s API to generate high-quality, smooth videos from text prompts. It supports different video generation models to create short video clips in various styles.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt_text| String| ""| Text prompt that guides the video generation  
model| Select| ”T2V-01”| Video model to use, options are “T2V-01” and “T2V-01-Director”  
seed| Integer| 0| Random seed for noise generation, defaults to 0  
  
### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
  
## 

​

Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class MinimaxTextToVideoNode:
        """
        Generates videos synchronously based on a prompt, and optional parameters using Minimax's API.
        """
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "prompt_text": (
                        "STRING",
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Text prompt to guide the video generation",
                        },
                    ),
                    "model": (
                        [
                            "T2V-01",
                            "T2V-01-Director",
                        ],
                        {
                            "default": "T2V-01",
                            "tooltip": "Model to use for video generation",
                        },
                    ),
                },
                "optional": {
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
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        RETURN_TYPES = ("VIDEO",)
        DESCRIPTION = "Generates videos from prompts using Minimax's API"
        FUNCTION = "generate_video"
        CATEGORY = "api node/video/Minimax"
        API_NODE = True
        OUTPUT_NODE = True
    
        def generate_video(
            self,
            prompt_text,
            seed=0,
            model="T2V-01",
            image: torch.Tensor=None, # used for ImageToVideo
            subject: torch.Tensor=None, # used for SubjectToVideo
            auth_token=None,
        ):
            '''
            Function used between Minimax nodes - supports T2V, I2V, and S2V, based on provided arguments.
            '''
            # upload image, if passed in
            image_url = None
            if image is not None:
                image_url = upload_images_to_comfyapi(image, max_images=1, auth_token=auth_token)[0]
    
            # TODO: figure out how to deal with subject properly, API returns invalid params when using S2V-01 model
            subject_reference = None
            if subject is not None:
                subject_url = upload_images_to_comfyapi(subject, max_images=1, auth_token=auth_token)[0]
                subject_reference = [SubjectReferenceItem(image=subject_url)]
    
    
            video_generate_operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/minimax/video_generation",
                    method=HttpMethod.POST,
                    request_model=MinimaxVideoGenerationRequest,
                    response_model=MinimaxVideoGenerationResponse,
                ),
                request=MinimaxVideoGenerationRequest(
                    model=Model(model),
                    prompt=prompt_text,
                    callback_url=None,
                    first_frame_image=image_url,
                    subject_reference=subject_reference,
                    prompt_optimizer=None,
                ),
                auth_token=auth_token,
            )
            response = video_generate_operation.execute()
    
            task_id = response.task_id
            if not task_id:
                raise Exception(f"Minimax generation failed: {response.base_resp}")
    
            video_generate_operation = PollingOperation(
                poll_endpoint=ApiEndpoint(
                    path="/proxy/minimax/query/video_generation",
                    method=HttpMethod.GET,
                    request_model=EmptyRequest,
                    response_model=MinimaxTaskResultResponse,
                    query_params={"task_id": task_id},
                ),
                completed_statuses=["Success"],
                failed_statuses=["Fail"],
                status_extractor=lambda x: x.status.value,
                auth_token=auth_token,
            )
            task_result = video_generate_operation.execute()
    
            file_id = task_result.file_id
            if file_id is None:
                raise Exception("Request was not successful. Missing file ID.")
            file_retrieve_operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/minimax/files/retrieve",
                    method=HttpMethod.GET,
                    request_model=EmptyRequest,
                    response_model=MinimaxFileRetrieveResponse,
                    query_params={"file_id": int(file_id)},
                ),
                request=EmptyRequest(),
                auth_token=auth_token,
            )
            file_result = file_retrieve_operation.execute()
    
            file_url = file_result.file.download_url
            if file_url is None:
                raise Exception(
                    f"No video was found in the response. Full response: {file_result.model_dump()}"
                )
            logging.info(f"Generated video URL: {file_url}")
    
            video_io = download_url_to_bytesio(file_url)
            if video_io is None:
                error_msg = f"Failed to download video from {file_url}"
                logging.error(error_msg)
                raise Exception(error_msg)
            return (VideoFromFile(video_io),)
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/minimax/minimax-text-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/minimax/minimax-text-to-video)

[MiniMax Image to Video - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-image-to-video)[Pika 2.2 Image to Video - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/pika/pika-image-to-video)

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
