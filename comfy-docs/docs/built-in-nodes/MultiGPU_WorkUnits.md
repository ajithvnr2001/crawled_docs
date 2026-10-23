---
url: https://docs.comfy.org/built-in-nodes/MultiGPU_WorkUnits/
title: MultiGPU_WorkUnits - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.469993+00:00
---

# MultiGPU_WorkUnits - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MultiGPU_WorkUnits/

Multigpu

# MultiGPU_WorkUnits - ComfyUI Built-in Node Documentation

Copy pageCopy page

The MultiGPU CFG Split Node allows diffusion processing to occur using multiple GPUs installed in the same system.

Copy pageCopy page

## 

​

Overview:

The MultiGPU CFG Split Node allows diffusion processing to occur using multiple GPUs installed in the same system. Performance results are workflow dependent, but speedups of up to 1.95x have been measured in common workflows.

## 

​

Key Details:

Mixing different GPU types is not supported, the installed GPUs must be the same (ie 2x 5090, or 2x 5080, etc.) ComfyUI will automatically detect multiple installed GPUs at startup.

## 

​

Supported GPUs:

Any homogeneous dual GPU setups with Ampere+ architecture (e.g 2 x 3090 or 2 x RTX6000 Pro)

## 

​

Supported Models:

  * LTX-2.3
  * WAN 2.2
  * FLUX.2 Klein - Base Versions
  * Z-Image
  * Stable Diffusion 3.5 Large
  * Hunyuan Video
  * Qwen-Image-Edit-2511
  * Hunyuan-3D-v2.1
  * SDXL



## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to prepare for MultiGPU CFG splitting before sampling.| MODEL| Yes| N/A  
`max_gpus`| The maximum number of identical GPUs to use for splitting the workload. Set this to the number of matching GPUs installed in your system.| INT| Yes| Minimum: 1  
Step: 1  
Default: 2  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The model prepared for MultiGPU CFG splitting, ready for accelerated sampling.| MODEL  
  
## 

​

Node:

![image1.png](https://mintcdn.com/dripart/IIhZk7lIscrNou-I/images/built-in-nodes/MultiGPU_WorkUnits/image1.png?fit=max&auto=format&n=IIhZk7lIscrNou-I&q=85&s=3d4e6500bfaebc81f4b6d5bdd3e4244a)  
The max_gpus field should be set to the maximum number of identical GPUs installed in the system. **Node placement:** The MultiGPU CFG Split needs to be placed between the Model Load node and Sampling node. If other nodes are connected to the model output of the model loader node, the MultiGPU CFG should be the last node in the chain before the Sampling node. ![image2.png](https://mintcdn.com/dripart/IIhZk7lIscrNou-I/images/built-in-nodes/MultiGPU_WorkUnits/image2.png?fit=max&auto=format&n=IIhZk7lIscrNou-I&q=85&s=ca6947270d328fb07b6f01ff0821946d) **Workflow Requirements:** The node works by splitting the diffusion workflow at the CFG level, due to this, the CFG in the workflow must be greater than CFG=1. Distilled workflows which require a CFG =1 will not show a performance benefit when using the MultiGPU CFG Split node to run on multiple GPUs.

## 

​

Verifying Multi-GPU Utilization

When running a workflow with MultiGPU CFG Split enabled, you can look at the Windows Task Manager and select the performance category  
![image3.png](https://mintcdn.com/dripart/IIhZk7lIscrNou-I/images/built-in-nodes/MultiGPU_WorkUnits/image3.webp?fit=max&auto=format&n=IIhZk7lIscrNou-I&q=85&s=4d737f7c1baf3bf538f95f09d935f06e)  
![image4.png](https://mintcdn.com/dripart/IIhZk7lIscrNou-I/images/built-in-nodes/MultiGPU_WorkUnits/image4.webp?fit=max&auto=format&n=IIhZk7lIscrNou-I&q=85&s=d57d9ddfd06dc4dcbbb0c259e5c1ac5e)  
You should see activity on both installed GPUs while the sampler is running in the workflow.

## 

​

Sample Multi-GPU Workflow: (Wan 2.2 FP8)

[Sample workflow (Wan 2.2 FP8)](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/asset/video_wan2_2_14B_t2v_mGPU.json)

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/en.md)

* * *

**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MultiGPU_WorkUnits.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MultiGPU_WorkUnits)

[MultiGPU_Options - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MultiGPU_Options)[SelectCLIPDevice - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SelectCLIPDevice)

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
