---
url: https://docs.comfy.org/custom-nodes/js/javascript_about_panel_badges/
title: About Panel Badges - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:37.649769+00:00
---

# About Panel Badges - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_about_panel_badges/

## On this page

  * Basic Usage
  * Badge Configuration
  * Icon Options
  * Example



JavaScript (UI)

# About Panel Badges

Copy pageCopy page

Add custom badges with labels, URLs, and icons to the ComfyUI About Panel using the About Panel Badges API, linking to docs, GitHub, or extension resources.

Copy pageCopy page

The About Panel Badges API allows extensions to add custom badges to the ComfyUI about page. These badges can display information about your extension and contain links to documentation, source code, or other resources.

## 

​

Basic Usage
    
    
    app.registerExtension({
      name: "MyExtension",
      aboutPageBadges: [
        {
          label: "Documentation",
          url: "https://example.com/docs",
          icon: "pi pi-file"
        },
        {
          label: "GitHub",
          url: "https://github.com/username/repo",
          icon: "pi pi-github"
        }
      ]
    });
    

## 

​

Badge Configuration

Each badge requires all of these properties:
    
    
    {
      label: string,           // Text to display on the badge
      url: string,             // URL to open when badge is clicked
      icon: string             // Icon class (e.g., PrimeVue icon)
    }
    

## 

​

Icon Options

Badge icons use PrimeVue’s icon set. Here are some commonly used icons:

  * Documentation: `pi pi-file` or `pi pi-book`
  * GitHub: `pi pi-github`
  * External link: `pi pi-external-link`
  * Information: `pi pi-info-circle`
  * Download: `pi pi-download`
  * Website: `pi pi-globe`
  * Discord: `pi pi-discord`

For a complete list of available icons, refer to the [PrimeVue Icons documentation](https://primevue.org/icons/).

## 

​

Example
    
    
    app.registerExtension({
      name: "BadgeExample",
      aboutPageBadges: [
        {
          label: "Website",
          url: "https://example.com",
          icon: "pi pi-home"
        },
        {
          label: "Donate",
          url: "https://example.com/donate",
          icon: "pi pi-heart"
        },
        {
          label: "Documentation",
          url: "https://example.com/docs",
          icon: "pi pi-book"
        }
      ]
    });
    

Badges appear in the About panel of the Settings dialog, which can be accessed via the gear icon in the top-right corner of the ComfyUI interface.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_about_panel_badges.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_about_panel_badges)

[ComfyUI Toast APIPrevious](https://docs.comfy.org/custom-nodes/js/javascript_toast)[Bottom Panel TabsNext](https://docs.comfy.org/custom-nodes/js/javascript_bottom_panel_tabs)

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
