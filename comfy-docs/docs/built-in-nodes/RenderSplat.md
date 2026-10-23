---
url: https://docs.comfy.org/built-in-nodes/RenderSplat/
title: RenderSplat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:50.415663+00:00
---

# RenderSplat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RenderSplat/

Splat

# RenderSplat - ComfyUI Built-in Node Documentation

Copy pageCopy page

Render a gaussian splat as an image using an anisotropic EWA rasterizer with oriented elliptical splats, antialiasing, and depth-sorted front-to-back rendering.

Copy pageCopy page

Render a gaussian splat as an image using an anisotropic EWA rasterizer with oriented elliptical splats, antialiasing, and depth-sorted front-to-back rendering. The camera comes from a camera_info input, or you can leave it empty to auto-frame the splat. Set frames greater than 1 for a turntable batch of images to feed a Video node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`splat`| The gaussian splat data to render| SPLAT| Yes| -  
`width`| Width of the output image (default: 1024)| INT| Yes| 64 to 2048 (step: 8)  
`height`| Height of the output image (default: 1024)| INT| Yes| 64 to 2048 (step: 8)  
`frames`| Number of frames to render. -1, 0, or 1 produces a single still image. Values greater than 1 create a turntable animation where the camera orbits over a full 360 degree turn. Negative values orbit in the opposite direction (default: 1)| INT| Yes| -240 to 240  
`splat_scale`| Multiplier on each splat’s projected footprint. Lower values produce crisper points, higher values produce softer and fuller surfaces (default: 1.0)| FLOAT| Yes| 0.1 to 5.0 (step: 0.05)  
`sharpen`| Controls sharpness of overlapping splats. A value of 1.0 gives physically-correct blending. Values above 1.0 bias each pixel toward its dominant (nearest) splat for crisper texture without shrinking splats or opening gaps (default: 2.0)| FLOAT| Yes| 1.0 to 8.0 (step: 0.5)  
`headlight_shading`| Diffuse shading from a light at the camera position, using the splat surfel normals. Darkens surfaces that turn away from view to reveal form and curvature. 0 gives flat albedo, 1 gives strongest shading (default: 0.0)| FLOAT| Yes| 0.0 to 3.0 (step: 0.05)  
`opacity_threshold`| Culls gaussians with opacity below this threshold, which removes faint floaters (default: 0.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`render_style`| What the image output shows. Options are: color (full color rendering), clay (neutral-albedo shaded), depth (near objects appear bright), normal (OpenGL normal map) (default: “color”)| COMBO| Yes| ”color"  
"clay"  
"depth"  
"normal”  
`background`| Solid background color for the render (default: #000000)| COLOR| Yes| -  
`bg_image`| Optional background plate composited behind the splat. Overrides the solid background color. Resized to the render size. A batch of images is used per frame, a single image is used for all frames. Only works with color and clay render styles| IMAGE| No| -  
`camera_info`| Camera to render from. Can come from a Load3D, Preview3D, or Create Camera Info node. If empty, the splat is auto-framed from a default 3/4 view| CAMERA_3D| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The rendered image of the gaussian splat| IMAGE  
`mask`| The alpha mask of the rendered splat| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderSplat/en.md)

* * *

**Source fingerprint (SHA-256):** `038bd9fb032f347ecda665c03719a64b0cf907599b701606f5cf6d0606d19d98`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RenderSplat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RenderSplat)

[MergeSplat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MergeSplat)[SplatToFile3D - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SplatToFile3D)

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
