---
url: https://developer.android.com/games/optimize/adpf/
title: Optimize thermal and CPU performance with the Android Dynamic Performance Framework \u00a0|\u00a0 Android game development \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:35:02.213565+00:00
---

# Optimize thermal and CPU performance with the Android Dynamic Performance Framework  |  Android game development  |  Android Developers

> Source: https://developer.android.com/games/optimize/adpf/

  * [ Android Developers ](https://developer.android.com/)
  * [ Google Play ](https://developer.android.com/distribute)
  * [ Games dev center ](https://developer.android.com/games)
  * [ Guides ](https://developer.android.com/games/guides)



Send feedback 

#  Optimize thermal and CPU performance with the Android Dynamic Performance Framework Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to use the Android Dynamic Performance Framework (ADPF) to optimize games based on the dynamic thermal and CPU management features on Android. The focus is on games, but you can also use the features for other performance-intensive apps.

ADPF is a set of APIs that allow games and performance-intensive apps to interact more directly with power and thermal systems of Android devices. With these APIs, you can monitor the dynamic behavior on Android systems and optimize game performance at a sustainable level that doesn't overheat devices.

Mobile SoCs and Android have more dynamic performance behaviors than desktops and consoles. These behaviors include thermal state management, varying CPU clocks, and varying CPU core types. This combined with the increasingly diverse core topology of SoCs creates challenges when trying to ensure that your game can take advantage of this behavior without negatively impacting device performance. ADPF provides some of this information in order to make performance more predictable.

Here are the main ADPF features:

  * **Thermal API** : Monitor the thermal state of a device so that the application can proactively adjust workload before it becomes unsustainable.
  * **Game Mode API & Game State API**: Enable game play optimization by prioritizing performance or battery life characteristics, based on user's settings and game specific configurations.
  * **Fixed Performance Mode** : Enable fixed-performance mode on a device during benchmarking to get measurements that aren't altered by dynamic CPU clocking.
  * **Power Efficiency Mode** : Tells the session that the threads in Performance Hint Session can be safely scheduled to prefer power efficiency over performance. ([Available in Android 15](https://developer.android.com/reference/android/os/PerformanceHintManager.Session#setPreferPowerEfficiency\(boolean\)))



Send feedback 

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
