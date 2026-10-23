---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkcontrolbar/
title: RtkControlbar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:30.933486+00:00
---

# RtkControlbar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkcontrolbar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React
  5. /RtkControlbar



# RtkControlbar

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Controlbar component provides you with various designs as variants.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`disableRender` | `boolean` | ✅ | - | Whether to render the default UI  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'boxed'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkControlbar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkControlbar />;
    }

### With Properties
    
    
    import { RtkControlbar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkControlbar
          disableRender={true}
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkConfirmationModal](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkconfirmationmodal/)[NextRtkControlbarButton](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkcontrolbarbutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react/RtkControlbar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
