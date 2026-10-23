---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/webinar-control-bar/
title: RtkWebinarControlBarView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:51.297340+00:00
---

# RtkWebinarControlBarView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/webinar-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkWebinarControlBarView



# RtkWebinarControlBarView

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A pre-built control bar for webinar meetings. Contains mic toggle, camera toggle, webinar stage toggle, more toggle, and leave button.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the control bar to the meeting state  
`deactivate` | - | Unbind the control bar and remove event listeners  
`refreshStageToggleButton` | - | Force a refresh of the stage toggle button state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbars.RtkWebinarControlBarView
        android:id="@+id/rtk_webinar_control_bar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val controlBar = findViewById<RtkWebinarControlBarView>(R.id.rtk_webinar_control_bar)
    controlBar.activate(meeting)

[PreviousRtkVideoPeer](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/video-peer/)[NextRtkWebinarStageToggleButton](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/webinar-stage-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/webinar-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
