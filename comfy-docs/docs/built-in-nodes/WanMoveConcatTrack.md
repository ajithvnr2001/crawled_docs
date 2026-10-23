---
url: https://docs.comfy.org/built-in-nodes/WanMoveConcatTrack/
title: WanMoveConcatTrack - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:24.768183+00:00
---

# WanMoveConcatTrack - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanMoveConcatTrack/

Move

# WanMoveConcatTrack - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanMoveConcatTrack node combines two sets of motion tracking data into a single, longer sequence.

Copy pageCopy page

The WanMoveConcatTrack node combines two sets of motion tracking data into a single, longer sequence. It works by joining the track paths and visibility masks from the input tracks along their respective dimensions. If only one track input is provided, it simply passes that data through unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`tracks_1`| The first set of motion tracking data to be concatenated.| TRACKS| Yes|   
`tracks_2`| An optional second set of motion tracking data. If not provided, `tracks_1` is passed directly to the output.| TRACKS| No|   
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`tracks`| The concatenated motion tracking data, containing the combined `track_path` and `track_visibility` from the inputs. Returns `tracks_1` unchanged when `tracks_2` is not connected.| TRACKS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/en.md)

* * *

**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanMoveConcatTrack.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanMoveConcatTrack)

[GenerateTracks - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GenerateTracks)[WanMoveTracksFromCoords - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanMoveTracksFromCoords)

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
