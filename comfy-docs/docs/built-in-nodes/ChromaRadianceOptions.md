---
url: https://docs.comfy.org/built-in-nodes/ChromaRadianceOptions/
title: ChromaRadianceOptions - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:34.807074+00:00
---

# ChromaRadianceOptions - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ChromaRadianceOptions/

Chroma Radiance

# ChromaRadianceOptions - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ChromaRadianceOptions node allows you to configure advanced settings for the Chroma Radiance model.

Copy pageCopy page

The ChromaRadianceOptions node allows you to configure advanced settings for the Chroma Radiance model. It attaches a wrapper to an existing model and applies the selected options during the denoising process only when the current sigma value falls within the configured range, giving control over NeRF tile size and text token ID handling.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply Chroma Radiance options to| MODEL| Yes| -  
`preserve_wrapper`| When enabled, will delegate to an existing model function wrapper if it exists. Generally should be left enabled. (default: True)| BOOLEAN| No| -  
`start_sigma`| First sigma that these options will be in effect. (default: 1.0)| FLOAT| No| 0.0 to 1.0  
`end_sigma`| Last sigma that these options will be in effect. (default: 0.0)| FLOAT| No| 0.0 to 1.0  
`nerf_tile_size`| Allows overriding the default NeRF tile size. -1 means use the default (32). 0 means use non-tiling mode (may require a lot of VRAM). (default: -1)| INT| No| -1 and above  
`force_sequential_txt_ids`| Force usage of sequential text token IDs instead of zeroes. Should be used for checkpoints from 2026-05-22 to 2026-06-01 that are trained in this way but do not contain the **sequential** key in the state dict. (default: False)| BOOLEAN| No| -  
  
**Note:** The Chroma Radiance options only take effect when the current sigma value falls between `end_sigma` and `start_sigma` (inclusive). The `nerf_tile_size` option is only applied when set to 0 or a higher value (a value of -1 uses the default tile size of 32 and stores no override). The `force_sequential_txt_ids` option is only applied when set to True. When `nerf_tile_size` is -1 and `force_sequential_txt_ids` is False, no options are configured and the model is returned unchanged without any wrapper applied. **Note:** All inputs other than `model` are advanced options.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The model with Chroma Radiance options applied, or the unchanged model if no options are active| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/en.md)

* * *

**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ChromaRadianceOptions.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ChromaRadianceOptions)

[AnimaLLLiteApply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AnimaLLLiteApply)[ModelSamplingFLUXNext](https://docs.comfy.org/built-in-nodes/ModelSamplingFLUX)

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
