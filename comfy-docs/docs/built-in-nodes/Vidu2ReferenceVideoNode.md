---
url: https://docs.comfy.org/built-in-nodes/Vidu2ReferenceVideoNode/
title: Vidu2ReferenceVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:20.208566+00:00
---

# Vidu2ReferenceVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu2ReferenceVideoNode/

Vidu

# Vidu2ReferenceVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu2 Reference-to-Video Generation node creates a video from a text prompt and multiple reference images.

Copy pageCopy page

The Vidu2 Reference-to-Video Generation node creates a video from a text prompt and multiple reference images. You can define up to seven subjects, each with its own set of reference images, and reference them in the prompt using `@subject{subject_id}`. The node generates a video with configurable duration, aspect ratio, and movement.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for video generation.| COMBO| Yes| `"viduq2"`  
`subjects`| For each subject, provide up to 3 reference images (7 images total across all subjects). Reference them in prompts via `@subject{subject_id}`.| AUTOGROW| Yes| N/A  
`prompt`| The text description used to guide the video generation. When the `audio` parameter is enabled, the video will include generated speech and background music based on this prompt.| STRING| Yes| N/A  
`audio`| When enabled, the video will contain generated speech and background music based on the prompt (default: `False`).| BOOLEAN| No| N/A  
`duration`| The length of the generated video in seconds (default: `5`).| INT| No| 1 to 10  
`seed`| A number used to control the randomness of the generation for reproducible results (default: `1`).| INT| No| 0 to 2147483647  
`aspect_ratio`| The shape of the video frame.| COMBO| No| `"16:9"`  
`"9:16"`  
`"4:3"`  
`"3:4"`  
`"1:1"`  
`resolution`| The pixel resolution of the output video (default: `"720p"`).| COMBO| No| `"720p"`  
`"1080p"`  
`movement_amplitude`| Controls the movement amplitude of objects in the frame (default: `"auto"`).| COMBO| No| `"auto"`  
`"small"`  
`"medium"`  
`"large"`  
  
**Constraints:**

  * The `prompt` must be between 1 and 2000 characters long.
  * You can define multiple subjects, but the total number of reference images across all subjects must not exceed 7.
  * Each individual subject can have a maximum of 3 reference images.
  * Each reference image must have a width-to-height ratio between 1:4 and 4:1.
  * Each reference image must be at least 128 pixels in both width and height.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `da4b0a24e186f24cff8031c786bb765299b00bbfa13cc4161d53d3a68e466744`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu2ReferenceVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu2ReferenceVideoNode)

[Vidu2ImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu2ImageToVideoNode)[Vidu2StartEndToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu2StartEndToVideoNode)

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
