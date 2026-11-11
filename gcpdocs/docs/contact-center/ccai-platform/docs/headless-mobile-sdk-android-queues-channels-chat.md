---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-queues-channels-chat/
title: Headless mobile SDK for Android: Queues, channels, and chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:09:41.929504+00:00
---

# Headless mobile SDK for Android: Queues, channels, and chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-queues-channels-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless mobile SDK for Android: Queues, channels, and chat Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to make support entry points (queues and channels) available in your app, and how to drive the full chat lifecycle: starting, resuming, sending messages and attachments, indicating typing, redacting sensitive data, escalating to human agents, and ending the session.

## Before you begin

Set up the SDK. For more information, see [Headless mobile SDK for Android: Get started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-getting-started).

**Note:** For brevity, most samples in this series catch only `Exception`. The SDK also throws `NetworkError` and `ChatServiceError`, which extend `Error`, and `ChatNetworkError`, which extends `Throwable`. An error that no handler catches crashes your app. In production code, use the pattern in [Handling SDK errors in Headless mobile SDK for Android: Advanced topics, localization, and post-session flows](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-advanced-topics#handle-sdk-errors).

## Select queues and channels

  * A queue usually represents a support entry point, such as "Billing", "Technical Support", or "VIP Support".

  * Each queue can offer one or more of the following channels:

    * Chat

    * Instant call (voice)

    * Scheduled call

    * Email

    * External deflection links (links to your self-service pages or other channels)




Queues and channel availability are configured by administrators in the **Contact Center AI Platform Admin Portal**.

### How it looks in your app

In your app, a typical flow is:

  1. You add a support entry point in your app (for example, a **Help** tab or a **Contact Us** button).

  2. When the user taps it, you fetch the queue menu using the SDK and render your own menu UI.

  3. When the user chooses a queue, you inspect its available channels.

  4. Your app shows those channels to the user (for example, **Chat now** , **Call now** , **Schedule a call** , **Email us** , **Visit Help Center**).

  5. When the user selects a channel, you call the corresponding SDK API.




#### Fetch queue menus from the SDK

The SDK provides `queueMenuService` to fetch queue menus. The `get` method returns a `QueueMenuResult` containing the list of queues (`List<QueueMenu>`) and an `isDirectAccess` flag. You can either fetch the full menu tree or use a Direct Access Key to jump directly to a specific queue:
    
    
    import com.ccaiplatform.ccaikit.CCAI
    import com.ccaiplatform.ccaikit.models.response.queuemenu.QueueMenuResult
    import com.ccaiplatform.ccaikit.models.response.queuemenu.QueueMenu
    
    // Fetch the full queue menu tree
    val menuResult: QueueMenuResult? = CCAI.queueMenuService?.get()
    
    // Or fetch a specific queue using a Direct Access Key
    val menuResult: QueueMenuResult? = CCAI.queueMenuService?.get(key = "billing_vip")
    

The optional `key` parameter lets you bypass the full queue menu and jump the user directly to a specific queue. In the CCAI Platform platform, this is achieved with a direct access point (DAP).

A DAP can be configured by administrators in the CCAI Platform portal in the following way:

  1. Go to **Settings** > **Queue** > Select any queue from the menu structure.

  2. From the **Access Point** section, click + **Create direct access point**.

  3. Enter the key in the text form.

  4. Click **Save**.




#### `QueueMenu` data structure

Each `QueueMenu` contains:

Property | Type | Description  
---|---|---  
`id` | Int | The unique identifier for this queue.  
`name` | String? | The display name (for example, "Billing Support").  
`children` | List<QueueMenu> | Sub-menus (empty list if this is a leaf node).  
`channels` | Channels? | Available channels for this queue.  
`hidden` | Boolean | Whether this queue should be hidden from consumers (administrator configured).  
`position` | Int? | Server-defined display position - preserves administrator portal ordering.  
`settings` | List<QueueMenuSetting>? | Queue-level settings configured in the administrator portal.  
`redirectionExtra` | QueueMenuRedirection? | Automatic redirection metadata when configured (see Redirect and deflection).  
`deflectionFrom` | List<QueueMenuDeflection>? | The queues that deflected to this one. The platform returns this queue in their place, so a non-empty list explains a redirect that already happened (see [Deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-smart-actions#deflection_after_hours_and_over-capacity))  
  
The `Channels` data class has these properties:

Property | Type | Description  
---|---|---  
`chat` | ChatChannel? | Chat channel configuration (`null` if chat isn't available for this queue).  
`voiceCall` | VoiceCallChannel? | Voice call channel configuration (`null` if voice isn't available). Contains flags such as `scheduleEnabled` and recording preferences.  
`email` | EmailChannel? | Email channel configuration (`null` if email isn't available). Access the address using `channels.email?.email`.  
`externalDeflectionLink` | ExternalDeflectionLink? | External deflection link configuration (`null` if not available). Access the URL using the structured type's properties.  
  
#### `VoiceCallChannel` fields (capability and deflection metadata)
    
    
    // VoiceCallChannel.kt (simplified)
    data class VoiceCallChannel(
        val instantEnabled: Boolean,            // Live voice call allowed now
        val preSessionSmartAction: Boolean,     // Per-channel pre-session smart action flag
        val scheduleEnabled: Boolean,           // Scheduled calls supported
        val recordingOption: RecordingOption?,  // ALWAYS / NEVER / ASK_USER
        val voicemailReason: String?,
        val phoneNumber: String?,
        val scheduleDeflectionType: String?,
        val deflected: Boolean?,
        val deflectedReason: String?
    )
    

#### Implementation example
    
    
    fun showAvailableChannels(queueMenu: QueueMenu) {
        val channels = queueMenu.channels
    
        val voice = channels?.voiceCall
    
        // Show only what the platform enabled, and hide everything else so
        // nothing carries over from a previously selected queue
        chatButton.isVisible = channels?.chat?.enabled == true
        callButton.isVisible = voice != null && voice.instantEnabled && !voice.deflected
        scheduleButton.isVisible = voice?.scheduleEnabled == true
        emailButton.isVisible = channels?.email?.enabled == true
    
        // External deflection links: the enabled entries that have a URL
        val links = channels?.externalDeflectionLink
            ?.takeIf { it.enabled }
            ?.links.orEmpty()
            .filter { it.enabled && it.url != null }
        helpLinksButton.isVisible = links.isNotEmpty()
    }
    

#### Fetching wait times

You can also retrieve estimated wait times for a specific queue:
    
    
    // Fetch wait time for a specific queue
    val waitTime = CCAI.queueMenuService?.getWaitTimes(menuId = queueMenu.id)
    
    // waitTime contains:
    // - chat: estimated wait time for chat (in seconds)
    // - voiceCall: estimated wait time for voice call (in seconds)
    

**Note:** The `getWaitTimes` method returns a `QueueMenuWaitTimeResponse`. The exact structure and property names may vary; verify against the SDK's actual response when testing.

### Single-channel queues

If a queue offers only one channel (for example, email only), you can:

  * Skip the channel selection step and go straight to the appropriate UI.

  * Or you can still show the available channel explicitly if that makes more sense in your UX.




The SDK's configuration and metadata tells you which channels are allowed; your app decides **how** to show them.

### Redirect and deflection

Admins can configure a queue to redirect users instead of offering channels. When `QueueMenu.redirectionExtra` is set, act on it as soon as the user selects the queue:

  * `option` says what to do: PHONE, MESSAGE, URL, VOICEMAIL, QUEUE, SIP, or CONTACT.
  * `data` carries the value, such as the number to dial, the message to show, or the URL to open.



`QueueMenu.deflectionFrom` is different. When a queue deflects to another queue, the platform returns the destination queue in place of the one the user selected and lists the source queues in deflectionFrom. It explains a redirect that already happened; it isn't a set of options to offer.

After-hours and over-capacity deflection is reported per channel. For how to handle it, see [Headless Mobile SDK for Android: Smart Actions, Attachments, and Deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-smart-actions).

## Channels

In the Headless Mobile SDK, your CCAI Platform administrator portal acts as the source of truth for your support operations. Administrators configure which support channels (such as chat, voice, email, or helpful links) are available for different support queues (such as "Billing" or "Tech Support").

The SDK's job is to securely fetch this configuration and hand it to your app. Your app's job is to read that configuration and draw the appropriate user interface.

**Tip:** For several channels in a headless architecture, the SDK tells you what is allowed and provides the routing metadata (for example, enabled flags, email addresses, and deflection URLs). Your app is responsible for building the UI and calling the corresponding SDK service APIs for the selected channel.

### Inspecting available channels

**What the SDK provides:** A real-time snapshot of which support channels are active and available for the specific queue the user selected, respecting your portal's business hours and capacity limits.

**What you build:** The UI menu (buttons, lists, or cards) that displays these available options to the user.

**Implementation example:** The following Kotlin code takes the queue the user just tapped and inspects the `Channels` data class to see which channels are enabled. It then decides which buttons to show on the screen.
    
    
    // Assuming 'selectedMenu' is a QueueMenu returned by the SDK
    fun setupChannelMenu(selectedMenu: QueueMenu) {
        val channels = selectedMenu.channels
    
        if (channels.chat != null) {
            showChatNowButton()
        }
    
        if (channels.voiceCall != null) {
            showCallNowButton()
        }
    
        if (channels.email != null) {
            showEmailUsButton()
        }
    
        if (channels.externalDeflectionLink != null) {
            showHelpCenterLinks()
        }
    }
    

The following sections cover chat in detail. For voice, screen share, scheduled call, email, and external deflection links, see [Headless Mobile SDK for Android: Voice, Screen Share, Scheduled Call, and Email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice)

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
**Note:** Beyond these core methods, the `chatService` also provides smart action tracking (`notifySmartActionReceived`, `updateSmartActionStatus`), form handling (`fetchWebForm`, `getCustomFormDetails`, `submitCustomForm`), post-session management (`startPostSession`, `readyPostSession`), transcript download (`downloadChatTranscript`, `downloadChatTranscriptData`), and attachment download (`downloadMedia`). For complete method signatures and parameters, see the Headless Mobile SDK - Android API Reference.

### `ChatRequest` and `ChatResponse` data structures

The `ChatRequest` data class contains the configuration for starting a new chat:
    
    
    data class ChatRequest(
        val chat: Chat? = null,                 // The session configuration (always pass one)
        val isScreenShareable: Boolean? = null, // Optional: enable screen share for this session
        val isVerifiable: Boolean? = null       // Optional: allow verification smart actions
    )
    
    data class Chat(
        val menuId: Int,                    // Required: queue menu ID
        val lang: String? = "en",           // Optional: language code override (defaults to "en")
        val ticketId: String? = null,       // Optional: associate with existing ticket
        val greeting: String? = null,       // Optional: custom greeting message
        val customData: CustomData? = null, // Optional: structured custom data
        val displayOrderInAdapter: List<String>? = null,
        val directAccessKeyId: Int? = null, // Optional: from QueueMenuResult (Direct Access Point)
        val dapRequestId: String? = null    // Optional: from QueueMenuResult (Direct Access Point)
    )
    

After you start or resume a chat, the SDK delivers its `ChatResponse` on the `chatReceived` Flow (`start()` and `resumeChat()` return nothing). The properties you reference most in this guide include:

  * `id` \- the unique chat session identifier.

  * `status` \- the current chat status (queued, active, ended, etc.).

  * `agent` / `virtualAgent` \- the assigned human or virtual agent.

  * `postSessionRequired` \- whether a post-session virtual agent is configured for the session. Surveys and CSAT are signaled by `surveyEnabled` and `csatSetting`.

  * `redactionEnabled` \- whether automatic PII redaction is active for this session.


**Note:** `ChatResponse` contains 20 properties in total (including `providerType`, `region`, `allAgents`, `allVirtualAgents`, `menus`, `features`, `timeoutAt`, `statusText`, `providerChannelId`, `postSessionOptInRequired`, `postSessionTransferStatus`, `csatSetting`, `surveyEnabled`, and more). For the full data class definition, see the Headless Mobile SDK - Android API Reference.

### Start a chat session

**Warning:** Always call `getLastChatInProgress()` before starting a new chat. If an earlier session is still active (for example, the app was force-quit mid-conversation, or the user switched accounts), starting a second chat fails or produces undefined behavior. This check is especially critical when `userId` changes between sessions. These examples run it through `startOrResumeChat()`, defined in the Minimal example.

To start a chat session, use the `chatService` with a `ChatRequest` specifying the queue menu ID.

#### Minimal example
    
    
    import android.util.Log
    import androidx.lifecycle.lifecycleScope
    import com.ccaiplatform.ccaichat.chatService
    import com.ccaiplatform.ccaichat.model.Chat
    import com.ccaiplatform.ccaichat.model.ChatRequest
    import com.ccaiplatform.ccaikit.CCAI
    import com.ccaiplatform.ccaiscreenshare.screenShareService
    import kotlinx.coroutines.launch
    
    // If screen share is initialized, pass isScreenShareable for agent visibility
    val chatRequest = ChatRequest(
        chat = Chat(menuId = 123),
        isScreenShareable = CCAI.screenShareService != null
    )
    startOrResumeChat(chatRequest)
    
    // Resumes an earlier chat if there is one; otherwise starts a new one
    fun startOrResumeChat(chatRequest: ChatRequest) {
        lifecycleScope.launch {
            val chatService = CCAI.chatService ?: return@launch
            try {
                // Pre-flight check: resume an earlier chat instead of starting a second one
                val existing = chatService.getLastChatInProgress()
                if (existing != null) {
                    chatService.resumeChat(existing)
                    return@launch
                }
    
                chatService.start(chatRequest)
                // Chat started - navigate to your custom chat screen
            } catch (e: Exception) {
                Log.e("CCAI", "Failed to start chat: ${e.message}")
            }
        }
    }
    

If your app doesn't include the `CCAIScreenShare` module, remove the `screenShareService` import and the `isScreenShareable` argument.

#### With explicit language
    
    
    val chatRequest = ChatRequest(
        chat = Chat(menuId = 123, lang = "en")
    )
    startOrResumeChat(chatRequest) // Defined in the Minimal example
    

### Resume a chat session

Resume a previously established chat session using a `ChatResponse` object:
    
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.resumeChat(chat)
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to resume chat: ${e.message}")
        }
    }
    

### Chat queue management

You can put the current chat back in the queue (its status becomes queued) or check for existing in-progress chats:
    
    
    // Enqueue the current chat (automatically calls checkStatus() after enqueuing)
    lifecycleScope.launch {
        try {
            CCAI.chatService?.enqueueCurrentChat()
            Log.d("CCAI", "Chat enqueued successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to enqueue chat: ${e.message}")
        }
    }
    
    // Check for an existing in-progress chat
    lifecycleScope.launch {
        try {
            val chat = CCAI.chatService?.getLastChatInProgress()
            if (chat != null) {
                Log.d("CCAI", "Found ongoing chat: ${chat.id}")
            } else {
                Log.d("CCAI", "No ongoing chat found")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to get last chat: ${e.message}")
        }
    }
    
    // Retrieve previous chat history with pagination
    lifecycleScope.launch {
        try {
            val previousChats = CCAI.chatService?.getPreviousChats(currentPage = 1)
            if (previousChats != null) {
                Log.d("CCAI", "Found ${previousChats.messages.size} previous messages")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to get previous chats: ${e.message}")
        }
    }
    

### Send messages

The `sendMessage` method supports multiple message types through the `OutgoingMessageContent` sealed class:
    
    
    sealed class OutgoingMessageContent {
        data class Text(val content: String) : OutgoingMessageContent()
        data class Photos(
            val images: List<UploadableImage>,
            val smartAction: SmartAction? = null
        ) : OutgoingMessageContent()
        data class Videos(
            val video: UploadableVideo,
            val smartAction: SmartAction? = null
        ) : OutgoingMessageContent()
        data class FormComplete(
            val type: String? = null,
            val signature: String? = null,
            val data: FormCompleteEventData
        ) : OutgoingMessageContent()
        data class ScreenShare(
            val event: String,
            val detail: ScreenShareResponse? = null
        ) : OutgoingMessageContent()
    }
    

The `UploadableImage` and `UploadableVideo` types (in `com.ccaiplatform.ccaikit.models.smartaction`) wrap media for upload:
    
    
    data class UploadableImage(
        val data: ByteArray,       // The binary data of the image
        val mimeType: String,      // For example, "image/jpeg" or "image/png"
        val uri: Uri? = null       // Optional URI for display and local file reference
    )
    
    data class UploadableVideo(
        val uri: Uri,              // The file URI of the video
        val mimeType: String       // For example, "video/mp4"
    )
    

`Photos` takes a list of images; `Videos` takes a single video. Avoid holding large media assets in memory while the user is waiting in queue or while an upload is pending.

#### Usage examples
    
    
    // Send text message
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(OutgoingMessageContent.Text("Hello world"))
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send message: ${e.message}")
        }
    }
    
    // Send image message (read the file off the main thread)
    lifecycleScope.launch {
        try {
            val imageData = withContext(Dispatchers.IO) {
                requireNotNull(contentResolver.openInputStream(selectedImageUri)).use { it.readBytes() }
            }
            val images = listOf(
                UploadableImage(data = imageData, mimeType = "image/jpeg", uri = selectedImageUri)
            )
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.Photos(
                    images = images,
                    smartAction = null
                )
            )
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send image: ${e.message}")
        }
    }
    
    // Send video message (one video per message)
    val video = UploadableVideo(uri = selectedVideoUri, mimeType = "video/mp4")
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.Videos(
                    video = video,
                    smartAction = null
                )
            )
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send video: ${e.message}")
        }
    }
    
    // Send form completion event
    // Note: status is a nullable String: "success", "error", or "cancelled".
    val formCompleteData = FormCompleteEventData(
        smartActionId = 123,
        status = "success",
        timestamp = "2024-01-01T12:00:00Z",
        details = FormCompleteEventDetails(message = "Form submitted successfully")
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.FormComplete(data = formCompleteData)
            )
            Log.d("CCAI", "Form completion event sent")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send form completion: ${e.message}")
        }
    }
    

The `ScreenShare` message type is used to send screen sharing events and responses to the server. Available screen share events include:

  * `screenShareRequestedFromAgent` \- agent requested screen sharing

  * `screenShareRequestedFromEndUser` \- end user requested screen sharing

  * `screenShareCodeGenerated` \- screen share code was generated

  * `screenShareFailed` \- screen sharing failed

  * `screenShareStarted` \- screen sharing session started

  * `screenShareEnded` \- screen sharing session ended


**Note:** If redaction is enabled (via the `redactionEnabled` property in `ChatResponse`), sensitive information in plain text messages is automatically redacted before being sent to the agent. See Message redaction for details.

### Typing indicators and message previews

Update the typing status and send message previews while the user is typing:
    
    
    // Update typing indicator
    CCAI.chatService?.typing(true)   // Start typing
    CCAI.chatService?.typing(false)  // Stop typing
    
    // Send message preview
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessagePreview("Typing...")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send message preview: ${e.message}")
        }
    }
    
    // Example: Send preview as user types
    fun onTextChanged(text: String) {
        lifecycleScope.launch {
            try {
                CCAI.chatService?.sendMessagePreview(text)
            } catch (e: Exception) {
                Log.e("CCAI", "Failed to send preview: ${e.message}")
            }
        }
    }
    

### Message redaction

Automatic redaction of sensitive information (PII, credit card numbers, etc.) is supported for plain text chat messages and message previews.

**Redaction configuration:**

  * Controlled by the `redactionEnabled` property in `ChatResponse`.

  * Configured in the portal under **Settings** > **Chat Settings** > **Automatic Redaction**.

  * When enabled, sensitive data is automatically replaced with placeholders before being sent to agents.



    
    
    // Redaction is automatically handled, use sendMessage as usual
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.Text("My phone number is 4155553423")
            )
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send message: ${e.message}")
        }
    }
    

**Note:** Redaction only applies to plain text messages. Redaction is automatically enabled or disabled based on portal configuration. The redaction status is available in `ChatResponse` after starting or resuming a chat. Message previews with timestamps older than the last sent preview are automatically skipped.

### End and escalate chats
    
    
    // End the current chat session
    lifecycleScope.launch {
        try {
            CCAI.chatService?.endChat()
            Log.d("CCAI", "Chat ended successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to end chat: ${e.message}")
        }
    }
    
    // Escalate to a human agent
    lifecycleScope.launch {
        try {
            CCAI.chatService?.escalateToHumanAgent()
            Log.d("CCAI", "Chat escalated to human agent")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to escalate chat: ${e.message}")
        }
    }
    
    // Record the deflection channel the user chose for an existing escalation
    // (the escalation must already exist; start one with escalateToHumanAgent())
    val escalationOption = ChatEscalationOption(
        escalationId = 123,
        deflectionChannel = DeflectionChannel.Email
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.updateEscalation(option = escalationOption)
            Log.d("CCAI", "Escalation updated successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to update escalation: ${e.message}")
        }
    }
    
    // Check the current chat status
    lifecycleScope.launch {
        try {
            CCAI.chatService?.checkStatus()
            Log.d("CCAI", "Status check completed successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to check status: ${e.message}")
        }
    }
    

### Chat events

Send chat events to the server for tracking user interactions. `ChatEvent.payload` is a non-nullable `Map<String, String>` — both keys and values must be strings.
    
    
    val event = ChatEvent(
        name = "form_received",
        payload = mapOf("name" to "contact_form")
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendEvent(event)
            Log.d("CCAI", "Event sent successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send event: ${e.message}")
        }
    }
    

Common event use cases include form interactions ("form_received", "form_clicked"), smart action events ("smart_action_received", "smart_action_clicked"), and custom user interactions for analytics.

## Module-specific build considerations

Consider the following for a module-specific build.

### Minimum Sdk level

The `CCAIChatRed` and `CCAICallRed` media-layer modules require **min Sdk = 23** (Android 6.0). If your app declares a lower `minSdkVersion`, Gradle will fail to merge manifests. Raise your `min Sdk` to at least 23 in `app/build.gradle.kts`:
    
    
    android {
        defaultConfig {
            minSdk = 23
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
