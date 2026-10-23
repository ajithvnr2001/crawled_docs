---
url: https://developer.android.com/training/monitoring-device-state/docking-monitoring/
title: Determine and monitor the docking state and type \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:13.507477+00:00
---

# Determine and monitor the docking state and type  |  App quality  |  Android Developers

> Source: https://developer.android.com/training/monitoring-device-state/docking-monitoring/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Determine and monitor the docking state and type Stay organized with collections  Save and categorize content based on your preferences. 

Android-powered devices can be docked into different kinds of docks. These include car docks, home docks, and digital or analog docks. The dock state is typically closely linked to the charging state, as many docks provide power to docked devices.

Your app affects the phone's update rate in the dock state. You can increase the update frequency of a sports news app when it's in the desktop dock, or disable your updates completely if the device is car docked. Conversely, you can maximize your updates while car docked if your background service is updating traffic conditions.

The dock state is also broadcast as a sticky `[Intent](https://developer.android.com/reference/android/content/Intent)`, letting you query whether the device is docked and in which kind of dock if so.

## Determine the current docking state

The dock state details are included as an extra in a [sticky broadcast](https://developer.android.com/topic/security/risks/sticky-broadcast) of the `[ACTION_DOCK_EVENT](https://developer.android.com/reference/android/content/Intent#ACTION_DOCK_EVENT)` action. Because it's sticky, you can call `[registerReceiver()](https://developer.android.com/reference/android/content/Context#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter\))`, passing in `null` as the broadcast receiver. The following snippet shows how to complete this process:

### Kotlin
    
    
    val dockStatus: Intent? = IntentFilter(Intent.ACTION_DOCK_EVENT).let { ifilter ->
        context.registerReceiver(null, ifilter)
    }

### Java
    
    
    IntentFilter ifilter = new IntentFilter(Intent.ACTION_DOCK_EVENT);
    Intent dockStatus = context.registerReceiver(null, ifilter);

You can extract the current docking status from the `EXTRA_DOCK_STATE` extra:

### Kotlin
    
    
    val dockState: Int = dockStatus?.getIntExtra(EXTRA_DOCK_STATE, -1) ?: -1
    val isDocked: Boolean = dockState != Intent.EXTRA_DOCK_STATE_UNDOCKED

### Java
    
    
    int dockState -1;
    if (dockStatus != null) {
      dockState = dockStatus.getIntExtra(EXTRA_DOCK_STATE, -1);
    }
    boolean isDocked = dockState != Intent.EXTRA_DOCK_STATE_UNDOCKED;

## Determine the current dock type

If a device is docked, it can be docked in any of the following four different dock types:

  * Car
  * Desk
  * Low-End (Analog) desk
  * High-End (Digital) desk



The latter two options are only introduced in Android API level 11, so it's good practice to check for all three desk types when you are only interested in the type of dock rather than it being digital or analog specifically:

### Kotlin
    
    
    val isCar: Boolean = dockState == EXTRA_DOCK_STATE_CAR
    val isDesk: Boolean = dockState == EXTRA_DOCK_STATE_DESK
            || dockState == EXTRA_DOCK_STATE_LE_DESK
            || dockState == EXTRA_DOCK_STATE_HE_DESK

### Java
    
    
    boolean isCar = dockState == EXTRA_DOCK_STATE_CAR;
    boolean isDesk = dockState == EXTRA_DOCK_STATE_DESK ||
                     dockState == EXTRA_DOCK_STATE_LE_DESK ||
                     dockState == EXTRA_DOCK_STATE_HE_DESK;

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2024-01-03 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-01-03 UTC."],[],[]] 
