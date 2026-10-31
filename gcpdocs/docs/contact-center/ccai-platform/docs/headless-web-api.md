---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-api/
title: Headless web SDK API methods \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T06:00:17.321142+00:00
---

# Headless web SDK API methods  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless web SDK API methods Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the API methods available for the headless web SDK.

## Company and menus

Methods for handling company values and menus.

## Methods

The headless SDK provides various methods that can be called on the client instance.

Here are some examples:

### Company and menus

Method name | Description  
---|---  
getCompany | Retrieves configured company information.  
getMenus | List all available menus for given tenant.  
getWaitTimes  | Get current wait times for various channels on a menu.  
  
### getCompany

Retrieves the configured company information for the authenticated instance, including the company name, supported languages, and feature settings. This method also sets the internal instance identifier (`OPTIONS.tenant`) as a side effect, which is why it is typically the first call made after constructing a Client.

#### Method signature
    
    
    getCompany(): Promise<CompanyResponse>
    

#### Return value

Returns a `CompanyResponse` object.

#### Interfaces
    
    
    interface CompanyResponse {
      name: string;
      subdomain: string;
      support_email: string;
      languages: LanguageOption[];
      action_tracking: boolean;
      email_transcripts: boolean;
      message_preview: boolean;
      email_enhancement: boolean;
      display_history: boolean;
      use_recording: boolean;
      use_web: boolean;
      cobrowse_domain?: string;
    }
    

#### Example usage
    
    
    try {
      const company = await client.getCompany()
    } catch (error) {
      // handle error
    }
    

### getMenus

This method is used to list all the menu items available for the instance. The `MenuResponse.direct` field tells callers whether the result came from a direct-access key (`direct.key: true`) or from user-level direct access (`direct.user: true`) - both affect how the menus should be presented.

#### Method signature
    
    
    getMenus(key?: string, lang?: string): Promise<MenuResponse>
    

#### Return value

Returns a `MenuResponse` object.

#### Interfaces
    
    
    interface MenuResponse {
      menus: MenuItem[];
      direct: {
        key: boolean;
        user: boolean;
        key_id: number | null;
      };
    }
    interface MenuItem {
      id: number;
      name?: string;
      enabled: boolean;
      redirection?: {
        option: string;
        data: string;
      };
      children?: MenuItem[];
      channels: MenuChannel[];
      deflection?: {
        enabled: boolean;
        type: string;
      };
      hidden: boolean;
    }
    

#### Example usage
    
    
    try {
      const data: MenuResponse = await client.getMenus("direct_menu_key")
      console.log(data.menus)
      console.log(data.direct)
    } catch (error) {
      // handle error
    }
    

### getWaitTimes

Retrieves the estimated waiting time (in seconds) for the chat and voice call channels of a given menu.

#### Method signature
    
    
    getWaitTimes(menuId: number | string, lang?: string): Promise<WaitTimeResponse | null>
    

#### Return value

Returns either a `WaitTimeResponse` object or `null`.

#### Interfaces
    
    
    interface WaitTimeResponse {
      chat: number;
      voice_call: number;
    }
    

#### Example usage
    
    
    try {
      const data = await client.getWaitTimes(123)
    } catch (error) {
      // handle error
    }
    

## Calls

Name | Description  
---|---  
`createCall` | Create an instant or scheduled call.  
`loadCall` | Get information from a given call id.  
`cancelCall` | Cancel the call with given call id.  
`getTimeSlots` | Get available time slots for scheduled calls for a given menu.  
`fetchTimeSlotAvailability` | Check whether time slots are available for a given menu.  
  
### createCall

Creates a new call for the given menu. This can be an instant call or a scheduled call, depending on whether the `scheduled_at` field is provided. The call type (`web_instant_call` versus `web_scheduled_call`) is determined automatically based on the presence of `scheduled_at`. `reschedule_call_id` is sent at the top level of the request, separate from the call body. The `menu_id` in the response is normalized from the API's `selected_menu.id`.

#### Method signature
    
    
    createCall(menuId: number | string, data: CallRequest): Promise<CallResponse>
    

#### Return value

Returns a `CallResponse` object.

#### Interfaces
    
    
    interface CallRequest {
      phone_number: string;
      lang?: string;
      scheduled_at?: string;
      ticket_id?: string;
      email?: string;
      recording_permission?: "recording_permission_not_asked" | "recording_permission_granted" | "recording_permission_denied";
      custom_data?: {
        signed?: string;
        unsigned?: Record<string, any>;
      };
      reschedule_call_id?: number;
    }
    

#### Example usage
    
    
    try {
     const call = await client.createCall(123, { phone_number: '+12345678' })
    } catch (error) {
     // handle error
    }
    

### loadCall

The `loadCall` method retrieves information about a specific call, identified by its ID.

#### Method signature
    
    
    loadCall(callId: number | string): Promise<CallResponse>
    

#### Return value

Returns a `CallResponse` object.

#### Interfaces
    
    
    interface CallResponse {
     id: number;
     lang: string;
     menu_id: number;
     status: string;
     type: string;
     scheduled_at?: string;
     recording_permitted: boolean;
     survey_enabled: boolean;
     created_at: string;
     menus: {
       id: number;
       name: string;
     }[];
    }
    

#### Example usage
    
    
    try {
     const call = await client.loadCall(1234)
    } catch (error) {
     // handle error
    }
    

### cancelCall

Cancels an existing call by its ID. Typically used to cancel a scheduled call that hasn't yet been placed.

#### Method signature
    
    
    cancelCall(callId: number | string): Promise<CallResponse>
    

#### Return value

Returns a CallResponse object.

#### Interfaces
    
    
    interface CallResponse {
     id: number;
     lang: string;
     menu_id: number;
     status: string;
     type: string;
     scheduled_at?: string;
     recording_permitted: boolean;
     survey_enabled: boolean;
     created_at: string;
     menus: {
       id: number;
       name: string;
     }[];
    }
    

#### Example usage
    
    
    try {
     const response = await client.cancelCall(1234)
    } catch (error) {
     // handle error
    }
    

### getTimeSlots

Retrieves available time slots for scheduled calls on a given menu. When called with a `GetTimeSlotsRequest` options object, supports rescheduling an existing call using `rescheduleCallId`. The deprecated `lang` string signature remains supported and routes to the same endpoint with only `lang` populated. Returns an array of time slot strings.

#### Method signature
    
    
    getTimeSlots(menuId: number | string, options?: GetTimeSlotsRequest): Promise<string[]>
    

**Warning:** The previous signature `getTimeSlots(menuId, lang?)` is deprecated. Migrate to the new options-based signature shown earlier. The old signature will continue to work but may be removed in a future release.

#### Return value

Returns an array of strings (time slots).

#### Interfaces
    
    
    interface GetTimeSlotsRequest {
     lang?: string;
     rescheduleCallId?: number;          // ID of an existing call being rescheduled
    }
    

#### Example usage
    
    
    // New options-based signature (recommended)
    try {
     const slots = await client.getTimeSlots(123, {
       lang: 'en',
       rescheduleCallId: 98765, // optional: pass when rescheduling an existing call
     })
    } catch (error) {
     // handle error
    }
    // Deprecated signature (still supported)
    try {
     const slots = await client.getTimeSlots(123, 'en')
    } catch (error) {
     // handle error
    }
    

### fetchTimeSlotAvailability

This method checks whether time slots are available for a given menu, without fetching the full list of time slots. It is useful for conditionally showing scheduling options in the UI.

#### Scope

`fetchTimeSlotAvailability` applies only to **scheduled voice call (callback) appointments**. It doesn't return information about chat, email, or instant-call channels. The supplied menu must be configured to support scheduled voice calls, with operation hours defined and at least one agent queued for that menu.

Typical use cases:

  * Conditionally rendering a _"Schedule a Callback"_ call-to-action only when slots are available.

  * Branching to a deflection flow (e.g., email, after-hours message) when no slots are available, without paying the cost of a full `getTimeSlots` call.

  * Pre-flighting a reschedule action before calling `getTimeSlots` with a `rescheduleCallId`.




#### Method signature
    
    
    fetchTimeSlotAvailability(menuId: number | string, lang?: string): Promise<boolean>
    

#### Return value

Returns `true` if time slots are available, `false` otherwise.

#### Example usage
    
    
    try {
     const isAvailable = await client.fetchTimeSlotAvailability(123, 'en')
     if (isAvailable) {
       // Show scheduling UI
     }
    } catch (error) {
     // handle error
    }
    

## Chats

Name | Description  
---|---  
`createChat` | Creates a new chat.  
`loadChat` | Retrieves chat with given chat id.  
`loadOngoingChat` | Attempts to load an ongoing chat.  
`resumeChat` | Resumes a dismissed chat with given chat id.  
`finishChat` | Set the current chat's status to finished.  
`destroyChat` | Calls `finishChat` and destroys the current chat  
`fetchMessages` | Retrieves previous messages - returns `[]` on failure.  
`sendTextMessage` | Sends a text message.  
`sendFileMessage` | Sends a file message - returns `-1` on upload failure.  
`sendPreviewMessage` | Sends a preview message.  
`getChatDeflection` | Gets the chat deflection configuration.  
`sendChatTranscripts` | Sends chat transcript to given emails.  
`downloadChatTranscript` | Downloads the chat transcript.  
`getPdfStatus` | Gets the PDF status for a transcript.  
`getChatSurvey` | Gets the chat survey questions.  
`sendChatSurvey` | Send user feedback from survey.  
`sendChatRate` | Send user feedback on chat.  
`escalateChat` | Escalates a chat from virtual agent to human agent.  
`trackChatEscalation` | Tracks chat escalation event.  
`trackChatEndUserEvent` | Tracks an end user event.  
`getChatHistory` | Retrieves the histories of a given chat.  
  
### Chat check-in

Check-in asks a consumer to confirm they're ready before connecting to an agent. This section documents the headless web SDK methods for implementing that experience. For what check-in is, how it's enabled and configured (wait-time, timeout, queue position, rejoin behavior), and reporting, see [Check-in for Chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-check-in).

Name | Description  
---|---  
`checkIn` | Sends a signal to the server to confirm user's presence in queue.  
`exitCheckIn` | Removes the user from the check-in queue.  
`notifyCheckInState` | Notifies the backend of the check-in modal visibility state.  
`rejoinChat` | Places the user back in queue after failure to confirm check-in.  
`trackCheckInEvent` | Signals to the backend when check-in events have been triggered by the UI.  
  
#### `checkIn`

Sends a confirmation signal to the server indicating the consumer is present and ready to connect with an agent during the check-in window. Updates the chat's `check_in_status` locally after the server acknowledges. Use in response to the `chat.checkInRequested` event.

#### Method signature
    
    
    checkIn(): Promise<CheckInResponse>
    

#### Return value

Returns a `CheckInResponse` object.

#### Interfaces
    
    
    interface CheckInResponse {
     chat_id: number;
     check_in_status: CheckInStatus;
     check_in_at?: string;
    }
    enum CheckInStatus {
     CONFIRMED = 'confirmed',
     EXITED = 'exited',
     PENDING = 'pending',
     REQUESTED = 'requested',
     SKIPPED = 'skipped',
     TIMED_OUT = 'timed_out',
    }
    

#### Example usage
    
    
    try {
     const response = await client.checkIn()
    } catch (error) {
     // handle error
    }
    

#### `exitCheckIn`

Signals to the server that the consumer has chosen to leave the check-in queue. Updates `check_in_status` locally. After calling this method, the consumer won't receive an agent connection for the current check-in cycle.

#### Method signature
    
    
    exitCheckIn(): Promise<CheckInResponse>
    

#### Return value

Returns a `CheckInResponse` object.

#### Interfaces
    
    
    interface CheckInResponse {
     chat_id: number;
     check_in_status: CheckInStatus;
     check_in_at?: string;
    }
    enum CheckInStatus {
     CONFIRMED = 'confirmed',
     EXITED = 'exited',
     PENDING = 'pending',
     REQUESTED = 'requested',
     SKIPPED = 'skipped',
     TIMED_OUT = 'timed_out',
    }
    

#### Example usage
    
    
    try {
     const response = await client.exitCheckIn()
    } catch (error) {
     // handle error
    }
    

#### `notifyCheckInState`

Informs the server of the check-in modal's current visibility state - whether the widget is minimized or the browser tab is inactive. The server uses this to make decisions about check-in timing. Should be called whenever the widget's visibility or tab focus changes while the `chat.checkInRequested` event is active.

#### Method signature
    
    
    notifyCheckInState(data: CheckInVisibilityStateRequest): Promise<void>
    

#### Interfaces
    
    
    interface CheckInVisibilityStateRequest {
     widget_minimized?: boolean;
     tab_inactive?: boolean;
    }
    

#### Example usage
    
    
    try {
     const visibilityState = {
       widget_minimized: true,
       tab_inactive: false,
     }
     await client.notifyCheckInState(visibilityState)
    } catch (error) {
     // handle error
    }
    

#### `rejoinChat`

Places the consumer back in the queue after they failed to confirm a check-in within the allotted time. Updates `check_in_status` locally. Use in response to the `chat.checkInTimedOut` event if the consumer still wants to connect.

#### Method signature
    
    
    rejoinChat(): Promise<CheckInResponse>
    

**Return value** : Returns a `CheckInResponse` object.

#### Interfaces
    
    
    interface CheckInResponse {
     chat_id: number;
     check_in_status: CheckInStatus;
     check_in_at?: string;
    }
    enum CheckInStatus {
     CONFIRMED = 'confirmed',
     EXITED = 'exited',
     PENDING = 'pending',
     REQUESTED = 'requested',
     SKIPPED = 'skipped',
     TIMED_OUT = 'timed_out',
    }
    

#### Example usage
    
    
    try {
     const response = await client.rejoinChat()
    } catch (error) {
     // handle error
    }
    

#### `trackCheckInEvent`

Notifies the server that the check-in modal has been displayed to the consumer. Call this once, immediately after presenting the check-in UI in response to `chat.checkInRequested`. The server uses it for operational analytics on check-in presentation rates. The call is awaited internally and returns a `Promise<void>` that can reject, so wrap it in `try/catch` (as the following example does).

#### Method signature
    
    
    trackCheckInEvent(): Promise<void>
    

#### Example usage
    
    
    try {
     await client.trackCheckInEvent()
    } catch (error) {
     // handle error
    }
    

### getMessageAttachment

Fetches an eligible attachment associated with a specific chat message. Only fetches if the message was sent by a non-end-user (`$userType !== 'end_user'`) and is of a supported attachment type (photo, video, audio, document). Returns `null` for any message that doesn't meet both conditions, not only for messages without a `media_id`. Saves the fetched file to the chat's local media cache after retrieval.

#### Method signature
    
    
    getMessageAttachment(message: MessageResponse): Promise<File | null>
    

#### Return value

Returns a File object if found, or null if not applicable.

#### Example usage
    
    
    try {
     const file = await client.getMessageAttachment(message)
    } catch (error) {
     // handle error
    }
    

### createChat

Creates a new chat session for the given menu. You can optionally specify the language, a greeting message, a trigger ID, a ticket ID, and custom data to send with the chat.

After the initial API call, the method polls the server until a `provider_channel_id` becomes available or the chat is canceled or finished. If a provider channel becomes available, the method initiates the connection to the real-time provider. The connection may still be completing when the promise resolves - listen for the `chat.connectedMessages` event to know when the connection and initial message retrieval have completed.

#### Method signature
    
    
    createChat(menuId: number | string, data: ChatRequest): Promise<Chat>
    

#### Return value

Returns a `Chat` instance.

**Warning:** This method throws immediately if there is already an ongoing chat. Check for an existing session before calling.

#### Interfaces
    
    
    interface ChatRequest {
      lang?: string;
      trigger_id?: string;
      ticket_id?: string;
      email?: string;
      greeting?: string;
      cobrowsable?: boolean;
      custom_data?: {
        signed?: string;
        unsigned?: Record<string, any>;
      };
    }
    

#### Example usage
    
    
    try {
     const chat = await client.createChat(123, { lang: 'en' })
    } catch (error) {
     // handle error
    }
    

### loadChat

Retrieves an existing chat session by its ID.

If the loaded chat is no longer ongoing, the method clears the stored chat ID and cobrowse nonce from local storage. It also does this on error, so callers don't need to handle storage cleanup manually after a failed load.

#### Method signature
    
    
    loadChat(chatId: number | string): Promise<Chat>
    

#### Return value

Returns a `Chat` instance.

**Warning:** In the case of an error, this method clears the stored chat and cobrowse session IDs from local storage before rethrowing. Any stored session reference is invalidated after a failed call.

#### Example usage
    
    
    try {
     const chat = await client.loadChat(1234)
    } catch (error) {
     // handle error
    }
    

### loadOngoingChat

Attempts to load the current ongoing chat session, if one exists. Returns `null` if no ongoing chat is found.

#### Method signature
    
    
    loadOngoingChat(): Promise<Chat | null>
    

#### Return value

Returns a `Chat` instance if found, or null if no ongoing chat exists. Will clean storage values if chat isn't ongoing.

**Warning:** In the case of an error, this method clears the stored chat ID from local storage before rethrowing. Any stored session reference is invalidated after a failed call.

#### Example usage
    
    
    try {
     const chat = await client.loadOngoingChat()
    } catch (error) {
     // handle error
    }
    

### resumeChat

Resumes a previously dismissed chat session by its ID, allowing the consumer to continue the conversation.

If the client already holds a reference to a chat with the same ID, the method short-circuits: it patches the status to `queued` on the existing instance rather than fetching a new one. If the IDs don't match, a new `Chat` instance is created and registered.

#### Method signature
    
    
    resumeChat(chatId: number | string): Promise<Chat>
    

#### Return value

Returns a `Chat` instance.

#### Example usage
    
    
    try {
     const chat = await client.resumeChat(1234)
    } catch (error) {
     // handle error
    }
    

### finishChat

Sets the current chat session's status to finished. This ends the chat from the consumer's side.

If the chat is both connected to the real-time provider and in an ended state after the PATCH, the method also disconnects from the provider. Callers don't need to call `destroyChat` if only ending the chat gracefully is the goal.

#### Method signature
    
    
    finishChat(): Promise<void>
    

#### Example usage
    
    
    try {
     await client.finishChat()
    } catch (error) {
     // handle error
    }
    

### destroyChat

Finishes and destroys the current chat session, cleaning up all internal state. This calls `finishChat` internally, then tears down the chat instance. Before finishing the chat, the method mutes it (suppresses incoming real-time events) to avoid processing messages during teardown. Clears the internal tracker ID after the chat is destroyed.

#### Method signature
    
    
    destroyChat(): Promise<void>
    

#### Example usage
    
    
    try {
     await client.destroyChat()
    } catch (error) {
     // handle error
    }
    

### fetchMessages

Retrieves the message history for the current chat session from the real-time provider. Should be called after the chat is connected; if called before the chat connects it returns an empty array rather than throwing. Automatically fetches document URLs for any `document`-type messages and merges them into the response. For `server_message`-type messages, fetches task virtual agent message content and formats it inline. Returns an empty array on failure rather than throwing.

#### Method signature
    
    
    fetchMessages(): Promise<MessageResponse[]>
    

#### Return value

Returns an array of `MessageResponse`. Returns empty array on failure.

**Warning:** This method doesn't throw on failure. Returns an empty array (`[]`) if message retrieval fails. Don't rely on `try/catch`; check the return value instead.

#### Interfaces
    
    
    interface MessageResponse {
      $index: number;
      $sid: string;
      $timestamp: Date;
      $userType: string;
      $userId: number;
      type: string;
      content?: string;
      event?: string;
      file?: File;
      media_id?: number;
      groupMessageId?: number;
      document?: {
        url: string;
      };
      unredacted?: string;
      buttons?: {
        title: string;
      }[];
      message?: { messages: string[], type };
      signature?: string,
      form?: {
        id: number,
        form_type: string,
        name: string,
        title: string,
        subtitle: string,
        external_form_id: string,
        smart_action_id: number,
        image: string
      }
    
      // allow extra parameters
      [key: string]: unknown;
    }
    

#### Example usage
    
    
    const messages = await client.fetchMessages()
    

### sendTextMessage

Sends a text message in the current chat session.

The method sanitizes the raw content before sending and returns early (no-op) if the result is empty. If the chat is in a task virtual agent flow (`inTask`), the message is routed through the task virtual agent endpoint instead of the regular channel. If server-side redaction is enabled, the message is sent using a server endpoint rather than through the real-time provider directly.

#### Method signature
    
    
    sendTextMessage(rawContent: string): Promise<void>
    

#### Example usage
    
    
    try {
     await client.sendTextMessage("hello world")
    } catch (error) {
     // handle error
    }
    

### sendFileMessage

Uploads a file to the current chat session through a three-step process: obtaining a presigned cloud-storage URL from the server, uploading the file directly to that URL, then confirming the upload back to the server. The upload route is determined automatically from the file's MIME type: images are sent as photo messages and videos as video messages; other file types are routed based on their MIME type. Returns the message ID on success, or `-1` on failure.

#### Method signature
    
    
    sendFileMessage(file: File): Promise<number>
    

#### Return value

Returns the message ID or `-1` if the upload failed. However, the subsequent message-send can still reject (for example, `ChatEndedError`), so wrap the call in `try/catch` in addition to checking for `-1`.

#### Example usage
    
    
    const input = document.querySelector('input[type="file"]')
    const file = input.files[0]
    try {
      const id = await client.sendFileMessage(file)
      if (id === -1) {
        // handle upload failure
      }
    } catch (error) {
      // handle message-send failure
    }
    

### sendPreviewMessage

Sends a preview message in the current chat session. Preview messages are typically used to show the agent what the consumer is typing before the message is submitted. If both `redaction_enabled` and `agent_incoming_ha_enabled` are true on the chat state, the preview is sent through a server endpoint (`POST /chats/{id}/redact_messages`) rather than the real-time provider channel.

#### Method signature
    
    
    sendPreviewMessage(content: string): Promise<void>
    

#### Example usage
    
    
    try {
     await client.sendPreviewMessage('preview content')
    } catch (error) {
     // handle error
    }
    

### getChatDeflection

Retrieves the chat deflection configuration for the current chat session, including whether deflection is enabled, the wait time threshold, and the available deflection options.

Returns `null` if deflection isn't enabled for the chat (the server response's `enabled` field is falsy). Callers should null-check before reading the response.

#### Method signature
    
    
    getChatDeflection(): Promise<ChatDeflectionResponse | null>
    

#### Return value

Returns either a `ChatDeflectionResponse` object or `null` if deflection isn't enabled for the chat.

#### Interfaces
    
    
    interface ChatDeflectionResponse {
     enabled: boolean;
     threshold: number;
     email: boolean;
     keep_waiting: boolean;
     external_deflection_links: {
       enabled: boolean;
       ids: number[];
     };
    }
    

#### Example usage
    
    
    try {
     const deflection = await client.getChatDeflection()
    } catch (error) {
     // handle error
    }
    

### sendChatTranscripts

Sends the current chat transcript to the specified email addresses.

#### Method signature
    
    
    sendChatTranscripts(emails: string[]): Promise<void>
    

#### Example usage
    
    
    try {
     await client.sendChatTranscripts([
       "name1@example.com",
       "name2@example.com",
     ])
    } catch (error) {
     // handle error
    }
    

### downloadChatTranscript

Initiates a download of the current chat transcript as a PDF. Returns a transcript object that can be used with `getPdfStatus` to track the generation progress.

#### Method signature
    
    
    downloadChatTranscript(): Promise<GenerateTranscriptResponse>
    

#### Return value

Returns the transcript object.

#### Interfaces
    
    
    interface GenerateTranscriptResponse {
     status: string;
     chat_transcript_id: number;
    }
    

#### Example usage
    
    
    try {
     const resp = await client.downloadChatTranscript()
    } catch (error) {
     // handle error
    }
    

### getPdfStatus

Checks the generation status of a previously requested chat transcript PDF. Use the `chat_transcript_id` returned by `downloadChatTranscript` to poll for completion.

#### Method signature
    
    
    getPdfStatus(id: number): Promise<RequestReturn>
    

#### Return value

Returns the PDF status object.

#### Interfaces
    
    
    interface RequestReturn {
       //...
       headers,
       data: PdfStatusResponse,
     }
    
    
     interface PdfStatusResponse {
       status: string;
       body?: File;
       failed_reason?: string;
     }
    

#### Example usage
    
    
    const response = await client.getPdfStatus(pdfId)
    // check header for status
    const status = response.headers['x-transcript-status'];
    // otherwise use status on data
    const data = response.data
    console.log(data.status)
    

### getChatSurvey

Retrieves the post-chat survey questions configured for the current chat session. The survey is presented to consumers after a chat ends.

#### Method signature
    
    
    getChatSurvey(): Promise<ChatSurveyResponse | null>
    

#### Return value

Returns either a `ChatSurveyResponse` object or null.

#### Interfaces
    
    
    interface QuestionItem {
     id: number;
     type: "csat" | "star" | "free-form" | "scale" | "enumeration";
     display_text: string;
     name?: string;
     is_csat?: boolean;
     position?: number;
     valid_answers?: {
       key: string;
       value: string;
     }[]
    }
    interface ChatSurveyResponse {
     id?: number;
     lang?: string;
     sign_off_display_text: string;
     questions: QuestionItem[];
    }
    

#### Example usage
    
    
    try {
     const data = await client.getChatSurvey()
     if (data) {
       console.log(data.questions)
     }
    } catch (error) {
     // handle error
    }
    

### sendChatSurvey

Submits the consumer's answers to the post-chat survey. Each answer is keyed by the question ID.

#### Method signature
    
    
    sendChatSurvey(answers: SurveyAnswers): Promise<void>
    

**Warning:** This method throws immediately if the chat's feedback type isn't `'survey'`. Callers should check `chat.feedbackType === 'survey'` before calling, or handle the error.

#### Interfaces
    
    
    interface SurveyAnswers {
     [question_id: string]: number | string;
    }
    

#### Example usage
    
    
    try {
     await client.sendChatSurvey({
       123: "a",
       231: "b",
     })
    } catch (error) {
     // handle error
    }
    

### sendChatRate

Submits the consumer's rating and optional feedback for the chat session. Used when the post-chat feedback type is a rating rather than a full survey.

#### Method signature
    
    
    sendChatRate(data: RateRequest): Promise<void>
    

**Warning:** This method throws immediately if the chat's feedback type isn't `'rate'`. Callers should check `chat.feedbackType === 'rate'` before calling, or handle the error.

#### Interfaces
    
    
    interface RateRequest {
     rating: number;
     feedback?: string;
    }
    

#### Example usage
    
    
    try {
     await client.sendChatRate({
       rating: 5,
       feedback: "Very good service",
     })
    } catch (error) {
     // handle error
    }
    

### escalateChat

Escalates the current chat from a virtual agent to a human agent.

#### Method signature
    
    
    escalateChat(data?: EscalateRequest): Promise<void>
    

#### Interfaces
    
    
    interface EscalateRequest {
     force_escalate: boolean;
     menu_id: number;
     lang: string;
    }
    

#### Example usage
    
    
    try {
     // Escalate to a specific menu in a given language
     await client.escalateChat({
       force_escalate: true,
       menu_id: 123,
       lang: 'en',
     })
    } catch (error) {
     // handle error
    }
    // Or, escalate without arguments to use defaults
    try {
     await client.escalateChat()
    } catch (error) {
     // handle error
    }
    

### trackChatEscalation

Tracks a chat escalation event, recording the escalation ID and the channel it was escalated to.

#### Method signature
    
    
    trackChatEscalation(escalationId: number, channel: string): Promise<void>
    

#### Example usage
    
    
    try {
     await client.trackChatEscalation(escalationId, channel)
    } catch (error) {
     // handle error
    }
    

### trackChatEndUserEvent

Tracks a custom end-user event during the chat session, which can be used for analytics or to trigger backend workflows. If the `data` object doesn't include `end_user_name` and a name is available on the authenticated user profile, it is populated automatically before the request is sent.

#### Method signature
    
    
    trackChatEndUserEvent(data: ChatEndUserEventRequest): Promise<void>
    

#### Return value

Returns void.

#### Interfaces
    
    
    interface ChatEndUserEventRequest {
      event: {
        name: string;
        payload: Record<string, string>;
      };
      end_user_name?: string;
    }
    

#### Example usage
    
    
    try {
     await client.trackChatEndUserEvent({
       event: {
         name: 'add_to_cart',
         payload: {
           product_id: 'sku-1234',
           quantity: '2',
         },
       },
       // end_user_name is auto-populated from the authenticated user
       // profile if omitted
     })
    } catch (error) {
     // handle error
    }
    

### getChatHistory

Retrieves the consumer's past chat history, including message content and metadata. Results are paginated. Page 1 returns up to 2 chats; subsequent pages return 1 chat each. This asymmetric pagination is intentional and allows the first call to pre-load adjacent history context.

#### Method signature
    
    
    getChatHistory(page?: number): Promise<ChatHistoryResponse | null>
    

#### Return value

Returns either a `ChatHistoryResponse` object or `null`.

#### Interfaces
    
    
    interface ChatHistoryItem {
     comm_id: number;
     assigned_at: string;
     comm_type: string;
     timezone: string;
     entries: MessageResponse[];
     [key: string]: unknown;
    }
    interface ChatHistoryResponse {
     chats: ChatHistoryItem[];
     missing_chat_ids: number[];
     pagination: {
       next_page: number;
       per_page: number;
     }
    }
    

#### Example usage
    
    
    try {
     const data = await client.getChatHistory(1) // page defaults to 1 if omitted
     console.log(data)
    } catch (error) {
     console.log(error)
    }
    

## Emails

Name | Description  
---|---  
`createEmail` | Send email to a given menu id's email channel.  
`getProhibitedFileTypes` | Get the prohibited file types for the email attachments.  
  
### createEmail

Sends an email message to the email channel associated with the given menu. The consumer can include a name, email address, message body, and optional file attachments.

#### Method signature
    
    
    createEmail(menuId: number | string, data: EmailRequest): Promise<EmailResponse>
    

#### Return value

Returns an `EmailResponse` object on failure or success.

#### Interfaces
    
    
    interface EmailRequest {
     name?: string;
     email: string;
     content: string;
     lang?: string;
     files?: File[];
     recaptcha?: string;
    }
    interface EmailResponse {
     id: number;
     type: string;
     status: string;
     fail_reason: string;
     attachment_count: number;
    }
    

#### Example usage
    
    
    try {
     await client.createEmail(123, {
       lang: "en",
       name: "User name",
       email: "name@example.com",
       content: "description of the question",
       files: input.files,
     })
    } catch (error) {
     console.log(error.message)
    }
    

### getProhibitedFileTypes

Retrieves the list of file types that aren't allowed as email attachments, as configured by the administrator.

#### Method signature
    
    
    getProhibitedFileTypes(): Promise<FileTypeItem[]>
    

#### Return value

Returns an array of `FileTypeItem`.

#### Interfaces
    
    
    interface FileTypeItem {
     extension: string;
     description: string;
    }
    

#### Example usage
    
    
    try {
     const types = await client.getProhibitedFileTypes()
    } catch (error) {
     // handle error
    }
    

## Screen share

Name | Description  
---|---  
`createCobrowseCode` | Generates a cobrowse code.  
`startCobrowse` | Request a cobrowse session.  
`restoreCobrowseSession` | Restores a cobrowse session after the browser window is reopened.  
  
### createCobrowseCode

Generates a unique cobrowse (screen share) session code that can be shared with an agent to initiate a session. Initializes the cobrowse client if it hasn't been initialized yet. Reuses any existing nonce from storage rather than generating a new one on each call, so the same session code can be retrieved across page loads.

#### Method signature
    
    
    createCobrowseCode(lang?: string, customData?: Record<string, string>): Promise<string>
    

#### Return value

Returns a cobrowse code string or empty string (`''`) on failure.

**Warning:** This method doesn't throw on failure. Don't rely on `try/catch`; check the return value instead.

#### Example usage
    
    
    const code = await client.createCobrowseCode()
    // 123456
    

### startCobrowse

Requests the start of a cobrowse (screen share) session from the end-user's side during an active chat.

#### Method signature
    
    
    startCobrowse(from?: string): Promise<void>
    

**Warning:** This method throws if the current chat wasn't created with `cobrowsable: true`. Callers can check `chat.cobrowsable` before calling to avoid the throw.

#### Example usage
    
    
    try {
     await client.startCobrowse()
    } catch (error) {
     // handle error
    }
    

### restoreCobrowseSession

Attempts to restore a previously active cobrowse session after the browser window is reopened or the widget is reloaded.

#### Method signature
    
    
    restoreCobrowseSession(): Promise<void>
    

#### Return value

Returns `Promise<void>`. This method is a no-op (returns immediately without error) if cobrowse isn't enabled in the client options or if no previous cobrowse session exists in storage.

**Warning:** This method doesn't throw. If an error occurs during restoration, the method logs the error internally and clears the stored cobrowse session, then returns cleanly. Callers don't need `try/catch`.

#### Example usage
    
    
    // Safe to call unconditionally - will no-op if cobrowse is not enabled
    // or if no previous session exists
    await client.restoreCobrowseSession()
    

## Post session virtual agent

Name | Description  
---|---  
`updatePostSession` | Set ongoing chat's post session status.  
  
### updatePostSession

This method is used to update the post-session virtual agent status for the ongoing chat.

  * Updates the post-session virtual agent status for the ongoing chat. Use this to signal readiness, progress, or completion of a post-session virtual agent flow.

  * Returns immediately as a no-op if `postSessionStatus` is `FINISHED` or `WAITING` — those transitions are handled internally.

  * Has internal retry logic specifically for the `IN_PROGRESS` status on a `400` response, so callers don't need to implement their own retry for that case.




#### Method signature
    
    
    updatePostSession(postSessionStatus: PostSessionStatus, optInSelection?: boolean): Promise<void>
    

#### Interfaces
    
    
    enum PostSessionStatus {
     READY = 'ready',
     IN_PROGRESS = 'in_progress',
     WAITING = 'waiting',
     FINISHED = 'finished',
    }
    

#### Example usage
    
    
    try {
     // Without opt-in selection
     await client.updatePostSession(PostSessionStatus.READY)
     // With opt-in selection
     await client.updatePostSession(PostSessionStatus.READY, true)
    } catch (error) {
     // handle error (e.g., show a notification to the user)
    }
    

#### Related interface
    
    
    interface ChatResponse {
     //...
     post_session_required?: boolean;
     post_session_opt_in_required?: boolean;
     post_session_transfer_status?: string;
    }
    

  * `post_session_required` \- post session required after a chat.

  * `post_session_opt_in_required` \- is opt in enabled.

  * `post_session_transfer_status` \- this is one of the PostSessionStatus enums.




## Debugging

Name | Description  
---|---  
`getLogs` | Retrieves internal debug logs from the SDK.  
`printLogs` | Prints internal debug logs to the browser console.  
  
### getLogs

Retrieves the internal debug logs collected by the SDK, including both bridge-level and root-level logs. Useful for troubleshooting integration issues.

#### Method signature
    
    
    getLogs(): Promise<{ bridgeLogs: LogHistoryData[], rootLogs: LogHistoryData[] }>
    

#### Return value

Returns an object containing two arrays of `LogHistoryData`.

#### Interfaces
    
    
    interface LogHistoryData {
     date: string;
     channel: string;
     level: string;
     args: any[];
    }
    

**Note:** Bridge logs are fetched first internally, because the fetch itself produces a root log entry. As a result, `rootLogs` intentionally captures that final log.

**Granularity**

Each `LogHistoryData` entry captures a single log event:

  * `date` \- ISO 8601 timestamp of the event.

  * `channel` \- the SDK module that emitted it (e.g., top-level client, chat layer, cobrowse layer, real-time provider).

  * `level` \- log severity: `debug`, `info`, `warn`, or `error`.

  * `args` \- the raw arguments captured by the log call.




Example entry:
    
    
    {
     "date": "2026-05-08T14:02:13.412Z",
     "channel": "Provider",
     "level": "info",
     "args": ["chat connected", { "chatId": 4421 }]
    }
    

The exact set of channels and message contents may evolve between SDK releases. Treat the logs as a debugging aid, not a stable parsing target - don't build production logic that depends on specific channel names or message strings.

##### Scope and recommended use

`getLogs` returns SDK-internal records intended to help diagnose integration issues with the headless web SDK itself. Its primary use case is **support diagnostics** : when an end user reports an issue, your application can capture the result of `getLogs` and attach it to the support ticket sent to CCAI Platform.

The returned logs do **not** include:

  * Your host page's application telemetry, business events, or user navigation.

  * Network failures the browser doesn't surface to the SDK (e.g., CORS, mixed-content, or certificate errors).

  * Server-side request traces or backend details beyond the HTTP status returned to the SDK.




`getLogs` is **not** a replacement for your own observability tooling. We recommend pairing the SDK with:

  * A browser-side error/RUM tracker (Sentry, Datadog Browser RUM, New Relic Browser, or equivalent).

  * Server-side logging on your authentication endpoint (the `authenticate` callback the SDK calls).

  * Application-level listeners on `chat.disconnected`, `chat.timeout`, and `chat.ended` if you need to forward chat lifecycle signals to your own telemetry pipeline.




#### Example usage
    
    
    try {
     const { bridgeLogs, rootLogs } = await client.getLogs()
     console.log('Bridge logs:', bridgeLogs)
     console.log('Root logs:', rootLogs)
    } catch (error) {
     // handle error
    }
    

### printLogs

Prints all internal debug logs directly to the browser console. This is a convenience method that calls `getLogs()` internally and formats the output.

#### Method signature
    
    
    printLogs(): Promise<void>
    

#### Example usage
    
    
    try {
     await client.printLogs()
    } catch (error) {
     // handle error
    }
    

## Miscellaneous

Name | Description  
---|---  
`runTrigger` | Checks proactive triggers for any that should be firing.  
`getAfterHourMessage` | Get the message for after hour deflection.  
  
### runTrigger

Iterates over configured proactive triggers and invokes the supplied callback for any whose conditions are met (URL keywords, page-visit count, stay time, visitor type).

#### Method signature
    
    
    runTrigger(cb: (trigger: TriggerItem) => void): Promise<void>
    

#### Interfaces
    
    
    interface TriggerItem {
     id: number;
     menu_id: number;
     messages: TriggerMessage[];
     keywords_included?: string[];
     keywords_included_or?: string[][];
     keywords_excluded?: string[];
     keywords_excluded_or?: string[][];
     lang?: string;
     page_visit_count: number;
     stay_time: number;
     visitor_type: string;
    }
    interface TriggerMessage {
     lang: string;
     text: string;
    }
    

#### Example usage
    
    
    await client.runTrigger((trigger: TriggerItem) => {
     // code to run for given trigger
    })
    

### getAfterHourMessage

Returns the configured deflection message to display when the requested channel is outside operating hours.

#### Method signature

The method signature is:
    
    
    getAfterHourMessage(lang?: string): Promise<string>
    

#### Return value

Returns a string containing a configured message.

#### Example usage
    
    
    try {
     const message: string = await client.getAfterHourMessage()
    } catch (error) {
     // handle error
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
