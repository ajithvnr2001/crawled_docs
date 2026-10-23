---
url: https://docs.comfy.org/tutorials/image/newbie-image/newbie-image-exp-0-1/
title: ComfyUI NewBie-image-Exp0.1 Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:22.655348+00:00
---

# ComfyUI NewBie-image-Exp0.1 Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/newbie-image/newbie-image-exp-0-1/

## On this page

  * NewBie-image text-to-image workflow
    * NewBie Exp0.1: Anime Generation
  * Model links
  * Prompt format
    * XML structured prompt
    * XML tag reference



NewBie-image

# ComfyUI NewBie-image-Exp0.1 Workflow Example

Copy pageCopy page

NewBie-image-Exp0.1 is a 3.5B anime-style text-to-image model built on Next-DiT, optimized for detailed anime art with XML structured prompts in ComfyUI.

Copy pageCopy page

**NewBie-image-Exp0.1** is a 3.5B parameter DiT model developed by NewBieAI Lab for anime-style text-to-image generation. Built on the Next-DiT architecture, it delivers remarkably detailed and visually striking anime images. **Key Features** :

  * **3.5B Parameter Model** : Efficient yet powerful model size for high-quality anime generation
  * **Next-DiT Architecture** : Based on research from the Lumina architecture with a newly designed NewBie architecture
  * **Dual Text Encoders** : Uses Gemma3-4B-it as primary encoder with Jina CLIP v2 for improved prompt understanding
  * **FLUX VAE** : Utilizes FLUX.1-dev 16-channel VAE for richer colors and finer texture details
  * **XML Structured Prompts** : Supports XML format for better attention binding and attribute disentanglement

**Related Links** :

  * [GitHub](https://github.com/NewBieAI-Lab/NewBie-image-Exp0.1)
  * [Hugging Face](https://huggingface.co/NewBie-AI/NewBie-image-Exp0.1)
  * [Getting Started Guide](https://ai.feishu.cn/wiki/NZl9wm7V1iuNzmkRKCUcb1USnsh)



## 

​

NewBie-image text-to-image workflow

### 

​

NewBie Exp0.1: Anime Generation

Generate detailed anime-style images with NewBie Exp0.1’s Next-DiT architecture. Supports XML structured prompts for better multi-character scenes and attribute binding. ![NewBie-image text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_newbieimage_exp0_1-t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “NewBie-image” in Template Library

**Example output** ![NewBie-image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_newbieimage_exp0_1-t2i.png)

  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## 

​

Model links

**text_encoders**

  * [gemma_3_4b_it_bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/blob/main/split_files/text_encoders/gemma_3_4b_it_bf16.safetensors)
  * [jina_clip_v2_bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/blob/main/split_files/text_encoders/jina_clip_v2_bf16.safetensors)

**diffusion_models**

  * [NewBie-Image-Exp0.1-bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/blob/main/split_files/diffusion_models/NewBie-Image-Exp0.1-bf16.safetensors)

**vae**

  * [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/blob/main/split_files/vae/ae.safetensors)

**Model Storage Location**
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │      ├── gemma_3_4b_it_bf16.safetensors
    │   │      └── jina_clip_v2_bf16.safetensors
    │   ├── diffusion_models/
    │   │      └── NewBie-Image-Exp0.1-bf16.safetensors
    │   └── vae/
    │          └── ae.safetensors
    

## 

​

Prompt format

NewBie-image is an anime image generation model optimized for character generation. It uses XML structured prompts for training, where each `<>` tag defines a category (like `<appearance>`, `<clothing>`) and `</>` closes it. The tags inside are standard Danbooru tags. This structure enables precise control over multi-character scenes with better attribute binding. For the complete prompt writing guide, see the [official documentation](https://ai.feishu.cn/wiki/NZl9wm7V1iuNzmkRKCUcb1USnsh). NewBie-image-Exp0.1 supports three prompt formats:

  * **Natural language** : Standard text descriptions
  * **Tags** : Danbooru-style tags
  * **XML structured format** : Recommended for multi-character scenes



### 

​

XML structured prompt

For multi-character scenes, using XML structured prompts typically leads to more accurate image generation results with better attention binding and attribute disentanglement.
    
    
    <character_1>
    <n>$character_1$</n>
    <gender>1girl</gender>
    <appearance>chibi, red_eyes, blue_hair, long_hair, hair_between_eyes, head_tilt, tareme, closed_mouth</appearance>
    <clothing>school_uniform, serafuku, white_sailor_collar, white_shirt, short_sleeves, red_neckerchief, bow, blue_skirt, miniskirt, pleated_skirt, blue_hat, mini_hat, thighhighs, grey_thighhighs, black_shoes, mary_janes</clothing>
    <expression>happy, smile</expression>
    <action>standing, holding, holding_briefcase</action>
    <position>center_left</position>
    </character_1>
    
    <character_2>
    <n>$character_2$</n>
    <gender>1girl</gender>
    <appearance>chibi, red_eyes, pink_hair, long_hair, very_long_hair, multi-tied_hair, open_mouth</appearance>
    <clothing>school_uniform, serafuku, white_sailor_collar, white_shirt, short_sleeves, red_neckerchief, bow, red_skirt, miniskirt, pleated_skirt, hair_bow, multiple_hair_bows, white_bow, ribbon_trim, ribbon-trimmed_bow, white_thighhighs, black_shoes, mary_janes, bow_legwear, bare_arms</clothing>
    <expression>happy, smile</expression>
    <action>standing, holding, holding_briefcase, waving</action>
    <position>center_right</position>
    </character_2>
    
    <general_tags>
    <count>2girls, multiple_girls</count>
    <style>anime_style, digital_art</style>
    <background>white_background, simple_background</background>
    <atmosphere>cheerful</atmosphere>
    <quality>high_resolution, detailed</quality>
    <objects>briefcase</objects>
    <other>alternate_costume</other>
    </general_tags>
    

### 

​

XML tag reference

Tag| Description  
---|---  
`<n>`| Character name/identifier  
`<gender>`| Character gender (1girl, 1boy, etc.)  
`<appearance>`| Physical features (hair, eyes, body type)  
`<clothing>`| Outfit and accessories  
`<expression>`| Facial expression  
`<action>`| Pose and actions  
`<position>`| Position in the image  
`<count>`| Number of characters  
`<style>`| Art style  
`<background>`| Background description  
`<atmosphere>`| Overall mood  
`<quality>`| Quality tags  
`<objects>`| Objects in the scene  
`<other>`| Additional tags  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/newbie-image/newbie-image-exp-0-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/newbie-image/newbie-image-exp-0-1)

[Ovis-Image ComfyUI Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/ovis/ovis-image)[ERNIE-Image ComfyUI workflow exampleNext](https://docs.comfy.org/tutorials/image/ernie-image/ernie-image)

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
