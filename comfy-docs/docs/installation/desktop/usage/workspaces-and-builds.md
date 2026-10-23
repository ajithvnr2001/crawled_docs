---
url: https://docs.comfy.org/installation/desktop/usage/workspaces-and-builds/
title: Workspaces and ComfyUI Builds in Comfy Desktop - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:58.799610+00:00
---

# Workspaces and ComfyUI Builds in Comfy Desktop - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/usage/workspaces-and-builds/

## On this page

  * Signing in
  * Switching workspaces
  * Installing a Build
  * Creating a Build from an instance



Usage Guide

# Workspaces and ComfyUI Builds in Comfy Desktop

Copy pageCopy page

Sign in to Comfy Desktop to switch workspaces, install ComfyUI Builds from your workspace, and create a Build from a local instance.

Copy pageCopy page

Comfy Desktop can connect to your Comfy account. Signing in adds workspace features to the Chooser: switch between your Personal workspace and any team workspace you belong to, see the instances that belong to the selected workspace, and install ComfyUI Builds published to it. You can also turn a local instance into a Build that other members of the workspace can install. Signing in is optional. Local instances, snapshots, and settings work without an account.

## 

​

Signing in

The account chip sits at the top right of the Chooser.

  * **Signed out** : the chip shows a **Log in** button. Click it to open the browser sign-in flow, then return to the app.
  * **Signed in** : the chip shows your avatar and email. Click it to open a menu with **Sign out**.

Signing out ends the session only. Your instances stay in place. If an installation is in progress, Comfy Desktop warns you that signing out cancels it before it continues.

## 

​

Switching workspaces

A workspace bar sits above the instance grid:

  * **Workspace switcher** : your **Personal** space and every team workspace you belong to. Click it to switch.
  * **Refresh workspaces** : appears once you are signed in. It reloads the workspace list and the Builds catalog for the selected workspace.
  * **INSTANCES** : the number of instances that belong to the selected workspace.

The selected workspace scopes the Chooser. The grid shows only the instances that belong to it, and the New Instance flow offers that workspace’s Builds. Comfy Desktop remembers the workspace you selected and restores it the next time you open the app.

## 

​

Installing a Build

A Build is a packaged ComfyUI environment published to a workspace. The New Instance wizard shows the Build’s release version, creator, hardware target, and an estimate of the disk space it needs. Installing a Build gives you that exact environment as a local instance, instead of a plain ComfyUI install.

  1. Click the **+** card in the Chooser to open the New Instance wizard.
  2. In the method row, select **Managed Builds**. If you are not signed in yet, Comfy Desktop asks you to sign in first.
  3. Under **Release** , pick the Build to install. Only Builds that are ready to install and compatible with your machine are listed. Use **View builds online** to open the Builds page in your browser, or the refresh button to reload the list.
  4. Under **Hardware** , pick the release target for your machine, for example Windows with NVIDIA (CUDA 12.8). The recommended target for your hardware is preselected.
  5. Continue through the wizard to install the instance.

When you are signed in, the wizard opens on **Managed Builds** and falls back to **Public Builds** when the selected workspace has no compatible Build. **Public Builds** is the standard ComfyUI install for your detected hardware.

## 

​

Creating a Build from an instance

You can publish a local instance as a Build so that other members of its workspace can install it.

  1. Sign in to your Comfy account.
  2. In the Chooser, open the instance’s **⋮ menu** and select **Create Build**.
  3. Comfy Desktop creates a draft Build from that instance in Comfy Developer Platform. The draft belongs to the workspace the instance belongs to.

**Create Build** is offered for local instances that are installed and have an installation path on disk. It is not offered for Cloud or remote instances. The Build starts as a draft, so you can review its contents before releasing it. For the full Build workflow, including how to create a Build from a Desktop snapshot or a workflow JSON file, see [Other Ways to Create a Comfy API Build](https://docs.comfy.org/development/serverless/build-sources).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/usage/workspaces-and-builds.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/usage/workspaces-and-builds)

[Instance ManagementPrevious](https://docs.comfy.org/installation/desktop/usage/instance-management)[Comfy Desktop SnapshotsNext](https://docs.comfy.org/installation/desktop/usage/snapshots)

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
