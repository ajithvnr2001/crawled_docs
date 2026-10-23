---
url: https://docs.comfy.org/installation/update_comfyui/
title: How to Update ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:59.556275+00:00
---

# How to Update ComfyUI - ComfyUI

> Source: https://docs.comfy.org/installation/update_comfyui/

## On this page

  * How to Update ComfyUI?
  * ComfyUI Version Types
  * What Needs to Be Updated When Updating ComfyUI?
  * Common Update Issues
    * Missing or Outdated Frontend, Workflow Templates, Node After Updates
    * How to Properly Update Core Dependencies
    * Core Dependency Update Troubleshooting
    * Why Can’t I Find New Features After Updating?
    * How to Switch Between Development (Nightly) and Stable (Release) Versions?
    * What to Do When Errors Occur After Updates?
    * How to Stay Updated on New Features?



Local (Self-Hosted)

# How to Update ComfyUI

Copy pageCopy page

Update ComfyUI on any install type: Portable update scripts, Desktop updates, and git pull for manual installs, plus fixes for common update issues.

Copy pageCopy page

While we’ve covered ComfyUI updates across different installation methods in various sections, this comprehensive guide consolidates all update procedures to help users clearly understand how to update ComfyUI.

## 

​

How to Update ComfyUI?

  * Portable

  * Desktop

  * Manual Installation




ComfyUI Portable provides convenient batch scripts for easy updates.

### 

​

Update Script Location

In the `update` folder within your portable installation directory, you’ll find the following update scripts:
    
    
    ComfyUI_windows_portable
    └─ 📂update
       ├── update.py
       ├── update_comfyui.bat                           // Update to latest development version
       ├── update_comfyui_stable.bat                    // Update to latest stable version
       └── update_comfyui_and_python_dependencies.bat   // ⚠️ DANGER: Reinstalls dependencies - may cause conflicts
    

Ensure a stable internet connection during updates.

**⚠️ DANGER: Use`update_comfyui_and_python_dependencies.bat` with extreme caution!**This script is more thorough than regular updates and will:

  * ✅ Update ComfyUI code itself
  * ✅ Update PyTorch (for NVIDIA GPU CUDA 12.9)
  * ✅ Reinstall ALL Python dependencies

**Risks:**

  * May cause dependency conflicts with your existing setup
  * Can break custom nodes that rely on specific package versions
  * May overwrite manually configured packages

**⚠️ Only use this script when:**

  * You need to fix dependency issues
  * Performing major version updates
  * For daily updates, use `update_comfyui.bat` instead

**Before running this script:**

  1. **Back up your entire ComfyUI installation**
  2. Document any custom package versions you’ve installed
  3. Be prepared to reinstall custom nodes if needed



Comfy Desktop uses Comfy Engine as a package manager to manage ComfyUI. To update the ComfyUI engine, open the [Manage panel](https://docs.comfy.org/installation/desktop/usage/manage#update-tab) and use the Update tab. You can choose between **Stable** (default) and **Latest on GitHub** update channels.The Desktop app itself updates automatically and is separate from ComfyUI engine updates.

Manually installed ComfyUI requires Git commands to complete updates.

### 

​

Pre-Update Requirements

Ensure your system has [Git](https://git-scm.com/downloads) installed and ComfyUI was installed via Git clone.

### 

​

Update Steps

1

Activate Virtual Environment

First, activate ComfyUI’s Python virtual environment (if using one):
    
    
    # For conda environment
    conda activate comfyui
    
    # For venv environment
    # Windows
    venv\Scripts\activate
    # macOS/Linux  
    source venv/bin/activate
    

2

Pull Latest Code

Navigate to your ComfyUI installation directory and pull the latest code:
    
    
    cd <ComfyUI-installation-path>
    git pull
    

3

Update Dependencies

Install or update ComfyUI’s dependency packages:
    
    
    pip install -r requirements.txt
    

Ensure you’re in ComfyUI’s virtual environment to avoid contaminating the system-level Python environment

4

Restart ComfyUI

After updating, restart ComfyUI:
    
    
    python main.py
    

### 

​

Version Switching (Optional)

To switch to a specific version, use these commands:
    
    
    # View commit history
    git log --oneline
    
    # Switch to specific commit
    git checkout <commit-hash>
    
    # Return to latest version
    git checkout master
    

Regular updates are recommended for the latest features and security fixes, while stable versions are recommended for system stability

## 

​

ComfyUI Version Types

Depending on your installation method, ComfyUI offers several installation versions. The links below contain update instructions for each version.

Comfy Desktop

Comfy Desktop supports standalone installation on **Windows** , **macOS (Apple Silicon)** , and **Linux** (AppImage and `.deb`).

  * Source is on [GitHub](https://github.com/Comfy-Org/Comfy-Desktop)



Desktop installs track the **stable** ComfyUI release by default. If you want every latest commit, use the portable version or a manual git install, or switch the instance update channel to **Latest on GitHub**.

You can choose the appropriate installation for your system and hardware below

  * Windows

  * macOS (Apple Silicon)

  * Linux




## Comfy Desktop (Windows) Installation Guide

Suitable for **Windows** 10 or later. NVIDIA or AMD GPU recommended.

## Comfy Desktop (macOS) Installation Guide

Suitable for macOS with **Apple Silicon**

## Comfy Desktop (Linux) Installation Guide

Install the AppImage or `.deb`, or build and run from source.

ComfyUI Portable (Windows)

Portable version is a ComfyUI version that integrates an independent embedded Python environment, using the portable version you can experience the latest features, currently only supports **Windows** system

## ComfyUI Portable (Windows) Installation Guide

Supports **Windows** ComfyUI version running on **Nvidia GPUs** or **CPU-only** , always use the latest commits and completely portable.

Manual Installation

## ComfyUI Manual Installation Guide

Supports all system types and GPU types (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)

## 

​

What Needs to Be Updated When Updating ComfyUI?

ComfyUI updates primarily consist of two components:

  1. Update ComfyUI’s core code
  2. Update ComfyUI’s core dependencies, including necessary Python dependencies and ComfyUI functional dependency packages

**Core Code** : New nodes, new model support, new features, etc. **Core Dependencies** : Mainly includes ComfyUI’s frontend functionality, workflow templates, node help documentation, etc.
    
    
    comfyui-frontend-package   # ComfyUI frontend functionality
    comfyui-workflow-templates # ComfyUI workflow templates  
    comfyui-embedded-docs      # ComfyUI node help documentation
    comfy-kitchen              # ComfyUI core utilities
    comfy-aimdo                # ComfyUI core utilities
    

These core dependencies are maintained in separate repositories:

  * [ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend/) \- Frontend interface and interactive features
  * [workflow_templates](https://github.com/Comfy-Org/workflow_templates) \- Pre-built workflow templates
  * [comfyui-embedded-docs](https://github.com/Comfy-Org/embedded-docs) \- Node help documentation
  * [comfy-kitchen](https://github.com/Comfy-Org/comfy-kitchen) \- Fast kernel library for Diffusion inference with multiple compute backends
  * [comfy-aimdo](https://github.com/Comfy-Org/comfy-aimdo) \- AI Model Demand Offloading Allocator

It’s important to understand the difference between development (nightly) and stable (release) versions:

  * **Development version (nightly)** : Latest commit code, giving you access to the newest features, but may contain potential issues
  * **Stable version (release)** : Built on stable releases, usually lags behind development versions but offers higher stability. We support stable versions after features are tested and stabilized

Many users often find themselves on release versions or desktop versions during updates, but discover that needed features are only available in development versions. In such cases, check if your local `ComfyUI/requirements.txt` matches the [nightly version dependencies](https://github.com/Comfy-Org/ComfyUI/blob/master/requirements.txt) to determine if all dependencies support the latest features.

## 

​

Common Update Issues

### 

​

Missing or Outdated Frontend, Workflow Templates, Node After Updates

  * Dependencies Not Properly Updated

  * Dependency Update Failures




Users often only use the `git pull` command to update ComfyUI code but **neglect core dependency updates** , leading to the following issues:

  * Missing or abnormal frontend functionality
  * Cannot find newly added workflow templates
  * Outdated or missing node help documentation
  * New features lack corresponding frontend support

After using the `git pull` command, use the corresponding ComfyUI environment to use `pip install -r requirements.txt` to update dependencies.

If dependency updates fail, it’s commonly due to network or computer permission issues. When core dependency failures occur during updates, the system falls back to older versions. You’ll typically see logs like this during startup:
    
    
    Falling back to the default frontend.
    ComfyUI frontend version: xxx
    

Follow these troubleshooting steps:

  1. Use `pip list` in the appropriate environment to view currently installed dependency packages. If you find version inconsistencies, use `pip install -r requirements.txt` in the ComfyUI environment to attempt dependency updates again.
  2. If issues persist after updating, check your network connection. Users in mainland China may need to configure a proxy to reliably access GitHub repositories.
  3. If problems continue, check computer permissions. If administrator privileges are required, run the command line with administrator rights.



### 

​

How to Properly Update Core Dependencies

  * Portable

  * Manual Installation

  * Desktop




**Recommended Method** : Use the `ComfyUI_windows_portable\update\update_comfyui.bat` batch script, which will update both ComfyUI code and all Python dependencies.**Manual Dependency Update** : If you need to manually update dependencies, use the following command:
    
    
    # Open command line in portable version directory
    .\python_embeded\python.exe -m pip install -r ComfyUI\requirements.txt
    

1

Activate Python Environment

If you use Conda to manage Python environments, activate your environment first:
    
    
    conda activate comfyui  # or other environment name
    

2

Update Code

Navigate to the ComfyUI root directory and update the code using Git:
    
    
    cd <ComfyUI_ROOT_PATH>
    git pull
    

3

Update Dependencies

Update ComfyUI dependencies - this step is crucial, especially for the `comfyui-frontend-package`:
    
    
    pip install -r requirements.txt
    

Desktop version usually handles dependency updates automatically. If you encounter issues:

  1. **Check if auto-update** is enabled
  2. **Manually trigger update** : Menu → Help → Check for Updates
  3. **Reinstall desktop version** (in extreme cases)



### 

​

Core Dependency Update Troubleshooting

If core dependency updates fail, follow these troubleshooting steps:

1

Check Network Connection

If located in mainland China, ensure you can access PyPI or configure a domestic mirror:
    
    
    # Using Tsinghua University mirror
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    

2

Install Core Packages Individually

If batch installation fails, try installing packages individually. **First check version requirements in`ComfyUI/requirements.txt`**:**Then install according to specified versions (use version numbers from your requirements.txt):**
    
    
     pip install comfyui-frontend-package==<version> 
    pip install comfyui-workflow-templates==<version>
    pip install comfyui-embedded-docs==<version>
    pip install comfy-kitchen==<version>
    pip install comfy-aimdo==<version>
    

It’s recommended to use the exact version numbers specified in `ComfyUI/requirements.txt`. Don’t upgrade to the latest versions independently, as this may cause compatibility issues.

### 

​

Why Can’t I Find New Features After Updating?

This is one of the most common issues:

  * If you’re using the **Desktop version** , features may lag behind because the desktop version is built on stable releases
  * Ensure you’re using the **development version (nightly)** , not the **stable version (release)**

Additionally, ensure that corresponding dependencies have been successfully updated during the update process. If issues persist after updating, refer to the Dependency Update Troubleshooting section to diagnose problems.

### 

​

How to Switch Between Development (Nightly) and Stable (Release) Versions?

Differences between versions:

  * Development Version (Nightly)

  * Stable Version (Release)




  * **Characteristics** : Contains the latest commit code
  * **Advantages** : Experience the latest features and improvements first
  * **Risks** : May contain undiscovered bugs or unstable factors
  * **Suitable for** : Developers, testers, users wanting to experience the latest features



  * **Characteristics** : Tested and verified stable code
  * **Advantages** : High stability, suitable for production environments
  * **Disadvantages** : Feature updates have delays, may lag behind development versions by weeks or months
  * **Suitable for** : Users requiring stability, production environment users



  * Portable

  * Manual Installation

  * Desktop




Use `update_comfyui.bat` instead of `update_comfyui_stable.bat`:
    
    
    # Development version (latest features)
    double-click: update_comfyui.bat
    
    # Stable version
    double-click: update_comfyui_stable.bat
    
    
    
    # Switch to development version
    git checkout master
    git pull
    
    # Switch to latest stable version
    git fetch --tags
    git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
    

Desktop version is typically built on stable releases and doesn’t currently support version switching. If you need the latest features, we recommend:

  1. Wait for desktop version updates
  2. Or use portable/manual installation to experience the latest features



### 

​

What to Do When Errors Occur After Updates?

  1. **Check Dependencies** : Run `pip install -r requirements.txt` to ensure all dependencies are updated
  2. **Check Custom Nodes** : Some custom nodes may be incompatible with new versions
  3. **Roll Back Version** : If issues are severe, you can roll back to a previous stable version

If problems occur, refer to our troubleshooting page for solutions.

## Troubleshooting

Learn how to troubleshoot ComfyUI issues

### 

​

How to Stay Updated on New Features?

  * **GitHub Releases** : Check [ComfyUI Releases](https://github.com/Comfy-Org/ComfyUI/releases) for stable version updates
  * **GitHub Commits** : View [latest commits](https://github.com/Comfy-Org/ComfyUI/commits/master) to understand development progress
  * **Community Discussion** : Follow our [blog](https://blog.comfy.org) and [Twitter](https://x.com/comfyui) for the latest updates



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/update_comfyui.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/update_comfyui)

[Install ComfyUI Manually (Windows, macOS, Linux)Previous](https://docs.comfy.org/installation/manual_install)[Comfy Cloud - Official ComfyUI Cloud Platform Powered by RTX 6000 ProNext](https://docs.comfy.org/get_started/cloud)

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
