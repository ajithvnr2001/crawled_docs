---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai-toggle/
title: rtk-ai-toggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:52.104190+00:00
---

# rtk-ai-toggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-ai-toggle



# rtk-ai-toggle

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-ai-toggle></rtk-ai-toggle>

### With Properties
    
    
    <!-- component.html -->
    <rtk-ai-toggle
     [meeting]="meeting"
     size="md"
     variant="button">
    </rtk-ai-toggle>

[Previousrtk-ai](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai/)[Nextrtk-ai-transcriptions](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai-transcriptions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-ai-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
