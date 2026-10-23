---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/setup-screen/
title: RtkSetupFragment \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:51.160786+00:00
---

# RtkSetupFragment · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/setup-screen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkSetupFragment



# RtkSetupFragment

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUsage Examples Basic Usage

A screen shown before joining the meeting, where you can edit your display name and media settings.

## Usage Examples

### Basic Usage
    
    
    val rtkSetupFragment = RtkSetupFragment()
    supportFragmentManager.beginTransaction()
        .add(R.id.fragmentContainer, rtkSetupFragment)
        .commit()

[PreviousRtkSettingsFragment](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/settings-fragment/)[NextRtkTabSyncToggleButton](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/tab-sync-toggle-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/setup-screen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
