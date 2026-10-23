---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkmenulist/
title: RtkMenuList \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:24.202201+00:00
---

# RtkMenuList · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkmenulist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React Native
  5. /RtkMenuList



# RtkMenuList

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage

A horizontal list container for menu items.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`children` | `ReactNode` | ✅ | - | Menu list content  
  
## Usage Examples

### Basic Usage
    
    
    import {
    	RtkMenuList,
    	RtkMenuItem,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMenuList>
    			<RtkMenuItem onClick={() => {}}>
    				<Text>Item 1</Text>
    			</RtkMenuItem>
    			<RtkMenuItem onClick={() => {}}>
    				<Text>Item 2</Text>
    			</RtkMenuItem>
    		</RtkMenuList>
    	);
    }

[PreviousRtkMenuItem](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkmenuitem/)[NextRtkMicToggle](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react-native/rtkmictoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react-native/RtkMenuList.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
