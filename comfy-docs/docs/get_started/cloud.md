---
url: https://docs.comfy.org/get_started/cloud/
title: Comfy Cloud - Official ComfyUI Cloud Platform Powered by RTX 6000 Pro - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:56.254674+00:00
---

# Comfy Cloud - Official ComfyUI Cloud Platform Powered by RTX 6000 Pro - ComfyUI

> Source: https://docs.comfy.org/get_started/cloud/

## On this page

  * What is Comfy Cloud?
    * Key features
  * Cloud vs local
  * Pricing and subscription
  * Comfy Cloud firewall allowlist
  * How to use ComfyUI Cloud
  * Feedback
    * How to Stop/Exit Comfy Cloud
  * Frequently Asked Questions
  * Next steps



Get Started

# Comfy Cloud - Official ComfyUI Cloud Platform Powered by RTX 6000 Pro

Copy pageCopy page

Run ComfyUI workflows online with Comfy Cloud, the official cloud platform powered by NVIDIA RTX 6000 Pro GPUs. No local installation required.

Copy pageCopy page

## Access Comfy Cloud

Click here to access ComfyUI Cloud directly

## 

​

What is Comfy Cloud?

ComfyUI Cloud is the cloud version of ComfyUI with the same features as the local version. Everything is pre-installed and ready to use.

### 

​

Key features

## Zero setup

No installation required. All models and custom nodes are pre-installed and ready to use

## Powerful GPUs

Run workflows fast on our powerful server GPUs without needing your own hardware

## Always up-to-date

Automatically stays current with the latest ComfyUI releases and features

## Access anywhere

Use ComfyUI from any device with an internet connection - no local installation needed

## Team collaboration

Create team workspaces to collaborate with your team members. Share subscription plans, credits, and workflows.

## 

​

Cloud vs local

ComfyUI offers both an official cloud version, [Comfy Cloud](https://comfy.org/cloud), and an open-source self-hosted version. If you have a powerful GPU, running ComfyUI locally is a great option. The cloud version, on the other hand, is an online service that’s ready to use instantly—simply open the URL, no installation or setup required.

Category| Comfy Cloud| Self-hosted (local ComfyUI)  
---|---|---  
**Cost**|  Free tier and paid subscription plans| Free  
**GPU**|  Powerful Blackwell RTX 6000 Pros| Bring your own GPU  
**Technical Knowledge**|  No technical knowledge required.| While desktop and portable give you easy ways to get started, you’ll need to troubleshoot custom node installations and local installation issues.  
**Custom Nodes**|  Use pre-installed custom nodes and never worry about compatibility issues.| Install any custom node you want, but you’ll need to manage it yourself.  
**Models**|  Use pre-installed models. Import models from Civitai and Hugging Face.| Use any models you want, but you’ll need to download them first.  
**Notable Differences**|  Easy to onboard your team with [Workspaces](https://docs.comfy.org/cloud/workspace)| Works offline, infinitely customizable  
**Get started**| [Run ComfyUI Cloud](https://comfy.org/cloud)| [Install ComfyUI locally](https://docs.comfy.org/installation/system_requirements)  
  
## 

​

Pricing and subscription

## Check pricing

View pricing and subscription options for Comfy Cloud

## 

​

Comfy Cloud firewall allowlist

Allow outbound HTTPS and WebSocket traffic on TCP 443 to:

  * **App:** `cloud.comfy.org`, `api.comfy.org`, `cdn.comfy.org`
  * **Uploads and outputs:** `comfy-hub-assets.comfy.org`, `storage.googleapis.com`
  * **Sign-in:** `dreamboothy.firebaseapp.com`, `identitytoolkit.googleapis.com`, `securetoken.googleapis.com`, `apis.google.com`, `challenges.cloudflare.com`
  * **Other features:** `registry.comfy.org`, `*.algolia.net`, `media.comfy.org`



## 

​

How to use ComfyUI Cloud

Using ComfyUI Cloud is essentially the same as using your local ComfyUI. If this is your first time using ComfyUI, here are some quick tips to get started:

1

Select a template

Click the template icon in the left sidebar to browse available workflows.![Open workflow template](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a32875bb4e6d1c92ea4f893831aff925)

2

Select the workflow you want to run

Click on the template you want to run.![Select workflow template](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b16043c4ad9372834eb7fe49c1180eee)

3

Update template inputs

  1. In the loaded workflow, since we have pre-installed all models in the cloud version, all templates are ready to run immediately after loading.
  2. If you need to make updates, you only need to provide image inputs or text prompts. Check the `Load Image` node or `CLIP Text Encode` node. ![Check inputs](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=56ca79d24c79e666146c927263c96e99)



4

Run your workflow

If everything is correct, click the “Run” icon or use the shortcut “Ctrl + Enter” to run the workflow.![Run workflow](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=546f1e0003941deba2006a36d8f9ed34)

5

View output

After clicking run, our service will start allocating a machine for your workflow. You can check the execution status of the corresponding workflow in the queue panel.![View queue](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=4ac366407cf13fa84e55ef7948cff36e)

6

Save content locally

After the workflow execution is complete, you can save the generated content locally. Depending on the asset type, the save method is as follows:

  * Save images

  * Save videos

  * Save audio

  * Save 3D assets




In the queue panel or on the save image node, right-click on the generated image and select “Save image” to save the image locally.![Save image assets](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a15e70a3649537fb8c6adc50689dfbe7)

In the queue panel or on the save video node:

  1. Click the three dots on the browser player component to open the menu
  2. Select “Download” to save the video locally. ![Save video assets](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=2c987025c1c25e954a3065775ef5223d)



In the queue panel or on the save audio node:

  1. Click the three dots on the browser player component to open the menu
  2. Select “Download” to save the audio file locally. ![Save audio assets](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8d876d9c3b89b2ae9f1e84ba8b3e9887)



In the 3D browser node menu, select the “Export” option, choose the format you want to save, and the 3D file will be saved locally.![Save 3D assets](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5e121107826658a3e1725b8d9840d94b)

## 

​

Feedback

If you have any thoughts, suggestions, or run into any issues, simply click the “Feedback” icon. This will directly send your feedback to us. ![Feedback](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f1306e3587e441fc9964ffc0f9e4cc73)

### 

​

How to Stop/Exit Comfy Cloud

Cloud sessions only bill you while the GPU is actively running. When you close the browser tab, the session stops automatically — you can close it anytime, just like a regular browser tab.

## 

​

Frequently Asked Questions

## View FAQs

View frequently asked questions and answers about Comfy Cloud, including pricing, features, limitations, and more

## 

​

Next steps

## Cloud API

Programmatically run workflows via the Cloud API

## Tutorials

Explore tutorials to learn ComfyUI workflows

## Support

Join our Discord community for help

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/get_started/cloud.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/get_started/cloud)

[How to Update ComfyUIPrevious](https://docs.comfy.org/installation/update_comfyui)[How to Install Custom Nodes in ComfyUINext](https://docs.comfy.org/installation/install_custom_node)

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
