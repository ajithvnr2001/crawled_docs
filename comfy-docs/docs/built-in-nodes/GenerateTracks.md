---
url: https://docs.comfy.org/built-in-nodes/GenerateTracks/
title: GenerateTracks - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:00.389787+00:00
---

# GenerateTracks - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GenerateTracks/

Move

# GenerateTracks - ComfyUI Built-in Node Documentation

Copy pageCopy page

The GenerateTracks node creates multiple parallel motion paths (tracks) for video generation.

Copy pageCopy page

The `GenerateTracks` node creates multiple parallel motion paths (tracks) for video generation. It defines a main path from a start position to an end position, then generates a set of tracks that run parallel to this path, spaced evenly apart. You can control the shape of the path (straight line or Bezier curve), the speed of movement along it, and which frames the tracks are visible in.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the video frame in pixels. The default value is 832.| INT| Yes| 16 - 4096  
`height`| The height of the video frame in pixels. The default value is 480.| INT| Yes| 16 - 4096  
`start_x`| Normalized X coordinate (0-1) for start position. The default value is 0.0.| FLOAT| Yes| 0.0 - 1.0  
`start_y`| Normalized Y coordinate (0-1) for start position. The default value is 0.0.| FLOAT| Yes| 0.0 - 1.0  
`end_x`| Normalized X coordinate (0-1) for end position. The default value is 1.0.| FLOAT| Yes| 0.0 - 1.0  
`end_y`| Normalized Y coordinate (0-1) for end position. The default value is 1.0.| FLOAT| Yes| 0.0 - 1.0  
`num_frames`| The total number of frames for which to generate track positions. The default value is 81.| INT| Yes| 1 - 1024  
`num_tracks`| The number of parallel tracks to generate. The default value is 5.| INT| Yes| 1 - 100  
`track_spread`| Normalized distance between tracks. Tracks are spread perpendicular to the motion direction. The default value is 0.025.| FLOAT| Yes| 0.0 - 1.0  
`bezier`| Enable Bezier curve path using the mid point as control point. The default value is False.| BOOLEAN| Yes| True / False  
`mid_x`| Normalized X control point for Bezier curve. Only used when ‘bezier’ is enabled. The default value is 0.5.| FLOAT| Yes| 0.0 - 1.0  
`mid_y`| Normalized Y control point for Bezier curve. Only used when ‘bezier’ is enabled. The default value is 0.5.| FLOAT| Yes| 0.0 - 1.0  
`interpolation`| Controls the timing/speed of movement along the path (default: “linear”):  
“linear” - constant speed  
”ease_in” - starts slow and speeds up  
”ease_out” - starts fast and slows down  
”ease_in_out” - smooth acceleration and deceleration  
”constant” - keeps all positions at the start point| COMBO| Yes| `"linear"`  
`"ease_in"`  
`"ease_out"`  
`"ease_in_out"`  
`"constant"`  
`track_mask`| Optional mask to indicate visible frames. If provided, frames where the mask has any nonzero pixel are marked as visible for all tracks.| MASK| No| -  
  
**Note:** The `mid_x` and `mid_y` parameters are only used when the `bezier` parameter is set to `True`. When `bezier` is `False`, the path is a straight line from the start to the end point.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`TRACKS`| A tracks object containing the generated path coordinates and visibility information for all tracks across all frames.| TRACKS  
`track_length`| The number of frames for which tracks were generated, matching the input `num_frames`.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/en.md)

* * *

**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GenerateTracks.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GenerateTracks)

[WanInfiniteTalkToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanInfiniteTalkToVideo)[WanMoveConcatTrack - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanMoveConcatTrack)

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
