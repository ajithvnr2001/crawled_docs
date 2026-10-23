---
url: https://developer.android.com/guide/topics/manifest/category-element/
title: <category> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:19.837028+00:00
---

# <category>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/category-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <category> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <category android:name="_string_ " />

contained in:
    `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)`
description:
    Adds a category name to an intent filter. See [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters) for details on intent filters and the role of category specifications within a filter.
attributes:
    

`android:name`
    The name of the category. Standard categories are defined in the `[Intent](https://developer.android.com/reference/android/content/Intent)` class as `CATEGORY__name_` constants. The name assigned here is derived from those constants by prefixing `android.intent.category.` to the `_name_` that follows `CATEGORY_`. For example, the string value for `CATEGORY_LAUNCHER` is `android.intent.category.LAUNCHER`. 

**Note:** To receive implicit intents, you must include the `[CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)` category in the intent filter. The methods `[startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity\(android.content.Intent\))` and `[startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult\(android.content.Intent,%20int\))` treat all intents as if they declared the `[CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)` category. If you don't declare it in your intent filter, no implicit intents can resolve your activity.

For custom categories, use the package name as a prefix so that they are unique. 

introduced in:
    API Level 1
see also:
    `[<action>](https://developer.android.com/guide/topics/manifest/action-element)`   
`[<data>](https://developer.android.com/guide/topics/manifest/data-element)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
