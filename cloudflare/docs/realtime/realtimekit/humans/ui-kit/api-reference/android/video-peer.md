---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/video-peer/
title: RtkVideoPeer \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:50.900959+00:00
---

# RtkVideoPeer · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/video-peer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkVideoPeer



# RtkVideoPeer

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A view that renders a participant's video stream with an avatar fallback when video is disabled.

## Methods

Method | Parameters | Description  
---|---|---  
`refresh` | `participant: RtkMeetingParticipant, isScreenShare: Boolean` | Update the view with the participant data  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkVideoPeer
        android:id="@+id/rtk_video_peer"
        android:layout_width="match_parent"
        android:layout_height="200dp" />

### With Methods
    
    
    val videoPeer = findViewById<RtkVideoPeer>(R.id.rtk_video_peer)
    videoPeer.refresh(participant, isScreenShare = false)

[PreviousRtkVideoDeviceSelector](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/video-device-selector/)[NextRtkWebinarControlBarView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/webinar-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/video-peer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
