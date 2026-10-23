---
url: https://docs.comfy.org/installation/desktop/windows/
title: Comfy Desktop for Windows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:58.941471+00:00
---

# Comfy Desktop for Windows - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/windows/

## On this page

  * System Requirements
  * Installation
  * Updating Comfy Desktop
  * Quick Update
  * Manual Update via Settings
  * Uninstalling
    * Remove Comfy Desktop
    * What Uninstalling the App Does NOT Remove



Installation

# Comfy Desktop for Windows

Copy pageCopy page

Install Comfy Desktop on Windows: system requirements, setup steps, updates, and a clean uninstall for running ComfyUI locally on Windows 10 and later.

Copy pageCopy page

**Comfy Desktop** is a multi-installation manager that lets you run multiple ComfyUI instances from a single launcher. This guide covers how to install and uninstall Comfy Desktop on Windows.

## 

​

System Requirements

  * **OS:** Windows 10 or later
  * **Architecture:** x64 or ARM64
  * **GPU:** Dedicated GPU (NVIDIA / AMD) recommended for good performance, but not required
  * **Disk Space:** At least 4.85 GB recommended per installation



## Download Comfy Desktop

Download the latest installer for Windows. The page will automatically detect your platform.

## 

​

Installation

Run the downloaded `.exe` installer (NSIS installer) and follow the prompts. After installation, launch Comfy Desktop from the Start Menu or desktop shortcut. ![Windows setup](https://mintcdn.com/dripart/cAVuyhdaebQHS2CS/images/desktop/installation/windows_1_install.png?fit=max&auto=format&n=cAVuyhdaebQHS2CS&q=85&s=2f32d2b272b240371c7b2290343cf400) When you first open the app, the first-run setup asks how you want to run Comfy: on Comfy Cloud, or installed locally on this machine. See [First Launch](https://docs.comfy.org/installation/desktop/overview#first-launch) for the choices it collects.

**Already using Legacy Desktop?** Comfy Desktop can automatically detect and migrate your existing installation. Your custom nodes, workflows, models, and settings are carried over, and Comfy Desktop backs up your legacy state before it starts. The migration reuses your existing data folder and Python environment in place, so back them up yourself if you need a pristine copy.Learn more in the [Migrate from Legacy](https://docs.comfy.org/installation/desktop/usage/migrate) guide.

## Next Step: Using Comfy Desktop

Once installed, learn how to create instances, manage installations, and configure settings.

## 

​

Updating Comfy Desktop

Comfy Desktop automatically checks for updates and lets you manage them in two ways.

## 

​

Quick Update

When an update is available, a **Desktop Update Ready** button appears at the top of the window: ![Desktop Update Ready button](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/install_update_1.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=fc104f738021e738dd56c9b4f8fa64e5) Just click the ① Desktop Update Ready button and Comfy Desktop will restart and install the update automatically.

## 

​

Manual Update via Settings

You can also check for and manage updates from the Settings panel:

1

Open Desktop Settings

![Open Desktop Settings menu](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/install_update_2-1.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=a43d379acfb8f89a4d4adab5ce63a920)

  1. **①** Click the hamburger menu (top-left)
  2. **②** Select **Desktop Settings**



2

Updates Panel

![Updates panel in Desktop Settings](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/install_update_2-2.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=f5e9af07392438b02f41d0a2211b6bd1)In the **Updates** panel:

  1. **① Updates** — Click the sidebar Updates tab
  2. **② Check for updates** — Manually check for available updates
  3. **③ Restart & Update** — Appears when a new version is available; click to restart and update
  4. **④ Automatically install Desktop updates** — Toggle this on/off to control automatic updates



## 

​

Uninstalling

### 

​

Remove Comfy Desktop

  1. Go to **Settings → Apps → Installed apps**
  2. Find **Comfy Desktop** and click **Uninstall**

![Uninstall Comfy Desktop on Windows](https://mintcdn.com/dripart/cAVuyhdaebQHS2CS/images/desktop/installation/windows_2_uninstall.png?fit=max&auto=format&n=cAVuyhdaebQHS2CS&q=85&s=53de7983e9318d6aecad6e76a25c5efe)

### 

​

What Uninstalling the App Does NOT Remove

Uninstalling Comfy Desktop only removes the launcher app itself. The following data is **not** removed and must be deleted manually if you want a complete cleanup:

Data| Default Location| Description  
---|---|---  
Installations| `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs`| Each ComfyUI installation you created (can also be deleted from within the app). Custom install paths are also not removed. Older installs may still live in `%USERPROFILE%\ComfyUI-Installs`.  
Shared models & outputs| `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared`| Shared model library, input/output directories. Older installs may still use `%USERPROFILE%\ComfyUI-Shared`.  
App settings & registry| `%APPDATA%\Comfy Desktop`| Settings and installation records  
Logs| `%APPDATA%\Comfy Desktop\logs`| Desktop app logs (`app.log`)  
  
The directories listed above contain your **personal ComfyUI data** (models, outputs, settings, and installations). They are **not** Comfy Desktop application files. Deleting them will permanently remove your data.

To fully remove everything:

  1. **Delete the app data folder** : `%APPDATA%\Comfy Desktop`
  2. **Delete individual installations** from within the app, or manually delete `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs` (or `%USERPROFILE%\ComfyUI-Installs` if that is where they were created). Also delete any custom installation directories you configured
  3. **Delete the shared model library** at `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared` (or `%USERPROFILE%\ComfyUI-Shared`) only if you no longer need these files



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/windows.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/windows)

[Comfy Desktop OverviewPrevious](https://docs.comfy.org/installation/desktop/overview)[Comfy Desktop for macOSNext](https://docs.comfy.org/installation/desktop/macos)

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
