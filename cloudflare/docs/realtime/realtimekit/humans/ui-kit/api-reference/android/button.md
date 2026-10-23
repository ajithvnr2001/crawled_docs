---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/button/
title: RtkButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:47.565564+00:00
---

# RtkButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkButton



# RtkButton

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesMethodsUsage Examples Basic Usage

A button that follows the RealtimeKit design system.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`rtk_btn_variant` | `primary | secondary | danger` | ❌ | - | Button variant  
  
## Methods

Method | Parameters | Description  
---|---|---  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
`refresh` | `uiTokens: RtkDesignTokens` | Refresh the button with the provided tokens  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.button.RtkButton
        android:id="@+id/btn_id"
        android:layout_width="200dp"
        android:layout_height="48dp"
        android:text="Text on Button"
        app:rtk_btn_variant="primary" />

[PreviousRtkAvatarView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/avatar-view/)[NextRtkCameraToggleButton](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/camera-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
