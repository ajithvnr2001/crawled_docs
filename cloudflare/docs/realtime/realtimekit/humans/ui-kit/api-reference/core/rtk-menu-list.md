---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-menu-list/
title: rtk-menu-list \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:11.166937+00:00
---

# rtk-menu-list · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-menu-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-menu-list



# rtk-menu-list

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A menu list component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`menuVariant` | `'primary' | 'secondary'` | ✅ | - | Variant  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-menu-list></rtk-menu-list>

### With Properties
    
    
    <rtk-menu-list>
    </rtk-menu-list>
    
    
    <script>
      const el = document.querySelector("rtk-menu-list");
    
      el.iconPack = defaultIconPack;
    </script>

[Previousrtk-menu-item](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-menu-item/)[Nextrtk-message-list-view](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-message-list-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-menu-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
