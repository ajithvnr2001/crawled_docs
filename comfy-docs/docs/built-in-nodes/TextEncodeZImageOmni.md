---
url: https://docs.comfy.org/built-in-nodes/TextEncodeZImageOmni/
title: TextEncodeZImageOmni - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:09.864093+00:00
---

# TextEncodeZImageOmni - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeZImageOmni/

Z Image

# TextEncodeZImageOmni - ComfyUI Built-in Node Documentation

Copy pageCopy page

TextEncodeZImageOmni encodes a text prompt together with up to three optional reference images into a conditioning format for image generation models.

Copy pageCopy page

TextEncodeZImageOmni encodes a text prompt together with up to three optional reference images into a conditioning format for image generation models. The prompt is tokenized and encoded with the CLIP model, and each connected image can optionally be processed by a vision encoder and/or a VAE so that visual references are embedded alongside the text. This node is marked as experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for tokenizing and encoding the text prompt.| CLIP| Yes|   
`image_encoder`| An optional vision encoder model. If provided, it is used to encode the input images, and the resulting embeddings are added to the conditioning.| CLIP_VISION| No|   
`prompt`| The text prompt to be encoded. Supports multiline input and dynamic prompts.| STRING| Yes|   
`auto_resize_images`| When enabled (default: True), input images are automatically resized before VAE encoding so their total pixel area is close to 1024x1024, with dimensions rounded to multiples of 8.| BOOLEAN| Yes| True  
False  
`vae`| An optional VAE model. If provided, it is used to encode the input images into latent representations, which are added to the conditioning as reference latents.| VAE| No|   
`image1`| The first optional reference image.| IMAGE| No|   
`image2`| The second optional reference image.| IMAGE| No|   
`image3`| The third optional reference image.| IMAGE| No|   
  
**Note:** The node accepts a maximum of three images (`image1`, `image2`, `image3`). The `image_encoder` and `vae` inputs are only used when at least one image is provided; when both are connected, each image is processed by both. When `auto_resize_images` is True and a `vae` is connected, images are resized to have a total pixel area close to 1024x1024 before encoding. If no images are provided, only the text prompt is encoded.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The final conditioning output. It contains the encoded text prompt and, when images are provided, may include encoded image embeddings, reference latents, and extra text embeddings derived from the image placeholder template.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/en.md)

* * *

**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeZImageOmni.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeZImageOmni)

[YuE2GenerateMusic - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/YuE2GenerateMusic)[AudioEncoderEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AudioEncoderEncode)

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
