---
url: https://docs.comfy.org/built-in-nodes/LTXVGeneratedKeyframesToGuides/
title: LTXVGeneratedKeyframesToGuides - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.588414+00:00
---

# LTXVGeneratedKeyframesToGuides - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVGeneratedKeyframesToGuides/

Ltxv

# LTXVGeneratedKeyframesToGuides - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Generated Keyframes to Guides node pins generated keyframes from an earlier stage as frozen image guides on a later canvas.

Copy pageCopy page

The LTXV Generated Keyframes to Guides node pins generated keyframes from an earlier stage as frozen image guides on a later canvas. It decodes the keyframes as standalone frames, resizes them if needed, and writes them with a noise mask of 0 so they are not denoised again. After a temporal upscale, recorded indices are scaled from the canvas they were generated on onto this one; use `override_frame_indices` to set positions explicitly.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning to add the keyframe guides to.| CONDITIONING| Yes|   
`negative`| Negative conditioning to add the keyframe guides to.| CONDITIONING| Yes|   
`vae`| The VAE used to decode the keyframes if resizing is needed.| VAE| Yes|   
`latent`| The target video latent to add the guides to, e.g. the temporally upscaled one.| LATENT| Yes|   
`keyframes`| The keyframes output of LTXV Separate Generated Keyframes, which carries the pixel frame index each keyframe was generated at.| LATENT| Yes|   
`strength`| Guide strength. 1.0 is a hard pin; lower values relax it. (default: 1.0)| FLOAT| Yes| 0.0 - 10.0 (step 0.01)  
`override_frame_indices`| Optional — pin at these pixel frames instead of the recorded (or auto-scaled) positions. Provide one index per keyframe. Leave empty to reuse recorded positions, or to scale them when the target canvas is a different length (e.g. after temporal x2). (default: "")| STRING| No|   
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with the keyframes pinned as image guides.| CONDITIONING  
`negative`| Negative conditioning with the keyframes pinned as image guides.| CONDITIONING  
`latent`| Target video latent with the keyframes added as frozen guides.| LATENT  
  
## 

​

Notes

  * The `keyframes` input must be connected to the keyframes output of LTXV Separate Generated Keyframes. The node raises an error if the latent does not carry generated keyframe positions.
  * The `positive` and `negative` conditioning inputs must come from the positive and negative outputs of LTXV Separate Generated Keyframes. The node raises an error if the positive conditioning still carries generated keyframes.
  * The `latent` input must be a plain video latent (5D tensor). Guides must be added before merging the video and audio latents with Concat AV Latent.
  * Only a batch size of 1 is supported. Each guide is encoded from one image, so it cannot differ across batch elements.
  * The number of keyframes in the `keyframes` latent must match the number of recorded positions; otherwise an error is raised.
  * If `override_frame_indices` is left empty, recorded positions are used. If the target canvas has a different number of frames than the canvas the keyframes were generated on, the recorded indices are scaled automatically.
  * If `override_frame_indices` is provided, it must contain one integer index per keyframe, separated by commas or spaces. Indices must be unique and lie between 1 and (number of pixel frames in the target latent - 1). Otherwise an error is raised.
  * If any final keyframe index is greater than or equal to the number of pixel frames in the target latent, the node raises an error. This can happen when the target was resized temporally after the keyframes were generated.
  * The `strength` parameter has a minimum of 0.0 and a maximum of 10.0.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/en.md)

* * *

**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVGeneratedKeyframesToGuides.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVGeneratedKeyframesToGuides)

[LTXVDurationPredictor - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVDurationPredictor)[LTXVImgToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVImgToVideo)

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
