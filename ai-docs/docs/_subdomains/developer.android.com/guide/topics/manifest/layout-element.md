---
url: https://developer.android.com/guide/topics/manifest/layout-element/
title: <layout> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:21.537643+00:00
---

# <layout>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/layout-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <layout> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <layout android:defaultHeight="_integer_ "
              android:defaultWidth="_integer_ "
              android:gravity=["top" | "end" | ...]
              android:minHeight="_integer_ "
              android:minWidth="_integer_ " />

contained in:
    `[<activity>](https://developer.android.com/guide/topics/manifest/activity-element)`
description:
    Contains attributes that affect how an activity behaves in multi-window mode. 
attributes:
    

`android:defaultHeight`
    Default height of the activity when launched in free-form mode.
`android:defaultWidth`
    Default width of the activity when launched in free-form mode.
`android:gravity`
    Initial placement of the activity when launched in free-form mode. See `[Gravity](https://developer.android.com/reference/android/view/Gravity)` for suitable values.
`android:minHeight`
    Minimum height for the activity in both split-screen and free-form modes. If the user moves the divider in split-screen mode to make an activity smaller than the specified minimum, the system crops the activity to the height the user requests.
`android:minWidth`
    Minimum width for the activity in both split-screen and free-form modes. If the user moves the divider in split-screen mode to make an activity smaller than the specified minimum, the system crops the activity to the width the user requests.
introduced in:
    API Level 24
see also:
    `[<activity>](https://developer.android.com/guide/topics/manifest/activity-element)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
