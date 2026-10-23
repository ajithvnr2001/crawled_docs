---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-text-to-video/
title: PixVerse Text to Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:32.478275+00:00
---

# PixVerse Text to Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-text-to-video/

## On this page

  * Parameters
    * Required Parameters
    * Optional Parameters
    * Limitations
    * Output
  * Source Code



PixVerse

# PixVerse Text to Video - ComfyUI Built-in Node Documentation

Copy pageCopy page

A node that converts text descriptions into videos using PixVerse AI technology

Copy pageCopy page

![ComfyUI Built-in PixVerse Text to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b565631bd9ca69e804d839e8d79a799c) The PixVerse Text to Video node connects to PixVerse’s text-to-video API, allowing users to generate high-quality videos from text descriptions. Users can customize their creations by adjusting various parameters like video quality, duration, and motion mode.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| string| ""| Text prompt describing the video content  
aspect_ratio| select| -| Output video aspect ratio  
quality| select| PixverseQuality.res_540p| Video quality level  
duration_seconds| select| -| Video duration  
motion_mode| select| -| Video motion mode  
seed| integer| 0| Random seed for consistent generation results  
  
### 

​

Optional Parameters

Parameter| Type| Default| Description  
---|---|---|---  
negative_prompt| string| ""| Elements to exclude from the video  
pixverse_template| PIXVERSE_TEMPLATE| None| Optional template for style settings  
  
### 

​

Limitations

  * 1080p quality only supports normal motion mode with 5-second duration
  * Non 5-second durations only support normal motion mode



### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| video| Generated video  
  
## 

​

Source Code

[Node Source Code (Updated 2025-05-05)]
    
    
    class PixverseTextToVideoNode(ComfyNodeABC):
        """
        Generates videos synchronously based on prompt and output_size.
        """
    
        RETURN_TYPES = (IO.VIDEO,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/video/Pixverse"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "prompt": (
                        IO.STRING,
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Prompt for the video generation",
                        },
                    ),
                    "aspect_ratio": (
                        [ratio.value for ratio in PixverseAspectRatio],
                    ),
                    "quality": (
                        [resolution.value for resolution in PixverseQuality],
                        {
                            "default": PixverseQuality.res_540p,
                        },
                    ),
                    "duration_seconds": ([dur.value for dur in PixverseDuration],),
                    "motion_mode": ([mode.value for mode in PixverseMotionMode],),
                    "seed": (
                        IO.INT,
                        {
                            "default": 0,
                            "min": 0,
                            "max": 2147483647,
                            "control_after_generate": True,
                            "tooltip": "Seed for video generation.",
                        },
                    ),
                },
                "optional": {
                    "negative_prompt": (
                        IO.STRING,
                        {
                            "default": "",
                            "forceInput": True,
                            "tooltip": "An optional text description of undesired elements on an image.",
                        },
                    ),
                    "pixverse_template": (
                        PixverseIO.TEMPLATE,
                        {
                            "tooltip": "An optional template to influence style of generation, created by the Pixverse Template node."
                        }
                    )
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        def api_call(
            self,
            prompt: str,
            aspect_ratio: str,
            quality: str,
            duration_seconds: int,
            motion_mode: str,
            seed,
            negative_prompt: str=None,
            pixverse_template: int=None,
            auth_token=None,
            **kwargs,
        ):
            # 1080p is limited to 5 seconds duration
            # only normal motion_mode supported for 1080p or for non-5 second duration
            if quality == PixverseQuality.res_1080p:
                motion_mode = PixverseMotionMode.normal
                duration_seconds = PixverseDuration.dur_5
            elif duration_seconds != PixverseDuration.dur_5:
                motion_mode = PixverseMotionMode.normal
    
            operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/pixverse/video/text/generate",
                    method=HttpMethod.POST,
                    request_model=PixverseTextVideoRequest,
                    response_model=PixverseVideoResponse,
                ),
                request=PixverseTextVideoRequest(
                    prompt=prompt,
                    aspect_ratio=aspect_ratio,
                    quality=quality,
                    duration=duration_seconds,
                    motion_mode=motion_mode,
                    negative_prompt=negative_prompt if negative_prompt else None,
                    template_id=pixverse_template,
                    seed=seed,
                ),
                auth_token=auth_token,
            )
            response_api = operation.execute()
    
            if response_api.Resp is None:
                raise Exception(f"Pixverse request failed: '{response_api.ErrMsg}'")
    
            operation = PollingOperation(
                poll_endpoint=ApiEndpoint(
                    path=f"/proxy/pixverse/video/result/{response_api.Resp.video_id}",
                    method=HttpMethod.GET,
                    request_model=EmptyRequest,
                    response_model=PixverseGenerationStatusResponse,
                ),
                completed_statuses=[PixverseStatus.successful],
                failed_statuses=[PixverseStatus.contents_moderation, PixverseStatus.failed, PixverseStatus.deleted],
                status_extractor=lambda x: x.Resp.status,
                auth_token=auth_token,
            )
            response_poll = operation.execute()
    
            vid_response = requests.get(response_poll.Resp.url)
            return (VideoFromFile(BytesIO(vid_response.content)),)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/pixverse/pixverse-text-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/pixverse/pixverse-text-to-video)

[PixVerse Template - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-template)[PixVerse Transition Video - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-transition-video)

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
