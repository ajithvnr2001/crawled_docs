---
url: https://docs.comfy.org/built-in-nodes/latent/video/trim-video-latent/
title: TrimVideoLatent Node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:40.035034+00:00
---

# TrimVideoLatent Node - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/latent/video/trim-video-latent/

## On this page

Back to top

  * Parameters
    * Input Parameters
    * Output Parameters
  * Usage Example
    * Source Code



Video

# TrimVideoLatent Node

Copy pageCopy page

Trim video frames in latent space

Copy pageCopy page

![ComfyUI TrimVideoLatent Node](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=87bf02eabffeba90db7e9409ddf48dd1) The TrimVideoLatent node is used to trim video frames in latent space (LATENT). It is commonly used when processing video latent sequences to remove unwanted frames from the beginning, achieving “forward trimming” of the video. Basic usage: Input the video latent data to be trimmed into samples, and set trim_amount to the number of frames to trim. The node will trim the specified number of frames from the beginning of the video and output the remaining latent sequence. Typical scenarios: Used in video generation, video editing and other scenarios to remove unwanted leading frames, or to work with other nodes to achieve video segment splicing and processing.

## Parameters

### Input Parameters

Parameter| Type| Required| Default| Description  
---|---|---|---|---  
samples| LATENT| Yes| None| Input latent video data  
trim_amount| INT| Yes| 0| Number of frames to trim (from start)  
  
### Output Parameters

Parameter| Type| Description  
---|---|---  
samples| LATENT| Trimmed video latent data  
  
## Usage Example

## Wan2.1 VACE Video Generation Workflow Example

Wan2.1 VACE Video Generation Workflow Example

### Source Code
    
    
    class TrimVideoLatent:
        @classmethod
        def INPUT_TYPES(s):
            return {"required": { "samples": ("LATENT",),
                                  "trim_amount": ("INT", {"default": 0, "min": 0, "max": 99999}),
                                 }}
    
        RETURN_TYPES = ("LATENT",)
        FUNCTION = "op"
    
        CATEGORY = "latent/video"
    
        EXPERIMENTAL = True
    
        def op(self, samples, trim_amount):
            samples_out = samples.copy()
    
            s1 = samples["samples"]
            samples_out["samples"] = s1[:, :, trim_amount:]
            return (samples_out,)
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/latent/video/trim-video-latent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/latent/video/trim-video-latent)

[Webcam Capture](https://docs.comfy.org/built-in-nodes/WebcamCapture)[Get Image/Video Latent Size](https://docs.comfy.org/built-in-nodes/GetLatentSize)
