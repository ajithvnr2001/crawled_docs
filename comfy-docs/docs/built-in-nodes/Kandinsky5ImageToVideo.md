---
url: https://docs.comfy.org/built-in-nodes/Kandinsky5ImageToVideo/
title: Kandinsky5ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:13.888025+00:00
---

# Kandinsky5ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Kandinsky5ImageToVideo/

Kandinsky

# Kandinsky5ImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kandinsky5ImageToVideo node prepares conditioning and latent data for video generation using the Kandinsky model.

Copy pageCopy page

The Kandinsky5ImageToVideo node prepares conditioning and latent data for video generation using the Kandinsky model. It creates an empty video latent sized to the requested width, height, length, and batch size, and can optionally encode a starting image to guide the initial frames of the generated video by updating the positive and negative conditioning.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning prompts to guide the video generation.| CONDITIONING| Yes| N/A  
`negative`| The negative conditioning prompts to steer the video generation away from certain concepts.| CONDITIONING| Yes| N/A  
`vae`| The VAE model used to encode the optional starting image into the latent space.| VAE| Yes| N/A  
`width`| The width of the output video in pixels (default: 768).| INT| Yes| 16 to 16384 (step 16)  
`height`| The height of the output video in pixels (default: 512).| INT| Yes| 16 to 16384 (step 16)  
`length`| The number of frames in the video (default: 121).| INT| Yes| 1 to 16384 (step 4)  
`batch_size`| The number of video sequences to generate simultaneously (default: 1).| INT| Yes| 1 to 4096  
`start_image`| An optional starting image or batch of frames. If provided, it is encoded and used to replace the noisy start of the model’s output latents.| IMAGE| No| N/A  
  
**Note:** When a `start_image` is provided, it is automatically resized to match the specified `width` and `height` using bilinear interpolation. Only the first `length` frames of the image batch are used for encoding; any additional frames are ignored. If the image batch has fewer than `length` frames, only those frames are used. Only the RGB channels of the image are encoded. The encoded latent is then injected into both the `positive` and `negative` conditioning to guide the video’s initial appearance, and the clean encoded frames replace the noisy start of the model’s output latents.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning, updated with encoded start image data when a `start_image` is provided.| CONDITIONING  
`negative`| The modified negative conditioning, updated with encoded start image data when a `start_image` is provided.| CONDITIONING  
`latent`| Empty video latent. A latent tensor filled with zeros, shaped for the specified dimensions.| LATENT  
`cond_latent`| Clean encoded start images, used to replace the noisy start of the model output latents. Empty when no `start_image` is provided.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Kandinsky5ImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Kandinsky5ImageToVideo)

[CLIPTextEncodeKandinsky5 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeKandinsky5)[LotusConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LotusConditioning)

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
