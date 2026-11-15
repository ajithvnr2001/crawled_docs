---
url: https://docs.comfy.org/built-in-nodes/LtxApiVideoAlphaGen/
title: LTX Video AlphaGen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.762706+00:00
---

# LTX Video AlphaGen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LtxApiVideoAlphaGen/

Video

# LTX Video AlphaGen - ComfyUI Built-in Node Documentation

Copy pageCopy page

Extracts a grayscale alpha matte, white for foreground, that matches the input video frame for frame.

Copy pageCopy page

Extracts a grayscale alpha matte, white for foreground, that matches the input video frame for frame. Feed the matte to Get Video Components and Image To Mask to turn it into a mask. Audio is not kept.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Video to matte, up to 10 seconds and 3840x2160 in either orientation.| VIDEO| Yes| -  
`seed`| Controls whether the node re-runs; results are non-deterministic regardless of the seed. Default: 42.| INT| No| 0 to 4294967295  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`matte`| The alpha matte as a video, one frame per input frame and without audio.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/en.md)

* * *

**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LtxApiVideoAlphaGen.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LtxApiVideoAlphaGen)

[FLUX 3 Max Text to Video](https://docs.comfy.org/built-in-nodes/Flux3MaxTextToVideoNode)[LTX Video Reframe](https://docs.comfy.org/built-in-nodes/LtxApiVideoReframe)
