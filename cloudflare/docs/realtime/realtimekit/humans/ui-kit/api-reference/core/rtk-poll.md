---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-poll/
title: rtk-poll \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:14.228032+00:00
---

# rtk-poll · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-poll/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-poll



# rtk-poll

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A poll component. Shows a poll where a user can vote.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`permissions` | `RTKPermissionsPreset` | ✅ | - | Permissions Object  
`poll` | `Poll` | ✅ | - | Poll  
`self` | `string` | ✅ | - | Self ID  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-poll></rtk-poll>

### With Properties
    
    
    <rtk-poll
     self="example">
    </rtk-poll>
    
    
    <script>
      const el = document.querySelector("rtk-poll");
    
      el.iconPack = defaultIconPack;
    </script>

[Previousrtk-plugins-toggle](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-plugins-toggle/)[Nextrtk-poll-form](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-poll-form/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-poll.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
