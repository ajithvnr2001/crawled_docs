---
url: https://docs.comfy.org/manager/configuration/
title: ComfyUI-Manager Configuration - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:04.149476+00:00
---

# ComfyUI-Manager Configuration - ComfyUI

> Source: https://docs.comfy.org/manager/configuration/

## On this page

  * Configuration paths
    * Configuration files
  * Config.ini options
    * Network modes
    * Security levels
    * Risk levels for features
  * Environment variables
    * Examples
  * Advanced configuration
    * Prevent downgrade of specific packages
    * Custom pip mapping
    * Prevent installation of specific pip packages
    * Automatically restore pip installation
    * Use aria2 as downloader
  * extra_model_paths.yaml configuration
  * CLI tools



ComfyUI-Manager

# ComfyUI-Manager Configuration

Copy pageCopy page

ComfyUI-Manager configuration reference: config.ini paths and options, security levels, and the protected system path introduced in V3.38.

Copy pageCopy page

## 

​

Configuration paths

Starting from V3.38, Manager uses a protected system path for enhanced security.

ComfyUI Version| Manager Path  
---|---  
v0.3.76+ (with System User API)| `<USER_DIRECTORY>/__manager/`  
Older versions| `<USER_DIRECTORY>/default/ComfyUI-Manager/`  
  
If executed without any options, the `<USER_DIRECTORY>` path defaults to `ComfyUI/user`. It can be set using `--user-directory <USER_DIRECTORY>`.

### 

​

Configuration files

File| Description  
---|---  
`config.ini`| Basic configuration  
`channels.list`| Configurable channel lists  
`pip_overrides.json`| Custom pip package mappings  
`pip_blacklist.list`| Packages to prevent installation  
`pip_auto_fix.list`| Packages to auto-restore  
`snapshots/`| Saved snapshot files  
`startup-scripts/`| Startup script files  
`components/`| Component files  
  
## 

​

Config.ini options

Modify the `config.ini` file to apply settings. The path is displayed in startup log messages.
    
    
    [default]
    git_exe = <path to git executable>
    use_uv = <True/False - use uv instead of pip>
    default_cache_as_channel_url = <True/False - retrieve DB designated as channel_url at startup>
    bypass_ssl = <True/False - disable SSL if errors occur>
    file_logging = <True/False - create log file>
    windows_selector_event_loop_policy = <True/False - fix event loop errors on Windows>
    model_download_by_agent = <True/False - use agent for model downloads>
    downgrade_blacklist = <comma-separated list of packages to prevent downgrades>
    security_level = <strong|normal|normal-|weak>
    always_lazy_install = <True/False - perform dependency installation on restart>
    network_mode = <public|private|offline>
    

### 

​

Network modes

Mode| Description  
---|---  
`public`| Standard public network environment  
`private`| Closed network with private node DB configured via `channel_url` (uses cache if available)  
`offline`| No external connections (uses cache if available)  
  
### 

​

Security levels

Level| Description  
---|---  
`strong`| Doesn’t allow high and middle level risky features  
`normal`| Doesn’t allow high level risky features; middle level features available  
`normal-`| Doesn’t allow high level risky features if `--listen` is specified and not starts with `127.`; middle level features available  
`weak`| All features available  
  
#### 

​

Risk levels for features

Risk Level| Features  
---|---  
**High**|  Install via git url, pip install, installation of custom nodes not in default channel, fix custom nodes  
**Middle**|  Uninstall/Update, installation of custom nodes in default channel, restore/remove snapshot, restart  
**Low**|  Update ComfyUI  
  
## 

​

Environment variables

Variable| Description  
---|---  
`COMFYUI_PATH`| Installation path of ComfyUI  
`GITHUB_ENDPOINT`| Reverse proxy for GitHub access  
`HF_ENDPOINT`| Reverse proxy for Hugging Face access  
  
### 

​

Examples

Redirecting GitHub requests through a proxy:
    
    
    GITHUB_ENDPOINT=https://mirror.ghproxy.com/https://github.com
    

Changing Hugging Face endpoint:
    
    
    HF_ENDPOINT=https://some-hf-mirror.com
    

## 

​

Advanced configuration

### 

​

Prevent downgrade of specific packages

List package names in the `downgrade_blacklist` section of `config.ini`, separated by commas:
    
    
    downgrade_blacklist = diffusers, kornia
    

### 

​

Custom pip mapping

Create a `pip_overrides.json` file to change the installation of specific pip packages to user-defined installations. Refer to `pip_overrides.json.template` for the format.

### 

​

Prevent installation of specific pip packages

List package names one per line in the `pip_blacklist.list` file.

### 

​

Automatically restore pip installation

List pip spec requirements in `pip_auto_fix.list` (similar to `requirements.txt`). It will automatically restore specified versions when starting ComfyUI or when versions get mismatched during custom node installations. `--index-url` can be used.

### 

​

Use aria2 as downloader

For faster downloads, you can configure ComfyUI-Manager to use aria2. See the [aria2 setup guide](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/docs/en/use_aria2.md).

## 

​

extra_model_paths.yaml configuration

The following settings are applied based on the section marked as `is_default`:

  * `custom_nodes`: Path for installing custom nodes
  * `download_model_base`: Path for downloading models



## 

​

CLI tools

ComfyUI-Manager provides `cm-cli`, a command line tool that allows you to use Manager features without running ComfyUI. This is useful for automating custom node installation and managing installations in headless environments. For detailed cm-cli documentation, see the [official cm-cli guide](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/docs/en/cm-cli.md). For a more comprehensive CLI experience, consider using [comfy-cli](https://docs.comfy.org/comfy-cli/getting-started).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/manager/configuration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/manager/configuration)

[Managing custom nodes with ComfyUI-Manager (legacy UI)Previous](https://docs.comfy.org/manager/legacy-ui)[ComfyUI Manager TroubleshootingNext](https://docs.comfy.org/manager/troubleshooting)

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
