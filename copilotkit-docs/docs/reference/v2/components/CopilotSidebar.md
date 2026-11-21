---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:45.065093+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar/

React/Components

# CopilotSidebar

Sidebar variant of CopilotChat that renders in a fixed side panel

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotSidebar` renders a fixed sidebar panel for chat interaction. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) and provides sidebar-specific layout and open/close behavior. The sidebar includes a header with a title and close button, and can be toggled via a floating button.

See [`CopilotPopup`](https://docs.copilotkit.ai/reference/components/CopilotPopup) for a popup variant of this component.

For a walkthrough, see [Sidebar](https://docs.copilotkit.ai/prebuilt-components/sidebar).

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## PropsCopy Anchor Link

### Own PropsCopy Anchor Link

Prop

Type

`header?`SlotValue<typeof CopilotModalHeader>

`defaultOpen?`boolean

`open?`boolean

`onOpenChange?`(open: boolean) => void

`width?`number | string

### Inherited CopilotChat PropsCopy Anchor Link

`CopilotSidebar` accepts all props from [`CopilotChatProps`](https://docs.copilotkit.ai/reference/components/CopilotChat) **except** `chatView`, which is set internally to `CopilotSidebarView`. This includes:

Prop

Type

`agentId?`string

`threadId?`string

`labels?`Partial<CopilotChatLabels>

`autoScroll?`"pin-to-bottom" | "pin-to-send" | "none" | boolean

`welcomeScreen?`SlotValue<React.FC<WelcomeScreenProps>> | boolean

The `CopilotChatView` slots `messageView`, `input`, `scrollView`, and `suggestionView` are also accepted and forwarded. To pass props to the input, use the `input` slot, for example `input={{ autoFocus: true }}`. The `disclaimer` prop is deprecated. Use `input={{ disclaimer: MyDisclaimer }}` instead.

## Slot SystemCopy Anchor Link

All slot props follow the same override pattern used across CopilotKit v2 components. Each slot accepts one of three value types:

Value| Behavior  
---|---  
**Component**|  Replaces the default component entirely. Receives the same props the default would.  
**`className` string**| Merged into the default component's class list via `twMerge`.  
**Partial props object**|  Spread into the default component as additional or overriding props.  
  
## UsageCopy Anchor Link

### Basic UsageCopy Anchor Link

Copy Text
    
    
    function App() {
      return (
        <CopilotSidebar
          agentId="my-agent"
          labels={{ modalHeaderTitle: "Assistant" }}
        />
      );
    }

### Default Open with Custom WidthCopy Anchor Link

Copy Text
    
    
    function App() {
      return <CopilotSidebar agentId="my-agent" defaultOpen={true} width={500} />;
    }

### Custom HeaderCopy Anchor Link

Copy Text
    
    
    function App() {
      return (
        <CopilotSidebar agentId="my-agent" header="bg-indigo-700 text-white" />
      );
    }

## BehaviorCopy Anchor Link

  * **Toggle button** : Renders a floating toggle button that opens and closes the sidebar. The button uses `CopilotChatToggleButton` internally.
  * **Modal state** : Open/close state is managed via the chat configuration context. The `defaultOpen` prop sets the initial state; after that, state changes come from user interaction (toggle button, close button in the header). Pass `open` and `onOpenChange` to own the state yourself, and to open or close the sidebar from your own UI.
  * **Layout** : The sidebar uses `CopilotSidebarView` internally. `CopilotSidebarView` builds on [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) and provides a sidebar-specific welcome screen layout with the welcome message centered and the suggestions just above the input at the bottom.
  * **Fixed positioning** : The sidebar renders as a fixed panel on one side of the viewport. On screens 768 px wide or wider, the open sidebar adds a margin to `document.body` on its side, so your page content moves aside. On narrower screens, it covers the page.
  * **Agent connection** : All agent wiring (messages, running state, suggestions) is handled by the parent `CopilotChat` logic.



How is this guide?

GoodBad

[Previous PageCopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[Next PageCopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)
