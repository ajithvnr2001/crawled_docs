---
url: https://docs.comfy.org/interface/appearance/
title: Customizing ComfyUI Appearance - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:59.971624+00:00
---

# Customizing ComfyUI Appearance - ComfyUI

> Source: https://docs.comfy.org/interface/appearance/

## On this page

  * Color Palette System
    * How to Customize Color Themes
  * Canvas
    * Background Image
  * General
    * Tab Bar Layout
    * Disable animations
  * Node
    * Node Opacity
  * Node Widget
    * Textarea Widget Font Size
  * Sidebar
    * Unified Sidebar Width
    * Sidebar Size
    * Sidebar Location
    * Sidebar Style
  * Tree Explorer
    * Tree Explorer Item Padding
  * Advanced Customization with user.css
    * Requirements
    * Setting Up user.css
    * User Directory Location
    * user.css Examples and Related Instructions



ComfyUI Settings

# Customizing ComfyUI Appearance

Copy pageCopy page

Learn how to customize the appearance of ComfyUI using color palettes and advanced CSS options

Copy pageCopy page

The settings described on this page are located in the **ComfyUI in-app settings menu**. You can open it by navigating to **Settings** (gear icon) or using the `Ctrl + ,` keyboard shortcut, then select the corresponding category to view and configure these options.

ComfyUI offers flexible appearance customization options that allow you to personalize the interface to your preferences.

## 

​

Color Palette System

The primary way to customize ComfyUI’s appearance is through the built-in color palette system. ![Color Palette](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=206dbb5bcf19ba1923bd722e20ba868e) This allows you to:

  1. Switch ComfyUI themes
  2. Export the currently selected theme as JSON format
  3. Load custom theme configuration from JSON file
  4. Delete custom theme configuration



For appearance needs that cannot be satisfied by the color palette, you can perform advanced appearance customization through the user.css file

### 

​

How to Customize Color Themes

The color palette allows you to modify many specific properties. Here are some of the most commonly customized elements, with colors represented in hexadecimal format:

  1. The JSON comments below are for illustration only. Do not copy the content below for modification as it will cause the theme to malfunction.
  2. Since we are still iterating frequently, the content below may change with ComfyUI frontend updates. If you need to modify, please export the theme configuration from settings and then modify it.


    
    
    {
      "id": "dark",                     // Must be unique, cannot be the same as other theme IDs
      "name": "Dark (Default)",         // Theme name, displayed in theme selector
      "colors": {
        "node_slot": {                  // Node connection slot color configuration
          "CLIP": "#FFD500",            // CLIP model connection slot color
          "CLIP_VISION": "#A8DADC",     // CLIP Vision model connection slot color
          "CLIP_VISION_OUTPUT": "#ad7452", // CLIP Vision output connection slot color
          "CONDITIONING": "#FFA931",     // Conditioning control connection slot color
          "CONTROL_NET": "#6EE7B7",     // ControlNet model connection slot color
          "IMAGE": "#64B5F6",           // Image data connection slot color
          "LATENT": "#FF9CF9",          // Latent space connection slot color
          "MASK": "#81C784",            // Mask data connection slot color
          "MODEL": "#B39DDB",           // Model connection slot color
          "STYLE_MODEL": "#C2FFAE",     // Style model connection slot color
          "VAE": "#FF6E6E",             // VAE model connection slot color
          "NOISE": "#B0B0B0",           // Noise data connection slot color
          "GUIDER": "#66FFFF",          // Guider connection slot color
          "SAMPLER": "#ECB4B4",         // Sampler connection slot color
          "SIGMAS": "#CDFFCD",          // Sigmas data connection slot color
          "TAESD": "#DCC274"            // TAESD model connection slot color
        },
        "litegraph_base": {             // LiteGraph base interface configuration
          "BACKGROUND_IMAGE": "",        // Background image, default is empty
          "CLEAR_BACKGROUND_COLOR": "#222", // Main canvas background color
          "NODE_TITLE_COLOR": "#999",    // Node title text color
          "NODE_SELECTED_TITLE_COLOR": "#FFF", // Selected node title color
          "NODE_TEXT_SIZE": 14,          // Node text size
          "NODE_TEXT_COLOR": "#AAA",     // Node text color
          "NODE_TEXT_HIGHLIGHT_COLOR": "#FFF", // Node text highlight color
          "NODE_SUBTEXT_SIZE": 12,       // Node subtext size
          "NODE_DEFAULT_COLOR": "#333",   // Node default color
          "NODE_DEFAULT_BGCOLOR": "#353535", // Node default background color
          "NODE_DEFAULT_BOXCOLOR": "#666", // Node default border color
          "NODE_DEFAULT_SHAPE": 2,        // Node default shape
          "NODE_BOX_OUTLINE_COLOR": "#FFF", // Node border outline color
          "NODE_BYPASS_BGCOLOR": "#FF00FF", // Node bypass background color
          "NODE_ERROR_COLOUR": "#E00",    // Node error state color
          "DEFAULT_SHADOW_COLOR": "rgba(0,0,0,0.5)", // Default shadow color
          "DEFAULT_GROUP_FONT": 24,       // Group default font size
          "WIDGET_BGCOLOR": "#222",       // Widget background color
          "WIDGET_OUTLINE_COLOR": "#666", // Widget outline color
          "WIDGET_TEXT_COLOR": "#DDD",    // Widget text color
          "WIDGET_SECONDARY_TEXT_COLOR": "#999", // Widget secondary text color
          "WIDGET_DISABLED_TEXT_COLOR": "#666", // Widget disabled state text color
          "LINK_COLOR": "#9A9",          // Connection line color
          "EVENT_LINK_COLOR": "#A86",    // Event connection line color
          "CONNECTING_LINK_COLOR": "#AFA", // Connecting line color
          "BADGE_FG_COLOR": "#FFF",      // Badge foreground color
          "BADGE_BG_COLOR": "#0F1F0F"    // Badge background color
        },
        "comfy_base": {                  // ComfyUI base interface configuration
          "fg-color": "#fff",            // Foreground color
          "bg-color": "#202020",         // Background color
          "comfy-menu-bg": "#353535",    // Menu background color
          "comfy-menu-secondary-bg": "#303030", // Secondary menu background color
          "comfy-input-bg": "#222",      // Input field background color
          "input-text": "#ddd",          // Input text color
          "descrip-text": "#999",        // Description text color
          "drag-text": "#ccc",           // Drag text color
          "error-text": "#ff4444",       // Error text color
          "border-color": "#4e4e4e",     // Border color
          "tr-even-bg-color": "#222",    // Table even row background color
          "tr-odd-bg-color": "#353535",  // Table odd row background color
          "content-bg": "#4e4e4e",       // Content area background color
          "content-fg": "#fff",          // Content area foreground color
          "content-hover-bg": "#222",    // Content area hover background color
          "content-hover-fg": "#fff",    // Content area hover foreground color
          "bar-shadow": "rgba(16, 16, 16, 0.5) 0 0 0.5rem" // Bar shadow effect
        }
      }
    }
    

## 

​

Canvas

### 

​

Background Image

  * **Requirements** : ComfyUI frontend version 1.20.5 or newer
  * **Function** : Set a custom background image for the canvas to provide a more personalized workspace. You can upload images or use web images to set the background for the canvas.

![Set Background Image](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f393d494dfdc8b7b84997d58735d2f86)

## 

​

General

### 

​

Tab Bar Layout

  * **Default Value** : Default
  * **Options** : Default, Legacy
  * **Function** : Controls which elements the integrated tab bar contains. Legacy shows the older set of tab bar elements.



### 

​

Disable animations

  * **Default Value** : Follows the reduced motion setting of your operating system
  * **Function** : Turns off most CSS animations and transitions in the interface. This can also speed up inference when the display GPU is also used for generation.



## 

​

Node

### 

​

Node Opacity

  * **Function** : Set the opacity of nodes, where 0 represents completely transparent and 1 represents completely opaque.

![Node Opacity](https://mintcdn.com/dripart/EeFKEryMLH5667kk/images/interface/setting/appearance/node-opacity.jpg?fit=max&auto=format&n=EeFKEryMLH5667kk&q=85&s=3e19ea90315d2111d63bafcb830c9959)

## 

​

Node Widget

### 

​

Textarea Widget Font Size

  * **Default Value** : 10
  * **Range** : 8 - 24
  * **Function** : Set the font size in textarea widgets. Adjusts the text display size in text input boxes to improve readability.

![Textarea Widget Font Size](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/appearance/textarea-font-size.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=3ccfe4281cdf094edda96d3384210c1c)

## 

​

Sidebar

### 

​

Unified Sidebar Width

  * **Default Value** : Enabled
  * **Function** : When enabled, the sidebar width will be unified to a consistent width when switching between different sidebars. If disabled, different sidebars can maintain their custom widths when switching.



### 

​

Sidebar Size

  * **Function** : Control the size of the sidebar, can be set to normal or small.



### 

​

Sidebar Location

  * **Function** : Control whether the sidebar is displayed on the left or right side of the interface, allowing users to adjust the sidebar position according to their usage habits.



### 

​

Sidebar Style

  * **Function** : Control the visual style of the sidebar. Options include: 
    * **Connected** : The sidebar appears connected to the edge of the interface.
    * **Floating** : The sidebar appears as a floating panel with visual separation from the interface edge.

![Sidebar Style](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/appearance/sidbar_style.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=b7721acb769d606bf9692c399200d1f6)

## 

​

Tree Explorer

### 

​

Tree Explorer Item Padding

  * **Default Value** : 8
  * **Function** : Set the padding of items in the tree explorer (sidebar panel), adjusting the spacing between items in the tree structure.

![Tree Explorer Item Padding](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/appearance/padding.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=2e5f2411060f8524eddbeebc60afbaa8)

## 

​

Advanced Customization with user.css

For cases where the color palette doesn’t provide enough control, you can use custom CSS via a user.css file. This method is recommended for advanced users who need to customize elements that aren’t available in the color palette system.

### 

​

Requirements

  * ComfyUI frontend version 1.20.5 or newer



### 

​

Setting Up user.css

  1. Create a file named `user.css` in your ComfyUI user directory (same location as your workflows and settings - see location details below)
  2. Add your custom CSS rules to this file
  3. Restart ComfyUI or refresh the page to apply changes



### 

​

User Directory Location

The ComfyUI user directory is where your personal settings, workflows, and customizations are stored. The location depends on your installation type:

  * Desktop - Windows

  * Desktop - macOS

  * Desktop - Linux

  * Manual Install

  * Portable



    
    
    C:\Users\<your username>\AppData\Roaming\ComfyUI\user
    
    
    
    ~/<ComfyUI installation path>/ComfyUI/user
    
    
    
    ~/.config/ComfyUI/user
    

The user directory is located in your ComfyUI installation folder:
    
    
    <ComfyUI installation path>/user
    

For example, if you cloned ComfyUI to `C:\ComfyUI`, your user directory would be `C:\ComfyUI\user\default` (or `C:\ComfyUI\user\john` if you’ve set up a custom username).

ComfyUI supports multiple users per installation. If you haven’t configured a custom username, it defaults to “default”. Each user gets their own subdirectory within the `user` folder.

The user directory is located in your ComfyUI portable folder:
    
    
    <ComfyUI_windows_portable>/ComfyUI/user
    

For example: `ComfyUI_windows_portable/ComfyUI/user/default`

ComfyUI supports multiple users per installation. If you haven’t configured a custom username, it defaults to “default”. Each user gets their own subdirectory within the `user` folder.

This location contains your workflows, settings, and other user-specific files. After finding the above folder location, please copy the corresponding CSS file to the corresponding user directory, such as the default user folder being `ComfyUI/user/default`, then restart ComfyUI or refresh the page to apply changes.

### 

​

user.css Examples and Related Instructions

The `user.css` file is loaded early in the application startup process. So you may need to use `!important` in your CSS rules to ensure they override the default styles. **user.css Customization Examples**
    
    
    /* Increase font size in inputs and menus for better readability */
    .comfy-multiline-input, .litecontextmenu .litemenu-entry {
        font-size: 20px !important;
    }
    
    /* Make context menu entries larger for easier selection */
    .litegraph .litemenu-entry,
    .litemenu-title {
      font-size: 24px !important; 
    }
    
    /* Custom styling for specific elements not available in the color palette */
    .comfy-menu {
        border: 1px solid rgb(126, 179, 189) !important;
        border-radius: 0px 0px 0px 10px !important;
        backdrop-filter: blur(2px);
    }
    

**Best Practices**

  1. **Start with the color palette** for most customizations
  2. Use **user.css only when necessary** for elements not covered by the color palette
  3. **Export your theme** before making significant changes so you can revert if needed
  4. **Share your themes** with the community to inspire others

**Troubleshooting**

  * If your color palette changes don’t appear, try refreshing the page
  * If CSS customizations don’t work, check that you’re using frontend version 1.20.5+
  * Try adding `!important` to user.css rules that aren’t being applied
  * Keep backups of your customizations to easily restore them



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/appearance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/appearance)

[ComfyUI LiteGraph (Canvas) SettingsPrevious](https://docs.comfy.org/interface/settings/lite-graph)[ComfyUI 3D SettingsNext](https://docs.comfy.org/interface/settings/3d)

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
