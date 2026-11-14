---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-image-to-video/
title: MiniMax Image to Video - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:37.741987+00:00
---

# MiniMax Image to Video - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-image-to-video/

## On this page

Back to top

  * Parameters
    * Required Parameters
    * Optional Parameters
    * Output
  * Source Code



MiniMax

# MiniMax Image to Video - ComfyUI Native Node Documentation

Copy pageCopy page

A node that converts static images to dynamic videos using MiniMax AI

Copy pageCopy page

![ComfyUI Native MiniMax Image to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=20daea4b1e99477334f1a7be3d3cb4d3) The MiniMax Image to Video node uses MiniMax’s API to generate videos from input images and text prompts.

## Parameters

### Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| -| Input image used as the first frame of video  
prompt_text| string| ""| Text prompt to guide video generation  
model| select| ”I2V-01”| Available models: “I2V-01-Director”, “I2V-01”, “I2V-01-live”  
  
### Optional Parameters

Parameter| Type| Description  
---|---|---  
seed| integer| Random seed for noise generation  
  
### Output

Output| Type| Description  
---|---|---  
VIDEO| video| Generated video  
  
## Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class MinimaxImageToVideoNode(MinimaxTextToVideoNode):
        """
        Generates videos synchronously based on an image and prompt, and optional parameters using Minimax's API.
        """
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "image": (
                        IO.IMAGE,
                        {
                            "tooltip": "Image to use as first frame of video generation"
                        },
                    ),
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
                            "I2V-01-Director",
                            "I2V-01",
                            "I2V-01-live",
                        ],
                        {
                            "default": "I2V-01",
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
        DESCRIPTION = "Generates videos from an image and prompts using Minimax's API"
        FUNCTION = "generate_video"
        CATEGORY = "api node/video/Minimax"
        API_NODE = True
        OUTPUT_NODE = True
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/minimax/minimax-image-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/minimax/minimax-image-to-video)

[Kling Text to Video](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-text-to-video)[MiniMax Text to Video](https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-text-to-video)
