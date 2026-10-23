---
url: https://docs.comfy.org/built-in-nodes/SAM3_TrackToMask/
title: SAM3_TrackToMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:07.540802+00:00
---

# SAM3_TrackToMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3_TrackToMask/

Detection

# SAM3_TrackToMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

Selects specific tracked objects from a SAM3 tracking session by their index numbers and combines them into a single output mask.

Copy pageCopy page

## 

​

Overview

Selects specific tracked objects from a SAM3 tracking session by their index numbers and combines them into a single output mask. This allows you to choose which objects to keep and which to ignore from the tracking results.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`track_data`| The tracking data output from a SAM3 tracker node, containing the packed masks and original image size.| SAM3TRACKDATA| Yes| N/A  
`object_indices`| Comma-separated object indices to include in the output mask (e.g., ‘0,2,3’). If left empty, all tracked objects are included.| STRING| No| Any comma-separated list of integers  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`masks`| A single binary mask for each frame, where selected objects are combined into one mask. If no objects are selected or no tracking data exists, returns a zero mask.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/en.md)

* * *

**Source fingerprint (SHA-256):** `77c9f5142f2078fabb81e58979df01ad9ec41d3de953939570bebb4f2687f8ad`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3_TrackToMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3_TrackToMask)

[SAM3_TrackPreview - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SAM3_TrackPreview)[SAM3_VideoTrack - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3_VideoTrack)

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
