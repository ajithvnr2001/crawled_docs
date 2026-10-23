---
url: https://docs.comfy.org/installation/desktop/usage/downloads/
title: Model Downloads in Comfy Desktop - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:57.800746+00:00
---

# Model Downloads in Comfy Desktop - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/usage/downloads/

## On this page

  * What appears in the downloads list
  * The Downloads tray
  * The full downloads view
  * Quitting with downloads in progress
  * Where downloads are saved



Usage Guide

# Model Downloads in Comfy Desktop

Copy pageCopy page

Track active and recent model and output downloads, retry or pause them, and see where Comfy Desktop saves each file.

Copy pageCopy page

Comfy Desktop downloads models for your instances and tracks every transfer in one place. When a ComfyUI instance asks for a model that is not on disk yet, Comfy Desktop handles the download and saves the file in the instance’s model directory, so you do not have to place it by hand. Open the **Downloads** tray from the title bar to follow active downloads, retry a failed one, or jump to the folder where a finished file landed.

## 

​

What appears in the downloads list

  * **Missing models** : when ComfyUI reports missing models in the missing-models dialog or the right side panel **Errors** tab, the download action is routed through Comfy Desktop. Each file is saved into the matching model folder, such as `checkpoints`, `diffusion_models`, `text_encoders`, `loras`, or `vae`. Supported model file types are `.safetensors`, `.sft`, `.ckpt`, `.pth`, and `.pt`.
  * **Template models** : when you set up an instance from a starter template, the models that template needs download in the background, and they appear in the tray like any other download. The progress screen keeps the model download step visible until they finish. If you would rather get started, **Skip & open ComfyUI** on that screen opens ComfyUI right away and the downloads keep running in the tray.
  * **Outputs from remote instances** : when you run a workflow on a remote or Cloud instance, finished outputs download to your local output directory automatically.



## 

​

The Downloads tray

Click the **Downloads** button in the title bar’s trailing controls to open the tray. Downloads are listed newest first, labeled with their model folder and filename, and active rows show transferred size, percentage, speed, and estimated time remaining. ![Downloads tray opened from the Comfy Desktop title bar, listing model downloads with their folder and progress](https://mintcdn.com/dripart/u_e-u6-s3jR2i6kZ/images/desktop/usage/downloads_01_tray.png?fit=max&auto=format&n=u_e-u6-s3jR2i6kZ&q=85&s=477a8b952fbbebe27cb71398d6945886) The button shows a badge with the number of active downloads. When nothing is downloading, it instead flags downloads that failed and you have not reviewed, or that finished and you have not opened yet. Each row has these actions:

  * **Click a finished row** to open the folder that holds the file (Show in Finder, Show in Explorer, or Show in Folder, depending on your system).
  * **Retry** a failed or cancelled download.
  * **✕** to cancel an active download, or remove a finished one from the list.

**View All Downloads** at the bottom of the tray opens the full downloads view.

## 

​

The full downloads view

The full view keeps the download history for the app and adds the controls that do not fit in the tray:

  * Filter the list by **All** , **Active** , **Completed** , or **Failed**.
  * **Pause** an active download, and **Resume** a paused one.
  * **Retry** a failed or cancelled download.
  * Open the file’s folder, or remove a single row.
  * **Clear finished** to remove every finished row at once.

The footer counts the active and completed downloads currently listed. ![Full Downloads view listing paused downloads, each with a Resume action, and the active count in the footer](https://mintcdn.com/dripart/u_e-u6-s3jR2i6kZ/images/desktop/usage/downloads_02_full_view.png?fit=max&auto=format&n=u_e-u6-s3jR2i6kZ&q=85&s=25934a96dcf459b2f3cc53688b668e8f)

## 

​

Quitting with downloads in progress

Model downloads are resumable. If you quit Comfy Desktop while a model transfer is running, the bytes already received are kept, and on the next launch the transfer returns as a paused row in the Downloads tray. Open **View All Downloads** to **Resume** it from where it stopped, or cancel it to drop the partial file. Output downloads from remote instances transfer on a separate path and do not resume after you quit. When a template’s models are still downloading, Comfy Desktop asks you to confirm the quit, because the template setup waits on those files:

  * **Quit Anyway** : pauses the downloads and quits. The rows are still there on the next launch.
  * **Keep Downloading** : cancels the quit and leaves Comfy Desktop running. This is the default.

Quits that Comfy Desktop starts itself, such as installing an update or restarting, skip this prompt. So does **Quit Desktop** in the title bar menu, which shows its own confirmation that lists the active downloads. The transfers are paused either way and come back on the next launch.

## 

​

Where downloads are saved

Model files are written to the instance’s model download directory: the shared model directory marked **DOWNLOADS** (set with **Use for Model Downloads**) when the instance includes shared model directories, otherwise the instance’s own `models` folder. Shared directories are configured in [Desktop Settings](https://docs.comfy.org/installation/desktop/usage/settings#storage), and each instance can opt out of them in its **Manage** panel [Storage tab](https://docs.comfy.org/installation/desktop/usage/manage#storage-tab). Outputs downloaded from a remote instance go to the shared output folder when the instance uses it, otherwise to the instance’s own output folder. A remote instance can turn automatic output downloads off with **Auto-Download Outputs** in its storage settings.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/usage/downloads.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/usage/downloads)

[Comfy Desktop SnapshotsPrevious](https://docs.comfy.org/installation/desktop/usage/snapshots)[Managing InstallationsNext](https://docs.comfy.org/installation/desktop/usage/manage)

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
