---
url: https://developer.android.com/guide/navigation/navigation-event/
title: Navigation Event \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:47.676319+00:00
---

# Navigation Event  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/navigation/navigation-event/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Navigation Event Stay organized with collections  Save and categorize content based on your preferences. 

Navigation Event is a library that provides a Kotlin Multiplatform (KMP) solution for integrating system-level navigation events into your application. It is designed to be the foundational layer for handling navigation directions across various [supported platforms](https://developer.android.com/kotlin/multiplatform#kotlin-multiplatform-and-jetpack-libraries).

## Key concepts

The Navigation Event system is built around a centralized dispatcher-handler model, often used in a parent-child hierarchy to map to complex UI structures, such as those found in Jetpack Compose.

### `NavigationEventDispatcher`

The [`NavigationEventDispatcher`](https://developer.android.com/reference/kotlin/androidx/navigationevent/NavigationEventDispatcher) is the central class responsible for managing all registered navigation event consumers ([`NavigationEventHandler`](https://developer.android.com/reference/kotlin/androidx/navigationevent/NavigationEventHandler)) and orchestrating the flow of events.

In a hierarchical setup, all dispatchers within the same chain share a single `NavigationEventProcessor`, which manages the global state and ensures a single, unified dispatching order across the entire tree.

### `NavigationEventHandler`

`NavigationEventHandler` is an abstract class that receives and handles navigation events dispatched by a `NavigationEventDispatcher`. It defines callback methods that correspond to different stages of a navigation gesture lifecycle, such as when a gesture starts, progresses, completes, or is cancelled.

Handlers can respond to these events to update UI or application state in response to user navigation actions. Multiple handlers can be registered with a dispatcher and are invoked based on priority and registration order.

### `NavigationEvent`

[`NavigationEvent`](https://developer.android.com/reference/androidx/navigationevent/NavigationEvent) is a data class that carries the details of the navigation gesture.

### `NavigationEventInfo`

[`NavigationEventInfo`](https://developer.android.com/reference/androidx/navigationevent/NavigationEventInfo) is an abstract class that provides contextual information about a navigation state.

### `NavigationEventInput`

[`NavigationEventInput`](https://developer.android.com/reference/androidx/navigationevent/NavigationEventInput) is an abstract class for components that generate and dispatch navigation events. It acts as the "input" side of the navigation system, translating platform-specific events (like system back gestures or button clicks) into standardized events that can be sent to a `NavigationEventDispatcher`.

## Supported navigation directions and triggers

The Navigation Event system is designed to encompass more than just the system back button, with designs supporting multiple navigation directions and input methods across platforms.

### Supported directions

Different platforms support varying navigation directions:

**Platform** | **Back** | **Up** | **Forward** | **Home**  
---|---|---|---|---  
**Android phone** | ✅ | ✅ | 🚫 | ✅  
**Android tablet** | ✅ | ✅ | 🚫 | ✅  
**Web (Browser)** | ✅ | ✅ | ✅ | 🚫  
**iOS (iPhone/iPad)** | ✅ | 🚫 | ✅ | ✅  
  
### Supported triggers

Input handling is achieved through various mechanisms on each platform:

**Trigger** | **Android Phone** | **Web (Browser)** | **iOS (iPhone/iPad)**  
---|---|---|---  
**Keyboard back button** | ✅ Back | ❓ | ✅ Back  
**Software back button** | 🚫 | ✅ Back | ✅ Back  
**Software up button** | ✅ Up | 🚫 | 🚫  
**Gesture from left** | ✅ Back | ❓ | ✅ Back  
**Gesture from right** | ✅ Back | ❓ | ✅ Forward  
**Gesture from bottom** | ✅ Home | 🚫 | ✅ Home  
**Note:** The **Web** platform has unique navigation handling, where the browser controls the back stack state. This requires synchronization between the browser window and the application's navigation stack. The question mark represents behavior that is inconsistent because web browsers don't have a single, unified "back" button or gesture.

[ Next Set up development environment  arrow_forward  ](https://developer.android.com/guide/navigation/navigation-event/setup)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
