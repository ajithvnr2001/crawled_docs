---
url: https://docs.comfy.org/installation/desktop/macos/
title: Comfy Desktop for macOS - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:57.576042+00:00
---

# Comfy Desktop for macOS - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/macos/

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

# Comfy Desktop for macOS

Copy pageCopy page

Install Comfy Desktop on macOS: system requirements, setup steps, updates, and a clean uninstall for running ComfyUI locally on Apple silicon Macs.

Copy pageCopy page

**Comfy Desktop** is a multi-installation manager that lets you run multiple ComfyUI instances from a single launcher. This guide covers how to install and uninstall Comfy Desktop on macOS.

## 

​

System Requirements

  * **OS:** macOS 13 (Ventura) or later
  * **Hardware:** Apple Silicon (M1 or later)
  * **Disk Space:** At least 4.85 GB recommended per installation



## Download Comfy Desktop

Download the latest installer for macOS. The page will automatically detect your platform.

## 

​

Installation

  1. Open the downloaded `.dmg` file
  2. Drag **Comfy Desktop** into the **Applications** folder
  3. Launch it from Launchpad or Spotlight

![Desktop MacOS](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/mac_1_install.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=32a354755add8f6d72a0787b9ad42b67) The first time you launch, macOS may show a security warning. Go to **System Settings → Privacy & Security** and click **Open Anyway** to allow it.

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

  1. Open **Applications** folder in Finder
  2. Right-click **Comfy Desktop** and select **Move to Trash**

![Uninstall Comfy Desktop on macOS](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/mac_2_uninstall.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=2b2704e427cfefa46b1a545ed55c498d)

### 

​

What Uninstalling the App Does NOT Remove

Uninstalling Comfy Desktop only removes the launcher app itself. The following data is **not** removed and must be deleted manually if you want a complete cleanup:

Data| Default Location| Description  
---|---|---  
Installations| `~/ComfyUI-Installs`| Each ComfyUI installation you created (can also be deleted from within the app). Custom install paths are also not removed.  
Shared models & outputs| `~/ComfyUI-Shared`| Shared model library, input/output directories  
App settings & registry| `~/Library/Application Support/Comfy Desktop`| Settings and installation records  
Logs| `~/Library/Logs/Comfy Desktop`| Desktop app logs (`app.log`)  
  
The directories listed above contain your **personal ComfyUI data** (models, outputs, settings, and installations). They are **not** Comfy Desktop application files. Deleting them will permanently remove your data.

To fully remove everything:

  1. **Delete the app data folder** : `~/Library/Application Support/Comfy Desktop`
  2. **Delete the logs folder** : `~/Library/Logs/Comfy Desktop`
  3. **Delete individual installations** from within the app, or manually delete `~/ComfyUI-Installs` plus any custom installation directories you configured
  4. **Delete the shared model library** at `~/ComfyUI-Shared` (only if you no longer need these files)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/macos.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/macos)

[Comfy Desktop for WindowsPrevious](https://docs.comfy.org/installation/desktop/windows)[Comfy Desktop on LinuxNext](https://docs.comfy.org/installation/desktop/linux)

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
