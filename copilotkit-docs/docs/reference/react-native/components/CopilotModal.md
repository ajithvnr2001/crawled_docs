---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotModal/
title: CopilotModal
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:31.503997+00:00
---

# CopilotModal

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotModal/

React Native/Components

# CopilotModal

Headless modal wrapper around CopilotChat, plus a prebuilt bottom-sheet chat from the /components subpath.

Copy MarkdownOpen

## OverviewCopy Anchor Link

Like [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat), `CopilotModal` ships in **two** versions, chosen by import path:

  * **Headless** (`@copilotkit/react-native`) is a thin wrapper around `CopilotChat` that mirrors the web SDK's `CopilotModal` API. It provides agent wiring only; you handle modal presentation with React Native's `Modal` (or any overlay) and build the chat UI from [`useCopilotChatContext`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#usecopilotchatcontext).
  * **Prebuilt UI** (`@copilotkit/react-native/components`) is a ready-made chat in a [`@gorhom/bottom-sheet`](https://ui.gorhom.dev/components/bottom-sheet/) with snap points and swipe-to-dismiss. See Prebuilt UI.



For a drawer or a floating button, see [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar) or [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup).

## Headless `CopilotModal`Copy Anchor Link

Copy Text
    
    
    import { CopilotModal } from "@copilotkit/react-native";

Accepts all [headless `CopilotChat` props](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#props) (`agentId`, `agentName`, `threadId`, `onError`, `throttleMs`, `attachments`), plus:

Prop

Type

`children?`ReactNode

### UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotModal } from "@copilotkit/react-native";
    import { Modal } from "react-native";
    
    function App({ isOpen }: { isOpen: boolean }) {
      return (
        <Modal visible={isOpen} animationType="slide">
          <CopilotModal agentId="default">
            <MyChatUI />
          </CopilotModal>
        </Modal>
      );
    }

## Prebuilt UICopy Anchor Link

Import `CopilotModal` from the `/components` subpath for a bottom-sheet chat. Control it imperatively through a `CopilotModalRef`, or declaratively with the `visible` prop. Requires the `@gorhom/bottom-sheet`, `react-native-gesture-handler`, and `react-native-reanimated` peer dependencies.

Copy Text
    
    
    import { CopilotModal, type CopilotModalRef } from "@copilotkit/react-native/components";

### PropsCopy Anchor Link

Like the prebuilt `CopilotChat`, this component selects its agent with `agentName` (the prop the prebuilt UI currently exposes), not the headless `agentId`.

Prop

Type

`visible?`boolean

`onDismiss?`() => void

`snapPoints?`(string | number)[]

`initialSnapIndex?`number

`enableDismissOnClose?`boolean

`backdropOpacity?`number

`agentName?`string

`placeholder?`string

`initialMessages?`string[]

`headerTitle?`string

### Ref handleCopy Anchor Link

Prop

Type

`CopilotModalRef?`{ open(): void; close(): void }

### UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotModal, type CopilotModalRef } from "@copilotkit/react-native/components";
    import { useRef } from "react";
    import { Button, View } from "react-native";
    
    export function ChatScreen() {
      const modalRef = useRef<CopilotModalRef>(null);
    
      return (
        <View style={{ flex: 1 }}>
          <Button title="Open chat" onPress={() => modalRef.current?.open()} />
          <CopilotModal
            ref={modalRef}
            agentName="default"
            headerTitle="Assistant"
            snapPoints={["50%", "90%"]}
          />
        </View>
      );
    }

How is this guide?

GoodBad

[Previous PageCopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[Next PageCopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)
