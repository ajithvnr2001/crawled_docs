---
url: https://docs.comfy.org/built-in-nodes/ReferenceTimbreAudio/
title: ReferenceTimbreAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:52.579992+00:00
---

# ReferenceTimbreAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ReferenceTimbreAudio/

Conditioning

# ReferenceTimbreAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node sets the reference audio for the “ace step 1.5” process.

Copy pageCopy page

This node sets the reference audio for the “ace step 1.5” process. It takes a conditioning input and optionally a latent representation of audio, then attaches that latent data to the conditioning so later nodes can use it as reference audio timbre latents. This node is marked as experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`conditioning`| The conditioning data to which the reference audio information will be attached.| CONDITIONING| Yes|   
`latent`| An optional latent representation of the reference audio (default: None). When provided, its samples are appended to the conditioning as reference audio timbre latents.| LATENT| No|   
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The modified conditioning data, now containing the reference audio timbre latents if the optional `latent` input was provided.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ReferenceTimbreAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ReferenceTimbreAudio)

[ReferenceMultiLatent](https://docs.comfy.org/built-in-nodes/ReferenceMultiLatent)[SaveConditioning](https://docs.comfy.org/built-in-nodes/SaveConditioning)
