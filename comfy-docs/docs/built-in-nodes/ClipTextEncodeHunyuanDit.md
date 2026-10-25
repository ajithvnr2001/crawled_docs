---
url: https://docs.comfy.org/built-in-nodes/ClipTextEncodeHunyuanDit/
title: CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:51.439829+00:00
---

# CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipTextEncodeHunyuanDit/

Hunyuan Image

# CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIPTextEncodeHunyuanDiT node converts text descriptions into a format that the HunyuanDiT model can understand.

Copy pageCopy page

The `CLIPTextEncodeHunyuanDiT` node converts text descriptions into a format that the HunyuanDiT model can understand. It is an advanced conditioning node designed for the dual text encoder architecture of HunyuanDiT, processing two separate text inputs through different tokenizers and combining their results into a single conditioning output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| A CLIP model instance used for text tokenization and encoding, which is core to generating conditions.| CLIP| Yes| -  
`bert`| Text input for encoding via the BERT tokenizer. Prefers phrases and keywords. Supports multiline and dynamic prompts.| STRING| Yes| -  
`mt5xl`| Text input for encoding via the mT5-XL tokenizer. Supports multiline and dynamic prompts (multilingual). Can use complete sentences and complex descriptions.| STRING| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The encoded conditioning output, combining both BERT and mT5-XL tokenized text, used for further processing in generation tasks.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/en.md)

* * *

**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipTextEncodeHunyuanDit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipTextEncodeHunyuanDit)

[Hunyuan3Dv2ConditioningMultiView](https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2ConditioningMultiView)[HunyuanImageToVideo](https://docs.comfy.org/built-in-nodes/HunyuanImageToVideo)
