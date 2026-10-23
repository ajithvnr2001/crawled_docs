---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/settings-bottomsheet/
title: RtkSettingsBottomsheet \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:51.220728+00:00
---

# RtkSettingsBottomsheet · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/settings-bottomsheet/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkSettingsBottomsheet



# RtkSettingsBottomsheet

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage

A settings bottom sheet that contains audio and video device selectors and a self-preview tile. Used in portrait orientation.

## Methods

Method | Parameters | Description  
---|---|---  
`show` | `fragmentManager: FragmentManager, tag: String?` | Display the settings bottom sheet  
  
## Usage Examples

### Basic Usage
    
    
    val settingsBottomSheet = RtkSettingsBottomsheet()
    settingsBottomSheet.show(fragmentManager, "SETTINGS_TAG")

[PreviousRtkRecordingIndicator](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/recording-indicator/)[NextRtkSettingsFragment](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/settings-fragment/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/settings-bottomsheet.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
