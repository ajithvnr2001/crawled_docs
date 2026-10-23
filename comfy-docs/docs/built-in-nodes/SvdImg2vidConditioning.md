---
url: https://docs.comfy.org/built-in-nodes/SvdImg2vidConditioning/
title: SvdImg2vidConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:06.967896+00:00
---

# SvdImg2vidConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SvdImg2vidConditioning/

Video Models

# SvdImg2vidConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed for generating conditioning data for video generation tasks, specifically tailored for use with SVDimg2vid models.

Copy pageCopy page

This node is designed for generating conditioning data for video generation tasks, specifically tailored for use with SVD_img2vid models. It takes various inputs including initial images, video parameters, and a VAE model to produce conditioning data that can be used to guide the generation of video frames.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`clip_vision`| Represents the CLIP vision model used for encoding visual features from the initial image, playing a crucial role in understanding the content and context of the image for video generation.| `CLIP_VISION`  
`init_image`| The initial image from which the video will be generated, serving as the starting point for the video generation process.| `IMAGE`  
`vae`| A Variational Autoencoder (VAE) model used for encoding the initial image into a latent space, facilitating the generation of coherent and continuous video frames.| `VAE`  
`width`| The desired width of the video frames to be generated, allowing for customization of the video’s resolution.| `INT`  
`height`| The desired height of the video frames, enabling control over the video’s aspect ratio and resolution.| `INT`  
`video_frames`| Specifies the number of frames to be generated for the video, determining the video’s length.| `INT`  
`motion_bucket_id`| An identifier for categorizing the type of motion to be applied in the video generation, aiding in the creation of dynamic and engaging videos.| `INT`  
`fps`| The frames per second (fps) rate for the video, influencing the smoothness and realism of the generated video.| `INT`  
`augmentation_level`| A parameter controlling the level of augmentation applied to the initial image, affecting the diversity and variability of the generated video frames.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Comfy dtype  
---|---|---  
`positive`| The positive conditioning data, consisting of encoded features and parameters for guiding the video generation process in a desired direction.| `CONDITIONING`  
`negative`| The negative conditioning data, providing a contrast to the positive conditioning, which can be used to avoid certain patterns or features in the generated video.| `CONDITIONING`  
`latent`| Latent representations generated for each frame of the video, serving as a foundational component for the video generation process.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SvdImg2vidConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SvdImg2vidConditioning)

[SVD_img2vid_Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SVD_img2vid_Conditioning)[ConditioningAverage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningAverage)

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
