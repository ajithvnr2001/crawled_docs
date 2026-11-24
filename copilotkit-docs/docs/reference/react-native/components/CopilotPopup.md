---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:51.356386+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup/

React Native/Components

# CopilotPopup

A prebuilt floating action button that opens a CopilotChat session in a modal overlay card.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotPopup` renders a floating action button (FAB) that opens a chat in a modal overlay card with a header and a dismissible backdrop. Like [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar), its chat area wraps a headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat). Provide your chat UI as `children`, or drop in the prebuilt UI `CopilotChat` from `@copilotkit/react-native/components`.

Control it imperatively through a `CopilotPopupHandle` ref.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotPopup, type CopilotPopupHandle } from "@copilotkit/react-native";

## PropsCopy Anchor Link

Prop

Type

`agentId?`string

`agentName?`string

`threadId?`string

`throttleMs?`number

`defaultOpen?`boolean

`height?`number | string

`onError?`(error: Error) => void

`headerTitle?`string

`attachments?`NativeAttachmentsConfig

`children?`ReactNode

`onOpen?`() => void

`onClose?`() => void

`dismissOnBackdropPress?`boolean

`showToggleButton?`boolean

`style?`ViewStyle

## Ref handleCopy Anchor Link

Prop

Type

`CopilotPopupHandle?`{ open(): void; close(): void; toggle(): void }

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotPopup, type CopilotPopupHandle } from "@copilotkit/react-native";
    import { CopilotChat } from "@copilotkit/react-native/components";
    import { useRef } from "react";
    
    export function ChatScreen() {
      const popupRef = useRef<CopilotPopupHandle>(null);
    
      return (
        <CopilotPopup ref={popupRef} agentId="default" headerTitle="Chat">
          <CopilotChat agentName="default" showHeader={false} />
        </CopilotPopup>
      );
    }

## BehaviorCopy Anchor Link

  * **Overlay** : the popup opens as a modal card floating above your content, with a semi-transparent backdrop.
  * **Backdrop dismiss** : tapping the backdrop closes the popup when `dismissOnBackdropPress` is `true`.
  * **FAB** : when `showToggleButton` is `true`, a floating action button opens the popup and hides while it is open.
  * **Height** : a percentage `height` (e.g. `"60%"`) resolves against the screen height; a number is used as points.



How is this guide?

GoodBad

[Previous PageCopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[Next PageCopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)
