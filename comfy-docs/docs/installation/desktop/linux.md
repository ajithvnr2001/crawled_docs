---
url: https://docs.comfy.org/installation/desktop/linux/
title: Comfy Desktop on Linux - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:57.115786+00:00
---

# Comfy Desktop on Linux - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/linux/

## On this page

  * System Requirements
  * Install the official package
  * Build and run from source
    * Prerequisites
    * Clone and install
    * Start the app
  * Updating
  * Optional: local package
  * Removing leftover data



Installation

# Comfy Desktop on Linux

Copy pageCopy page

Install Comfy Desktop on Linux using the official .deb or AppImage packages. Source builds need Ubuntu 22.04+, x64, and Node.js v22 LTS.

Copy pageCopy page

**Comfy Desktop** can run on Linux. Official `.deb` (Debian/Ubuntu) and AppImage packages are distributed through the [Comfy Desktop repository](https://github.com/Comfy-Org/Comfy-Desktop). Download them with the [universal download link](https://dl.todesktop.com/241130tqe9q3y), which auto-detects your platform. Most users should use one of those packages. If you want to run the app from source instead, clone the repository and follow the steps below.

## 

​

System Requirements

  * **OS:** Linux (Ubuntu 22.04 or later recommended)
  * **Architecture:** x64
  * **Node.js:** v22 LTS or later (source build only)
  * **pnpm:** v10 or later, enabled with Corepack (source build only)
  * **Build tools:** `build-essential` and `git` (source build only)
  * **GPU:** A dedicated GPU (NVIDIA / AMD) is recommended, but not required
  * **Disk Space:** At least 4.85 GB recommended per ComfyUI installation



## 

​

Install the official package

Download the Linux package with the [universal download link](https://dl.todesktop.com/241130tqe9q3y) (it auto-detects your platform), then install it:
    
    
    sudo apt install ./*.deb
    

For the AppImage:
    
    
    chmod +x ./*.AppImage
    ./*.AppImage
    

If the app fails to launch, your distribution may be blocking Electron’s sandbox (Ubuntu 24.04+ restricts unprivileged user namespaces through AppArmor). In that case retry with `--no-sandbox`. Note that this flag disables Electron sandboxing for every process, so only use it when sandboxed launches fail.

## 

​

Build and run from source

These steps match the [Development](https://github.com/Comfy-Org/Comfy-Desktop#development) section in the repository README.

### 

​

Prerequisites

Install the build tools and git first. A fresh Ubuntu install ships without them, and `pnpm run init` compiles native modules such as `node-pty`, which fails with `Error: not found: make` if `build-essential` is missing:
    
    
    sudo apt install build-essential git
    

Then install Node.js 22 and enable pnpm:
    
    
    nvm install 22 && nvm use 22
    corepack enable
    

If you do not use nvm, install Node.js 22 from [nodejs.org](https://nodejs.org/) instead.

### 

​

Clone and install
    
    
    git clone https://github.com/Comfy-Org/Comfy-Desktop.git
    cd Comfy-Desktop
    pnpm run init
    

`pnpm run init` installs dependencies and builds the bundled bootstrap Python.

### 

​

Start the app
    
    
    ./linux-dev.sh
    

This starts Comfy Desktop in development mode. The script sets `ELECTRON_DISABLE_SANDBOX=1` because Electron’s sandbox often fails in Linux dev environments.

## Next Step: Using Comfy Desktop

Once the app is running, learn how to create instances, manage installations, and configure settings.

## 

​

Updating

There is no in-app auto-update for a source checkout. Pull the latest code and start the app again:
    
    
    git pull
    pnpm run init
    ./linux-dev.sh
    

## 

​

Optional: local package

To produce a local `.deb` or AppImage for yourself (not an official Comfy Org download):
    
    
    pnpm run build:linux
    

Artifacts land in `dist/`. If an AppImage fails because Chromium cannot create a sandbox, retry with `--no-sandbox`. That flag disables Electron sandboxing for every process.

## 

​

Removing leftover data

Stopping the source checkout does not delete ComfyUI installations or app data. Delete these folders only if you want a complete cleanup:

Data| Default Location| Description  
---|---|---  
Installations| `~/ComfyUI-Installs`| Each ComfyUI installation you created (can also be deleted from within the app). Custom install paths are also not removed.  
Shared models & outputs| `~/ComfyUI-Shared`| Shared model library, input/output directories  
App config| `~/.config/comfyui-desktop-2`| Settings and installation records  
App data| `~/.local/share/comfyui-desktop-2`| Persistent app data  
Cache| `~/.cache/comfyui-desktop-2`| Download cache and other non-essential files  
State| `~/.local/state/comfyui-desktop-2`| Runtime state such as port locks  
Logs| `~/.config/comfyui-desktop-2/logs`| Desktop app logs (`app.log`)  
  
To fully remove everything:

  1. **Delete the clone** of `Comfy-Desktop`
  2. **Delete the config folder** : `~/.config/comfyui-desktop-2`
  3. **Delete the data, cache, and state folders** : `~/.local/share/comfyui-desktop-2`, `~/.cache/comfyui-desktop-2`, and `~/.local/state/comfyui-desktop-2`
  4. **Delete individual installations** from within the app, or manually delete `~/ComfyUI-Installs` plus any custom installation directories you configured
  5. **Delete the shared model library** at `~/ComfyUI-Shared` (only if you no longer need these files)

Packaged installs (`.deb` or AppImage) also keep the app profile and logs in `~/.config/Comfy Desktop`. To clear those, run the repository’s [reset-linux.sh](https://github.com/Comfy-Org/Comfy-Desktop/blob/main/scripts/reset-linux.sh) script; it removes every known app data location but leaves your `~/ComfyUI-Installs` untouched.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/linux.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/linux)

[Comfy Desktop for macOSPrevious](https://docs.comfy.org/installation/desktop/macos)[Using Comfy DesktopNext](https://docs.comfy.org/installation/desktop/usage/overview)

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
