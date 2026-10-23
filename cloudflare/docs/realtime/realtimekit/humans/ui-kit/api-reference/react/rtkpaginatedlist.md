---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkpaginatedlist/
title: RtkPaginatedList \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:36.022091+00:00
---

# RtkPaginatedList · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkpaginatedlist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /React
  5. /RtkPaginatedList



# RtkPaginatedList

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`autoScroll` | `boolean` | ✅ | - | auto scroll list to bottom  
`createNodes` | `(data: unknown[]) => VNode[]` | ✅ | - | Create nodes  
`emptyListLabel` | `string` | ✅ | - | label to show when empty  
`fetchData` | `(timestamp: number, size: number, reversed: boolean) => Promise<unknown[]>` | ✅ | - | Fetch the data  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`onNewNode` | `(node: DataNode) => Promise<void>` | ✅ | - | Adds a new node to the beginning of the paginated list  
`onNodeDelete` | `(id: string) => Promise<void>` | ✅ | - | Deletes a node anywhere from the list  
`onNodeUpdate` | `(id: string, node: DataNode) => Promise<void>` | ✅ | - | Updates an existing node in the paginated list.  
`pageSize` | `number` | ✅ | - | Page Size  
`pagesAllowed` | `number` | ✅ | - | Number of pages allowed to be shown  
`rerenderList` | `() => Promise<void>` | ✅ | - | Rerender paginated list  
`reset` | `(timestamp?: number) => Promise<void>` | ❌ | - | Resets the paginated list to a given timestamp  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPaginatedList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPaginatedList />;
    }

### With Properties
    
    
    import { RtkPaginatedList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPaginatedList
          autoScroll={true}
          createNodes={handleEvent}
          emptyListLabel="example"
        />
      );
    }

[PreviousRtkOverlayModal](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkoverlaymodal/)[NextRtkParticipant](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/react/rtkparticipant/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/react/RtkPaginatedList.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
