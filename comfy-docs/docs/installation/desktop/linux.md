---
url: https://docs.comfy.org/installation/desktop/linux/
title: Comfy Desktop on Linux - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:32.945893+00:00
---

# Comfy Desktop on Linux - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/linux/

## On this page

Back to top

  * System Requirements
  * Install the official package
  * Build and run from source
    * Prerequisites
    * Clone and install
    * Start the app
  * Updating
    * .deb installs
    * AppImage
    * Source checkout
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
    

The `.deb` package installs Comfy Desktop under `/opt/Comfy Desktop` and, during installation, adds an APT source for Comfy Desktop’s package repository, so later releases arrive through your system package manager. See Updating. When AppArmor is enabled and its parser accepts the bundled profile (Ubuntu 24.04 and later, where unprivileged user namespaces are restricted), the package also installs an AppArmor profile for the app at `/etc/apparmor.d/comfyui-desktop-2`. Electron’s sandbox therefore works on those systems without extra flags. Older distributions skip the profile because their AppArmor cannot load it, and the sandbox works there without it. Where unprivileged user namespaces do not work at all, the package marks its `chrome-sandbox` helper setuid instead. To check whether the profile was installed:
    
    
    ls /etc/apparmor.d/comfyui-desktop-2
    

The package’s install scripts write the profile whenever the package is installed or upgraded. If you installed the `.deb` on Ubuntu 22.04 and later upgraded the system to 24.04, run the install scripts again:
    
    
    sudo apt reinstall comfyui-desktop-2
    

For the AppImage:
    
    
    chmod +x ./*.AppImage
    ./*.AppImage
    

The AppImage runs no package install scripts, so it adds neither the AppArmor profile nor the APT source. Launching it from the app menu already passes `--no-sandbox`. If you start the file directly and it fails to launch, your distribution may be blocking Electron’s sandbox, so add the flag:
    
    
    ./*.AppImage --no-sandbox
    

That flag disables Electron sandboxing for every process, so only use it when the sandboxed launch fails.

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

How Comfy Desktop updates depends on how you installed it.

### 

​

.deb installs

Installing the `.deb` also adds an APT source (`/etc/apt/sources.list.d/comfyui-desktop-2.sources`) and an unattended-upgrades entry for it, so new releases arrive with your normal system updates:
    
    
    sudo apt update
    sudo apt upgrade
    

You do not need to download the `.deb` again for each release. `sudo apt remove comfyui-desktop-2` leaves the APT source on disk; `sudo apt purge comfyui-desktop-2` removes it together with the unattended-upgrades entry.

### 

​

AppImage

The AppImage updates itself: Comfy Desktop downloads the new build and replaces the `.AppImage` file you launched, so keep it in a folder your user account can write to. If the file sits in a read-only location, the update cannot replace it.

### 

​

Source checkout

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

Removing the app and removing your data are separate steps. Uninstall the app first:

  * **`.deb`** : `sudo apt remove comfyui-desktop-2`. The removal also deletes the AppArmor profile at `/etc/apparmor.d/comfyui-desktop-2`. Use `sudo apt purge comfyui-desktop-2` to remove the APT source and the unattended-upgrades entry too.
  * **AppImage** : delete the `.AppImage` file.

Neither touches your ComfyUI installations or app data. Delete these folders only if you want a complete cleanup:

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

[macOS](https://docs.comfy.org/installation/desktop/macos)[Overview](https://docs.comfy.org/installation/desktop/usage/overview)
