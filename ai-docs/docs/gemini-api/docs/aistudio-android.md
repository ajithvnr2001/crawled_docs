---
url: https://ai.google.dev/gemini-api/docs/aistudio-android/
title: Build Android apps in Google AI Studio
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:44.593513+00:00
---

# Build Android apps in Google AI Studio

> Source: https://ai.google.dev/gemini-api/docs/aistudio-android/

Google AI Studio lets you build native Android apps from a natural language prompt. Describe the app you want, and the [Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode#antigravity-agent) generates a complete Kotlin and [Jetpack Compose](https://developer.android.com/develop/ui/compose) project. From your browser, you can preview your app in a browser-based Android emulator, install it on a physical device, and publish it for testing.

Android apps also support Firebase integration for calling Gemini models with Firebase AI Logic and App Check, storing data in Cloud Firestore, and signing in users with Firebase Authentication.

## Get started

To start building an Android app:

  1. Go to [Build mode](https://aistudio.google.com/apps) in Google AI Studio using the left-hand navigation panel.
  2. Select **Android** from the platform picker.
  3. Enter a prompt describing the app you want to build (for example, _"Create a daily task tracker with local storage"_ or _"Build a recipe app that uses AI to suggest meals from ingredients"_).
  4. The agent generates the project and launches it in the browser-based Android emulator.



You can then iterate on your app using the chat panel, just like the web experience. The agent manages all files in your Android project and propagates changes across the codebase.

## Firebase integration

Google AI Studio integrates with [Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration) so your Android app can call Gemini models securely, persist data, and authenticate users without a custom server-side backend. When you prompt the agent to build features that require generative AI, a database, or sign-in, it can automatically provision and configure the following services in your Firebase project:

  * **[Firebase AI Logic](https://firebase.google.com/docs/ai-logic) and [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check)**: Call Gemini models directly from your Android app without embedding raw API keys in the APK. AI Studio automatically configures App Check to verify that requests originate from an authentic instance of your app: 
    * **Testing and sharing (debug builds)** : Uses an App Check debug token managed automatically by AI Studio when previewing in the browser-based emulator, installing over USB, or sharing with testers.
    * **Publishing to Google Play (release builds)** : Automatically switches to reCAPTCHA Enterprise using a pre-configured site key when building a release version for Google Play.
  * **Cloud Firestore** : Store and sync data in a NoSQL cloud database, including automatically generated Firestore Security Rules (`firestore.rules`).
  * **Firebase Authentication** : Add "Sign in with Google" flows to authenticate users.



You can enable Firebase from the setup card that appears in chat when you request these features, or at any time under **Settings > Integrations**. For details on project setup, shared quotas, and the App Check lifecycle, see [Add Firebase to your Google AI Studio app](https://firebase.google.com/docs/ai-assistance/ai-studio-integration).

## Browser-based Android emulator

The Android emulator runs entirely in the cloud and streams to your browser. You don't need to install the Android SDK, Android Studio, or a local emulator.

The emulator provides:

  * **Pixel-like device simulation** : tap, scroll, and interact with your app just like on a real device.
  * **Rotation support** : toggle between portrait and landscape orientation.
  * **Live preview** : when the agent makes code changes, the app rebuilds and the emulator refreshes automatically.



### Emulator limitations

The browser-based emulator doesn't support all hardware features. The following are not available in the emulator:

  * Camera and photo capture
  * NFC and Bluetooth
  * GPS (location is simulated)
  * Google Play services (Google Sign-In, Maps, and other Play services features work on a real device but not in the emulator)



## Install on a device with ADB

You can install the built APK directly on a physical Android device connected to your computer using USB. This uses [WebUSB](https://developer.chrome.com/docs/capabilities/usb) to communicate with your device through the browser. No local ADB installation is required.

### Prerequisites

  * A Chrome or Edge browser that supports WebUSB.
  * An Android device with [Developer Options and USB Debugging](https://developer.android.com/studio/debug/dev-options) enabled.
  * A USB cable connecting your device to your computer.



### Install the app on your device

  1. Click **Install on Device** in the preview panel.
  2. Select your Android device from the browser's USB device picker.
  3. The APK is transferred and installed on your device.
  4. The app launches automatically.



## Publish to the Play Store

You can publish your Android app to the [Google Play Console](https://play.google.com/console) internal testing track, which lets you distribute the app to up to 100 testers.

### Prerequisites

  * A [Google Play Developer account](https://play.google.com/console/signup) (requires a one-time $25 registration fee).
  * A completed developer profile in the Play Console.



### Publish your app

  1. Open **Settings > Publish** in Google AI Studio.
  2. Click **Publish to Play Store**.
  3. Authenticate with your Google Play Developer account.
  4. AI Studio signs the APK, creates the app listing (or uploads a new version), and publishes to the internal testing track.
  5. You receive a link to share with your testers.



AI Studio manages APK signing automatically using a managed keystore. You can customize the app listing (icon, screenshots, description) later in the Play Console.

## What's generated

When you build an Android app, the agent generates a standard Gradle-based project with the following structure:

  * **Build configuration** : `build.gradle.kts` files (project and app level) using Kotlin DSL.
  * **UI layer** : [Jetpack Compose](https://developer.android.com/develop/ui/compose) components with [Material 3](https://m3.material.io/) theming.
  * **Architecture** : single-activity architecture with ViewModels and data classes.
  * **Resources** : `AndroidManifest.xml`, drawables, strings, and other Android resources.
  * **Firebase configuration** (when Firebase is enabled): `google-services.json`, `firebase_applet_config.xml`, and `firestore.rules`.



The agent automatically manages Gradle dependencies, adding packages from Maven and Google repositories as needed.

You can view and edit the generated code using the **Code** tab in the preview panel. To continue development in Android Studio, download the project as a **ZIP file**.

## Limitations

Android app building in AI Studio has the following limitations:

### Platform limitations

  * **Client-side only** : Android apps don't include a server-side component. Features requiring a server runtime (secrets management, multiplayer, Google Workspace APIs) are not available.
  * **Single-activity architecture** : only single-activity, single-module projects are supported.
  * **Jetpack Compose only** : apps use Kotlin and Jetpack Compose. Java and XML layouts are not supported.
  * **No NDK or native code** : C and C++ code is not supported.
  * **No Wear OS or Android TV** : only phone and tablet form factors are supported.



### Export limitations

  * **ZIP download only** : you can download the project as a ZIP file. GitHub export is not yet available for Android projects.



## What's next

  * [Build apps in Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode)
  * [Developing Full-Stack Apps](https://ai.google.dev/gemini-api/docs/aistudio-fullstack) (web)
  * See examples in the [App Gallery](https://aistudio.google.com/apps?source=showcase).


