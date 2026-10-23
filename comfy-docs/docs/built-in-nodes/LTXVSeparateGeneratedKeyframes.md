---
url: https://docs.comfy.org/built-in-nodes/LTXVSeparateGeneratedKeyframes/
title: LTXVSeparateGeneratedKeyframes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.905949+00:00
---

# LTXVSeparateGeneratedKeyframes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVSeparateGeneratedKeyframes/

Ltxv

# LTXVSeparateGeneratedKeyframes - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Separate Generated Keyframes node splits the generated keyframes added by LTXV Add Generated Keyframes back out of a sampled latent and removes them

Copy pageCopy page

## 

​

Overview

The LTXV Separate Generated Keyframes node splits the generated keyframes added by LTXV Add Generated Keyframes back out of a sampled latent and removes them from the conditioning. Use it before spatially upscaling the video latent. Do not run LTXV Crop Guides first — it treats generated keyframes as disposable guides and drops them.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning that holds the generated-keyframe metadata. The metadata is removed from it on output.| CONDITIONING| Yes| N/A  
`negative`| Negative conditioning that holds the generated-keyframe metadata. The metadata is removed from it on output.| CONDITIONING| Yes| N/A  
`latent`| Video latent that contains the generated keyframes. The keyframes are stripped from it on output.| LATENT| Yes| N/A  
`keyframes_to_batch`| Return the keyframes as a batch of single-frame latents. Leave off to get them as one multi-frame latent, which is what the latent upsampler and a later Add Generated Keyframes expect.| BOOLEAN| No| default: False  
  
### 

​

Notes on Inputs

  * `positive` must contain generated-keyframe metadata, otherwise the node raises an error telling you to add them with LTXV Add Generated Keyframes first.
  * `latent` must be a plain video latent (a 5D tensor). If the video and audio latents are still combined, split them with Separate AV Latent first.
  * The number of tokens per latent frame recorded when the keyframes were added must match the tokens per frame of the supplied `latent`. If the latent was rescaled after the keyframes were added, they no longer line up and the node raises an error — separate them before upscaling the latent.
  * The recorded keyframe frame range must fit inside the supplied `latent`, otherwise the node raises an error that the keyframes were recorded against a different latent.
  * The recorded guide attention entry index must still exist in the conditioning. If the conditioning was rebuilt after the keyframes were added, the node raises an error.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with generated-keyframe metadata removed.| CONDITIONING  
`negative`| Negative conditioning with generated-keyframe metadata removed.| CONDITIONING  
`latent`| Video latent with the generated keyframes stripped.| LATENT  
`keyframes`| The peeled keyframes, labeled with generated_keyframe_indices and generated_keyframe_num_frames. Feed these to a later Add Generated Keyframes to initialize new slots, or to Generated Keyframes To Guides to pin them as frozen image guides (indices are remapped if the canvas length changed).| LATENT  
  
## 

​

Notes

  * The `keyframes_to_batch` parameter determines whether the keyframes are returned as a batch of single-frame latents or as one multi-frame latent.
  * The node ensures that the generated keyframes are removed from the conditioning and the latent before any further processing.
  * The `keyframes` output can be used to initialize new slots for generated keyframes or to pin them as frozen image guides.
  * The node raises a `ValueError` if the latent does not contain generated keyframes or if the keyframes do not match the expected format.
  * The node assumes that the generated keyframes were added using the LTXV Add Generated Keyframes node and that they are compatible with the current latent.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/en.md)

* * *

**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVSeparateGeneratedKeyframes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVSeparateGeneratedKeyframes)

[LTXVReferenceAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVReferenceAudio)[CLIPTextEncodeLumina2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeLumina2)

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
