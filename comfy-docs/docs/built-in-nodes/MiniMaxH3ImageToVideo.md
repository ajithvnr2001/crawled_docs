---
url: https://docs.comfy.org/built-in-nodes/MiniMaxH3ImageToVideo/
title: MiniMaxH3ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.549865+00:00
---

# MiniMaxH3ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MiniMaxH3ImageToVideo/

Minimax

# MiniMaxH3ImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node prepares the conditioning and empty latent needed to generate a video with the MiniMax H3 model.

Copy pageCopy page

This node prepares the conditioning and empty latent needed to generate a video with the MiniMax H3 model. It takes a text prompt and, optionally, images for the first and/or last frame of the video, and converts them into model inputs. Keyframe images are resized, encoded, and attached to the conditioning at the start and end of the video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| CLIP model used to tokenize the prompt and encode the keyframe images into conditioning.| CLIP| Yes|   
`vae`| VAE model used to encode the keyframe images into latent space when keyframe images are provided.| VAE| Yes|   
`prompt`| Text prompt describing the video to generate. Supports multiple lines and dynamic prompts.| STRING| Yes|   
`width`| Width of the video in pixels (default: 1344).| INT| Yes| 32 to MAX_RESOLUTION (step 32)  
`height`| Height of the video in pixels (default: 768).| INT| Yes| 32 to MAX_RESOLUTION (step 32)  
`length`| Frame count at 24 fps, snapped up to the model’s 17k+5 grid (124 = ~5s; trained range is ~124-362, longer is untested) (default: 124).| INT| Yes| 5 to 3600 (step 17)  
`first_frame`| Optional image used as the first frame of the video. It is stretched to the full canvas size, so its aspect ratio is not preserved. Only the first image of the input batch is used.| IMAGE| No|   
`last_frame`| Optional image used as the last frame of the video. It is cropped to cover the canvas while preserving its aspect ratio. Only the first image of the input batch is used.| IMAGE| No|   
  
When `first_frame` and/or `last_frame` are provided, the keyframe images are encoded with the VAE and attached to the conditioning at frame 0 and at the final frame, respectively. When neither is provided, the node works from the prompt alone. The requested `length` is snapped up to the nearest valid frame count (17k + 5), so the effective frame count may be slightly higher than requested. The audio-video latent is created as an empty pair matching the requested `width`, `height`, and the snapped frame count. The audio portion is sized from the same frame count at 40 audio frames per second.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Conditioning containing the encoded prompt and, when keyframe images are provided, the encoded keyframes and frame count for the MiniMax H3 model.| CONDITIONING  
`latent`| Empty audio-video latent representing the content to be generated, with the requested width, height, and frame count.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MiniMaxH3ImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MiniMaxH3ImageToVideo)

[MiniMaxH3AddGuide - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MiniMaxH3AddGuide)[MiniMaxH3ReferenceToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MiniMaxH3ReferenceToVideo)

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
