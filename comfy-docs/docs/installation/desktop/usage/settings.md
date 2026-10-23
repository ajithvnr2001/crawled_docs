---
url: https://docs.comfy.org/installation/desktop/usage/settings/
title: Comfy Desktop Settings - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:58.714770+00:00
---

# Comfy Desktop Settings - ComfyUI

> Source: https://docs.comfy.org/installation/desktop/usage/settings/

## On this page

  * Preferences
    * App Behavior
    * Privacy
    * Community
  * Updates
  * Storage
  * Advanced
  * Logs
  * Data Locations
  * Keyboard Shortcuts
  * Feedback and Issues



Usage Guide

# Comfy Desktop Settings

Copy pageCopy page

Global settings, proxy/mirror configuration, and data locations

Copy pageCopy page

Click the ☰ menu (1) in the top-left corner and select **Desktop Settings** (2) to open the global settings panel. ![Desktop Settings panel open on Preferences, including Opt-in to beta features](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/comfy_desktop_settings_00_menu.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=ce79710629308873469d181d40e95e94) The settings panel is organized into five tabs. Click a tab in the sidebar to switch views.

## 

​

Preferences

![Preferences: language, app behavior, telemetry, and Opt-in to beta features](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/comfy_desktop_settings_01_preferences.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=d26ec3f3f24b60f8269004090d402716) The Preferences tab opens with a **Language** picker, then groups the rest of its controls into three sections.

  * **Language** : Choose the display language. **English** and **中文** are available.



### 

​

App Behavior

  * **Auto-launch on startup** : Pick which instance to start when Comfy Desktop opens. **None (show dashboard)** is the default. You can also choose **Last used instance** , or a specific install.
  * **Confirm before closing a window** : Ask for confirmation before closing a window that is running a local install.
  * **Warn before running multiple instances** : Show a warning before launching another local ComfyUI instance while one is already running or starting.
  * **Hide Cloud from the Instance Picker** : Hide the Cloud row from the Dashboard. Cloud still works if you re-enable this later.



### 

​

Privacy

  * **Share anonymous usage telemetry** : Send anonymous usage data to help improve Comfy Desktop.
  * **Opt-in to beta features** : Let Comfy Desktop turn on early Core features for your instances. The switch stays disabled until you confirm data sharing with **Share anonymous usage telemetry** , even when telemetry is already on.

Beta features arrive as extra startup arguments, added on top of the ones you set yourself: Comfy Desktop never removes or replaces your own arguments. When a beta feature turns on for an instance, a card headed **A beta feature is on** appears in the title bar. **Got it** dismisses it, and **Settings** opens this panel on the opt-in switch. You can see which arguments a beta feature added in the instance’s Startup Args tab, behind the **+N beta** pill next to **Startup Arguments**.

### 

​

Community

  * **Comfy Desktop** : A card linking to the [Comfy Desktop GitHub repository](https://github.com/Comfy-Org/Comfy-Desktop), with a star count.



## 

​

Updates

![Updates tab: installed version, Check for updates, Automatically install Desktop updates](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/comfy_desktop_settings_02_updates.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=d7b780adfd08e8275b3a9f56e487869c)

  * **Status** : Shows whether Comfy Desktop is up to date, the installed version, and the last check time.
  * **Check for updates** : Manually check for a new version. Button changes to **Download** then **Install** when an update is available.
  * **Automatically install Desktop updates** : Auto-download and install updates in the background.



## 

​

Storage

The Storage tab is where you configure where Comfy Desktop finds and stores files. The key concept is **sharing** : instead of each instance having its own isolated models, inputs, and outputs, you set up shared directories accessible to all instances. ![Storage tab: Shared Models, Shared Input, and Shared Output paths](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/comfy_desktop_settings_03_storage.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=63ea57dc4995d29907eca09be715703d)

  * **Shared Models** : Each directory listed here is scanned for models by every instance. New models download to the directory marked with the **DOWNLOADS** badge. ![Directory ⋯ menu with Use for Model Downloads](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/comfy_desktop_settings_03-2_storage.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=7e1e33f18b3b1f50142486e71e0680b7)
    * Click the folder icon to open a directory in your file manager.
    * Click the **…** menu (1) on a directory, then select **Use for Model Downloads** (2) to make that directory the download target.
    * Click **\+ Add Shared Directory** to add more model directories.
  * **Shared Input** : A shared path where all instances look for input files (images, videos, etc.).
  * **Shared Output** : A shared path where all instances save generated outputs. Customizing this lets you keep all results in one place.
  * Click the folder icon to browse and select a new path. **?** tooltips provide additional details.

Per-instance overrides (include shared dirs, split input/output, extra model folders) live in the instance [Manage](https://docs.comfy.org/installation/desktop/usage/manage#storage-tab) Storage tab.

## 

​

Advanced

![Advanced tab: default install location, mirrors, and hardware acceleration](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/comfy_desktop_settings_04_advanced.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=4fe36d942b9521b109f99449dd326886)

  * **Default Install Location** : Where new standalone instances are created. Click the folder icon to change it.
  * **Use hardware acceleration** : Use the GPU to render Comfy Desktop. Restart Comfy Desktop for changes to take effect.
  * **PyPI Mirror URL** : Custom pip mirror (e.g. `https://mirrors.aliyun.com/pypi/simple/`).
  * **Use Chinese Mirrors (Git & PyPI)**: Use Chinese mirror servers for Git and PyPI. Helpful in mainland China.
  * **Cache Directory** : Where Comfy Desktop stores temporary and cached data. Click the folder icon to change it.



## 

​

Logs

  * **Diagnostics** : **Open logs folder** reveals the Desktop app log directory (`app.log`). See [How do I check Comfy Desktop startup logs?](https://docs.comfy.org/installation/desktop/faq#how-do-i-check-comfy-desktop-startup-logs).



## 

​

Data Locations

Comfy Desktop stores data in platform-specific directories.

  * Windows

  * macOS

  * Linux



    
    
    App data:     %APPDATA%\Comfy Desktop
    Logs:         %APPDATA%\Comfy Desktop\logs
    Installs:     %LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs
    Shared data:  %LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared
    

New installs put large data (installs, shared models, cache) under `%LOCALAPPDATA%\Comfy-Desktop`. If you already had `ComfyUI-Installs` or `ComfyUI-Shared` in your user profile before upgrading, those home-root folders are kept. If you installed the app to another drive, large data lives in `<drive>\Comfy-Desktop\` instead.
    
    
    App data:     ~/Library/Application Support/Comfy Desktop
    Logs:         ~/Library/Logs/Comfy Desktop
    Installs:     ~/ComfyUI-Installs
    Shared data:  ~/ComfyUI-Shared
    
    
    
    Config:       ~/.config/comfyui-desktop-2
    Data:         ~/.local/share/comfyui-desktop-2
    Cache:        ~/.cache/comfyui-desktop-2
    State:        ~/.local/state/comfyui-desktop-2
    Logs:         ~/.config/comfyui-desktop-2/logs
    Installs:     ~/ComfyUI-Installs
    Shared data:  ~/ComfyUI-Shared
    

On Linux, Electron stores user data under the package name `comfyui-desktop-2`, not the display name Comfy Desktop.

## 

​

Keyboard Shortcuts

Shortcut| Action  
---|---  
`Ctrl+R` / `Cmd+R`| Reload the current ComfyUI instance  
`Ctrl+W` / `Cmd+W`| Close the current window  
`Escape`| Close a dialog or popup  
`Ctrl+,` / `Cmd+,`| Open Comfy Desktop Settings  
  
## 

​

Feedback and Issues

Found a bug or have a suggestion? Comfy Desktop is open source. You can report issues and check planned features here:

  * **Comfy Desktop issues** : [github.com/Comfy-Org/Comfy-Desktop/issues](https://github.com/Comfy-Org/Comfy-Desktop/issues)
  * **Documentation issues** : [github.com/Comfy-Org/docs/issues](https://github.com/Comfy-Org/docs/issues)

For general questions about ComfyUI, visit the [ComfyUI GitHub Discussions](https://github.com/Comfy-Org/ComfyUI/discussions) or join the [ComfyUI Discord](https://www.comfy.org/discord).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/desktop/usage/settings.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/desktop/usage/settings)

[Managing InstallationsPrevious](https://docs.comfy.org/installation/desktop/usage/manage)[Performance Tests and BenchmarksNext](https://docs.comfy.org/installation/desktop/usage/performance-tests)

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
