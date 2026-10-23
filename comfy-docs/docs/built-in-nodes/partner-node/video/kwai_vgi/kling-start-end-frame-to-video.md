---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-start-end-frame-to-video/
title: Kling Start-End Frame to Video - ComfyUI Built-in Node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:31.209293+00:00
---

# Kling Start-End Frame to Video - ComfyUI Built-in Node - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-start-end-frame-to-video/

## On this page

  * Parameters
    * Required Parameters
    * Mode Options
    * Output
  * How It Works
  * Source Code



Kling

# Kling Start-End Frame to Video - ComfyUI Built-in Node

Copy pageCopy page

A node that creates smooth video transitions between start and end frames using Kling’s AI technology

Copy pageCopy page

![ComfyUI Built-in Kling Start-End Frame to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-start-end-frame-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=211ba371516fd05518ad7e503ae9e283) The Kling Start-End Frame to Video node lets you create smooth video transitions between two images. It automatically generates all the intermediate frames to produce a fluid transformation.

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Description  
---|---|---  
start_frame| Image| Starting image for the video  
end_frame| Image| Ending image for the video  
prompt| String| Text describing video content and transition  
negative_prompt| String| Elements to avoid in the video  
cfg_scale| Float| Controls how closely to follow the prompt  
aspect_ratio| Select| Output video aspect ratio  
mode| Select| Video generation settings (mode/duration/model)  
  
### 

​

Mode Options

Available mode combinations:

  * standard mode / 5s duration / kling-v1
  * standard mode / 5s duration / kling-v1-5
  * pro mode / 5s duration / kling-v1
  * pro mode / 5s duration / kling-v1-5
  * pro mode / 5s duration / kling-v1-6
  * pro mode / 10s duration / kling-v1-5
  * pro mode / 10s duration / kling-v1-6

Default: “pro mode / 5s duration / kling-v1”

### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
  
## 

​

How It Works

The node analyzes the start and end frames to create a smooth transition sequence between them. It sends the images and parameters to Kling’s API server, which generates all necessary intermediate frames for a fluid transformation. The transition style and content can be guided using prompts, while negative prompts help avoid unwanted elements.

## 

​

Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    
    class KlingStartEndFrameNode(KlingImage2VideoNode):
        """
        Kling First Last Frame Node. This node allows creation of a video from a first and last frame. It calls the normal image to video endpoint, but only allows the subset of input options that support the `image_tail` request field.
        """
    
        @staticmethod
        def get_mode_string_mapping() -> dict[str, tuple[str, str, str]]:
            """
            Returns a mapping of mode strings to their corresponding (mode, duration, model_name) tuples.
            Only includes config combos that support the `image_tail` request field.
            """
            return {
                "standard mode / 5s duration / kling-v1": ("std", "5", "kling-v1"),
                "standard mode / 5s duration / kling-v1-5": ("std", "5", "kling-v1-5"),
                "pro mode / 5s duration / kling-v1": ("pro", "5", "kling-v1"),
                "pro mode / 5s duration / kling-v1-5": ("pro", "5", "kling-v1-5"),
                "pro mode / 5s duration / kling-v1-6": ("pro", "5", "kling-v1-6"),
                "pro mode / 10s duration / kling-v1-5": ("pro", "10", "kling-v1-5"),
                "pro mode / 10s duration / kling-v1-6": ("pro", "10", "kling-v1-6"),
            }
    
        @classmethod
        def INPUT_TYPES(s):
            modes = list(KlingStartEndFrameNode.get_mode_string_mapping().keys())
            return {
                "required": {
                    "start_frame": model_field_to_node_input(
                        IO.IMAGE, KlingImage2VideoRequest, "image"
                    ),
                    "end_frame": model_field_to_node_input(
                        IO.IMAGE, KlingImage2VideoRequest, "image_tail"
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
                    "cfg_scale": model_field_to_node_input(
                        IO.FLOAT, KlingImage2VideoRequest, "cfg_scale"
                    ),
                    "aspect_ratio": model_field_to_node_input(
                        IO.COMBO,
                        KlingImage2VideoRequest,
                        "aspect_ratio",
                        enum_type=AspectRatio,
                    ),
                    "mode": (
                        modes,
                        {
                            "default": modes[2],
                            "tooltip": "The configuration to use for the video generation following the format: mode / duration / model_name.",
                        },
                    ),
                },
                "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
            }
    
        DESCRIPTION = "Generate a video sequence that transitions between your provided start and end images. The node creates all frames in between, producing a smooth transformation from the first frame to the last."
    
        def parse_inputs_from_mode(self, mode: str) -> tuple[str, str, str]:
            """Parses the mode input into a tuple of (model_name, duration, mode)."""
            return KlingStartEndFrameNode.get_mode_string_mapping()[mode]
    
        def api_call(
            self,
            start_frame: torch.Tensor,
            end_frame: torch.Tensor,
            prompt: str,
            negative_prompt: str,
            cfg_scale: float,
            aspect_ratio: str,
            mode: str,
            auth_token: Optional[str] = None,
        ):
            mode, duration, model_name = self.parse_inputs_from_mode(mode)
            return super().api_call(
                prompt=prompt,
                negative_prompt=negative_prompt,
                model_name=model_name,
                start_frame=start_frame,
                cfg_scale=cfg_scale,
                mode=mode,
                aspect_ratio=aspect_ratio,
                duration=duration,
                end_frame=end_frame,
                auth_token=auth_token,
            )
    
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/kwai_vgi/kling-start-end-frame-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/kwai_vgi/kling-start-end-frame-to-video)

[Kling Image to Video - ComfyUI Built-in NodePrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-image-to-video)[Kling Text to Video - ComfyUI Built-in NodeNext](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-text-to-video)

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
