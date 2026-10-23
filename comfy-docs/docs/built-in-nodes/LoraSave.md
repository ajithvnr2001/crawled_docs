---
url: https://docs.comfy.org/built-in-nodes/LoraSave/
title: LoraSave - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.608217+00:00
---

# LoraSave - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoraSave/

Experimental

# LoraSave - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoraSave node extracts and saves LoRA (Low-Rank Adaptation) files from model differences.

Copy pageCopy page

The LoraSave node extracts and saves LoRA (Low-Rank Adaptation) files from model differences. It can process diffusion model differences, text encoder differences, or both, converting them into LoRA format with specified rank and type. The resulting LoRA file is saved to the output directory for later use.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`filename_prefix`| The prefix for the output filename (default: “loras/ComfyUI_extracted_lora”)| STRING| Yes| -  
`rank`| The rank value for the LoRA, controlling the size and complexity (default: 8)| INT| Yes| 1-4096  
`lora_type`| The type of LoRA to create. “standard” extracts low-rank matrices via SVD; “full_diff” saves the full weight difference (default: “standard”)| COMBO| Yes| `"standard"`  
`"full_diff"`  
`bias_diff`| Whether to include bias differences in the LoRA calculation (default: True)| BOOLEAN| Yes| -  
`model_diff`| The ModelSubtract output to be converted to a lora| MODEL| No| -  
`text_encoder_diff`| The CLIPSubtract output to be converted to a lora| CLIP| No| -  
  
**Note:** At least one of `model_diff` or `text_encoder_diff` must be provided for the node to function. If both are omitted, the node will produce no output.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
-| This node saves a LoRA file to the output directory but does not return any data through the workflow| -  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/en.md)

* * *

**Source fingerprint (SHA-256):** `642510bfe083130cb2724d7ae38d30d4694c85a43c7ce27230690ddd9fe76b79`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoraSave.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoraSave)

[LatentBlend - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentBlend)[Mahiro - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Mahiro)

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
