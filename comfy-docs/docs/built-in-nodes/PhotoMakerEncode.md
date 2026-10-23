---
url: https://docs.comfy.org/built-in-nodes/PhotoMakerEncode/
title: PhotoMakerEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:41.558107+00:00
---

# PhotoMakerEncode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PhotoMakerEncode/

Photomaker

# PhotoMakerEncode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PhotoMakerEncode node combines a reference image with a text prompt to create conditioning data for image generation.

Copy pageCopy page

The PhotoMakerEncode node combines a reference image with a text prompt to create conditioning data for image generation. When the text contains the word “photomaker”, the node uses the PhotoMaker model to insert the visual identity of the reference image into the conditioning at that position in the prompt.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`photomaker`| The PhotoMaker model used to process the reference image and generate image-based embeddings| PHOTOMAKER| Yes| -  
`image`| The reference image that provides the visual characteristics for the conditioning| IMAGE| Yes| -  
`clip`| The CLIP model used for text tokenization and text encoding| CLIP| Yes| -  
`text`| The text prompt for conditioning generation. Supports multiline text and dynamic prompts (default: “photograph of photomaker”)| STRING| Yes| Any string  
  
**Note:** When the text contains “photomaker” as a standalone word, the node removes that word from the encoded prompt and applies the reference image’s identity at that position using the PhotoMaker model. If “photomaker” is not found in the text, the node returns standard text conditioning without image influence.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| Conditioning data containing the text and image embeddings that guide image generation, together with the pooled output from the CLIP text encoder| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/en.md)

* * *

**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PhotoMakerEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PhotoMakerEncode)

[MiniMaxMusic3TextEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MiniMaxMusic3TextEncode)[CLIPTextEncodePixArtAlpha - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPTextEncodePixArtAlpha)

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
