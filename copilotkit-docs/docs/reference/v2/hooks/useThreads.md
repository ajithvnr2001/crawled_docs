---
url: https://docs.copilotkit.ai/reference/v2/hooks/useThreads/
title: useThreads
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:23.211489+00:00
---

# useThreads

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useThreads/

React/Hooks

# useThreads

React hook for listing, managing, and syncing conversation threads with useThreads. Rename, archive, delete, and paginate threads with realtime updates via WebSocket.

Copy MarkdownOpen

[useThreads needs a CopilotKit Intelligence projectCreate a cloud-hosted project or connect a self-hosted deployment to start syncing threads.Create a free account](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_reference_use_threads&utm_frontend=react)

## OverviewCopy Anchor Link

Intelligence’s [AG-UI streams](https://docs.copilotkit.ai/AG-UI-Streams) provide the event history and delivery behind these conversations. For the event replay model, see [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/intelligence/threads-explained). Use `useThreads` to manage the conversation list, then pass the selected `threadId` to your chat. Your framework keeps its own conversation and model-context management.

`useThreads` is a React hook for managing conversation threads in CopilotKit Intelligence. It fetches the thread list for a given agent, keeps it synchronized in realtime via WebSocket, and exposes mutation methods for renaming, archiving, and deleting threads.

Threads are sorted by the most recent run (`lastRunAt`), then by `updatedAt` for threads that have not run. The hook supports cursor-based pagination when a `limit` is provided.

For a full thread sidebar, see [Headless Threads](https://docs.copilotkit.ai/headless-threads).

`useThreads` only activates when the connected runtime advertises compatible REST thread endpoints. Cloud-hosted Intelligence provides those endpoints for thread metadata and realtime updates. A self-managed runner, such as `AgentRunner`, `SqliteAgentRunner`, or a custom runner, can persist and replay chat history. It does not provide the thread list, the thread mutations, or the realtime updates that `useThreads` needs.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useThreads } from "@copilotkit/react-core/v2";
    
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
    
    
    import { useThreads } from "@copilotkit/react-core/v2";
    
    function ThreadList() {
      const {
        threads,
        isLoading,
        renameThread,
        archiveThread,
        deleteThread,
      } = useThreads({ agentId: "my-agent" });
    
      if (isLoading) return <div>Loading threads...</div>;
    
      return (
        <ul>
          {threads.map((thread) => (
            <li key={thread.id}>
              <span>{thread.name ?? "Untitled"}</span>
              <button onClick={() => renameThread(thread.id, "New name")}>
                Rename
              </button>
              <button onClick={() => archiveThread(thread.id)}>Archive</button>
              <button onClick={() => deleteThread(thread.id)}>Delete</button>
            </li>
          ))}
        </ul>
      );
    }

## BehaviorCopy Anchor Link

  * On mount, fetches the thread list and establishes a realtime WebSocket subscription.
  * If the runtime does not advertise thread endpoints, no `/threads` request is made and `error` explains that thread endpoints are unavailable.
  * Thread creates, renames, archives, and deletes from any client are reflected immediately without polling.
  * Mutations update the list at once (optimistic). If the server rejects a delete, the thread comes back and `error` is set. Rename, archive, and unarchive do not roll back. The promises resolve on server confirmation and reject on failure.
  * The `error` state updates with the most recent error from any operation.
  * The `threads` array is sorted by the most recent run (`lastRunAt`), then by `updatedAt` for threads that have not run.
  * New threads are **automatically named** when their first run creates them. By default, the name is the first user message. To get a short summary title from a model, set `generateThreadNames: { model }` on the runtime.



How is this guide?

GoodBad

[Previous PageuseSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[Next PageOverview](https://docs.copilotkit.ai/reference/v1)
