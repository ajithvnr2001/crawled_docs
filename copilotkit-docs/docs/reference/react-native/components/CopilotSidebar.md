---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:30.664222+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar/

React Native/Components

# CopilotSidebar

A prebuilt slide-in drawer from the right edge of the screen that wraps a CopilotChat session.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotSidebar` renders a slide-in drawer from the right edge of the screen, with a header bar, a backdrop, and an optional floating action button (FAB) to toggle it. The drawer's chat area wraps a headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat). Render your chat UI as `children` (consuming [`useCopilotChatContext`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#usecopilotchatcontext)) or drop in the prebuilt UI `CopilotChat` from `@copilotkit/react-native/components`. For a centered card, see [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup).

Control it imperatively through a `CopilotSidebarHandle` ref.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotSidebar, type CopilotSidebarHandle } from "@copilotkit/react-native";

## PropsCopy Anchor Link

Accepts the headless [`CopilotChat` props](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#props) (`agentId`, `agentName`, `threadId`, `onError`, `throttleMs`, `attachments`) except `children` is repurposed for the drawer body, plus:

Prop

Type

`defaultOpen?`boolean

`width?`number | string

`headerTitle?`string

`showToggleButton?`boolean

`onOpen?`() => void

`onClose?`() => void

`style?`ViewStyle

`children?`ReactNode

## Ref handleCopy Anchor Link

Prop

Type

`CopilotSidebarHandle?`{ open(): void; close(): void; toggle(): void }

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotSidebar, type CopilotSidebarHandle } from "@copilotkit/react-native";
    import { CopilotChat } from "@copilotkit/react-native/components";
    import { useRef } from "react";
    
    export function ChatScreen() {
      const sidebarRef = useRef<CopilotSidebarHandle>(null);
    
      return (
        <CopilotSidebar ref={sidebarRef} agentId="default" headerTitle="Assistant">
          <CopilotChat agentName="default" showHeader={false} />
        </CopilotSidebar>
      );
    }

## BehaviorCopy Anchor Link

  * **Animation** : slides in/out over 300ms using the React Native `Animated` API.
  * **Backdrop** : a semi-transparent, pressable backdrop dismisses the drawer.
  * **FAB** : when `showToggleButton` is `true`, a floating button opens the drawer and hides while it is open.



How is this guide?

GoodBad

[Previous PageCopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[Next PageGenerativeUIActivity](https://docs.copilotkit.ai/reference/react-native/components/GenerativeUIActivity)
