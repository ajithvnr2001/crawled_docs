---
url: https://docs.comfy.org/built-in-nodes/WebcamCapture/
title: Webcam Capture - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:40.750954+00:00
---

# Webcam Capture - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WebcamCapture/

Image

# Webcam Capture - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WebcamCapture node captures images from a webcam device and converts them into a format that can be used within ComfyUI workflows.

Copy pageCopy page

The WebcamCapture node captures images from a webcam device and converts them into a format that can be used within ComfyUI workflows. It inherits from the LoadImage node and provides options to control the capture dimensions and timing. When enabled, the node can capture new images each time the workflow queue is processed.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The webcam input source to capture images from| WEBCAM| Yes| -  
`width`| The desired width for the captured image (default: 0, uses webcam’s native resolution)| INT| Yes| 0 to MAX_RESOLUTION  
`height`| The desired height for the captured image (default: 0, uses webcam’s native resolution)| INT| Yes| 0 to MAX_RESOLUTION  
`capture_on_queue`| When enabled, captures a new image each time the workflow queue is processed (default: True)| BOOLEAN| Yes| -  
  
**Note:** When both `width` and `height` are set to 0, the node uses the webcam’s native resolution. Setting either dimension to a non-zero value will resize the captured image accordingly.

## Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The captured webcam image converted to ComfyUI’s image format| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/en.md)

* * *

**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WebcamCapture.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WebcamCapture)

[Save SVG](https://docs.comfy.org/built-in-nodes/SaveSVGNode)[TrimVideoLatent](https://docs.comfy.org/built-in-nodes/latent/video/trim-video-latent)
