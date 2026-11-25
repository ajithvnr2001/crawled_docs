---
url: https://docs.fish.audio/agents/deploy/android/
title: Voice Agents Android SDK - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-25T18:05:12.036791+00:00
---

# Voice Agents Android SDK - Fish Audio

> Source: https://docs.fish.audio/agents/deploy/android/

## On this page

Back to top

  * Requirements
  * Install
  * Quick start
  * The microphone permission
  * Start a session
    * From your backend (recommended)
    * Public agent
  * Conversation
    * Events
    * One call per app
    * Threads
    * Compatibility
    * What is left out
  * Client tools
  * Background calls
  * Troubleshooting
  * Going further



Deploy

# Voice Agents Android SDK

Copy pageCopy page

Add voice calls with your agent to a native Android app in Kotlin with the agent-android-core library

Copy pageCopy page

The `agent-android-core` library adds voice calls with your agent to a native Android app, in Kotlin. It behaves like the [Web SDK](https://docs.fish.audio/agents/deploy/web-sdk) and the [React Native SDK](https://docs.fish.audio/agents/deploy/react-native): the same session options, events, error codes, and end reasons. On top of the call, it handles what a phone needs:

  * A foreground service that keeps the microphone running while your app is in the background
  * Audio routing (loudspeaker, earpiece, headsets)
  * A helper to ask for the microphone permission

It has no UI. You build the screen, and the SDK gives you the state to show.

Calls, the microphone, audio routes, reconnection, and calls in the background and with the screen locked were checked on a Pixel 8. Headsets, phone-call interruptions, and moving between Wi-Fi and cellular have not been checked yet.

## Authenticated sessions

Create session tokens on your backend.

## Web SDK reference

Events, session options, and error codes.

## Source and example app

The library and a one-screen example.

## Requirements

  * **Android 7.0 (API 24) or later.** Built against API 36.
  * **Kotlin 2.1 or newer** in the app’s build. The SDK is compiled with Kotlin 2.2, which older compilers cannot read.
  * **Kotlin coroutines.** State is exposed as `StateFlow`, events as `SharedFlow`.
  * **Your own backend** to create session tokens, or a public agent. Never ship an API key inside an app.
  * **Tested with** `io.livekit:livekit-android` 2.30.0, Android Gradle Plugin 9.2, and Gradle 9.4, on a Pixel 8 with Android 17 and an Android 16 emulator. Other versions may work but are untested.



## Install

The SDK is built on LiveKit, and one of LiveKit’s dependencies is only published on JitPack. Add JitPack to the repositories in `settings.gradle.kts`:

settings.gradle.kts
    
    
    dependencyResolutionManagement {
        repositories {
            google()
            mavenCentral()
            maven("https://jitpack.io")
        }
    }
    

Then add the SDK to your app module:

build.gradle.kts
    
    
    dependencies {
        implementation("com.fishaudio.agent:agent-android-core:1.0.0")
    }
    

The SDK’s manifest is merged into your app. It adds the permissions a call needs (`INTERNET`, `RECORD_AUDIO`, `MODIFY_AUDIO_SETTINGS`, `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_MICROPHONE`, `POST_NOTIFICATIONS`) and the call service, `com.fishaudio.agent.FishCallService`. Release builds need no extra R8 rules. LiveKit’s own manifest also declares the camera permission and a screen capture service, for video calls. The SDK takes both out again: a voice call uses neither, and the camera permission would hide your app from devices without a camera on Google Play. If your app uses the camera, declare `CAMERA` in its own manifest as usual; that declaration is kept.

## Quick start

Keep the `Conversation` somewhere that outlives an Activity instance. Android recreates an Activity when the device rotates and at other configuration changes; a `Conversation` that is closed in `onDestroy` ends the call each time.

CallViewModel.kt
    
    
    class CallViewModel(application: Application) : AndroidViewModel(application) {
        val conversation = Conversation(application)
    
        override fun onCleared() = conversation.close()
    }
    

Start the call from an Activity or a composable’s click handler:
    
    
    lifecycleScope.launch {
        // The SDK does not ask for the microphone permission. Ask first.
        if (!FishAgentPermissions.requestMicrophonePermission(activity)) return@launch
        try {
            val token = SessionToken.fromJson(fetchTokenFromYourBackend())
            viewModel.conversation.startSession(SessionAuth.Token(token))
        } catch (_: ConversationStartCancelledException) {
            // The user hung up while the call was starting.
        } catch (error: FishAgentException) {
            showError(error.code, error.message)
        }
    }
    

Show the call from the flows:
    
    
    conversation.status.collect { status -> /* IDLE, CONNECTING, CONNECTED, RECONNECTING, ENDED */ }
    conversation.mode.collect { mode -> /* LISTENING, THINKING, SPEAKING */ }
    conversation.messages.collect { messages -> /* the chat log, streaming entries included */ }
    

Hang up with `conversation.endSession()`. The [example app](https://github.com/fishaudio/fish-agent-android/tree/main/example) is one screen that does all of this.

## The microphone permission

`startSession` checks `RECORD_AUDIO` and does not ask for it: a permission dialog has to come from an Activity, and the SDK does not own one. Without the permission, a call that uses the microphone fails with `mic_permission_denied` before any session is created. `FishAgentPermissions.requestMicrophonePermission(activity)` shows the system dialog if needed and returns whether your app holds the permission. You can call it at any time while the Activity is started, for example from a click handler. It needs a `ComponentActivity` (`AppCompatActivity` and Compose activities are). If the Activity is destroyed while the dialog is showing (a rotation, for example), the answer cannot reach the call: it returns whether the permission is held at that moment, usually `false`. Ask again, or check `hasMicrophonePermission` when the new Activity starts. This is one step more than the React Native SDK, whose `startSession` asks by itself.

## Start a session

An app starts a call in one of two ways, the same two the browser SDKs offer.

### From your backend (recommended)

When the user starts a call, the app asks your backend for a session token. The backend calls `POST /v1/agent/sessions` with your API key and returns the response unchanged. The endpoint is the same one web apps use; see [Authenticated sessions](https://docs.fish.audio/agents/deploy/authenticated-sessions) for backend examples. Pass the response body to the SDK without picking fields out of it:
    
    
    val token = SessionToken.fromJson(responseBody)
    conversation.startSession(SessionAuth.Token(token))
    

During development, `localhost` is the phone, not your computer. On an emulator your computer is `10.0.2.2`. On a phone, use your computer’s LAN address or forward the port with `adb reverse tcp:3001 tcp:3001`.

### Public agent

An agent with [public access](https://docs.fish.audio/agents/deploy/public-agents) turned on takes sessions with just its id, with no API key and no backend:
    
    
    conversation.startSession(SessionAuth.AgentId("YOUR_AGENT_ID"))
    

If the agent has **Restrict origins** on, the platform checks the request’s `Origin` header against the agent’s allowed origins. An app sends none, so pass one that is on the list:
    
    
    @OptIn(ExperimentalFishAgentApi::class)
    suspend fun startRestrictedCall() {
        conversation.startSession(SessionAuth.AgentId("YOUR_AGENT_ID")) {
            origin = "https://www.example.com"
        }
    }
    

Without it, a restricted agent answers `origin_forbidden`.

The `origin` option is experimental and may change in a minor release: a dedicated way for apps to identify themselves may replace it. It is marked `@ExperimentalFishAgentApi`, and code that uses it does not compile without `@OptIn(ExperimentalFishAgentApi::class)`.

Anyone with the agent id can start sessions, billed to you. For a production app, especially one with signed-in users, prefer your backend: it decides who gets a token and can attribute sessions to your users. The React Native page says more about [what a public agent exposes](https://docs.fish.audio/agents/deploy/react-native#public-agent); all of it applies here.

## `Conversation`

One object for your app’s calls. It can make any number of calls, one at a time.
    
    
    Conversation(context, defaults = SessionOptions(), options = ConversationOptions())
    

Member| Description  
---|---  
`status: StateFlow<ConversationStatus>`| `IDLE` before the first call and after a failed start. Stays `ENDED` after a call until the next one starts  
`mode: StateFlow<AgentMode>`| What the agent is doing: `LISTENING`, `THINKING`, or `SPEAKING`  
`micMuted: StateFlow<Boolean>`| Whether the microphone is muted  
`audioOutput: StateFlow<AudioOutputRoute>`| The route that was asked for, not the device audio is playing on  
`messages: StateFlow<List<ChatMessage>>`| The chat log of the current call, streaming entries included (`isFinal` is false while one is streaming). It stays after the call and is emptied when the next call starts  
`endReason: StateFlow<EndReason?>`| Why the last call ended  
`events: SharedFlow<ConversationEvent>`| What happened. Nothing is replayed; see Events  
`sessionId`, `isSpeaking`| The id of the current or last call’s session, and whether `mode` is `SPEAKING`  
`transcript: List<TranscriptSegment>`| Every transcript segment of the current or last call, in conversation order. A snapshot: later segments are not added to it  
`suspend startSession(auth, configure)`| Starts a call. Returns the session id once connected  
`suspend endSession()`| Hangs up. Safe at any time  
`suspend setMicMuted(muted)`| Mutes or unmutes the microphone  
`sendUserMessage(text, audio = false)`| Sends a typed message. The agent answers in text only unless `audio` is true  
`sendUserActivity()`, `interrupt()`| Tells the agent the user is active (typing, for example), or stops the agent’s current reply  
`setAudioOutput(route)`| `AUTO`, `SPEAKER`, or `EARPIECE`, during a call or before one  
`registerClientTool(name, handler)`| Registers a client tool for the current call and every later one  
`close()`| Ends the call and releases the conversation  
  
`SessionOptions` has the same fields as the Web SDK’s [session options](https://docs.fish.audio/agents/deploy/web-sdk#options): `origin`, `serverUrl`, `language`, `timezone`, `context`, `overrides`, `dynamicVariables`, `endUserId`, `metadata`, `toolEvents`, `clientTools`, `clientToolTimeout`, and `microphone`. `clientToolTimeout` is a `kotlin.time.Duration` (`15.seconds` by default) where the Web SDK counts milliseconds. `ConversationOptions` holds what the phone needs around calls: `audioOutput` (an `AudioOutputRoute`, in the package `com.fishaudio.agent.audio`) and `callNotification`. Options are built in a block, and a call can adjust the conversation’s defaults the same way:
    
    
    val conversation = Conversation(
        context,
        defaults = SessionOptions { language = "ja" },
        options = ConversationOptions { audioOutput = AudioOutputRoute.SPEAKER },
    )
    
    conversation.startSession(auth) { microphone = false }
    

Inside a block, a name is the option. When a variable of yours has the same name, write `this.origin = origin`. A nested block (`overrides = SessionOverrides { … }`) sets only its own options, and naming one of the outer block there does not compile. The same rules as the other SDKs apply:

  * A second `startSession` while one is on its way, or during a live call, joins that call.
  * `endSession` during a start stops it where it is, before the microphone is captured if the call had not got that far: `startSession` throws `ConversationStartCancelledException`, and the session, if one was created, is closed.
  * A failed start puts `status` back to `IDLE`.
  * `sendUserMessage`, `sendUserActivity`, and `interrupt` do nothing when there is no call.
  * The start belongs to the conversation. Cancelling the coroutine that called `startSession` stops the wait, not the call. Call `endSession` to hang up.



### Events

`events` carries the same events as the Web SDK’s [event reference](https://docs.fish.audio/agents/deploy/web-sdk#events), as subclasses of `ConversationEvent`. It replays nothing: an event emitted before you started collecting is gone, so read state from the flows. A collector that falls more than 256 events behind loses the oldest ones.

### One call per app

Only one call can run in a process at a time, whichever `Conversation` makes it. A second conversation’s `startSession` throws `IllegalStateException` until the first call has ended. The call service and the audio session are shared by the whole process.

### Threads

You can call the methods from any thread. The flows are updated on the main thread, and client tools run there. Move slow work in a tool to another dispatcher.

### Compatibility

Options are built in blocks and events are made only by the SDK, so a new option or a new field on an event does not break an app built against an older version. What can gain cases in a minor release is shaped so that your code already handles a case it does not know.

  * **Events.** `ConversationEvent` is not a sealed class, so a `when` over events has an `else` branch.
  * **End reasons, error codes, error stages, tool sources, and audio routes.** `EndReason`, `FishAgentErrorCode`, `FishAgentErrorStage`, `ToolCallSource`, and `AudioOutputRoute` are classes with constants, not enums. Compare with the constants (`reason == EndReason.USER_HANGUP`) and keep an `else` branch. Their `value` is the text the API and the other SDKs use (`"user_hangup"`), which is also how this page writes them.

`ConversationStatus`, `AgentMode`, and `MessageRole` are enums. They are closed sets, and a minor release adds no value to them, so a `when` over one of them needs no `else` branch.

### What is left out

As in the React Native SDK, the browser-only members are not there: `startAudio`, `setOutputVolume`, `setInputDevice`, `setOutputDevice`, audio levels, and the screen wake lock. There is also no `getRoom()`: no LiveKit type appears in the SDK’s API, so your app can move to a newer LiveKit 2.x without the SDK changing.

## Client tools

A [client tool](https://docs.fish.audio/agents/build/client-tools) is a suspending function from the arguments to a result:
    
    
    val conversation = Conversation(
        context,
        defaults = SessionOptions {
            clientTools = mapOf(
                "get_cart" to ClientToolHandler { params, _ ->
                    mapOf("items" to cart.items.size, "total" to cart.total)
                },
            )
        },
    )
    

Arguments and results are plain Kotlin values: `Map<String, Any?>`, `List<Any?>`, `String`, `Boolean`, `Long` or `Double`, and `null`. Returning `null` sends no result. Throwing reports a failure to the agent.

## Background calls

During a call with the microphone on, the SDK runs a foreground service with an ongoing notification. Without it, Android 14 and later silence your app’s microphone as soon as it leaves the foreground, and the agent hears nothing.

  * The service starts with the call and stops when the call ends, from either side.
  * A call started with `microphone = false` runs no service. The service starts on the first unmute.
  * Change the notification with `ConversationOptions { callNotification = CallNotification { title = "…"; text = "…"; smallIcon = R.drawable.ic_call; channelName = "…" } }`. Set it to `null` to run no service at all.
  * Give it a `smallIcon`: a flat, one-colour drawable. Without one the app’s launcher icon is used, which Android usually shows as a plain square. `channelName` is what the user sees in the system’s notification settings; translate it.
  * The notification is only visible if your app holds `POST_NOTIFICATIONS` (Android 13 and later). The service works either way. Asking for that permission is up to your app.
  * Google Play asks apps that declare a microphone foreground service to describe its use in the Play Console.



## Troubleshooting

Symptom| Cause and fix  
---|---  
The build cannot find `com.github.davidliu:audioswitch`| JitPack is missing from the repositories. See Install  
`mic_permission_denied` from `startSession`| Your app does not hold `RECORD_AUDIO`. Call `FishAgentPermissions.requestMicrophonePermission` first  
`IllegalStateException`: another Conversation has a call in progress| Only one call runs per app. End the other call, or use one `Conversation` for the app  
A public agent fails with `origin_forbidden`| The agent restricts origins. Pass `origin`, matching one of its allowed origins exactly (scheme, host, and port)  
The token request fails on an emulator or phone| `localhost` is the device. Use `10.0.2.2` on an emulator, or your computer’s LAN address. Plain `http` also needs `android:usesCleartextTraffic="true"` during development  
The agent stops hearing the user in the background| The call service is not running: `callNotification` is `null`, or the service was refused because the call started while your app was in the background  
No call notification| Your app does not hold `POST_NOTIFICATIONS`. The service still runs  
The call ends when the phone rotates or the screen turns off| The `Conversation` is held by the Activity and closed in `onDestroy`. Hold it in a ViewModel  
  
## Going further

## React Native SDK

The same call in a React Native or Expo app.

## Client tools

Let the agent call functions in your app.

## Authenticated sessions

Create session tokens on your backend.

## Wire protocol

What the SDK speaks underneath.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/agents/deploy/android.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/agents/deploy/android)

[React Native Widget](https://docs.fish.audio/agents/deploy/react-native-widget)[Wire Protocol](https://docs.fish.audio/agents/deploy/protocol)
