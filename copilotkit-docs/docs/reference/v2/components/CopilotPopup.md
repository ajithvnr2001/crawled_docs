---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:12.724833+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotPopup/

React/Components

# CopilotPopup

Popup variant of CopilotChat that renders in a floating panel with a toggle button

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotPopup` renders a floating chat popup with a toggle button. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) and provides popup-specific layout, sizing, and open/close behavior. The popup includes a header with a title and close button, and can be dismissed by clicking outside.

See [`CopilotSidebar`](https://docs.copilotkit.ai/reference/components/CopilotSidebar) for a sidebar variant of this component.

For a walkthrough, see [Popup](https://docs.copilotkit.ai/prebuilt-components/popup).

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotPopup } from "@copilotkit/react-core/v2";
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

`height?`number | string

`clickOutsideToClose?`boolean

### Inherited CopilotChat PropsCopy Anchor Link

`CopilotPopup` accepts all props from [`CopilotChatProps`](https://docs.copilotkit.ai/reference/components/CopilotChat) **except** `chatView`, which is set internally to `CopilotPopupView`. This includes:

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
        <CopilotPopup
          agentId="my-agent"
          labels={{ modalHeaderTitle: "Assistant" }}
        />
      );
    }

### Custom Size and Default OpenCopy Anchor Link

Copy Text
    
    
    function App() {
      return (
        <CopilotPopup
          agentId="my-agent"
          defaultOpen={true}
          width={450}
          height="80vh"
          clickOutsideToClose={false}
        />
      );
    }

### Custom HeaderCopy Anchor Link

Copy Text
    
    
    function App() {
      return <CopilotPopup agentId="my-agent" header="bg-blue-600 text-white" />;
    }

## BehaviorCopy Anchor Link

  * **Toggle button** : Renders a floating toggle button (typically in the bottom-right corner) that opens and closes the popup. The button uses `CopilotChatToggleButton` internally.
  * **Modal state** : Open/close state is managed via the chat configuration context. The `defaultOpen` prop sets the initial state; after that, state changes come from user interaction (toggle button, close button, clicking outside). Pass `open` and `onOpenChange` to own the state yourself, and to open or close the popup from your own UI.
  * **Click outside** : When `clickOutsideToClose` is `true` (the default), clicking anywhere outside the popup panel closes it.
  * **Layout** : The popup uses `CopilotPopupView` internally. `CopilotPopupView` builds on [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) and provides a popup-specific welcome screen layout with the welcome message centered vertically and suggestions just above the input.
  * **Agent connection** : All agent wiring (messages, running state, suggestions) is handled by the parent `CopilotChat` logic.



How is this guide?

GoodBad

[Previous PageCopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[Next PageCopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)
