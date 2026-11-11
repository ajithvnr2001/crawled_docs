---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started/
title: Headless Mobile SDK for iOS: Get started \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:59:08.885819+00:00
---

# Headless Mobile SDK for iOS: Get started  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless Mobile SDK for iOS: Get started Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to get started with the Headless Mobile SDK for iOS.

The Headless Mobile SDK for iOS lets you add CCAI Platform-powered support directly into your own built-in iOS experience without using a prebuilt CCAI Platform UI.

Instead of presenting a CCAI Platform-branded widget, you:

  * Integrate the CCAI iOS SDK into your app.

  * Build your own screens, navigation, and visual design.

  * Use the SDK to:

    * Start and manage chat and voice sessions.

    * Offer email, scheduled calls, and deflection options.

    * Support smart actions, attachments, and post-session flows (CSAT, surveys, virtual agent).




CCAI Platform handles the **contact center logic** (routing, queues, channels, configuration, reporting). You own the **entire app experience** (UI, flows, and branding).

If you prefer a **prebuilt configurable UI** instead of building your own, use the **Standard Mobile SDK**.

## Requirements

These are the requirements to integrate the Headless Mobile SDK for iOS.

### iOS platform requirements

  * **Minimum iOS version** : iOS 16.6 or later

  * **Language** : Swift

  * **IDE** : Latest stable Xcode version supported by your app

  * **Architectures** : Standard iOS architectures supported by your current Xcode toolchain.




### App permissions

Because your built-in app handles the UI for smart actions (capturing photos, recording videos, or verifying identity), you must declare Apple's mandatory privacy permissions.

**Warning:** If your app attempts to access the device's camera, microphone, or photo library without a corresponding purpose string in the `Info.plist`, iOS will instantly terminate the app.

Add the following keys to your `Info.plist` with a description of how your app uses the data:

  * `NSCameraUsageDescription`: Required for users to take and send photos/videos, or for agent-requested smart actions.

  * `NSMicrophoneUsageDescription`: Required for instant voice calls and for recording videos with sound.

  * `NSPhotoLibraryUsageDescription`: Required for users to upload existing photos or videos from their camera roll.

  * `NSFaceIDUsageDescription`: Required if you support biometric verification smart actions.




### CCAI Platform instance requirements

You need access to your CCAI Platform instance's **Developer settings** to obtain the following details:

  * Company key

  * Company secret code

  * Host URL - the hostname for the CCAI platform (for example, `your_subdomain.ccaiplatform.com`)




These values are used for:

  * **Company key + host URL** : In your iOS app to initialize the SDK.

  * **Company secret code** : In your backend to sign JSON Web Tokens (JWT) used to authenticate users.




### Push notifications

Push notifications are optional. Without them, chat (including smart actions the agent requests during a chat) and calls the user starts still work while your app is open. You need push notifications only for incoming calls (agent callbacks and scheduled calls), smart actions the agent requests during a call, and alerts about new agent messages and chat updates while your app is in the background or closed. For these, you need:

  * Apple Push Notification service (APNs) configuration for standard push notifications.

  * A VoIP Services certificate (if your app receives incoming calls).




You will:

  * Configure APNs in the Apple Developer portal, and VoIP credentials if your app receives incoming calls.

  * Upload the converted certificates in the CCAI Platform administrator portal under **Settings > Developer settings > Mobile app**.

  * Register for remote notifications in your app, and for VoIP pushes if your app receives incoming calls.

  * Forward the appropriate device tokens to the SDK.

  * In **Target > Signing & capabilities**, enable the capabilities for the features you use:

    * **Push notifications** capability.

    * **Background modes** capability with these items checked:

      * **Voice over IP** \- required for VoIP push notifications (incoming calls).

      * **Audio, AirPlay, and Picture in Picture** \- required for voice call audio to continue when the app is backgrounded.

      * **Remote notifications** \- required for standard APNs push delivery.




## How the headless iOS SDK fits into your app

The Headless Mobile SDK for iOS can be viewed as three layers:

### CCAI Platform platform and SDK

The SDK securely interacts with the CCAI Platform platform and provides:

  * Authentication using JSON Web Tokens (JWT).

  * Queue and channel routing metadata (chat, voice, scheduled call, email, external deflection links).

  * Real-time session state management.

  * The secure transport pipeline for smart actions, file attachments, and screen share.

  * Deflection logic and post-session hierarchy evaluation.




### Your iOS app (UI and logic is handled by you)

You control the entire visual and navigational experience:

  * **Entry points** : For example, a **Help** tab or **Contact us** button.

  * **Menus** : How you surface queues (for example, **Billing** , **Tech Support**).

  * **In-session UI** : Your custom chat bubbles, call screens, and controls.

  * **What your app does** : Calls SDK APIs to start and end sessions, listens for SDK events, and drives view controller navigation.




### CCAI Platform administrator portal configuration

Your CCAI Platform admins configure the rules of engagement (operating hours, available channels, wait time thresholds, and surveys). The SDK reads this configuration and exposes it to your app as raw data and events. You decide how to draw that configuration on the screen.

## Retrieve company credentials

Before you integrate the SDK, obtain the credentials from your CCAI Platform instance:

  1. Sign in to the CCAI Platform administrator portal with an administrator account.

  2. Navigate to **Settings > Developer settings**.

  3. Under **Company key & secret code**, copy:

     * Company key

     * Company secret code

  4. **Note your host URL** :the hostname for the CCAI platform (for example, `your_subdomain.ccaiplatform.com`).




You will use:

  * In your iOS app: Company key + host URL.

  * In your backend server: Company secret code to sign JWTs for:

    * End-user authentication.

    * Optional custom data or context used by CCAI Platform.




## Add the SDK to your iOS app

The Headless SDK v3 is built using a modular architecture. The `CCAIKit` package product includes every module: chat (`CCAIChat`), voice and scheduled calls (`CCAICall`), and screen share (`CCAIScreenShare`). If your app needs only one of those features, add that feature's product (`CCAIChat`, `CCAICall`, or `CCAIScreenShare`) instead of `CCAIKit`; each one includes the core SDK.

To integrate the iOS SDK in your app, follow the next sequence of steps.

### Option A: Swift Package Manager (recommended)

  1. Add the following to your `Package.swift` file:
         
         dependencies: [
             .package(url: "https://github.com/UJET/ccai-ios-sdk.git", from: "3.5.0")
         ],
         targets: [
             .target(
                 name: "YourTargetName",
                 dependencies: [
                     .product(name: "CCAIKit", package: "ccai-ios-sdk")
                 ]
             )
         ]
         

  2. Import `CCAIKit` in your `AppDelegate` file:
         
         import CCAIKit
         

  3. If your project is SwiftUI, declare `@UIApplicationDelegateAdaptor` in your `App` struct:
         
         @main
         struct YourAppName: App {
            @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
            // ...
         }
         




In Xcode, you can instead choose **File > Add Package Dependencies…**, enter `https://github.com/UJET/ccai-ios-sdk`, and add the `CCAIKit` product to your app target.

**Note:** If your project builds in Swift 6 language mode with strict concurrency checking, calls into the SDK can fail to compile with errors about non-`Sendable` types. In the files that call the SDK, import its modules with `@preconcurrency` (for example, `@preconcurrency import CCAIKit`).

Importing an SDK module doesn't make `Foundation` available. In each file, import the frameworks and SDK modules whose types or APIs the file uses: for example, `import Foundation` for `DispatchQueue`, `UUID`, or `Date`, and `import CCAIKit` for CCAI.

## Initialize the headless SDK

Initialize the SDK during app launch. Because of the SDK's modular architecture, you must initialize the core CCAI system first, and then register the specific service modules (such as chat or screen share).

### Basic initialization

The SDK uses an `InitOptions` struct that bundles all required configuration:
    
    
    import UIKit
    import CCAIKit
    import CCAIChat        // If using Chat
    import CCAICall        // If using voice or scheduled calls
    import CCAIScreenShare // If using Screen Share
    
    class AppDelegate: NSObject, UIApplicationDelegate, CCAIDelegate {
    
        func application(
            _ application: UIApplication,
            didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
        ) -> Bool {
    
            // 1. Configure initialization options
            let options = InitOptions(
                key: "YOUR_COMPANY_KEY",
                urlHost: "your_subdomain.ccaiplatform.com",
                delegate: self,
                cacheAuthToken: true       // Whether to cache the auth token (defaults to true)
            )
    
            // 2. Initialize the Core SDK
            do {
                try CCAI.shared.initialize(options: options)
            } catch {
                print("Failed to initialize CCAI: \(error.localizedDescription)")
                return true
            }
    
            // Optional: set the SDK language (ISO 639 code; defaults to "en")
            CCAI.shared.languageService?.languageCode = "en"
    
            // 3. Initialize Feature Modules
            // Chat - minimal (no options required)
            CCAI.shared.initializeChat()
    
            // Chat - with optional configuration
            // let chatOptions = ChatOptions(
            //     webFormHandler: { request in await presentWebForm(request) }, // Optional: render web forms in your own UI
            //     downloadTranscriptVisibility: .hideInPostChat // Hide the post-chat download affordance
            // )
            // To set a chat greeting, pass greeting: in the ChatRequest
            // CCAI.shared.initializeChat(chatOptions)
    
            // Voice (required whenever your app uses voice or scheduled calls)
            CCAI.shared.initializeCall()
    
            // Screen Share (optional)
            // let screenShareOptions = ScreenShareOptions(
            //     key: "YOUR_SCREEN_SHARE_LICENSE_KEY", // License Key (Settings > Developer Settings > Screen Share)
            //     domain: "https://your-screen-share-domain.example.com" // Optional: the Screen Share Domain URL
            // )
            // CCAI.shared.initializeScreenShare(screenShareOptions)
    
            return true
        }
    
        // ... CCAIDelegate methods (Authentication) go here ...
    }
    

#### `InitOptions` configuration reference
    
    
    public struct InitOptions {
        /// The company key used for authentication
        public let key: String
    
        /// The host URL for CCAI platform (for example, "my-unique-tenant.uc1.ccaiplatform.com")
        public let urlHost: String
    
        /// The delegate that handles authentication
        public var delegate: CCAIDelegate?
    
        /// Whether to cache the authentication token (defaults to true)
        public let cacheAuthToken: Bool
    }
    

**Note:** The SDK keeps a strong reference to your delegate, so you can pass a newly created object. To release it, set `CCAI.shared.delegate = nil` or call `CCAI.shared.clearDelegate()`.

### Available SDK services

After initialization, you can access various services through the `CCAI.shared` singleton:
    
    
    let authService = CCAI.shared.authService
    let companyService = CCAI.shared.companyService
    let queueMenuService = CCAI.shared.queueMenuService
    let languageService = CCAI.shared.languageService
    let pushNotificationService = CCAI.shared.pushNotificationService
    let endUserService = CCAI.shared.endUserService
    let chatService = CCAI.shared.chatService           // Only available after initializeChat()
    let screenShareService = CCAI.shared.screenShareService // Only available after initializeScreenShare()
    let callService = CCAI.shared.callService           // Only available after initializeCall()
    let rateService = CCAI.shared.rateService           // For CSAT ratings and survey submission
    let smartActionService = CCAI.shared.smartActionService // Dedicated service for smart action lifecycle
    

### Fetch company configuration

After initialization, fetch company-level configuration using the `companyService`. This is useful for populating language pickers, displaying the company name, or reading support contact details before the user enters a queue.
    
    
    do {
        let company = try await CCAI.shared.companyService?.get()
        print("Company: \(company?.displayName ?? "Unknown")")
    } catch {
        print("Failed to get company info: \(error)")
    }
    

**Tip:** The languages list returned by `companyService` reflects what your admins have enabled in the CCAI Platform administrator portal. Use it to build a language picker in your app's settings (see the _Languages and Localization_ section in the [Headless mobile SDK for iOS: advanced topics, localization, and post-session flows](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-advanced-topics) article).

## Authenticate end users

The Headless Mobile SDK uses JSON Web Tokens (JWT) to authenticate users and securely pass contextual information to the agent's CRM.

### How it works

The SDK uses a streamlined two-step async authentication flow:

  1. The SDK determines it needs to authenticate the user.

  2. It calls your `CCAIDelegate` method - `ccaiShouldAuthenticate()` \- which is an async function.

  3. Your app signs a JWT remotely on your backend server using your company secret code.

  4. Your app then passes the signed JWT to `CCAI.shared.authService?.authenticate(jwt)` to exchange it for an auth token.

  5. The auth token is returned to the SDK to complete the connection.


**Warning:** JWT signing must always be performed on your backend server. Never embed the company secret code inside your compiled iOS app, as this creates a severe security vulnerability.

### Implement the `CCAIDelegate` for authentication

Your app must implement the `CCAIDelegate` protocol. The SDK calls the single async delegate method when it needs authentication.

#### `CCAIDelegate` protocol
    
    
    public protocol CCAIDelegate: AnyObject {
        /// Authenticates the end user and returns an auth token
        func ccaiShouldAuthenticate() async -> String?
    }
    

#### Implementation example (Swift)
    
    
    class AppDelegate: CCAIDelegate {
        func ccaiShouldAuthenticate() async -> String? {
            // 1. Sign JWT remotely on your backend server
            guard let jwt = await signJWTRemotely() else { return nil }
    
            // 2. Authenticate JWT using authService to get an auth token
            return try? await CCAI.shared.authService?.authenticate(jwt)
        }
    }
    

### Pass custom data to the CRM

If you want to pass contextual data to the agent (for example, the user's current device OS, their location, or their account tier), your backend must inject a `custom_data` object into the JWT payload before signing it.

Each piece of custom data must be formatted as a JSON object containing a `label` (what the agent sees), a `value`, and a `type`.

#### Supported data types

  * `string`: Standard text (for example, "iPhone 14 Pro").

  * `number`: Integers or floats (for example, 1234 or 99.99).

  * `date`: A 13-digit UTC Unix timestamp including milliseconds (for example, 1537399655992).

  * `url`: Standard HTTP/HTTPS URL format.

  * `boolean`: Standard true or false value.


**Agent visibility:** You can optionally pass data to the CCAI Platform platform that is hidden from the human agent but available for routing or backend analytics. To do this, include `"invisible_to_agent": true` in the data object. 

### Reserved CRM keys

CCAI Platform supports specific reserved keys that trigger built-in behaviors in the platform, such as flagging a user as a VIP or warning an agent about a bad actor. These must be formatted as boolean types and are only accepted if the payload is signed using the secure JWT method.

  * `reserved_verified_customer`: Indicates whether a customer has been successfully authenticated by your internal systems.

  * `reserved_bad_actor`: Flags the user to the agent as a potential spammer or fraudulent account.

  * `reserved_repeat_customer`: Indicates whether this customer has frequently contacted support recently.




#### Example payload with reserved keys
    
    
    {
      "iat": 1537399656,
      "exp": 1537400256,
      "custom_data": {
        "reserved_verified_customer": {
          "label": "Verified Customer",
          "value": true,
          "type": "boolean"
        },
        "reserved_bad_actor": {
          "label": "Bad Actor",
          "value": false,
          "type": "boolean"
        },
        "reserved_repeat_customer": {
          "label": "Repeat Customer",
          "value": false,
          "type": "boolean"
        }
      }
    }
    

### Manage auth tokens

The SDK also provides methods to manually update or clear the cached authentication token:
    
    
    // Set a new auth token
    CCAI.shared.authService?.updateAuthToken("new_auth_token")
    
    // Clear the current token (for example, on user logout)
    CCAI.shared.authService?.updateAuthToken(nil)
    

**Warning:** When `cacheAuthToken` is `true` (the default in `InitOptions`), the SDK caches the auth token in the iOS Keychain so it can be reused across app launches without re-signing. The cached token is used until it expires or is explicitly cleared. Clear the cached token whenever user-related data changes - most importantly on sign-out events, user switching, or profile updates. Failing to do so can cause the SDK to authenticate the _previous_ user's session. Call `updateAuthToken(nil)` as part of your logout routine (see also the _Error handling, fallback, and session management_ section in the [Headless mobile SDK for iOS: advanced topics, localization, and post-session flows](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-advanced-topics) article).

### Custom data JWT payload schema

When your backend constructs the final payload to be signed with your company secret code, it must strictly follow this schema. Note the mandatory `iat` (issued at) and `exp` (expiration) timestamps.
    
    
    {
      "iat": 1537399656,
      "exp": 1537400256,
      "custom_data": {
        "os_version": {
          "label": "OS Version",
          "value": "16.4",
          "type": "string"
        },
        "membership_tier": {
          "label": "Membership Tier",
          "value": "Platinum",
          "type": "string"
        },
        "ssn_last_four": {
          "label": "SSN",
          "value": "1234",
          "type": "string",
          "invisible_to_agent": true
        },
        "reserved_verified_customer": {
          "label": "Verified Customer",
          "value": true,
          "type": "boolean"
        }
      }
    }
    

## Enable push notifications

The SDK uses push notifications for:

  * **Incoming calls** (agent callbacks and scheduled calls).

  * **Smart actions** the agent requests during a call.

  * **Alerts** about new agent messages and chat updates while your app is in the background or closed.


**Note:** Push notifications are optional. If your app doesn't need these features, you can skip this section.

### Configure certificates

CCAI Platform uses two types of Apple push certificates, saved in the CCAI Platform administrator portal:

  * An **Apple Push Notification service (APNs) SSL certificate** used for standard remote push notifications.

  * A **VoIP Services certificate** used for incoming calls. You need it only if your app receives incoming calls.




Both certificates are created in the **Apple Developer** portal, converted to PEM format, and then uploaded to the CCAI Platform administrator portal.

#### Create an APNs SSL certificate

Follow these next steps — based on Apple's official [Establishing a Certificate-Based Connection to APNs](https://developer.apple.com/documentation/usernotifications/establishing-a-certificate-based-connection-to-apns) guide — to create an APNs SSL certificate.

  1. Sign in to [developer.apple.com](http://developer.apple.com/) and navigate to **Certificates, Identifiers & Profiles**.

  2. Select the **+** button to create a new certificate.

  3. Under Services, select **Apple Push Notification service SSL (Sandbox & Production)**.

  4. Choose the App ID that matches your application's bundle identifier, then select **Continue**.

  5. Upload a Certificate Signing Request (CSR) generated from Keychain Access on your Mac:

     * Open **Keychain Access > Certificate Assistant > Request a Certificate From a Certificate Authority…**

     * Enter your email address, leave CA Email Address empty, select **Saved to disk** , and select **Continue**.

  6. Select **Continue** , then **Download** the generated `.cer` file.

  7. Double-click the `.cer` file to install it in your Keychain.

  8. In Keychain Access, locate the installed certificate, right-click it, and select **Export…** to save it as a `.p12` file. You are prompted to set an export password.

  9. Convert the `.p12` file to PEM format using `openssl`:
         
         # Extract the certificate
         openssl pkcs12 -in apns_certificate.p12 -out apns_cert.pem -clcerts -nokeys
         
         # Extract the private key
         openssl pkcs12 -in apns_certificate.p12 -out apns_key.pem -nocerts -nodes
         
         # (Optional) Combine into a single PEM file
         cat apns_cert.pem apns_key.pem > apns_combined.pem
         




#### Create a VoIP services certificate

VoIP services certificates allow your app to receive high-priority push notifications through Apple's [PushKit](https://developer.apple.com/documentation/PushKit) framework, which can wake your app from a terminated state to handle incoming calls. For the latest official steps, see [Create VoIP services certificates](https://developer.apple.com/help/account/certificates/create-voip-services-certificates/) in the Apple Developer documentation.

  1. Sign in to [developer.apple.com](http://developer.apple.com/) and navigate to **Certificates, Identifiers & Profiles**.

  2. Select the **+** button to create a new certificate.

  3. Under Services, select **VoIP Services Certificate**.

  4. Choose the App ID that matches your application's bundle identifier, then select **Continue**.

  5. Upload the same Certificate Signing Request (CSR) you generated for your APNs SSL certificate (or create a new one).

  6. Select **Continue** , then **Download** the generated `.cer` file.

  7. Double-click the `.cer` file to install it in your Keychain.

  8. In Keychain Access, locate the installed VoIP services certificate, right-click it, and select **Export…** to save it as a `.p12` file.

  9. Convert the `.p12` file to PEM format using `openssl`:
         
         # Extract the certificate
         openssl pkcs12 -in voip_certificate.p12 -out voip_cert.pem -clcerts -nokeys
         
         # Extract the private key
         openssl pkcs12 -in voip_certificate.p12 -out voip_key.pem -nocerts -nodes
         
         # (Optional) Combine into a single PEM file
         cat voip_cert.pem voip_key.pem > voip_combined.pem
         




#### Upload certificates to the CCAI Platform administrator portal

  1. Sign in to the CCAI Platform administrator portal.

  2. Navigate to **Settings > Developer Settings > Mobile App**.

  3. Upload the APNs PEM certificate.

  4. If your app receives incoming calls, upload the VoIP PEM certificate.


**Warning:** If a certificate you use is missing or expired, the push notifications that depend on it fail silently. The APNs certificate handles standard push delivery, including smart actions during a call, and the VoIP certificate handles incoming calls. Renew each certificate before it expires (Apple certificates are typically valid for one year).

### Request push notification permissions

The SDK provides a convenience method that requests notification permission and, if the user grants it, registers your app with APNs. If your app hasn't asked for notification permission by the time the first chat, instant call, or voicemail starts, the SDK asks then. To control when the prompt appears, request permission yourself earlier, for example during onboarding.

The method doesn't return the user's choice. To track it, subscribe to `grantStatusChanged` before you request permission. The publisher doesn't replay earlier values: it publishes `true` once the APNs device token reaches the SDK, and `false` if the user denies permission or registration fails, so a subscription made after the request can miss the answer.
    
    
    // 1. Subscribe first: grantStatusChanged doesn't replay earlier values
    CCAI.shared.pushNotificationService?.grantStatusChanged
        .receive(on: DispatchQueue.main)
        .sink { granted in
            print(granted ? "Push notifications enabled" : "Push notifications disabled")
        }
        .store(in: &cancellables)
    
    // 2. Then request permission and register with APNs
    let options: UNAuthorizationOptions = [.alert, .sound]
    try await CCAI.shared.pushNotificationService?.registerForPushNotifications(options: options)
    

### Register for remote notifications

Implement the push notification delegates in your `AppDelegate`. The SDK provides `pushNotificationService` for forwarding tokens:
    
    
    import CCAIKit
    
    class AppDelegate: NSObject, UIApplicationDelegate {
        func application(
            _ application: UIApplication,
            didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
        ) {
            CCAI.shared.pushNotificationService?.updatePushToken(
                data: deviceToken,
                type: .apns
            )
        }
    
        func application(
            _ application: UIApplication,
            didFailToRegisterForRemoteNotificationsWithError error: Error
        ) {
            CCAI.shared.pushNotificationService?.updatePushToken(
                data: nil,
                type: .apns
            )
        }
    }
    

Make sure to also enable **Capabilities > Push notifications** and **Background modes** for remote notifications from the **Target > Signing & capabilities** tab in Xcode.

### Handle incoming push notifications

When you receive a push payload, forward it to the SDK for processing:
    
    
    func application(
        _ application: UIApplication,
        didReceiveRemoteNotification userInfo: [AnyHashable: Any],
        fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
    ) {
        Task {
            // handlePushNotification is async, so call it from a Task
            await CCAI.shared.pushNotificationService?.handlePushNotification(userInfo)
            completionHandler(.newData)
        }
    }
    

The SDK processes payloads that CCAI Platform sent and publishes each one on a `pushNotificationService` publisher, such as `chatNotificationReceived`, `callNotificationReceived`, or `requestNotificationReceived`.

### Register for VoIP push notifications

For incoming calls, the SDK needs a VoIP push token. VoIP pushes are delivered with high priority and can wake your app from a terminated state. If your app doesn't receive incoming calls, skip this section.

**Step 1** : Import `PushKit`, `UIKit`, `CCAIKit`, and `CCAICall`, keep a `PKPushRegistry` in a property of your `AppDelegate`, and configure it in `didFinishLaunchingWithOptions`:
    
    
    import PushKit
    import UIKit
    import CCAIKit
    import CCAICall
    
    class AppDelegate: NSObject, UIApplicationDelegate, PKPushRegistryDelegate {
    
        // Keep a strong reference: a registry held only in a local constant is
        // released, and stops delivering VoIP tokens and pushes
        private let voipRegistry = PKPushRegistry(queue: .main)
    
        func application(
            _ application: UIApplication,
            didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
        ) -> Bool {
    
            // ... SDK initialization ...
    
            // Register for VoIP push notifications
            voipRegistry.delegate = self
            voipRegistry.desiredPushTypes = [.voIP]
    
            return true
        }
    }
    

**Step 2** : Implement the `PKPushRegistryDelegate` methods to forward VoIP tokens and payloads to the SDK:
    
    
    // MARK: - PKPushRegistryDelegate
    
    func pushRegistry(
        _ registry: PKPushRegistry,
        didUpdate credentials: PKPushCredentials,
        for type: PKPushType
    ) {
        guard type == .voIP else { return }
        // Forward the VoIP token to the SDK
        CCAI.shared.pushNotificationService?.updatePushToken(
            data: credentials.token,
            type: .voip
        )
    }
    
    func pushRegistry(
        _ registry: PKPushRegistry,
        didInvalidatePushTokenFor type: PKPushType
    ) {
        // Clear the VoIP token
        CCAI.shared.pushNotificationService?.updatePushToken(
            data: nil,
            type: .voip
        )
    }
    
    func pushRegistry(
        _ registry: PKPushRegistry,
        didReceiveIncomingPushWith payload: PKPushPayload,
        for type: PKPushType,
        completion: @escaping () -> Void
    ) {
        guard type == .voIP else {
            completion()
            return
        }
    
        // Forward the VoIP payload to the SDK using the `handleVoIPPush`
        // extension on `CCAI` (defined in the `CCAICall` module). The SDK
        // takes ownership of the call lifecycle; invoke PushKit's completion
        // handler in the trailing closure once the SDK has accepted the
        // payload.
        CCAI.shared.handleVoIPPush(payload: payload.dictionaryPayload) { completion() }
    }
    

`handleVoIPPush` also works on a cold start, before `CCAI.shared.initializeCall()` has run: the SDK reports the incoming call to CallKit right away and hands it to the call service once you initialize the call module.

**Note:** VoIP push notifications only work on physical devices — they are not supported in the iOS Simulator. Make sure your VoIP Services certificate is uploaded in the CCAI Platform administrator portal and that the **Voice over IP** background mode is enabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
