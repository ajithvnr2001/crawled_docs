---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkparticipants/
title: RtkParticipants \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:25.236604+00:00
---

# RtkParticipants · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkparticipants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React Native
  5. /RtkParticipants



# RtkParticipants

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Full participants list panel showing on-stage participants, viewers, waitlisted users, and stage request management with accept/reject all functionality.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipants } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkParticipants meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkParticipants } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkParticipants meeting={meeting} size="md" config={customConfig} />;
    }

[PreviousRtkParticipantCount](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkparticipantcount/)[NextRtkParticipantTile](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkparticipanttile/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react-native/RtkParticipants.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
