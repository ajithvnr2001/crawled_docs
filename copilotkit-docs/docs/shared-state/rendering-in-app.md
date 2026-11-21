---
url: https://docs.copilotkit.ai/shared-state/rendering-in-app/
title: Render agent state in your app
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:43.977197+00:00
---

# Render agent state in your app

> Source: https://docs.copilotkit.ai/shared-state/rendering-in-app/

Shared state

# Render agent state in your app

Read agent.state with useAgent and render it in your main view or canvas.

Copy MarkdownOpen

[Shared state](https://docs.copilotkit.ai/shared-state) is most useful when the agent's state shows up in your main view, such as a dashboard, document canvas, map, or table. Because `agent.state` is plain React data, you can subscribe to it from any component in your tree and render it however you like.

## The patternCopy Anchor Link

[`useAgent`](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) works in any component under `<CopilotKit>`. It doesn't have to be near the chat. Call it in your main-view component, read `agent.state`, and render:

components/Canvas.tsx

Copy Text
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    
    type CanvasState = {
      title: string;
      items: { id: string; label: string; done: boolean }[];
    };
    
    const INITIAL_CANVAS_STATE: CanvasState = {
      title: "Project launch",
      items: [
        { id: "research", label: "Research user needs", done: true },
        { id: "prototype", label: "Build a prototype", done: false },
      ],
    };
    
    export function Canvas() {
      // No agentId means the "default" agent. Pass { agentId } to target another.
      const { agent, isReady } = useAgent();
      const state = (agent.state ?? {}) as Partial<CanvasState>;
    
      useEffect(() => {
        if (!isReady) return;
    
        const current = (agent.state ?? {}) as Partial<CanvasState>;
        const updates: Partial<CanvasState> = {};
    
        if (current.title === undefined) {
          updates.title = INITIAL_CANVAS_STATE.title;
        }
        if (current.items === undefined) {
          updates.items = INITIAL_CANVAS_STATE.items;
        }
    
        if (Object.keys(updates).length > 0) {
          agent.setState({ ...(agent.state ?? {}), ...updates });
        }
      }, [agent, isReady, state.title, state.items]);
    
      return (
        <main className="canvas">
          <h1>{state.title ?? "Untitled"}</h1>
          <ul>
            {(state.items ?? []).map((item) => (
              <li key={item.id} data-done={item.done}>
                {item.label}
              </li>
            ))}
          </ul>
        </main>
      );
    }

The `INITIAL_CANVAS_STATE` value is UI-owned initial state for this example. It makes the canvas visible before the agent writes state. The effect sets only `undefined` fields and preserves all other state. If the backend owns the initial state, define it in the shared-state setup for that framework.

Every time the agent mutates its state, whether from a tool call, node transition, or [streamed update](https://docs.copilotkit.ai/shared-state/streaming), `useAgent` re-renders this component with the new values. The chat can be in a sidebar, a popup, or absent entirely; your canvas updates the same way.

## Put it anywhere in your layoutCopy Anchor Link

The agent lives on the `<CopilotKit>` provider, so the chat surface and your main-view components are just two consumers of the same agent. A typical layout renders the canvas as the main view and the chat as a docked sidebar:

app/page.tsx

Copy Text
    
    
    import { CopilotKit, CopilotSidebar } from "@copilotkit/react-core/v2";
    import { Canvas } from "../components/Canvas";
    
    export default function Page() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit">
          <div className="app-shell">
            {/* Your app UI, driven by agent.state */}
            <Canvas />
            {/* Chat is just another consumer of the same agent */}
            <CopilotSidebar />
          </div>
        </CopilotKit>
      );
    }

`<Canvas>` and `<CopilotSidebar>` both call `useAgent()` for the same `agentId`, so they share one agent instance and one state object. There's nothing chat-specific about reading `agent.state`. The sidebar is not special.

## Writing back from the main viewCopy Anchor Link

The same `agent` exposes `setState`, so your canvas can be interactive, not just a read-only mirror. A click handler in the main view can push a new value that the agent reads on its next turn:

Copy Text
    
    
    function toggleItem(id: string) {
      agent.setState({
        ...agent.state,
        items: (agent.state?.items ?? []).map((it) =>
          it.id === id ? { ...it, done: !it.done } : it,
        ),
      });
    }

This is the same two-way channel described in [Shared State](https://docs.copilotkit.ai/shared-state). The only difference here is that the reads and writes happen in your main view.

If the agent must only read a UI value, and never write it, use [agent read-only context](https://docs.copilotkit.ai/shared-state/agent-readonly).

## TipsCopy Anchor Link

  * **Target a specific agent** with `useAgent({ agentId: "research-agent" })` when you have more than one. The default is the agent named `"default"`.
  * **Throttle high-frequency updates** with `useAgent({ throttleMs })` if a streaming run re-renders a heavy canvas too often.
  * **Treat`agent.state` as possibly partial** while a run is in progress. Guard with defaults (as above) so half-streamed state doesn't crash your render.



## Try itCopy Anchor Link

Ask the agent to add a task called "Write the launch post". A new item appears in the canvas list. Then mark an item done with `toggleItem`, and ask the agent which tasks are done. The agent names the item that you marked.

How is this guide?

GoodBad

[Previous PageShared State](https://docs.copilotkit.ai/shared-state)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/shared-state/agent-readonly)
