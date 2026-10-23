---
url: https://docs.comfy.org/built-in-nodes/WebcamCapture/
title: WebcamCapture - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.515106+00:00
---

# WebcamCapture - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WebcamCapture/

Image

# WebcamCapture - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WebcamCapture node captures images from a webcam device and converts them into a format that can be used within ComfyUI workflows.

Copy pageCopy page

The WebcamCapture node captures images from a webcam device and converts them into a format that can be used within ComfyUI workflows. It inherits from the LoadImage node and provides options to control the capture dimensions and timing. When enabled, the node can capture new images each time the workflow queue is processed.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The webcam input source to capture images from| WEBCAM| Yes| -  
`width`| The desired width for the captured image (default: 0, uses webcam’s native resolution)| INT| Yes| 0 to MAX_RESOLUTION  
`height`| The desired height for the captured image (default: 0, uses webcam’s native resolution)| INT| Yes| 0 to MAX_RESOLUTION  
`capture_on_queue`| When enabled, captures a new image each time the workflow queue is processed (default: True)| BOOLEAN| Yes| -  
  
**Note:** When both `width` and `height` are set to 0, the node uses the webcam’s native resolution. Setting either dimension to a non-zero value will resize the captured image accordingly.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The captured webcam image converted to ComfyUI’s image format| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/en.md)

* * *

**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WebcamCapture.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WebcamCapture)

[SaveSVGNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveSVGNode)[TrimVideoLatent NodeNext](https://docs.comfy.org/built-in-nodes/latent/video/trim-video-latent)

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
