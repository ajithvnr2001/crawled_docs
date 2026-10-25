---
url: https://docs.comfy.org/built-in-nodes/VeedFabricNode/
title: VeedFabricNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:47.602381+00:00
---

# VeedFabricNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VeedFabricNode/

Video

# VeedFabricNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Turn a still image and a speech track into a talking, lip-synced video with VEED Fabric.

Copy pageCopy page

Turn a still image and a speech track into a talking, lip-synced video with VEED Fabric. It works with photos, illustrations and mascots as long as the face is clearly visible; the video keeps the image’s aspect ratio and is as long as the audio.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use. Selecting a model reveals the parameters specific to it: `image`, `audio` and `resolution`.| DYNAMIC_COMBO| Yes| `"fabric-1.0"`  
`image`| Image with a clearly visible face. The video keeps its aspect ratio.| IMAGE| Yes| -  
`audio`| Speech to lip-sync to, up to 300 seconds. Sets the video length.| AUDIO| Yes| Up to 300 seconds  
`resolution`| Output size class: about 0.4 megapixels at `"480p"` (864x480 at 16:9) and 0.9 megapixels at `"720p"` (1312x736 at 16:9). (default: `"720p"`)| COMBO| Yes| `"480p"`  
`"720p"`  
  
The node stops with an error when the speech track is longer than 300 seconds.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The talking video: the input image animated to match the speech track.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/en.md)

* * *

**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VeedFabricNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VeedFabricNode)

[VeedCleanVideoAudioNode](https://docs.comfy.org/built-in-nodes/VeedCleanVideoAudioNode)[VeedLipsyncNode](https://docs.comfy.org/built-in-nodes/VeedLipsyncNode)
