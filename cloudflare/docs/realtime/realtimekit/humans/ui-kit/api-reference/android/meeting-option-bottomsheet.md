---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-option-bottomsheet/
title: RtkMeetingOptionBottomSheet \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:49.714193+00:00
---

# RtkMeetingOptionBottomSheet · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-option-bottomsheet/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkMeetingOptionBottomSheet



# RtkMeetingOptionBottomSheet

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage

A bottom sheet shown when tapping the more button. Contains options for participants, chat, polls, plugins, recording, screen share, mute all, and settings.

## Methods

Method | Parameters | Description  
---|---|---  
`show` | `fragmentManager: FragmentManager, tag: String?` | Display the meeting options bottom sheet  
  
## Usage Examples

### Basic Usage
    
    
    val meetingOptions = RtkMeetingOptionBottomSheet()
    meetingOptions.show(fragmentManager, "MEETING_OPTIONS_TAG")

[PreviousRtkMeetingHeaderView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-header/)[NextRtkMeetingTitleView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-title-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/meeting-option-bottomsheet.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
