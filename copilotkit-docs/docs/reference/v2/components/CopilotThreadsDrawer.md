---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer/
title: CopilotThreadsDrawer
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:21.621078+00:00
---

# CopilotThreadsDrawer

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer/

React/Components

# CopilotThreadsDrawer

Prebuilt threads drawer that lists, switches, and manages threads next to CopilotChat

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotThreadsDrawer` is a prebuilt thread switcher. Put it and [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) inside one `CopilotChatConfigurationProvider`. It lists the threads of the user and lets them switch, start, archive, and delete threads with **no active-thread state to wire up**. (Thread rename is available headlessly via [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads), not through the drawer's row menu.) It is a thin React wrapper around the framework-agnostic `<copilotkit-threads-drawer>` shadow-DOM web component, fed by the [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads) hook and the surrounding chat configuration.

When `onThreadSelect` / `onNewThread` are omitted, the drawer drives the surrounding chat configuration directly: selecting a row connects the chat to that thread (and replays its history); the "New Conversation" row resets the chat to a fresh welcome screen. Pass the callbacks only to take control of the active thread yourself.

Pair it with the v2 `CopilotChat` or `CopilotSidebar` from `@copilotkit/react-core/v2`. `@copilotkit/react-ui` exports components with those same two names, and those are the [deprecated v1 components](https://docs.copilotkit.ai/migrate/v2).

See the [CopilotThreadsDrawer guide](https://docs.copilotkit.ai/prebuilt-components/copilot-threads-drawer) for a walkthrough, and [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads) for the headless data layer underneath.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotThreadsDrawer } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## PropsCopy Anchor Link

Prop

Type

`agentId?`string

`onThreadSelect?`(threadId: string) => void

`onNewThread?`() => void

`renderRow?`(thread: Thread) => React.ReactNode

`label?`string

`recentLabel?`string

`limit?`number

`collapsible?`boolean

`onCollapseChange?`(collapsed: boolean) => void

`data-testid?`string

## CustomizationCopy Anchor Link

The drawer renders inside a shadow root and ships its own self-contained, theme-inheriting styles, so it looks correct in any host (including dark mode) with zero config. Three bounded escape hatches pierce the boundary.

### SlotsCopy Anchor Link

Project light-DOM children with a `slot` attribute to replace a region:

Slot| Replaces  
---|---  
`header`| The drawer header region (renders only when you project content).  
`empty`| The empty-state body shown when there are no threads.  
`footer`| A footer region (hidden until you project content).  
`memories`| An extra region above the footer, hidden until you project content.  
`launcher-icon`| The icon inside the floating mobile launcher.  
`row:{id}`| Per-row content. Prefer the `renderRow` prop, which manages this.  
  
Copy Text
    
    
    <CopilotThreadsDrawer>
      <span slot="header">My conversations</span>
    </CopilotThreadsDrawer>

### CSS partsCopy Anchor Link

Style structural elements with `::part()`:

  * **Structure** : `root`, `header`, `list`, `footer`
  * **Rows** : `row`, `row-active` (the selected row), `row-name`, `row-menu` (kebab), `row-menu-popover`, `row-archive`, `row-unarchive`, `row-delete`
  * **New conversation & sections**: `new-thread-button`, `section-heading`
  * **Filter** : `filter-toggle`, `filter-indicator`, `filter-active`, `filter-all`, `filters`
  * **Collapse, mobile & launcher**: `collapse-toggle` (desktop), `close-toggle` (mobile), `backdrop` (mobile scrim), `launcher`, `launcher-cluster`, `launcher-new-thread`
  * **Pagination** : `load-more`, `fetching-more`, `fetch-more-error`, `fetch-more-retry`
  * **States & upsell**: `loading`, `empty`, `error`, `retry-button`, `licensed`, `licensed-cta`, `memories`
  * **Delete confirm dialog** : `confirm-dialog`, `confirm-cancel`, `confirm-delete`



The Active/All filter lives behind the `filter-toggle` funnel, whose `filter-indicator` dot shows when a non-default filter is applied. Per-row Archive/Delete actions live in the `row-menu` kebab and its `row-menu-popover`. When the list is collapsed on desktop (or closed on mobile), the floating `launcher-cluster` holds the `launcher` toggle and the `launcher-new-thread` button.

### CSS variable tokensCopy Anchor Link

Tokens override the bundled defaults. Color tokens fall back to the host theme variable in the Fallback column, so the drawer follows light and dark themes automatically.

Group| Token| Fallback| Sets  
---|---|---|---  
Colors| `--cpk-drawer-bg`| `--background`| Background of the drawer panel.  
Colors| `--cpk-drawer-fg`| `--foreground`| Text color of the drawer.  
Colors| `--cpk-drawer-border`| `--border`| Borders of the panel, the launcher cluster, and menus.  
Colors| `--cpk-drawer-surface`| `--card`| Background of the launcher cluster and the menus.  
Colors| `--cpk-drawer-surface-fg`| `--card-foreground`| Text on the launcher cluster and the menus.  
Colors| `--cpk-drawer-muted`| `--muted`| Hover and pressed background of the icon buttons.  
Colors| `--cpk-drawer-muted-fg`| `--muted-foreground`| Section headings, archived rows, and icon buttons.  
Colors| `--cpk-drawer-accent`| `--accent`| Background of the active row.  
Colors| `--cpk-drawer-accent-fg`| `--accent-foreground`| Text of the active row.  
Colors| `--cpk-drawer-primary`| `--primary`| Background of primary buttons.  
Colors| `--cpk-drawer-primary-fg`| `--primary-foreground`| Text of primary buttons.  
Colors| `--cpk-drawer-danger`| `--destructive`| The delete action and error text.  
Colors| `--cpk-drawer-indicator`| `#5b94e4`| The dot that shows a filter is applied.  
Colors| `--cpk-drawer-ring`| `--ring`| Focus ring color. The current styles do not read it.  
Shape| `--cpk-drawer-radius`| `--radius`| Corner radius, capped at `4px`.  
Shape| `--cpk-drawer-width`| `320px`| Width of the drawer.  
Type| `--cpk-drawer-font-family`| `ui-sans-serif`| Font family.  
Type| `--cpk-drawer-font-size`| `14px`| Font size.  
Type| `--cpk-drawer-line-height`| `1.4`| Line height.  
Launcher position| `--cpk-drawer-launcher-top`| `24px`| Distance of the launcher cluster from the top.  
Launcher position| `--cpk-drawer-launcher-left`| `24px`| Distance of the launcher cluster from the left.  
  
## UsageCopy Anchor Link

### Basic usageCopy Anchor Link

Wrap the drawer and `CopilotChat` in a shared `CopilotChatConfigurationProvider` so they operate on the **same** chat configuration. That shared config is how selecting a thread (or "New Conversation") drives the chat. Without a shared provider the drawer sits beside the chat's own scoped configuration and can't switch its thread.

Copy Text
    
    
    import {
      CopilotThreadsDrawer,
      CopilotChat,
      CopilotChatConfigurationProvider,
    } from "@copilotkit/react-core/v2";
    
    function App() {
      return (
        <CopilotChatConfigurationProvider>
          <div style={{ display: "flex", height: "100%" }}>
            <CopilotThreadsDrawer />
            <CopilotChat />
          </div>
        </CopilotChatConfigurationProvider>
      );
    }

### Custom row content + labelCopy Anchor Link

Copy Text
    
    
    function App() {
      return (
        <CopilotThreadsDrawer
          label="History"
          renderRow={(thread) => <em>{thread.name ?? "New conversation"}</em>}
        />
      );
    }

## BehaviorCopy Anchor Link

  * **Self-connecting** : without `onThreadSelect`/`onNewThread`, the drawer drives the chat configuration. Select connects + replays; the "New Conversation" row shows the welcome screen.
  * **Collapsible sidebar** : on larger screens the drawer is an expanded sidebar by default with a collapse toggle (sidebar glyph) in the header. Collapsing replaces the panel with a small floating cluster: a sidebar toggle to expand plus a "New Conversation" button. Collapsing also lets a host grid reclaim the column (via `--cpk-drawer-reserved-width`). Set `collapsible={false}` to omit the toggle. "New Conversation" is its own row below the header; project `slot="header"` content to add your own chrome beside the toggle.
  * **Row actions** : per-row **Archive/Delete** live behind a per-row kebab (⋮) menu (`row-menu`); delete asks for confirmation.
  * **Optimistic mutations** : archive/unarchive/rename/delete are optimistic in the core thread store; delete rolls back if the server rejects.
  * **Deleting the active thread** resets to a fresh thread; **archiving** the active thread keeps you viewing it. Archived threads render italic/muted inline in the "All" view.
  * **Filter** : an Active/All filter lives behind a **funnel** icon popover under the "Recent Conversations" heading; a small indicator dot appears on the funnel when a non-default filter is applied. Toggling the filter refetches server-side.
  * **Mobile** : below 768px the drawer is an off-canvas modal. Closed, it shows the same floating cluster (a launcher to open it + a "New Conversation" button); open, it slides in and is dismissed by tapping the backdrop or pressing Escape. The launcher icon (`launcher-icon` slot) and position (`--cpk-drawer-launcher-*`) are customizable.
  * **Intelligence access** : threads require CopilotKit Intelligence. If the runtime reports that Threads are unavailable, the drawer shows a locked view in place of the list. Cloud-hosted projects use `CPK_INTELLIGENCE_API_KEY` on the server. A licensed self-hosted deployment uses `COPILOTKIT_LICENSE_TOKEN` on the server.



How is this guide?

GoodBad

[Previous PageCopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[Next PageuseAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)
