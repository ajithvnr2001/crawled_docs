---
url: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeLumina2/
title: CLIPTextEncodeLumina2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:33.529403+00:00
---

# CLIPTextEncodeLumina2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeLumina2/

Lumina

# CLIPTextEncodeLumina2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node encodes a system prompt and a user prompt using a CLIP model into an embedding that can be used to guide the diffusion model towards generating

Copy pageCopy page

This node encodes a system prompt and a user prompt using a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images. It combines a pre-defined Lumina 2 system prompt with your custom text prompt and processes them through the CLIP model to create conditioning data for image generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`system_prompt`| Lumina2 provide two types of system prompts: Superior: You are an assistant designed to generate superior images with the superior degree of image-text alignment based on textual prompts or user prompts. Alignment: You are an assistant designed to generate high-quality images with the highest degree of image-text alignment based on textual prompts.| COMBO| Yes| `"superior"`  
`"alignment"`  
`user_prompt`| The text to be encoded. Supports multiline input and dynamic prompts.| STRING| Yes| N/A  
`clip`| The CLIP model used for encoding the text.| CLIP| Yes| N/A  
  
**Note:** The `clip` input is required and cannot be None. If the clip input is invalid, the node will raise an error indicating that the checkpoint may not contain a valid CLIP or text encoder model.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| A conditioning containing the embedded text used to guide the diffusion model.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/en.md)

* * *

**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CLIPTextEncodeLumina2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CLIPTextEncodeLumina2)

[LTXVSeparateGeneratedKeyframes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVSeparateGeneratedKeyframes)[TextEncodeMageFlowEdit - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeMageFlowEdit)

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
