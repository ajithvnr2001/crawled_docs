---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkplugins/
title: RtkPlugins \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:26.209880+00:00
---

# RtkPlugins · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkplugins/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React Native
  5. /RtkPlugins



# RtkPlugins

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Plugin management panel showing active plugins and the plugin store with activate/deactivate controls.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPlugins } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPlugins meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkPlugins } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPlugins meeting={meeting} size="md" config={customConfig} />;
    }

[PreviousRtkPluginMain](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkpluginmain/)[NextRtkPluginsToggle](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkpluginstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react-native/RtkPlugins.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
