---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-more-toggle/
title: rtk-more-toggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:58.554565+00:00
---

# rtk-more-toggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-more-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-more-toggle



# rtk-more-toggle

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visibility of a more menu. When clicked it emits a `rtkStateUpdate` event with the data:
    
    
    { activeMoreMenu: boolean; }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-more-toggle></rtk-more-toggle>

### With Properties
    
    
    <!-- component.html -->
    <rtk-more-toggle
     size="md">
    </rtk-more-toggle>

[Previousrtk-mixed-grid](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-mixed-grid/)[Nextrtk-mute-all-button](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-mute-all-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/angular/rtk-more-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
