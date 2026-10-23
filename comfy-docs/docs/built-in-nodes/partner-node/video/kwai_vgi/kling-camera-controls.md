---
url: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-controls/
title: Kling Camera Controls - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:31.324695+00:00
---

# Kling Camera Controls - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-controls/

## On this page

  * Parameters
    * Output
  * Source Code



Kling

# Kling Camera Controls - ComfyUI Built-in Node Documentation

Copy pageCopy page

A node that provides camera control parameters for Kling video generation

Copy pageCopy page

![ComfyUI Built-in Kling Camera Controls Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=916ab6bab186b773cfda29470f7a45b6) The Kling Camera Controls node defines virtual camera behavior parameters to control camera movement and view changes during Kling video generation.

## 

​

Parameters

Parameter| Type| Default| Description  
---|---|---|---  
camera_control_type| Select| ”simple”| Preset camera motion types. simple: Custom camera movement; down_back: Camera moves down and back; forward_up: Camera moves forward and up; right_turn_forward: Rotate right and move forward; left_turn_forward: Rotate left and move forward  
horizontal_movement| Float| 0| Controls camera movement on horizontal axis (x-axis). Negative values move left, positive values move right  
vertical_movement| Float| 0| Controls camera movement on vertical axis (y-axis). Negative values move down, positive values move up  
pan| Float| 0.5| Controls camera rotation in vertical plane (x-axis). Negative values rotate down, positive values rotate up  
tilt| Float| 0| Controls camera rotation in horizontal plane (y-axis). Negative values rotate left, positive values rotate right  
roll| Float| 0| Controls camera roll amount (z-axis). Negative values rotate counterclockwise, positive values rotate clockwise  
zoom| Float| 0| Controls camera focal length. Negative values narrow field of view, positive values widen it  
  
**Note** : At least one non-zero camera control parameter is required for the effect to work.

### 

​

Output

Output| Type| Description  
---|---|---  
camera_control| CAMERA_CONTROL| Configuration object with camera settings  
  
**Note** : Not all model and mode combinations support camera control. Please check the Kling API documentation for details.

## 

​

Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class KlingCameraControls(KlingNodeBase):
        """Kling Camera Controls Node"""
    
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": {
                    "camera_control_type": (
                        IO.COMBO,
                        {
                            "options": [
                                camera_control_type.value
                                for camera_control_type in CameraType
                            ],
                            "default": "simple",
                            "tooltip": "Predefined camera movements type. simple: Customizable camera movement. down_back: Camera descends and moves backward. forward_up: Camera moves forward and tilts up. right_turn_forward: Rotate right and move forward. left_turn_forward: Rotate left and move forward.",
                        },
                    ),
                    "horizontal_movement": get_camera_control_input_config(
                        "Controls camera's movement along horizontal axis (x-axis). Negative indicates left, positive indicates right"
                    ),
                    "vertical_movement": get_camera_control_input_config(
                        "Controls camera's movement along vertical axis (y-axis). Negative indicates downward, positive indicates upward."
                    ),
                    "pan": get_camera_control_input_config(
                        "Controls camera's rotation in vertical plane (x-axis). Negative indicates downward rotation, positive indicates upward rotation.",
                        default=0.5,
                    ),
                    "tilt": get_camera_control_input_config(
                        "Controls camera's rotation in horizontal plane (y-axis). Negative indicates left rotation, positive indicates right rotation.",
                    ),
                    "roll": get_camera_control_input_config(
                        "Controls camera's rolling amount (z-axis). Negative indicates counterclockwise, positive indicates clockwise.",
                    ),
                    "zoom": get_camera_control_input_config(
                        "Controls change in camera's focal length. Negative indicates narrower field of view, positive indicates wider field of view.",
                    ),
                }
            }
    
        DESCRIPTION = "Kling Camera Controls Node. Not all model and mode combinations support camera control. Please refer to the Kling API documentation for more information."
        RETURN_TYPES = ("CAMERA_CONTROL",)
        RETURN_NAMES = ("camera_control",)
        FUNCTION = "main"
    
        @classmethod
        def VALIDATE_INPUTS(
            cls,
            horizontal_movement: float,
            vertical_movement: float,
            pan: float,
            tilt: float,
            roll: float,
            zoom: float,
        ) -> bool | str:
            if not is_valid_camera_control_configs(
                [
                    horizontal_movement,
                    vertical_movement,
                    pan,
                    tilt,
                    roll,
                    zoom,
                ]
            ):
                return "Invalid camera control configs: at least one of the values must be non-zero"
            return True
    
        def main(
            self,
            camera_control_type: str,
            horizontal_movement: float,
            vertical_movement: float,
            pan: float,
            tilt: float,
            roll: float,
            zoom: float,
        ) -> tuple[CameraControl]:
            return (
                CameraControl(
                    type=CameraType(camera_control_type),
                    config=CameraConfig(
                        horizontal=horizontal_movement,
                        vertical=vertical_movement,
                        pan=pan,
                        roll=roll,
                        tilt=tilt,
                        zoom=zoom,
                    ),
                ),
            )
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-controls.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-controls)

[Kling Text to Video (Camera Control) - ComfyUI Built-in NodePrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-camera-control-t2v)[Kling Image to Video - ComfyUI Built-in NodeNext](https://docs.comfy.org/built-in-nodes/partner-node/video/kwai_vgi/kling-image-to-video)

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
