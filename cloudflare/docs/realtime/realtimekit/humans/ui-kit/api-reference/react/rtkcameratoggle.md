---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkcameratoggle/
title: RtkCameraToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:29.599216+00:00
---

# RtkCameraToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkcameratoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React
  5. /RtkCameraToggle



# RtkCameraToggle

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles your camera.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkCameraToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkCameraToggle />;
    }

### With Properties
    
    
    import { RtkCameraToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkCameraToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkCameraSelector](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkcameraselector/)[NextRtkCaptionToggle](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkcaptiontoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react/RtkCameraToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
