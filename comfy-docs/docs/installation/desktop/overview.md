---
url: https://docs.comfy.org/installation/desktop/overview/
title: Comfy Desktop Overview - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:57.477764+00:00
---

# Comfy Desktop Overview - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/overview/

## On this page

  * Get Started
  * First Launch
    * Cloud or Local
    * Terms and data sharing
    * Express Install
    * Migrating an existing install
    * Chinese mirrors
    * After setup
  * Usage Guide
  * Migrate from Legacy Desktop
  * Open Source



Comfy Desktop

# Comfy Desktop Overview

Copy pageCopy page

Comfy Desktop overview: a desktop app that installs, manages, and launches multiple instances of ComfyUI, the node-based engine for generative AI.

Copy pageCopy page

**Comfy Desktop** is a desktop application that lets you install, manage, and launch multiple ComfyUI instances from a single launcher. To put it simply: **Comfy Desktop** is the app that manages and launches **ComfyUI** , the node-based engine for generative AI. You don’t install ComfyUI separately — Comfy Desktop handles the installation, Python environment, and dependencies for you. Each ComfyUI instance runs independently with its own version, custom nodes, and settings. ![Comfy Desktop dashboard with instance cards](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/01-homepage.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=3e4bf3a9d50aef3ab85fba271b1c945e) Comfy Desktop runs on **Windows 10+** , **macOS 13+ (Apple Silicon)** , and **Linux** (official `.deb` and AppImage packages). Each standalone installation requires at least **4.85 GB** of disk space and **8 GB RAM (16 GB recommended)**. Check the platform-specific pages for full details.

## 

​

Get Started

Choose your platform to begin:

## Windows

Step-by-step installation guide for Windows 10 or later.

## macOS

Step-by-step installation guide for macOS 13+ (Apple Silicon).

## Linux

Install the official `.deb` or AppImage, or build from source.

## 

​

First Launch

The first time you open Comfy Desktop, a full-screen setup asks **How do you want to run Comfy?** and collects the choices it needs before anything is installed. The window stays in this setup until you finish it: if you close the app partway through, the same screen comes back on the next launch.

### 

​

Cloud or Local

![First-run setup asking Cloud or Local](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/first_run_cloud_local.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=5209bcecf72c91605d695662cef60a2d) Two cards cover the two ways to run ComfyUI:

  * **Cloud** runs ComfyUI on Comfy Cloud GPUs. Nothing is installed on your machine and there is nothing to download. The card carries a **TRY FREE** pill while free Cloud runs are available.
  * **Local** installs ComfyUI on this machine. You control the ComfyUI version, custom nodes, and startup arguments, and it runs offline.

If Comfy Desktop detects that this machine’s GPU is not powerful enough for most workflows, the Cloud card carries a **Recommended for your hardware** badge and neither card is preselected, so the choice is deliberate rather than a default. **Continue** stays disabled until a card is selected.

### 

​

Terms and data sharing

Three checkboxes sit below the cards:

  * **I agree to the EULA and Terms of Service** : required. The links open the EULA, the Terms of Service, and the Privacy Policy. **Continue** does not proceed until this box is ticked, every time the setup runs.
  * **Help improve Comfy by sharing anonymous usage data** : optional and ticked by default. Comfy Desktop sends anonymous usage data and never collects workflow contents, prompts, generated media, or personal information. You can change this later in [Desktop Settings](https://docs.comfy.org/installation/desktop/usage/settings).
  * **Opt in to beta features and help test what ships next** : optional and ticked by default, and available only while data sharing is on. Clearing data sharing also clears this box.



### 

​

Express Install

![First-run setup with Local selected](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/first_run_local_selected.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=4a81a4b22722b83833eb4b121643d968) When **Local** is selected, an **Express Install with recommended settings** checkbox appears. It is cleared by default, so the install wizard shows the ComfyUI version, install location, and startup options before anything is written to disk. Tick it to skip that step and install a Standalone instance with the recommended settings. Comfy Desktop then names the hardware it detected under the checkbox, so you can clear it if the detected GPU is not the one you want to use.

### 

​

Migrating an existing install

If Comfy Desktop finds a Legacy Desktop installation on the machine, a **Migrate existing instance** checkbox appears next to Express Install, ticked by default. Leave it ticked to bring your workflows, models, and settings over when you continue, see [Migrate from Legacy Desktop](https://docs.comfy.org/installation/desktop/usage/migrate) for what moves. Clear it to install a fresh instance instead. With both checkboxes cleared, Comfy Desktop asks once more before the install starts: select **Migrate** to bring the Legacy Desktop install over, or **Start Fresh** to install a clean instance and leave the existing projects in place.

### 

​

Chinese mirrors

When the app runs in Chinese, the setup adds one question after **Continue** : **Enable Chinese Mirrors?** Select **Enable Mirrors** to clone Git repositories from `gitcode.com` and fetch PyPI packages from Aliyun and Tencent mirrors instead of `github.com` and `pypi.org`, which is faster in mainland China. Select **Not now** to keep the defaults. Either answer is stored as the **Use Chinese Mirrors (Git & PyPI)** setting, so you can change it later.

### 

​

After setup

**Continue** saves your choices and shows a short **Preparing your install…** step.

  * **Cloud** : Comfy Desktop closes the setup and launches Comfy Cloud.
  * **Local** : the install wizard runs unless Express Install is on, the install shows its progress, and the finished instance appears on the dashboard.

If Comfy Desktop already has a standalone, tracked, or remote installation, it skips the Cloud or Local choice and takes you straight to the dashboard once the terms are accepted. Consenting is required every time the setup runs. The setup is a full-screen takeover: the title bar is locked while it is open, and once you leave the consent step the app menu (☰) is reduced to a single **Skip Onboarding** item, which closes the setup and drops you on the dashboard without installing anything.

## 

​

Usage Guide

Once installed, learn how to use Comfy Desktop:

## Comfy Desktop Usage Guide

Dashboard overview, instance management, settings, snapshots, and more.

## 

​

Migrate from Legacy Desktop

If you’re still using the older Legacy Desktop version (single-install desktop app), you can migrate your custom nodes, workflows, and models to the new Comfy Desktop. Your existing data is preserved — no manual migration needed.

## Migration Guide

Step-by-step guide to migrate from Legacy Desktop to Comfy Desktop.

## 

​

Open Source

Comfy Desktop source is on [GitHub](https://github.com/Comfy-Org/Comfy-Desktop). It is dual-licensed: AGPL-3.0-or-later, or a commercial license from Comfy Org.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/overview)

[System RequirementsPrevious](https://docs.comfy.org/installation/system_requirements)[Comfy Desktop for WindowsNext](https://docs.comfy.org/installation/desktop/windows)

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
