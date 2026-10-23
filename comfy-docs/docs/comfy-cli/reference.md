---
url: https://docs.comfy.org/comfy-cli/reference/
title: Comfy CLI Command Reference - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:35.310801+00:00
---

# Comfy CLI Command Reference - ComfyUI

> Source: https://docs.comfy.org/comfy-cli/reference/

## On this page

  * CLI
  * Generate (partner nodes) — Beta
    * list
    * schema
    * refresh
    * upload
    * resume
    * Model aliases (selected)
  * Nodes
    * deps-in-workflow
    * disable
    * enable
    * fix
    * install
    * install-deps
    * reinstall
    * restore-dependencies
    * restore-snapshot
    * save-snapshot
    * show
    * simple-show
    * uninstall
    * update
  * Models
    * download
    * list
    * remove



Comfy CLI

# Comfy CLI Command Reference

Copy pageCopy page

Full reference for the Comfy CLI, covering installation commands, node management, and model downloads for setting up and managing ComfyUI from the terminal.

Copy pageCopy page

# 

​

CLI

## 

​

Generate (partner nodes) — Beta

**`comfy generate` is in beta.** Flag names, model aliases, and output formats may change. The underlying partner endpoints are stable; the CLI surface is still evolving. File feedback on the [comfy-cli GitHub repo](https://github.com/Comfy-Org/comfy-cli/issues).

**Usage** :
    
    
    $ comfy generate [OPTIONS] <MODEL_OR_ACTION> [--<param> value]...
    

`<MODEL_OR_ACTION>` is either:

  * A **model alias** (e.g. `flux-pro`, `ideogram-edit`, `kling`, `dalle`) — calls that partner model directly.
  * A **reserved action** : `list`, `schema`, `refresh`, `upload`, `resume`.

Anything not in the reserved set is treated as a model alias and the request is dispatched to that partner endpoint. **Auth** : Set the `COMFY_API_KEY` environment variable, or pass `--api-key <KEY>` on each call. Get a key at [platform.comfy.org](https://platform.comfy.org). **Run-level flags** (work with any model):

  * `--download PATH`: Save the result image/video to `PATH`.
  * `--async`: Submit and return a job id immediately instead of polling to completion. Resume later with `comfy generate resume <model> <job_id>`.
  * `--json`: Emit the raw API response as JSON (useful for scripting).
  * `--timeout SECONDS`: Override the default 300s polling timeout.
  * `--api-key KEY`: Inline API key (overrides `COMFY_API_KEY`).

**Examples** :
    
    
    comfy generate flux-pro --prompt "a cat on the moon" --width 1024 --height 1024 --download cat.png
    comfy generate ideogram-edit --image cat.png --mask m.png --prompt "add sunglasses" --rendering_speed TURBO
    comfy generate kling --prompt "a paper boat drifting at dusk" --duration 5 --download boat.mp4
    

### 

​

`list`

List available partner models with their short aliases. **Usage** :
    
    
    $ comfy generate list [OPTIONS]
    

**Options** :

  * `--partner TEXT` / `-p TEXT`: Filter by partner (e.g. `bfl`, `kling`, `ideogram`, `openai`).
  * `--category TEXT` / `--style TEXT` / `-c TEXT`: Filter by category (e.g. `text-to-image`, `image-edit`, `inpaint`, `upscale`, `text-to-video`, `image-to-video`).
  * `--query TEXT` / `-q TEXT`: Substring match against model id/summary.



### 

​

`schema`

Show the parameters for a specific model, including required/optional flags, types, defaults, and an example invocation. **Usage** :
    
    
    $ comfy generate schema <MODEL>
    

**Example** :
    
    
    comfy generate schema flux-pro
    comfy generate schema kling-i2v
    

### 

​

`refresh`

Refresh the local cached model catalog from the cloud OpenAPI spec. Useful when new partner models are added. **Usage** :
    
    
    $ comfy generate refresh
    

### 

​

`upload`

Upload a local file (or rehost a remote URL) to Comfy’s storage and print the signed URL. Most models accept local file paths directly — this is for cases where you want the URL explicitly (e.g. to reuse the same asset across multiple calls). **Usage** :
    
    
    $ comfy generate upload <FILE_OR_URL> [--json]
    

**Example** :
    
    
    comfy generate upload ./photo.jpg
    comfy generate upload ./photo.jpg --json
    

**Reference assets are auto-deleted after 24 hours.** Uploaded files (whether via `comfy generate upload` or implicitly when you pass a local file path to a model) are stored in a Comfy-managed GCS bucket (`api-nodes-prod`) and reachable only via a signed URL. Objects are automatically deleted **1 day after upload** by a bucket lifecycle rule. If you need an asset to persist across long-running async jobs, re-upload it before each job, or host it yourself and pass the URL directly.

### 

​

`resume`

Resume a previously submitted async job (typically a video job submitted with `--async`). Polls until the result is ready and optionally downloads it. **Usage** :
    
    
    $ comfy generate resume <MODEL> <JOB_ID> [--download PATH] [--json]
    

**Example** :
    
    
    comfy generate resume luma 7c3f9e2a --download out.mp4
    

### 

​

Model aliases (selected)

The following short aliases are accepted as `<MODEL>`. Run `comfy generate list` for the full, up-to-date catalog. **Popular** :

Alias| Partner| Category  
---|---|---  
`nano-banana`| Google (Gemini Flash Image)| text-to-image / image-edit  
`seedance`| ByteDance| text-to-video / image-to-video (async)  
`grok`, `grok-edit`| xAI| text-to-image / image-edit  
`grok-video`| xAI| text-to-video (async)  
  
**Everything else** :

Alias| Partner| Category  
---|---|---  
`flux-pro`, `flux-ultra`, `flux-2`| BFL| text-to-image (async)  
`flux-kontext`, `flux-kontext-max`| BFL| image-edit (async)  
`flux-fill`, `flux-expand`, `flux-canny`, `flux-depth`| BFL| inpaint / outpaint / controlnet  
`ideogram`, `ideogram-edit`, `ideogram-remix`, `ideogram-reframe`, `ideogram-bg`| Ideogram| text-to-image / image-edit  
`dalle`, `dalle-edit`| OpenAI| text-to-image / image-edit  
`stability-ultra`, `stability-sd3`, `stability-upscale`, `stability-upscale-creative`, `stability-upscale-fast`| Stability| text-to-image / upscale  
`recraft`, `recraft-vectorize`, `recraft-rmbg`, `recraft-replace-bg`, `recraft-i2i`, `recraft-inpaint`, `recraft-upscale`, `recraft-upscale-creative`| Recraft| text-to-image / image-edit  
`reve`, `reve-edit`| Reve| text-to-image / image-edit  
`runway`| Runway| text-to-image  
`kling`, `kling-i2v`, `kling-extend`, `kling-lipsync`| Kling| text-to-video / image-to-video / video-extend / lipsync (async)  
`luma`, `luma-i2v`| Luma| text-to-video / image-to-video (async)  
`hailuo`| MiniMax| text-to-video (async)  
`runway-i2v`| Runway| image-to-video (async)  
`moonvalley-t2v`, `moonvalley-i2v`| Moonvalley| text-to-video / image-to-video (async)  
`pika`, `pika-i2v`| Pika| text-to-video / image-to-video (async)  
`vidu`, `vidu-i2v`, `vidu-extend`| Vidu| text-to-video / image-to-video / video-extend (async)  
  
## 

​

Nodes

**Usage** :
    
    
    $ comfy node [OPTIONS] COMMAND [ARGS]...
    

**Options** :

  * `--install-completion`: Install completion for the current shell.
  * `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
  * `--help`: Show this message and exit.

**Commands** :

  * `deps-in-workflow`
  * `disable`
  * `enable`
  * `fix`
  * `install`
  * `install-deps`
  * `reinstall`
  * `restore-dependencies`
  * `restore-snapshot`
  * `save-snapshot`: Save a snapshot of the current ComfyUI…
  * `show`
  * `simple-show`
  * `uninstall`
  * `update`



### 

​

`deps-in-workflow`

**Usage** :
    
    
    $ deps-in-workflow [OPTIONS]
    

**Options** :

  * `--workflow TEXT`: Workflow file (.json/.png) [required]
  * `--output TEXT`: Workflow file (.json/.png) [required]
  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`disable`

**Usage** :
    
    
    $ disable [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: disable custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`enable`

**Usage** :
    
    
    $ enable [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: enable custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`fix`

**Usage** :
    
    
    $ fix [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: fix dependencies for specified custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`install`

**Usage** :
    
    
    $ install [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: install custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`install-deps`

**Usage** :
    
    
    $ install-deps [OPTIONS]
    

**Options** :

  * `--deps TEXT`: Dependency spec file (.json)
  * `--workflow TEXT`: Workflow file (.json/.png)
  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`reinstall`

**Usage** :
    
    
    $ reinstall [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: reinstall custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`restore-dependencies`

**Usage** :
    
    
    $ restore-dependencies [OPTIONS]
    

**Options** :

  * `--help`: Show this message and exit.



### 

​

`restore-snapshot`

**Usage** :
    
    
    $ restore-snapshot [OPTIONS] PATH
    

**Arguments** :

  * `PATH`: [required]

**Options** :

  * `--help`: Show this message and exit.



### 

​

`save-snapshot`

Save a snapshot of the current ComfyUI environment **Usage** :
    
    
    $ save-snapshot [OPTIONS]
    

**Options** :

  * `--output TEXT`: Specify the output file path. (.json/.yaml)
  * `--help`: Show this message and exit.



### 

​

`show`

**Usage** :
    
    
    $ show [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: [installed|enabled|not-installed|disabled|all|snapshot|snapshot-list] [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`simple-show`

**Usage** :
    
    
    $ simple-show [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: [installed|enabled|not-installed|disabled|all|snapshot|snapshot-list] [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`uninstall`

**Usage** :
    
    
    $ uninstall [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: uninstall custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`update`

**Usage** :
    
    
    $ update [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: update custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



## 

​

Models

**Usage** :
    
    
    $ comfy model [OPTIONS] COMMAND [ARGS]...
    

**Options** :

  * `--install-completion`: Install completion for the current shell.
  * `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
  * `--help`: Show this message and exit.

**Commands** :

  * `download`: Download a model to a specified relative…
  * `list`: Display a list of all models currently…
  * `remove`: Remove one or more downloaded models,…



### 

​

`download`

Download a model to a specified relative path if it is not already downloaded. **Usage** :
    
    
    $ download [OPTIONS]
    

**Options** :

  * `--url TEXT`: The URL from which to download the model [required]
  * `--relative-path TEXT`: The relative path from the current workspace to install the model. [default: models/checkpoints]
  * `--help`: Show this message and exit.



### 

​

`list`

Display a list of all models currently downloaded in a table format. **Usage** :
    
    
    $ list [OPTIONS]
    

**Options** :

  * `--relative-path TEXT`: The relative path from the current workspace where the models are stored. [default: models/checkpoints]
  * `--help`: Show this message and exit.



### 

​

`remove`

Remove one or more downloaded models, either by specifying them directly or through an interactive selection. **Usage** :
    
    
    $ remove [OPTIONS]
    

**Options** :

  * `--relative-path TEXT`: The relative path from the current workspace where the models are stored. [default: models/checkpoints]
  * `--model-names TEXT`: List of model filenames to delete, separated by spaces
  * `--help`: Show this message and exit.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/comfy-cli/reference.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/comfy-cli/reference)

[Get Started with Comfy CLIPrevious](https://docs.comfy.org/comfy-cli/getting-started)[Comfy CLI Troubleshooting GuideNext](https://docs.comfy.org/comfy-cli/troubleshooting)

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
