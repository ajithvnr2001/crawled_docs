---
url: https://docs.comfy.org/built-in-nodes/SaveTrainingDataset/
title: SaveTrainingDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.541817+00:00
---

# SaveTrainingDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveTrainingDataset/

Training

# SaveTrainingDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node saves an encoded training dataset to disk for efficient loading during training.

Copy pageCopy page

This node saves an encoded training dataset to disk for efficient loading during training. It takes image latents and their matching text conditioning, splits them into smaller files called shards, and stores them in a folder inside the datasets directory. It also writes a metadata file describing the dataset.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latents`| List of latent dicts from MakeTrainingDataset.| LATENT| Yes| N/A  
`conditioning`| List of conditioning lists from MakeTrainingDataset.| CONDITIONING| Yes| N/A  
`folder_name`| Name of folder to save the dataset into, inside the datasets directory. Subfolders like ‘project/run1’ are allowed. (default: “training_dataset”)| STRING| Yes| N/A  
`shard_size`| Number of samples per shard file. (default: 1000)| INT| Yes| 1 to 100000  
  
**Note:** The number of items in `latents` must exactly match the number of items in `conditioning`; the node raises an error if these counts do not match. The `folder_name` must name a subfolder of the datasets directory (for example `my_dataset`) — it cannot be the datasets directory itself, and folder names that would resolve outside the datasets directory are rejected. The `shard_size` parameter is an advanced setting.

## 

​

Outputs

This node does not produce any output data. Its function is to save files to your disk. Each shard is saved as a `shard_XXXX.pkl` file in the chosen folder, and a `metadata.json` file records the total number of samples, the number of shards, and the shard size.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveTrainingDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveTrainingDataset)

[ResolutionBucket - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ResolutionBucket)[TrainLoraNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TrainLoraNode)

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
