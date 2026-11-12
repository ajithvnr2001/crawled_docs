---
url: https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/copilot-threads-drawer/
title: Threads Drawer
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:46.070207+00:00
---

# Threads Drawer

> Source: https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/copilot-threads-drawer/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Threads

[Threads Drawer](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/copilot-threads-drawer)[Headless Threads](https://docs.copilotkit.ai/openai-agents-python/headless-threads)

[Frontend-tools](https://docs.copilotkit.ai/openai-agents-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/openai-agents-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/openai-agents-python/learning)

[User Memories](https://docs.copilotkit.ai/openai-agents-python/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/openai-agents-python/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/openai-agents-python/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/openai-agents-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/openai-agents-python/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/openai-agents-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/openai-agents-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Threads Drawer

BasicsThreads

# Threads Drawer

Drop-in threads drawer that lists, switches, and manages conversations next to your chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

`<CopilotThreadsDrawer>` gives your app a ready-made conversation sidebar. Users can list, switch, start, archive, and delete their threads, and you wire up **no active-thread state** to make it work. Drop it next to your chat and it connects automatically.

If your project was created from a CopilotKit CLI starter, the Drawer and its shared chat configuration are already included. Otherwise, use the setup below to add it to an existing CopilotKit application. This guide also covers Drawer customization and component options.

![A support desk application with a Threads Drawer listing customer conversations beside CopilotChat case details for Northstar Analytics](https://docs.copilotkit.ai/images/threads/support-desk-threads.png)

Under the hood it's a thin React wrapper around the self-contained `copilotkit-threads-drawer` web component, fed by [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads) and your chat configuration.

Prefer to build your own thread UI? The same data and actions are available headlessly through the `useThreads` hook (see [Headless Threads](https://docs.copilotkit.ai/openai-agents-python/headless-threads)). Thread **rename** is one of those headless actions: the prebuilt drawer's row menu covers archive/unarchive and delete, so wire up rename with `useThreads` and your own UI if you need it.

## When should I use this?#

Use the drawer when you want:

  * A persistent thread switcher beside your chat (chat-history sidebar)
  * Thread switching, new conversations, archive, and delete with zero wiring
  * A self-contained, themeable UI that follows your app's light/dark theme
  * A mobile-ready off-canvas drawer with its own launcher



It requires CopilotKit Intelligence (threads are stored and synced server-side). [Start cloud-hosted setup](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_drawer&utm_frontend=react&utm_backend=openai-agents-python) to create or select a project.

For multi-user applications, configure the Runtime to [scope AG-UI Streams to the signed-in user](https://docs.copilotkit.ai/openai-agents-python/threads-lifecycle#scope-rich-threads-to-the-signed-in-user).

[Threads run in CopilotKit IntelligenceConnect a cloud-hosted project to get persistent threads and realtime sync.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_drawer&utm_frontend=react&utm_backend=openai-agents-python)

## Set up the Threads Drawer#

Place `<CopilotThreadsDrawer>` next to `<CopilotChat>` and wrap **both** in a shared `<CopilotChatConfigurationProvider>`. If you are using a CLI-created starter, this structure is already in place. That shared configuration is what lets the Drawer drive the chat: with no callbacks, selecting a row connects the chat to that thread and replays its history; the "New Conversation" row resets the chat to a fresh welcome screen. The following example shows the essential structure to add to an existing app or preserve while customizing a starter.

**The Drawer ships only in`@copilotkit/react-core/v2`.** There is no v1 Drawer, so take the Drawer, the chat and the provider from that one package. Watch the import path: `@copilotkit/react-ui` is the [deprecated v1 package](https://docs.copilotkit.ai/openai-agents-python/migrate/v2) and it exports its own `CopilotChat` and `CopilotSidebar` under those same names.

app/page.tsx
    
    
    import {
      CopilotKitProvider,
      CopilotChatConfigurationProvider,
      CopilotChat,
      CopilotThreadsDrawer,
    } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    export default function Page() {
      return (
        <CopilotKitProvider runtimeUrl="/api/copilotkit">
          <CopilotChatConfigurationProvider>
            <div style={{ display: "flex", height: "100dvh" }}>
              <CopilotThreadsDrawer />
              <CopilotChat />
            </div>
          </CopilotChatConfigurationProvider>
        </CopilotKitProvider>
      );
    }

That's the whole integration. A hand-rolled sidebar would have you track the active `threadId` in your own state and pass selection/new-thread handlers between the list and the chat; here the drawer and the `CopilotChatConfigurationProvider` share that state, so there is none of that wiring to write.

## Use the Drawer with a sidebar chat#

`<CopilotChat>` is not the only host. `<CopilotSidebar>` works the same way, because it renders a `<CopilotChat>` inside itself and therefore shares the same chat configuration. Keep the Drawer as a sibling of your content and put the sidebar alongside it:

app/page.tsx
    
    
    import {
      CopilotKitProvider,
      CopilotChatConfigurationProvider,
      CopilotSidebar,
      CopilotThreadsDrawer,
    } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    export default function Page() {
      return (
        <CopilotKitProvider runtimeUrl="/api/copilotkit">
          <CopilotChatConfigurationProvider>
            <div style={{ display: "flex", height: "100dvh" }}>
              <CopilotThreadsDrawer />
              <main style={{ flex: 1 }}>
                <YourMainContent />
                <CopilotSidebar defaultOpen={true} />
              </main>
            </div>
          </CopilotChatConfigurationProvider>
        </CopilotKitProvider>
      );
    }

`<CopilotPopup>` hosts the Drawer on the same terms, for the same reason.

The launcher button that opens the Drawer from the chat header appears on mobile viewports only. On desktop the Drawer is a persistent in-flow panel that is always visible, so a launcher there would do nothing. A missing desktop launcher is the design, not a broken wiring.

## Add your own "New conversation" button#

The Drawer has its own "New Conversation" row. Your app can also keep its own button, for example in a toolbar or a page header. To start a new conversation from that button, call `startNewThread()` from [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration). This is the same function the Drawer calls for its own row.

app/page.tsx
    
    
    import {
      CopilotKitProvider,
      CopilotChatConfigurationProvider,
      CopilotChat,
      CopilotThreadsDrawer,
      useCopilotChatConfiguration,
    } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function NewConversationButton() {
      const configuration = useCopilotChatConfiguration(); 
    
      return (
        <button
          type="button"
          onClick={() => configuration?.startNewThread()} 
        >
          New conversation
        </button>
      );
    }
    
    export default function Page() {
      return (
        <CopilotKitProvider runtimeUrl="/api/copilotkit">
          <CopilotChatConfigurationProvider>
            <div style={{ display: "flex", height: "100dvh" }}>
              <CopilotThreadsDrawer />
              <main style={{ flex: 1, display: "flex", flexDirection: "column" }}>
                <header>
                  <NewConversationButton />
                </header>
                <CopilotChat />
              </main>
            </div>
          </CopilotChatConfigurationProvider>
        </CopilotKitProvider>
      );
    }

How it works:

  * Put the button inside the same `<CopilotChatConfigurationProvider>` as the Drawer and the chat. Outside a provider, `useCopilotChatConfiguration()` returns `null` and the button does nothing.

  * `startNewThread()` gives the chat a new thread id and shows the welcome screen. The Drawer reads the active thread from the same configuration, so no row stays selected.

  * The new thread appears in the Drawer list after its first run. An empty thread does not get a row.

  * If you set the `threadId` prop on `<CopilotChatConfigurationProvider>`, your app controls the thread. Then `startNewThread()` and the Drawer's own row selection do nothing and log a warning. Keep the thread id in your own state, and pass the Drawer two callbacks that update that state: `onThreadSelect` for a selected row, and `onNewThread` for its "New Conversation" row. Your button runs the same code as `onNewThread`:
        
        function ControlledChat() {
          const [threadId, setThreadId] = useState(() => crypto.randomUUID());
          const startNew = () => setThreadId(crypto.randomUUID());
        
          return (
            <CopilotChatConfigurationProvider threadId={threadId}>
              <CopilotThreadsDrawer
                onThreadSelect={(id) => setThreadId(id)}
                onNewThread={startNew}
              />
              <button type="button" onClick={startNew}>
                New conversation
              </button>
              <CopilotChat />
            </CopilotChatConfigurationProvider>
          );
        }




To show only your button, hide the Drawer's own new-conversation controls with their CSS parts. `new-thread-button` is the row in the open Drawer. `launcher-new-thread` is the (+) button in the closed or collapsed launcher.
    
    
    copilotkit-threads-drawer::part(new-thread-button),
    copilotkit-threads-drawer::part(launcher-new-thread) {
      display: none;
    }

## Which agent's threads the drawer shows#

The drawer lists the threads of **one** agent. It takes the first agent ID it finds, in this order:

  1. The drawer's own `agentId` prop.
  2. The `agentId` of the nearest `<CopilotChatConfigurationProvider>`. `<CopilotKit>` renders one of these around your app with its `agent` prop, so under `<CopilotKit agent="...">` the drawer stops here. Without `agent`, it resolves to `"default"`.
  3. The `agentId` on `<CopilotKitProvider>`.
  4. `"default"`.



Most framework quickstarts use `<CopilotKit agent="...">`. The built-in agent and LangGraph quickstarts use `<CopilotKitProvider agentId="...">`. The drawer finds the agent under either one.

If your runtime registers several agents, the drawer shows only the threads of the agent it resolved. To list another agent's threads, pass that agent's ID:
    
    
    <CopilotThreadsDrawer agentId="research_agent" />

`<CopilotChat>` resolves its agent in the same order. To move the drawer and the chat to another agent together, set `agentId` once on the shared `<CopilotChatConfigurationProvider>` instead.

## Configuring the drawer#

`<CopilotThreadsDrawer>` works with zero props. The optional ones:

Prop| Description  
---|---  
`agentId`| Agent whose threads to list. Defaults to the chat configuration's agent, then `agentId` on `<CopilotKitProvider>`, then `"default"`. See Which agent's threads the drawer shows.  
`label`| Accessible name for the drawer region and thread listbox. Defaults to `"Threads"`. The redesigned header has no visible title.  
`recentLabel`| Section heading shown above the thread list. Defaults to `"Recent Conversations"`.  
`onThreadSelect`| Escape hatch to take over thread selection yourself.  
`onNewThread`| Escape hatch to handle the "New Conversation" row yourself.  
`renderRow`| Render custom content per row (keeps the row chrome around it).  
`limit`| Page size for pagination. Shows a "Load more" control while more threads remain. Omit to load all at once.  
  
See the [Threads Drawer reference](https://docs.copilotkit.ai/reference/components/CopilotThreadsDrawer) for the full prop and type list.

## Customization#

The drawer renders in a shadow root with self-contained, theme-inheriting styles, so it looks correct in any app (including dark mode) with no config. Three bounded escape hatches pierce the boundary:

  * **Slots** : project children with a `slot` attribute (`header`, `empty`, `footer`, `memories`, `launcher-icon`):
        
        <CopilotThreadsDrawer>
          <span slot="header">My conversations</span>
        </CopilotThreadsDrawer>

  * **Per-row content** : the `renderRow` prop projects custom content into each row while the element keeps selection, archived styling, and the per-row kebab menu (Archive/Delete).

  * **CSS parts + variable tokens** : restyle structural `::part()`s or override `--cpk-drawer-*` tokens. The full list is in the [reference](https://docs.copilotkit.ai/reference/components/CopilotThreadsDrawer#customization).




## Intelligence access#

Threads require CopilotKit Intelligence. The drawer resolves its entitlement through the Runtime, so the credential is server-side configuration rather than a prop on the provider. Which credential you set depends on how you deploy.

**Cloud-hosted Intelligence.** The project-scoped `CPK_INTELLIGENCE_API_KEY` is the credential, and the Runtime resolves the drawer's entitlement from your organization's subscription. Cloud-hosted setup does not issue `COPILOTKIT_LICENSE_TOKEN`. That token is only for offline or self-hosted licensing and does not replace the cloud-hosted project API key. If the CLI created your project, the key is already in `.env` and the drawer needs nothing further.

**Self-hosted and open source.** Give the Runtime a license token, either as the `licenseToken` option or as the `COPILOTKIT_LICENSE_TOKEN` environment variable. The option wins when you set both. Without a token the drawer shows a locked view with an Upgrade link in place of the list, and it issues no thread requests.

The locked view appears whenever the Runtime reports no active entitlement: a self-hosted deployment whose license token is missing or expired, or a cloud-hosted project whose subscription is inactive.

## Related#

  * [AG-UI Streams overview](https://docs.copilotkit.ai/openai-agents-python/AG-UI-Streams): compare thread UI and deployment paths
  * [Headless Threads](https://docs.copilotkit.ai/openai-agents-python/headless-threads): build a custom UI with the `useThreads` data layer
  * [Threads Drawer reference (React)](https://docs.copilotkit.ai/reference/components/CopilotThreadsDrawer)
  * [CopilotChat](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/chat): the chat the drawer connects to



### On this page

What is this?When should I use this?Set up the Threads DrawerUse the Drawer with a sidebar chatAdd your own "New conversation" buttonWhich agent's threads the drawer showsConfiguring the drawerCustomizationIntelligence accessRelated
