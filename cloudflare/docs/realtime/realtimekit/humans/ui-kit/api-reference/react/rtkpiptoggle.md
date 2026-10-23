---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkpiptoggle/
title: RtkPipToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:37.704647+00:00
---

# RtkPipToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkpiptoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React
  5. /RtkPipToggle



# RtkPipToggle

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button to turn Picture-in-Picture mode on or off when available. For example, a participant can keep the meeting video visible while using another app.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPipToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPipToggle />;
    }

### With Properties
    
    
    import { RtkPipToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPipToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkPinnedMessageSelector](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkpinnedmessageselector/)[NextRtkPluginMain](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkpluginmain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react/RtkPipToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
