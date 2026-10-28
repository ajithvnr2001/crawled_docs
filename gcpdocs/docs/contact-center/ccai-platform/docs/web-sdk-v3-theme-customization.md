---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-theme-customization/
title: Theme customization \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T09:53:01.260764+00:00
---

# Theme customization  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-theme-customization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Theme customization Stay organized with collections  Save and categorize content based on your preferences. 

Any customizations applied to the web SDK widget UI beyond those documented here are unsupported and might result in unexpected behavior. Google recommends using the [Headless SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide) if you require more advanced customizations.

To make sure that your theme customizations appears as expected, Google recommends that you test your changes in a test environment before deploying them to production.

## Launcher design

The icon, size, position, and color of the launcher can be customized.

![The launcher design widget.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/launcher-design-window.png)

  1. Launcher

  2. Open Icon

  3. Close Icon




### Icons

If the default launcher's UI doesn't match your branding, you can customize the launcher's icons with your own SVG file. You cannot add a URL to the SVG file, it must be the SVG file itself.
    
    
    ccaas.config({
      launcherOpenIcon: '<svg ....>',
      launcherCloseIcon: '<svg ....>',
    })
    

![An icon customization example.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icons-web-sdk-v3.png)

### Size

The default width and height of the launcher is `80px`. You can change it to a different size:
    
    
    #ccaas-widget {
      --launcher-size: 60px;
    }
    

### Interaction states

The launcher's border, background, and foreground colors are configured per interaction state — default, hover, focus, and active. Each state has its own set of CSS variables, all sharing the same naming pattern: `--launcher-{state}-{property}`.

### Launcher border customization

You can customize the following options for the launcher border:

  * Border (color, width, and style — set together using the CSS border shorthand, per interaction state).
  * Drop shadow (increase or decrease).



The launcher border is configured per interaction state using the CSS border shorthand. There is no separate variable for border color or border width.
    
    
    --launcher-default-border
    --launcher-hover-border
    --launcher-focus-border
    --launcher-active-border
    --launcher-shadow
    

### Launcher colors

By default, the launcher uses the accent color.
    
    
    #ccaas-widget {
      --launcher-default-border: 6px solid var(--accent-9);
      --launcher-default-background: var(--accent-9);
      --launcher-default-color: var(--accent-contrast);
    }
    

The same pattern applies to the hover, focus, and active states (each with its own `*-border`, `*-background`, and `*-color` variable). The four `*-border` variables were listed in the Launcher border customization section. The remaining eight background and foreground state variables are:
    
    
    --launcher-default-background
    --launcher-default-color
    --launcher-hover-background
    --launcher-hover-color
    --launcher-focus-background
    --launcher-focus-color
    --launcher-active-background
    --launcher-active-color
    

You can customize the launcher to use a different color. For example:
    
    
    #ccaas-widget {
      --launcher-default-border: 6px solid var(--green-10);
      --launcher-default-background: var(--blue-10);
      --launcher-default-color: white;
    }
    

To style the launcher's hover, focus, and active states, repeat the pattern with the matching state prefix:
    
    
    #ccaas-widget {
      --launcher-hover-background: var(--blue-11);
      --launcher-focus-background: var(--blue-11);
      --launcher-active-background: var(--blue-11);
    }
    

![Launcher color customization](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-customization-example.png)

### Disable launcher

For aesthetic reasons, you might want to hide the web SDK launcher, opting to instead use a proactive chat trigger or to start the chat programmatically. You can hide or disable the launcher's UI using `disableLauncher`:
    
    
    ccaas.config({
      disableLauncher: true
    })
    

When the launcher is disabled, you can open the widget with:
    
    
    ccaas.show()
    

## Widget design

![The widget design window with options.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/widget-design-web-sdk.png)

  1. Widget

  2. Logo




### Fonts

Select different fonts for your user interface.

`--font-en`: Roboto, Verdana, Helvetica Neue

`--font-zh`: PingFang SC, Hiragino Sans GB, Droid Sans Fallback, Microsoft YaHei

`--font-ja`: Hiragino Sans, Meiryo

### Accent color

You can customize the accent `color` by selecting a predefined color option using the following configuration:
    
    
    ccaas.config({
      accent: 'green',
    })
    

Predefined colors include `default`, `blue`, `green`, `purple`, `orange`, `yellow`, `gold`, `red`.

![A chat window with the accent colors is displayed.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/accent-colors-web-sdk.png)

#### Accent customization

If the predefined choices don't suit your business needs, you can customize the style with the CSS variables.
    
    
    #ccaas-widget {
      --accent-1: #fbfdff;
      --accent-2: #f4faff;
      --accent-3: #e6f4fe;
      --accent-4: #d5efff;
      --accent-5: #c2e5ff;
      --accent-6: #acd8fc;
      --accent-7: #8ec8f6;
      --accent-8: #5eb1ef;
      --accent-9: #0090ff;
      --accent-10: #0588f0;
      --accent-11: #0d74ce;
      --accent-12: #113264;
      --accent-contrast: white;
      --chat-input-selection-color: var(--accent-11);
    }
    

The 12 accent steps follow the [Radix UI Colors scale model](https://www.radix-ui.com/docs/colors/palette). The predefined accents (`default`, `blue`, `green`, `purple`, `orange`, `yellow`, `gold`, `red`) come from this scale and are ready to use using the `accent` configuration. For any other named scale on the Radix Colors site (`mint`, `crimson`, `cyan`), copy its 12-step palette into the `--accent-1` through `--accent-12` values.

### Position

If the mount point is `#ccaas-widget`, you can update the widget position using:
    
    
    #ccaas-widget {
      --ujet-right: 20px;
      --ujet-bottom: 10px;
    }
    

### Logo

Choose a custom `logo` to appear in the widget.
    
    
    ccaas.config({
      logo: 'https://example.com/logo.png'
    })
    

![Logo customization example.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/logo-example-web-sdk.png)

### Widget border customization

You can customize the following options for the widget border:

  * Border color
  * Border width
  * Drop shadow (increase or decrease)


    
    
    --widget-border-color
    --widget-border-width
    --widget-shadow
    

### Hide the agent logo border

If the mount point is `#ccaas-widget`, you can hide the Agent Logo Border using the following code sample:
    
    
    #ccaas-widget {
    --head-logo-shadow: none;
    }
    

### Miscellaneous components

Besides accent colors and the position, the Web SDK widget has provided more CSS variables to configure some of the other components used in the widget.

If the mount point is `#ccaas-widget`, you can customize them using the following code sample:
    
    
    #ccaas-widget {
      --variable-name: value;
    }
    

The available CSS variables for each component are listed in the next section.

#### General CSS variables

`--text-font:` Default text font family.

`--text-color:` Default text color.

`--end-color:` Default color of end buttons (end chat, exit chat, end cobrowse)

#### Confirmation icon

The confirmation icon that appears on various pages throughout the SDK can be customized. You can replace the default icon with a custom icon, and control the size and color.

`--confirmation-icon-size`

`--confirmation-icon-color`

#### Buttons

You can granularly control the customization of different button types. The following table explains the expected behavior when customizing different types of buttons in combination.

**Button customizations applied** | **Result**  
---|---  
None  | Default behavior (all button styles appear according to the primary theme).   
General button customizations  | **All buttons** (excluding Dialogs/Chat screens) appear according to the customizations as set by the customer. This includes Menu Buttons.  If any general button customization variable is **NOT** specified, the default behavior is applied.   
Menu button customizations  Dialog button customizations  | **Menu Buttons** appear according to the `--menu-button` variable.  **Dialog Buttons** appear according to the `--dialog-primary-button` and `--dialog-secondary-button` variables  If any menu / dialog button customization variable is **NOT** specified, the default behavior is applied.   
General button customizations  Menu button customization  Dialog button customizations  | Menu buttons appear according to the `--menu-button` variable  Dialog buttons appear according to the `--dialog-primary-button` and `--dialog-secondary-button` variables.  Buttons that are **NOT** Menu buttons or dialog buttons appear according to the general customizations.  If any general / menu / dialog button customization variable is **NOT** specified, the default behavior is applied for that button.   
  
#### General buttons

All other buttons SDK-wide that don't have their own CSS variables use the General button configuration and customization.
    
    
    --general-button-default-background
    --general-button-default-border
    --general-button-default-color
    --general-button-default-outline
    --general-button-hover-background
    --general-button-hover-border
    --general-button-hover-color
    --general-button-hover-outline
    --general-button-active-background
    --general-button-active-border
    --general-button-active-color
    --general-button-active-outline
    --general-button-focus-background
    --general-button-focus-border
    --general-button-focus-color
    --general-button-focus-outline
    

#### Primary button
    
    
    --primary-button-default-background
    --primary-button-default-color
    --primary-button-focus-background
    --primary-button-focus-color
    --primary-button-hover-background
    --primary-button-hover-color
    --primary-button-active-background
    --primary-button-active-color
    --primary-button-disabled-background
    --primary-button-disabled-color
    

#### Secondary buttons
    
    
    --secondary-button-default-background
    --secondary-button-default-border
    --secondary-button-default-color
    --secondary-button-hover-background
    --secondary-button-hover-border
    --secondary-button-hover-color
    --secondary-button-active-background
    --secondary-button-active-border
    --secondary-button-active-color
    --secondary-button-disabled-background
    --secondary-button-disabled-border
    --secondary-button-disabled-color
    --secondary-button-focus-background
    --secondary-button-focus-border
    --secondary-button-focus-outline
    --secondary-button-focus-color
    

#### Secondary buttons (inverse)
    
    
    --inverse-button-default-background
    --inverse-button-default-border
    --inverse-button-default-outline
    --inverse-button-default-color
    --inverse-button-hover-background
    --inverse-button-hover-border
    --inverse-button-hover-outline
    --inverse-button-hover-color
    --inverse-button-active-background
    --inverse-button-active-border
    --inverse-button-active-outline
    --inverse-button-active-color
      
    --inverse-button-disabled-background
    --inverse-button-disabled-border
    --inverse-button-disabled-color
    --inverse-button-focus-background
    --inverse-button-focus-border
    --inverse-button-focus-outline
    --inverse-button-focus-color
    

#### Menu buttons

For example, queue selection and channel selection.
    
    
    --menu-button-default-background
    --menu-button-default-border
    --menu-button-default-color
    --menu-button-default-outline
    --menu-button-hover-background
    --menu-button-hover-border
    --menu-button-hover-color
    --menu-button-hover-outline
    --menu-button-active-background
    --menu-button-active-border
    --menu-button-active-color
    --menu-button-active-outline
    --menu-button-focus-background
    --menu-button-focus-border
    --menu-button-focus-color
    --menu-button-focus-outline
    

![An example of menu buttons is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/menu-buttons-web-sdk.png)

#### Dialog buttons

For example, modals or pop-ups.
    
    
    --dialog-background
    --dialog-color
    --dialog-primary-button-default-background
    --dialog-primary-button-default-border
    --dialog-primary-button-default-color
    --dialog-primary-button-default-outline
    --dialog-primary-button-hover-background
    --dialog-primary-button-hover-border
    --dialog-primary-button-hover-color
    --dialog-primary-button-hover-outline
    --dialog-primary-button-focus-background
    --dialog-primary-button-focus-border
    --dialog-primary-button-focus-color
    --dialog-primary-button-focus-outline
    --dialog-primary-button-active-background
    --dialog-primary-button-active-border
    --dialog-primary-button-active-color
    --dialog-primary-button-active-outline
    --dialog-secondary-button-default-background
    --dialog-secondary-button-default-border
    --dialog-secondary-button-default-color
    --dialog-secondary-button-default-outline
    --dialog-secondary-button-hover-background
    --dialog-secondary-button-hover-border
    --dialog-secondary-button-hover-color
    --dialog-secondary-button-hover-outline
    --dialog-secondary-button-focus-background
    --dialog-secondary-button-focus-border
    --dialog-secondary-button-focus-color
    --dialog-secondary-button-focus-outline
    --dialog-secondary-button-active-background
    --dialog-secondary-button-active-border
    --dialog-secondary-button-active-color
    --dialog-secondary-button-active-outline
    

![An example of a dialog buttons with options to end a chat is
shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dialog-buttons-web-sdk.png)

#### Chat header
    
    
    --options-menu-icon-default-color
    --options-menu-icon-hover-color
    --options-menu-icon-active-color
    --options-menu-icon-default-background
    --options-menu-icon-hover-background
    --options-menu-icon-active-background
    --options-menu-icon-focus-background
    

![An example of a chat window with the header
emphasized.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/chat-header-web-sdk.png)

#### Mute chat
    
    
    ccaas.config({
      enableMuteChat: true,
    })
    

#### Chat bubble
    
    
    --chat-bubble-background
    --chat-bubble-border
    --chat-bubble-text
    --chat-bubble-line-height
    --chat-bubble-agent-background
    --chat-bubble-agent-color
    --chat-bubble-agent-border
    --chat-bubble-agent-border-radius
    --chat-bubble-user-background
    --chat-bubble-user-color
    --chat-bubble-user-border
    --chat-bubble-user-border-radius
    

![An example of a chat window with the message bubbles highlighted is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/chat-bubbles.png)

### Chat bubble customization

**Message** :
    
    
    --message-event-general-font
    --message-event-general-font-size
    --message-event-general-font-weight
    --message-event-general-color
    --message-event-error-font
    --message-event-error-font-size
    --message-event-error-font-weight
    --message-event-error-color
    --message-event-confirmation-font
    --message-event-confirmation-font-size
    --message-event-confirmation-font-weight
    --message-event-confirmation-color
    

![An example of a chat window with the custom message bubbles highlighted is
shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/message-customization.png)
    
    
    --message-progress-color
    --message-button-font-family
    --message-button-font-size
    --message-button-default-background
    --message-button-default-border
    --message-button-default-color
    --message-button-default-font-style
    --message-button-hover-background
    --message-button-hover-border
    --message-button-hover-color
    --message-button-hover-font-style
    --message-button-focus-background
    --message-button-focus-border
    --message-button-focus-color
    --message-button-focus-font-style
    --message-button-active-background
    --message-button-active-border
    --message-button-active-color
    --message-button-active-font-style
    --message-button-disabled-background
    --message-button-disabled-border
    --message-button-disabled-color
    --message-button-disabled-font-style
    

**Post-session virtual agent** :
    
    
    --post-session-background
    --post-session-padding
    

![An example of the post-session window is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/post-session-virtual-agent.png)

**Custom form link** :
    
    
    --form-card-background
    --form-card-title-color
    --form-card-status-color
    --form-card-subtitle-color
    --form-card-image-height
    --form-card-title-font-size
    --form-card-title-font-weight
    --form-card-border-radius
    --form-card-subtitle-font-weight
    --form-card-subtitle-font-size
    

**Custom form** :
    
    
    --form-title-font-size
    --form-title-font-weight
    --form-title-color
    --form-title-font-style
    --form-header-font-size
    --form-header-font-weight
    --form-header-color
    --form-header-font-style
    --form-footer-font-size
    --form-footer-font-weight
    --form-footer-color
    --form-footer-font-style
    --form-field-border-radius
    --form-field-cursor-color
    --form-field-label-font-size
    --form-field-label-font-weight
    --form-field-label-color
    --form-field-label-font-style
    --form-field-active-border-color
    --form-field-active-border-width
    --form-field-inactive-border-color
    --form-field-inactive-border-width
    --form-field-list-selection-checkbox-color
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
