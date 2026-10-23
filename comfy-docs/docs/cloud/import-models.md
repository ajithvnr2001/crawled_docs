---
url: https://docs.comfy.org/cloud/import-models/
title: Import models - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:34.185923+00:00
---

# Import models - ComfyUI

> Source: https://docs.comfy.org/cloud/import-models/

## On this page

  * Overview
  * Requirements
  * How to import models
    * 1\. Access the import feature
    * 2\. Paste the link
  * How to view imported models
  * How to get model import links
    * 1\. Get link from Civitai
    * 2\. Get link from Hugging Face
  * Import private models
    * 1\. Generate your API keys
    * 2\. Save your API keys
    * 3\. Import the private model
  * FAQ



Cloud Exclusive

# Import models

Copy pageCopy page

Learn how to import models from Civitai and Hugging Face to Comfy Cloud

Copy pageCopy page

This is a **Comfy Cloud** feature and is only available in the cloud version. To learn more about Comfy Cloud, see [Comfy Cloud](https://docs.comfy.org/get_started/cloud).

## 

​

Overview

Comfy Cloud allows you to import models directly from Civitai and Hugging Face. This feature is available for users with a **Creator** subscription or higher.

## 

​

Requirements

  * **Subscription** : Creator tier or above
  * **Supported sources** : Civitai and Hugging Face



## 

​

How to import models

### 

​

1\. Access the import feature

![Import](https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=0621b50c1cc510ddcdd5bb69f96625b7)

  1. Click the **Models** button in the left sidebar to open the Model Library.
  2. In the Model Library modal, click the **Import** button.



### 

​

2\. Paste the link

  1. Paste the model link you obtained from Hugging Face or Civitai. ![Import Modal](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=077d3bf113f8139db1ce9f94e3c42202)
  2. If the link is valid, you will see a confirmation indicator and can click the `Continue` button to proceed. ![Import Modal](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=3b35abf880dc14c6d0186e1e6a104f92)
  3. Select the model type and target folder. ![Import Modal](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=10c28ec6293b6d2658d2899ebbae072f)
  4. Wait for the model to finish downloading. ![Import Modal](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=d80d9bb488937b1b2493dfc4929b7a17)
  5. Once downloaded, you can find the model in your Model Library.



## 

​

How to view imported models

In the Model Library, select “My Models” in the dropdown filter to filter out the models you imported. ![Imported Models](https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=9e0b5c5f1a200c7337f94aa67d7ffd36)

## 

​

How to get model import links

### 

​

1\. Get link from Civitai

  1. Go to [Civitai](https://civitai.com/) and find the model you want to import.
  2. Right-click the download button and select “Copy link address” to get the model download link.

![Copy Civitai Link](https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=48e3791d2dda7a9df235b1b4e73b0942)

### 

​

2\. Get link from Hugging Face

  1. Go to [Hugging Face](https://huggingface.co/) and find the model repository you want to import.
  2. Navigate to the model files page. Supported formats are typically “.safetensor” or “.sft” files. Click on the specific model name to enter its detail page.

![Copy Huggingface model link](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=786214df669fd53613b295e6bd6e8cef)

  3. On the detail page, click the `Copy Download Link` button to get the model download link.

![Copy Huggingface model link](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=4681f3e56576eb36ad4e26287bebc65b)

## 

​

Import private models

If you want to import private models from Hugging Face or Civitai, you need to configure your API keys first.

### 

​

1\. Generate your API keys

First, you need to generate API keys from the respective platforms:

  * Civitai

  * Hugging Face




  1. Log in to Civitai and visit <https://civitai.com/user/account>.
  2. Generate your API key in the account settings. ![Civitai API Key](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=50e93b8937fe90a70f7aec140db65d30)



  1. Visit <https://huggingface.co/settings/tokens>.
  2. Generate your API token. ![Hugging Face API Key](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=32729b7a20a9ebe16d546c4836b92b49)
  3. Make sure your token has read access to the repositories containing the private models you want to import. ![Hugging Face Token Permissions](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=2ae808aa8052e3cc98e8d91b5fde551c)



### 

​

2\. Save your API keys

  1. Go to [Comfy Cloud Settings](https://cloud.comfy.org) and navigate to the **Secrets** section.

![Settings Secrets](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=15ea8a8aeeb50da9bedc00429c9c05b1)

  2. Click to add your API keys (you can name the key anything you like):

![Add Secret Key](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=b87a3c87203a4e3929ae41295281a823)

  3. Make sure your API keys have access permissions to the private models you want to import.



### 

​

3\. Import the private model

Once your API keys are configured, you can import private models using the same process as public models:

  1. Get the model link from Hugging Face or Civitai.
  2. Paste the link in the import modal.
  3. The system will automatically use your saved API keys to access the private model.



Make sure your API key has the necessary permissions to access the specific private model you want to import.

## 

​

FAQ

Are there restrictions on what models I can upload?

Yes. Only **safetensor** file types are supported. There is effectively no file size limit (up to 100GB).

Are the models I upload private or shared with everyone?

Models you import are **private to you**. Only you can see the models in your library.

Can I upload my own custom models from my local hard drive?

Currently, you need to upload the model to a **public Hugging Face or Civitai repository** first, then import from those platforms.

Can I upload chunked model files?

No. You will need to combine chunked model files into one file before importing.

Is this feature included in my current cloud subscription?

This feature is available for **Creator** and **Pro** plans only.

Is this feature accessible on the Desktop or portable versions of Comfy?

No. This is a **Cloud-only** feature.

Can I delete a model that I uploaded?

Yes. You can delete models you imported. Note that models uploaded by the Comfy internal team cannot be deleted.

What model types can I import (BYOM)?

Not only the examples below. BYOM supports any model folder that Comfy Cloud lists in the **import type selector** during import. That list comes from Comfy Cloud’s supported ComfyUI model folders and is the source of truth.In practice, if ComfyUI treats a file as a model weight (checkpoint, LoRA, VAE, ControlNet, embedding, upscaler, IP-Adapter, SAM, audio encoder, and similar), you can import it as long as the folder appears in that selector.Common examples:

  * **Checkpoints and UNets** : `checkpoints`, `diffusion_models`
  * **LoRAs and adapters** : `loras`, `animatediff_motion_lora`, `cogvideox_loras`, and similar adapter folders
  * **VAE** : `vae`, `vae_approx`
  * **ControlNet** : `controlnet`
  * **CLIP and text encoders** : `clip_vision`, `text_encoders`
  * **Embeddings / textual inversion** : `embeddings` (reference in `CLIPTextEncode` prompts with `embedding:my-embedding-name`)
  * **Upscalers** : `upscale_models`, `latent_upscale_models`
  * **Vision / segmentation / removal** : `ipadapter`, `gligen`, `sams`, `sam3`, `rmbg`, `ultralytics_bbox`, `ultralytics_segm`
  * **Other folders in the selector** : `audio_encoders`, `model_patches`, `style_models`, `photomaker`, `LLM`, `CogVideo`, and more

What actually limits import is not the model category, but these rules:

  * **File format** : `.safetensors` only (even if ComfyUI locally supports `.ckpt`, `.pth`, or `.onnx` for that folder)
  * **Source** : Civitai or Hugging Face download links only (no direct local upload)
  * **Blocked folder** : `nlf` models cannot be imported



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/cloud/import-models.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/cloud/import-models)

[Share workflowsPrevious](https://docs.comfy.org/cloud/share-workflow)[ComfyUI Text to Image WorkflowNext](https://docs.comfy.org/tutorials/basic/text-to-image)

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
