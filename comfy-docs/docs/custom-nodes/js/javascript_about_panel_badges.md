---
url: https://docs.comfy.org/custom-nodes/js/javascript_about_panel_badges/
title: About Panel Badges - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:51.440130+00:00
---

# About Panel Badges - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_about_panel_badges/

## On this page

Back to top

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
          icon: "icon-[lucide--file]"
        },
        {
          label: "GitHub",
          url: "https://github.com/username/repo",
          icon: "icon-[lucide--github]"
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
      icon: string             // Icon class (e.g., "icon-[lucide--github]")
    }
    

## 

​

Icon Options

Badge icons use [Lucide](https://lucide.dev/icons/) icon classes in the form `icon-[lucide--<icon-name>]`. Here are some commonly used icons:

  * Documentation: `icon-[lucide--file]` or `icon-[lucide--book-open]`
  * GitHub: `icon-[lucide--github]`
  * External link: `icon-[lucide--external-link]`
  * Information: `icon-[lucide--info]`
  * Download: `icon-[lucide--download]`
  * Website: `icon-[lucide--globe]`

The frontend generates these classes when it is built, so only the Lucide icons that the frontend itself uses are available. If an icon does not render, pick another icon, or define your own icon class in a stylesheet that your extension loads. PrimeIcons classes such as `pi pi-file` still render for now, but they are being phased out. Don’t use them in new code. See [PrimeVue removal migration](https://docs.comfy.org/custom-nodes/js/primevue-removal-migration).

## 

​

Example
    
    
    app.registerExtension({
      name: "BadgeExample",
      aboutPageBadges: [
        {
          label: "Website",
          url: "https://example.com",
          icon: "icon-[lucide--globe]"
        },
        {
          label: "Donate",
          url: "https://example.com/donate",
          icon: "icon-[lucide--heart]"
        },
        {
          label: "Documentation",
          url: "https://example.com/docs",
          icon: "icon-[lucide--book-open]"
        }
      ]
    });
    

Badges appear in the About panel of the Settings dialog, which can be accessed via the gear icon in the top-right corner of the ComfyUI interface.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_about_panel_badges.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_about_panel_badges)

[Toast API](https://docs.comfy.org/custom-nodes/js/javascript_toast)[Bottom Panel Tabs](https://docs.comfy.org/custom-nodes/js/javascript_bottom_panel_tabs)
