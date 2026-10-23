---
url: https://docs.comfy.org/manager/troubleshooting/
title: ComfyUI Manager Troubleshooting - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:04.777995+00:00
---

# ComfyUI Manager Troubleshooting - ComfyUI

> Source: https://docs.comfy.org/manager/troubleshooting/

## On this page

  * Common issues
    * Custom git executable path
    * ComfyUI-Manager update fails
    * Windows: Overlapped Object error
    * SSL certificate verification failed
  * Installation issues
    * Incorrect installation path
  * Network issues
    * GitHub access problems
    * Hugging Face access problems
  * Scanner troubleshooting
  * Security policy
    * Risk levels for features
  * Getting help



ComfyUI-Manager

# ComfyUI Manager Troubleshooting

Copy pageCopy page

Fix common ComfyUI-Manager issues: custom git executable paths, database errors, update failures, and more.

Copy pageCopy page

## 

​

Common issues

### 

​

Custom git executable path

If your `git.exe` is installed in a specific location other than the system default:

  1. Install ComfyUI-Manager and run ComfyUI once
  2. Open `<USER_DIRECTORY>/default/ComfyUI-Manager/config.ini`
  3. Specify the full path including the file name in `git_exe =`


    
    
    git_exe = C:\Program Files\Git\bin\git.exe
    

### 

​

ComfyUI-Manager update fails

If updating ComfyUI-Manager itself fails, go to the ComfyUI-Manager directory and run:
    
    
    git update-ref refs/remotes/origin/main a361cc1 && git fetch --all && git pull
    

### 

​

Windows: Overlapped Object error

If you encounter `Overlapped Object has pending operation at deallocation on ComfyUI Manager load`: Edit `config.ini` and add:
    
    
    windows_selector_event_loop_policy = True
    

### 

​

SSL certificate verification failed

If you encounter `SSL: CERTIFICATE_VERIFY_FAILED` error: Edit `config.ini` and add:
    
    
    bypass_ssl = True
    

## 

​

Installation issues

### 

​

Incorrect installation path

ComfyUI-Manager files must be located in `ComfyUI/custom_nodes/comfyui-manager`. **Common mistakes to avoid:**

Issue| Problem  
---|---  
Files in wrong location| Manager files like `__init__.py` placed directly in `custom_nodes` directory  
Double nested folder| Installed as `custom_nodes/ComfyUI-Manager/ComfyUI-Manager`  
Wrong folder name| Installed as `custom_nodes/ComfyUI-Manager-main`  
Compressed format| Installing from a compressed file without proper extraction  
  
If installed incorrectly, ComfyUI-Manager may appear to work but won’t be recognized for updates and may cause duplicate installations. Remove it and reinstall properly via `git clone`.

## 

​

Network issues

### 

​

GitHub access problems

If you have limited access to GitHub, set the `GITHUB_ENDPOINT` environment variable:
    
    
    GITHUB_ENDPOINT=https://mirror.ghproxy.com/https://github.com
    

### 

​

Hugging Face access problems

If you have limited access to Hugging Face, set the `HF_ENDPOINT` environment variable:
    
    
    HF_ENDPOINT=https://some-hf-mirror.com
    

## 

​

Scanner troubleshooting

When running the `scan.sh` script:

  * It updates `extension-node-map.json` by pulling or cloning custom nodes listed in `custom-node-list.json` into `~/.tmp/default`
  * It updates `github-stats.json` using the GitHub API



Option| Description  
---|---  
`--skip-update`| Skip updating extension-node-map.json  
`--skip-stat-update`| Skip updating github-stats.json  
`--skip-all`| Skip both update steps  
  
To avoid GitHub API rate limits, set your token: `export GITHUB_TOKEN=your_token_here`

If you want to specify a different path instead of `~/.tmp/default`, run `python scanner.py [path]` directly instead of `scan.sh`.

## 

​

Security policy

If you encounter the error `This action is not allowed with this security level configuration` when installing custom nodes via git URL or using the nightly version, you need to adjust the security level in your `config.ini` file. The `config.ini` file is located at:

  * **ComfyUI v0.3.76+** : `<USER_DIRECTORY>/__manager/config.ini`
  * **Older versions** : `<USER_DIRECTORY>/default/ComfyUI-Manager/config.ini`

Where `<USER_DIRECTORY>` defaults to `ComfyUI/user`. See [Configuration](https://docs.comfy.org/manager/configuration) for more details. Configure security levels in `config.ini`:
    
    
    security_level = normal
    

Level| Description  
---|---  
`strong`| Doesn’t allow high and middle level risky features  
`normal`| Doesn’t allow high level risky features; middle level features available  
`normal-`| Doesn’t allow high level risky features if `--listen` is specified and not starts with `127.`; middle level features available  
`weak`| All features available  
  
### 

​

Risk levels for features

Risk Level| Features  
---|---  
**High**|  Install via git url, pip install, installation of custom nodes not in default channel, fix custom nodes  
**Middle**|  Uninstall/Update, installation of custom nodes in default channel, restore/remove snapshot, restart  
**Low**|  Update ComfyUI  
  
To install custom nodes via git URL or nightly versions, set `security_level = weak` in your `config.ini`.

## 

​

Getting help

If you’re still experiencing issues:

  1. Check the [ComfyUI-Manager GitHub issues](https://github.com/Comfy-Org/ComfyUI-Manager/issues) for similar problems
  2. Review the startup log messages for error details
  3. Join the [ComfyUI Discord](https://discord.com/invite/comfyorg) for community support



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/manager/troubleshooting.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/manager/troubleshooting)

[ComfyUI-Manager ConfigurationPrevious](https://docs.comfy.org/manager/configuration)[Getting Started with AI Image GenerationNext](https://docs.comfy.org/get_started/first_generation)

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
