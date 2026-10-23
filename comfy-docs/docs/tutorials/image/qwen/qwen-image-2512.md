---
url: https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512/
title: Qwen-Image-2512 ComfyUI Native Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:23.573644+00:00
---

# Qwen-Image-2512 ComfyUI Native Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512/

## On this page

  * Supported Aspect Ratios
  * Qwen-Image-2512 ComfyUI Native Workflow Example
    * Qwen Image 2512
    * 1\. Workflow file
    * 2\. Model download



Qwen

# Qwen-Image-2512 ComfyUI Native Workflow Example

Copy pageCopy page

Generate images with Qwen-Image-2512 in ComfyUI, the December update of Qwen-Image with enhanced human realism, finer natural detail, and better text rendering.

Copy pageCopy page

**Qwen-Image-2512** is the December update of Qwen-Image’s text-to-image foundational model. Compared to the base Qwen-Image model released in August, Qwen-Image-2512 features significant improvements in image quality and realism. **Key Enhancements in Qwen-Image-2512** :

  * **Enhanced Human Realism** : Significantly reduces the “AI-generated” look and substantially enhances overall image realism, especially for human subjects
  * **Finer Natural Detail** : Delivers notably more detailed rendering of landscapes, animal fur, and other natural elements
  * **Improved Text Rendering** : Improves the accuracy and quality of textual elements, achieving better layout and more faithful multimodal (text + image) composition

**Official Links** :

  * [GitHub Repository](https://github.com/QwenLM/Qwen-Image)
  * [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-2512)
  * [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-2512)
  * [Tech Report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf)
  * [Blog](https://qwen.ai/blog?id=qwen-image-2512)



## 

​

Supported Aspect Ratios

Aspect Ratio| Resolution  
---|---  
1:1| 1328x1328  
16:9| 1664x928  
9:16| 928x1664  
4:3| 1472x1104  
3:4| 1104x1472  
3:2| 1584x1056  
2:3| 1056x1584  
  
## 

​

Qwen-Image-2512 ComfyUI Native Workflow Example

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

### 

​

Qwen Image 2512

Text-to-image model with enhanced human realism, finer natural details, and improved text rendering. ![Qwen-Image-2512 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Qwen-Image-2512” in Template Library

**Example output** ![Qwen-Image-2512 example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_qwen_Image_2512.png)

### 

​

1\. Workflow file

After updating ComfyUI, you can find the workflow file from the templates, or drag the workflow preview above into ComfyUI to load it. The workflow includes two subgraphs:

  * **Text to Image (Qwen-Image 2512)** : Standard 50-step generation
  * **Text to Image (Qwen-Image 2512 4steps)** : Accelerated 4-step generation using Lightning LoRA



### 

​

2\. Model download

**Text Encoders**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**LoRA (Optional - for 4-step Lightning acceleration)**

  * [Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0.safetensors)

**Diffusion Models**

  * [qwen_image_2512_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) (Recommended for most users)
  * [qwen_image_2512_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_2512_bf16.safetensors) (If you have enough VRAM and want better quality)

**VAE**

  * [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors)

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   ├── 📂 loras/
    │   │      └── Qwen-Image-Lightning-4steps-V1.0.safetensors
    │   ├── 📂 diffusion_models/
    │   │      ├── qwen_image_2512_bf16.safetensors
    │   │      └── qwen_image_2512_fp8_e4m3fn.safetensors
    │   └── 📂 vae/
    │          └── qwen_image_vae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/qwen/qwen-image-2512.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/qwen/qwen-image-2512)

[Qwen-Image ComfyUI Native Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/qwen/qwen-image)[Qwen-Image-Edit ComfyUI Native Workflow ExampleNext](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)

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
