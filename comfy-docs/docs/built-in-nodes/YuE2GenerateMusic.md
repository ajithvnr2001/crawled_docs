---
url: https://docs.comfy.org/built-in-nodes/YuE2GenerateMusic/
title: YuE2GenerateMusic - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:27.149010+00:00
---

# YuE2GenerateMusic - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/YuE2GenerateMusic/

Yue2

# YuE2GenerateMusic - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates music tokens and acoustic conditioning from a style, lyrics, and an ABC notation.

Copy pageCopy page

Generates music tokens and acoustic conditioning from a style, lyrics, and an ABC notation. It returns the conditioning and the generated duration in seconds, which should be provided to the Empty YuE2 Latent Audio node. If the ABC input is left empty, the selected mode is ignored and off mode is used automatically.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used to tokenize and encode the music inputs.| CLIP| Yes| -  
`style`| Text describing the musical style. Supports multiline input and dynamic prompts.| STRING| Yes| Multiline text  
`lyrics`| Lyrics for the generated music. Supports multiline input and dynamic prompts.| STRING| Yes| Multiline text  
`abc`| Connect the ABC generator or supply an edited score. Leave empty to use off mode automatically. default: ""| STRING| Yes| Multiline text  
`seed`| Random seed for generation. default: 0| INT| Yes| 0 to 18446744073709551615  
`mode`| full: generates melody and chords; melody: generates melody only, recommended for covers. default: “full”| COMBO| Yes| ”full"  
"melody”  
`max_duration`| Maximum duration in seconds. Automatically reduced for long prompts; generation can stop earlier. default: 360.0| FLOAT| Yes| 0.04 to 900.0  
`temperature`| Sampling temperature for generation. default: 1.0 (advanced)| FLOAT| Yes| 0.0 to 5.0  
`top_p`| Nucleus sampling probability threshold. default: 0.95 (advanced)| FLOAT| Yes| 0.01 to 1.0  
`top_k`| Top-k sampling limit. default: 100 (advanced)| INT| Yes| 1 to 32768  
`repetition_penalty`| Penalty applied to repeated tokens. default: 1.2 (advanced)| FLOAT| Yes| 0.01 to 10.0  
`cfg_scale`| Autoregressive guidance for style and lyrics. 1.0 disables CFG, matching the ABC workflow. Use 1.01 to match the original off-mode guidance. default: 1.0 (advanced, optional)| FLOAT| No| 0.0 to 100.0  
  
Note: If `abc` is empty or contains only whitespace, the `mode` selection is ignored and off mode is used automatically.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| Acoustic conditioning generated from the music tokens.| CONDITIONING  
`seconds`| The generated audio duration in seconds. Provide this value to the Empty YuE2 Latent Audio node.| FLOAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/en.md)

* * *

**Source fingerprint (SHA-256):** `5a88e185d2998c51acff7f0c76c8c35ca30b80b88cb541d97f9ab91566b5a3ed`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/YuE2GenerateMusic.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/YuE2GenerateMusic)

[YuE2GenerateABC - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/YuE2GenerateABC)[TextEncodeZImageOmni - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeZImageOmni)

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
