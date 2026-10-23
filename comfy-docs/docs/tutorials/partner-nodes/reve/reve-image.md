---
url: https://docs.comfy.org/tutorials/partner-nodes/reve/reve-image/
title: Reve Image in ComfyUI: Retired Partner Node Reference - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:07.419125+00:00
---

# Reve Image in ComfyUI: Retired Partner Node Reference - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/reve/reve-image/

## On this page

  * What Reve Image is good at
  * Example outputs
    * Reve: Text to Image
    * Example outputs
    * Reve: Image Edit
    * Example outputs
    * Reve: Image Remix And Edit
    * Example outputs
  * Get started
  * Available nodes



Reve

# Reve Image in ComfyUI: Retired Partner Node Reference

Copy pageCopy page

Reve discontinued its image service, so these Partner Nodes no longer run. This page keeps the archived text-to-image, edit, and remix workflows as reference.

Copy pageCopy page

Reve is no longer available: the provider has discontinued the Reve service. The Reve partner nodes have been retired and the workflows are archived for reference only. They can no longer be run on Comfy Cloud.

Reve is an image generation model available in ComfyUI through Partner Nodes. It supports text-to-image generation at up to **4K resolution** , image editing, and image remixing through three dedicated nodes.

## 

​

What Reve Image is good at

  * **Up to 4K resolution** : Generates sharp, detailed images at high resolutions
  * **Built-in aesthetic training** : Produces results suited for fashion editorial, cinematic, and natural lighting styles
  * **Image editing** : Modifies lighting conditions, color grading, and adds motion effects to existing images
  * **Image remixing** : Combines elements from reference images into a target image while preserving consistency



## 

​

Example outputs

Text-to-image generation with detailed aesthetics: ![Reve: Text to Image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_reve_image_create.png) Cinematic text-to-image work, here a fashion editorial portrait with dual-tone lighting: ![Fashion editorial portrait with dual-tone lighting](https://substack-post-media.s3.amazonaws.com/public/images/279c7067-7c65-4bb3-95ef-6d1ec934050b_2720x1536.png) 4K resolution output with fine detail preservation: ![Jaguar F-Type on a coastal trail at twilight](https://substack-post-media.s3.amazonaws.com/public/images/bf51794c-7044-4b1e-a5f1-1857ff78fb22_5440x3072.png) Image editing with text instructions: ![Reve: Image Edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_reve_image_edit.png) Image remixing, combining multiple reference images into a single output: ![Reve: Image Remix And Edit example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_reve_image_remix.png)

Reve is no longer available: the provider has discontinued the Reve service. The Reve partner nodes have been retired and the workflows below are archived for reference only.

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

### 

​

Reve: Text to Image

Input text prompts to generate high-quality images with detailed aesthetics and accurate text rendering. ![Reve: Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/archived/api_reve_image_create-1.webp)

## Download Workflow

Download JSON or search “Reve: Text to Image” in Template Library

**Example output** ![Reve: Text to Image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_reve_image_create.png)

### 

​

Example outputs

![Fashion editorial portrait with dual-tone lighting](https://substack-post-media.s3.amazonaws.com/public/images/279c7067-7c65-4bb3-95ef-6d1ec934050b_2720x1536.png)
    
    
    A high-fashion editorial portrait of a young East Asian model with long, straight black hair and thick bangs, crouched in a studio setting. She wears a minimalist, muted beige dress. The image features a cinematic dual-tone lighting setup, where the left side is washed in a soft greenish-yellow glow and the right side is cast in cool, muted blue-grey, creating a subtle color bleed effect. There is a slight motion blur, with the subject looking directly at the camera with a calm, neutral expression. High-end fashion magazine aesthetic, soft focus background, structured silhouette.
    

![Red sports car speeding through the night](https://substack-post-media.s3.amazonaws.com/public/images/5563d900-336c-42d0-b48c-6978883ae4ff_1360x768.png)
    
    
    A high-speed, cinematic capture of a vibrant red sports car speeding through the night. The camera angle is positioned near the rear-three-quarter view, emphasizing the sleek, metallic curves and the car's aerodynamic design. The entire background is transformed into a dramatic radial blur of brilliant yellow, orange, and white light streaks, suggesting extreme velocity. The car's surface reflects the warm ambient lights of the city, contrasting sharply with the deep, dark blue of the night sky.
    

![Woman with glowing orb and amber tones](https://substack-post-media.s3.amazonaws.com/public/images/fea68697-1783-4f84-99a7-3065b4df577c_2720x1536.png)
    
    
    A cinematic photograph of a woman with a bob haircut looking at her reflection in a mirror, her hands gently cradling a brilliant, glowing spherical white orb. The image is saturated in deep orange and amber tones, with heavy light leaks and lens flares washing out the center of the frame as the sphere radiates subtle, ethereal light. The composition features a soft, dreamy focus with significant analog film grain, creating a nostalgic atmosphere where the reflected face in the mirror appears slightly blurred and obscured by the warmth of the light leakage.
    

![Rally car drifting near a volcano](https://substack-post-media.s3.amazonaws.com/public/images/b73ad263-3045-4579-9e46-b6faaace9e5f_1360x768.png)
    
    
    A high-action, wide-angle nighttime shot of a legendary Audi Quattro rally car drifting through a barren rocky field at the base of a volcano. The car is coated in white and black. Powerful auxiliary spotlights on the front of the car cast a bright, warm glow, catching the thick dust kicked up by the aggressive tread of the tires. In the background, out-of-focus volcano spraying lava. The scene is cold and dark, with the intense light from the lava creating dramatic contrast.
    

The following examples demonstrate 4K resolution output with fine detail preservation: ![Jaguar F-Type on a coastal trail at twilight](https://substack-post-media.s3.amazonaws.com/public/images/bf51794c-7044-4b1e-a5f1-1857ff78fb22_5440x3072.png)
    
    
    A wide-angle landscape photograph of a solitary Jaguar F-Type car in British green, on a dirt trail facing a distant beach at twilight. The sky features dramatic long-exposure cloud streaks radiating from a low sun on the horizon. The foreground is dominated by jagged limestone rocks and blades of grass, leading the viewer's eye along a path that cuts through grassy hills toward the water. The lighting is cool and moody, casting deep shadows against the golden glow of the setting sun.
    

![White owl in a desert at golden hour](https://substack-post-media.s3.amazonaws.com/public/images/1af7e42a-aded-420b-b6b5-d2f96e5c5788_2720x1536.png)
    
    
    A minimalist wide shot of a vast white sand dune desert during golden hour. A white owl with its wings spread is in the foreground. Soft warm sunlight grazing the tops of the dunes, casting long shadows. Sparse, golden-brown desert shrubs are scattered across the ripples, with a prominent patch of dry, cracked, hexagonal mud in the bottom right foreground. In the far distance, a hazy, ethereal range of mountains rests against a pale, washed-out sky.
    

### 

​

Reve: Image Edit

Upload an image and provide text instructions to edit it. Generate a modified output image using Reve’s advanced editing model. ![Reve: Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/archived/api_reve_image_edit-1.webp)

## Download Workflow

Download JSON or search “Reve: Image Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## woman_running_in_field.png

`LoadImage` node 4 · `woman_running_in_field.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/woman_running_in_field.png)![Reve: Image Edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_reve_image_edit.png)

### 

​

Example outputs

![Motion blur edit example](https://substack-post-media.s3.amazonaws.com/public/images/1842aadb-ae80-45e7-be65-c6cc8e7aaea5_1024x1024.png)
    
    
    Add a cinematic horizontal streaks motion blur to the subject's body. The hand stays in clear focus.
    

![Lighting edit example](https://substack-post-media.s3.amazonaws.com/public/images/7cfec95f-40b0-4a09-9991-c37b6919155b_1920x1080.png)
    
    
    The lighting is cold, soft glow emits from the window.
    

![Side profile edit example](https://substack-post-media.s3.amazonaws.com/public/images/52617409-4c10-4944-985d-ee86b01bde05_1024x1024.png)
    
    
    Side profile shot of the subject, his hand is grabbing the sunglasses.
    

### 

​

Reve: Image Remix And Edit

Remix and edit images using Reve’s advanced model. Combine multiple reference images into a single output. ![Reve: Image Remix And Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/archived/api_reve_image_remix-1.webp)

## Download Workflow

Download JSON or search “Reve: Image Remix And Edit” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## iced_drink_cup.png

`LoadImage` node 2 · `iced_drink_cup.png`

## casual_male_portrait.png

`LoadImage` node 4 · `casual_male_portrait.png`

## japanese_street_alley.png

`LoadImage` node 5 · `japanese_street_alley.png`

**Example output** ![Reve: Image Remix And Edit example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_reve_image_remix.png)

### 

​

Example outputs

![Shadow transfer remix example](https://substack-post-media.s3.amazonaws.com/public/images/bc91f624-5d2f-47d9-8299-31e06e72fc59_1920x1080.png)
    
    
    Edit the shadows on the subject in image 1 to match the shadows from image 2.
    

![Color grading transfer remix example](https://substack-post-media.s3.amazonaws.com/public/images/87fc38a6-2cce-4de6-aa48-520fbdecff2a_1920x1080.png)
    
    
    Transfer the color grading and aesthetic from image 2 onto image 1.
    

## 

​

Get started

  1. **Update** ComfyUI to the latest version or visit [Comfy Cloud](https://cloud.comfy.org/?utm_source=docs).
  2. **Find** the Reve Image Create, Reve Image Remix, and Reve Image Edit nodes in the Node Library or Templates in the left sidebar.
  3. **Drop a node** on your canvas to begin.



## 

​

Available nodes

Node| Type| Description  
---|---|---  
**Reve Image Create**|  Text-to-Image| Generates images at up to 4K resolution from text prompts  
**Reve Image Edit**|  Image Edit| Modifies lighting, color grading, and motion in existing images  
**Reve Image Remix**|  Image Remix| Transfers visual properties from reference images to a target image  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/reve/reve-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/reve/reve-image)

[Recraft Text to Image in ComfyUI: Images with Preset StylesPrevious](https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-text-to-image)[Runway Image Generation in ComfyUI: Text-to-Image and Reference ImagesNext](https://docs.comfy.org/tutorials/partner-nodes/runway/image-generation)

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
