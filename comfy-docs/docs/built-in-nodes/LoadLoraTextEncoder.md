---
url: https://docs.comfy.org/built-in-nodes/LoadLoraTextEncoder/
title: LoadLoraTextEncoder - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.461649+00:00
---

# LoadLoraTextEncoder - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadLoraTextEncoder/

Loaders

# LoadLoraTextEncoder - ComfyUI Built-in Node Documentation

Copy pageCopy page

Apply a stack of LoRAs to a CLIP text encoder in a single node.

Copy pageCopy page

Apply a stack of LoRAs to a CLIP text encoder in a single node. Each row of `loras` holds a LoRA file, its strength and an on/off switch, and the rows are applied from top to bottom so every row patches the result of the row above it. LoRA files that change the text encoder are usually applied to the model as well, so this node is normally paired with Load LoRA (Model) using the same rows.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP text encoder the LoRAs will be applied to.| CLIP| Yes| -  
`loras`| Growable group of LoRAs, applied to the text encoder in row order (`loras.0`, `loras.1`, and so on). Add one row per LoRA; each row holds a file, a strength and an on/off switch.| DYNAMIC_GROUP| Yes| 1 to 20 rows  
  
### 

​

`loras` Row Fields

Every row repeats the following fields, and each field is required within a submitted row.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`lora_name`| The name of the LoRA file to apply.| COMBO| Yes| Multiple options available  
`strength`| How strongly to apply this LoRA to the text encoder. `0` turns it off, and a negative value inverts the effect. (default: 1.0)| FLOAT| Yes| -100 to 100 (step 0.01)  
`enabled`| Turn off to skip this LoRA without changing its file or strength. (default: true)| BOOLEAN| Yes| false / true  
  
### 

​

Parameter Constraints

  * **Row count:** at least one row must be submitted and at most 20 rows are accepted, so the highest row index is 19.
  * **Skipped rows:** a row is skipped when its file is empty, when `enabled` is off, or when `strength` is `0`. A negative strength is passed through rather than skipped.
  * **Row order:** rows are applied in the order they appear, and each row starts from the text encoder returned by the previous row.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CLIP`| The CLIP text encoder after the LoRA rows that are not skipped have been applied.| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/en.md)

* * *

**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadLoraTextEncoder.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadLoraTextEncoder)

[LoadLoraModel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadLoraModel)[LoadMediaPipeFaceLandmarker - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadMediaPipeFaceLandmarker)

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
