---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-text-to-vector/
title: Recraft Text to Vector - ComfyUI Native Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:29.960248+00:00
---

# Recraft Text to Vector - ComfyUI Native Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-text-to-vector/

## On this page

  * Parameters
    * Basic Parameters
    * Optional Parameters
    * Output
  * Source Code



Recraft

# Recraft Text to Vector - ComfyUI Native Node Documentation

Copy pageCopy page

A Recraft Partner node that generates scalable vector graphics from text descriptions

Copy pageCopy page

![ComfyUI Native Recraft Text to Vector Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=868aafbbe8b41edf218df85bd0f17fa0) The Recraft Text to Vector node lets you create high-quality vector graphics (SVG format) from text descriptions using Recraft’s API. It’s perfect for making logos, icons, and infinitely scalable illustrations.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
prompt| string| ""| Text description of the vector graphic to generate  
substyle| select| -| Vector style subtype  
size| select| 1024x1024| Canvas size for the vector output  
n| integer| 1| Number of results to generate (1-6)  
seed| integer| 0| Random seed value  
  
### 

​

Optional Parameters

Parameter| Type| Description  
---|---|---  
negative_prompt| string| Elements to exclude from generation  
recraft_controls| Recraft Controls| Additional control parameters (colors, etc.)  
  
### 

​

Output

Output| Type| Description  
---|---|---  
SVG| vector| Generated SVG vector graphic, connect to SaveSVG node to save  
  
## 

​

Source Code

[Node source code (Updated on 2025-05-03)]
    
    
    class RecraftTextToVectorNode:
        """
        Generates SVG synchronously based on prompt and resolution.
        """
    
        RETURN_TYPES = (RecraftIO.SVG,)
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "api_call"
        API_NODE = True
        CATEGORY = "api node/image/Recraft"
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "prompt": (
                        IO.STRING,
                        {
                            "multiline": True,
                            "default": "",
                            "tooltip": "Prompt for the image generation.",
                        },
                    ),
                    "substyle": (get_v3_substyles(RecraftStyleV3.vector_illustration),),
                    "size": (
                        [res.value for res in RecraftImageSize],
                        {
                            "default": RecraftImageSize.res_1024x1024,
                            "tooltip": "The size of the generated image.",
                        },
                    ),
                    "n": (
                        IO.INT,
                        {
                            "default": 1,
                            "min": 1,
                            "max": 6,
                            "tooltip": "The number of images to generate.",
                        },
                    ),
                    "seed": (
                        IO.INT,
                        {
                            "default": 0,
                            "min": 0,
                            "max": 0xFFFFFFFFFFFFFFFF,
                            "control_after_generate": True,
                            "tooltip": "Seed to determine if node should re-run; actual results are nondeterministic regardless of seed.",
                        },
                    ),
                },
                "optional": {
                    "negative_prompt": (
                        IO.STRING,
                        {
                            "default": "",
                            "forceInput": True,
                            "tooltip": "An optional text description of undesired elements on an image.",
                        },
                    ),
                    "recraft_controls": (
                        RecraftIO.CONTROLS,
                        {
                            "tooltip": "Optional additional controls over the generation via the Recraft Controls node."
                        },
                    ),
                },
                "hidden": {
                    "auth_token": "AUTH_TOKEN_COMFY_ORG",
                },
            }
    
        def api_call(
            self,
            prompt: str,
            substyle: str,
            size: str,
            n: int,
            seed,
            negative_prompt: str = None,
            recraft_controls: RecraftControls = None,
            auth_token=None,
            **kwargs,
        ):
            # create RecraftStyle so strings will be formatted properly (i.e. "None" will become None)
            recraft_style = RecraftStyle(RecraftStyleV3.vector_illustration, substyle=substyle)
    
            controls_api = None
            if recraft_controls:
                controls_api = recraft_controls.create_api_model()
    
            if not negative_prompt:
                negative_prompt = None
    
            operation = SynchronousOperation(
                endpoint=ApiEndpoint(
                    path="/proxy/recraft/image_generation",
                    method=HttpMethod.POST,
                    request_model=RecraftImageGenerationRequest,
                    response_model=RecraftImageGenerationResponse,
                ),
                request=RecraftImageGenerationRequest(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    model=RecraftModel.recraftv3,
                    size=size,
                    n=n,
                    style=recraft_style.style,
                    substyle=recraft_style.substyle,
                    controls=controls_api,
                ),
                auth_token=auth_token,
            )
            response: RecraftImageGenerationResponse = operation.execute()
            svg_data = []
            for data in response.data:
                svg_data.append(download_url_to_bytesio(data.url, timeout=1024))
    
            return (SVG(svg_data),)
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/recraft-text-to-vector.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/recraft-text-to-vector)

[Recraft Text to Image - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-text-to-image)[Recraft Vectorize Image - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-vectorize-image)

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
