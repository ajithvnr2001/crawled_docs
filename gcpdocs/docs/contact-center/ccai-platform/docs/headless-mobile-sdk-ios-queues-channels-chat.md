---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat/
title: Headless mobile SDK for iOS: Queues, channels, and chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:17:50.841076+00:00
---

# Headless mobile SDK for iOS: Queues, channels, and chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless mobile SDK for iOS: Queues, channels, and chat Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate and customize the headless mobile SDK in your iOS application. It covers how to expose your support entry points (queues and channels) in your app, and how to drive the full chat lifecycle: starting, resuming, sending messages and attachments, indicating typing, redacting sensitive data, escalating to human agents, and ending the session.

**Note:** Before you begin, make sure you have completed initialization, authentication, and push-notification setup in [Headless mobile SDK for iOS: getting started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started).

## Select queues and channels

  * A queue usually represents a support entry point, such as "Billing", "Technical Support", or "VIP Support".

  * Each queue can offer one or more of the following channels:

    * Chat

    * Instant call (voice)

    * Scheduled call

    * Email

    * External deflection links (links to your self-service pages or other channels)




Queues and channel availability are configured by admins in the **Contact Center AI Platform Admin Portal**.

### How it looks in your app

In your app, a typical flow is:

  1. You add a support entry point in your app (for example, a "Help" tab or a "Contact Us" button).

  2. When the user taps it, you fetch the queue menu from the SDK and render your own menu UI.

  3. When the user chooses a queue, you inspect its available channels.

  4. Your app shows those channels to the user (for example, "Chat now", "Call now", "Schedule a call", "Email us", "Visit Help Center").

  5. When the user selects a channel, you call the corresponding SDK API.




#### Fetch queue menus from the SDK

The SDK provides `queueMenuService` to fetch queue menus. The `get` method returns a `QueueMenuResult` containing the list of queues (`menus: [QueueMenu]`) and an `isDirectAccess` flag:
    
    
    do {
        let (menus, isDirectAccess) = try await CCAI.shared.queueMenuService?.get(
            key: nil,       // Optional: Direct Access Point key
            language: "en"  // Optional: Language code
        )
        // Display menus in your custom UI
        displayQueueMenu(menus)
    } catch {
        print("Failed to fetch queue menus: \(error)")
    }
    

The optional `key` parameter lets you bypass the full queue menu and jump the user directly to a specific queue. In the Contact Center AI Platform, this is achieved with a direct access point (DAP).

A DAP can be configured by admins in the CCAI Platform portal in the following way:

  1. Go to **Settings > Queue** and select any queue from the menu structure.

  2. From the **Access Point** section, click **\+ Create direct access point**.

  3. Enter the key in the text form.

  4. Click **Save**.




When a `key` is provided and `isDirectAccess` returns `true`, skip rendering the menu tree and proceed directly to the channel selection or session start for that queue. This is useful for deep-linked support flows (for example, a "Chat about this order" button on an order details screen).

`QueueMenuResult` also carries the Direct Access Point context of the request:

**Property** | **Type** | **Description**  
---|---|---  
`menus` | [QueueMenu]  | The queues to show the user.   
`isDirectAccess` | Bool  | `true` when the request matched a Direct Access Point.   
`directAccessKeyId` | Int?  | The ID of the matched Direct Access Point, or `nil` if none matched.   
`dapRequestId` | String?  | The ID of the routing request when an API Request Direct Access Point for Chat ran (see below), or `nil`.   
  
When the user starts a chat from these results, pass `directAccessKeyId` and `dapRequestId` into the `ChatRequest` (see Start a chat from a Direct Access Point).

#### Route through an API Request Direct Access Point for Chat:

If your admins enable API Request Direct Access Point for Chat (**Settings > Developer Settings > Manage API Request Direct Access Point**), the platform calls your routing API when your app fetches the queue menu, and routes the user to the access point that the API selects. To give your API more to route on, pass the user's custom data and first message to get:
    
    
    let menuResult = try await CCAI.shared.queueMenuService?.get(
        key: nil,
        language: nil,
        customData: customData,                              // Signed and/or unsigned custom data
        initialMessage: "I want to update my billing address" // The user's first message
    )
    

**Warning:** When the access point type is Webhook Response, the platform holds the menu response until your system calls back. get waits for the callback, checking every 2 seconds, until routing completes or the API Callback Timeout passes; it then returns the menu. Call it from a Task you can cancel, and show a loading state while it runs.

#### `QueueMenu` data structure
    
    
    public struct QueueMenu: Codable, Identifiable, Hashable {
        public let id: Int
        public let name: String?
        public let hidden: Bool?
        public let position: Int?
        public let settings: [QueueMenuSetting]?
        public let children: [QueueMenu]?
        public let channels: Channels?
        public let redirectionExtra: QueueMenuRedirection?
        public let deflectionFrom: [QueueMenuDeflection]?
    }
    
    public struct Channels: Codable {
        public let email: EmailChannel?
        public let chat: ChatChannel?
        public let voiceCall: VoiceCallChannel?
        public let externalDeflectionLink: ExternalDeflectionLink?
    }
    
    // VoiceCallChannel (simplified - see the "Voice, screen share, scheduled call, and email" article for per-field usage)
    public struct VoiceCallChannel: Codable {
        public let instantEnabled: Bool?            // Live voice call allowed now
        public let preSessionSmartAction: Bool?     // Per-channel pre-session smart action flag
        public let scheduleEnabled: Bool?           // Scheduled calls supported
        public let recordingOption: RecordingOption? // .always / .never / .askUser
        public let voicemailReason: String?
        public let phoneNumber: String?
        public let scheduleDeflectionType: DeflectionType?
        public let deflected: Bool?
        public let deflectedReason: DeflectionType?
    }
    

#### Fetch wait times

You can also retrieve estimated wait times for a specific queue:
    
    
    do {
        let waitTimes = try await CCAI.shared.queueMenuService?.getWaitTimes(
            menuId: 123,
            language: "en"
        )
        print("Chat wait: \(waitTimes?.chat ?? 0) seconds")
        print("Voice wait: \(waitTimes?.voiceCall ?? 0) seconds")
    } catch {
        // handle error
    }
    

**Note:** `getWaitTimes` returns a `QueueMenuWaitTimeResponse` with two `Int` properties, `chat` and `voiceCall`. By default, the SDK raises `voiceCall` to at least 60 seconds so your UI never shows a misleadingly short wait; pass `minimumSeconds: 0` to receive the raw server value.

#### Implementation example
    
    
    func showAvailableChannels(for queueMenu: QueueMenu) {
        guard let channels = queueMenu.channels else { return }
    
        // Update your custom UI based on what the SDK says is active
        chatButton.isHidden = channels.chat == nil
        callButton.isHidden = channels.voiceCall == nil
        emailButton.isHidden = channels.email == nil
    
        // External deflection link
        if let deflectionLink = channels.externalDeflectionLink {
            deflectionLinkButton.isHidden = false
            // Open in SFSafariViewController or UIApplication.shared.open()
        }
    }
    

### Single-channel queues

Sometimes a queue offers only one channel (for example, "Email only"). In this case, you can:

  * Skip the channel selection step and go straight to your email form UI.

  * Or you can still show the available channel explicitly if that makes more sense in your UX.




The SDK's configuration and metadata tells you which channels are allowed; your app decides **how** to show them.

### Redirect and deflection

Admins can configure a queue to redirect users instead of offering channels. When `QueueMenu.redirectionExtra` is set, act on it as soon as the user selects the queue:

  * `option` says what to do: `.phone`, `.message`, `.url`, `.voicemail`, `.queue`, `.sip`, or `.contact`.

  * `data` carries the value, such as the number to dial, the message to show, or the URL to open.




`QueueMenu.deflectionFrom` is different. When a queue deflects to another queue, the platform returns the destination queue in place of the one the user selected and lists the source queues in `deflectionFrom`. It explains a redirect that already happened; it isn't a set of options to offer.

After-hours and overcapacity deflection is reported per channel. For how to handle it, see [Headless mobile SDK for iOS: smart actions, attachments, and deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-smart-actions).

## Channels

In the Headless mobile SDK, your CCAI Platform Admin Portal acts as the source of truth for your support operations. Admins configure which support channels (such as chat, voice, email, or helpful links) are available for different support queues (such as "Billing" or "Tech Support").

The SDK's job is to securely fetch this configuration and hand it to your app. Your app's job is to read that configuration and draw the appropriate user interface.

**Note:** For several channels in a headless architecture, the SDK tells you what is allowed and provides the routing metadata (for example, enabled flags, email addresses, and deflection URLs). Your app is responsible for building the UI and calling the corresponding SDK service APIs for the selected channel.

### Inspect available channels

**What the SDK provides:** A real-time list of which support channels are active and available for the specific queue the user selected, respecting your portal's business hours and capacity limits.

**What you build:** The UI menu (buttons, lists, or cards) that displays these available options to the user.

**Implementation example:** The following Swift code takes the queue the user just tapped and inspects the `Channels` struct to see which channels are enabled. It then decides which buttons to show on the screen.
    
    
    // Assuming 'selectedMenu' is a QueueMenu returned by the SDK
    func setupChannelMenu(for selectedMenu: QueueMenu) {
        hideAllChannelButtons()  // Start clean for each queue
        guard let channels = selectedMenu.channels else { return }
    
        if channels.chat?.enabled == true {
            showChatNowButton()
        }
    
        if channels.voiceCall?.instantEnabled == true {
            showCallNowButton()
        }
        if channels.voiceCall?.scheduleEnabled == true {
            showScheduleCallButton()
        }
    
        if channels.email?.enabled == true {
            showEmailUsButton()
        }
    
        if channels.externalDeflectionLink?.enabled == true {
            showHelpCenterLinks()  // One button per link in externalDeflectionLink.links whose enabled is true
        }
    }
    

To get the same list the SDK's own menu uses, call `selectedMenu.getEnabledChannels()`. It returns a `[ChannelType]` with one entry per enabled option (`.chat`, `.instantCall`, `.scheduleCall`, `.pstnCall`, `.voiceMail`, `.email`, and `.externalDeflection`).

The next sections cover each channel in detail. For chat, continue reading. For voice, screen share, scheduled call, email, and external deflection links, see [Headless mobile SDK for iOS: voice, screen share, scheduled call, and email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-voice).

## Chat service API

The `chatService` manages the full chat lifecycle. The core methods you use most frequently are:

Method | Description  
---|---  
`start` | Starts a new chat session with a `ChatRequest`.  
`sendMessage` | Sends a message (text, image, video, or form event).  
`typing` | Updates the typing indicator.  
`endChat` | Ends the current chat session.  
`resumeChat` | Resumes a previously established chat session.  
`escalateToHumanAgent` | Transfers from a virtual agent to a human agent.  
`checkStatus` | Refreshes the current chat status from the server.  
**Note:** Beyond these core methods, the `chatService` also provides smart action tracking (`notifySmartActionReceived`, `updateSmartActionStatus`), form handling (`fetchWebForm`, `getCustomFormDetails`, `submitCustomForm`), post-session management (`startPostSession`, `readyPostSession`), and transcript download. For complete method signatures and parameters, see the **Headless mobile SDK - iOS API reference**.

### `ChatRequest` and `ChatResponse` data structures

The `ChatRequest` structure contains the configuration for starting a new chat:
    
    
    public struct ChatRequest: Encodable {
        /// Convenience initializer - pass the flattened parameters.
        /// `ChatRequest` is `Encodable`; the inner `Chat` struct's stored
        /// properties are internal. Construct a `ChatRequest` using this init
        /// rather than touching the inner struct directly.
        public init(
            menuId: Int,
            lang: String = "en",
            ticketId: String? = nil,
            greeting: String? = nil,
            customData: CustomData? = nil,
            displayOrderInAdapter: [String]? = nil,
            directAccessKeyId: Int? = nil,   // From QueueMenuResult (Direct Access Point)
            dapRequestId: String? = nil,     // From QueueMenuResult (Direct Access Point)
            isScreenShareable: Bool? = nil,
            isVerifiable: Bool? = nil
        )
    }
    

After you start or resume a chat, the SDK delivers its `ChatResponse` on the `chatReceived` publisher (`start(request:)` and `resumeChat(_:)` return nothing). The properties you reference most in this guide include:

  * `id` \- The unique chat session identifier.

  * `status` \- The current chat status (queued, active, ended, etc.).

  * `agent` / `virtualAgent` \- The assigned human or virtual agent.

  * `postSessionRequired` \- Whether a post-session virtual agent is configured for the session. Surveys and CSAT are signaled by `surveyEnabled` and `csatSetting`.

  * `redactionEnabled` \- Whether automatic PII redaction is active for this session.


**Note:** `ChatResponse` contains 20 properties in total (including `providerType`, `region`, `allAgents`, `allVirtualAgents`, `menus`, `features`, `timeoutAt`, `statusText`, `providerChannelId`, `postSessionOptInRequired`, `postSessionTransferStatus`, `csatSetting`, `surveyEnabled`, and more). For the full struct definition, see the **Headless mobile SDK - iOS API reference**.

### Start a chat session

**Warning:** always call `getLastChatInProgress()` before starting a new chat. If an earlier session is still active (for example, the app was force-quit mid-conversation, or the user switched accounts), starting a second chat fails or produces undefined behavior. This check is especially critical when `userId` changes between sessions.

To start a chat session, use the `chatService` with a `ChatRequest` specifying the queue menu ID.

#### Minimal
    
    
    import CCAIKit
    import CCAIChat
    import CCAIScreenShare // If using Screen Share
    
    // If screen share is initialized, pass isScreenShareable for agent visibility
    let chatRequest = ChatRequest(
        menuId: 123,
        isScreenShareable: CCAI.shared.screenShareService != nil
    )
    await startOrResumeChat(chatRequest)
    
    // Resumes an earlier chat if there is one; otherwise starts a new one
    func startOrResumeChat(_ chatRequest: ChatRequest) async {
        guard let chatService = CCAI.shared.chatService else { return }
        do {
            // Pre-flight check: resume an earlier chat instead of starting a second one
            if let existing = try await chatService.getLastChatInProgress() {
                try await chatService.resumeChat(existing)
                return
            }
            try await chatService.start(request: chatRequest)
        } catch {
            print("Failed to start chat: \(error)")
        }
    }
    

If your app doesn't include the `CCAIScreenShare` module, remove `import CCAIScreenShare` and the `isScreenShareable` argument.

#### With explicit language and custom data
    
    
    let chatRequest = ChatRequest(menuId: 123, lang: "en")
    await startOrResumeChat(chatRequest) // Defined in the Minimal example
    

#### Start a chat from a Direct Access Point

When the user reaches a queue through a Direct Access Point, pass the access point context from the `QueueMenuResult` into the `ChatRequest`. The SDK doesn't add it for you.

  * `directAccessKeyId` \- Shows the Greeting Message configured on the access point as the chat's greeting, in place of greeting. The platform uses it only when API Request Direct Access Point for Chat is enabled, and only for a chat started on the access point's own queue.

  * `dapRequestId` \- Links the chat to its routing decision for reporting, and applies any actions your routing API returned for the session (for example, a message to send or an instruction to end the chat).



    
    
    // menuResult: the QueueMenuResult from the get call that listed selectedMenu
    
    func startChat(selectedMenu: QueueMenu, menuResult: QueueMenuResult) async {
        let chatRequest = ChatRequest(
            menuId: selectedMenu.id,
            lang: CCAI.shared.languageService?.languageCode ?? "en",
            directAccessKeyId: menuResult.directAccessKeyId,
            dapRequestId: menuResult.dapRequestId
        )
        // Defined in the Minimal example under Starting a chat session
        await startOrResumeChat(chatRequest)
    }
    

Use the values from the `get` call that led to this queue. Each dapRequestId belongs to a single routing request, so don't reuse it for a later chat. If an earlier chat is still in progress, `startOrResumeChat(_:)` resumes it, and these values aren't used.

### Resume a chat session

Resume a previously established chat session using a `ChatResponse` object:
    
    
    do {
        try await CCAI.shared.chatService?.resumeChat(chat)
    } catch {
        // handle error
    }
    

### Chat queue management

You can enqueue the current chat for later retrieval or check for existing in-progress chats:
    
    
    // Enqueue the current chat (automatically calls checkStatus() after enqueuing)
    do {
        try await CCAI.shared.chatService?.enqueueCurrentChat()
        print("Chat enqueued successfully")
    } catch {
        print("Failed to enqueue chat: \(error)")
    }
    
    // Check for an existing in-progress chat
    do {
        let chat = try await CCAI.shared.chatService?.getLastChatInProgress()
        if let chat = chat {
            print("Found ongoing chat: \(chat.id)")
        } else {
            print("No ongoing chat found")
        }
    } catch {
        print("Failed to get last chat: \(error)")
    }
    
    // Retrieve previous chat history with pagination
    do {
        let previousChats = try await CCAI.shared.chatService?.getPreviousChats(currentPage: 1)
        if let chats = previousChats {
            print("Found \(chats.messages.count) previous messages")
        }
    } catch {
        print("Failed to get previous chats: \(error)")
    }
    

### Send messages

The `sendMessage` method supports multiple message types through the `OutgoingMessageContent` enum:
    
    
    public enum OutgoingMessageContent {
        case text(content: String)
        case images(images: [UploadableImage], smartAction: SmartAction?)
        case videos(videos: [UploadableVideo], smartAction: SmartAction?)
        case formComplete(payload: FormCompletePayload)
        case screenShare(event: ChatMessageEvent, response: ScreenShareResponse?)
    }
    

The `UploadableImage` and `UploadableVideo` types encapsulate media data for upload:
    
    
    public struct UploadableImage {
        public let data: Data        // The binary data of the image
        public let mimeType: String  // e.g. "image/jpeg", "image/png"
    }
    
    public struct UploadableVideo {
        public let url: URL          // The file URL of the video
        public let mimeType: String  // e.g. "video/mp4"
    }
    

**Usage examples**
    
    
    // Send text message
    do {
        try await CCAI.shared.chatService?.sendMessage(.text(content: "Hello world"))
    } catch {
        print("Failed to send message: \(error)")
    }
    
    // Send image message
    let imageData = UIImage(named: "photo")?.jpegData(compressionQuality: 0.8) ?? Data()
    let uploadableImage = UploadableImage(data: imageData, mimeType: "image/jpeg")
    do {
        try await CCAI.shared.chatService?.sendMessage(
            .images(images: [uploadableImage], smartAction: nil)
        )
    } catch {
        print("Failed to send image: \(error)")
    }
    
    // Send form completion event
    let formCompletePayload = FormCompletePayload(
        type: "form_complete",
        signature: "form_signature",
        data: FormCompleteData(
            smartActionId: 123,
            status: .success,
            timestamp: "2024-01-01T12:00:00Z",
            details: FormCompleteDataDetails(message: "Form submitted successfully")
        )
    )
    do {
        try await CCAI.shared.chatService?.sendMessage(.formComplete(payload: formCompletePayload))
        print("Form completion event sent")
    } catch {
        print("Failed to send form completion: \(error)")
    }
    

The `screenShare` message type is used to send screen sharing events and responses to the server. Available screen share events include:

  * `screenShareRequestedFromAgent` \- Agent requested screen sharing

  * `screenShareRequestedFromEndUser` \- End user requested screen sharing

  * `screenShareCodeGenerated` \- Screen share code was generated

  * `screenShareFailed` \- Screen sharing failed

  * `screenShareStarted` \- Screen sharing session started

  * `screenShareEnded` \- Screen sharing session ended


**Note:** If redaction is enabled (via the `redactionEnabled` property in `ChatResponse`), sensitive information in plain text messages is automatically redacted before being sent to the agent. See Message redaction for details.

### Typing indicators and message previews

Update the typing status and send message previews while the user is typing:
    
    
    // Update typing indicator
    CCAI.shared.chatService?.typing(true)   // Start typing
    CCAI.shared.chatService?.typing(false)  // Stop typing
    
    // Send message preview (only works when Task virtual agent is not active)
    do {
        try await CCAI.shared.chatService?.sendMessagePreview("Typing...")
    } catch {
        print("Failed to send message preview: \(error)")
    }
    
    // Example: Send preview as user types
    func onTextChanged(_ text: String) {
        Task {
            do {
                try await CCAI.shared.chatService?.sendMessagePreview(text)
            } catch {
                print("Failed to send preview: \(error)")
            }
        }
    }
    

### Message redaction

Automatic redaction of sensitive information (PII, credit card numbers, etc.) is supported for plain text chat messages and message previews.

**Redaction configuration**

  * Controlled by the `redactionEnabled` property in `ChatResponse`.

  * Configured in the portal under **Settings** > **Chat Settings** > **Automatic Redaction**.

  * When enabled, sensitive data is automatically replaced with placeholders before being sent to agents.



    
    
    // Redaction is automatically handled. Use sendMessage as usual
    do {
        // If redaction is enabled, sensitive data will be automatically redacted
        try await CCAI.shared.chatService?.sendMessage(
            .text(content: "My phone number is 4155553423")
        )
        // The message will be sent with sensitive information redacted
    } catch {
        print("Failed to send message: \(error)")
    }
    

**Note:**

  * Redaction only applies to plain text messages.

  * Redaction is automatically enabled or disabled based on portal configuration.

  * The redaction status is available in `ChatResponse` after starting or resuming a chat.

  * Message previews with timestamps older than the last sent preview are automatically skipped.




### Ending and escalating chats
    
    
    // End the current chat session
    do {
        try await CCAI.shared.chatService?.endChat()
        print("Chat ended successfully")
    } catch {
        print("Failed to end chat: \(error)")
    }
    
    // Escalation from a virtual agent to a human agent.
    //
    // `escalateToHumanAgent()` is `async throws -> Void` and initiates a basic
    // escalation directly. Use it for queues where your UI doesn't need to
    // present an option picker.
    do {
        try await CCAI.shared.chatService?.escalateToHumanAgent()
        print("Escalation requested successfully")
    } catch {
        print("Escalation failed: \(error)")
    }
    
    // Escalation with a specific option (for example, "Email us instead").
    // `escalate(option:)` is the single-call form when the user has already
    // picked an option in your UI.
    let option = ChatEscalationOption(escalationId: 123, deflectionChannel: "email")
    do {
        try await CCAI.shared.chatService?.escalate(option: option)
        print("Escalation committed successfully")
    } catch {
        print("Escalation failed: \(error)")
    }
    
    // `updateEscalation(option:)` is `async throws -> Void`. Use it only when
    // an escalation has already started with `escalateToHumanAgent()` and your
    // UI needs to commit a specific option mid-flight.
    do {
        try await CCAI.shared.chatService?.updateEscalation(option: option)
        print("Escalation updated successfully")
    } catch {
        print("Failed to update escalation: \(error)")
    }
    
    // Check the current chat status (refreshes from server)
    do {
        try await CCAI.shared.chatService?.checkStatus()
        print("Status check completed successfully")
    } catch {
        print("Failed to check status: \(error)")
    }
    

### Chat events

Send chat events to the server for tracking user interactions:
    
    
    let event = ChatEvent(
        name: "form_received",
        payload: ["name": "contact_form"]
    )
    
    do {
        try await CCAI.shared.chatService?.sendEvent(event)
        print("Event sent successfully")
    } catch {
        print("Failed to send event: \(error)")
    }
    

Common event use cases include form interactions (`"form_received"`, `"form_clicked"`), smart action events (`"smart_action_received"`, `"smart_action_clicked"`), and custom user interactions for analytics.

### Network connectivity changes

**What the SDK provides:** A `networkConnectivityChanged` publisher on chatService that reports whether the device has a network connection. It publishes the current value when you subscribe, and again whenever connectivity is lost or restored.

**What you build:** A subtle banner or toast that reflects the connectivity state (for example, **Reconnecting…** or **Back online**), and the handling for any message that fails to send while the device is offline.

**Implementation example:** Subscribe to `networkConnectivityChanged` and toggle a connectivity banner on the main thread.
    
    
    CCAI.shared.chatService?.networkConnectivityChanged
        .receive(on: DispatchQueue.main)
        .sink { connected in
            connectivityBanner.isHidden = connected
        }
        .store(in: &cancellables)
    

### Download transcript visibility

The `downloadTranscriptVisibility` parameter on `ChatOptions` stores where your app should offer a transcript download. In a headless integration, your UI draws the download control, so the SDK doesn't hide anything itself: read the setting from `CCAI.shared.chatService?.options?.downloadTranscriptVisibility`, or pass it to `ChatState.availableActions(canEscalate:hasMessageExchange:downloadTranscriptVisibility:)`, which leaves out `.downloadTranscript` when `hideInOptionMenu` is set. `DownloadTranscriptVisibility` is an `OptionSet`, so you can combine cases.

  * `hideInOptionMenu` \- don't offer the transcript during an active session.

  * `hideInPostChat` \- don't offer the transcript after the session ends.

  * `hideAll` \- never offer the transcript. Equivalent to `[.hideInOptionMenu, .hideInPostChat]`.

  * Omit the parameter (or pass an empty `OptionSet`) to offer it everywhere.



    
    
    // Offer the download during the session, but not after it ends
    let chatOptions = ChatOptions(
        downloadTranscriptVisibility: .hideInPostChat
    )
    CCAI.shared.initializeChat(chatOptions)
    
    // Never offer the download
    let chatOptionsHidden = ChatOptions(
        downloadTranscriptVisibility: .hideAll
    )
    CCAI.shared.initializeChat(chatOptionsHidden)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
