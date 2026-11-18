---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useThreads/
title: useThreads
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:28:00.874077+00:00
---

# useThreads

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useThreads/

React Native/Hooks

# useThreads

React hook for listing, managing, and syncing conversation threads with useThreads. Rename, archive, delete, and paginate threads with realtime updates via WebSocket.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useThreads` is a React hook for managing conversation threads in CopilotKit Intelligence. It fetches the thread list for a given agent, keeps it synchronized in realtime via WebSocket, and exposes mutation methods for renaming, archiving, and deleting threads. For a full walkthrough, see [Headless Threads](https://docs.copilotkit.ai/headless-threads).

Thread persistence runs in CopilotKit Intelligence, which is accessed with a `publicLicenseKey`. That key is **not yet supported on React Native** (see [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)), so `useThreads` is documented here for API parity but is not yet usable on React Native.

Re-exported from `@copilotkit/react-core/v2`, identical to the [React (V2) `useThreads`](https://docs.copilotkit.ai/reference/v2/hooks/useThreads). The only difference is the import path.

Threads are sorted by most recent run first. The hook supports cursor-based pagination when a `limit` is provided.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useThreads } from "@copilotkit/react-native";
    
    function useThreads(input: UseThreadsInput): UseThreadsResult

## ParametersCopy Anchor Link

Prop

Type

`input?`UseThreadsInput

## Return ValueCopy Anchor Link

Prop

Type

`result?`UseThreadsResult

## UsageCopy Anchor Link

ThreadList.tsx

Copy Text
    
    
    import { useThreads } from "@copilotkit/react-native";
    import { FlatList, Text, TouchableOpacity, View } from "react-native";
    
    function ThreadList() {
      const {
        threads,
        isLoading,
        renameThread,
        archiveThread,
        deleteThread,
      } = useThreads({ agentId: "my-agent" });
    
      if (isLoading) {
        return (
          <View>
            <Text>Loading threads...</Text>
          </View>
        );
      }
    
      return (
        <FlatList
          data={threads}
          keyExtractor={(thread) => thread.id}
          renderItem={({ item: thread }) => (
            <View>
              <Text>{thread.name ?? "Untitled"}</Text>
              <TouchableOpacity onPress={() => renameThread(thread.id, "New name")}>
                <Text>Rename</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => archiveThread(thread.id)}>
                <Text>Archive</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => deleteThread(thread.id)}>
                <Text>Delete</Text>
              </TouchableOpacity>
            </View>
          )}
        />
      );
    }

## BehaviorCopy Anchor Link

  * On mount, fetches the thread list and establishes a realtime WebSocket subscription. [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/intelligence/threads-explained) explains the event replay model and the WebSocket sync.
  * Thread creates, renames, archives, and deletes from any client are reflected immediately without polling.
  * Mutations update the list at once, before the server confirms. If the server rejects a delete, the thread comes back and `error` is set. Rename, archive, and unarchive do not roll back. Promises resolve when the server accepts the request and reject on failure.
  * The `error` state updates with the most recent error from any operation.
  * The `threads` array is sorted by most recent run first (`lastRunAt`, then `updatedAt`, then `createdAt`). For a thread that has run, a rename or archive does not change its place.
  * New threads are **automatically named** when their first run creates them. By default, the name is the first user message. To get a short summary title from a model, set `generateThreadNames: { model }` on the runtime.



How is this guide?

GoodBad

[Previous PageuseSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[Next PageOverview](https://docs.copilotkit.ai/reference/vue)
