---
url: https://docs.comfy.org/built-in-nodes/WanMoveVisualizeTracks/
title: WanMoveVisualizeTracks - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:25.429702+00:00
---

# WanMoveVisualizeTracks - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanMoveVisualizeTracks/

Move

# WanMoveVisualizeTracks - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanMoveVisualizeTracks node overlays motion tracking data onto a sequence of images or video frames.

Copy pageCopy page

The WanMoveVisualizeTracks node overlays motion tracking data onto a sequence of images or video frames. It draws visual representations of tracked points, including their movement paths and current positions, making the motion data visible and easier to analyze.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The sequence of input images or video frames to visualize the tracks on.| IMAGE| Yes| -  
`tracks`| The motion tracking data containing point paths and visibility information. If not provided, the input images are passed through unchanged.| TRACKS| No| -  
`line_resolution`| The number of previous frames to use when drawing the trailing path line for each track (default: 24).| INT| Yes| 1 - 1024  
`circle_size`| The size of the circle drawn at the current position of each track (default: 12). Marked as an advanced parameter.| INT| Yes| 1 - 128  
`opacity`| The opacity of the drawn track overlays (default: 0.75).| FLOAT| Yes| 0.0 - 1.0  
`line_width`| The width of the lines used to draw the track paths (default: 16). Marked as an advanced parameter.| INT| Yes| 1 - 128  
  
**Note:** If the number of input images does not match the number of frames in the provided `tracks` data, the image sequence will be repeated to match the track length. **Note:** Track points are drawn with a limited set of repeating colors, and a point is skipped in a frame when its visibility flag is zero for that frame.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The sequence of images with the motion tracking data visualized as overlays. If no `tracks` were provided, the original input images are returned.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/en.md)

* * *

**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanMoveVisualizeTracks.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanMoveVisualizeTracks)

[WanMoveTrackToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanMoveTrackToVideo)[WanTrackToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanTrackToVideo)

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
