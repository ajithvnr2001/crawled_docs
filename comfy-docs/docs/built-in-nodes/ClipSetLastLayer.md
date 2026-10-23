---
url: https://docs.comfy.org/built-in-nodes/ClipSetLastLayer/
title: CLIPSetLastLayer - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:35.708592+00:00
---

# CLIPSetLastLayer - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipSetLastLayer/

Conditioning

# CLIPSetLastLayer - ComfyUI Built-in Node Documentation

Copy pageCopy page

CLIP Set Last Layer is a core node in ComfyUI for controlling the processing depth of CLIP models.

Copy pageCopy page

`CLIP Set Last Layer` is a core node in ComfyUI for controlling the processing depth of CLIP models. It allows users to precisely control where the CLIP text encoder stops processing, affecting both the depth of text understanding and the style of generated images. The original CLIP model is left unchanged: the node works on a copy and returns the modified copy.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model to be modified| CLIP| Yes| -  
`stop_at_clip_layer`| Specifies which layer to stop at. A value of -1 uses all layers, while -24 uses only the first layer (default: -1). This is an advanced parameter.| INT| Yes| -24 to -1 (step: 1)  
  
The values are negative and count backwards from the end of the model: -1 refers to the last (deepest) layer and -24 to the first (shallowest) layer, which is why the allowed range only covers -24 through -1.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`clip`| The modified CLIP model (a clone of the input; the original CLIP model is not changed) with the specified layer set as the last one| CLIP  
  
## 

​

Why Set the Last Layer

  * **Performance Optimization** : Like not needing a PhD to understand simple sentences, sometimes shallow understanding is enough and faster
  * **Style Control** : Different levels of understanding produce different artistic styles
  * **Compatibility** : Some models might perform better at specific layers

Imagine the CLIP model as a 24-layer intelligent brain:

  * Shallow layers (1-8): Recognize basic letters and words
  * Middle layers (9-16): Understand grammar and sentence structure
  * Deep layers (17-24): Grasp abstract concepts and complex semantics

`CLIP Set Last Layer` works like a **“thinking depth controller”** :

  * -1: Use all 24 layers (complete understanding)
  * -2: Stop at layer 23 (slightly simplified)
  * -12: Stop at layer 13 (medium understanding)
  * -24: Use only layer 1 (basic understanding)



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSetLastLayer/en.md)

* * *

**Source fingerprint (SHA-256):** `41a7feb9729dbb2a987a15a53c56641eae2a5611db8762ef2ce14b58970752fe`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipSetLastLayer.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipSetLastLayer)

[AudioEncoderEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AudioEncoderEncode)[CLIPTextEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipTextEncode)

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
