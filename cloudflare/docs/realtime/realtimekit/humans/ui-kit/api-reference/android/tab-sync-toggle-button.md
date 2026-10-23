---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/tab-sync-toggle-button/
title: RtkTabSyncToggleButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:50.837046+00:00
---

# RtkTabSyncToggleButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/tab-sync-toggle-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkTabSyncToggleButton



# RtkTabSyncToggleButton

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A toggle button for syncing plugin tabs.

## Methods

Method | Parameters | Description  
---|---|---  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkTabSyncToggleButton
        android:id="@+id/rtk_tab_sync"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val tabSyncButton = findViewById<RtkTabSyncToggleButton>(R.id.rtk_tab_sync)
    tabSyncButton.isActivated = true

[PreviousRtkSetupFragment](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/setup-screen/)[NextRtkVideoDeviceSelector](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/video-device-selector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/tab-sync-toggle-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
