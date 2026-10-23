---
url: https://docs.comfy.org/built-in-nodes/LoadTrainingDataset/
title: LoadTrainingDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.358443+00:00
---

# LoadTrainingDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadTrainingDataset/

Training

# LoadTrainingDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node loads an encoded training dataset (latents and conditioning) that was previously saved to disk.

Copy pageCopy page

This node loads an encoded training dataset (latents and conditioning) that was previously saved to disk. It reads all `shard_*.pkl` data shard files from a selected dataset folder in the datasets directory and returns the combined latent vectors and conditioning data for use in training workflows.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`folder_name`| Saved dataset to load, from the datasets directory.| COMBO| Yes| One option per dataset folder found in the datasets directory  
  
Note: The `folder_name` options are built automatically by scanning the datasets directory. A subfolder is listed as a dataset when it contains a `metadata.json` file or at least one `.safetensors` file (the scan does not descend into a folder that matches). The selected dataset folder is searched across all configured dataset root directories, and the folder name must resolve to a subfolder inside one of those roots. The node reads all files named `shard_*.pkl` in the selected folder, in sorted order, and raises an error if no shard files are found or if the folder cannot be located.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latents`| List of latent dicts (output list), where each dict contains a `"samples"` key with a tensor.| LATENT  
`conditioning`| List of conditioning lists (output list), where each inner list contains conditioning data for the corresponding sample.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadTrainingDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadTrainingDataset)

[KSamplerAdvanced - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KSamplerAdvanced)[LossGraphNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LossGraphNode)

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
