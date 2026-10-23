---
url: https://docs.comfy.org/built-in-nodes/SAM3_VideoTrack/
title: SAM3_VideoTrack - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.102614+00:00
---

# SAM3_VideoTrack - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3_VideoTrack/

Detection

# SAM3_VideoTrack - ComfyUI Built-in Node Documentation

Copy pageCopy page

Track objects across video frames using SAM3’s memory-based tracker.

Copy pageCopy page

Track objects across video frames using SAM3’s memory-based tracker. The node processes a sequence of video frames and maintains object identities across frames, using either initial masks or text prompts to define what to track, and can detect new objects along the way using text conditioning.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Video frames as batched images| IMAGE| Yes| Batched video frames  
`model`| The SAM3 model to use for tracking| MODEL| Yes| SAM3 model  
`initial_mask`| Mask(s) for the first frame to track (one per object)| MASK| No| One mask per object  
`conditioning`| Text conditioning for detecting new objects during tracking| CONDITIONING| No| Text conditioning  
`detection_threshold`| Score threshold for text-prompted detection (default: 0.5)| FLOAT| No| 0.0 to 1.0 (step 0.01)  
`max_objects`| Max tracked objects. Initial masks count toward this limit. 0 uses the internal cap of 64. (default: 4)| INT| No| 0 to 64  
`detect_interval`| Run detection every N frames (1=every frame). Higher values save compute. (default: 1)| INT| No| 1 or higher  
  
**Note:** Either `initial_mask` or `conditioning` must be provided. If both are omitted, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`track_data`| Tracking data containing object masks and metadata across all video frames| SAM3_TRACK_DATA  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/en.md)

* * *

**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3_VideoTrack.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3_VideoTrack)

[SAM3_TrackToMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SAM3_TrackToMask)[SAM3DBody_FaceExpression - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3DBody_FaceExpression)

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
