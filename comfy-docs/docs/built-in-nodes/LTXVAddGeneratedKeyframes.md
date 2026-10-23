---
url: https://docs.comfy.org/built-in-nodes/LTXVAddGeneratedKeyframes/
title: LTXVAddGeneratedKeyframes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:16.786830+00:00
---

# LTXVAddGeneratedKeyframes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVAddGeneratedKeyframes/

Ltxv

# LTXVAddGeneratedKeyframes - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Add Generated Keyframes node appends detailing keyframes to a video latent.

Copy pageCopy page

The LTXV Add Generated Keyframes node appends detailing keyframes to a video latent. Each keyframe is one latent frame of tokens positioned over a single pixel frame; it is denoised with the video and is not part of the decoded output. Placement is one slot every `interval_frames` pixels, skipping I2V frames, existing guides, and generated keyframes already on the conditioning; pull them back out with LTXV Separate Generated Keyframes. A checkpoint trained for generated keyframes (one carrying `keyframes_abs_pos_embedding`) is required.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning the keyframes are attached to.| CONDITIONING| Yes| N/A  
`negative`| Negative conditioning the keyframes are attached to.| CONDITIONING| Yes| N/A  
`vae`| Only used to read the latent scale factors.| VAE| Yes| N/A  
`latent`| Plain 5D video latent to generate keyframes alongside. Add them before Concat AV Latent.| LATENT| Yes| N/A  
`interval_frames`| Pixel-frame stride for auto placement. Default 24 is about one keyframe per second at 24 fps. Occupied pixels are skipped. Ignored when frame_indices is set. (default: 24)| INT| No| 1-1024  
`keyframes`| Optional content to initialize the new keyframes with. Connect keyframes from an earlier Separate (same spatial size), or a plain video latent to copy the nearest frame at each new slot (e.g. after temporal upscale). These are still denoised, not pinned as guides. Recorded indices on a keyframes latent are ignored unless frame_indices is set. Only has an effect when sampling starts below sigma 1.| LATENT| No| N/A  
`frame_indices`| Optional pixel-frame indices. Leave empty to place from interval_frames on the current canvas. When set, this list is the placement (connected keyframes are matched in order). The last frame is allowed; frame 0 is not (it is already a standalone token). (default: empty string)| STRING| No| Comma-separated integers; 1 to the last pixel frame (frame 0 excluded)  
  
**Note:** The `latent` must be a plain 5D video latent with generated keyframes added before Concat AV Latent. When `frame_indices` is set, each listed pixel frame must be unique and cannot already hold an image keyframe, a guide, or a generated keyframe. If `frame_indices` is empty, occupied pixels are skipped automatically; if no free detailing slot exists, the node raises an error. When appending to existing generated keyframes, the latent must still have the same tokens per frame and the existing block must end at the last latent frame.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with generated-keyframe attention attached.| CONDITIONING  
`negative`| Negative conditioning with generated-keyframe attention attached.| CONDITIONING  
`latent`| Video latent with generated keyframes appended on T.| LATENT  
  
## 

​

Notes

  * The `interval_frames` parameter sets the spacing of auto-placed keyframes. A higher value results in fewer keyframes and wider spacing; a lower value produces more keyframes.
  * The `keyframes` input allows you to initialize the new keyframes with existing keyframes or a video latent. If a longer plain video latent is provided, the nearest video frame is copied at each new slot. These keyframes are still denoised and are not pinned as guides.
  * The `frame_indices` parameter allows you to specify exact pixel-frame indices where keyframes should be placed. When provided, `interval_frames` is ignored. The list must contain unique integers within the valid pixel range, and frame 0 is not allowed.
  * The `positive` and `negative` outputs contain the conditioning with generated-keyframe attention attached.
  * The `latent` output contains the video latent with generated keyframes appended on T.
  * A checkpoint trained for generated keyframes (one carrying `keyframes_abs_pos_embedding`) is required.
  * Pull generated keyframes back out with LTXV Separate Generated Keyframes.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/en.md)

* * *

**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVAddGeneratedKeyframes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVAddGeneratedKeyframes)

[GetICLoRAParameters - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GetICLoRAParameters)[LTXVAddGuide - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVAddGuide)

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
