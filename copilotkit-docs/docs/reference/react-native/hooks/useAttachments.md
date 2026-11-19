---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments/
title: useAttachments
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:30.365397+00:00
---

# useAttachments

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments/

React Native/Hooks

# useAttachments

React Native hook for adding multimodal file attachments to a chat using Expo's document picker and file system.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useAttachments` is the React Native counterpart of the web `useAttachments` hook. It manages picking, validating, uploading, and consuming file attachments for a chat, using [`expo-document-picker`](https://docs.expo.dev/versions/latest/sdk/document-picker/) and [`expo-file-system`](https://docs.expo.dev/versions/latest/sdk/filesystem/) in place of the web `FileReader` / `<input type="file">` APIs.

The headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat) wires this hook up for you when you pass its `attachments` prop. Call `useAttachments` directly only when you manage attachments outside of `CopilotChat`. Requires the `expo-document-picker` and `expo-file-system` peer dependencies.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useAttachments } from "@copilotkit/react-native";
    
    function useAttachments(props: UseNativeAttachmentsProps): UseNativeAttachmentsReturn;

## ParametersCopy Anchor Link

Prop

Type

`props?`UseNativeAttachmentsProps

## Return ValueCopy Anchor Link

Prop

Type

`attachments?`Attachment[]

`enabled?`boolean

`openPicker?`() => Promise<void>

`processFiles?`(files: NativeFileInput[]) => Promise<void>

`removeAttachment?`(id: string) => void

`consumeAttachments?`() => Attachment[]

### `NativeFileInput`Copy Anchor Link

The React Native equivalent of the web `File` object.

Prop

Type

`uri?`string

`name?`string

`size?`number

`mimeType?`string

## UsageCopy Anchor Link

Copy Text
    
    
    import { useAttachments } from "@copilotkit/react-native";
    import { getSourceUrl } from "@copilotkit/shared";
    import { Button, Image, View } from "react-native";
    
    function Composer() {
      const { attachments, openPicker, removeAttachment } = useAttachments({
        config: {
          enabled: true,
          accept: "image/*,application/pdf",
          maxSize: 10 * 1024 * 1024,
        },
      });
    
      return (
        <View>
          <Button title="Attach file" onPress={openPicker} />
          {attachments.map((a) => (
            <Image
              key={a.id}
              source={{ uri: getSourceUrl(a.source) }}
              style={{ width: 48, height: 48 }}
            />
          ))}
        </View>
      );
    }

Each `Attachment` exposes its content as a `source` (a base64 data source or a URL source), not a ready-made URL. `getSourceUrl` from `@copilotkit/shared` converts either form to a string you can pass to `Image`.

Most apps enable attachments declaratively through `CopilotChat` instead:

Copy Text
    
    
    <CopilotChat agentId="default" attachments={{ enabled: true, accept: "image/*" }}>
      <MyChatUI />
    </CopilotChat>

Children of `CopilotChat` read `openPicker` and `removeAttachment` from [`useCopilotChatContext`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#usecopilotchatcontext).

How is this guide?

GoodBad

[Previous PageuseAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[Next PageuseCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)
