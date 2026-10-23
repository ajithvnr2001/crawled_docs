---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkparticipantsstagequeue/
title: RtkParticipantsStageQueue \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:37.158774+00:00
---

# RtkParticipantsStageQueue · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkparticipantsstagequeue/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantsStageQueue



# RtkParticipantsStageQueue

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays participants who have requested access to the stage. The list includes controls for accepting or denying their requests.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantsStageQueue } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantsStageQueue />;
    }

### With Properties
    
    
    import { RtkParticipantsStageQueue } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantsStageQueue
          meeting={meeting}
          size="md"
          view={participantsviewmode}
        />
      );
    }

[PreviousRtkParticipantsStageList](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkparticipantsstagelist/)[NextRtkParticipantsToggle](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkparticipantstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react/RtkParticipantsStageQueue.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
