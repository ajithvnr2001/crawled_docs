---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-image-to-video/
title: PixVerse Image to Video - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:37.177114+00:00
---

# PixVerse Image to Video - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-image-to-video/

## On this page

Back to top

  * Parameters
    * Required Parameters
    * Optional Parameters
    * Output
  * Source Code



PixVerse

# PixVerse Image to Video - ComfyUI Native Node Documentation

Copy pageCopy page

A node that converts static images to dynamic videos using PixVerse AI

Copy pageCopy page

![ComfyUI Native PixVerse Image to Video Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=5dad32a76df9845caf721b255b39df09) The PixVerse Image to Video node uses PixVerse’s API to transform static images into dynamic videos. It preserves the visual features of the original image while adding natural motion based on text prompts.

## Parameters

### Required Parameters

Parameter| Type| Default| Description  
---|---|---|---  
image| Image| -| Input image to convert to video  
prompt| String| ""| Text prompt describing video motion/content  
negative_prompt| String| ""| Elements to avoid in the video  
seed| Integer| -1| Random seed (-1 for random)  
quality| Select| ”high”| Output video quality level  
aspect_ratio| Select| ”r16_9”| Output video aspect ratio  
duration| Select| ”seconds_4”| Length of generated video  
motion_mode| Select| ”standard”| Video motion style  
  
### Optional Parameters

Parameter| Type| Default| Description  
---|---|---|---  
pixverse_template| PIXVERSE_TEMPLATE| None| Optional PixVerse template  
  
### Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
  
## Source Code

[Node Source Code (Updated 2025-05-05)]
    
    
    class PixverseImageToVideoNode(ComfyNodeABC):
        """
        Pixverse Image to Video
    
        Generates videos from an image and prompts.
        """
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "image": ("IMAGE",),
                    "prompt": ("STRING", {"multiline": True, "default": ""}),
                    "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                    "seed": ("INT", {"default": -1, "min": -1, "max": 0xffffffffffffffff}),
                    "quality": (list(PixverseQuality.__members__.keys()), {"default": "high"}),
                    "aspect_ratio": (list(PixverseAspectRatio.__members__.keys()), {"default": "r16_9"}),
                    "duration": (list(PixverseDuration.__members__.keys()), {"default": "seconds_4"}),
                    "motion_mode": (list(PixverseMotionMode.__members__.keys()), {"default": "standard"}),
                },
                "optional": {
                    "pixverse_template": ("PIXVERSE_TEMPLATE",),
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        RETURN_TYPES = ("VIDEO",)
        DESCRIPTION = "Generates videos from an image and prompts using Pixverse's API"
        FUNCTION = "generate_video"
        CATEGORY = "api node/video/Pixverse"
        API_NODE = True
        OUTPUT_NODE = True
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/pixverse/pixverse-image-to-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/pixverse/pixverse-image-to-video)

[PikaTextToVideoNode2_2](https://docs.comfy.org/built-in-nodes/PikaTextToVideoNode2_2)[PixVerse Template](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-template)
