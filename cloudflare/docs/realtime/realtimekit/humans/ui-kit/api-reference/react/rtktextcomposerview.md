---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtktextcomposerview/
title: RtkTextComposerView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:40.468773+00:00
---

# RtkTextComposerView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtktextcomposerview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React
  5. /RtkTextComposerView



# RtkTextComposerView

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a text composer

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`disabled` | `boolean` | ✅ | - | Disable the text input (default = false)  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`keyDownHandler` | `(e: KeyboardEvent) => void` | ✅ | - | Keydown event handler function  
`maxLength` | `number` | ✅ | - | Max length for text input  
`placeholder` | `string` | ✅ | - | Placeholder text  
`rateLimitBreached` | `boolean` | ✅ | - | Boolean to indicate if rate limit is breached  
`setText` | `(text: string, focus?: boolean) => Promise<void>` | ❌ | - | Sets value of the text input  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`value` | `string` | ✅ | - | Default value for text input  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkTextComposerView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkTextComposerView />;
    }

### With Properties
    
    
    import { RtkTextComposerView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkTextComposerView
          disabled={true}
          keyDownHandler={handleEvent}
          maxLength={42}
        />
      );
    }

[PreviousRtkTabBar](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtktabbar/)[NextRtkTextMessage](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtktextmessage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react/RtkTextComposerView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
