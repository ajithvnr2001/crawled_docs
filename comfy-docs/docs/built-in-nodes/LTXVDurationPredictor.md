---
url: https://docs.comfy.org/built-in-nodes/LTXVDurationPredictor/
title: LTXVDurationPredictor - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.454302+00:00
---

# LTXVDurationPredictor - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVDurationPredictor/

Ltxv

# LTXVDurationPredictor - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node predicts the natural shot duration for a text prompt using an LTX 2.4 duration head loaded with ModelPatchLoader

Copy pageCopy page

This node predicts the natural shot duration for a text prompt using an LTX 2.4 duration head loaded with ModelPatchLoader, then snaps the result to the VAE’s 8k+1 frame grid. The prediction is converted into a frame count using the selected frame rate and the minimum and maximum duration limits.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model used to preprocess the text embeddings and run the duration head.| MODEL| Yes| N/A  
`positive`| The conditioning that provides the prompt’s text embeddings and metadata for the duration prediction.| CONDITIONING| Yes| N/A  
`duration_head`| LTX 2.4 duration head loaded with ModelPatchLoader. Must be an LTX duration head.| MODEL_PATCH| Yes| N/A  
`frame_rate`| Frame rate in frames per second used to convert seconds to frames (default: 24.0).| FLOAT| Yes| 1.0 to 120.0  
`min_seconds`| Minimum duration in seconds used when converting the prediction to a frame count (default: 1.0).| FLOAT| Yes| 0.5 to 120.0  
`max_seconds`| Maximum duration in seconds used when converting the prediction to a frame count (default: 20.0).| FLOAT| Yes| 0.5 to 120.0  
  
Note: The `duration_head` input must be a model patch containing an LTX duration head. If the connected model patch is not an LTX duration head, the node raises a ValueError. Only the first conditioning entry is used — if `positive` contains a batch of more than one prompt, the node evaluates just the first one.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`num_frames`| The predicted duration converted to a number of frames and snapped to the VAE’s 8k+1 frame grid.| INT  
`seconds`| Raw (unclamped) predicted duration. This is the value before snapping to the frame grid.| FLOAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/en.md)

* * *

**Source fingerprint (SHA-256):** `a4abb43128b8fe396e4c986d75028aea6bfdd9bb6fda07e24c88f8e04a61669e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVDurationPredictor.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVDurationPredictor)

[LTXVCropGuides - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVCropGuides)[LTXVGeneratedKeyframesToGuides - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVGeneratedKeyframesToGuides)

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
