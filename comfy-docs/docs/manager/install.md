---
url: https://docs.comfy.org/manager/install/
title: ComfyUI-Manager Installation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:03.876347+00:00
---

# ComfyUI-Manager Installation - ComfyUI

> Source: https://docs.comfy.org/manager/install/

## On this page

  * Desktop users
  * Portable users
  * Manual install users
    * Command line options
    * Switch between new and legacy UI
  * Updating ComfyUI-Manager
  * Legacy installation methods



ComfyUI-Manager

# ComfyUI-Manager Installation

Copy pageCopy page

Install ComfyUI-Manager on Desktop, Portable, or manual ComfyUI setups to search, install, and update custom nodes from inside the app.

Copy pageCopy page

## 

​

Desktop users

Comfy Desktop installs ComfyUI-Manager with every ComfyUI installation and starts it with `--enable-manager`, so there is nothing for you to install. Manager is configured per installation from inside the app:

1

Open the Manage panel for the installation

In Comfy Desktop, open the installation and go to the **Manage panel** , then switch to the **Startup Args** tab.

2

Set the Manager options

  * **Manager Security Level** decides which node packs Manager may install: **Strict** , **Standard** (recommended), **Relaxed** , or **Permissive**. Stricter levels matter most when ComfyUI is exposed to your network with `--listen`
  * **Manager Network Mode** decides how Manager reaches the node registry: **Public** (default), **Private** , **Offline** , or **Personal cloud** (only for a machine you control)

Both options apply the next time you launch the installation.

3

Change the flags Manager starts with (optional)

**Startup Arguments** on the same tab controls the flags the installation launches with. Remove `--enable-manager` to run ComfyUI without Manager, or keep it and add `--disable-manager-ui` to hide the Manager UI while its background tasks continue.

See the [Startup Args tab](https://docs.comfy.org/installation/desktop/usage/manage#startup-args-tab) for the rest of the per-installation settings and the [startup flags reference](https://docs.comfy.org/development/comfyui-server/startup-flags) for the Manager flags.

## 

​

Portable users

For users running the [Windows Portable](https://docs.comfy.org/installation/comfyui_portable_windows) version, the new ComfyUI-Manager is built into ComfyUI core but needs to be enabled.

  1. Install the manager dependencies:
         
         .\python_embeded\python.exe -m pip install -r ComfyUI\manager_requirements.txt
         

  2. Launch ComfyUI with the manager enabled:
         
         .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-manager
         pause
         




## 

​

Manual install users

For users with a [manual installation](https://docs.comfy.org/installation/manual_install), the new ComfyUI-Manager is built into ComfyUI core but needs to be enabled.

  1. Activate your virtual environment:
         
         # Windows
         venv\Scripts\activate
         
         # Linux/macOS
         source venv/bin/activate
         

  2. Install the manager dependencies:
         
         pip install -r manager_requirements.txt
         

  3. Enable the manager with the `--enable-manager` flag when running ComfyUI:
         
         python main.py --enable-manager
         




### 

​

Command line options

Flag| Description  
---|---  
`--enable-manager`| Enable ComfyUI-Manager  
`--enable-manager-legacy-ui`| Use the legacy manager UI instead of the new UI (requires `--enable-manager`)  
`--disable-manager-ui`| Disable the manager UI and endpoints while keeping background features (requires `--enable-manager`)  
  
### 

​

Switch between new and legacy UI

The following version updates only support pip installations. Versions installed via custom nodes do not support switching to the new UI.

  * Non-Desktop users

  * Desktop users




To use the new UI:
    
    
    python main.py --enable-manager
    

To use the legacy UI:
    
    
    python main.py --enable-manager --enable-manager-legacy-ui
    

Desktop users can switch to the legacy UI in **Server Settings → UI Settings → Use legacy manager interface**![Switch to legacy UI](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5a47648f9d602868c022a17b01c4d2df)

## 

​

Updating ComfyUI-Manager

ComfyUI-Manager ships as its own Python package, and ComfyUI core pins the version it works with in `manager_requirements.txt`. How you update the Manager depends on how ComfyUI is installed:

  * Desktop

  * Portable and manual installs

  * Git clone




Desktop includes the Manager and keeps it current with Comfy Desktop updates. Update the ComfyUI engine from the [Manage panel](https://docs.comfy.org/installation/desktop/usage/manage#update-tab).

Updating ComfyUI may leave the installed Manager package unchanged. Install the manager requirements in the environment you launch ComfyUI from, then restart ComfyUI with `--enable-manager`:
    
    
    # Portable (Windows)
    .\python_embeded\python.exe -m pip install -r ComfyUI\manager_requirements.txt
    .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-manager
    
    # Manual install
    pip install -r manager_requirements.txt
    python main.py --enable-manager
    

If you cloned the Manager into `custom_nodes` yourself:
    
    
    cd ComfyUI/custom_nodes/comfyui-manager
    git pull
    

Then restart ComfyUI.

## 

​

Legacy installation methods

Method 1: Git clone (general installation)

To install ComfyUI-Manager in addition to an existing installation of ComfyUI:

  1. Navigate to `ComfyUI/custom_nodes` directory in terminal
  2. Clone the repository: 
         
         git clone https://github.com/Comfy-Org/ComfyUI-Manager comfyui-manager
         

  3. Install the manager dependencies: 
         
         cd comfyui-manager
         pip install -r requirements.txt
         

  4. Restart ComfyUI



Method 2: Portable version (Windows)

  1. Install [Git for Windows](https://git-scm.com/download/win) (standalone version, select “use windows default console window”)
  2. Download [install-manager-for-portable-version.bat](https://github.com/Comfy-Org/ComfyUI-Manager/raw/main/scripts/install-manager-for-portable-version.bat) into your `ComfyUI_windows_portable` directory
  3. Double-click the batch file to install



Method 3: comfy-cli (recommended for new installations)

comfy-cli provides various features to manage ComfyUI from the CLI.**Prerequisites** : Python 3, Git**Windows:**
    
    
     python -m venv venv
    venv\Scripts\activate
    pip install comfy-cli
    comfy install
    

**Linux/macOS:**
    
    
     python -m venv venv
    . venv/bin/activate
    pip install comfy-cli
    comfy install
    

See also: [comfy-cli documentation](https://docs.comfy.org/comfy-cli/getting-started)

Method 4: Linux + venv

**Prerequisites** : python-is-python3, python3-venv, git

  1. Download [install-comfyui-venv-linux.sh](https://github.com/comfy-org/ComfyUI-Manager/raw/main/scripts/install-comfyui-venv-linux.sh) into an empty install directory
  2. Run: 
         
         chmod +x install-comfyui-venv-linux.sh
         ./install-comfyui-venv-linux.sh
         

  3. Execute ComfyUI with `./run_gpu.sh` or `./run_cpu.sh`



**Installation precautions:**

  * ComfyUI-Manager files must be accurately located in the path `ComfyUI/custom_nodes/comfyui-manager`
  * Do not decompress directly into `ComfyUI/custom_nodes` (files like `__init__.py` should not be in that directory)
  * Do not install in paths like `ComfyUI/custom_nodes/ComfyUI-Manager/ComfyUI-Manager` or `ComfyUI/custom_nodes/ComfyUI-Manager-main`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/manager/install.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/manager/install)

[ComfyUI-Manager OverviewPrevious](https://docs.comfy.org/manager/overview)[Custom nodes (new UI)Next](https://docs.comfy.org/manager/pack-management)

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
