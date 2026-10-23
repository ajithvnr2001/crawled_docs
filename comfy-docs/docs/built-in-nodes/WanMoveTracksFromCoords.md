---
url: https://docs.comfy.org/built-in-nodes/WanMoveTracksFromCoords/
title: WanMoveTracksFromCoords - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:24.650018+00:00
---

# WanMoveTracksFromCoords - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanMoveTracksFromCoords/

Move

# WanMoveTracksFromCoords - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanMoveTracksFromCoords node creates motion tracks from a JSON-formatted string of coordinates.

Copy pageCopy page

The WanMoveTracksFromCoords node creates motion tracks from a JSON-formatted string of coordinates. It converts the coordinate data into a track format that can be used by other video processing nodes, and can optionally apply a mask to control the visibility of the tracks over time.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`track_coords`| A JSON-formatted string containing the coordinate data for the tracks. The default value is an empty list (`"[]"`). This input is a forced input, so it must be connected in the UI.| STRING| No| N/A  
`track_mask`| An optional mask. When provided, the node uses it to determine the visibility of tracks per frame: tracks are visible in frames where the mask contains any nonzero pixel. When not provided, all tracks are visible in all frames.| MASK| No| N/A  
  
**Note:** The `track_coords` input expects a specific JSON structure. It should be a list of tracks, where each track is a list of frames, and each frame is an object with `x` and `y` coordinates. The number of frames must be consistent across all tracks, and at least one track must be provided.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`tracks`| The generated track data, containing the path coordinates and visibility information for each track.| TRACKS  
`track_length`| The total number of frames in the generated tracks.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/en.md)

* * *

**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanMoveTracksFromCoords.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanMoveTracksFromCoords)

[WanMoveConcatTrack - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanMoveConcatTrack)[WanMoveTrackToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanMoveTrackToVideo)

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
