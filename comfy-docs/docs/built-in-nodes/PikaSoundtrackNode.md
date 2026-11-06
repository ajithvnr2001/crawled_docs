---
url: https://docs.comfy.org/built-in-nodes/PikaSoundtrackNode/
title: PikaSoundtrackNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:52.915272+00:00
---

# PikaSoundtrackNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PikaSoundtrackNode/

Video

# PikaSoundtrackNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a synchronized soundtrack for a video with Pika.

Copy pageCopy page

This node generates a synchronized soundtrack for a video with Pika. The picture and the length are kept; only the audio is replaced. Describe the sound you want, or leave the instruction empty to derive it from the picture.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The clip to write a soundtrack for. Up to 10 minutes.| VIDEO| Yes| -  
`instruction`| What the audio should be: sound effects, ambience, music or style. Leave empty to derive it from the picture. Default: "" (empty string).| STRING| Yes| 0 to 10000 characters  
`seed`| Seed for sampling. Default: 42.| INT| Yes| 0 to 2147483647  
  
**Constraints:**

  * The input video must be 10 minutes or shorter.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The input clip with the generated soundtrack in place of the original audio.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSoundtrackNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9820efec607ba52dbabe5e4fb0862240fb0f0215ce7e72914451823b7e75120b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PikaSoundtrackNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PikaSoundtrackNode)

[PikaH3FlexVideoNode](https://docs.comfy.org/built-in-nodes/PikaH3FlexVideoNode)[VEED Dubbing](https://docs.comfy.org/built-in-nodes/VeedDubbingNode)
