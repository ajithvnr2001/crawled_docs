---
url: https://docs.comfy.org/built-in-nodes/SCAIL2ColoredMask/
title: SCAIL2ColoredMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:54.722340+00:00
---

# SCAIL2ColoredMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SCAIL2ColoredMask/

Scail

# SCAIL2ColoredMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node renders SAM3 tracking data into colored masks that are consumed by the WanSCAILToVideo node.

Copy pageCopy page

This node renders SAM3 tracking data into colored masks that are consumed by the WanSCAILToVideo node. It processes tracking data from a driving pose video and optionally a reference image, assigning consistent colors to each tracked person across both outputs.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`driving_track_data`| SAM3 track of the driving pose video. Will be rendered into the pose_video_mask output.| SAM3_TRACK_DATA| Yes| -  
`ref_track_data`| SAM3 track of the reference image(s) (one identity per object, colored in batch order), or a plain MASK of the reference subject (rendered as a single identity).| SAM3_TRACK_DATA or MASK| No| -  
`object_indices`| Comma-separated list of person indices to include (e.g. ‘0,2,3’). Applied to both reference and pose video masks. Empty = all. (default: "")| STRING| Yes| -  
`sort_by`| Order in which palette colors are assigned to the tracked objects (applied to both reference and pose video so each identity keeps the same color). Objects that appear in earlier frames always come first; within a frame, left_to_right = leftmost object (by centroid at first appearance) gets the first color, area = biggest object (by mask area at first appearance) gets the first color; none = keep SAM3’s order. (default: “left_to_right”)| COMBO| Yes| `"none"`  
`"left_to_right"`  
`"area"`  
`replacement_mode`| False = Animation Mode (pose_video_mask has black background, reference_image_mask has white background). True = Replacement Mode (pose_video_mask has white background, reference_image_mask has black background). (default: False)| BOOLEAN| Yes| False  
True  
  
Note: `object_indices` only accepts comma-separated digits; non-numeric entries and out-of-range indices are ignored. When `ref_track_data` is not provided, the `reference_image_mask` output is a solid fill using the reference background color (white in Animation Mode, black in Replacement Mode).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`pose_video_mask`| Colored mask rendered from the driving pose video tracking data. Background color follows replacement_mode setting.| IMAGE  
`reference_image_mask`| Colored mask rendered from the reference image tracking data. Background is black in Replacement Mode, white in Animation Mode. If no reference data is provided, returns a solid fill matching the reference background color.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/en.md)

* * *

**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SCAIL2ColoredMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SCAIL2ColoredMask)

[WanPhantomSubjectToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanPhantomSubjectToVideo)[WanSCAILToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanSCAILToVideo)

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
