---
url: https://developer.android.com/training/wearables/wff/ambient/
title: Save power using ambient mode requirements \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:29.808782+00:00
---

# Save power using ambient mode requirements  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/ambient/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Save power using ambient mode requirements Stay organized with collections  Save and categorize content based on your preferences. 

All watch faces should have not only an interactive mode, but also ambient mode. The Wear OS App Quality guidelines specify that only [15% of pixels are illuminated in ambient mode](https://developer.android.com/docs/quality-guidelines/wear-app-quality#wff).

Typically, the watch spends much more time in ambient mode, and during this time, conserving power is a priority.

Well designed ambient displays contain only essential information, and they minimize the number of pixels that are illuminated.

The recommended approach for implementing a component that alters in appearance between ambient and interactive modes is to add two elements, each with a `Variant`. Adding this at the `Part*` or `Group` level makes it possible keep the number of `Variant` elements to a minimum.
    
    
    <Group name="logo_interactive" x="100" y="100" width="200" height="200">
        <!-- Hide these elements in ambient mode -->
        <Variant mode="AMBIENT" target="alpha" value="0" />
        <!-- Components to show in interactive mode -->
    </Group>
    <Group name="logo_ambient" x="100" y="100" width="200" height="200" alpha="0">
        <Variant mode="AMBIENT" target="alpha" value="255" />
        <!-- Components to show in ambient mode -->
    </Group>
    
    [watchface_ambient.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_ambient.xml#L20-L46)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
