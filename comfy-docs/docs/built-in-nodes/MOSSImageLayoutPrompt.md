---
url: https://docs.comfy.org/built-in-nodes/MOSSImageLayoutPrompt/
title: MOSSImageLayoutPrompt - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:21.444168+00:00
---

# MOSSImageLayoutPrompt - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MOSSImageLayoutPrompt/

Moss Image

# MOSSImageLayoutPrompt - ComfyUI Built-in Node Documentation

Copy pageCopy page

Builds the layout prompt that MOSS-Image reads.

Copy pageCopy page

Builds the layout prompt that MOSS-Image reads. It takes the elements drawn in the Create Bounding Boxes node and emits a JSON layout with one entry per box: its label, its caption, and its rectangle in the pixel space of the target canvas. Set `width` and `height` to the size of the image you plan to generate, then connect the output to the prompt input of the text encoder. With no elements connected the prompt text is returned unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Description of the whole image. It becomes the caption of the layout.| STRING| Yes| -  
`element`| The elements to place, taken from the Create Bounding Boxes node. Each box contributes its caption; text boxes also contribute their text, and boxes that carry a color palette keep it.| ARRAY| Yes| -  
`width`| Width of the generated image in pixels. The boxes are converted into this pixel grid, so use the size of the image you plan to generate (default: 1024).| INT| Yes| 16 to 16384 (step 16)  
`height`| Height of the generated image in pixels. The boxes are converted into this pixel grid, so use the size of the image you plan to generate (default: 1024).| INT| Yes| 16 to 16384 (step 16)  
`character_boxes`| Numbers of the boxes to label as characters instead of objects, as tagged in the Create Bounding Boxes preview, for example “1, 3”. Every number in the string is read, so any separator works (default: empty).| STRING| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`prompt`| The layout prompt: a JSON object holding the caption, one entry per box, and the box coordinate format. The input text is passed through when no elements are connected.| STRING  
  
## 

​

Notes

Box rectangles arrive from Create Bounding Boxes as normalized coordinates between 0 and 1000 and are written to the layout in pixels relative to the center of the canvas, in `yxyx` order. The `width` and `height` values therefore have to match the image you generate, otherwise the boxes land in the wrong place. A box that holds text is always labeled as text, a box whose number is listed in `character_boxes` is labeled as a character, and every other box is labeled as an object.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageLayoutPrompt/en.md)

* * *

**Source fingerprint (SHA-256):** `da012a8d0dceaf6391110c90bd677d7929920d60fe961c00e5011b037206aa9a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MOSSImageLayoutPrompt.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MOSSImageLayoutPrompt)

[MiniMaxMusic3TextEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MiniMaxMusic3TextEncode)[PhotoMakerEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PhotoMakerEncode)

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
