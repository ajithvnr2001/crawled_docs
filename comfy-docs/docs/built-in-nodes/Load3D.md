---
url: https://docs.comfy.org/built-in-nodes/Load3D/
title: Load3D - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:22.497607+00:00
---

# Load3D - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Load3D/

3D

# Load3D - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Load3D node is a core node for loading and processing 3D model files.

Copy pageCopy page

The Load3D node is a core node for loading and processing 3D model files. When loading the node, it automatically retrieves available 3D resources from `ComfyUI/input/3d/`. You can also upload supported 3D files for preview using the upload function. **Supported Formats** Currently, this node supports multiple 3D file formats, including `.gltf`, `.glb`, `.obj`, `.fbx`, and `.stl`. **3D Node Preferences** Some related preferences for 3D nodes can be configured in ComfyUI’s settings menu. Please refer to the following documentation for corresponding settings: [Settings Menu](https://docs.comfy.org/interface/settings/3d) Besides regular node outputs, Load3D has lots of 3D view-related settings in the canvas menu.

## 

​

Inputs

Parameter Name| Description| Type| Default| Range  
---|---|---|---|---  
model_file| 3D model file path, supports upload, defaults to reading model files from `ComfyUI/input/3d/`| File Selection| -| Supported formats  
width| Canvas rendering width| INT| 1024| 1-4096  
height| Canvas rendering height| INT| 1024| 1-4096  
  
## 

​

Outputs

Parameter Name| Description| Data Type  
---|---|---  
image| Canvas rendered image| IMAGE  
mask| Mask containing current model position| MASK  
mesh_path| Model file path| STRING  
normal| Normal map| IMAGE  
lineart| Line art image output, corresponding `edge_threshold` can be adjusted in the canvas model menu| IMAGE  
camera_info| Camera information| LOAD3D_CAMERA  
recording_video| Recorded video (only when recording exists)| VIDEO  
  
All the outputs preview: ![View Operation Demo](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/load3d_outputs.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=9f5a50adc39a7614a8f83ee709f1fbda)

## 

​

Canvas Area Description

The Load3D node’s Canvas area contains numerous view operations, including:

  * Preview view settings (grid, background color, preview view)
  * Camera control: Control FOV, camera type
  * Global illumination intensity: Adjust lighting intensity
  * Video recording: Record and export videos
  * Model export: Supports `GLB`, `OBJ`, `STL` formats
  * And more

![Load 3D Node UI](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/load3d_ui.jpg?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=ee504a68a45a19e68bf27635cf5d1436)

  1. Contains multiple menus and hidden menus of the Load 3D node
  2. Menu for `resizing preview window` and `canvas video recording`
  3. 3D view operation axis
  4. Preview thumbnail
  5. Preview size settings, scale preview view display by setting dimensions and then resizing window



### 

​

1\. View Operations

Your browser does not support video playback.View control operations:

  * Left-click + drag: Rotate the view
  * Right-click + drag: Pan the view
  * Middle wheel scroll or middle-click + drag: Zoom in/out
  * Coordinate axis: Switch views



### 

​

2\. Left Menu Functions

![Menu](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=8d906a62632bc4a4eae4e76aada77862) In the canvas, some settings are hidden in the menu. Click the menu button to expand different menus

  *     1. Scene: Contains preview window grid, background color, preview settings
  *     2. Model: Model rendering mode, texture materials, up direction settings
  *     3. Camera: Switch between orthographic and perspective views, and set the perspective angle size
  *     4. Light: Scene global illumination intensity
  *     5. Export: Export model to other formats (GLB, OBJ, STL)



#### 

​

Scene

![scene menu](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_scene.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=ecbfa96b458f8a1799d447557a49bd6e) The Scene menu provides some basic scene setting functions

  1. Show/Hide grid
  2. Set background color
  3. Click to upload a background image
  4. Hide the preview



#### 

​

Model

![Menu_Scene](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_model.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=755a3f4e1aec5042b9893b37c6d987e8) The Model menu provides some model-related functions

  1. **Up direction** : Determine which axis is the up direction for the model
  2. **Material mode** : Switch model rendering modes - Original, Normal, Wireframe, Lineart



#### 

​

Camera

![menu_modelmenu_camera](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_camera.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=575bff41361272230d0928595da65d16) This menu provides switching between orthographic and perspective views, and perspective angle size settings

  1. **Camera** : Quickly switch between orthographic and orthographic views
  2. **FOV** : Adjust FOV angle



#### 

​

Light

![menu_modelmenu_camera](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_light.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=d242f04c2061d2458ffc8a5906d7747b) Through this menu, you can quickly adjust the scene’s global illumination intensity

#### 

​

Export

![menu_export](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_export.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=a6df9da61ff0168f4d403ff20f087c7e) This menu provides the ability to quickly convert and export model formats

### 

​

3\. Right Menu Functions

Your browser does not support video playback.The right menu has two main functions:

  1. **Reset view ratio** : After clicking the button, the view will adjust the canvas rendering area ratio according to the set width and height
  2. **Video recording** : Allows you to record current 3D view operations as video, allows import, and can be output as `recording_video` to subsequent nodes



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3D/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Load3D.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Load3D)

[Get3DComponents - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Get3DComponents)[Load3DAdvanced - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Load3DAdvanced)

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
