---
url: https://docs.comfy.org/built-in-nodes/PH3ImageConditioning/
title: PH3ImageConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:52.062956+00:00
---

# PH3ImageConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PH3ImageConditioning/

Conditioning

# PH3ImageConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node turns a prompt into conditioning and an empty latent for a single still image with p-h3-image.

Copy pageCopy page

This node turns a prompt into conditioning and an empty latent for a single still image with p-h3-image. Without images it is text to image; with images connected, `image_1` is the image being edited and the other slots act as references, which the prompt addresses as `<Picture 1>`, `<Picture 2>`, and so on. The sampler needs a model patched by the MiniMax H3 sigma shift node with both shift values at 1.0.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The p-h3-image CLIP model used to tokenize the prompt, including any reference images, and to encode the conditioning.| CLIP| Yes| -  
`prompt`| What to generate, or how to edit `image_1`. With images connected, a short instruction gets `Edit <Picture 1>. ` prepended. An instruction that already starts with `Edit <Picture` or an edit brief produced by a prompt upsampler is used exactly as written.| STRING| Yes| -  
`width`| Output width in pixels. 0 uses the width of `image_1` after scaling, or 2912 when no image is connected (default: 0).| INT| Yes| 0 to MAX_RESOLUTION  
`height`| Output height in pixels. 0 uses the height of `image_1` after scaling, or 2912 when no image is connected (default: 0).| INT| Yes| 0 to MAX_RESOLUTION  
`vae`| The p-h3-image VAE. Required as soon as an image slot is connected, because the reference latents are encoded with it.| VAE| No| -  
`images`| Growable group of up to 9 images, `image_1` through `image_9`. `image_1` is the image being edited, the remaining slots are references.| AUTOGROW| No| 0 to 9 images  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Conditioning for the p-h3-image sampler. When images are connected it also carries the packed reference latents.| CONDITIONING  
`latent`| Empty latent for one still frame, including the two audio latents the model expects.| LATENT  
  
**Note:** Images require the `vae` input. Running the node with an image connected and no VAE raises an error. **Note:** The conditioning covers a single frame. For video or audio, use the MiniMax H3 video nodes instead.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `f1f5e5b2d3ff9bc2f3b81f3d0dd722e725c7930c6f95bf44ad83bc64357d2fb7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PH3ImageConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PH3ImageConditioning)

[Text Encode MOSS-Image Edit](https://docs.comfy.org/built-in-nodes/TextEncodeMOSSImageEdit)[RelayVSRConditioning](https://docs.comfy.org/built-in-nodes/RelayVSRConditioning)
