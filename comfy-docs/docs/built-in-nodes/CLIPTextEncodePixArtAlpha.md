---
url: https://docs.comfy.org/built-in-nodes/CLIPTextEncodePixArtAlpha/
title: CLIPTextEncodePixArtAlpha - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:53.379454+00:00
---

# CLIPTextEncodePixArtAlpha - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CLIPTextEncodePixArtAlpha/

Pixart

# CLIPTextEncodePixArtAlpha - ComfyUI Built-in Node Documentation

Copy pageCopy page

Encodes text and sets the resolution conditioning for PixArt Alpha.

Copy pageCopy page

Encodes text and sets the resolution conditioning for PixArt Alpha. This node processes text input and adds width and height information to create conditioning data specifically for PixArt Alpha models. It does not apply to PixArt Sigma models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width dimension for resolution conditioning (default: 1024)| INT| Yes| 0 to MAX_RESOLUTION  
`height`| The height dimension for resolution conditioning (default: 1024)| INT| Yes| 0 to MAX_RESOLUTION  
`text`| Text input to be encoded. Supports multiline input and dynamic prompts.| STRING| Yes| -  
`clip`| CLIP model used for tokenization and encoding| CLIP| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| Encoded conditioning data with text tokens and resolution information| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/en.md)

* * *

**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CLIPTextEncodePixArtAlpha.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CLIPTextEncodePixArtAlpha)

[PhotoMakerEncode](https://docs.comfy.org/built-in-nodes/PhotoMakerEncode)[QwenImage21Cache](https://docs.comfy.org/built-in-nodes/QwenImage21Cache)
