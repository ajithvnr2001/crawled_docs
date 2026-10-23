---
url: https://developer.android.com/guide/topics/manifest/action-element/
title: <action> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:18.010237+00:00
---

# <action>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/action-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <action> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <action android:name="_string_ " />

contained in:
    `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)`

description:
    Adds an action to an intent filter. An `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)` element must contain one or more `<action>` elements. If there are no `<action>` elements in an intent filter, the filter doesn't accept any `[Intent](https://developer.android.com/reference/android/content/Intent)` objects. For details about intent filters and the role of action specifications within a filter, see [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters). 
attributes:
    

`android:name`
    The name of the action. Some standard actions are defined in the `[Intent](https://developer.android.com/reference/android/content/Intent#ACTION_CHOOSER)` class as `ACTION__string_` constants. To assign one of these actions to this attribute, prepend `android.intent.action.` to the `_string_` that follows `ACTION_`. For example, for `ACTION_MAIN`, use `android.intent.action.MAIN`, and for `ACTION_WEB_SEARCH`, use `android.intent.action.WEB_SEARCH`. 

For actions you define, it's best to use your app's package name as a prefix to help ensure uniqueness. For example, a `TRANSMOGRIFY` action might be specified as follows: 
    
    
    <action android:name="com.example.project.TRANSMOGRIFY" />

introduced in:
    API Level 1
see also:
    `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
