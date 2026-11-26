---
url: https://docs.copilotkit.ai/prebuilt-components/chat-controls/
title: Open, close, and feedback
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:35.760960+00:00
---

# Open, close, and feedback

> Source: https://docs.copilotkit.ai/prebuilt-components/chat-controls/

Chat/Prebuilt Components

# Open, close, and feedback

Open and close the prebuilt chat from your UI, and capture assistant message feedback.

Copy MarkdownOpen

This page covers two tasks for the prebuilt chat:

  * Open and close the chat from your own UI, for example from a button in your nav bar.
  * Capture thumbs-up and thumbs-down feedback on assistant replies.



## Control the open state from your own UICopy Anchor Link

Pass `open` and `onOpenChange` to `<CopilotSidebar>` or `<CopilotPopup>` to own the open state yourself. This is the controlled pattern. The surface shows whatever `open` says. The toggle button and click-outside on the popup send their request to `onOpenChange`, and the surface does not move by itself.

Copy Text
    
    
    import { useState } from "react";
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    
    function Layout() {
      const [chatOpen, setChatOpen] = useState(false);
    
      return (
        <>
          <nav>
            <button onClick={() => setChatOpen(true)}>Ask the assistant</button>
          </nav>
    
          <CopilotSidebar open={chatOpen} onOpenChange={setChatOpen} />
        </>
      );
    }

The button lives outside the sidebar, which is the point: nothing has to be rendered inside the chat subtree to open or close it. Because `open` is the source of truth, you can also keep the chat in sync with a route, a keyboard shortcut, or any other state you already have.

`onOpenChange` reports a request, not a change. If you do not feed the new value back into `open`, the surface stays where it is. That is what makes it possible to gate opening the chat, for example behind a sign-in check. You can also pass `onOpenChange` on its own, without `open`: the surface keeps managing itself and you are notified each time it opens or closes.

## Programmatically open or close the chatCopy Anchor Link

If you would rather not lift the state into your own component, the open state for `<CopilotPopup>` and `<CopilotSidebar>` also lives in the **chat configuration context**. Read it with `useCopilotChatConfiguration()` and call `setModalOpen(true | false)` from anywhere inside the provider:

Copy Text
    
    
    import { useCopilotChatConfiguration } from "@copilotkit/react-core/v2";
    
    function OpenChatButton() {
      const config = useCopilotChatConfiguration();
    
      // setModalOpen is only present when a provider in the tree owns modal state
      // (the prebuilt CopilotPopup / CopilotSidebar create it for you).
      if (!config?.setModalOpen) return null;
    
      return (
        <button onClick={() => config.setModalOpen(true)}>
          Ask the assistant
        </button>
      );
    }

To toggle, read `config.isModalOpen` and flip it:

Copy Text
    
    
    <button onClick={() => config.setModalOpen(!config.isModalOpen)}>
      {config.isModalOpen ? "Close chat" : "Open chat"}
    </button>

`setModalOpen` / `isModalOpen` are only defined when a provider in the tree owns modal state. The prebuilt `<CopilotPopup>` and `<CopilotSidebar>` create this state inside the chat only. To open the chat from a button outside it, use `open` and `onOpenChange`, or wrap the button and the chat in one `<CopilotChatConfigurationProvider isModalDefaultOpen={false}>`. If you compose chat yourself, wrap the relevant subtree in the same provider so the modal state exists. See the [`useCopilotChatConfiguration` reference](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration#modal-state-management).

You can also set the **initial** open state declaratively, and then let the surface manage itself. The prebuilt surfaces accept a `defaultOpen` prop:

Copy Text
    
    
    <CopilotSidebar defaultOpen={false} />

`defaultOpen` and `open` are the usual uncontrolled/controlled pair: use `defaultOpen` for a starting point, and `open` when your own state decides. When both are passed, `open` wins.

## Capture message feedback (thumbs up / down)Copy Anchor Link

The assistant-message toolbar can show thumbs-up and thumbs-down buttons. To show the buttons, pass `onThumbsUp` and `onThumbsDown` to the **assistant message slot**. Without Automatic Learning capture, the buttons only render when a handler or a custom thumb slot is provided:

Copy Text
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          onThumbsUp: (message) => {
            analytics.track("feedback", { messageId: message.id, value: "up" });
          },
          onThumbsDown: (message) => {
            analytics.track("feedback", { messageId: message.id, value: "down" });
          },
        },
      }}
    />;

Each handler receives the assistant `message`, so you can record the feedback against the specific response (`message.id`). The same `messageView` slot works on `<CopilotPopup>` and `<CopilotSidebar>` since they wrap `<CopilotChat>`.

For raw AG-UI event data on the message, see [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage).

The button labels come from the chat labels (`assistantMessageToolbarThumbsUpLabel` defaults to `"Good response"`, `assistantMessageToolbarThumbsDownLabel` to `"Bad response"`); override them via [chat labels](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration#copilotchatlabels).

The buttons appear without handlers when all of these are true:

  * [Automatic Learning capture](https://docs.copilotkit.ai/intelligence/capture-interactions#collect-reply-ratings) is on.
  * A Trajectory is started.
  * The chat renders messages with `CopilotChatMessageView` inside a `CopilotChatConfigurationProvider`. `CopilotChat`, `CopilotPopup`, and `CopilotSidebar` do.



A rating then also goes to the active Trajectory, the user can add a comment, and clicking the chosen thumb again removes the rating. Your handlers run when a rating is given, not when it is removed.

Building a fully custom message component instead of using the slot? The underlying [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage) exposes the same `onThumbsUp` / `onThumbsDown` props directly, but callback metadata enrichment is owned by `CopilotChatMessageView`.

How is this guide?

GoodBad

[Previous PageCopilotPopup](https://docs.copilotkit.ai/prebuilt-components/popup)[Next PageCSS Customization](https://docs.copilotkit.ai/custom-look-and-feel/css)
