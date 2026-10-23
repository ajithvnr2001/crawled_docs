---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-control-i2v/
title: Kling Image to Video (Camera Control) - ComfyUI Built-in Node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:31.621457+00:00
---

# Kling Image to Video (Camera Control) - ComfyUI Built-in Node - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-control-i2v/

## On this page

  * Parameters
    * Basic Parameters
    * Camera Control Parameters
    * Output
  * Source Code



Kling

# Kling Image to Video (Camera Control) - ComfyUI Built-in Node

Copy pageCopy page

Image to video conversion node with camera control features

Copy pageCopy page

![ComfyUI Built-in Kling Image to Video \(Camera Control\) Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0a03149e96eb31344041b9fe455bba1d) The Kling Image to Video (Camera Control) node converts static images into videos with professional camera movements. It supports camera controls like zoom, rotation, pan, tilt and first-person view while maintaining focus on the original image content.

## 

​

Parameters

### 

​

Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
start_frame| Image| -| Input image to convert to video  
prompt| String| ""| Text prompt describing video action and content  
negative_prompt| String| ""| Elements to avoid in the video  
cfg_scale| Float| 7.0| Controls how closely to follow the prompt  
aspect_ratio| Select| 16:9| Output video aspect ratio  
  
### 

​

Camera Control Parameters

Parameter| Type| Description  
---|---|---  
camera_control| CameraControl| Camera control config from Kling Camera Controls node  
  
### 

​

Output

Output| Type| Description  
---|---|---  
VIDEO| Video| Generated video  
  
## 

​

Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class KlingCameraControlI2VNode(KlingImage2VideoNode):
        """
        Kling Image to Video Camera Control Node. This node is a image to video node, but it supports controlling the camera.
        Duration, mode, and model_name request fields are hard-coded because camera control is only supported in pro mode with the kling-v1-5 model at 5s duration as of 2025-05-02.
        """
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "start_frame": model_field_to_node_input(
                        IO.IMAGE, KlingImage2VideoRequest, "image"
                    ),
                    "prompt": model_field_to_node_input(
                        IO.STRING, KlingImage2VideoRequest, "prompt", multiline=True
                    ),
                    "negative_prompt": model_field_to_node_input(
                        IO.STRING,
                        KlingImage2VideoRequest,
                        "negative_prompt",
                        multiline=True,
                    ),
                    "cfg_scale": model_field_to_node_input(
                        IO.FLOAT, KlingImage2VideoRequest, "cfg_scale"
                    ),
                    "aspect_ratio": model_field_to_node_input(
                        IO.COMBO,
                        KlingImage2VideoRequest,
                        "aspect_ratio",
                        enum_type=AspectRatio,
                    ),
                    "camera_control": (
                        "CAMERA_CONTROL",
                        {
                            "tooltip": "Can be created using the Kling Camera Controls node. Controls the camera movement and motion during the video generation.",
                        },
                    ),
                },
                "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
            }
    
        DESCRIPTION = "Transform still images into cinematic videos with professional camera movements that simulate real-world cinematography. Control virtual camera actions including zoom, rotation, pan, tilt, and first-person view, while maintaining focus on your original image."
    
        def api_call(
            self,
            start_frame: torch.Tensor,
            prompt: str,
            negative_prompt: str,
            cfg_scale: float,
            aspect_ratio: str,
            camera_control: CameraControl,
            auth_token: Optional[str] = None,
        ):
            return super().api_call(
                model_name="kling-v1-5",
                start_frame=start_frame,
                cfg_scale=cfg_scale,
                mode="pro",
                aspect_ratio=aspect_ratio,
                duration="5",
                prompt=prompt,
                negative_prompt=negative_prompt,
                camera_control=camera_control,
                auth_token=auth_token,
            )
    
    
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-control-i2v.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-control-i2v)

[Google Veo2 Video - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/google/google-veo2-video)[Kling Text to Video (Camera Control) - ComfyUI Built-in NodeNext](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-control-t2v)

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
