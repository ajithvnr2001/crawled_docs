---
url: https://docs.comfy.org/built-in-nodes/RecraftTextToVectorNode/
title: RecraftTextToVectorNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.995376+00:00
---

# RecraftTextToVectorNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftTextToVectorNode/

Recraft

# RecraftTextToVectorNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates SVG vector illustrations synchronously based on a text prompt and resolution.

Copy pageCopy page

Generates SVG vector illustrations synchronously based on a text prompt and resolution. This node sends your prompt to the Recraft API and returns the generated SVG content.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the image generation. (default: "", maximum 1000 characters)| STRING| Yes| -  
`substyle`| The specific vector illustration style to use for generation.| COMBO| Yes| `"2d_character"`  
`"2d_gradient"`  
`"2d_illustration"`  
`"2d_flat_character"`  
`"2d_flat_illustration"`  
`"2d_art"`  
`"2d_art_character"`  
`"2d_pattern"`  
`"2d_pixel_art"`  
`"2d_cyberpunk"`  
`"2d_engraving"`  
`"2d_black_and_white"`  
`"2d_ink"`  
`"2d_sketch"`  
`"2d_watercolor"`  
`"2d_animation"`  
`"2d_comic"`  
`"2d_children_illustration"`  
`"2d_vintage"`  
`"2d_retro"`  
`"2d_hand_drawn"`  
`"2d_psychedelic"`  
`"2d_graffiti"`  
`"2d_ukiyo_e"`  
`"2d_woodcut"`  
`"2d_art_deco"`  
`"2d_art_nouveau"`  
`"2d_bauhaus"`  
`"2d_constructivism"`  
`"2d_cubism"`  
`"2d_futurism"`  
`"2d_glitch"`  
`"2d_impressionism"`  
`"2d_naive"`  
`"2d_pointillism"`  
`"2d_pop_art"`  
`"2d_realism"`  
`"2d_renaissance"`  
`"2d_rococo"`  
`"2d_romanticism"`  
`"2d_surrealism"`  
`"2d_suprematism"`  
`"2d_symbolism"`  
`"2d_expressionism"`  
`"2d_abstract"`  
`"2d_minimalism"`  
`"2d_contemporary"`  
`"2d_modern"`  
`"2d_brutalism"`  
`"2d_metaphysical"`  
`"2d_mannerism"`  
`"2d_baroque"`  
`"2d_neoclassicism"`  
`"2d_orientalism"`  
`"2d_primitivism"`  
`"2d_fauvism"`  
`"2d_rayonism"`  
`"2d_orphism"`  
`"2d_vorticism"`  
`"2d_dadaism"`  
`"2d_neo_expressionism"`  
`"2d_transavantgarde"`  
`"2d_new_wild"`  
`"2d_graffiti_classic"`  
`"2d_graffiti_modern"`  
`"2d_graffiti_wildstyle"`  
`"2d_graffiti_bubble"`  
`"2d_graffiti_throwup"`  
`"2d_graffiti_tag"`  
`"2d_graffiti_blockbuster"`  
`"2d_graffiti_mural"`  
`"2d_graffiti_stencil"`  
`"2d_graffiti_3d"`  
`"2d_graffiti_character"`  
`"2d_graffiti_abstract"`  
`"2d_graffiti_urban"`  
`"2d_graffiti_neo_muralism"`  
`"2d_graffiti_post_graffiti"`  
`"2d_graffiti_street_art"`  
`size`| The size of the generated image. (default: “1024x1024”)| COMBO| Yes| `"1024x1024"`  
`"1024x2048"`  
`"2048x1024"`  
`"2048x2048"`  
`"512x512"`  
`"512x1024"`  
`"1024x512"`  
`"2048x512"`  
`"512x2048"`  
`n`| The number of images to generate. (default: 1, min: 1, max: 6)| INT| Yes| 1-6  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. (default: 0, min: 0, max: 18446744073709551615)| INT| Yes| 0-18446744073709551615  
`negative_prompt`| An optional text description of undesired elements on an image. (default: "", when empty no negative prompt is used)| STRING| No| -  
`recraft_controls`| Optional additional controls over the generation via the Recraft Controls node.| CONTROLS| No| -  
  
**Note:** The `seed` parameter only controls when the node re-runs but does not make the generation results deterministic.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SVG`| The generated vector illustration in SVG format| SVG  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/en.md)

* * *

**Source fingerprint (SHA-256):** `aec7e96e339047e75dfe419d94d23a613595bc22e7f187895c52b143780fcbf3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftTextToVectorNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftTextToVectorNode)

[RecraftTextToImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftTextToImageNode)[RecraftV4CreateStyleNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftV4CreateStyleNode)

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
