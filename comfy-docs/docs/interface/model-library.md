---
url: https://docs.comfy.org/interface/model-library/
title: Model Library - Browse Local Models - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:01.693165+00:00
---

# Model Library - Browse Local Models - ComfyUI

> Source: https://docs.comfy.org/interface/model-library/

## On this page

  * Opening the Model Library
  * Browse by folder
  * Search
  * Preview and refresh
  * Drag a model onto the canvas
  * Related settings
  * Related pages



Left sidebar

# Model Library - Browse Local Models

Copy pageCopy page

Open the Model Library sidebar to find checkpoints and other models under your ComfyUI models folder, then drag them onto the canvas.

Copy pageCopy page

The **Models** entry in the left sidebar opens the Model Library. After ComfyUI starts, it lists model folders and files detected under your `ComfyUI/models` tree (and any extra model paths you configured). Use it to search by name, browse by folder type, preview metadata, and drag a model onto the canvas to insert the matching loader node. Availability differs by version:

  * **Self-hosted / Desktop** : the sidebar shows a folder tree of local model files. On Desktop, in-progress downloads appear at the top of the panel, and the sidebar icon can show a badge with the download count.
  * **Comfy Cloud** : when the assets system is available and **Use the asset browser for the model library** is on (Cloud default), clicking **Models** opens the asset browser for models instead of the sidebar tree. Uploading or importing your own weights is covered in [Import models](https://docs.comfy.org/cloud/import-models).

Media files (images, video, audio, 3D) are not listed here. Those live in [Assets](https://docs.comfy.org/interface/assets). ![The Model Library sidebar with the checkpoints folder expanded and the search box above the tree](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/model-library/model_library.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=45a85041be034c947ab6e8b6fe8092f9)

## 

​

Opening the Model Library

Click the **Models** icon in the left sidebar. The panel title is **Model Library**.

## 

​

Browse by folder

Without a search query, the panel lists root model folders (for example `checkpoints`, `loras`, `vae`, `controlnet`, `diffusion_models`, `upscale_models`, `text_encoders`, and others returned by the server). Expand a folder to load its files. By default, root folders load their contents when you open them. You can change that in Settings:

  * **Automatically load all model folders** (`Comfy.ModelLibrary.AutoLoadAll`): when on, every folder loads as soon as you open the library (can be slow on large libraries). When off (default on self-hosted), a folder loads when you expand it. This setting is hidden on Comfy Cloud.
  * **What name to display in the model library tree view** (`Comfy.ModelLibrary.NameFormat`): `title` (default) uses model metadata titles when available; `filename` shows a simplified file name without the directory or `.safetensors` extension.

When the assets feature flag is off, a **Load all folders** button appears in the panel header next to refresh.

## 

​

Search

The search box at the top filters models by name and related searchable fields as you type. Searching loads all folders so results are complete. Results auto-expand in the tree. If more than 500 models match, the panel shows a capped-results note; refine the query to reach the rest.

## 

​

Preview and refresh

Hover a model leaf to open a preview card when metadata is available. The card can show title, file name, architecture, author, preview image, usage hint, trigger phrase, and description. Use the refresh button in the panel header, or press `r` (`Comfy.RefreshNodeDefinitions`), after you add or remove model files while ComfyUI is running. That refresh also reloads node combo lists so loader widgets pick up new files.

## 

​

Drag a model onto the canvas

Model leaves are draggable. Drag one onto the canvas to create the loader node mapped for that folder (for example `CheckpointLoaderSimple` for `checkpoints`, `LoraLoader` for `loras`, `VAELoader` for `vae`, `UNETLoader` for `diffusion_models`, `CLIPLoader` for `text_encoders`, and other mappings registered in the frontend). The matching widget is filled with the model file name. If a folder type has no registered loader mapping, the drop may not create a node. Missing models that a workflow expects still appear under the [Right Side Panel](https://docs.comfy.org/interface/right-side-panel) **Errors** tab, with download or import actions when available.

## 

​

Related settings

Setting| Where| What it does  
---|---|---  
Automatically load all model folders| `Comfy` → Model Library| Load every folder on open vs on expand  
Name format| `Comfy` → Model Library| Show `title` or `filename` in the tree  
Use the asset browser for the model library| Experimental / Cloud-oriented| Open the asset browser instead of the sidebar tree when assets are enabled  
  
## 

​

Related pages

  * [Interface Overview](https://docs.comfy.org/interface/overview)
  * [Assets](https://docs.comfy.org/interface/assets) (media files, not model weights)
  * [Import models](https://docs.comfy.org/cloud/import-models) (Cloud)
  * [Right Side Panel](https://docs.comfy.org/interface/right-side-panel) (missing-model errors)
  * [Comfy settings](https://docs.comfy.org/interface/settings/comfy) (Model Library section)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/model-library.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/model-library)

[Node Library - Browse and Add NodesPrevious](https://docs.comfy.org/interface/node-library)[Workflows Sidebar - Saved and Open GraphsNext](https://docs.comfy.org/interface/workflows)

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
