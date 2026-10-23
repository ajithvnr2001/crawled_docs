---
url: https://developer.android.com/studio/profile/sample-callstack/
title: Sample the callstack \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:05.256572+00:00
---

# Sample the callstack  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/profile/sample-callstack/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Sample the callstack Stay organized with collections  Save and categorize content based on your preferences. 

Callstacks are useful for identifying _CPU hot spots_ , or sections of code that take a long time to execute. Callstacks help you understand which part of the code has been executed, and why it was invoked.

**Note:** To sample the callstack, you must deploy your app to a device running Android 8.0 (API level 26) or higher.

## Callstack sample overview

To sample the callstack, [select the **Find CPU Hotspots (Callstack Sample)** task](https://developer.android.com/studio/profile#start-profiling) from the Android Studio Profiler **Home** tab. After the recording is parsed you see the following visuals:

![](https://developer.android.com/static/studio/images/profiler-callstack-sample.png)

To supplement the [**CPU Usage** and **Interactions** timelines](https://developer.android.com/studio/profile/cpu-profiler), the **Threads** section shows frames for every call that your app and the system makes. Here are some tips for navigating the callstack sample:

  * Expand the thread of interest and use [keyboard shortcuts](https://developer.android.com/studio/profile/cpu-profiler#ui-shortcuts) to navigate the stack frames. Click a stack frame to get details about the event and related calls in the **Analysis** pane.
  * To filter to certain types of stack frames, click **Collapse frames** and check the frame types you want to hide. Collapsing frames removes them from both the **Threads** and **Analysis** sections. Depending on your investigation, you might want to collapse frames from the Java virtual machine (for example `android::AndroidRuntime::start` and `art::{...}`), and the system kernel (for example `[kernel.kallsyms]+{offset}`). Usually this corresponds to collapsing frames related to `[kernel.kallsyms]`, `/apex/`, and `/system/*`.



![](https://developer.android.com/static/studio/images/profiler-callstack-frame-menu.png)

Because a Java/Kotlin program typically executes through a Java virtual machine, when Android Studio collects the callstack for a Java/Kotlin program, the callstack usually includes not just the Java/Kotlin code but also the native code required to run the program itself and for the program to talk with the system and hardware.

  * To jump to the source code associated with a stack frame, right-click the frame and click **Jump to source**.
  * To highlight the stack frame associated with an event in the event table, click the event.



For information about the other visuals, see [Record a system trace](https://developer.android.com/studio/profile/cpu-profiler) and the [chart glossary](https://developer.android.com/studio/profile/chart-glossary/flame-chart).

## Sample native code using the command line

Internally, Android Studio uses [simpleperf](https://developer.android.com/ndk/guides/simpleperf) to trace your app's native code. If you want to specify additional options for Simpleperf, such as sampling specific device CPUs or specifying sampling durations at a high accuracy, you can [use simpleperf from the command line](https://android.googlesource.com/platform/system/extras/+/master/simpleperf/doc/README.md).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
