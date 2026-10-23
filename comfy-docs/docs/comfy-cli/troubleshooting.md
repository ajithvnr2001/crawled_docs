---
url: https://docs.comfy.org/comfy-cli/troubleshooting/
title: Comfy CLI Troubleshooting Guide - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:36.042635+00:00
---

# Comfy CLI Troubleshooting Guide - ComfyUI

> Source: https://docs.comfy.org/comfy-cli/troubleshooting/

## On this page

  * Prerequisites
  * Install ComfyUI in a virtual environment
  * Install the PyTorch build that matches your GPU
  * Set up Comfy Cloud without a browser
  * Get more help



Comfy CLI

# Comfy CLI Troubleshooting Guide

Copy pageCopy page

Fix common Comfy CLI setup problems: missing git, Python and virtual environment requirements, headless Comfy Cloud auth, and GPU library installs.

Copy pageCopy page

Most Comfy CLI failures come from a missing prerequisite or a setup step that was skipped. Check the items below before reporting a problem.

## 

​

Prerequisites

Comfy CLI needs [git](https://git-scm.com/downloads) installed on your system. Install it first, so `comfy install` and `comfy update` can clone ComfyUI and its custom nodes.

## 

​

Install ComfyUI in a virtual environment

`comfy install` installs ComfyUI into the active Python environment, which must be Python 3.10 or newer. Create and activate a virtual environment before running it:
    
    
    python3 -m venv comfy-env
    source comfy-env/bin/activate
    comfy install
    

## 

​

Install the PyTorch build that matches your GPU

`comfy install` asks which GPU you have and installs the matching PyTorch build. Answer the prompt, or pass a GPU flag so the command can run unattended:

Platform| What `comfy install` installs| What you still need  
---|---|---  
NVIDIA| PyTorch with CUDA runtime (pip wheel)| Current GPU driver (not the full CUDA Toolkit)  
AMD Linux| ROCm PyTorch wheels| ROCm-capable AMD GPU driver/stack for those wheels  
AMD Windows| `torch-directml`| Compatible AMD GPU (DirectML; not ROCm)  
Apple silicon| PyTorch nightly wheels (CPU index; Metal/MPS)| macOS on Apple silicon  
Intel Arc| PyTorch XPU wheels| Compatible Intel Arc GPU / XPU stack  
CPU| CPU PyTorch wheels| No discrete GPU required  
      
    
    comfy install --nvidia
    

Pass `--skip-torch-or-directml` if you install PyTorch yourself. `comfy env` prints the Python environment and workspace ComfyUI uses.

## 

​

Set up Comfy Cloud without a browser

`comfy setup` signs in through your browser, so it cannot complete in CI, a devcontainer, or a headless server. Pass an API key and run non-interactive instead:
    
    
    comfy setup --where cloud --api-key comfyui-... --non-interactive
    

## 

​

Get more help

  * [Get Started with Comfy CLI](https://docs.comfy.org/comfy-cli/getting-started) covers install, routing, and generation.
  * [Comfy CLI Command Reference](https://docs.comfy.org/comfy-cli/reference) lists every command and flag.
  * Report a reproducible CLI bug in the [comfy-cli repository](https://github.com/Comfy-Org/comfy-cli/issues).



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/comfy-cli/troubleshooting.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/comfy-cli/troubleshooting)

[Comfy CLI Command ReferencePrevious](https://docs.comfy.org/comfy-cli/reference)[Workflow JSONNext](https://docs.comfy.org/specs/workflow_json)

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
