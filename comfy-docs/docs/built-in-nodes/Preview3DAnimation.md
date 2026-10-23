---
url: https://docs.comfy.org/built-in-nodes/Preview3DAnimation/
title: Preview3DAnimation - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:43.964998+00:00
---

# Preview3DAnimation - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Preview3DAnimation/

3D

# Preview3DAnimation - ComfyUI Built-in Node Documentation

Copy pageCopy page

Preview3DAnimation node is mainly used to preview 3D model outputs.

Copy pageCopy page

Preview3DAnimation node is mainly used to preview 3D model outputs. This node takes two inputs: one is the `camera_info` from the Load3D node, and the other is the path to the 3D model file. The model file path must be located in the `ComfyUI/output` folder. **Supported Formats** Currently, this node supports multiple 3D file formats, including `.gltf`, `.glb`, `.obj`, `.fbx`, and `.stl`. **3D Node Preferences** Some related preferences for 3D nodes can be configured in ComfyUI’s settings menu. Please refer to the following documentation for corresponding settings: [Settings Menu](https://docs.comfy.org/interface/settings/3d)

## 

​

Inputs

Parameter Name| Description| Type  
---|---|---  
camera_info| Camera information| LOAD3D_CAMERA  
model_file| Model file path under `ComfyUI/output/`| STRING  
  
## 

​

Canvas Area Description

Currently, the 3D-related nodes in the ComfyUI frontend share the same canvas component, so their basic operations are mostly consistent except for some functional differences.

> The following content and interface are mainly based on the Load3D node. Please refer to the actual node interface for specific features.

The Canvas area includes various view operations, such as:

  * Preview view settings (grid, background color, preview view)
  * Camera control: FOV, camera type
  * Global illumination intensity: adjust lighting
  * Model export: supports `GLB`, `OBJ`, `STL` formats
  * etc.

![Load 3D Node UI](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Preview3DAnimation/preview3d_canvas.jpg?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=c01b0e8f88db6a63825e2c04eb26146e)

  1. Contains multiple menus and hidden menus of the Load 3D node
  2. 3D view operation axis



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

![Menu](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp) In the preview area, some view operation menus are hidden in the menu. Click the menu button to expand different menus.

  *     1. Scene: Contains preview window grid, background color, thumbnail settings
  *     2. Model: Model rendering mode, texture material, up direction settings
  *     3. Camera: Switch between orthographic and perspective views, set perspective angle
  *     4. Light: Scene global illumination intensity
  *     5. Export: Export model to other formats (GLB, OBJ, STL)



#### 

​

Scene

![scene menu](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp) The Scene menu provides some basic scene setting functions:

  1. Show/Hide grid
  2. Set background color
  3. Click to upload a background image
  4. Hide preview thumbnail



#### 

​

Model

![Menu_Scene](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp) The Model menu provides some model-related functions:

  1. **Up direction** : Determine which axis is the up direction for the model
  2. **Material mode** : Switch model rendering modes - Original, Normal, Wireframe, Lineart



#### 

​

Camera

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp) This menu provides switching between orthographic and perspective views, and perspective angle size settings:

  1. **Camera** : Quickly switch between orthographic and perspective views
  2. **FOV** : Adjust FOV angle



#### 

​

Light

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp) Through this menu, you can quickly adjust the scene’s global illumination intensity

#### 

​

Export

![menu_export](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp) This menu provides the ability to quickly convert and export model formats

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAnimation/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Preview3DAnimation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Preview3DAnimation)

[Preview3DAdvanced - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Preview3DAdvanced)[PreviewGaussianSplat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PreviewGaussianSplat)

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
