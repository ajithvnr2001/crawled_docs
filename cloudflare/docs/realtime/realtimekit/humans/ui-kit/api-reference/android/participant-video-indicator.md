---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-video-indicator/
title: RtkParticipantVideoIndicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:50.332445+00:00
---

# RtkParticipantVideoIndicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-video-indicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkParticipantVideoIndicator



# RtkParticipantVideoIndicator

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A video indicator that shows a participant's camera status.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `participant: RtkMeetingParticipant` | Bind the indicator to a participant  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkParticipantVideoIndicator
        android:id="@+id/video_indicator"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val videoIndicator = findViewById<RtkParticipantVideoIndicator>(R.id.video_indicator)
    videoIndicator.activate(participant)

[PreviousRtkParticipantTileView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-tile-view/)[NextRtkPluginsBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/plugins/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-video-indicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
