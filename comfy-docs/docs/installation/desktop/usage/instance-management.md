---
url: https://docs.comfy.org/installation/desktop/usage/instance-management/
title: Instance Management - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:22.792793+00:00
---

# Instance Management - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/usage/instance-management/

## On this page

  * Instance Types
  * Creating a New Instance
  * Tracking an Existing Installation
    * Detecting Your Installation
    * Confirming the Detected Installation
    * Track vs Standalone
  * Launching, Stopping, and Restarting an Instance
    * Launching an Instance
    * Launching While Another Instance Is Running
    * Stopping an Instance
    * Restarting After a Crash
  * Uninstalling an Instance
  * Duplicating an Instance
  * Editing an Instance
  * Error State



Usage Guide

# Instance Management

Copy pageCopy page

Create, edit, rename, and delete ComfyUI instances in Comfy Desktop

Copy pageCopy page

Comfy Desktop lets you manage multiple ComfyUI instances from the Chooser view.

### 

​

Instance Types

Comfy Desktop supports four types of instances. Each type appears on its card and in the title bar; **Tracked** instances share the **Standalone** icon.

Type| Icon| Description  
---|---|---  
**Standalone**|  💻| A self-contained ComfyUI instance created by Comfy Desktop. Includes bundled Python, automatic updates, and full snapshot support. This is the default when you click **New Instance**.  
**Cloud**|  ☁️| A Comfy Cloud instance. Requires a Comfy Cloud account. Cloud instances run on Comfy’s servers and are billed separately.  
**Remote**|  🌐| Connects to a ComfyUI instance running on another machine on your network. Configure the remote host and port during setup.  
**Tracked**|  💻| Tracks an existing ComfyUI installation (Git clone or portable). Uses the same icon as **Standalone**. You manage updates manually. See Tracking an Existing Installation.  
  
The image below labels the key actions available for each instance card: ![Instance card ⋮ menu: Manage, Duplicate Instance, Show in Finder, Export Snapshot, Restore Snapshot, Uninstall](https://mintcdn.com/dripart/PBKxxhs8nJtECa3d/images/desktop/interface/interface_instance_menu.png?fit=max&auto=format&n=PBKxxhs8nJtECa3d&q=85&s=0b9bb65143494b31d90c57470cb4b584)

  1. **New Instance** : Create a brand new ComfyUI instance. See Creating a New Instance. You can also [create an instance from a snapshot file](https://docs.comfy.org/installation/desktop/usage/snapshots#create-an-instance-from-a-snapshot-file).
  2. **⋮ Menu** : Click the three-dot icon to open the action menu for an instance. Right-clicking the card opens the same menu.
  3. **Manage** : Open the Manage panel to configure the instance (path, launch args, model directories, environment variables). See the [Manage](https://docs.comfy.org/installation/desktop/usage/manage) page.
  4. **Duplicate Instance** : Copy a standalone installation, with its own Python environment and custom nodes. See Duplicating an Instance.
  5. **Show in Finder** , **Show in Explorer** , or **Show in Folder** : Open the installation folder in your file manager. The name follows your operating system.
  6. **Export Snapshot** : Export the instance’s newest snapshot to a file you can share. See [Share a Snapshot](https://docs.comfy.org/installation/desktop/usage/snapshots#share-a-snapshot).
  7. **Restore Snapshot** : Revert the instance to a previous snapshot. See the [Snapshots](https://docs.comfy.org/installation/desktop/usage/snapshots) page.
  8. **Uninstall** : Permanently delete the instance and all its files from disk. See Uninstalling an Instance.

The menu also lists actions that only appear in certain states: **Stop** while the instance is running, **Update** when a new ComfyUI version is available, **Migrate to Standalone** for an installation you can migrate, and **Create Build** for a local instance you can publish to a workspace. **Forget** is not part of this menu; it sits in the Manage panel, see Uninstalling an Instance.

## 

​

Creating a New Instance

Click the **+** card (top-left) in the Chooser view to add a new ComfyUI instance.

1

Create a New Instance

  * Windows

  * macOS

  * Linux




![The Create a New Instance wizard on Windows, annotating the name \(1\), build mode \(2\), release channel \(3\), hardware \(4\) and install location \(5\)](https://mintcdn.com/dripart/cAVuyhdaebQHS2CS/images/desktop/usage/new_install_01_settings_windows.png?fit=max&auto=format&n=cAVuyhdaebQHS2CS&q=85&s=f293743f357c88ea7639667b957053de)

![The Create a New Instance wizard on macOS, annotating the name \(1\), the install method \(2\), the release channel \(3\), the hardware \(4\) and the install location \(5\)](https://mintcdn.com/dripart/PBKxxhs8nJtECa3d/images/desktop/usage/new_install_01_settings_mac.png?fit=max&auto=format&n=PBKxxhs8nJtECa3d&q=85&s=3574ee56cd34b97aadfeb9a84df1aaf8)

![Create a New Instance wizard on Linux: name, Public Builds, release, hardware \(AMD/NVIDIA/Intel Arc\), and install location with free space](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/new_install_01_settings_linux.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=03b4201e96f77d5ecac7d8920268992e)

  1. **Name** : The name of your instance. The default is “ComfyUI”.
  2. **Public Builds** : The recommended option. A standard ComfyUI install built for your detected hardware. Select **Managed Builds** to install a Build from one of your workspaces instead (see [Workspaces and Builds](https://docs.comfy.org/installation/desktop/usage/workspaces-and-builds#installing-a-build)), or **Remote Connection** to connect to a ComfyUI instance running on another machine.
  3. **Release** : The release channel to install. **Stable (Recommended)** is preselected.
  4. **Hardware** : Comfy Desktop detects your GPU and preselects the matching build (NVIDIA, AMD, Intel Arc (XPU), or CPU). Each option shows the ComfyUI version, the Python version, and the download size.
  5. **Install Location** : Where ComfyUI is installed. On Windows, it’s strongly recommended to use an **SSD** and avoid the root of the C: drive. The field shows free space on the drive and an install size estimate when Comfy Desktop knows it.

If free space looks low, the wizard shows a **Low Disk Space** dialog. Choose **Continue Anyway** , or cancel and pick another path.![Low Disk Space dialog showing free space versus required install size, with Cancel and Continue Anyway](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/low_disk_space_dialog.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=7306da9f6d98179436d54fa23581eb62)

2

Installing

![Installing progress: Downloading ComfyUI with percent, throughput, and remaining steps](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/new_install_02_installing.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=56f28d2fc1eb721c2ef27d4229816095)Comfy Desktop will handle the rest: downloading Python, setting up the environment, and installing ComfyUI. The progress screen shows the current step.

3

Choose a Template

![Choose a starter workflow step with Video/Image/3D/Audio tabs before install finishes](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/new_install_03_interface_template.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=c02ae0bffd0167cecf0fea20418cba79)Once the installation is complete, Comfy Desktop opens the template library where you can pick a workflow template to get started.Templates that download models need enough free space for those files. If the drive cannot hold a template’s models, the wizard blocks that choice. Pick a lighter template or free space. On very small disks, the template step may be skipped entirely.

## 

​

Tracking an Existing Installation

If you already have a ComfyUI installation (either manually set up from the Git repository or downloaded as a portable version), you can add it to Comfy Desktop without creating a new one. Open the ☰ menu in the title bar and select **Add Existing Instance**. ![The ☰ menu open on the Dashboard, with Add Existing Instance marked \(2\)](https://mintcdn.com/dripart/PBKxxhs8nJtECa3d/images/desktop/usage/track_instance_01.png?fit=max&auto=format&n=PBKxxhs8nJtECa3d&q=85&s=843fefad1f2629325238092d45240b4e)

  1. The **☰** menu button in the top-left corner of the title bar.
  2. **Add Existing Instance** : Opens the dialog that tracks an existing ComfyUI installation.



### 

​

Detecting Your Installation

In the dialog, click **Browse…** and select the installation folder. Comfy Desktop probes the folder and fills in the rest of the dialog. The **Detected type** dropdown lists what it found:

  * **Standalone** : A Comfy Desktop installation. The probe looks for a `standalone-env` directory and `ComfyUI/main.py`.
  * **Portable** : A Windows portable build. The probe looks for `python_embeded`, either in the folder you selected or in a folder directly inside it.
  * **Git Clone** : A clone of the ComfyUI repository. The probe looks for a `.git` directory.
  * **Legacy Desktop** : An installation of the older ComfyUI Desktop app, recognized by its `models/`, `user/`, and `.venv` directories. See [Migrate from Legacy Desktop](https://docs.comfy.org/installation/desktop/usage/migrate).

If the probe finds nothing, the dropdown reads **No known install detected**. Select the folder that holds the installation itself, not a parent or unrelated folder.

### 

​

Confirming the Detected Installation

After the probe finishes, the dialog shows what it found. Check the paths before you track the installation. ![The Add Existing Instance dialog with a Git clone detected: install location, version, repository, branch, and virtual environment](https://mintcdn.com/dripart/PBKxxhs8nJtECa3d/images/desktop/usage/track_instance_02.png?fit=max&auto=format&n=PBKxxhs8nJtECa3d&q=85&s=49d1202e57fd41b6f4ca412b990c77cf)

  * **Install location** : The folder you selected. Click the path to open it, or **Browse…** to pick another one. For a portable build, point at the folder that contains `python_embeded`.
  * **Name** : How the instance is listed in the Chooser. The dialog suggests a name.
  * **Detected type** : Which kind of installation the folder holds.
  * **Version** , **Repository** , and **Branch** : Shown for a Git clone.
  * **Virtual Environment** : Shown for a Git clone when Comfy Desktop finds one, in `.venv`, `venv`, `.env`, or `env` with a `pyvenv.cfg` file inside. **Browse…** points the instance at a different environment.

Click **Track Install** to add the instance. No files are moved or copied.

### 

​

Track vs Standalone

The key difference between a **Tracked** (Add Existing Instance) installation and a **Standalone** installation is how updates are managed:

Aspect| Tracked (Existing)| Standalone  
---|---|---  
**Updates**|  No automatic updates: in a Git clone you pull and reinstall yourself, and a portable build is replaced by a newer one| Built-in automatic updates  
**Python**|  Uses an existing Python environment (`.venv`, `python_embeded`, etc.)| Bundled Python, automatic dependency management  
**Isolation**|  Shares the existing path and environment| Fully self-contained, isolated installation  
**Snapshots**|  Not supported| Snapshot support available  
**Use case**|  Already have ComfyUI set up and customized| Fresh install from scratch  
  
> **Note:** Comfy Desktop runs a tracked installation with its existing Python environment and does not reinstall ComfyUI or manage its packages. Snapshot capture runs only for Standalone instances.

## 

​

Launching, Stopping, and Restarting an Instance

↩ Back to overview

### 

​

Launching an Instance

Click an instance card in the Chooser to launch it. While ComfyUI starts, the window shows the startup progress, then the ComfyUI interface once the server is ready.

### 

​

Launching While Another Instance Is Running

When you launch a local instance while another local instance is running or starting, Comfy Desktop shows an **An instance is already running** dialog that lists the instances it would stop:

  * **Close & Launch**: stops the listed instances, then launches the one you picked.
  * **Run All** : launches the new instance alongside the running ones.

Dismiss the dialog to cancel the launch. Restarting an instance never shows this dialog. To stop seeing it, turn off **Warn before running multiple instances** in [Desktop Settings → Preferences](https://docs.comfy.org/installation/desktop/usage/settings#preferences).

### 

​

Stopping an Instance

Select **Stop** from the instance card’s ⋮ menu. The ComfyUI server stops and the window stays open with a **ComfyUI is stopped** card. Select **Relaunch ComfyUI** to start the server again, or **Return to Dashboard** to go back to the Chooser.

### 

​

Restarting After a Crash

If ComfyUI fails to start or exits unexpectedly, the window stays open with a card describing what happened:

  * **ComfyUI could not start** : the instance did not start.
  * **ComfyUI exited unexpectedly** : the process stopped. When Comfy Desktop can read it, the card also shows the exit code, or the signal that ended the process.

On Windows, a crash can report a memory access violation and note that some Microsoft Visual C++ Redistributable files appear to be missing. Expand the card’s logs for details, then select **Restart ComfyUI** to launch again, or **Back** to return to the dashboard. If ComfyUI stops because it cannot open the asset database it keeps inside the installation, the error it stops with explains the reason instead of only reporting an exit code:

  * **Another ComfyUI is using this installation’s database** : close that ComfyUI (or the app that started it), or give one of them its own database location with the `--database-url` startup argument.
  * **Any other database failure** , from one locked by another program to one written by a newer version of ComfyUI or impossible to create in that folder: the message names the file and the fix, and ends with the option to start the instance without the asset system, by adding `--disable-assets` to its startup arguments.



## 

​

Uninstalling an Instance

↩ Back to overview When you want to remove an instance, two actions decide whether its files stay on disk. ![Forget and Uninstall in the Manage panel's More menu](https://mintcdn.com/dripart/PBKxxhs8nJtECa3d/images/desktop/usage/instance_uninstall.png?fit=max&auto=format&n=PBKxxhs8nJtECa3d&q=85&s=620dca5ad4180a25c2deb1d8165ff3fb)

  1. **Forget** : Removes the instance from the app without deleting anything. The installation folder and all its data stay on disk. Use this when you only want to clean up the list but might need the instance again later.
  2. **Uninstall** : Permanently removes the installation and all its files from disk. Model files in shared directories are not affected.

**Uninstall** is also on the instance card’s ⋮ menu. **Forget** is not part of that menu; you find it in the Manage panel, in the **More** menu at the bottom of the panel. An installation Comfy Desktop adopted, such as one migrated from Legacy Desktop, has no **Forget** action.

## 

​

Duplicating an Instance

↩ Back to overview You can duplicate an existing standalone installation. Open the card’s ⋮ menu and select **Duplicate Instance** , or use **Duplicate Instance** in the Manage panel’s **More** menu. The copy gets:

  * A new Python environment
  * The same ComfyUI version
  * Its own custom node setup

Enter a name for the duplicate when prompted. The copy is created next to the original. Cloud, remote, and tracked installations cannot be duplicated.

## 

​

Editing an Instance

↩ Back to overview In the **Manage** panel for an instance, you can:

  * Change the installation path
  * Adjust launch arguments
  * Modify model directories
  * Update environment variables
  * Rename the instance, from the name at the top of the **About** tab or from **Rename** in the **More** menu
  * Change the connection address of a Remote Connection, in the **About** tab

Open the **Manage** panel by right-clicking the instance card (or selecting **Manage** in its ⋮ menu).

## 

​

Error State

If an installation encounters a problem, an **Error** badge appears on its card. Select the badge to read the details: the message, the exit code or signal when Comfy Desktop has one, and the last lines of error output. Launching or restarting the instance clears the badge. If the problem comes back, check the logs at the [Data Locations](https://docs.comfy.org/installation/desktop/usage/settings#data-locations).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/usage/instance-management.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/usage/instance-management)

[Using Comfy DesktopPrevious](https://docs.comfy.org/installation/desktop/usage/overview)[Workspaces and ComfyUI Builds in Comfy DesktopNext](https://docs.comfy.org/installation/desktop/usage/workspaces-and-builds)

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
