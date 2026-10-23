---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-image-to-video/
title: MiniMax Image to Video - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:31.702279+00:00
---

# MiniMax Image to Video - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-image-to-video/

## On this page

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

## 

​

Parameters

### 

​

Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| image| -| Input image used as the first frame of video  
prompt_text| string| ""| Text prompt to guide video generation  
model| select| ”I2V-01”| Available models: “I2V-01-Director”, “I2V-01”, “I2V-01-live”  
  
### 

​

Optional Parameters

Parameter| Type| Description  
---|---|---  
seed| integer| Random seed for noise generation  
  
### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| video| Generated video  
  
## 

​

Source Code

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

[Kling Text to Video - ComfyUI Built-in NodePrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-text-to-video)[MiniMax Text to Video - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/video/minimax/minimax-text-to-video)

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
