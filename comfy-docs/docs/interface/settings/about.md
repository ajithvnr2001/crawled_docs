---
url: https://docs.comfy.org/interface/settings/about/
title: ComfyUI About Page: Version Badges and System Info - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:02.467942+00:00
---

# ComfyUI About Page: Version Badges and System Info - ComfyUI

> Source: https://docs.comfy.org/interface/settings/about/

## On this page

  * Version Information Badges
  * Custom Node Badges
  * System Info
  * Extension Developer Guide



ComfyUI Settings

# ComfyUI About Page: Version Badges and System Info

Copy pageCopy page

Where to find version badges, custom node badges, and system information in ComfyUI, plus how extensions add their own About page badges.

Copy pageCopy page

The settings described on this page are located in the **ComfyUI in-app settings menu**. You can open it by navigating to **Settings** (gear icon) or using the `Ctrl + ,` keyboard shortcut, then select the corresponding category to view and configure these options.

The About page is an information display panel in the ComfyUI settings system, used to show application version information, related links, and system statistics. These settings can provide us with critical information when you submit feedback or report issues. ![about](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/settings-about.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=36423b9d7d78b257e2d34d37b91b8a22)

### 

​

Version Information Badges

The About page displays the following core version information:

  * **ComfyUI Version** : Shows the backend ComfyUI version number, linked to the official GitHub repository
  * **ComfyUI_frontend Version** : Shows the frontend interface version number, linked to the frontend GitHub repository
  * **Discord Community** : Provides a link to the ComfyOrg Discord server
  * **Official Website** : Links to the ComfyOrg official website



Since the version information here mainly corresponds to stable version information, if you are using the nightly version, the corresponding commit hash will not be displayed here. If you are using the nightly version, you can use the `git log` command in the corresponding ComfyUI main directory to view the corresponding commit hash and other information. Another common issue is that different dependency packages may fail and rollback during updates.

### 

​

Custom Node Badges

If custom nodes are installed, the About page will also display additional badge information provided by custom nodes. These badges are registered by each custom node through the `aboutPageBadges` property.

### 

​

System Info

The bottom of the page displays detailed system statistics, including:

  * Hardware configuration information
  * Software environment information
  * System performance data



## 

​

Extension Developer Guide

Extension developers can add custom badges to the About page by adding the `aboutPageBadges` property to their extension configuration:
    
    
    app.registerExtension({
      name: 'MyExtension',
      aboutPageBadges: [
        {
          label: 'My Extension v1.0.0',
          url: 'https://github.com/myuser/myextension',
          icon: 'pi pi-github'
        }
      ]
    })
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/settings/about.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/settings/about)

[Extension SettingsPrevious](https://docs.comfy.org/interface/settings/extension)[Account ManagementNext](https://docs.comfy.org/interface/user)

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
