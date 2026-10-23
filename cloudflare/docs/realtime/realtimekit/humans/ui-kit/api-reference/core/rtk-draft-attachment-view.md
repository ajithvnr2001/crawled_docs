---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-draft-attachment-view/
title: rtk-draft-attachment-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:08.144920+00:00
---

# rtk-draft-attachment-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-draft-attachment-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-draft-attachment-view



# rtk-draft-attachment-view

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders the draft attachment to send

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`attachment` | `{ type: 'image' | 'file'; file: File; }` | ✅ | - | Attachment to display  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-draft-attachment-view></rtk-draft-attachment-view>

### With Properties
    
    
    <rtk-draft-attachment-view>
    </rtk-draft-attachment-view>
    
    
    <script>
      const el = document.querySelector("rtk-draft-attachment-view");
    
      el.attachment = {};
    </script>

[Previousrtk-dialog-manager](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-dialog-manager/)[Nextrtk-emoji-picker](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-emoji-picker/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/core/rtk-draft-attachment-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
