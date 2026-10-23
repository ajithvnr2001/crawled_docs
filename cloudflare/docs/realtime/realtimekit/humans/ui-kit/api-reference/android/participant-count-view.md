---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-count-view/
title: RtkParticipantCountView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:50.145103+00:00
---

# RtkParticipantCountView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-count-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkParticipantCountView



# RtkParticipantCountView

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A text view that displays the current number of participants in a meeting. It automatically updates when the participant count changes.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the view to the meeting state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkParticipantCountView
        android:id="@+id/rtk_participant_count"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val countView = findViewById<RtkParticipantCountView>(R.id.rtk_participant_count)
    countView.activate(meeting)

[PreviousRtkParticipantAudioIndicator](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-audio-indicator/)[NextRtkParticipantsFragment](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/participants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/participant-count-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
