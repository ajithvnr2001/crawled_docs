---
url: https://docs.comfy.org/tutorials/partner-nodes/beeble/beeble-switchx/
title: Beeble SwitchX in ComfyUI: Relighting and Environment Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:25.738824+00:00
---

# Beeble SwitchX in ComfyUI: Relighting and Environment Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/beeble/beeble-switchx/

## On this page

  * What Beeble SwitchX is good at
  * Beeble SwitchX: Image Edit
    * How It Works
    * Steps to Run
    * Node Parameters
  * Beeble SwitchX: Video Edit
    * How It Works
    * Steps to Run
    * Outputs



Beeble

# Beeble SwitchX in ComfyUI: Relighting and Environment Editing

Copy pageCopy page

Relight images and videos with Beeble SwitchX in ComfyUI: replace backgrounds, composite a subject into a new scene, and export cutouts or alpha mattes.

Copy pageCopy page

The [Beeble SwitchX](https://docs.comfy.org/built-in-nodes/BeebleSwitchXImageEdit) Partner Nodes allow you to transform the environment, lighting, and style of existing images and videos while preserving the original subject. Upload a character or subject image along with a reference environment, and SwitchX composites your subject into the new scene with realistic lighting and shadows.

## 

​

What Beeble SwitchX is good at

  * **Environment replacement** : Replaces the background environment of an image or video with a reference scene while preserving the original subject
  * **Realistic relighting** : Composites the subject into the new environment with proper lighting, shadows, and perspective
  * **Video editing with motion preserved** : Applies relighting to masked subject regions in a video while unmasked areas keep the original pixels and motion
  * **Compositing-ready outputs** : The image workflow saves a masked cutout, and the video workflow generates a separate alpha matte for easy compositing



To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

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

Beeble SwitchX: Image Edit

Replace the background environment and relight your subject with a reference image. ![Beeble SwitchX Image Edit Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Beeble SwitchX: Image Edit” in Template Library

### 

​

How It Works

This workflow takes two input images:

  * **Subject image** : your character or main subject (with background)
  * **Reference environment** : the new scene, lighting, or style you want to apply

The node generates an output where the subject is naturally composited into the new environment with proper lighting, shadows, and perspective.

### 

​

Steps to Run

  1. **Upload subject image** : use the first **LoadImage** node to load your subject image (e.g., a person wearing headphones)
  2. **Upload reference image** : use the second **LoadImage** node to load the target environment or style
  3. **Enter your prompt** : describe the scene in the **BeebleSwitchXImageEdit** node
  4. **Set resolution** : choose output resolution
  5. **Adjust seed** : modify the seed for different results
  6. **Click Queue** : press `Ctrl+Enter` to generate
  7. **View results** : the edited image appears in **SaveImage** , and a masked cutout is saved separately



### 

​

Node Parameters

Parameter| Description  
---|---  
`prompt`| Description of the scene and environment  
`resolution`| Output resolution (e.g., 720p)  
`seed`| Random seed for reproducible results  
  
## 

​

Beeble SwitchX: Video Edit

Apply environment relighting to a video while preserving the original motion and unmasked regions. ![Beeble SwitchX Video Edit Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_video_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Beeble SwitchX: Video Edit” in Template Library

### 

​

How It Works

This workflow takes a source video and a reference image, then applies the reference lighting and environment to the masked subject regions in the video. Unmasked areas preserve the original pixels and motion. The workflow also generates an alpha matte for easy compositing.

### 

​

Steps to Run

  1. **Upload source video** : use the **LoadVideo** node to load your input video
  2. **Upload reference image** : use the **LoadImage** node to load the target environment/style
  3. **Set video range** : the **Video Slice** node controls which frames to process (start, end, inclusive)
  4. **Enter your prompt** : describe the desired environment and lighting in the **BeebleSwitchXVideoEdit** node
  5. **Set resolution** : choose output resolution
  6. **Adjust seed** : modify the seed for different results
  7. **Click Queue** : press `Ctrl+Enter`
  8. **View results** : the edited video is saved, and a separate alpha matte video is generated for compositing



### 

​

Outputs

Output| Description  
---|---  
**Edited video** (`SaveVideo`)| The final video with new environment/lighting applied to masked regions  
**Alpha matte** (`SaveVideo`)| A separate alpha video for compositing the edited regions  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/beeble/beeble-switchx.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/beeble/beeble-switchx)

[FLUX 3 Image in ComfyUI: Text to Image and Image EditPrevious](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-image)[Bria Background Removal in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/bria/background-removal)

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
