---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/livestream-control-bar/
title: RtkLivestreamControlBarView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:48.811011+00:00
---

# RtkLivestreamControlBarView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/livestream-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkLivestreamControlBarView



# RtkLivestreamControlBarView

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A pre-built control bar for livestream meetings. Contains mic toggle, camera toggle, livestream toggle, join stage button, more toggle, and leave button.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the control bar to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbars.RtkLivestreamControlBarView
        android:id="@+id/rtk_livestream_control_bar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val controlBar = findViewById<RtkLivestreamControlBarView>(R.id.rtk_livestream_control_bar)
    controlBar.activate(meeting)

[PreviousRtkLeaveMeetingView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/leave-meeting-dialog/)[NextRtkLivestreamHeaderView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/livestream-header-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/livestream-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
