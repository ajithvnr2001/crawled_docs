---
url: https://docs.comfy.org/built-in-nodes/BasicScheduler/
title: BasicScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:22.708806+00:00
---

# BasicScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BasicScheduler/

Schedulers

# BasicScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The BasicScheduler node is designed to compute a sequence of sigma values for diffusion models based on the provided scheduler, model

Copy pageCopy page

The `BasicScheduler` node is designed to compute a sequence of sigma values for diffusion models based on the provided scheduler, model, and denoising parameters. It dynamically adjusts the total number of steps based on the denoise factor to fine-tune the diffusion process, providing precise “recipes” for different stages in advanced sampling processes that require fine control (such as multi-stage sampling).

## 

​

Inputs

Parameter| Metaphor Description| Data Type| Input Type| Default| Range| Technical Purpose  
---|---|---|---|---|---|---  
`model`| **Canvas Type** : Different canvas materials need different paint formulas| MODEL| Input| -| -| Diffusion model object, determines sigma calculation basis  
`scheduler`| **Mixing Technique** : Choose how paint concentration changes| COMBO[STRING]| Widget| -| 9 options| Scheduling algorithm, controls noise decay mode  
`steps`| **Mixing Count** : 20 mixes vs 50 mixes precision difference| INT| Widget| 20| 1-10000| Sampling steps, affects generation quality and speed  
`denoise`| **Creation Intensity** : Control level from fine-tuning to repainting| FLOAT| Widget| 1.0| 0.0-1.0| Denoising strength, supports partial repainting scenarios  
  
### 

​

Scheduler Types

Based on source code `comfy.samplers.SCHEDULER_NAMES`, supports the following 9 schedulers:

Scheduler Name| Characteristics| Use Cases| Noise Decay Pattern  
---|---|---|---  
**normal**|  Standard linear| General scenarios, balanced| Uniform decay  
**karras**|  Smooth transition| High quality, detail-rich| Smooth non-linear decay  
**exponential**|  Exponential decay| Fast generation, efficiency| Exponential rapid decay  
**sgm_uniform**|  SGM uniform| Specific model optimization| SGM optimized decay  
**simple**|  Simple scheduling| Quick testing, basic use| Simplified decay  
**ddim_uniform**|  DDIM uniform| DDIM sampling optimization| DDIM specific decay  
**beta**|  Beta distribution| Special distribution needs| Beta function decay  
**linear_quadratic**|  Linear quadratic| Complex scenario optimization| Quadratic function decay  
**kl_optimal**|  KL optimal| Theoretical optimization| KL divergence optimized decay  
  
## 

​

Outputs

Parameter| Metaphor Description| Data Type| Output Type| Technical Meaning  
---|---|---|---|---  
`sigmas`| **Paint Recipe Chart** : Detailed paint concentration list for step-by-step use| SIGMAS| Output| Noise level sequence, guides diffusion model denoising process  
  
## 

​

Node Role: Artist’s Color Mixing Assistant

Imagine you are an artist creating a clear image from a chaotic mixture of paint (noise). `BasicScheduler` acts like your **professional color mixing assistant** , whose job is to prepare a series of precise paint concentration recipes:

### 

​

Workflow

  * **Step 1** : Use 90% concentration paint (high noise level)
  * **Step 2** : Use 80% concentration paint
  * **Step 3** : Use 70% concentration paint
  * **…**
  * **Final Step** : Use 0% concentration (clean canvas, no noise)



### 

​

Color Assistant’s Special Skills

**Different mixing methods (scheduler)** :

  * **“karras” mixing method** : Paint concentration changes very smoothly, like professional artist’s gradient technique
  * **“exponential” mixing method** : Paint concentration decreases rapidly, suitable for quick creation
  * **“linear” mixing method** : Paint concentration decreases uniformly, stable and controllable

**Fine control (steps)** :

  * **20 mixes** : Quick painting, efficiency priority
  * **50 mixes** : Fine painting, quality priority

**Creation intensity (denoise)** :

  * **1.0 = Complete new creation** : Start completely from blank canvas
  * **0.5 = Half transformation** : Keep half of original painting, transform half
  * **0.2 = Fine adjustment** : Only make subtle adjustments to original painting



### 

​

Collaboration with Other Nodes

`BasicScheduler` (Color Assistant) → Prepare Recipe → `SamplerCustom` (Artist) → Actual Painting → Completed Work

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BasicScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BasicScheduler)

[AlignYourStepsScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AlignYourStepsScheduler)[BetaSamplingScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BetaSamplingScheduler)

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
