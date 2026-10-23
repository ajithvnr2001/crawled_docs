---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-header/
title: RtkMeetingHeaderView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:49.490003+00:00
---

# RtkMeetingHeaderView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-header/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkMeetingHeaderView



# RtkMeetingHeaderView

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A pre-built meeting header that contains meeting title, clock, recording indicator, participant count, grid paginator, and switch camera button.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the header to the meeting state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.headers.RtkMeetingHeaderView
        android:id="@+id/rtk_meeting_header"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val header = findViewById<RtkMeetingHeaderView>(R.id.rtk_meeting_header)
    header.activate(meeting)

[PreviousRtkMeetingControlBarView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-control-bar/)[NextRtkMeetingOptionBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-option-bottomsheet/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-header.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
