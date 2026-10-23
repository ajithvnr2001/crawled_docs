---
url: https://developer.android.com/topic/performance/appstartup/setup-env/
title: Set up your environment for performance testing \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:05.841928+00:00
---

# Set up your environment for performance testing  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/appstartup/setup-env/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Set up your environment for performance testing Stay organized with collections  Save and categorize content based on your preferences. 

You can identify potential bottlenecks and improve overall app performance by recording device activity over a short period of time and [collecting traces of your app's startup period](https://developer.android.com/topic/performance/tracing). This page shows how to set up your environment for performance testing.

## Use the Macrobenchmark library

The [Macrobenchmark library](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) measures larger end-user interactions, such as startup, interacting with the UI, and animations. The library provides direct control over the performance environment you're testing. It lets you control compiling, starting, and stopping your app to directly measure precise app startup time. It also works to minimize the noise and differences between test runs.

## Use mid-range devices to identify potential performance issues

Test performance on each device type you care about. High-end devices with fast components can hide performance problems on earlier, slower, or low RAM devices. Lower-end devices can take longer to load data or run code, making it easier to identify bottlenecks. Optimizing performance for low-end devices usually also benefits optimization for high-end devices.

## Reduce noise

  * Network: test your apps or processes with strong and stable internet Wi-Fi speeds. If the app startup time includes a network request, note this as a place where variability might occur.
  * RAM usage: don't have any other apps running in the background of your device while testing app startup performance.
  * Battery: ensure your device is charged to avoid any hardware-specific low power performance throttling.



## Test on release builds

Use release builds to test performance. Debug builds are [unsuitable for performance debugging](https://developer.android.com/studio/profile/measuring-performance#apk-considerations), as they don't provide compilation optimization and significantly impact performance.

However, it's okay to use an unobfuscated release build to identify classes and operation names. Specifically, we recommend enabling [minify (R8)](https://developer.android.com/studio/build/shrink-code) and disabling obfuscation, with [`-dontobfuscate`](https://developer.android.com/studio/build/shrink-code#obfuscate) in the proguard file. It's easier to identify layouts, assets, and resources if the build is unobfuscated.

Make sure you include the [profileable](https://developer.android.com/guide/topics/manifest/profileable-element) flag in the manifest so that your custom events are visible in non-debuggable builds. This flag is available on Android 10 (API level 29) and later.

## Add custom traces to your app operations

Add [custom traces](https://developer.android.com/topic/performance/tracing/custom-events) within your app to make it easier to identify what operations are performed by your app compared to other libraries. This helps give you more context about what the app is doing at all times.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
