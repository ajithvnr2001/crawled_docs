---
url: https://developer.android.com/training/cars/testing/emulator/configurable/
title: Test using the configurable emulator \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:17.073347+00:00
---

# Test using the configurable emulator  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/testing/emulator/configurable/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Test using the configurable emulator Stay organized with collections  Save and categorize content based on your preferences. 

To help emulate some of the configurations seen across OEMs, certain [hardware profiles](https://developer.android.com/training/cars/testing/emulator#bundled-profiles) support runtime configurability.

These configurations are implemented using [Runtime Resource Overlays](https://source.android.com/docs/core/runtime/rros) (RROs) and can be managed using the `adb shell cmd overlay` command.

Use the following commands to enable or disable a RRO:
    
    
    adb shell cmd overlay enable NAME
    adb shell cmd overlay disable NAME

## Modify system bar position

By default, the configurable emulator has two system bars – a status bar on the top of the screen and a navigation bar at the bottom of the screen. Though many cars share this layout, some don't. Some cars have their system bars on the horizontal sides of the screen instead of the vertical sides, which can break assumptions that you make when developing apps for mobile form factors. See [System bars, immersive mode, and edge-to-edge rendering](https://developer.android.com/training/cars/parked/automotive-os#bars-immersive-edge) for more details and technical guidance.

The following RROs can be used to modify the system bars:

  * `com.android.systemui.rro.bottom`
  * `com.android.systemui.rro.bottom.rounded`
  * `com.android.systemui.rro.left`
  * `com.android.systemui.rro.right`



## Emulate display cutouts

Some cars have screens with display cutouts that are very different when compared to those seen on mobile devices. Instead of the notches or pinhole camera cutouts, some Android Automotive OS vehicles have curved screens that make the screen non-rectangular. See [Adapt to irregularly shaped displays](https://developer.android.com/training/cars/parked/automotive-os#irregular-displays) for more details and technical guidance.

The following RROs can be used to emulate display cutouts:

  * `com.android.internal.display.cutout.emulation.top_and_right`
  * `com.android.internal.display.cutout.emulation.free_form`
  * `com.android.internal.emulation.automotive_ultrawide_cutout`



## Recommended testing configurations

Because you can create many configurations by combining these RROs, we recommend that you test your app using the following combinations of [hardware profiles](https://developer.android.com/training/cars/testing/emulator#bundled-profiles) and RROs. These combinations are similar to some vehicles on the road today.

  * _Automotive (1080p landscape)_ with `com.android.systemui.rro.left` or `com.android.systemui.rro.right`
  * _Automotive Ultrawide_ with `com.android.systemui.rro.left` and `com.android.internal.emulation.automotive_ultrawide_cutout`



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
