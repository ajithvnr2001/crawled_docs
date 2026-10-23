---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai/
title: rtk-ai \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:51.712041+00:00
---

# rtk-ai · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-ai



# rtk-ai

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

The AI panel shows meeting transcriptions. For example, participants can read the conversation in the sidebar during a meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`view` | `AIView` | ✅ | - | View type  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-ai></rtk-ai>

### With Properties
    
    
    <!-- component.html -->
    <rtk-ai
     [meeting]="meeting"
     size="md"
     [view]="aiview">
    </rtk-ai>

[PreviousRtkWebinarStageToggleButton](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/webinar-stage-toggle/)[Nextrtk-ai-toggle](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
