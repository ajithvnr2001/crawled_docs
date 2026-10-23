---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/chat-panel/
title: Build a Chat Panel \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-13T08:46:37.385748+00:00
---

# Build a Chat Panel · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/chat-panel/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)
  5. /Build a Chat Panel



# Build a Chat Panel

Last updated Oct 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRender the full chat panelBuild a custom chat layout

Prerequisite

This guide builds on top of the [Build Your Own UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/). It is recommended to read that guide first. Portions of the code will not be repeated here for brevity.

The chat components on this page require RealtimeKit Web UI Kit 1.1.0 or later and work best with RealtimeKit Web Core 1.2.4 or later.

The UI Kit includes a full chat panel and lower-level chat components. The chat components load messages in pages, instead of loading the entire chat history when they join. This keeps chat responsive in meetings with many participants or long chat history.

Use the full panel when you want RealtimeKit to manage chat behavior for you.

Use lower-level components when you need to control the layout around message lists, pinned messages, or the composer.

This page is not available for the **Mobile** platform.

WebMobile

ReactWeb ComponentsAngular

## Render the full chat panel

Use `rtk-chat` to render the full chat panel. It includes public chat, private chat, paginated messages, pinned messages, file uploads, image uploads, edit actions, delete actions, and emoji input.
    
    
    <rtk-ui-provider id="rtk-ui-provider">
    	<rtk-chat style="height: 480px;"></rtk-chat>
    </rtk-ui-provider>

To set chat UI overrides, assign the `overrides` property on `rtk-ui-provider` or `rtk-meeting`.
    
    
    const provider = document.querySelector("rtk-ui-provider");
    
    provider.overrides = {
    	disableEmojiPicker: true,
    	disablePrivateChat: true,
    };

The `disableEmojiPicker` override hides the emoji picker button. The `disablePrivateChat` override hides private chat even when the preset allows it.

To control private chat for all participants, prefer preset permissions.

Use `RtkChat` to render the full chat panel. It includes public chat, private chat, paginated messages, pinned messages, file uploads, image uploads, edit actions, delete actions, and emoji input.
    
    
    import { RtkChat, RtkUiProvider } from "@cloudflare/realtimekit-react-ui";
    
    function ChatPanel({ meeting }) {
    	return (
    		<RtkUiProvider
    			meeting={meeting}
    			overrides={{
    				disableEmojiPicker: true,
    				disablePrivateChat: true,
    			}}
    		>
    			<RtkChat style={{ height: "480px" }} />
    		</RtkUiProvider>
    	);
    }

The `disableEmojiPicker` override hides the emoji picker button. The `disablePrivateChat` override hides private chat even when the preset allows it.

To control private chat for all participants, prefer preset permissions.

Use `rtk-chat` to render the full chat panel. It includes public chat, private chat, paginated messages, pinned messages, file uploads, image uploads, edit actions, delete actions, and emoji input.
    
    
    <rtk-ui-provider [meeting]="meeting" [overrides]="chatOverrides">
    	<rtk-chat style="height: 480px;"></rtk-chat>
    </rtk-ui-provider>
    
    
    chatOverrides = {
    	disableEmojiPicker: true,
    	disablePrivateChat: true,
    };

The `disableEmojiPicker` override hides the emoji picker button. The `disablePrivateChat` override hides private chat even when the preset allows it.

To control private chat for all participants, prefer preset permissions.

## Build a custom chat layout

You can create your own chat layout from the same UI Kit components that `RtkChat` uses. Place each component wherever your design needs it, such as the message list in a sidebar and the composer in a footer, and connect them through your own state.

Component | What it renders  
---|---  
`RtkChatSelector` | A dropdown to switch between public chat and private conversations. Emits `rtkChatSelectorChange` with the selected participant.  
`RtkPinnedMessageSelector` | A collapsible header that expands to show pinned messages.  
`RtkChatMessagesUiPaginated` | The message list. Loads public messages when `privateChatRecipient` is empty, and the private conversation when you pass a participant.  
`RtkChatComposerView` | The message input, with file, image, and emoji buttons.  
  
When you build your own layout, your code connects the components to `meeting.chat`:

  * `RtkChatMessagesUiPaginated` emits `pinMessage`, `editMessage`, and `deleteMessage` events from its message menu but does not act on them. Handle these events and call the matching `meeting.chat` methods.
  * `RtkChatComposerView` emits `newMessage` and `editMessage` events. Send or edit the message with `meeting.chat`.
  * Pass `meeting.chat.maxTextLimit` and `meeting.chat.rateLimits` to `RtkChatComposerView` so the composer enforces the same limits as the meeting.



The following example stacks the components vertically. Rearrange them to fit your layout.
    
    
    import {
    	RtkChatComposerView,
    	RtkChatMessagesUiPaginated,
    	RtkChatSelector,
    	RtkPinnedMessageSelector,
    } from "@cloudflare/realtimekit-react-ui";
    import { useState } from "react";
    
    function CustomChat({ meeting }) {
    	const [privateChatRecipient, setPrivateChatRecipient] = useState(null);
    	const [editingMessage, setEditingMessage] = useState(null);
    	const { chatPublic, chatPrivate } = meeting.self.permissions;
    	const publicChat = {
    		canSendText: chatPublic.canSend && chatPublic.text,
    		canSendFiles: chatPublic.canSend && chatPublic.files,
    	};
    	const privateChat = {
    		canSendText: Boolean(chatPrivate?.canSend && chatPrivate?.text),
    		canSendFiles: Boolean(chatPrivate?.canSend && chatPrivate?.files),
    	};
    	const activeChat = privateChatRecipient ? privateChat : publicChat;
    
    	return (
    		<div style={{ height: "480px" }}>
    			<RtkChatSelector
    				meeting={meeting}
    				onRtkChatSelectorChange={(event) => {
    					setPrivateChatRecipient(event.detail.selectedUser ?? null);
    				}}
    			/>
    			<RtkPinnedMessageSelector meeting={meeting} />
    			<RtkChatMessagesUiPaginated
    				meeting={meeting}
    				privateChatRecipient={privateChatRecipient}
    				onPinMessage={(event) => {
    					const message = event.detail;
    					if (message.pinned) {
    						meeting.chat.unpin(message.id);
    					} else {
    						meeting.chat.pin(message.id);
    					}
    				}}
    				onEditMessage={(event) => {
    					if (event.detail.type === "text") {
    						setEditingMessage(event.detail);
    					}
    				}}
    				onDeleteMessage={(event) => {
    					if (editingMessage?.id === event.detail.id) {
    						setEditingMessage(null);
    					}
    					meeting.chat.deleteMessage(event.detail.id);
    				}}
    			/>
    			<RtkChatComposerView
    				canSendTextMessage={activeChat.canSendText}
    				canSendFiles={activeChat.canSendFiles}
    				maxLength={meeting.chat.maxTextLimit}
    				rateLimits={meeting.chat.rateLimits}
    				inputTextPlaceholder="Enter a message"
    				isEditing={!!editingMessage}
    				message={editingMessage ? editingMessage.message : ""}
    				storageKey={
    					editingMessage
    						? `custom-chat-edit-${editingMessage.id}`
    						: "custom-chat-draft"
    				}
    				onNewMessage={(event) =>
    					meeting.chat.sendMessage(
    						event.detail,
    						privateChatRecipient ? [privateChatRecipient.id] : [],
    					)
    				}
    				onEditMessage={async (event) => {
    					try {
    						await meeting.chat.editTextMessage(editingMessage.id, event.detail);
    					} finally {
    						setEditingMessage(null);
    					}
    				}}
    				onEditCancel={() => setEditingMessage(null)}
    			/>
    		</div>
    	);
    }

Refer to the [`RtkChat`](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/), [`RtkChatSelector`](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/), [`RtkPinnedMessageSelector`](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpinnedmessageselector/), [`RtkChatMessagesUiPaginated`](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/), and [`RtkChatComposerView`](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerview/) API references for component props.

[PreviousBuild Your Own UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/)[NextAdd Custom Header](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/custom-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/chat-panel.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
