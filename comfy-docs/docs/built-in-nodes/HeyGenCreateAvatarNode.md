---
url: https://docs.comfy.org/built-in-nodes/HeyGenCreateAvatarNode/
title: HeyGenCreateAvatarNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:03.155444+00:00
---

# HeyGenCreateAvatarNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HeyGenCreateAvatarNode/

Heygen

# HeyGenCreateAvatarNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Create a reusable HeyGen avatar from a photo of a person or from a text prompt describing a character to generate.

Copy pageCopy page

Create a reusable HeyGen avatar from a photo of a person or from a text prompt describing a character to generate. The resulting `avatar_id` can be used with the HeyGen Avatar Video node, and should be saved to reuse the avatar in future workflows.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`source`| Generate a new character from a text prompt, or create the avatar from a connected photo of a person.| DYNAMIC_COMBO| Yes| `"prompt"`  
`"photo"`  
  
### 

​

Prompt Inputs

Available when `source` is set to `"prompt"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Description of the avatar to generate (up to 1000 characters). Must contain at least 1 non-whitespace character. Default: empty string.| STRING| Yes| 1 to 1000 characters  
  
### 

​

Photo Inputs

Available when `source` is set to `"photo"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`identity_photo`| Photo of the person to turn into an avatar. Downscaled automatically if larger than 2K.| IMAGE| Yes| Single image  
  
### 

​

Reference Inputs

Available when `source` is set to `"prompt"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_images`| Growable slot: connect up to 3 images (`ref_image_1`…`ref_image_3`) guiding the generated look. Images are downscaled automatically if larger than 2K.| IMAGE| No| 0 to 3 images  
  
**Note:** The `source` parameter switches between two mutually exclusive modes. In `"prompt"` mode, `prompt` is required and up to 3 reference images can optionally be connected. In `"photo"` mode, `identity_photo` is required. Photos and reference images are downscaled automatically when larger than 2K; more than 3 reference images are not accepted.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`avatar_id`| Avatar look ID. Pass it to HeyGen Avatar Video’s `custom_avatar_id`; save it to reuse the avatar later.| STRING  
`preview`| Preview image of the generated avatar.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/en.md)

* * *

**Source fingerprint (SHA-256):** `3669686fc6d089909bd5d2d75292ceef05702ed3cc7b14e561bcb444c30a4e63`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HeyGenCreateAvatarNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HeyGenCreateAvatarNode)

[HeyGenAvatarVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HeyGenAvatarVideoNode)[HeyGenImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HeyGenImageToVideoNode)

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
